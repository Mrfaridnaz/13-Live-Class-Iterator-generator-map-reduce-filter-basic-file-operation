name = "Mohammad Farid"

# next(name)
# TypeError: 'str' object is not an iterator

name1 = iter(name)  # object is iterable
print(next(name1))
print(next(name1))
print(next(name1))
print(next(name1))
