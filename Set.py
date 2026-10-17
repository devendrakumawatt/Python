# Set in Python -

s = {1,2,3,4,5}
print(s)
print(type(s))

# Hashing -
a = "Dev"
b = hash(a)
print(b)


# Set Methods -
s = {1,2,3,4,5}

s.add(8)        # Add element in set
print(s)   

s.remove(4)     # Remove 4 (Give error if not found)
print(s)

s.discard(2)    # Remove 2 (No error , if not found)
print(s)

s.pop()         # remove random element
print(s)

s.clear()       # Remove all elements
print(s)



# 2 Set Methods -
s1 = {1,2,3,4}
s2 = {3,4,5,6}

# Union - 
u1 = s1.union(s2)
print(u1)
u2 = s1 | s2
print(u2)

# Intersection -
i1 = s1.intersection(s2)
print(i1)
i2 = s1 & s2
print(i2)

# Difference - 
d1 = s1.difference(s2)
print(d1)
d2 = s1 - s2
print(d2)

# Symmetric Difference - 
sd1 = s1.symmetric_difference(s2)
print(sd1)
sd2 = s1 ^ s2
print(sd2)