#file = open("example.txt","r")
#for line in file:
    #print(line.strip()) #.strip() method helps in removing the empty lines 
    
#file = open("example.txt","w")
#file.write("This is a new line")
#print("new line added")

###File Handling without overwriting

#file = open("example.txt","a")
#file.write("This is a new line part-2\n")
#print("new line added")

file = open("example.txt","w")
lines = ["First line \n", "Second Line\n", "Third Line\n"]

file.writelines(lines)
print("new line added")