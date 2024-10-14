# Working With JSON Data in Python
![Featued image for: Working With JSON Data in Python](https://cdn.thenewstack.io/media/2024/10/fd160d1f-claudio-schwarz-fyeoxvyviyy-unsplash-1-1024x683.jpg)
[JavaScript Object Notation (JSON)](https://thenewstack.io/an-introduction-to-json/) facilitates information sharing between applications. It’s the go-to choice for exchanging data between web clients and servers and for communication between [APIs](https://thenewstack.io/api-management/) and various services or data sources. JSON’s format is both machine-readable and human-friendly, making it easy to parse, generate, and understand. Its efficiency in reducing data transmission makes [JSON](https://thenewstack.io/how-to-convert-google-spreadsheet-to-json-formatted-text/) the go-to format for information sharing
**JSON is:**
**Lightweight:**JSON is minimalistic and efficient, making it suitable for transmitting data over networks.**Text-based:**JSON’s plain-text format is composed of readable characters and symbols. Though JSON is based on a subset of[JavaScript](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/), it’s language-independent and compatible with most[modern programming languages](https://thenewstack.io/the-fastest-programming-language-daves-garage-seeks-the-answer/).**Structured data:**JSON represents data as[key-value](https://thenewstack.io/akamai-brings-key-value-data-to-the-edge-adds-api-acceleration/)pairs, which can be organized in nested structures like objects (dictionaries) and lists.
Working with JSON data is a common occurrence when building and maintaining applications.

## JSON in the Real World
JSON performs the following tasks quickly and efficiently.

**API interaction:**[Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/)applications often send and receive responses in JSON.
Examples: weather data and stock data sharing**Data Storage:**JSON is used to store and share data within different parts of a system and across different systems.
Examples: configuration files and logs**Serialization and Deserialization:**JSON converts data structures into a string format (serialization) and then reconstructs them into their original form (deserialization). This process simplifies data sharing and interchange.
Examples: storing user preferences and the transmission of complex data objects
## Get Started: Working With JSON in Python Applications
Importing the `json`
module is the first step.

#### Parsing and Accessing JSON Data
#### Parsing data
Parsing JSON data converts JSON-encoded data (usually in string form) into a format that can be accessed within a programming environment. In Python applications, the JSON string is converted into native Python data structures like dictionaries and lists.

`json.loads()`
is the `json`
module’s data parsing function.
Output: {‘apple’: ‘red’, ‘banana’: ‘yellow’, ‘cucumber’: ‘green’, ‘types’: [‘fruit’, ‘vegetable’]}

The `json.loads()`
function is the same for both nested and unnested data.

#### Accessing Unnested Data
You can access the JSON data after parsing.

**Hardcoded:**
Output:
red
yellow
[‘fruit’, ‘vegetable’]

**Dynamic:**
39

#### Accessing nested data
Often, JSON data is nested. This means the data includes dictionaries or lists within other dictionaries or lists.

Nested data is incredibly common because it mirrors how data is organized in the real world. An example of nested data is a user profile on an e-commerce site that contains personal details, addresses, and a list of purchases, all with their own attributes.

Accessing nested JSON data requires a different code setup than unnested data.

**Hardcoded:**
Output:
Sarah Ellington
B+

**Dynamic:**
Working with nested data dynamically requires a recursive or iterative function. Though both work, recursive solutions are more elegant and slightly easier to read.

Output:

### Reading and Writing JSON Data to a File
#### Writing
`json.dumps()`
saves JSON data in a file. `json.dumps()`
converts Python objects into a JSON-formatted string, known as serializing the data. The serialized data is then written to a file or transmitted over a network. Writing nested and unnested data follows similar protocols.
**Unnested:**
**Nested:**
`open('data.json', 'w')`
opens `data.json`
in write mode. Write mode overwrites the file if it exists or creates a new file if it doesn’t.
#### Reading
Reading data differs between nested and unnested data. Since nested data is so common when in doubt, write a function that reads nested data. The `json`
module’s data reading function is `json.load(file)`
.

Here’s the unnested version just for reference and comparison.

### Pretty Printing
Pretty printing JSON data improves readability and simplifies debugging by formatting the data with indentation and line breaks. Pretty printing provides a clear, accessible format for shared data. This helps with documentation and collaboration.

The `indent`
parameter in the `json.dumps()`
function formats JSON data with the indentation. Pretty printing follows the same process for both nested and unnested data.

The number following `indent`
in the `json.dumps()`
function dictates how many spaces to indent. Four is fairly common though indent best practices can vary by system.

Output:

### Error Handling
JSON presents different exceptions depending on how you interact with the data, but in all cases, using `try…except`
blocks is the standard approach for handling errors when working with JSON.

Output:
Failed to decode JSON: Expecting property name enclosed in double quotes: line 1 column 29 (char 28)

For more on how to handle errors, check out our error-handling tutorial.

### Retrieving JSON Data from APIs
JSON is a common format for data transmitted through APIs, and the `requests`
library is frequently used to handle such data in Python.

Here’s an example of how to retrieve JSON data from an API with error handling:

## Conclusion
JavaScript Object Notation (JSON) is a fundamental tool for data interchange between applications. Its efficiency in reducing data transmission makes it the preferred choice for web clients, servers and API interactions. Understanding JSON’s capabilities and best practices, including proper error handling and pretty printing, are the first steps toward working efficiently in real-world scenarios.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)