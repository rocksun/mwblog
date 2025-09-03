<!--
title: Python 氛围编程：Copilot、CodeGPT 和 Tabnine 哪家强？
cover: https://cdn.thenewstack.io/media/2025/09/5a7fc978-alexander-ross-ywmrhtdm9g8-unsplash-1.jpg
summary: 根据测试，GitHub Copilot 通过聊天机器人快速修复错误，更易于使用。CodeGPT 和 Tabnine 类似，但 GitHub Copilot 是首选。
-->

根据测试，GitHub Copilot 通过聊天机器人快速修复错误，更易于使用。CodeGPT 和 Tabnine 类似，但 GitHub Copilot 是首选。

> 译自：[Vibe Coding Python: Testing Copilot vs. CodeGPT vs. Tabnine](https://thenewstack.io/vibe-coding-python-testing-copilot-vs-codegpt-vs-tabnine/)
> 
> 作者：Jessica Wachtel

我测试了三个[氛围编程工具](https://thenewstack.io/python-vibe-coding-tools/)。目的不是为了找到最好的一个，只是为了看看它们有什么不同。哪一个更容易使用？我使用了三个免费工具，所以你也可以尝试这个项目，看看你的 AI 会给出什么。我选择的工具是 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) (很明显)，[CodeGPT](https://codegpt.co/) 和 [Tabnine](https://www.tabnine.com/)。我用 [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 编写了我的代码。

我选择构建的应用程序是一个简单的计算器应用程序，你可以在终端中与之交互。起初我确实想做得更大一点，尝试做一个包含 [HTML 和 CSS](https://thenewstack.io/html-first-framework-second-is-javascript-finally-growing-up/) 的小费计算器应用程序，但在大约 10 分钟后，我意识到我可以用更简单的东西来完成这个体验。

以下是我作为基线提出的提示：

```
# 创建一个简单的终端计算器


# 询问用户想要进行哪种运算：加、减、乘、除
# 持续提示，直到用户输入有效的运算


# 询问用户第一个数字
# 验证输入是否为数字


# 询问用户第二个数字
# 验证输入是否为数字
# 如果运算是除法，还要确保数字不为零


# 执行所选的运算
# 处理加、减、乘、除


# 以清晰的消息打印结果


# 询问用户是否要再次计算
# 持续提示，直到用户输入是或否


# 重复计算器循环，直到用户选择否
```

以下是我在此过程中发现的。

## GitHub Copilot

我从 GitHub Copilot 开始。GitHub Copilot 是一个聊天机器人。我点击了我想使用的文件，GitHub Copilot 就是这样知道要用哪种语言进行编码的。使用 GitHub Copilot，我将所有提示一次性复制/粘贴到聊天中，看看会发生什么。

它返回了完整的应用程序，读取了每个提示。当我在终端中运行该文件时，我遇到了语法错误。我将整个函数（包括有错误和无错误的代码）复制/粘贴回 GitHub Copilot，它能够立即修复该错误。我更新了代码文件。经过大约 1.5 次迭代，计算器完全可以正常工作了。

这是它提供的代码：

```
# 简单的终端计算器


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

接下来，我探索了 CodeGPT。我通过命令面板 (Cmd + Shift + P) 访问它，然后选择 CodeGPT: Reset 以重新开始。我立即注意到的一件事是 CodeGPT 不处理批量提示。你一次只能输入一个。

在它为提示提供代码后，它会建议后续步骤。例如，在我要求它输入第一个数字后，它立即提示输入第二个数字。我决定一直遵循 CodeGPT 的提示直到结束。

CodeGPT 的提示包括错误处理，我第一次尝试就可以在终端中与计算器交互。但我确实注意到一件事，CodeGPT 提示的应用程序只在一次计算后就终止了。

这是代码：

```
# 创建一个简单的终端计算器


# 询问用户想要进行哪种运算：加、减、乘、除
# 持续提示，直到用户输入有效的运算
operation = ""
while operation not in ["add", "subtract", "multiply", "divide"]:
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()




# 询问用户两个数字 
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
result = None
# 执行运算并打印结果
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

我使用 CodeGPT 又做了一次，这次复制并粘贴了我最初编写的提示。这是 CodeGPT 提出的：

```
# 询问用户想要进行哪种运算：加、减、乘、除
# 持续提示，直到用户输入有效的运算
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
while operation not in ['add', 'subtract', 'multiply', 'divide']:
    print("Invalid operation. Please try again.")
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()


# 询问用户第一个数字
# 验证输入是否为数字
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")   
num1 = get_number("Enter the first number: ")


# 询问用户第二个数字
# 验证输入是否为数字
# 如果运算是除法，还要确保数字不为零
num2 = get_number("Enter the second number: ")
if operation == 'divide':
    while num2 == 0:
        print("Error: Division by zero is not allowed.")
        num2 = get_number("Please enter a non-zero second number: ")        
result = None
# 执行所选的运算
# 处理加、减、乘、除
if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    result = num1 / num2    




# 以清晰的消息打印结果
print(f"The result of {operation}ing {num1} and {num2} is: {result}")


# 询问用户是否要再次计算
# 持续提示，直到用户输入是或否
again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
while again not in ['yes', 'no']:
    print("Invalid input. Please enter 'yes' or 'no'.")
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
if again == 'yes':
    print("Restart the program to perform another calculation.")    


# 重复计算器循环，直到用户选择否
else:
    print("Thank you for using the calculator. Goodbye!")       
```

## Tabnine

我用于此实验的最后一个工具是 Tabnine。第一次尝试时，我按照它在给出第一个提示后提供的提示。它们看起来与 CodeGPT 提供的提示非常相似。完全公开，这是我第一次进行[氛围编程](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)，我不确定提示是否以某种方式保存，或者 Tabnine 和 CodeGPT 是否提出了类似的提示。

不过，Tabnine 的一个不同之处是，提示没有结束。如果我接受一个提示，它会提供代码。最后几个提示都是一样的。它一直问用户是否要再次计算。我确实决定不遵循最后一个提示，并在我的终端中运行该应用程序。

由于错误，我无法这样做。我很快地完成了这个过程，但我没有看到像 GitHub Copilot 那样容易修复错误的选择。最终决定再次尝试 Tabnine，这次遵循我列表中的提示。

以下是使用 Tabnine 的提示的代码：

```
# 询问用户想要进行哪种运算：加、减、乘、除
# 持续提示，直到用户输入有效的运算
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
while operation not in ['add', 'subtract', 'multiply', 'divide']:
    print("Invalid operation. Please try again.")
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
    # 询问用户第一个数字
# 验证输入是否为数字
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            # 询问用户第二个数字
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
# 如果运算是除法，还要确保数字不为零
if operation == 'divide':
    while num2 == 0:
        print("Error: Division by zero is not allowed.")
        num2 = get_number("Please enter a non-zero second number: ")
result = None
# 执行所选的运算
# 处理加、减、乘、除
if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    result = num1 / num2
    # 打印结果
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    # 询问用户是否要再次计算
    again = ask_again()
    if not again:
        print("Thank you for using the calculator.")
        break
        # 如果运算不是以上之一，则打印错误消息
    else: 
        print("Error: Invalid operation.")
 
        #
        # 重复计算器循环，直到用户选择否
        # 询问用户是否要再次计算
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        while again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again == 'yes':
                print("Restart the program to perform another calculation.")
                # 重复计算器循环，直到用户选择否
            else:
                print("Thank you for using the calculator. Goodbye!")
# Function to ask the user if they want to calculate again




```

以下是使用我的提示的代码：

```
# 询问用户想要进行哪种运算：加、减、乘、除
# 持续提示，直到用户输入有效的运算
operation = ""
while operation not in ["add", "subtract", "multiply", "divide"]:
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()




# 询问用户第一个数字
# 验证输入是否为数字
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")   
num1 = get_number("Enter the first number: ")


# 询问用户第二个数字
# 验证输入是否为数字   
num2 = get_number("Enter the second number: ")


# 如果运算是除法，还要确保数字不为零
if operation == "divide":
    while num2 == 0:
        print("Error: Division by zero is not allowed.")
        num2 = get_number("Please enter a non-zero second number: ")
        # 执行所选的运算
result = None
# 处理加、减、乘、除
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    result = num1 / num2
# 以清晰的消息打印结果
print(f"The result of {operation}ing {num1} and {num2} is: {result}")
# 询问用户是否要再次计算
# 持续提示，直到用户输入是或否    
def ask_again():
    again = ""
    while again not in ["yes", "no"]:
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return again == "yes"
```

## 要点：

氛围编程可能会更容易，但你真的需要知道自己在做什么。这是一个简单的计算器应用程序，但它会变得更加复杂。你需要构建一些错误处理，并考虑你希望应用程序如何运行。如果我必须选择我最喜欢的，而我实际上只在这些技术中工作了大约一个小时，我会选择 GitHub Copilot。我更喜欢聊天机器人而不是内联代码。我喜欢它如何快速修复小错误。