# What Are Python Lambda Functions and How Do You Use Them?
![Featued image for: What Are Python Lambda Functions and How Do You Use Them?](https://cdn.thenewstack.io/media/2024/03/2067792a-gabriel-alenius-ijsv5be3p3m-unsplash-1-1024x576.jpg)
Although
[Python](https://thenewstack.io/what-is-python/) is generally a very easy-to-learn and easily comprehended language, it doesn’t mean there aren’t concepts that can tend to be a bit more challenging. One such concept is the [Lambda function](https://thenewstack.io/tips-for-writing-lambda-functions-in-node-8/). These [functions](https://thenewstack.io/so-much-more-python-for-beginners-functions/) (also called [anonymous functions](https://en.wikipedia.org/wiki/Anonymous_function)) are similar to those functions you build yourself but do not have a name.
But what are these functions for? Simply put, you use Lambda functions when you want to write a function that only contains simple expressions. You might have an expression you need to use that doesn’t need a full-blown function to perform properly or will only be used once in your code/application. That’s when Lambda functions come into play.
Lambda functions consist of only three parts: the keyword (which is lambda), a placeholder to hold the value to be passed to the expression, and the expression.
The format of a Lambda function looks like this:
*lambda arguments : expression*
In the example above,
*arguments* is the value placeholder.
To illustrate how handy a Lambda function can be, consider that we want to write a function that will add 20 to the variable
*a* and print the results. That function might look like this:
|
1
|
x = lambda a : a + 20
Let me explain. What we’re doing is defining the variable
*x *with the Lambda *a* function that adds 20 to the a variable. Of course, we have to define *a*, which we can do within the *print()* function like so:
|
1
|
print(x10))
The entire code looks like this:
|
1
2
|
x = lambda a : a + 20
print(x10))
If you were to run the above code, the result would be 30. Why? Because we’ve defined our Lambda function such that it adds the value 20 to
*a* and then we define *a* as 10. *20+10=30*
We can also create a Lambda function that includes two variables (let’s say
*x* and *y*) and multiply them together. That Lambda function would look like this:
|
1
|
a = lambda x, y : x * y
What we did above was define
*a *with our new Lambda function that then multiplies *x * y*. We can then define *x* and *y* in our print function like so:
|
1
|
print(a(10, 50))
The entire code looks like this:
|
1
2
|
a = lambda x, y : x * y
print(a(10, 50))
Run the above code and the result would be 500.
10 * 50 = 500
Neat.
Let’s take this one step further. Let’s add multiple variables together in a Lambda function. That might look like this:
|
1
2
|
x = lambda a, b, c : a + b * c
print(x(10, 20, 30))
The result of the above is 610.
But how do we effectively use Lambda functions within our code? Why don’t we define a function with a Lambda function and then call that function later in the code? To do this, we’re going to use the return statement, which is used to end the execution of a function call and return the results.
Let’s first define a Lambda function that multiplies
*a* times *x* that looks like this:
|
1
2
|
def myfunc(x):
return lambda a : a * x
Next, we’re going to triple the value from myfunc(x) with the line:
|
1
|
tripler = myfunc(3)
What we’ve done above is called myfunc and defined
*x* as 3 for the Lambda function.
Our next line looks like this:
|
1
|
print(tripler(10))
What we’ve done here is define
*a* (from our Lambda function) as 10, so we effectively have 10 times 3. The result (as expected) will be 30.
Let’s compare the Lambda function to a standard function (so you can see how effective it can be). Consider this:
|
1
2
3
4
|
def a(x):
return x * 10
print(a(3))
If we run the above, it will print out 30.
But how would that work as a Lambda function? Like so:
|
1
2
|
a = lambda x : x * 10
print(a(3))
The above code would print out the same results, but we’ve only had to use 2 lines of code.
Of course, if we wanted to create a function that would be used over and over within our code, we wouldn’t opt for a Lambda function. But for those functions that will only be used once, Lambda is the way to go. Why is this the case? Because our Lambda functions don’t have names and, without a name, they can’t be called later on.
## Using Lambda Functions with Lists
You can also use Lambda functions with lists. This is accomplished using the
*filter()* function, which uses a function and a list of arguments and makes it easy to filter out objects from the sequence that the function returns as true. Let’s say you want to return only the odd numbers from a list. We can do that with the Lambda function:
|
1
|
x : (x % 2 !=0)
What does that do? Simple. With the % operator it returns the remainder when the first operand is divided by the second and then != means does not equal. That function will return False if
*x* is not even.
Our list will be:
|
1
|
lista = [1, 3, 6, 9, 11, 16, 21, 24, 30, 31]
We then define odd_out with our Lambda function like this:
|
1
|
odd_out = list(filter(lambda x : (x % 2 != 0), lista))
We can then print the results with:
|
1
|
print(odd_out)
The entire code looks like this:
|
1
2
3
4
5
|
lista = [1, 3, 6, 9, 11, 16, 21, 24, 30, 31]
odd_out = list(filter(lambda x : (x % 2 != 0), lista))
print(odd_out)
If we run the above code, we get the following output:
*[1, 3, 9, 11, 21, 31]*
Only the odd numbers are printed.
And that, my friends, is your introduction to Lambda functions in Python. These little ditties can come in very handy and even keep your code a bit cleaner.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)