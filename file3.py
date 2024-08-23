# If you want to read from a specific index in a file, such as starting from the
# 10th index, you can use the seek() method to move the file pointer to that position
# before reading. Here’s an example:

# Create or open the file in write and read mode
f = open("fad.txt", 'w+')
f.write("My name is Mohammad Farid")

# Move the file pointer to the beginning of the file
f.seek(0)

# Now move the file pointer to the 10th index
f.seek(10)

# Read the content from the 10th index onwards
content_from_index_10 = f.read()
print("Content from index 10:", content_from_index_10)

# Close the file
f.close()
