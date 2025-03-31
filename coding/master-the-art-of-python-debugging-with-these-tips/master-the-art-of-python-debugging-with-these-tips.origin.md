# Master the Art of Python Debugging With These Tips
![Featued image for: Master the Art of Python Debugging With These Tips](https://cdn.thenewstack.io/media/2025/03/28e4ccdd-getty-images-cnekrh4k6f8-unsplash-1-1024x576.jpg)
Every developer, regardless of their experience, encounters bugs.** Bugs are a normal part of coding** — maybe not everyone’s favorite part but definitely still part of their daily work. Coding success is less about avoiding bugs and more about how you approach and solve them. [Debugging code](https://thenewstack.io/rookout-brings-debugging-to-third-party-code/) is an essential skill for any programmer, and as a [Python](https://thenewstack.io/python/) beginner, developing effective debugging habits will help you solve problems more quickly and learn the language better. [Debugging](https://thenewstack.io/how-generative-ai-is-revolutionizing-debugging/) is not a reflection of your coding ability; it’s an opportunity to grow and improve. These [Python beginner](https://thenewstack.io/python-for-beginners-lists/) debugging tips will help get you started!

**“I can do it” mindset > “Oh no! I’ll never solve this”**
The right mindset is the key to success during many challenges. Debugging is no different.

- Debugging takes time and practice. Be patient.
- Change one thing at a time and retest. Don’t try to do everything at once.
- Debugging is a puzzle. It’s easy to get frazzled, but stay calm. Calmness and diligence will lead to clarity.
- Take breaks! If debugging becomes too frustrating or overwhelming, step away and come back after a walk outside or a slice of pizza.
The easiest way to start debugging is to check for common mistakes. This can include indentation errors (since Python is sensitive to indentation), variable scope issues or accidental typos. When that doesn’t work, check out these tools.

### Understand Error Messages
Python provides helpful error messages, also known as stack traces, when something goes wrong. Here’s how to use them effectively:

- Read the last line first. This is the actual error type and message.
- Trace back through the lines. The stack trace shows where the error occurred in your code.
Code example:

Output: ZeroDivisionError: division by zero

### Use `print()`
Statements
Adding `print()`
statements to your code helps track the flow and values of variables. If you get an error, check if the printed values match your expectations. You can use as many `print()`
statements as you’d like.

Code example:

Output: Debug: a = 5, b = 3

Debug: result = 8

8

**Print statement for input values**: The first print shows the values of a and b before the operation, helping verify they are what you expect.**Print statement for result**: The second print shows the result after the addition, which helps confirm if the function is performing as expected.
### Leverage `pdb`
`pdb`
is Python’s built-in debugger. It allows you to pause execution and inspect variables interactively.
Add this line where you want to debug:

Code example:

In the debugger, you can:

- Type
`n`
to go to the next line. - Type
`p variable_name`
to inspect variables. - Type
`c`
to continue execution.
### Check Assumptions
Be sure there aren’t any simple mistakes and fixes. Ask yourself questions like:

- Is the data type correct?
- Are loops and conditions behaving as expected?
Code example:

Python has built-in functions that help with this. In this example, `len(nums)`
will confirm the range limit. [Here’s more info](https://docs.python.org/3/library/functions.html#len) on the `len()`
function and where you can read more on similar functions.

### Use `logging`
The `logging`
module in Python provides a flexible framework for emitting log messages from your application. Unlike using `print()`
statements for debugging, `logging`
allows you to categorize log messages by severity (e.g., `DEBUG`
, `INFO`
, `WARNING`
, `ERROR`
, `CRITICAL`
) and output them to different destinations (console, files, remote servers).

Code example:

Output:

INFO:root:Application started

DEBUG:root:Starting data processing

INFO:root:Data processing started

WARNING:root:Data quality is low

ERROR:root:Error occurred during processing

CRITICAL:root:Processing failed!

INFO:root:Application finished

For more on `logging`
, check out the [Python docs](https://docs.python.org/3/library/logging.html).

### Write Unit Tests
Python has a `unittest`
module to help you write tests that validates your code.

Code example:

**Function to test**:`add_numbers(a, b)`
returns the sum of`a`
and`b`
.**Test case class**:`TestAddNumbers`
inherits from`unittest.TestCase`
and includes three test methods (`test_add_positive_numbers`
,`test_add_negative_numbers`
and`test_add_mixed_numbers`
), each testing a different scenario for the add_numbers function.**Assertions**: The`assertEqual()`
method checks that the result of`add_numbers(a, b)`
matches the expected result.
### Use an IDE With Built-In Debugging
[Integrated development environments (IDEs)](https://thenewstack.io/best-open-source-ides/) like [PyCharm](https://thenewstack.io/getting-started-with-python-on-macos/), [VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) or [Thonny](https://thonny.org/) have built-in debugging tools. IDEs provide tools like the following to facilitate easier debugging.
**Breakpoints**
Most IDEs allow you to set breakpoints in your code. A breakpoint pauses the execution of your program at a specific line, enabling you to inspect variables, evaluate expressions and step through the code line by line.

**Step Through (Step Over, Step Into, Step Out)**
These features allow you to control the execution flow of your program.

- Step Over: Executes the current line of code and moves to the next one.
- Step Into: Enters into a function or method to debug it line by line.
- Step Out: Exits the current function and returns to the calling function.
**Variable Watch**
This tool lets you track the values of specific variables during the execution of your program. You can monitor how they change as you step through the code, helping identify issues related to variable state.

**Call Stack Inspection **
The call stack shows you the function calls that lead up to the current point in the execution. By inspecting the call stack, you can understand the sequence of function calls and where your code is in its execution flow.

**Console Output/Log Window**
IDEs often include a console or log window where you can see the output of print statements or logging. This is useful for tracking real-time output, error messages and warnings, which can provide important context for debugging.

### Use External Tools
A **linter** is a tool that analyzes your source code to detect potential errors, bugs or stylistic issues based on predefined coding standards. Popular linters like `pylint`
and `flake8`
can catch style and syntax issues.

A **static analyzer** is a tool that examines source code without executing it to find potential errors, bugs or security vulnerabilities. It inspects the code’s structure, flow and logic, often flagging issues such as uninitialized variables, memory leaks and violations of coding standards. `mypy`
is a static analyzer that can help check type consistency.

### It Gets Easier With Time!
Debugging is a skill that improves with practice. Embrace debugging as a normal part of development. By following these tips, you’ll become more confident in identifying and resolving bugs in your Python code.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)