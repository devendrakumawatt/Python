from pathlib import Path
import os

# read file and folder in the directory
def readFileAndFolder() :
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items) :   #list as idx:item
        print(f"{i+1} : {items}")


# file creation function
def createFile() :
    try :
        readFileAndFolder()
        name = input("Please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs :
                data = input("Enter your file data :- ")
                fs.write(data)
        
            print(f"FILE CREATED SUCCESSFULLY")         
            
        else : 
            print("File with name already exists.")
    except Exception as err :
        print(f"An error occured as {err}")


# file read function
def readFile() :
    try :
        readFileAndFolder()
        name = input("Please tell your file to read :- ")
        p = Path(name)
        if p.exists() and p.is_file() :
            with open(p, 'r') as fs :
                data = fs.read()
                print(data)

            print(f"FILE READ SUCCESSFULLY")

        else:
            print("File not found.")

    except Exception as err :
        print(f"An error occured as {err}")



# file update function
def updateFile() :
    try :
        readFileAndFolder()
        name = input("Please tell your file to update :-")
        p = Path(name)

        if p.exists() and p.is_file() :
            print("Enter 1. : To update file name.")
            print("Enter 2. : To overwrite file data.")
            print("Enter 3. : To append data in the file.")

            res = int(input("Enter your choice of operation :- "))

            if res == 1 :
                name2 = input("Enter your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
                print(f"FILE NAME UPDATED SUCCESSFULLY")

            if res == 2 :
                with open(p, "w") as fs :
                    data = input("Enter data to overwrite file data :- ")
                    fs.write(data)

                print(f"FILE DATA OVERWRITE SUCCESSFULLY")

            if res == 3 :
                with open(p, "a") as fs :
                    data = input("Enter data to append in the file :- ")
                    fs.write(" " + data)

                print(f"FILE DATA APPENDED SUCCESSFULLY")

    except Exception as err :
        print(f"An error occured as {err}")


# file delete function
def deleteFile() :
    readFileAndFolder()

    name = input("Enter your file to delete :- ")
    p = Path(name)

    if p.exists() and p.is_file() :
        os.remove(name)
        print(f"FILE DELETED SUCCESSFULLY")

    else :
        print("File not found.")


# main
print("Enter 1. : To create a file.")
print("Enter 2. : To read a file.")
print("Enter 3. : To update a file.")
print("Enter 4. : To delete a file.")

choice = int(input("Enter your choice of operation : "))

if choice == 1 :
    createFile()

if choice == 2 :
    readFile()

if choice == 3 :
    updateFile()

if choice == 4 :
    deleteFile()