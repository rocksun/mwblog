Earlier today, I got curious and asked myself, “How well would using [command line AI](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) work for programming?”

I’ve used various [IDEs](https://thenewstack.io/best-open-source-ides/) to test how well their AI functions could work with creating programs of different types, but I’d not tried doing the same thing from the command line.

Today, I decided to change that.

Here’s what I discovered.

## The Tools I Used

For this test, I worked on [Pop!\_OS Linux](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) with the [Ollama AI](https://thenewstack.io/install-ollama-ai-on-ubuntu-linux-to-use-llms-on-your-own-machine/) and a specific model that is geared toward coding. You don’t have to use [Linux](https://thenewstack.io/introduction-to-linux-operating-system/). As long as your OS works with Ollama, you’ll be good to go.

Speaking of which …

## Installing Ollama

If you’re using either macOS or Windows, installing Ollama is as easy as downloading the installer file for your OS from the official Ollama site and running it.

With Linux, you simply have to run the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo curl -fsSL https://ollama.com/install.sh | sh |

Once Ollama has been installed, you’ll then need to download a programming-centric AI model. For me, I used qwen3-coder. To use that model, you have to first pull it with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

This model is roughly 15GB, so give it plenty of time to download.

When the download finishes, you then need to run the model with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

You should now find yourself at the Ollama prompt, ready to get to work.

## Creating the First Program

What I decided to do was ask qwen3-coder to create a [Python](https://thenewstack.io/introduction-to-linux-operating-system/) program that would accept user input for name, age, email and phone number and save the data to a file.

The specific query was:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Write a python program that accepts input from a user (for name, age, email address, and phone number) and then saves it to a file |

It took qwen3-coder no time to start generating code. What it came up with was quite long and looked like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def get\_user\_input(): |
|  |  |
|  | """Get user input for name, age, email, and phone number""" |
|  |  |
|  | print("Please enter your information:") |
|  |  |
|  | name = input("Name: ").strip() |
|  |  |
|  | while not name: |
|  |  |
|  | print("Name cannot be empty. Please try again.") |
|  |  |
|  | name = input("Name: ").strip() |
|  |  |
|  | age = input("Age: ").strip() |
|  |  |
|  | while not age.isdigit() or int(age) <= 0: |
|  |  |
|  | print("Please enter a valid age (positive number).") |
|  |  |
|  | age = input("Age: ").strip() |
|  |  |
|  | age = int(age) |
|  |  |
|  | email = input("Email address: ").strip() |
|  |  |
|  | while not email or '@' not in email: |
|  |  |
|  | print("Please enter a valid email address.") |
|  |  |
|  | email = input("Email address: ").strip() |
|  |  |
|  | phone = input("Phone number: ").strip() |
|  |  |
|  | while not phone: |
|  |  |
|  | print("Phone number cannot be empty. Please try again.") |
|  |  |
|  | phone = input("Phone number: ").strip() |
|  |  |
|  | return name, age, email, phone |
|  |  |
|  | def save\_to\_file(name, age, email, phone): |
|  |  |
|  | """Save user information to a file""" |
|  |  |
|  | try: |
|  |  |
|  | with open("user\_info.txt", "a") as file: |
|  |  |
|  | file.write(f"Name: {name}\n") |
|  |  |
|  | file.write(f"Age: {age}\n") |
|  |  |
|  | file.write(f"Email: {email}\n") |
|  |  |
|  | file.write(f"Phone: {phone}\n") |
|  |  |
|  | file.write("-" \* 30 + "\n")  # Separator between entries |
|  |  |
|  | print("Information saved successfully!") |
|  |  |
|  | except Exception as e: |
|  |  |
|  | print(f"Error saving to file: {e}") |
|  |  |
|  | def main(): |
|  |  |
|  | """Main function to run the program""" |
|  |  |
|  | print("User Information Collector") |
|  |  |
|  | print("=" \* 30) |
|  |  |
|  | # Get user input |
|  |  |
|  | name, age, email, phone = get\_user\_input() |
|  |  |
|  | # Display entered information |
|  |  |
|  | print("\nEntered Information:") |
|  |  |
|  | print(f"Name: {name}") |
|  |  |
|  | print(f"Age: {age}") |
|  |  |
|  | print(f"Email: {email}") |
|  |  |
|  | print(f"Phone: {phone}") |
|  |  |
|  | # Confirm save |
|  |  |
|  | confirm = input("\nDo you want to save this information? (y/n): ").strip().lower() |
|  |  |
|  | if confirm in ['y', 'yes']: |
|  |  |
|  | save\_to\_file(name, age, email, phone) |
|  |  |
|  | print("Thank you for providing your information!") |
|  |  |
|  | else: |
|  |  |
|  | print("Information not saved.") |
|  |  |
|  | if \_\_name\_\_ == "\_\_main\_\_": |
|  |  |
|  | main() |

I copied the above code to a file named *ai\_input.py* and ran it with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

To my surprise, it ran flawlessly.

Next, I decided to test it further by querying:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Can you turn that same program into a GUI app? |

I was certain qwen3-coder would fail at this point. Sure, it might generate some code, but there’s no way it would get this right.

It took roughly the same amount of time for the model to spit out the new code, which looked like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | import tkinter as tk |
|  |  |
|  | from tkinter import ttk, messagebox |
|  |  |
|  | import datetime |
|  |  |
|  | class UserInformationApp: |
|  |  |
|  | def \_\_init\_\_(self, root): |
|  |  |
|  | self.root = root |
|  |  |
|  | self.root.title("User Information Collector") |
|  |  |
|  | self.root.geometry("500x400") |
|  |  |
|  | self.root.resizable(True, True) |
|  |  |
|  | # Create main frame |
|  |  |
|  | main\_frame = ttk.Frame(root, padding="20") |
|  |  |
|  | main\_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)) |
|  |  |
|  | # Configure grid weights |
|  |  |
|  | root.columnconfigure(0, weight=1) |
|  |  |
|  | root.rowconfigure(0, weight=1) |
|  |  |
|  | main\_frame.columnconfigure(1, weight=1) |
|  |  |
|  | # Title |
|  |  |
|  | title\_label = ttk.Label(main\_frame, text="User Information Collector", |
|  |  |
|  | font=("Arial", 16, "bold")) |
|  |  |
|  | title\_label.grid(row=0, column=0, columnspan=2, pady=(0, 20)) |
|  |  |
|  | # Name field |
|  |  |
|  | ttk.Label(main\_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5) |
|  |  |
|  | self.name\_entry = ttk.Entry(main\_frame, width=30) |
|  |  |
|  | self.name\_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5) |
|  |  |
|  | # Age field |
|  |  |
|  | ttk.Label(main\_frame, text="Age:").grid(row=2, column=0, sticky=tk.W, pady=5) |
|  |  |
|  | self.age\_entry = ttk.Entry(main\_frame, width=30) |
|  |  |
|  | self.age\_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5) |
|  |  |
|  | # Email field |
|  |  |
|  | ttk.Label(main\_frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=5) |
|  |  |
|  | self.email\_entry = ttk.Entry(main\_frame, width=30) |
|  |  |
|  | self.email\_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5) |
|  |  |
|  | # Phone field |
|  |  |
|  | ttk.Label(main\_frame, text="Phone:").grid(row=4, column=0, sticky=tk.W, pady=5) |
|  |  |
|  | self.phone\_entry = ttk.Entry(main\_frame, width=30) |
|  |  |
|  | self.phone\_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5) |
|  |  |
|  | # Buttons frame |
|  |  |
|  | button\_frame = ttk.Frame(main\_frame) |
|  |  |
|  | button\_frame.grid(row=5, column=0, columnspan=2, pady=20) |
|  |  |
|  | # Save button |
|  |  |
|  | save\_button = ttk.Button(button\_frame, text="Save Information", command=self.save\_information) |
|  |  |
|  | save\_button.pack(side=tk.LEFT, padx=5) |
|  |  |
|  | # Clear button |
|  |  |
|  | clear\_button = ttk.Button(button\_frame, text="Clear Fields", command=self.clear\_fields) |
|  |  |
|  | clear\_button.pack(side=tk.LEFT, padx=5) |
|  |  |
|  | # Exit button |
|  |  |
|  | exit\_button = ttk.Button(button\_frame, text="Exit", command=root.quit) |
|  |  |
|  | exit\_button.pack(side=tk.LEFT, padx=5) |
|  |  |
|  | # Status bar |
|  |  |
|  | self.status\_var = tk.StringVar() |
|  |  |
|  | self.status\_var.set("Ready") |
|  |  |
|  | status\_bar = ttk.Label(main\_frame, textvariable=self.status\_var, relief=tk.SUNKEN) |
|  |  |
|  | status\_bar.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0)) |
|  |  |
|  | # Bind Enter key to save |
|  |  |
|  | self.root.bind('<Return>', lambda event: self.save\_information()) |
|  |  |
|  | # Focus on name field |
|  |  |
|  | self.name\_entry.focus() |
|  |  |
|  | def validate\_input(self): |
|  |  |
|  | """Validate all input fields""" |
|  |  |
|  | name = self.name\_entry.get().strip() |
|  |  |
|  | age = self.age\_entry.get().strip() |
|  |  |
|  | email = self.email\_entry.get().strip() |
|  |  |
|  | phone = self.phone\_entry.get().strip() |
|  |  |
|  | # Check if fields are empty |
|  |  |
|  | if not name: |
|  |  |
|  | messagebox.showerror("Error", "Name cannot be empty!") |
|  |  |
|  | self.name\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | if not age: |
|  |  |
|  | messagebox.showerror("Error", "Age cannot be empty!") |
|  |  |
|  | self.age\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | if not email: |
|  |  |
|  | messagebox.showerror("Error", "Email cannot be empty!") |
|  |  |
|  | self.email\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | if not phone: |
|  |  |
|  | messagebox.showerror("Error", "Phone cannot be empty!") |
|  |  |
|  | self.phone\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | # Validate age is a number |
|  |  |
|  | try: |
|  |  |
|  | age\_int = int(age) |
|  |  |
|  | if age\_int <= 0: |
|  |  |
|  | messagebox.showerror("Error", "Age must be a positive number!") |
|  |  |
|  | self.age\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | except ValueError: |
|  |  |
|  | messagebox.showerror("Error", "Age must be a valid number!") |
|  |  |
|  | self.age\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | # Validate email format |
|  |  |
|  | if '@' not in email: |
|  |  |
|  | messagebox.showerror("Error", "Please enter a valid email address!") |
|  |  |
|  | self.email\_entry.focus() |
|  |  |
|  | return None |
|  |  |
|  | return { |
|  |  |
|  | 'name': name, |
|  |  |
|  | 'age': age\_int, |
|  |  |
|  | 'email': email, |
|  |  |
|  | 'phone': phone |
|  |  |
|  | } |
|  |  |
|  | def save\_information(self): |
|  |  |
|  | """Save user information to file""" |
|  |  |
|  | # Validate input |
|  |  |
|  | user\_data = self.validate\_input() |
|  |  |
|  | if not user\_data: |
|  |  |
|  | return |
|  |  |
|  | try: |
|  |  |
|  | # Create or append to file |
|  |  |
|  | with open("user\_info.txt", "a") as file: |
|  |  |
|  | file.write(f"\n{'='\*50}\n") |
|  |  |
|  | file.write(f"Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n") |
|  |  |
|  | file.write(f"Name: {user\_data['name']}\n") |
|  |  |
|  | file.write(f"Age: {user\_data['age']}\n") |
|  |  |
|  | file.write(f"Email: {user\_data['email']}\n") |
|  |  |
|  | file.write(f"Phone: {user\_data['phone']}\n") |
|  |  |
|  | file.write(f"{'='\*50}\n") |
|  |  |
|  | # Show success message |
|  |  |
|  | messagebox.showinfo("Success", "Information saved successfully!") |
|  |  |
|  | self.status\_var.set("Information saved successfully!") |
|  |  |
|  | # Clear fields after successful save |
|  |  |
|  | self.clear\_fields() |
|  |  |
|  | except Exception as e: |
|  |  |
|  | messagebox.showerror("Error", f"Failed to save information: {str(e)}") |
|  |  |
|  | self.status\_var.set(f"Error: {str(e)}") |
|  |  |
|  | def clear\_fields(self): |
|  |  |
|  | """Clear all input fields""" |
|  |  |
|  | self.name\_entry.delete(0, tk.END) |
|  |  |
|  | self.age\_entry.delete(0, tk.END) |
|  |  |
|  | self.email\_entry.delete(0, tk.END) |
|  |  |
|  | self.phone\_entry.delete(0, tk.END) |
|  |  |
|  | self.name\_entry.focus() |
|  |  |
|  | self.status\_var.set("Fields cleared") |
|  |  |
|  | def main(): |
|  |  |
|  | root = tk.Tk() |
|  |  |
|  | app = UserInformationApp(root) |
|  |  |
|  | root.mainloop() |
|  |  |
|  | if \_\_name\_\_ == "\_\_main\_\_": |
|  |  |
|  | main() |

That’s a lot of code, and surely it would error out, right?

It did.

However, the error was simply because the program couldn’t find tkinter. I installed it with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install python3-tk -y |

I reran the code, and to my shock, the graphical user interface (GUI) opened (Figure 1).

[![](https://cdn.thenewstack.io/media/2025/11/02b3cce3-qwen3_1.jpg)](https://cdn.thenewstack.io/media/2025/11/02b3cce3-qwen3_1.jpg)

Figure 1: My new Python GUI app works surprisingly well.

I could type input, save it, type more input, save it and keep going until I clicked Exit.

I decided to throw it for another look and ran another follow-up query:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Can you change the background color of the GUI to pink? |

Qwen3-coder went to work and spit out more code. I saved the output, ran it, and found that (once again) the app was successful.

Ruh roh. This time the program errored out with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | "save\_button = ttk.Button(button\_frame, text="Save Information", comman |
|  |  |
|  | ... d=self.save\_information" |

So, I ran another query informing qwen3-coder about the error to see if it could fix it. It went to work and believed it found the error. After it produced the new code: rinse, wash, repeat.

This time, the code was considerably longer (not sure why) and, according to qwen3-coder, this is what was fixed:

* Fixed the button creation syntax\*\* — Added the missing closing parenthesis and proper styling.
* Added the missing `save_information` method\*\* — This was causing the error since it was referenced but not defined.
* Added proper file saving functionality\*\* — The save button now actually saves data to a file.
* Fixed the lambda binding\*\* — Made it properly formatted.
* Added proper error handling\*\* — For file operations.
* Fixed the method call\*\* — Made sure all method references are properly defined.

This time, the code ran fine. Although the background of the app wasn’t pink, the background for all the fields was.

Picking at nits.

The important thing here is that the Ollama command line AI tool was successful at what I’d asked it to do. Even with an error, I was able to do follow-up queries to resolve issues and even improve the code.

Does that mean you can stop learning the craft of programming and rely solely on AI? I wouldn’t. Because I know enough about Python, I am better capable of using the tool to either create something new or learn new concepts for the language.

Of course, your mileage may vary.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)