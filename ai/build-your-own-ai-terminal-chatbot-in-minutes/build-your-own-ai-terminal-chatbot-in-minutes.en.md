A few months ago, we built an [AI chatbot in under 10 minutes](https://thenewstack.io/build-a-python-chatgpt-3-5-chatbot-in-10-minutes/). Today, we’re going to build a similar [chatbot](https://thenewstack.io/a-practical-guide-to-building-a-rag-powered-chatbot/) directly in your terminal. What’s the value of building something like this into your terminal? Working right in your terminal lets you stay in your dev flow. It can interact with your local files, tools and system. Essentially, the terminal chatbot brings AI right into your environment. You can ask [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) questions, have it review or generate code and even run commands without any context switching.

The chatbot that we’re going to build will take it one step further than the one we built previously. The terminal chatbot will include the same conversation functionality, but we’re also going to make it able to reply with code snippets and shell commands.

*Note: Before you build ChatGPT or any other AI into your system, take time to read about training data and privacy policies for the version of AI you use so you can work with AI safely.*

### Let’s Get Set up With OpenAI First

1. Go to https://platform.openai.com/signup and create an account.
2. After logging in, go to <https://platform.openai.com/account/api-keys>.
3. Click Create new secret key.
4. Copy the key (starts with sk-…). Don’t share your API key.

GPT-3.5 is free, but anything higher (4.0 is the basic model we use now) is only available for pay-as-you-go users, not the free account. The following tutorial uses GPT-4.0. I made the minimum payment of $10. That said, you can build this with GPT-3.5. I will make a note of where to specify 3.5 in the code.

Let’s move over to the terminal.

## Basic Setup

Set up your project folder by copying and pasting the code below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | mkdir terminal-chatbot |
|  | cd terminal-chatbot |

View the code on [Gist](https://gist.github.com/JessicaWachtel/5ec29b2daee155a5748639a3cebb31b7).

The next step is to create and activate a virtual [Python](https://thenewstack.io/python/) environment. We want to create a virtual environment because it provides a safe, isolated workspace. It keeps everything organized, predictable and conflict-free. We aren’t setting up a virtual environment because the chatbot itself may cause issues.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | python3 -m venv venv |
|  | source venv/bin/activate |

View the code on [Gist](https://gist.github.com/JessicaWachtel/0a1fcda01b0014dce74679f66c943dbe).

After this code, you should see (venv) in your terminal prompt.

Now it’s time to install the required packages. For this project, we’ll need `openai`, the official Python client library for interacting with OpenAI’s APIs. We’ll also need `python-dotenv`. `python-dotenv` lets your code automatically read `.env` variables. 

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | pip install openai python-dotenv |

View the code on [Gist](https://gist.github.com/JessicaWachtel/073c5672d3eea1bbd63b481a28cd0b83).

Let’s store our API key in a `.env` file. For this, we’re going to use nano.

Open nano.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

View the code on [Gist](https://gist.github.com/JessicaWachtel/eb482b5dbdb61a17ac8e81e18ed0997c).

Paste your key in:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | OPENAI\_API\_KEY=YOUR KEY HERE |

View the code on [Gist](https://gist.github.com/JessicaWachtel/16237ef842680b9065769ef5c16be1df).

You can save and exit nano using the following commands:

* `Ctrl + O` (the letter, not the number) to save.
* `Enter` to confirm.
* `Ctrl + X` to exit.

## Create Chatbot Script

We’re going to use nano again to create the code file. There are other ways to do this, but I like nano. If you prefer a text file or something else, please feel free to use that.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

View the code on [Gist](https://gist.github.com/JessicaWachtel/19eb572cfe91b5ad3a27116d2c42b701).

Once your file is open, paste all the code in the next few sections into the file. I broke them up here to explain what each block is doing, but they are all part of the same file.

Import our dependencies:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | # -\*- coding: utf-8 -\*- |
|  | import os |
|  | from openai import OpenAI |
|  | from dotenv import load\_dotenv |

View the code on [Gist](https://gist.github.com/JessicaWachtel/0f4114e0a0efba77acedd625b510640d).

Then we want to load our environment variables and create the OpenAI API client:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | # load variables from .env file |
|  | load\_dotenv() |
|  |  |
|  | # create OpenAI API client |
|  | client = OpenAI(api\_key=os.getenv("OPENAI\_API\_KEY")) |

View the code on [Gist](https://gist.github.com/JessicaWachtel/1908502d8364509c32c0fb6fc757d390).

Now we’re ready to add our connection to ChatGPT. The function `connect_to_gpt` will send the current conversation to ChatGPT and return ChatGPT’s reply as plain text. This allows you to have a consistent conversation where it “remembers” the context and what’s already been shared.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def connect\_to\_gpt(history): |
|  | response = client.chat.completions.create( |
|  | model="gpt-4", # Change to "gpt-3.5" if you have a free account |
|  | messages=history |
|  | ) |
|  | return response.choices[0].message.content |

View the code on [Gist](https://gist.github.com/JessicaWachtel/38b121bc4913bed7200f24703784a2a3).

The following line means “if you run this file directly” (not import it as a module), run the code below. It will let you know when the chatbot is ready by printing, “Let’s get started! Type ‘exit’ to quit.\n”

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def connect\_to\_gpt(history): |
|  | response = client.chat.completions.create( |
|  | model="gpt-4", # Change to "gpt-3.5" if you have a free account |
|  | messages=history |
|  | ) |
|  | return response.choices[0].message.content |

View the code on [Gist](https://gist.github.com/JessicaWachtel/342211d50c626c7ab5a05475ea15be9b).

The next code is part of the loop that powers your chat session. It initializes the conversation as an empty list called `chat_history`. This is what stores the conversation and allows ChatGPT to have context based on what’s already been discussed.

The infinite loop `while True` keeps the conversation going until they quit. It also reads user input and checks to see if the user has exited.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | chat\_history = [] # stores conversation history for normal chat |
|  |  |
|  | while True: |
|  | user\_input = input("You > ").strip() |
|  |  |
|  | if user\_input.lower() in {"exit", "quit"}: |
|  | print("Goodbye!") |
|  | break |

View the code on [Gist](https://gist.github.com/JessicaWachtel/6a128c1b25ebf646f385000713401f6a).

The next bit of code checks to see if the user wants an answer in code form. If the user input starts with `/cmd` or `/code`, the chatbot will reply using code. 

The system message is an instruction for the AI. By typing, “You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations,” you guide the AI to give focused, concise answers. 

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | #if user wants a reply in code |
|  | if user\_input.startswith("/code") or user\_input.startswith("/cmd"): |
|  | prompt = user\_input.split(" ", 1)[1] if " " in user\_input else "" |
|  | system\_message = { |
|  | "role": "system", |
|  | "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations." |
|  | } |

View the code on [Gist](https://gist.github.com/JessicaWachtel/e65c5bb4f34756f9dc402fcd36a1b28e).

The next bit of code builds the request to send to OpenAI and prints the reply.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | # prepare messages with system instructions + user prompt |
|  | messages = [ |
|  | system\_message, |
|  | {"role": "user", "content": prompt} |
|  | ] |
|  | reply = connect\_to\_gpt(messages) |
|  | print(f"Chatbot > {reply}\n") |

View the code on [Gist](https://gist.github.com/JessicaWachtel/fa61a93e4f15f175d13ddda1655b1f79).

The following code handles normal chat mode, when the user doesn’t want a code reply.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | #regular conversation |
|  | else: |
|  | chat\_history.append({"role": "user", "content": user\_input}) |
|  | reply = connect\_to\_gpt(chat\_history) |
|  | print(f"Chatbot > {reply}\n") |
|  | chat\_history.append({"role": "assistant", "content": reply}) |

View the code on [Gist](https://gist.github.com/JessicaWachtel/a3d8518b967e0522d6c0dc8ccd1df536).

You can save an exit nano using the following commands:

* `Ctrl + O` (the letter, not the number) to save.
* `Enter` to confirm.
* `Ctrl + X` to exit.

Here is the full code file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | # -\*- coding: utf-8 -\*- |
|  | import os |
|  | from openai import OpenAI |
|  | from dotenv import load\_dotenv |
|  |  |
|  | # load variables from .env file |
|  | load\_dotenv() |
|  |  |
|  | # create OpenAI API client |
|  | client = OpenAI(api\_key=os.getenv("OPENAI\_API\_KEY")) |
|  |  |
|  | def connect\_to\_gpt(history): |
|  | response = client.chat.completions.create( |
|  | model="gpt-4", # Change to "gpt-3.5" if you have a free account |
|  | messages=history |
|  | ) |
|  | return response.choices[0].message.content |
|  |  |
|  | if \_\_name\_\_ == "\_\_main\_\_": |
|  | print("Terminal Chatbot Ready! Type 'exit' to quit.\n") |
|  |  |
|  | chat\_history = [] # stores conversation history for normal chat |
|  |  |
|  | while True: |
|  | user\_input = input("You > ").strip() |
|  |  |
|  | if user\_input.lower() in {"exit", "quit"}: |
|  | print("Goodbye!") |
|  | break |
|  |  |
|  | if user\_input.startswith("/code") or user\_input.startswith("/cmd"): |
|  | prompt = user\_input.split(" ", 1)[1] if " " in user\_input else "" |
|  | system\_message = { |
|  | "role": "system", |
|  | "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations." |
|  | } |
|  |  |
|  | # prepare messages with system instructions + user prompt |
|  | messages = [ |
|  | system\_message, |
|  | {"role": "user", "content": prompt} |
|  | ] |
|  | reply = connect\_to\_gpt(messages) |
|  | print(f"Chatbot > {reply}\n") |
|  |  |
|  | #regular conversation |
|  | else: |
|  | chat\_history.append({"role": "user", "content": user\_input}) |
|  | reply = connect\_to\_gpt(chat\_history) |
|  | print(f"Chatbot > {reply}\n") |
|  | chat\_history.append({"role": "assistant", "content": reply}) |

View the code on [Gist](https://gist.github.com/JessicaWachtel/9e671a02c11f586d34ee9fc06e7d0245).

You can run the chatbot using this command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

View the code on [Gist](https://gist.github.com/JessicaWachtel/96633956a356f5b05dda6d13fb877e08).

Test it out! Try asking for code: /code bash command to list all .txt files recursively.

Or just ask it a question in plain English. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)