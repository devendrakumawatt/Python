
import json
import secrets
import string
import hashlib
import hmac
from pathlib import Path


class Bank:
    def __init__(self, database="data/accounts.json"):
        self.database = Path(database)
        self.database.parent.mkdir(parents=True, exist_ok=True)

        if not self.database.exists():
            self.database.write_text("[]", encoding="utf-8")

        try:
            self.data = json.loads(
                self.database.read_text(encoding="utf-8")
            )
            if not isinstance(self.data, list):
                raise ValueError("Database must contain a JSON list.")
        except (json.JSONDecodeError, ValueError) as error:
            raise RuntimeError(
                f"Could not load account database: {error}"
            ) from error

    def _save(self):
        # Atomic replacement helps prevent partially written JSON.
        temporary = self.database.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(self.data, indent=4),
            encoding="utf-8",
        )
        temporary.replace(self.database)

    @staticmethod
    def _hash_pin(pin, salt=None):
        salt = salt or secrets.token_hex(16)
        hashed = hashlib.pbkdf2_hmac(
            "sha256",
            pin.encode("utf-8"),
            bytes.fromhex(salt),
            200_000,
        ).hex()
        return salt, hashed

    @staticmethod
    def _validate_pin(pin):
        if not pin.isdigit() or len(pin) != 4:
            raise ValueError("PIN must contain exactly 4 digits.")

    def _find_account(self, account_no):
        return next(
            (
                account
                for account in self.data
                if account["account_no"] == account_no
            ),
            None,
        )

    def authenticate(self, account_no, pin):
        if not pin.isdigit() or len(pin) != 4:
            return False

        account = self._find_account(account_no)
        if not account:
            return False

        _, candidate = self._hash_pin(
            pin, account["pin_salt"]
        )
        return hmac.compare_digest(
            candidate, account["pin_hash"]
        )

    def create_account(self, name, age, email, pin):
        name = name.strip()
        email = email.strip()

        if not name:
            raise ValueError("Name is required.")
        if age < 18:
            raise ValueError("You must be at least 18.")
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Enter a valid email address.")

        self._validate_pin(pin)

        account_no = "".join(
            secrets.choice(string.digits) for _ in range(10)
        )
        while self._find_account(account_no):
            account_no = "".join(
                secrets.choice(string.digits) for _ in range(10)
            )

        salt, pin_hash = self._hash_pin(pin)

        account = {
            "account_no": account_no,
            "name": name,
            "age": age,
            "email": email,
            "pin_salt": salt,
            "pin_hash": pin_hash,
            "balance": 0.0,
        }

        self.data.append(account)
        try:
            self._save()
        except OSError:
            self.data.remove(account)
            raise

        return account_no

    def get_account(self, account_no):
        account = self._find_account(account_no)
        if not account:
            return None

        # Never return authentication secrets to the UI.
        return {
            key: value
            for key, value in account.items()
            if key not in ("pin_salt", "pin_hash")
        }

    def deposit(self, account_no, amount):
        if amount <= 0 or amount > 10000:
            raise ValueError(
                "Deposit must be greater than 0 and at most 10,000."
            )

        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")

        old_balance = account["balance"]
        account["balance"] += amount
        try:
            self._save()
        except OSError:
            account["balance"] = old_balance
            raise

    def withdraw(self, account_no, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")

        if amount > account["balance"]:
            raise ValueError("Insufficient balance.")

        old_balance = account["balance"]
        account["balance"] -= amount
        try:
            self._save()
        except OSError:
            account["balance"] = old_balance
            raise

    def update_account(
        self, account_no, name=None, email=None, pin=None
    ):
        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")

        changes = {}

        if name is not None:
            name = name.strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            changes["name"] = name

        if email is not None:
            email = email.strip()
            if "@" not in email or "." not in email.split("@")[-1]:
                raise ValueError("Enter a valid email address.")
            changes["email"] = email

        if pin is not None:
            self._validate_pin(pin)
            salt, pin_hash = self._hash_pin(pin)
            changes["pin_salt"] = salt
            changes["pin_hash"] = pin_hash

        old_values = {key: account[key] for key in changes}
        account.update(changes)

        try:
            self._save()
        except OSError:
            account.update(old_values)
            raise

    def delete_account(self, account_no):
        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")

        index = self.data.index(account)
        self.data.pop(index)
        try:
            self._save()
        except OSError:
            self.data.insert(index, account)
            raise
