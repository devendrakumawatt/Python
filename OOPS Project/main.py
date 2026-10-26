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


    def withdrawMoney(self) :
        accountNo = input("Enter your account number : ")
        pin = int(input("Enter your 4-digit pin : "))
    
        userData = [i for i in Bank.data if i["accountNo."] == accountNo and i["pin"] == pin]
    
        if userData == False :
            print("Sorry! No data found")
    
        else :
            amount = int(input("Enter the amount to withdraw : "))
            if userData[0]['balance'] < amount : 
                print("Sorry! You cannot withdraw more than your balance.")
    
            else :
                userData[0]["balance"] -= amount
                Bank.update()
                print("Money withdrew successfully.")

    def showDetails(self) :
        accountNo = input("Enter your account number : ")
        pin = int(input("Enter your 4-digit pin : "))

        userData = [i for i in Bank.data if i["accountNo."] == accountNo and i["pin"] == pin]

        print("Your Information : \n")
        for i in userData[0] :
            print(f"{i} : {userData[0][i]}")


    def updateDetails(self) :
        accountNo = input("Enter your account number : ")
        pin = int(input("Enter your 4-digit pin : "))

        userData = [i for i in Bank.data if i["accountNo."] == accountNo and i["pin"] == pin]

        if userData == False :
            print("Sorry! No data found.")

        else :
            print("You cannot change your age, account no. , balance.")

            print("Fill details for change or leave empty if no change.")

            newData = {
                "name" : input("Enter your name or leave empty : "),
                "email" : input("Enter your email or leave empty : "),
                "pin" : input("Enter your 4-digit pin or leave empty : "),
            }

            if newData["name"] == "" :
                newData["name"] = userData[0]["name"]

            if newData["email"] == "" :
                newData["email"] = userData[0]["email"]

            if newData["pin"] == "" :
                newData["pin"] = userData[0]["pin"]

            newData["age"] = userData[0]["age"]
            newData["accountNo."] = userData[0]["accountNo."]
            newData["balance"] = userData[0]["balance"]

            if type(newData['pin']) == str :
                newData['pin'] = int(newData['pin'])


            for i in newData :
                if newData[i] == userData[0][i] :
                    continue

                else :
                    userData[0][i] = newData[i]

            Bank.update()
            print("Details updated successfully.")


    def delete(self) :
        accountNo = input("Enter your account number : ")
        pin = int(input("Enter your 4-digit pin : "))
        
        userData = [i for i in Bank.data if i["accountNo."] == accountNo and i["pin"] == pin]

        if userData == False :
            print("Sorry! No data found.")

        else :
            check = input("Are you sure you want to delete your account? (y/n) : ")

            if check == "n" or check == "N" :
                print("Account remains as it is.")

            else :
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                Bank.update()
                print("Account deleted successfully.")


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

if choice == 3 :
    user.withdrawMoney()

if choice == 4 :
    user.showDetails()

if choice == 5 :
    user.updateDetails()

if choice == 6 :
    user.delete()