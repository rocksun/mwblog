# Python for Automating APIs: Create a Trivia Quiz CSV File
![Featued image for: Python for Automating APIs: Create a Trivia Quiz CSV File](https://cdn.thenewstack.io/media/2024/07/cb8acd7b-trivia2-1024x575.png)
Technology is changing the scope of work, and automation is one way to do tasks faster with less time and effort.

With advanced tools and programming languages like Python, it is possible to learn to automate things like file operations, spreadsheets, email, file and directory management, and even work with different APIs to get desired information as structured data like JSON, XML, CSV (comma-separated value) and so on.

Developers are always looking for ways to improve and make the software development life cycle more efficient. Python, with its simple syntax and ability to process and handle complex tasks, is a handy tool for this purpose.

## The Role of Automation
Automation involves creating scripts and applications that automatically perform repetitive tasks without human intervention or assistance.

If you work with large datasets or do manual tasks to compute data, automation is valuable for:

- Software development
- Marketing professionals
- Data science
- Business analysts and financial analysts
The following guide will help you understand how to interact with APIs to take automation to the next level. It will also help you integrate an API into a program to fetch its data sources and generate a list of CSV trivia questions on demand, along with the answers, using the [Trivia API](https://opentdb.com/api_config.php).

## Setup and Installation
To ensure your scripts can handle connecting and retrieving information from websites and APIs (server), the Python `requests`
module is required:

`pip install requests`
The requests module is an HTTP library for exchanging information over the internet.

The other modules, `csv`
and `html`
come pre-installed as part of the Python standard library.

: This module creates a CSV file.**csv**
: This helps to decode or unescape html entities or ASCII characters into their original characters in plain text.**html**
## Building the Trivia QA Project
First, let’s set up the program by creating a file called main.py in any code editor you choose. This program will run in your terminal’s CLI.

Make sure the file is contained within a folder.

These three libraries will do all the work for the program, including sending the HTTP requests and writing the response to a CSV file.

Next, let’s prompt the user to do the following with the `input`
function:

This allows the user to enter the number of trivia questions they’d like to see

Also, prompt the user to specify the difficulty of the questions:

**Define the API endpoint**
Use the Open Trivia Database as shown in the URL variable:

## Set Up Request Parameters
Request parameters offer a structured way to send additional or optional information through key-value pairs that append to an API URL after the question mark. Therefore, the request parameter allows both the client and the server to have a more specific interaction, enabling the server to return data that is aligned more closely with what the client or user is looking for.

Define and set the following request parameters to the `request_params`
variable:

The value for each key in the `request_params`
represents information like amount, difficulty and category from the Trivia API. The category value set to “18” relates to the “Science: Computers” question category.

## Requesting JSON and Extracting the Data With Python
To fetch data from a web server, the `GET`
request is paired to the Trivia API using the `requests`
library:

The `response`
variable accepts the API URL, `headers`
that format the server’s data as JSON and the parameters dictionary.

To extract the trivia data, parse the response as JSON using the `.json`
method of the response object:

![Extracting data from Python for Trivia Quiz CSV File](https://cdn.thenewstack.io/media/2024/07/88878d65-image1a.jpg)
The resulting data

## Initialize a List
Initializing a list is important at this stage to hold the question-and-answer pairs later in the saved CSV.

The header row starts with Question and Answer.

## Looping Through the Trivia Data
Handling each item in the data is achieved using the `for loop`
as shown:

This arrangement helps to unescape the HTML entities in the question and answer using the `html.unescape`
method. For example, `< &`
will be converted to `<, &`
where such occurrence appears.

Also, if the question type is a Boolean, prepend `“True or False? “`
to the question.

Now, append each question and its correct answer to the list to create a new row using the `qna`
variable:

## Creating the CSV
The final step is to write the question-and-answer pairs to a CSV file named “tech_trivia.csv” with the code:

This code block opens the file in write mode with newline set to an empty string. Thereafter, use the writer method of the CSV library to create a CSV writer object and write the rows to the file using the `writerows`
method.

When the file is executed with the command `python main.py`
in the terminal, the message “File created” appears, signifying that the file was created!

## Conclusion
Automation has made simple tasks autonomous. For example, using Python code and API, you can generate a file populated with [trivia questions and answers](https://drive.google.com/file/d/1oFpW5WVlPlWxcIe8v_yJuPARGUDNzPcO/view).

With this knowledge, you can do a lot more by making boring tasks enjoyable, and everyone benefits without the need for manual data computation.

As technology evolves and businesses become more reliant on software, Python development has become one of the most in-demand skills in the job market. However, finding the right Python developer for your company can be daunting. Read this guide to navigate the [hiring process for a Python developer](https://www.andela.com/blog-posts/how-to-hire-a-python-developer-a-guide-to-finding-the-right-fit?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=hire-python-developers&utm_term=writers-room), including defining your project needs and evaluating and hiring candidates.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)