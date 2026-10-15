# Contional Statements in Python -

# If Statement - 
a = 23
b = 10
if a > b :
    print(f"{a} is greater than {b}")


# If-Else Statement -
a = 23
b = 100
if a > b :
    print(f"{a} is greater than {b}")
else :
    print(f"{b} is greater than {a}")


# If-Elif-Else statement -
a = 20
b = 20
if a > b :
    print(f"{a} is greater than {b}")
elif b > a :
    print(f"{b} is greater than {a}")
else :
    print(f"{a} is equal to {b}")



# Question / Answers -
# Q1. Accept two numbers and print the greatest between them.
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if num1 > num2 :
    print(f"{num1} is greater than {num2}")
else :
    print(f"{num2} is greater than {num1}")


# Q2. Accept the gender from the user as char and print the respective greeting message.
gender = input("Enter your gender : ")
if gender == "male" :
    print("Good Morning Sir!")
elif gender == "female" :
    print("Good Morning Ma'am!")
else :
    print("Good Morning!")


# Q3. Accept an integer and check whether it is an even number or odd.
num = int(input("Enter a number : "))
if num % 2 == 0 :
    print(f"{num} is an even no.")
else :
    print(f"{num} is an odd no.")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
if age >=18 :
    print(f"Hello, {name} you are a valid voter.")
else :
    print(f"Hello, {name} you are not a valid voter.")

# Q5. Accept a year and check if it a leap year or not.
year = int(input("Enter a year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0) :
    print(f"{year} is a leap year.")
else : 
    print(f"{year} is not a leap year.") 


# Q6. Take the input of temperature in celsius 
# Below 0°C → "Freezing Cold"
# 0°C to 10°C → "Very Cold"
# 10°C to 20°C → "Cold"
# 20°C to 30°C → "Pleasant"
# 30°C to 40°C → "Hot"
# Above 40°C → "Very Hot" 

temp = float(input("Enter the temperature (in celsius) : "))
if temp < 0 :
    print("Freezing Cold")
elif temp >= 0 and temp < 10 :
    print("Very Cold")
elif temp >= 10 and temp < 20 :
    print("Cold")
elif temp >=20 and temp < 30 :
    print("Pleasant")
elif temp >= 30 and temp < 40 :
    print("Hot")
else :
    print("Very Hot")