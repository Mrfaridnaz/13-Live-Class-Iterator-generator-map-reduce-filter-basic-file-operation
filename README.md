# 13-Live-Class-Iterator-generator-map-reduce-filter-basic-file-operation

1.1 
How the for loop works internally:
Initialization: When a for loop starts, Python first gets an iterator from the iterable. 
It does this by calling the iter() function on the iterable object.

Iteration: The loop then repeatedly calls the next() function on the iterator to get the 
next item in the sequence.

End of Iteration: When the next() function raises a StopIteration exception (indicating 
that there are no more items to return), the loop terminates.

1.2
A generator is a special type of function that allows you to iterate over a sequence of values. 
Unlike a typical function that computes all the values and returns them at once, a generator produces 
values one at a time and only when requested. This feature makes generators memory efficient and 
suitable for working with large datasets or streams of data where computing all values at once might 
not be feasible.

Here’s how generators work:

Definition: Generators are defined using functions, but instead of using the return statement, 
they use the yield statement to yield a value and pause the function.

State Preservation: When a generator function yields a value, its state is preserved. The next 
time you request a value from the generator, it resumes execution from where it left off.

Iteration: Generators are iterable, meaning you can use them in a loop or with functions like next() 
to retrieve values one at a time.

