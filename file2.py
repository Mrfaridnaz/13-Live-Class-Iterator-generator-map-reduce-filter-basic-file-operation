f = open("fad.txt", 'w+')
f.write("My name is Mohammad Farid")

# Get the current position of the file pointer after writing
position = f.tell()
print("Current position after writing:", position)

# Move the file pointer to the beginning of the file
f.seek(0)

# Read the content
content = f.read()
print("Content:", content)

# Get the current position of the file pointer after reading
position_after_reading = f.tell()
print("Current position after reading:", position_after_reading)

# Close the file
f.close()
