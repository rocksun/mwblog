# Tips and Tricks for Clean, Readable Python Code
![Featued image for: Tips and Tricks for Clean, Readable Python Code](https://cdn.thenewstack.io/media/2024/11/1f937e51-pablo-merchan-montes-ckosbupolsq-unsplash-1024x683.jpg)
Learning to code comes is a steep climb. One side of the learning covers learning how to code and the other side includes how to do that elegantly. For me, that was the hardest part. I could brute force and clunkily solve many things but when it came to writing an elegant solution, no thank you, I’ll take the
[nested loops](https://thenewstack.io/how-to-use-loops-in-python/) every single time. But of course, that doesn’t work for a few reasons since code should be DRY (Don’t Repeat Yourself), memory-friendly, and readable by other people. But [Python](https://thenewstack.io/python/)’s built-in helpers that aid in code readability and ease.
## *args and **kwargs
*args and **kwargs help make functions widely useable. Using *args as a functions parameter allows the function to take any arbitrary number of arguments. Without *args, integer and string arguments would have to be accounted for.
With *args:
And without it just throws an error…
**kwargs carries similar functionality as *args but does so for key value pairs. **kwargs can be used in a function that doesn’t have a required number or has an unknown number of
[key value pairs](https://thenewstack.io/akamai-brings-key-value-data-to-the-edge-adds-api-acceleration/).
## List Comprehension
List comprehensions allow developers to create lists using only a single line. Without using a list comprehension, you could build a numbers list using the following code:
A list comprehension turns that code into a single line. The basic syntax is:
[expression for item in iterable] and in simple code, it looks like this:
List comprehensions can also include filtering functionality.
Lists aren’t the only data structure you can create in this way. We can create a dictionary and set it using the same creation pattern. The dictionary’s basic syntax is:
{key_expression: value_expression for item in iterable}.
We can multiply each number in our numbers list by 10 to a by_tens dictionary.
We can also do this with a set. The basic syntax is
{expression for item in iterable}. The code looks like this:
## zip()
zip() allows you to iterate over multiple lists simultaneously and create tuples of corresponding elements.
zip() shortens what could have been a multi-line iteration into a single line of code.
zip() iterates over the length of the smallest list. If the given lists are of different lengths, the tuples will only be as long as the smallest list. The code below provides a clear illustration of both above points:
## Merging Dictionaries
You can merge dictionaries using the
update() functionality or the dictionary unpacking syntax (
**).
or you could use the update function to add the
water_pets object to the
land_pets object:
land_pets.update(water_pets).
## Chaining Comparison Operators
Chaining comparison operators allows you to combine multiple comparisons into a single expression. Chaining removes the need for the explicit and` operator. It helps code readability and performance because it reduces the number of separate comparisons.
The example below compares the variable
miles to determine if the distance is in range. The code looks like this without chaining comparison operators:
When the comparison is expressed as a compound condition, it looks like this:
## Ternary Operator
Ternary operators allow developers to write if conditionals in a single line. The basic syntax is:
result = true_value if condition else false_value
If the condition evaluates to
True the expression returns the true value. If the condition evaluates to
False, the expression returns the false value. Here’s an example without the turnery operator:
Versus the if conditional with the ternary operator:
## Decorators
Decorators modify functions without changing the source code. A decorator is a new function that takes the original function as an argument, uses a new function to modify it, and then returns the function with updated functionality.
Let’s start with a basic division function.
division(10,5) prints 2
division(9, 3) prints 3
For purposes of this example, let’s pretend this function always needs to have the larger number divided by the smaller number. There are many reasons why it would be unideal to edit the source code and, in those instances, a decorator comes in handy. If you’re familiar with closures, this will look familiar. For those unfamiliar, the decorator is a function that builds, modifies, and returns a function. The shell of the decorator will look like this:
Inside the inner function is where we’ll check to see if the arguments are in the correct order and make the necessary swaps (another Python trick) if not.
The inner function looks and behaves like any basic function does.
Now there are a few different ways we can use the decorator function to modify the division function. The first way to do this is to use
@decorator and it looks like this:
Another way to do this is to assign the function as a variable:
## Happy Coding!
Those tips are sure to elevate code from basic to elegant. The more you work with Python, the easier it gets.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)