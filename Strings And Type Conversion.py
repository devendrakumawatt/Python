# Strings And Type Conversion -

str1 = "Devendra"
print(type(str1))  #type of str1
print(ord("D"))    #ASCII / Unicode of 'D'
print(chr(65))    #Character value of unicode 65


# string indexing -
name = "Devendra"
print(name[0])
print(name[-1])

# string Slicing -
user = "Devendra"
print(user[0:4])
print(user[1:4:1])

# Type Conversion -
a = 23
print(type(a))
a = str(a)
print(type(a))

b = "abc"
# b = int(b)
# print(type(b))

c = 0
d = "2"
print(bool(c))
print(bool(d))

