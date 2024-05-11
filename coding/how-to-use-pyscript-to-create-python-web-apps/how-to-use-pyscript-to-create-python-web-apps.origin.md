# How To Use Pyscript To Create Python Web Apps
![Featued image for: How To Use Pyscript To Create Python Web Apps](https://cdn.thenewstack.io/media/2024/05/40cb9c0f-line-1184810_1280-1024x690.jpg)
When considering web development, most likely you automatically think of
[JavaScript](https://thenewstack.io/javascript/). There’s a good reason for that, as JS is one of the most popular languages on the market. One of the reasons JavaScript is so popular is that it can run natively within a web browser, so no extra runtimes are required.
But then came
[WebAssembly](https://thenewstack.io/webassembly/), which is a low-level assembly-like language that uses a compact binary format and near-native performance to allow languages like C, [C++](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/), [Rust](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/), and [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) to run on the web.
That doesn’t mean, however, you can simply write traditional Python code and have it run within a web browser. To make it happen, you have to
[employ PyScript](https://thenewstack.io/python-in-the-browser-free-pyscript-saas-launches/). With the help of [PyScript](https://pyscript.net/), you can develop rich frontends with Python for the web and even make use of various Python modules, such as [NumPy](https://numpy.org/).
PyScript provides a simple and clean API, pluggable and extendable components, and extended support for HTML. Although PyScript isn’t intended to replace JavaScript, it’s a great addition to your developer toolkit.
I want to show you how PyScript makes this possible, by demonstrating how to create a simple Hello, World! application that runs within a web browser.
## What You’ll Need
I’m going to demonstrate this on an instance of Ubuntu Server 22.04, that way you’ll have an Apache web server at your disposal. You’ll also need a text editor and a web browser. To install Apache, you’ll also need a user with sudo privileges.
That’s it. Let’s get to work.
## Installing Apache
The first thing we’re going to do is install Apache. To do that, log int your Ubuntu Server instance, and issue the following command:
*sudo apt-get install apache2 -y*
When the above command finishes, Apache should be up and running. You can verify this by opening a web browser and pointing it to http://SERVER (where SERVER is the IP address of the hosting server). You should see the Apache Welcome page.
## Creating Your HTML File
Now that the server is up and running, you can create the HTML file that will house the PyScript code. First, let’s create a basic HTML file with the command:
*sudo nano /var/www/html/pyscript.html*
The content of the basic file looks like this:
*<!DOCTYPE html>*
*<html lang=”en”>*
*<head>*
* <title>New Stack: PyScript</title>*
*</head>*
*<body>*
* <body>Hello, World!</body>*
*</body>*
*</html>*
Save and close the file. If you point your web browser to http://SERVER/pyscript.html, you’ll see
*Hello, World!* printed out. That’s great, but that’s straight-up HTML. How do we do this with PyScript?
Let’s open the pyscript.html file for editing again with:
*sudo nano/var/www/html/pyscript.html*
The first thing we’re going to do is Link PyScript to our HTML file. Without this linkage, our pyscript.html file wouldn’t have access to the PySript interface.
For this, we add two lines at the bottom of the <head> section. The first line links to a CSS file from pyscript.net and looks like this:
*<link rel=”stylesheet” href=”https://pyscript.net/alpha/pyscript.css” />*
If you open that file in your browser (with the address
[https://pyscript.net/alpha/pyscript.css](https://pyscript.net/alpha/pyscript.css)), you notice it is a rather long style sheet.
In the next line we’ll add links to the pyscript.js JavaScript file which looks like this:
*<script defer src=”https://pyscript.net/alpha/pyscript.js”></script>*
Our <head> section now looks like this:
*<head>*
* <meta charset=”UTF-8″>*
* <title>New Stack: PyScript</title>*
* <link rel=”stylesheet” href=”https://pyscript.net/alpha/pyscript.css” />*
* <script defer src=”https://pyscript.net/alpha/pyscript.js”></script>*
*</head>*
Finally, we have to add the code that will print the Hello, New Stack! message within the browser page.
If you recall, the Python code for printing out a string of characters is simply:
|
1
|
print("Hello, New Stack!")
Run the above and you’ll see the correct output.
How we add that code into our HTML file is with the line:
*<body> <py-script> print(“Hello, New Stack!!”) </py-script> </body>*
Within the <body></body> tags, we use the <py-script></py-script> tags to indicate our code.
Now, our entire HTML file looks like this:
*<!DOCTYPE html>*
*<html lang=”en”>*
*<head>*
* <meta charset=”UTF-8″>*
* <title>New Stack: PyScript</title>*
* <link rel=”stylesheet” href=”https://pyscript.net/alpha/pyscript.css” />*
* <script defer src=”https://pyscript.net/alpha/pyscript.js”></script>*
*</head>*
*<body>*
* <body> <py-script> print(“Hello, New Stack!!”) </py-script> </body>*
*</body>*
*</html>*
Save and close the file. Refresh the page within your browser and you’ll see the runtime do its thing and eventually print out “Hello, New Stack!” on the page.
Let’s have some fun. We’ll create a simple web app that translates English into Pirate Speech.
For this, we need to create three files:
- pirate.html – the main file that includes our HTML and Pyscript code.
- pyscript.json – informs the browser of certain configurations for the app.
- main.py – defines the behavior of the application.
Create the pirate.html file and paste the following contents:
*<!DOCTYPE html>*
*<html>*
* <head>*
* <meta charset=”utf-8″ />*
* <meta name=”viewport” content=”width=device-width,initial-scale=1″ />*
* <title>Pirate Speak PyScript</title>*
* <link rel=”stylesheet” href=”https://pyscript.net/releases/2024.1.1/core.>*
* <script type=”module” src=”https://pyscript.net/releases/2024.1.1/core.js>*
* </head>
*<body>
<p>Type an English phrase and click Translate</p>
<input type=”text” id=”english” placeholder=”Type English here…” />
<button py-click=”translate_english”>Translate</button>
<div id=”output”></div>
<script type=”py” src=”./main.py” config=”./pyscript.json”></script>
</body>
</html>
As you can see, we’ve linked a stylesheet and the JavaScript core in the <head> section and called our main.py and pyscript.json files within the <body> section. We’ve also added an input section that allows users to type in a phrase to be translated.
Create the pyscript.json file and paste the following content:
*{*
* “packages”: [“arrr”]*
*}*
What this file does is call arrr.py, which is the
[Python arr package](https://arrr.readthedocs.io/en/latest/).
Finally, create the main.py file and add the following:
*import arrr*
*from pyscript import document* *def translate_english(event):*
* input_text = document.querySelector(“#english”)*
* english = input_text.value*
* output_div = document.querySelector(“#output”)*
* output_div.innerText = arrr.translate(english)*
The first two lines define what we’re importing. The next block defines a function named
*translate_english()* that takes the inputted text and translates it from English to arrr speak.
All three of these files should be placed in the /var/www/html/ directory. For a larger project, you’d want to add them to their own directory.
Once you’ve saved all the files, point your web browser to http://SERVER/pirate.html. You should see
*Type an English Phrase and click Translate*. Below that, you’ll find a text field and a Translate button. Type a phrase and click Translate and you’ll be returned with the Pirate Speak translation for the phrase you typed.
Arrr matey.
And that’s how you use PyScript with HTML to create simple Python web applications.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)