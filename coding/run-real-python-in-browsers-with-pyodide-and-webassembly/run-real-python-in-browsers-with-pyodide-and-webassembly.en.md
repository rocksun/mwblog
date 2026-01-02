There are many ways to bring [Python](https://thenewstack.io/what-is-python/) to the browser (thanks, [WebAssembly](https://thenewstack.io/webassembly/webassembly-when-you-hate-rust-but-love-python/)). But there’s only one way to bring Python’s full functionality (really no compromises) to the browser: [Pyodide](https://pyodide.com/). Pyodide is a full Python runtime compiled to WebAssembly that allows you to run standard Python code directly in the browser. Yes, other tools exist, but the functionality has more limits than with Pyodide.

Pyodide is powerful because it’s a port of the [CPython](https://thenewstack.io/guido-van-rossums-ambitious-plans-for-improving-python-performance/) interpreter to WebAssembly (Wasm). Pyodide takes the standard CPython engine and re-engineers it to run inside a browser’s WebAssembly sandbox. This allows the browser to execute complex, real-world Python libraries at high speeds without needing any external servers or local installations. This means that, unlike smaller Python variants or transpilation approaches, when using Pyodide, you can:

* Run full Python in the browser.
* Support C-extension libraries like Pandas, NumPy and Matplotlib client-side.
* Run Python entirely client-side without any backend.
* Execute Python dynamically client-side.

Whereas with other Python-focused Wasm tools, you can’t. One small technical clarification: [PyScript](https://thenewstack.io/how-to-use-pyscript-to-create-python-web-apps/) brings the same functionality to the browser. PyScript is a framework that uses Pyodide as its backend. It adds an HTML/templating layer to the Pyodide runtime.

The beauty of Pyodide is that it doesn’t require a complex build system or a specialized environment. If you can write a standard HTML file, you can run Pyodide.

* **Zero installation:** You don’t need to install Python, manage virtual environments or pip-install a single thing. Everything happens within the browser the moment you load the page.
* **Minimal setup:** You can pull Pyodide into your project via a CDN link. Once loaded, you’re just one function call away from executing Python logic: `pyodide.runPython()`.
* **Direct communication:** Pyodide includes a powerful bridge between Python and JavaScript. You can pass data structures between the two languages seamlessly — for example, using JavaScript to fetch data and Python to analyze it with a specialized library.

Pyodide is a full-weight runtime. It downloads and executes the entire CPython engine directly on your device rather than using a ‘lite’ version or sending code to a server for processing. That makes it a solid choice for applications like privacy-first data tools, analysis, data processing and offline-capable applications.

To show you how to get started with Pyodide, we’re going to build an application that:

* Loads Python and Pandas in the browser with Pyodide.
* Accepts an uploaded CSV.
* Uses Python to:
  + Display the first rows of the dataset.
  + Populate a column selector.
  + Generate summary statistics.

And this all happens client-side!

I think it’s important to say you don’t need any project-specific tools or libraries installed on your machine to successfully execute this tutorial. You only need the following:

* Modern browser
* Internet connection
* Text editor or IDE
* CSV file (only if you want to see the full functionality of the project)

Because we’re working in the browser, the project code includes HTML, CSS and JavaScript, along with our Pyodide and Python code. All of our code will live in a single file, `index.html`. I’ll share the complete code file first and then provide detailed explanations of the Pyodide sections and how they work (HTML, CSS and [JavaScript](https://thenewstack.io/introduction-to-javascript/) are outside the scope of this tutorial).

`index.html`

## Working With Pyodide

The first time we encounter Pyodide in `index.html` is with the line below:

The code above downloads the Wasm version of Python. It also installs a Python interpreter inside the browser tab. Lastly, it exposes a JavaScript API (`loadPyodide`) that interacts with the interpreter.

Without this line of code, you can’t execute Python in the browser.

### Pyodide Boots Python and Installs Python Packages

The next thing we’ll need Pyodide to do is initialize the Python interpreter, create the Python execution environment and download/install compiled [Python packages](https://thenewstack.io/the-top-5-python-packages-and-what-they-do "Python packages") into the environment. The code below essentially replaces `python -m venv`, `pip install pandas` and any backend service needed to run Pandas. Think of it as Python loading in the browser.

### Pyodide Bridges JavaScript and Python Memory

Now we need JavaScript to call Python like a function. Without Pyodide, you would need an API request, backend endpoint or some other workaround. This is where Pyodide makes JavaScript and Python interoperable.

In the code below, Pyodide copies a JavaScript string into Python’s global namespace. This makes browser data available to Python without using serialization APIs or sending it over HTTP.

### Execute Python Code

`pyodide.runPython()`executes the Python code in the browser. It takes in Python code as a string, maintains Python state between executions and allows multiple Python calls to share variables and data. The string is made of standard Python code, not a Python/JavaScript hybrid.

The code below is what reads the CSV into a Pandas DataFrame, displays the first few rows, populates the column dropdown dynamically and calculates summary statistics. Pyodide allows Python to access the browser DOM, so all updates will happen directly on the page without any server or API calls.

The next code block, also using `pyodide.runPython()`, runs Python via Pyodide whenever the user selects a column from the dropdown. It checks if a column is selected, then extracts that column from the DataFrame and displays the first few values in the browser. If no column is selected, it clears the output. Pyodide allows Python to update the HTML directly, so the user sees the column data instantly without any server requests.

One important line that appears in both code blocks is `from js import document`. This makes JavaScript objects accessible in Python and allows Python to call browser APIs directly. With this line, Python can interact with the browser like a first-class language, updating the DOM and responding to actions without any server code.

### Pyodide Helps Python Drive the UI

There’s another piece of code in the Python string I want to point out:

This code updates the UI without switching languages. It does so by routing Python calls to JavaScript DOM methods and converting Python strings into JavaScript strings.

## Conclusion

Pyodide turns the traditional frontend architecture on its head! It embeds a persistent Python runtime in the browser and provides a two-way bridge between JavaScript and Python. With Pyodide, Python libraries like Pandas can run client-side and interact directly with the DOM. It brings functionality that used to require a full Python backend straight to the client. What will you build in the browser with Pyodide?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)