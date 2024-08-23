x = 23
next(x)
#when we try to iterate any object, it will give the error and mention that
#    first make it iterator by using iter() function, you need to make it iterable first.
#    'int' object is not an iterator

# you need to apply iter() to any object before using next()
# may be the number is iterable or not

iter(23)
# 'int' object is not iterable, it is not able to conveted into iterable