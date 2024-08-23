my_list = [1, 2, 3, 4]

# Under the hood, this happens:
iterator = iter(my_list)  # Creates an iterator from the iterable
while True:
    try:
        item = next(iterator)  # Fetches the next item
        print(item)
    except StopIteration:
        break  # Stops iteration when there are no more items
