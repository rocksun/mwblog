# How to Use JSON In Your Python Code
![Featued image for: How to Use JSON In Your Python Code](https://cdn.thenewstack.io/media/2024/09/00feadeb-getty-images-wy-8vsqrj5w-unsplash-1-1024x683.jpg)
If you’re familiar with [containers](https://thenewstack.io/containers/), you probably are also familiar with [JSON](https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/). If not, JSON is fairly straightforward to understand. JSON stands for [JavaScript Object Notation](https://thenewstack.io/an-introduction-to-json/) and it serves as a syntax for storing and exchanging data. JSON is especially handy for data that is sent to a web page from a server.

The basic structure of JSON is name/value pairs, separated by commas with objects held by curly braces, and arrays wrapped in brackets. It looks like this:

1234567 |
{"students":[ {"firstName":"Olivia", "lastName":"Nightingale", "year":"senior"}, {"firstName":"Anton", "lastName":"Frank", "year":"sophomore"}, {"firstName":"Jean", "lastName":"Barber", "year":"freshman"}]} |
The breakdown looks like this:
- “firstName”:”Olivia” is a key/value pair
*{“firstName”:”Olivia”, “lastName”:”Nightingale”, “year”:”senior”}*is an object*“students”:[*
* {“firstName”:”Olivia”, “lastName”:”Nightingale”, “year”:”senior”},*
* {“firstName”:”Anton”, “lastName”:”Frank”, “year”:”sophomore”},*
* {“firstName”:”Jean”, “lastName”:”Barber”, “year”:”freshman”}*
*] *is an array.
But how do we use JSON within our [Python](https://thenewstack.io/python/) code? Fortunately, there’s a library that makes this possible. Said library is *json* and can be imported with the line:

1 |
import json |
Easy.
To use JSON in [Python](https://thenewstack.io/python/), you’ll want to know how to covert JSON to Python and Python to JSON. Let’s first examine how these two things are done.

## Convert JSON to Python
Let’s take a JSON string and convert it within a simple block of Python code. To do this, we have to use the *json.loads()* function. After our *import json* line, we’ll define x with some JSON key/value pairs, like this:

1 |
x = '{ "firstName":"Olivia", "lastName":"Nightingale", "year":"senior"}' |
Notice we had to wrap the object in single quotes. If we don’t do that, Python will report an error.
Next, we parse the JSON object (as “y”) with the json.loads() function like this:

1 |
y = json.loads(x) |
Finally, we print out a single element from the object with:
1 |
print(y["year"]) |
The entire code looks like this:
1234567 |
import jsonx = '{ "firstName":"Olivia", "lastName":"Nightingale", "year":"senior"}'y = json.loads(x)print(y["year"]) |
The output from the above block of code will be:
*senior*
## Convert Python to JSON
We can also do the opposite by converting a Python object to a JSON string. This time around, we use the *json.dumps() *function.

Let’s use a similar example to what we did above. We’ll define x with a Python dictionary (dict) like this:

12345 |
x = { "name": "Olivia Nightingale", "age": "17", "year": "senior"} |
We then define “y” using the *json.dumps() *function, like this:
1 |
y = json.dumps(x) |
Let’s print the results with:
1 |
print(y) |
The entire block of code looks like this:
1234567891011 |
import jsonx = { "name": "Olivia Nightingale", "age": "17", "year": "senior"}y = json.dumps(x)print(y) |
The output of the above code will be in the form of a JSON object that looks like this:
*{“name”: “Olivia Nightingale”, “age”: “17”, “year”: “senior”}*
With the json library, you can covert the following objects into their JSON equivalent:

- dic
- list
- tuple
- str
- int
- float
- True
- False
- None
It’s important to understand that JSON values are limited to the following:

- object – collection of key-value pairs
- array – a list of values contained within square brackets
- string – text contained in double quotes
- number – integers or floating point numbers
- boolean – true or false
- null – a null value
Let me demonstrate how to convert each of the above with a single block of code:

123456789101112131415 |
import jsonx = { "name": "Olivia", "age": "20", "graduated": False, "married": False, "majors": ("Theatre", "Communications") "minors": None, "vehicles": [ {"type": "bicycle", "color": "pink"}, {"type": "car", "make": "Mini Cooper"} ]}print(json.dumps(x)) |
The output of the above would be:
*{“name”: “Olivia”, “age”: “20”, “graduated”: false, “married”: false, “majors”: [“Theatre”, “Communications”], “minors”: null, “vehicles”: [{“type”: “bicycle”, “color”: “pink”}, {“type”: “car”, “make”: “Mini Cooper”}]}*
That’s looks ugly. Let’s do some formatting. With *json.dumps()*, you can define indention and separators. Let’s indent by 5 and use the . and = separators, which is done in the *print* line like so:

1 |
print(json.dumps(x, indent=5, separators=(". ", " = "))) |
The output now looks like this:
*{
*
*“name” = “Olivia”.*
*“age” = “20”.*
*“graduated” = false.*
*“married” = false.*
*“majors” = [*
*“Theatre”.*
*“Communications”*
*].*
*“minors” = null.*
*“vehicles” = [*
*{*
*“type” = “bicycle”.*
*“color” = “pink”*
*}.*
*{*
*“type” = “car”.*
*“make” = “Mini Cooper”*
*}*
*]*
*}*
That’s better.

We can also order the results with the *json.dumps()* function and the *sort_keys *parameter. That line looks like this:

1 |
print(json.dumps(x, indent=5, separators=(". ", " = "), sort_keys=True)) |
Our output now looks like:
*{
*
*“age” = “20”.*
*“graduated” = false.*
*“majors” = [*
*“Theatre”.*
*“Communications”*
*].*
*“married” = false.*
*“minors” = null.*
*“name” = “Olivia”.*
*“vehicles” = [*
*{*
*“color” = “pink”.*
“type” = “bicycle”
* }.
*
*{*
*“make” = “Mini Cooper”.*
*“type” = “car”*
*}*
*]*
*}*
We can also write a JSON file from [Python code](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/), which can be very handy (especially when you need to pass data from a Python app to a web app that requires JSON formatting. Let’s use our example above and write the data to the file “students.json”. The code looks like this:

12345678910111213141516 |
import jsonx = { "name": "Olivia", "age": "20", "graduated": False, "married": False, "majors": ("Theatre", "Communications") "minors": None, "vehicles": [ {"type": "bicycle", "color": "pink"}, {"type": "car", "make": "Mini Cooper"} ]}with open("students.json", mode="w", encoding="utf-8") as write_file: json.dump(x, write_file) |
The above code wouldn’t print any output to the terminal but instead would write the output to the file “students.json”. Open the file for viewing and you’ll see the data is in JSON format.
And there you have it, my Python learning friends: how you can easily use JSON in your Python code or convert data from Python to JSON. This feature will come in handy as you dive further down the Python rabbit hole.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)