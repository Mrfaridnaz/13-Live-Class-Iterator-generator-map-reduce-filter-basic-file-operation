li = [1,2,3,4,5]

# Initialization: When a for loop starts, Python first gets an iterator from the iterable.
#                 It does this by calling the iter() function on the iterable object.
b = iter(li)

#Iteration: The loop then repeatedly calls the next() function on the iterator to get the
#           next item in the sequence.
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# End of Iteration: When the next() function raises a StopIteration exception (indicating
#                   that there are no more items to return), the loop terminates.
print(next(b))