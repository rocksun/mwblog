<!--
title: 命令行AI：你的编程效率倍增器？
cover: https://cdn.thenewstack.io/media/2025/11/b0452122-thisisengineering-64yrpkiguae-unsplash.jpg
summary: 文章探讨了使用命令行AI编程的效果。作者使用Ollama AI的qwen3-coder模型，成功创建了Python命令行程序和GUI应用，并解决了报错。结果显示命令行AI对编程有效，但仍需用户具备一定编程知识。
-->

文章探讨了使用命令行AI编程的效果。作者使用Ollama AI的qwen3-coder模型，成功创建了Python命令行程序和GUI应用，并解决了报错。结果显示命令行AI对编程有效，但仍需用户具备一定编程知识。

> 译自：[Is Using Command Line AI an Option for Helping You Code?](https://thenewstack.io/is-using-command-line-ai-an-option-for-helping-you-code/)
> 
> 作者：Jack Wallen

今天早些时候，我好奇地问自己：“使用[命令行AI](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/)进行编程的效果会如何？”

我曾使用各种[IDE](https://thenewstack.io/best-open-source-ides/)测试它们的AI功能在创建不同类型的程序时表现如何，但我从未尝试从命令行做同样的事情。

今天，我决定改变这一点。

以下是我的发现。

## 我使用的工具

对于这项测试，我在[Pop!\_OS Linux](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/)上使用[Ollama AI](https://thenewstack.io/install-ollama-ai-on-ubuntu-linux-to-use-llms-on-your-own-machine/)和一个专门用于编程的模型。你不必使用[Linux](https://thenewstack.io/introduction-to-linux-operating-system/)。只要你的操作系统与Ollama兼容，就能正常运行。

说到这里……

## 安装 Ollama

如果你使用macOS或Windows，安装Ollama就像从Ollama官方网站下载适用于你操作系统的安装文件并运行它一样简单。

对于Linux，你只需运行以下命令：

```bash
sudo curl -fsSL https://ollama.com/install.sh | sh
```

Ollama安装完成后，你需要下载一个以编程为中心的AI模型。我使用的是qwen3-coder。要使用该模型，你必须首先使用以下命令拉取它：

```bash
ollama pull qwen3-coder
```

该模型大约15GB，所以请预留充足的时间下载。

下载完成后，你需要使用以下命令运行该模型：

```bash
ollama run qwen3-coder
```

现在你应该会看到Ollama提示符，准备开始工作。

## 创建第一个程序

我决定让qwen3-coder创建一个[Python](https://thenewstack.io/introduction-to-linux-operating-system/)程序，该程序接受用户输入的姓名、年龄、电子邮件和电话号码，并将数据保存到文件中。

具体的查询是：

```
Write a python program that accepts input from a user (for name, age, email address, and phone number) and then saves it to a file
```

qwen3-coder很快就开始生成代码。它生成了相当长的代码，看起来像这样：

```py
def get_user_input():
    """Get user input for name, age, email, and phone number"""
    print("Please enter your information:")
    name = input("Name: ").strip()
    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Name: ").strip()
    age = input("Age: ").strip()
    while not age.isdigit() or int(age) <= 0:
        print("Please enter a valid age (positive number).")
        age = input("Age: ").strip()
    age = int(age)
    email = input("Email address: ").strip()
    while not email or '@' not in email:
        print("Please enter a valid email address.")
        email = input("Email address: ").strip()
    phone = input("Phone number: ").strip()
    while not phone:
        print("Phone number cannot be empty. Please try again.")
        phone = input("Phone number: ").strip()
    return name, age, email, phone

def save_to_file(name, age, email, phone):
    """Save user information to a file"""
    try:
        with open("user_info.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone: {phone}\n")
            file.write("-" * 30 + "\n")  # Separator between entries
        print("Information saved successfully!")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    """Main function to run the program"""
    print("User Information Collector")
    print("=" * 30)
    # Get user input
    name, age, email, phone = get_user_input()
    # Display entered information
    print("\nEntered Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    # Confirm save
    confirm = input("\nDo you want to save this information? (y/n): ").strip().lower()

    if confirm in ['y', 'yes']:
        save_to_file(name, age, email, phone)
        print("Thank you for providing your information!")
    else:
        print("Information not saved.")
if __name__ == "__main__":
    main()
```

我将上述代码复制到一个名为 `ai_input.py` 的文件中，并使用以下命令运行：

```
python3 ai_input.py
```

令我惊讶的是，它完美运行。

接下来，我决定通过查询进一步测试它：

```
Can you turn that same program into a GUI app?
```

我确信qwen3-coder会在这里失败。当然，它可能会生成一些代码，但不可能把它做对。

模型花费了大致相同的时间吐出了新代码，看起来像这样：

```py
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class UserInformationApp:

    def __init__(self, root):
        self.root = root
        self.root.title("User Information Collector")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="User Information Collector",
                               font=("Arial", 16, "bold"))

        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Name field
        ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # Age field
        ttk.Label(main_frame, text="Age:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.age_entry = ttk.Entry(main_frame, width=30)
        self.age_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # Email field
        ttk.Label(main_frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(main_frame, width=30)
        self.email_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

        # Phone field
        ttk.Label(main_frame, text="Phone:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.phone_entry = ttk.Entry(main_frame, width=30)
        self.phone_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)

        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)

        # Save button
        save_button = ttk.Button(button_frame, text="Save Information", command=self.save_information)
        save_button.pack(side=tk.LEFT, padx=5)

        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear Fields", command=self.clear_fields)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Exit button
        exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
        exit_button.pack(side=tk.LEFT, padx=5)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)

        status_bar.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0))
        # Bind Enter key to save
        self.root.bind('<Return>', lambda event: self.save_information())
        # Focus on name field
        self.name_entry.focus()

    def validate_input(self):
        """Validate all input fields"""
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        # Check if fields are empty

        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            self.name_entry.focus()
            return None
        if not age:
            messagebox.showerror("Error", "Age cannot be empty!")
            self.age_entry.focus()
            return None

        if not email:
            messagebox.showerror("Error", "Email cannot be empty!")
            self.email_entry.focus()
            return None

        if not phone:
            messagebox.showerror("Error", "Phone cannot be empty!")
            self.phone_entry.focus()
            return None
        # Validate age is a number

        try:
            age_int = int(age)
            if age_int <= 0:
                messagebox.showerror("Error", "Age must be a positive number!")
                self.age_entry.focus()
                return None

        except ValueError:
            messagebox.showerror("Error", "Age must be a valid number!")
            self.age_entry.focus()
            return None
        # Validate email format

        if '@' not in email:
            messagebox.showerror("Error", "Please enter a valid email address!")
            self.email_entry.focus()
            return None
        return {
            'name': name,
            'age': age_int,
            'email': email,
            'phone': phone
        }

    def save_information(self):
        """Save user information to file"""
        # Validate input
        user_data = self.validate_input()
        if not user_data:
            return
        try:
            # Create or append to file
            with open("user_info.txt", "a") as file:
                file.write(f"\n{'='*50}\n")
                file.write(f"Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Name: {user_data['name']}\n")
                file.write(f"Age: {user_data['age']}\n")
                file.write(f"Email: {user_data['email']}\n")
                file.write(f"Phone: {user_data['phone']}\n")
                file.write(f"{'='*50}\n")
            # Show success message
            messagebox.showinfo("Success", "Information saved successfully!")
            self.status_var.set("Information saved successfully!")
            # Clear fields after successful save
            self.clear_fields()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save information: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")

    def clear_fields(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.name_entry.focus()
        self.status_var.set("Fields cleared")

def main():
    root = tk.Tk()
    app = UserInformationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

代码量很大，肯定会出错，对吧？

确实出错了。

然而，错误仅仅是因为程序找不到tkinter。我用以下命令安装了它：

```py
sudo apt-get install python3-tk -y
```

我重新运行了代码，令我震惊的是，图形用户界面（GUI）打开了（图1）。

[![](https://cdn.thenewstack.io/media/2025/11/02b3cce3-qwen3_1.jpg)](https://cdn.thenewstack.io/media/2025/11/02b3cce3-qwen3_1.jpg)

图1：我的新Python GUI应用程序出人意料地运行良好。

我可以输入、保存，再次输入、保存，并一直重复，直到我点击“退出”。

我决定再次测试它，并运行了另一个后续查询：

```
Can you change the background color of the GUI to pink?
```

Qwen3-coder开始工作并又吐出了一些代码。我保存了输出，运行它，发现（再次）应用程序成功了。

糟糕。这次程序报错了：

```py
"save_button = ttk.Button(button_frame, text="Save Information", comman

... d=self.save_information"
```

于是，我又运行了一个查询，将错误告知qwen3-coder，看看它是否能修复。它开始工作，并认为它找到了错误。在它生成新代码之后：清理、冲洗、重复。

这一次，代码明显更长（不确定为什么），根据qwen3-coder的说法，以下是修复内容：

* 修复了按钮创建语法——添加了缺失的右括号和正确的样式。
* 添加了缺失的`save_information`方法——由于该方法被引用但未定义，导致了错误。
* 添加了正确的文件保存功能——现在保存按钮确实可以将数据保存到文件中。
* 修复了lambda绑定——使其格式正确。
* 添加了正确的错误处理——用于文件操作。
* 修复了方法调用——确保所有方法引用都正确定义。

这次代码运行正常。尽管应用程序的背景不是粉红色，但所有字段的背景都是粉红色的。

吹毛求疵。

这里重要的是，Ollama命令行AI工具成功完成了我要求它做的事情。即使出现错误，我也能够进行后续查询来解决问题，甚至改进代码。

这是否意味着你可以停止学习编程技艺，完全依赖AI呢？我不会。因为我对Python足够了解，所以我能更好地利用这个工具来创建新事物或学习该语言的新概念。

当然，效果因人而异。