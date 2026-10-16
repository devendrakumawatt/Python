# For Loop in python -

for i in range(1,6) :         # For loop for numbers
    print(i)

str = "Devendra"
for i in range(len(str)) :     # For loop for strings
    print(str[i])

str2 = "Nature"
for chr in str2 :             # For loop for strings
    print(chr)


# Questions / Answer (For Loop) -
# Q1. Accept an integer and Print hello world n times
num = int(input("Enter a number : "))
for i in range(num) : 
    print("Hello World")

# Q2. Print natural number upto n
nat = int(input("Enter a number : "))
for i in range(1 , nat+1) : 
    print(i)

# Q3. Reverse for loop. Print n to 1
rev = int(input("Enter a number : "))
for i in range(rev, 0, -1) :
    print(i)

# Q4. Take a number as input and print its table
tab = int(input("Enter a number : "))
for i in range(1, 11) :
    print(f"{tab} x {i} = {tab*i}")

# Q5. Sum up to n terms
sum = 0
nm = int(input("Enter a number : "))
for i in range(1, nm + 1) :
    sum += i
print(sum)

# Q6. Factorial of a number
num = int(input("Enter a number : "))
fact = 1
for i in range(1, num + 1) : 
    fact *= i
print(fact)

# Q7. Print the sum of all even & odd numbers in a range separately
evenSum = 0
oddSum = 0
for i in range(1,21) :
    if i % 2 == 0 :
        evenSum += i
    else :
        oddSum += i
print(f"Even Sum : {evenSum}")
print(f"Odd Sum : {oddSum}")

# Q8. Print all the factors of a number
num = int(input("Enter a number : "))
for i in range(1, num + 1) :
    if num % i == 0 :
        print(i)

# Q9. Accept a number and check if it a perfect number or not. 
perfNum = int(input("Enter a number : "))
sum = 0
for i in range(1, (perfNum // 2) + 1) :
    if(perfNum % i == 0) :
        sum += i
if sum == perfNum :
    print(f"{perfNum} is a perfect number.")
else :
    print(f"{perfNum} is not a perfect number.")


# 10. Check wether the number is prime or not
primeNum = int(input("Enter a number : "))
if primeNum == 2 : 
    print(f"{primeNum} is a prime number")
for i in range(2, primeNum) : 
    if primeNum % i == 0 :
        print(f"{primeNum} is not a prime number.")
        break
    else :
        print(f"{primeNum} is a prime number.")
        break

# Q11. Reverse a string without using in build functions.
str = input("Enter a string : ")
rev = ""
for i in range(len(str) - 1, -1, -1) :
    rev += str[i]
print(rev)

# Q12. Check string is Pallindrome or not
str = input("Enter a string : ")
isPallindrome = True
for i in range(0, len(str)) :
    if str[i] != str[len(str) - 1 - i] :
        isPallindrome = False
        break
if isPallindrome == True :
    print(f"{str} is a pallindrome")
else :
    print(f"{str} is not a pallindrome")
        

# Q13. Count all letters, digits, and special symbols from a given string 
str = input("Enter a string : ")
digits = 0
letters = 0
symbols = 0
for i in range(len(str)) :
    if str[i].isalpha() :
        letters += 1
    elif str[i].isdigit() :
        digits += 1
    else :
        symbols += 1
print(f"Digits : {digits}")
print(f"Letters : {letters}")
print(f"Symbols : {symbols}")