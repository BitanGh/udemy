file = open("example.txt","r")
for line in file:
    print(line.strip()) #.strip() method helps in removing the empty lines 