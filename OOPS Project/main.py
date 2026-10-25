import json
import random
import string
from pathlib import Path

class Bank :
    database = "OOPS Project/data.json"
    data = []

    try:
        if Path(database).exists() :
            with open(database, 'r') as fs :
                data = json.loads(fs.read())   #load json file data 

        else :
            print("No such file exists.")

    except Exception as err :
        print(f"An error occured as {err}")


    @staticmethod
    def update() :
        with open(Bank.database, "w") as fs :
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountGenerate(cls) :
        alpha = random.choices(string.ascii_letters, k =3)
        num = random.choices(string.digits, k = 3)
        spChar = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spChar
        random.shuffle(id)
        return "".join(id)


    def createAccount(self) :
        info = {
            "name" : input("Enter your name : "),
            "age" : int(input("Enter your age : ")),
            "email" : input("Enter your email : "),
            "pin" : int(input("Enter your 4-digit pin : ")),
            "accountNo." : Bank.__accountGenerate(),
            "balance" : 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry! You cannot create an account.")

        else :
            print("Account created successfully.")
            for i in info :
                print(f"{i} : {info[i]}")

            print("Please store your account number and pin safely.")

            Bank.data.append(info)
            Bank.update()


    def depositeMoney(self) :
        accountNo = input("Enter your account number : ")
        pin = int(input("Enter your 4-digit pin : "))

        userData = [i for i in Bank.data if i["accountNo."] == accountNo and i["pin"] == pin]

        if userData == False :
            print("Sorry! No data found")

        else :
            amount = int(input("Enter the amount to deposite : "))
            if amount > 10000 or amount < 0 : 
                print("Sorry! You cannot deposite more than 10000.")

            else :
                userData[0]["balance"] += amount
                Bank.update()
                print("Money deposite successfully.")


user = Bank()



print("Enter 1 : For creating an account.")
print("Enter 2 : For deposititing the money.")
print("Enter 3 : For withdrawing the money.")
print("Enter 4 : For details.")
print("Enter 5 : For updating the details.")
print("Enter 6 : For deleting the account.")


choice = int(input("Enter your choice : "))

if choice == 1 :
    user.createAccount()

if choice == 2 :
    user.depositeMoney()