# Tuple in python - 

t = ("dev", 1, True, 0.3)
print(t)


# Tuple Slicing -
t = ("dev", 1, True, 0.3)
print(t[0:2])

# traversal of tuple -

t = ("dev", 1, True, 0.3)
for i in t :      # Direct value Traversal
    print(i)

for i in range(len(t)) :  # Index Traversal
    print(t[i])


# Tuple Methods -
t = (1,2,2,2,2,3,3,3)
print(t.count(2))
print(t.index(3))


# tuple unpacking
a,b,c = (1,2,3)
print(a)     # 1
print(b)     # 2
print(c)    # 3


# tuple type
a = (1)
print(type(a))        # type - int
a = (1,)
print(type(a))         #type - tuple