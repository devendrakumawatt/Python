# While Loop in python -

i = 1
while i <= 5 :
    print("Hello World!")
    i += 1


# Questions / Answer (While Loop) -

# Q1. Separate each digit of a number and print it on the new line
num = int(input("Enter a Multi Digit Number : "))
while num > 0 :
    rem = num % 10
    print(rem)
    num = num // 10

# Q2. Accept a number and print its reverse
num = int(input("Enter a number : "))
rev = 0
while num > 0 :
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print(f"Reverse of num : {rev}")

# Q3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
num = int(input("Enter a number : "))
rev = 0
palNum = num
while num > 0 :
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if palNum == rev :
    print(f"{palNum} is a pallindromic number.")
else :
    print(f"{palNum} is not a pallindromic number.")

# GAME :  Create a random number guessing game with python
import random
num = random.randint(1,10)
guess = int(input("Guess the number (1 to 10) : "))
count = 1
if num == guess :
    print("Congratulations! You guessed the number in 1st attempt.")
while num != guess :
    if num > guess :
        print("Hint :- Your number is smaller")
    else :
        print("Hint :- Your number is greater")
    count += 1
    guess = int(input("Guess the number (1 to 10) : "))
print(f"Congratulations! You guessed the number in {count} attempts.")
