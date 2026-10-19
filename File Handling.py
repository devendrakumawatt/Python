# File Handling in Pyhton -

# Open a file - 
p = open(r"C:\Users\Genius\Documents\imp.txt")
print(p.read())        # Read a file
p.close()



# Write a file -
r = open("myfile.txt","w")
r.write("Name - Devendra\n")
r.close()


# Append a file - 
r = open("myfile.txt", "a")
r.write("Age - 24\n")
r.write("This and age line is a appended line.\n")
r.close()

