# unittest: Python’s Built-In Safety Net for Developers
![Featued image for: unittest: Python’s Built-In Safety Net for Developers](https://cdn.thenewstack.io/media/2025/02/97b6f181-levi-meir-clancy-9fpm0ruywww-unsplash-1-1024x683.jpg)
Testing isn’t typically the favorite part of coding for most developers, but it is 100% necessary. An instructor from my [coding bootcamp](https://thenewstack.io/?p=2176624) once referred to testing as the “vegetables of coding” and that’s really what it is. Thorough testing fosters confidence in the quality and stability of software by [catching bugs](https://thenewstack.io/meet-early-the-ai-that-catches-bugs-before-they-bite/) during development, when you want to catch them. It reduces the risk of improper software behavior in production, which in turn improves application performance, improves security and minimizes downtime.

Well-tested code benefits your fellow engineers too, as it’s reliable, maintainable and easier to refactor. Tests serve as a safety net, ensuring that existing features continue to work after changes are made. Additionally, automated tests enable faster iteration, enhance collaboration and provide clear documentation on how the code is intended to behave.

There are many options when it comes to choosing a testing framework. This tutorial will focus on simple tests using Python’s built-in package, [unittest](https://docs.python.org/3/library/unittest.html). This tutorial is focused on developers new to coding who don’t have experience with unit testing. `unittest`
is an excellent option for developers who prefer a built-in approach. Python’s `unittest`
module excels in handling basic unit tests that verify the correctness of individual functions or methods in isolation. It’s also a great starting point for building your own tests and getting familiar with how they work.

## Getting Started With Python’s `unittest`
` unittest.TestCase`
is a class in Python’s `unittest`
module that provides the framework for writing and running tests. It’s the base class for creating tests, which are individual units in Python.
When you create a class that inherits from `unittest.TestCase`
, you can define methods to test specific functionality in your code. These test methods should start with `test`
(e.g., `test_addition`
). Inside each method, you use various assertion methods to check if the actual results match the expected results.

An assertion is a statement that checks whether a condition is true. If it’s false, it raises an error or exception. `unittest.TestCase`
provides the following assertions:

`assertEqual(a, b)`
passes if`a == b`
`assertNotEqual(a, b)`
passes if`a != b`
`assertTrue(x)`
passes if`x`
is`True`
`assertFalse(x)`
passes if`x`
is`False`
`assertIsNone(x)`
passes if`x`
is`None`
`assertRaises(Exception, func, *args)`
passes if`func(*args)`
raises an exception
## Building Your First Test
It’s very simple. After importing `unittest`
, all we need to do is build the function, then create and run the test.

Define the function:

Create the test using the `unittest.TestCase`
class:

Note that if you are using a Jupyter notebook, you will need to replace the following code …

with this code …

at the bottom of your code.

Running this test will yield a success message.

However, just a few small tweaks will make the test fail:

`setup()`
and `teardown()`
These methods ensure each test is isolated and runs in a clean environment with everything it needs.

`setup()`
is a method that runs before each unit test and sets up any necessary state or resources. This may be used when preparing a specific environment or resources (e.g., a database connection or test files) before each test method runs.`teardown()`
cleans up those connections and resources between tests to ensure each test stands on its own.
## Object Mocking
`unittest.mock`
allows you to replace dependencies with mock objects (e.g., API requests). Here is how you can mock an API request:
## Conclusion
Python’s `unittest`
module offers tools for more complex testing needs than those listed above, but these are the basics for getting started. `unittest`
is great for beginners and seasoned engineers alike, making it a great choice for developers looking for a built-in, reliable solution to safeguard the quality of their code.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)