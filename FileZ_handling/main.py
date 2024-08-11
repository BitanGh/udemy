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

#file = open("example.txt","w")
#lines = ["First line \n", "Second Line\n", "Third Line\n"]

#file.writelines(lines)
#print("new line added")

###  Reading information from a source_file and writing the same info. in some other file say Destination.txt

source_file = open('example.txt',"r")
print(source_file.read())
content = source_file.read()

destination_file = open('destination.txt',"w")
destination_file.write(content)
print("Succesfully Done")