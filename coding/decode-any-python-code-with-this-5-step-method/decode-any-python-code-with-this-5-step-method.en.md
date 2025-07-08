Being able to read others’ code is essential for maintaining, improving and collaborating on any meaningful software project. It’s rare to write all the original code in an application yourself, and even rarer for an application to be completely rewritten from scratch. More likely, your workflow will involve working with code that was written by someone else (who may no longer be available to explain it) and iterated on by others (who also might be out of reach) long before it ever appears on your screen.

This makes reading and understanding existing code just as important as writing it yourself. Without knowing what’s going on, line by line, character by character, you won’t be able to [debug](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/), enhance features, evolve a product or collaborate effectively with anyone. Sometimes the code is neat, organized and well-documented. Sometimes less so. Your ability to make sense of it shouldn’t depend on how polished it is.

In this tutorial, we’ll walk through a small application with unclear naming. Using a checklist as our guide, we’ll take it step by step to decode what’s going on.

The file below is called `script.py`:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | import json |
|  | from collections import defaultdict |
|  |  |
|  | def f1(path): |
|  | with open(path, 'r') as f: |
|  | return json.load(f) |
|  |  |
|  | def f2(items): |
|  | result = defaultdict(list) |
|  | for i in items: |
|  | k = i.get('category', 'Unknown') |
|  | result[k].append(i) |
|  | return result |
|  |  |
|  | def f3(d): |
|  | out = {} |
|  | for k, v in d.items(): |
|  | s = sum(x['value'] for x in v) |
|  | m = s / len(v) |
|  | out[k] = m |
|  | return out |
|  |  |
|  | def runner(): |
|  | data = f1('data.json') |
|  | grouped = f2(data) |
|  | stats = f3(grouped) |
|  | for k, v in stats.items(): |
|  | print(f"{k}: {v:.2f}") |
|  |  |
|  | if \_\_name\_\_ == '\_\_main\_\_': |
|  | runner() |

View the code on [Gist](https://gist.github.com/JessicaWachtel/ee7f77b7b7d6c86e9b0bf660ae14c907).

This file is `data.json`:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | [ |
|  | {"category": "A", "value": 10}, |
|  | {"category": "B", "value": 20}, |
|  | {"category": "A", "value": 30}, |
|  | {"category": "C", "value": 40}, |
|  | {"category": "B", "value": 25} |
|  | ] |

View the code on [Gist](https://gist.github.com/JessicaWachtel/4ffb4be4acc9e66767b88fb1317e23fe).

## We’ll Use a 5-Step Checklist To Identify What This Code Is Doing

### Item 1: What Does the Program Do Overall?

Uncovering the program’s big-picture purpose provides the blueprint to understanding its details.

A good place to start is by looking for its main function and seeing how the other functions interact with it. In our example, `runner()` is the main function. We can tell it’s the main function because it calls `f1`, `f2` and `f3`, respectively. 

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def runner(): |
|  | data = f1('data.json') |
|  | grouped = f2(data) |
|  | stats = f3(grouped) |
|  | for k, v in stats.items(): |
|  | print(f"{k}: {v:.2f}") |

View the code on [Gist](https://gist.github.com/JessicaWachtel/f6edf4ed8451453c725cc881bda1aa33).

In `runner()`, we can interpret the following workflow:

* f1(‘data.json’) is the very first thing that happens.
* f2(data) processes the data returned by f1.
* f3(grouped) processes the result of f2.
* Finally, it loops over stats.items() and prints something formatted like a number ({v:.2f}).

We can also make the reasonable conclusion that:

`f1` loads data (we can tell this by `json.load()`).

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def f1(path): |
|  | with open(path, 'r') as f: |
|  | return json.load(f) |

View the code on [Gist](https://gist.github.com/JessicaWachtel/d12ceff15dd0e4d535365d312d975b4b).

`f2` groups or reorganizes it using `defaultdict(list)` and `append(i)` per category.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def f2(items): |
|  | result = defaultdict(list) |
|  | for i in items: |
|  | k = i.get('category', 'Unknown') |
|  | result[k].append(i) |
|  | return result |

View the code on [Gist](https://gist.github.com/JessicaWachtel/aa17a7557e1c5f465ba8513b4dd1f84a).

`f3` computes numeric summaries or aggregates using `sum(...)` and dividing by `len(v)`.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | def f3(d): |
|  | out = {} |
|  | for k, v in d.items(): |
|  | s = sum(x['value'] for x in v) |
|  | m = s / len(v) |
|  | out[k] = m |
|  | return out |

View the code on [Gist](https://gist.github.com/JessicaWachtel/e93e6bd733cac38f95fdc98a1505698a).

The loop prints results:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | for k, v in stats.items(): |
|  | print(f"{k}: {v:.2f}") |

View the code on [Gist](https://gist.github.com/JessicaWachtel/e23562f318014799e94af69abdd08816).

We’re ready to answer the next question…

### Item 2: How Is the Code Organized?

Understanding the structure tells you where to look for each piece of logic.

A great starting point for understanding how code is organized is to look for imports, functions and entry points.

The top of the file identifies imports:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | import json |
|  | from collections import defaultdict |

View the code on [Gist](https://gist.github.com/JessicaWachtel/7956d303dfb7b82f1653e45c31d23de1).

This means our script is using functionality from other modules. Through understanding the imports, you can anticipate data types or methods used in the code.

You can identify functions by looking for lines that start with `def`. Breaking the code into functions helps you read and understand one piece at a time.

You can identify the entry point in this special block near the bottom of the script:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | if \_\_name\_\_ == '\_\_main\_\_': |
|  | runner() |

View the code on [Gist](https://gist.github.com/JessicaWachtel/770291ad825b69ab7f53958892da75ab).

Understanding where the program begins helps you trace the flow from start to finish. This means when you run the script directly (`python script.py`), [Python](https://thenewstack.io/python/) runs the code inside this block. The function or code called here (`runner()` in this case) is the starting point of execution.

In our example, the script imports `json` and `defaultdict`, so you can expect it to handle [JSON](https://thenewstack.io/how-to-use-json-in-your-python-code/) data and perform grouping operations. It defines the functions `f1`, `f2`, `f3` and `runner()`. Building off of what we learned in the last section, this suggests the code is organized into modular tasks such as file reading, data processing and running the main logic.

The entry point calls `runner()`, indicating that this function is the main routine coordinating the program’s execution.

### Item 3: What Are the Main Inputs and Outputs?

Understanding what goes into the program (input) and what comes out (output) helps you mentally frame what the script is doing at a high level.

Here’s how to find the inputs.

Look at the first function called in `runner()`: `data = f1(‘data.json’)`. This tells us the following:

* The script reads from a file called `data.json`.
* If we peek inside `f1()`, we see it uses `json.load(f)`, which confirms the input is a JSON-formatted file.
* The actual contents (in `data.json`) are a list of dictionaries, each with a `category` and a `value` field.
* This structured input is parsed into a [Python list](https://thenewstack.io/python-for-beginners-lists/) of dictionaries, each dictionary representing a single data point.

Here’s how to find the outputs.

This loop is at the end of `runner()`:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | for k, v in stats.items(): |
|  | print(f"{k}: {v:.2f}") |

View the code on [Gist](https://gist.github.com/JessicaWachtel/4b91e92856c9c0a8f3a888d5c344f9f0).

The loop prints each key (likely a category name) and a floating-point number with two decimal places. Based on the earlier functions, we can infer that this is the average value for each category.

Example output from this loop:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | A: 20.00 |
|  | B: 22.50 |
|  | C: 40.00 |

View the code on [Gist](https://gist.github.com/JessicaWachtel/736e559e37236bfeb0876013cc0cd1cd).

This confirms the script is summarizing values by category and printing the results.

From all these details, we can understand the inputs and outputs. The main input is a JSON file containing a list of items, each with a category and a value. The output is plain text printed to the console (specifically, a summary showing the average value for each category).

### Item 4: How Does Data Flow Through Functions?

Tracing how data moves and changes step by step is one of the most important ways to understand what code does. It helps you see not just what each function does in isolation, but how they work together to transform input into output.

Let’s follow the data through each function in the order it’s called.

`f1('data.json')`

*The input is `data.json`*

The function opens the file called `data.json` in read mode. It uses `json.load()` to parse the contents. The result is returned as a list of dictionaries like this (`json.load()` always outputs dictionaries and lists).

*Output:*

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | [ |
|  | {"category": "A", "value": 10}, |
|  | {"category": "B", "value": 20}, |
|  | {"category": "A", "value": 30}, |
|  | {"category": "C", "value": 40}, |
|  | {"category": "B", "value": 25} |
|  | ] |

View the code on [Gist](https://gist.github.com/JessicaWachtel/340738cd3abacd5691fd513a5b77d7e1).

*This then becomes the input for `f2`.*

`f2(items)`

This function creates an empty `defaultdict` with lists as the default value. It loops over every dictionary in the list returned by `f1`. It looks up the `’category’` key for each item. If no category exists, it returns `’Unknown’`. It then appends the entire dictionary to the corresponding category’s list.

*Output:*

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | { |
|  | 'A': [ |
|  | {"category": "A", "value": 10}, |
|  | {"category": "A", "value": 30} |
|  | ], |
|  | 'B': [ |
|  | {"category": "B", "value": 20}, |
|  | {"category": "B", "value": 25} |
|  | ], |
|  | 'C': [ |
|  | {"category": "C", "value": 40} |
|  | ] |
|  | } |

View the code on [Gist](https://gist.github.com/JessicaWachtel/2f42c8590d6e5d201f019a6dbed3400b).

*This data becomes the input for `f3`.*

`f3(d)`

This function takes the grouped dictionary from `f2`. It creates an empty dictionary called `out`. In each key-value pair, `k` is the category and `v` is the list of items in that category.

It computes the following:

* `s = sum(x['value'] for x in v)`: The total of all `value` fields
* `m = s / len(v)`: The average

It stores the average in `out[k]`.

*Output:*

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | { |
|  | 'A': 20.0, |
|  | 'B': 22.5, |
|  | 'C': 40.0 |
|  | } |

View the code on [Gist](https://gist.github.com/JessicaWachtel/eb5f53922130b0b3c16277edef13e503).

*It becomes the variable `stats` in `runner()`, which is then printed.*

`runner()`

`runner()` calls `f1`, `f2` and `f3` in their proper sequence. It receives the final dictionary of averages. It then loops over `stats.items()` and prints each category and its average, formatted to 2 decimal places.

*Output:*

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | A: 20.00 |
|  | B: 22.50 |
|  | C: 40.00 |

View the code on [Gist](https://gist.github.com/JessicaWachtel/a9f0fe8d2b964d503932b2feff814085).

What does this mean?

Following the data through each function shows you the progressive transformation:

The raw JSON list becomes grouped by category, which becomes averaged per category, and is finally printed as summaries.

To work through this on your own and see what any function returns, add `print()` statements after each call:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | print("Data loaded:", data) |
|  | print("Grouped data:", grouped) |
|  | print("Computed stats:", stats) |

View the code on [Gist](https://gist.github.com/JessicaWachtel/056a6b14d7b369bc93602f2d6e03b15f).

### Item 5: Run the Code and See What Happens

Running the script is the quickest way to validate your mental model of what the code is doing. You can do this step really at any time in this process. Running the code also helps you catch missing files, date format problems and all other unexpected errors.

How to run this file:

1. Make sure you saved your script as `script.py`.
2. Make sure your `data.json` file is in the same folder as `script.py`.
3. Open your terminal or command prompt.
4. Navigate to the folder containing both files.
5. Run: `python script.py`.

Actual output:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | A: 20.00 |
|  | B: 22.50 |
|  | C: 40.00 |

View the code on [Gist](https://gist.github.com/JessicaWachtel/d6455197df334f13d3c07247e24c1979).

When the expected output matches the actual output, it confirms that you don’t have any errors and your environment is set up correctly. It also confirms you have the correct understanding of what the code is doing.

### Helpful Tips

Here are some things you can do in addition to the checklist to aid in your understanding of code:

* Use tools to inspect variables. Inspecting variables lets you see exactly what’s in memory.
* Make notes and diagrams based on the code. Notes and diagrams help you keep track of relationships between data structures.
* Learn which libraries are being used. Understanding libraries helps you know what helpers are available.

And finally: Be patient! Even experienced developers take time to decode unclear names.

## Conclusion

Reading someone else’s Python code, especially when names are unclear, can be challenging, especially at first. But by breaking it down step by step, you can turn confusing scripts into something you fully understand.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)