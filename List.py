# List in Python -

list1 = ["Dev", 1, True, 0.2]
print(list1)                 # Print the list
print(list1[0], list1[2])    # Indexing of list
print(list1[1:3])            # Slicing of list
list1[0] = "Devendra"        # Mutability of list
print(list1)



# Traversal of list -
list2 = ["john", 1, 3, 5, False, 0.3]
for i in list2 :         # Direct value Traversal of list
    print(i)

for i in range(len(list2)) :  # Index Traversal of list
    print(list2[i])


# List Methods - 
list3 = [1,2,3,4,5,6,7,8,9]

list3.append(10)  # Add element at last
print(list3)

list3.insert(0,0) # insert value at index
print(list3)

list3.extend([11,11,12]) # add list at last
print(list3)

list3.remove(11)  # remove 1st occurance
print(list3) 

list3.pop()   # remove from last
print(list3)

print(list3.index(5))  # return index of value

print(list3.copy())  # return copy of list

print(list3.count(11))  # return count of a value

list3.sort()   # sort the list
print(list3)

list3.reverse()  # reverse the list
print(list3)

list3.clear()  # clear the list
print(list3)


# Questions / Answer -
# Q1. Print positive and negative elements of an List
list4 = [-1,-2,-4,1,2,3,4] 
pos = []
neg = []
for i in list4 :
    if i > 0 :
        pos.append(i)
    else :
        neg.append(i)

print(f"Positive elements : {pos}")
print(f"Negative elements : {neg}")

# Q2. Mean of List elements
list5 = [1,2,3,4,5,6,7]
sum = 0
for i in list5 :
    sum += i

mean = sum / len(list5)
print(f"Mean of List : {mean}")


# Q3. Find the greatest element and print its index too
list6 = [1,3,5,6,7,8,9]
idx = 0
greatest = list6[0]
for i in list6 :
    if i > greatest : 
        greatest = i
        idx = list6.index(i)

print(f"Greatest element is : {greatest} at index {idx} ")


# Q4. Find the second greatest element
list7 = [1,3,5,6,7,8,9]
max1 = list7[0]
max2 = list7[1]
if max2 > max1 :
    max1, max2 = max2, max1

for i in range(2, len(list7)) :
    if list7[i] > max1 :
        max2 = max1
        max1 = list7[i]
    elif list7[i] > max2 and list7[i] < max1 :
        max2 = list7[i]

print(f"2nd Greatest element is : {max2}")

# Q5. Check if List is sorted or not.
list8 = [1,2,3,4,5]
for i in range(0, len(list8) - 1) :
    if list8[i] > list8[i + 1] :
        print("List is not sorted.")
        break
    
else :
    print("List is sorted.")