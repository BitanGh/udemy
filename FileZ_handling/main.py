#file = open("example.txt","r")
#for line in file:
    #print(line.strip()) #.strip() method helps in removing the empty lines 
    
file = open("example.txt","w")
file.write("This is a new line")
print("new line added")