# Dictionary in Python -

dict = {"name" : "Devendra", "age" : 24, "isLoggedIn" : True}
print(dict)
print(dict["name"])


# Dictionary Methods -
dict = {"name" : "Devendra", "age" : 24, "isLoggedIn" : True}
print(dict.keys())
print(dict.values())
print(dict.items())


# Dictionary Traversal -

d = {1:100,2:200,3:300,4:400}
for i in d :                  # Both Traversal
    print(i, ":", d[i])       

d1 = {1:100,2:200,3:300,4:400}
for i in d1.keys() :          # Key traversal
    print(i)

d2 = {1:100,2:200,3:300,4:400}
for i in d2.values() :      #value traversal
    print(i)


# Dictionary C R U D -
dst = {1:100,2:200,3:300,4:400}
print(dst)

dst[5] = 500        #C - Create
print(dst)

print(dst[2])       #R - Read

dst[3] = 3000       #U - Update
print(dst)

del dst[4]          #D - Delete
print(dst)


# Question / Answer -
# Q1. Write a Python script to merge two Python dictionaries
dist1 = {1:100, 2:200, 3:300, 4:400}
dist2 = {5:500, 6:600, 7:700, 8:800}

for i in dist2 : 
    dist1[i] = dist2[i]

print(dist1)

# Q2. Write a Python program to sum all the values in a dictionary
dist1 = {1:100, 2:200, 3:300, 4:400, 5:500}
sum = 0
for i in dist1 :
    sum += dist1[i]

print(sum)

# Q3. Count the frequency of each element in a list
lst = [1,1,1,1,2,2,2,3,3,3,3,4,4,5,6,7,7,8,9]
dist = {}
for i in lst :
    if i in dist:
        dist[i] += 1 
    else :
        dist[i] = 1

print(dist)


# Q4. Write a Python program to combine two dictionary by adding values for common keys
dist1 = {1:100, 2:200, 3:300, 4:400}
dist2 = {2:500, 4:600, 5:500, 6:600}

for i in dist2 :
    if i in dist1 : 
        dist1[i] += dist2[i]
    else :
        dist1[i] = dist2[i]

print(dist1)