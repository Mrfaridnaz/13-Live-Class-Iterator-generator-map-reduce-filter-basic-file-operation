# when you use 'w' mode, it will create and open the file
f = open("fad.txt",'w')
f.write("this is my very first file")
f.close()

# Store this information in file
li = [1,2,3,4,5,6,67,7,8]
f = open("fad.txt",'w')
f.write(str(li))
f.close()

