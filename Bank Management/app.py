import streamlit as st
from bank import Bank

st.set_page_config(
    page_title="SecureBank | Banking App",
    page_icon="🏦",
    layout="wide",
)

st.title("🏦 SecureBank")
st.caption("A Python OOP banking project powered by Streamlit")

@st.cache_resource
def get_bank():
    return Bank("data/accounts.json")

try:
    bank = get_bank()
except (RuntimeError, OSError) as error:
    st.error(str(error))
    st.stop()

if "account_no" not in st.session_state:
    st.session_state.account_no = None

def logout():
    st.session_state.account_no = None
    st.rerun()

def show_error(error):
    st.error(str(error))

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Create Account",
        "Login",
        "Dashboard",
        "Deposit",
        "Withdraw",
        "Update Details",
        "Delete Account",
    ],
)

if page == "Home":
    st.subheader("Welcome to your banking application")
    st.write(
        "Manage a demo account, deposit money, withdraw funds, "
        "and update your profile."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Account management", "Available")
    col2.metric("Deposit & withdrawal", "Available")
    col3.metric("Storage", "JSON")

    st.info(
        "This is an educational demo, not a production banking system."
    )

elif page == "Create Account":
    st.subheader("Create a new account")

    with st.form("create_account_form"):
        name = st.text_input("Full name")
        age = st.number_input(
            "Age", min_value=1, max_value=120, value=18
        )
        email = st.text_input("Email address")
        pin = st.text_input(
            "Choose a 4-digit PIN",
            type="password",
            max_chars=4,
        )
        submitted = st.form_submit_button(
            "Create account", type="primary"
        )

    if submitted:
        try:
            account_no = bank.create_account(
                name, int(age), email, pin
            )
            st.success("Account created successfully!")
            st.code(account_no, language=None)
            st.warning(
                "Save your account number. It is needed to log in."
            )
        except (ValueError, OSError) as error:
            show_error(error)

elif page == "Login":
    st.subheader("Login to your account")

    with st.form("login_form"):
        account_no = st.text_input("Account number")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button(
            "Login", type="primary"
        )

    if submitted:
        if bank.authenticate(account_no.strip(), pin):
            st.session_state.account_no = account_no.strip()
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid account number or PIN.")

elif page == "Dashboard":
    account_no = st.session_state.account_no

    if not account_no:
        st.warning("Please log in first from the Login page.")
    else:
        account = bank.get_account(account_no)

        if not account:
            st.session_state.account_no = None
            st.error("Account not found. Please log in again.")
        else:
            st.subheader(f"Welcome, {account['name']}!")
            left, middle, right = st.columns(3)
            left.metric("Account number", account["account_no"])
            middle.metric("Current balance", f"₹{account['balance']:,.2f}")
            right.metric("Account age", f"{account['age']} years")

            st.write(f"**Email:** {account['email']}")
            st.button("Logout", on_click=logout)

elif page in ("Deposit", "Withdraw"):
    account_no = st.session_state.account_no

    if not account_no:
        st.warning("Please log in first.")
    else:
        action = "Deposit" if page == "Deposit" else "Withdraw"
        st.subheader(f"{action} money")

        with st.form(f"{action.lower()}_form"):
            amount = st.number_input(
                "Amount (₹)",
                min_value=0.0,
                value=100.0,
                step=100.0,
            )
            submitted = st.form_submit_button(
                action, type="primary"
            )

        if submitted:
            try:
                if action == "Deposit":
                    bank.deposit(account_no, amount)
                else:
                    bank.withdraw(account_no, amount)

                st.success(f"{action} successful!")
                st.rerun()
            except (ValueError, OSError) as error:
                show_error(error)

elif page == "Update Details":
    account_no = st.session_state.account_no

    if not account_no:
        st.warning("Please log in first.")
    else:
        account = bank.get_account(account_no)

        if not account:
            st.error("Account not found.")
        else:
            st.subheader("Update your profile")

            with st.form("update_form"):
                name = st.text_input(
                    "Name", value=account["name"]
                )
                email = st.text_input(
                    "Email", value=account["email"]
                )
                pin = st.text_input(
                    "New PIN (leave blank to keep current PIN)",
                    type="password",
                    max_chars=4,
                )
                submitted = st.form_submit_button(
                    "Save changes", type="primary"
                )

            if submitted:
                try:
                    bank.update_account(
                        account_no,
                        name=name,
                        email=email,
                        pin=pin or None,
                    )
                    st.success("Details updated successfully.")
                    st.rerun()
                except (ValueError, OSError) as error:
                    show_error(error)

elif page == "Delete Account":
    account_no = st.session_state.account_no

    if not account_no:
        st.warning("Please log in first.")
    else:
        st.subheader("Delete account")
        st.warning(
            "This permanently deletes the account from the demo database."
        )

        with st.form("delete_form"):
            pin = st.text_input(
                "Confirm your PIN", type="password", max_chars=4
            )
            confirm = st.checkbox(
                "I understand that this action cannot be undone."
            )
            submitted = st.form_submit_button(
                "Delete my account", type="primary"
            )

        if submitted:
            if not confirm:
                st.error("Please confirm account deletion.")
            elif not bank.authenticate(account_no, pin):
                st.error("Incorrect PIN.")
            else:
                try:
                    bank.delete_account(account_no)
                    st.session_state.account_no = None
                    st.success("Account deleted successfully.")
                    st.rerun()
                except (ValueError, OSError) as error:
                    show_error(error)
