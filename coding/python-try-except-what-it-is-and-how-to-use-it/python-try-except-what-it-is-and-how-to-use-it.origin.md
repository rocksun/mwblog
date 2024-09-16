# Python Try … Except: What It Is and How to Use It
![Featued image for: Python Try … Except: What It Is and How to Use It](https://cdn.thenewstack.io/media/2024/09/5bb27c44-python-try-except-command.jpg)
The more complicated your code, the more you’ll depend on dealing with [exceptions](https://thenewstack.io/python-how-to-work-with-basic-exception-handling/). If you’ve yet to run across exceptions, they are errors that occur during the execution of a program. With [Python](https://thenewstack.io/python/), exceptions don’t produce informative errors but, rather, will just stop. When your application stops without explanation, you (or your users) could be at a loss.

For Python, there’s a one-two punch to help ease this problem, `try … except`
. `Try`
allows you to test a block of code for errors and `except`
allows for the [handling of errors](https://thenewstack.io/error-handling-from-backends-to-the-frontend/).

Think of it this way:

Python will *try* to execute your code and if an error occurs, *except* deals with it.

The structure of `try … except`
looks like this:

1234 |
try: <try to do something> except Exception: <handle the error> |
Here’s a very simple example of `try … except`
:
1234 |
try: print(x)except: print("An exception has occurred") |
If you run the above, the output will be:
1 |
An exception has occurred |
Why is this? In the above code, `x`
was never defined. To better illustrate that, let’s run only the `print(x)`
line, which will output:
1 |
NameError: name 'x' is not defined |
When we have the `try … except`
block, Python will see that `x`
isn’t defined, then go to the `except`
section and execute the second `print`
line.
It’s also possible to specify the error to watch out for. Let’s stick with what we know (in this case, `NameError`
). Take a look at the following code block:

123456 |
try: print(x)except NameError: print("You've not defined x")except: print("Something other than a NameError went wrong") |
You can probably predict what the output will be:
1 |
You've not defined x |
There are other types of exceptions that can be caught with `try … except`
, such as:
- Exception: Non-system-exiting exceptions and user-defined exceptions.
- ArithmeticError: Various arithmetic errors.
- BufferError: When a buffer-related operation cannot be performed.
- LookupError: When a key or index on a mapping or sequence is invalid.
- AssertionError: When an assert statement fails.
- AttributeError: When an attribute reference or assignment fails.
- EOFError: When a function hits an end-of-file condition without reading any data.
- ImportError: When an import statement has trouble loading a module or when a “from list” has a name that cannot be found.
You’ll find a complete list of Python exceptions in the [official documentation](https://docs.python.org/3/library/exceptions.html).

Remember the example above that had two `except`
statements? You can also use a `finally`
statement that will be executed regardless if a code block raises an error. The `finally`
statement looks like this:

123456 |
try: print(x)except: print("X was not defined")finally: print("Our try … except block is complete") |
You might assume the above block of code will print out the single line:
1 |
X was not defined |
However, the `finally`
statement executes the code regardless, so the output will actually be:
12 |
X was not definedOur try … except block is complete |
The `finally`
statement can be helpful for closing objects and cleaning up valuable resources.
Create a code block that will create a file for writing, write to the file, close the file and then print an error should something go wrong. The code block looks like this:

12345678910 |
try: x = open("newstack.txt") try: x.write("Hello, New Stack!") except: print("An error occurred when writing to the file") finally: x.close()except: print("Something went wrong when opening the file") |
Can you guess what the output for the above will be? If you guessed `Something went wrong when opening the file`
, you are correct. We received this error because the newstack.txt file wasn’t opened with write permissions.
Give the file proper access like this:

12345678910 |
try: x = open("newstack.txt", 'w') try: x.write("Hello, New Stack!") except: print("An error occurred when writing to the file") finally: x.close()except: print("Something went wrong when opening the file") |
When you run the above code, no error will appear in the output. Instead, the line `Hello, New Stack!`
is written to the newstack.txt file. No errors. However, thanks to the `finally`
statement, you know the newstack.txt file was properly closed, so you’re good to go.
You can also raise an exception using the `raise`
keyword. The `raise`
keyword is used to raise exceptions and stop the flow of the program. For example, this can be used to stop a program if a user inputs data outside of the required parameters.

Here’s how the `raise`
keyword works:

1234 |
x = "New Stack"if not type(x) is int: raise TypeError("You can only input integers") |
The output of the above command will include the statement:
1 |
You can only input integers |
Why? Because `New Stack`
is a string and not an integer.
And that, my friends, is the gist of Python’s `try … except`
statement. This will come in very handy to ensure your Python programs are better capable of handling errors that occur either from programming issues or user input.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)