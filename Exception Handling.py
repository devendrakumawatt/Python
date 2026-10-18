# Exception Handling - 

# print("Start")
# print(10/0)         # ZeroDivisionError
# print("End")        # This line will not execute


# try - except block -
print("Shuru")
try :
    print(10/0)

except ZeroDivisionError as err : 
    print("Error - ", err)

print("Divide hogya!")


# try - except - else block - 
print("Shuru")
try :
    print(10/1)

except ZeroDivisionError as err : 
    print("Error - ", err)

else :
    print("Koi error nhi aaya!")

print("Divide hogya!")


# try - except - else - finally block - 
print("Shuru")
try :
    print(10/1)

except ZeroDivisionError as err : 
    print("Error - ", err)

else :
    print("Koi error nhi aaya!")

finally :
    print("Mai toh hamesha chalta hu")

print("Divide hogya!")


# Raise - Manually raising error 

age = 20

if age < 18 : 
    raise Exception("You are not eligible to vote")
else :
    print("You are eligible to vote")

print("End")


# 

print ("Shuru")

try : 
    age = 2
    if age < 18 : 
        raise Exception("You are not eligible to vote")
    else :
        print("You are eligible to vote")
except Exception as err : 
    print ("Error - ",err)

print("End")