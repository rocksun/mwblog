I put three [vibe coding tools](https://thenewstack.io/python-vibe-coding-tools/) to the test. Not with the goal of finding the best one, just to see how they’re different. Is one easier? I used three free tools so you can try this project as well and see what your AI comes up with. The tools I chose were [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) (obviously), [CodeGPT](https://codegpt.co/) and [Tabnine](https://www.tabnine.com/). I wrote my code in [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/).

The app I chose to build was a simple calculator app that you can interact with in the terminal. I did want to go a little bigger at first, and try a tip calculator app complete with [HTML and CSS,](https://thenewstack.io/html-first-framework-second-is-javascript-finally-growing-up/) but after about 10 minutes, I realized I could complete this experience with something simpler.

Here are the prompts I came up with as a baseline:

```
# Create a simple terminal calculator


# Ask the user which operation they want: add, subtract, multiply, divide
# Keep prompting until the user enters a valid operation


# Ask the user for the first number
# Validate that the input is a number


# Ask the user for the second number
# Validate that the input is a number
# If operation is divide, also ensure the number is not zero


# Perform the selected operation
# Handle add, subtract, multiply, divide


# Print the result in a clear message


# Ask the user if they want to calculate again
# Keep prompting until the user enters yes or no


# Repeat the calculator loop until the user chooses no
```

Here’s what I discovered along the way.

## GitHub Copilot

I started with GitHub Copilot. GitHub Copilot is a chatbot. I clicked the file I wanted to work with, and that is how GitHub Copilot knew which language to code in. With GitHub Copilot, I copied/pasted all prompts into the chat at the same time to see what it would do.

It returned the full application, reading each prompt. When I ran the file in my terminal, I had a syntax error. I copied/pasted the full function (including buggy and non-buggy code) back into GitHub Copilot, and it was able to fix the bug immediately. I updated the code file. After about 1.5 iterations, the calculator was fully functional.

Here’s the code it provided:

```
# Simple terminal calculator


def get_operation():
    valid_ops = ["add", "subtract", "multiply", "divide"]
    while True:
        op = input("Which operation do you want? (add, subtract, multiply, divide): ").strip().lower()
        if op in valid_ops:
            return op
        print("Please enter a valid operation.")


def get_number(prompt, allow_zero=True):
    while True:
        try:
            num = float(input(prompt))
            if not allow_zero and num == 0:
                print("Cannot be zero. Please enter another number.")
                continue
            return num
        except ValueError:
            print("Please enter a valid number.")


def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


def ask_again():
    while True:
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again in ["yes", "no"]:
            return again == "yes"
        print("Please enter 'yes' or 'no'.")


def main():
    while True:
        operation = get_operation()
        num1 = get_number("Enter the first number: ")
        if operation == "divide":
            num2 = get_number("Enter the second number: ", allow_zero=False)
        else:
            num2 = get_number("Enter the second number: ")
        try:
            print(f"DEBUG: num1={num1}, num2={num2}, operation={operation}")  # Debug line
            result = calculate(num1, num2, operation)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        if not ask_again():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
```

## CodeGPT

Next, I explored CodeGPT. I accessed it via the command palette (Cmd + Shift + P) and selected CodeGPT: Reset to start fresh. One thing I immediately noticed is that CodeGPT doesn’t handle bulk prompts. You can only enter one at a time.

After it provided code for a prompt, it suggested the next steps. For example, after I asked it to enter the first number, it immediately prompted for the second number. I decided to follow the CodeGPT prompts all the way to the end.

The CodeGPT prompts included error handling, and I was able to interact with the calculator in the terminal on the first try. One thing I did notice, though, is that the CodeGPT prompted app terminated after only one calculation.

Here’s the code:

```
# Create a simple terminal calculator


# Ask the user which operation they want: add, subtract, multiply, divide
# Keep prompting until the user enters a valid operation
operation = ""
while operation not in ["add", "subtract", "multiply", "divide"]:
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()




# Ask the user for two numbers 
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
result = None
# Perform the operation and print the result
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")        
if result is not None:
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")           
 


```

I did another one using CodeGPT, this time copying and pasting the prompts as I originally wrote them. This is what CodeGPT came up with:

```
# Ask the user which operation they want: add, subtract, multiply, divide
# Keep prompting until the user enters a valid operation
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
while operation not in ['add', 'subtract', 'multiply', 'divide']:
    print("Invalid operation. Please try again.")
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()


# Ask the user for the first number
# Validate that the input is a number
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")   
num1 = get_number("Enter the first number: ")


# Ask the user for the second number
# Validate that the input is a number
# If operation is divide, also ensure the number is not zero
num2 = get_number("Enter the second number: ")
if operation == 'divide':
    while num2 == 0:
        print("Error: Division by zero is not allowed.")
        num2 = get_number("Please enter a non-zero second number: ")        
result = None
# Perform the selected operation
# Handle add, subtract, multiply, divide
if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    result = num1 / num2    




# Print the result in a clear message
print(f"The result of {operation}ing {num1} and {num2} is: {result}")


# Ask the user if they want to calculate again
# Keep prompting until the user enters yes or no
again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
while again not in ['yes', 'no']:
    print("Invalid input. Please enter 'yes' or 'no'.")
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
if again == 'yes':
    print("Restart the program to perform another calculation.")    


# Repeat the calculator loop until the user chooses no
else:
    print("Thank you for using the calculator. Goodbye!")       
```

## Tabnine

The last tool I used for this experiment is Tabnine. The first go around, I followed the prompts it offered after I gave the first one. They looked oddly similar to the prompts CodeGPT provided. Full disclosure, this is my first time [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/), I wasn’t sure if the prompts were saved somehow or if Tabnine and CodeGPT came up with similar prompts.

One thing that was different with Tabnine, though, is that the prompting didn’t end. If I accepted a prompt, it offered code. The last few prompts were the same. It kept asking if the user wanted to calculate again. I did decide not to follow the last prompt and try to run the app in my terminal.

I was unable to do so due to an error. I ran through this pretty quickly but I didn’t see any easy bug fix options like I did with GitHub Copilot. Ultimately decided to try Tabnine again and this time follow the prompts on my list.

Here’s the code using Tabnine’s prompts:

```
# Ask the user which operation they want: add, subtract, multiply, divide
# Keep prompting until the user enters a valid operation
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
while operation not in ['add', 'subtract', 'multiply', 'divide']:
    print("Invalid operation. Please try again.")
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
    # Ask the user for the first number
# Validate that the input is a number
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            # Ask the user for the second number
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
# If operation is divide, also ensure the number is not zero
if operation == 'divide':
    while num2 == 0:
        print("Error: Division by zero is not allowed.")
        num2 = get_number("Please enter a non-zero second number: ")
result = None
# Perform the selected operation
# Handle add, subtract, multiply, divide
if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    result = num1 / num2
    # Print the result
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    # Ask the user if they want to calculate again
    again = ask_again()
    if not again:
        print("Thank you for using the calculator.")
        break
        # If operation is not one of the above, print an error message
    else: 
        print("Error: Invalid operation.")
 
        #
        # Repeat the calculator loop until the user chooses no
        # Ask the user if they want to calculate again
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        while again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again == 'yes':
                print("Restart the program to perform another calculation.")
                # Repeat the calculator loop until the user chooses no
            else:
                print("Thank you for using the calculator. Goodbye!")
# Function to ask the user if they want to calculate again




```

Here’s the code using my prompts:

```
# Ask the user which operation they want: add, subtract, multiply, divide
# Keep prompting until the user enters a valid operation
operation = ""
while operation not in ["add", "subtract", "multiply", "divide"]:
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()




# Ask the user for the first number
# Validate that the input is a number
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")   
num1 = get_number("Enter the first number: ")


# Ask the user for the second number
# Validate that the input is a number   
num2 = get_number("Enter the second number: ")


# If operation is divide, also ensure the number is not zero
if operation == "divide":
    while num2 == 0:
        print("Error: Division by zero is not allowed.")
        num2 = get_number("Please enter a non-zero second number: ")
        # Perform the selected operation
result = None
# Handle add, subtract, multiply, divide
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    result = num1 / num2
# Print the result in a clear message
print(f"The result of {operation}ing {num1} and {num2} is: {result}")
# Ask the user if they want to calculate again
# Keep prompting until the user enters yes or no    
def ask_again():
    again = ""
    while again not in ["yes", "no"]:
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return again == "yes"
```

## Takeaways:

Vibe coding can be easier, but you really need to know what you’re doing. This was a simple calculator app, but it gets much more complicated. You need to build in some error handling and think through how you want the application to run. If I had to choose my favorite, and I really only worked in these technologies for about an hour each, I’d say GitHub Copilot. I preferred the chatbot over the inline code. I liked how it fixed the small bug quickly.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)