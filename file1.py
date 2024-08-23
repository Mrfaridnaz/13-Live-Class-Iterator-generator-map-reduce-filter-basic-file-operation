# Perform read operation
f = open("fad.txt",'w+')
f.write("My name is Mohammad Farid")
print(f.read())

# you will not get any content
# The issue is that you're trying to read from the file immediately after writing to it
# without resetting the file pointer to the beginning. When you open a file with 'w+' mode,
# the file pointer is at the start for writing, but after writing, the pointer is at the end of
# the file. To read what you've written, you need to reset the pointer back to the beginning of
# the file.

# ===================================================
f = open("fad.txt", 'w+')
f.write("My name is Mohammad Farid")

# Move the file pointer to the beginning of the file
f.seek(0)
# Now read the content
print(f.read())
# Don't forget to close the file
f.close()

# ==================================================
f = open("fad.txt", 'w+')
f.write("My name is Mohammad Farid")

f.seek(4) # pointer start reading from 4
print(f.read())
f.close()

# ==================================================
