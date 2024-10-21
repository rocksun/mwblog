# Documenting Python Code With Docstrings
![Featued image for: Documenting Python Code With Docstrings](https://cdn.thenewstack.io/media/2024/10/fab2a3a1-bozhin-karaivanov-iiiu2fiury8-unsplash-1-1024x683.jpg)
[Documenting code](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/) is an absolute must, especially if you’re working with a team of developers on a project. Without proper documentation, other developers on your team might not know what it is you’re trying to accomplish with a block of code, which can lead to bottlenecks. In a world where efficiency rules the day, it’s imperative that you avoid causing slowdowns in the workflow.
How do you do that?

Documenting your code.

Of course, there’s always the traditional method of documenting code, which looks something like this:
What we have above is a simple [Hello World application](https://thenewstack.io/typescript-tutorial-go-beyond-hello-world/) with a single comment that is defined by a single # character. If that comment wrapped into a second line, you could add another # character like so:

That’s an easy way to comment your code but it’s not the only way. Let me introduce you to another method of documenting [Python code](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/), the docstring.
## The Docstring
The docstring is a great commenting method, when you know your comments are going to take up several lines and you don’t want to clutter it up with a column of # characters.

Essentially, a docstring is a specific type of comment that describes the purpose and/or functionality of a block of code. This can be used for modules, classes, methods, and/or functions and is placed immediately after the definition of each.

To use a docstring, you place a triple-double quote (“””) at the beginning and end of the code block like so:
In the above example, our docstring is:

As you can see, there are triple double quotes at the top and bottom, which indicates to Python that it’s a docstring. Here’s a full app (that takes user input and writes it to a file) with two docstrings as well as regular comments:
Docstrings can also take up a single line, like this:
1 |
"""This is my comment for Python code""" |
One thing to keep in mind is that, like with regular comments, the [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) standard library requires lines of code be no longer than 79 characters and the style guide for Python Code suggests that the line length of docstrings be limited to 72 characters. What that means is a single line of a comment should not go beyond 72 characters, which is why docstrings are important. When you have a comment that requires more than one line to explain what you’re doing, you would either add a # character before each line or use a docstring.
However, typical best practices indicate that docstrings tend to be used to explain objects. For other bits of code, use a traditional comment. Docstrings are typically comprised of the following components:

- A one-line summary.
- A blank line below the summary.
- Further elaboration.
- Another blank line.
We’ve already seen this at work in the above code. For example:
The first line is the summary, followed by a blank line. Next comes the elaboration, which is followed by the closing “””. To complete the docstring properly, there would be a space between the closing “”” and the next line of code.

## The Class Docstrings
And then there are the class docstrings, which are used to explain classes that you create. A class docstring consists of the following:

- A brief summary of what the class does.
- Descriptions of attributes and methods.
- Any important notes or usage examples.
Here’s an example of a class docstring:
As you can see, we have a multi-line class docstring and two single-line docstrings.

There are other docstrings you can use, such as:

- Package and module docstrings: Lists the modules and sub-packages that are exported. These are similar to class docstrings, only used for modules and the functions within them.
- Script docstrings: A docstring that describes the overall purpose and functionality of an entire Python script or module.
And that’s your introduction to Python docstrings. Using these is a great way to ensure your code is easy to read and understand, which makes them a must for projects where multiple team members have to get involved with the code you write and you don’t want your code cluttered with multiple blocks of traditional comments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)