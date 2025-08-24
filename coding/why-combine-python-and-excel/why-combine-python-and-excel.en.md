Why should you combine [Python](https://thenewstack.io/what-is-python/) and [Excel](https://thenewstack.io/microsoft-puts-python-in-excel/)? In short, Python removes the limitations set by Excel’s built-in formulas. The same reasons why Python is one of the most popular languages for application developers apply to those working with Python in Excel. Working with Python in Excel brings Python’s advanced analytics libraries (`pandas`, `NumPy`), automation capabilities, data visualization tools (`Matplotlib`) and scalability to Excel.

## Prerequisites and Setup

### Installing Python and `pip`

1. Download the latest version of Python from [python.org](https://python.org).
2. During installation, check the box for “Add Python to PATH.”
3. Install or upgrade `pip` (Python’s package manager):

```
python -m ensurepip --upgrade
```

Test the installation:

```
python --version
pip --version
```

Output: Most recent version of Python and pip

Once you have recent versions of Python and pip installed on your machine, we can move over to setting up Excel.

## Enabling Excel-Python Add-Ins (`xlwings`, `PyXll`)

### `xlwings`

`xlwings` is a free, open source Excel-Python bridge allowing you to call Python scripts from Excel. It’s ideal for automating reports, cleaning data and building custom functions without [Visual Basic for Applications (VBA)](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office).

First, install on your machine using the terminal:

```
pip install xlwings
```

Then enable it from Excel:

1. Open Excel, then Developer Tab, then Excel Add-Ins, and check “xlwings.”
2. Use the `RunPython` macro to execute Python code from a cell.

### `PyXLL`

`PyXLL` is a professional-grade (paid) Excel-Python integration tool designed for production environments. It’s more advanced than `xlwings`. It allows you to create custom Excel functions in Python, run [Python code](https://thenewstack.io/how-to-use-json-in-your-python-code/) when workbooks open and integrate with advanced data science libraries.

1. Download from [pyxll.com](http://pyxll.com).
2. Install and activate your license.
3. Configure your `pyxll.cfg` (or `.ini`) file to set Python paths and options.
4. Restart Excel and start using Python functions directly from cells.

Use `xlwings` for free, open source Excel automation and quick Python integrations (e.g., pulling data from a CSV, cleaning it with pandas and sending it back to Excel). Choose `PyXLL` for advanced, production-grade solutions that require high performance, custom functions and professional support (e.g., creating a live market data feed in Excel with real-time calculations).

*This tutorial will use `xlwings` over `PyXLL` since `xlwings` is the open source option.*

### Trying Microsoft 365 “Python in Excel” Preview

Microsoft 365’s “Python in Excel” (beta) is great in cases where you need immediate access to Python inside Excel without any installs. It’s not a true replacement for `xlwings` or `PyXLL` as those tools have more robust functionalities. Use cases for Microsoft 365 “Python in Excel” are:

* Tasks are simple or exploratory.
* Experimenting or learning Python in Excel.

Microsoft 365 “Python in Excel” gives you immediate access to Python libraries like `pandas` and `Matplotlib` using the `=PY()` function.

You can try the beta if you’re part of the Microsoft 365 Insiders Beta Channel. Open Excel and enter a formula like this:

```
=PY("print('Hello from Python!')")  
```

This function will run inside the cell.

## Running Python Code From Excel

There are a few ways to do this based on your needs and preferences.

### Inline Python Cells

Run small Python scripts using the `=PY()` function directly inside Excel cells. Think lightweight calculations and simple data transformations.

```
=PY("sum([1, 2, 3, 4])")  
```

### User-Defined Functions (UDFs)

[UDFs](https://thenewstack.io/scylladbs-take-on-webassembly-for-user-defined-functions/) are custom functions that integrate Python logic into spreadsheets. You can create UDFs when using `xlwings` and `PyXLL`. UDFs are great for real-time data integration, custom financial calculations and data validation and cleaning.

How to create a UDF:

* Build a Python code file:
  + Open a text editor or IDE (e.g., [VS Code,](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) [PyCharm](https://thenewstack.io/7-must-have-python-tools-for-ml-devs-and-data-scientists/), Sublime, etc.).
  + Save a new file, for example `py`.
  + Write the code (e.g., basic addition code).

```
import xlwings as xw


@xw.func
def add_numbers(a, b):
    return a + b
```

* Connect to Excel (must have `xlwings` installed and `xlwings` enabled in Excel):
  + Point the add-in to your `udfs.py` file in the `xlwings` settings in Excel.
* Call it from Excel:
  + In any cell, type the function name as defined in `py`.

```
=add_numbers(5, 10)
```

Excel will run the Python code and return 15.

### VBA-To-Python Interoperability

If you’re already using VBA macros, you can leverage them to trigger Python scripts using `xlwings` or `PyXLL`. This allows you to introduce Python to your VBA workflow without rebuilding everything from scratch.

Similar to the UDF example above, you need to have `xlwings` installed (or `PyXLL` depending on which tool you’re using) and `xlwings` enabled in Excel.

**Create a Python code file**

The file needs to contain a `main()` function to match the VBA call. Let’s call the file `vba_file.py`.

```
def main():
    print("Yay Python code")
```

Configure the path in `xlwings` settings (or in your VBA code) to make sure Python knows where your script is located.

When you run the VBA macro inside Excel, it will use `xlwings` (or `PyXLL`). After Python executes the code, the results can be sent back into Excel or used to update your workbook.

## Data Analysis Workflows

These workflows will not use inline code. They will follow closely along with the UDF example above (but not all these functions are UDFs). That means you’ll have to point `xlwings` to the name of your Python script file in Excel or configure it properly using your VBA `RunPython` calls.

### Importing Data With `pandas`

Use the `pandas` library to import and analyze data from Excel files. The example below reads data from an Excel file, performs basic analysis and writes the results back to the workbook.

```
import pandas as pd
import xlwings as xw


def analyze_and_write():
    # Connect to the calling Excel workbook
    wb = xw.Book.caller()       
    sheet = wb.sheets[0]


    # Step 1: Read data from a local Excel file 
    df = pd.read_excel("sales.xlsx")


    # Step 2: Analyze data
    summary = df.describe()


    # Step 3: Write the summary statistics back into Excel, starting at cell A10
    sheet.range('A10').options(index=True).value = summary
```

### Visualizing With `Matplotlib`

`Matplotlib` is a data visualization tool. The example below reads data from an Excel file, generates a bar chart, saves it as an image and inserts the chart into the workbook.

```
import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw


def create_and_insert_chart():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]


    # read data 
    df = pd.read_excel("sales.xlsx")


    # create  bar chart for 'Revenue' column
    df['Revenue'].plot(kind='bar')
    plt.title('Monthly Revenue')
    plt.tight_layout()
    plt.savefig('revenue_chart.png')  # Save chart as image file
    plt.close()


    # insert chart  into Excel sheet at cell E2
    sheet.pictures.add('revenue_chart.png', left=sheet.range('E2').left, top=sheet.range('E2').top)
```

The machine learning (ML) example below uses `pandas` to handle Excel data and `joblib` to load the pre-trained model for making predictions. The tools work together to load data from the Excel file. It then applies a pre-trained model that predicts outcomes and writes results back to the workbook.

```
import pandas as pd
import xlwings as xw
from joblib import load


def predict_and_write():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]


    # load data for prediction
    df = pd.read_excel("sales.xlsx")


    # load pre-trained ML model
    model = load('model.joblib')


    # predict using selected features
    predictions = model.predict(df[['feature1', 'feature2']])


    # write predictions back to Excel starting at cell D2
    sheet.range('D2').options(index=False, header=False).value = predictions
```

## Reading and Writing Excel files From Python

`openpyxl` and `xlsxwriter` are popular Python libraries for working with Excel files.

### `openpyxl` Basics

`openpyxl` is a great tool for when you need to read or modify existing Excel files. Think editing spreadsheets, working with formulas, reading data.

`openxyl` works with Excel files on disk, meaning it reads from or writes to `.xlsx` files saved on your computer. You don’t need `xlwings` for this.

The example below opens a file, updates it and saves the changes.

```
from openpyxl import load_workbook


# Load an existing workbook
wb = load_workbook("existing_file.xlsx")


# Select the active worksheet (or specify by name: wb['Sheet1'])
ws = wb.active


# Modify a cell value
ws['A1'] = 'Updated Hello Excel'


# Save changes back to the file (can overwrite or save as new file)
wb.save("existing_file.xlsx")
```

### `xlswriter` Basics

`xlswriter` creates new Excel files with advanced formatting and charts. It can’t modify existing files. Think generating a report or file from scratch.

`xlswriter` is a standalone Python library. It writes files directly to disk but does not interact with an open Excel application.

The example below creates a formatted Excel file.

```
import xlsxwriter


workbook = xlsxwriter.Workbook('output_xlsxwriter.xlsx')
worksheet = workbook.add_worksheet()


worksheet.write('A1', 'Hello Excel with XlsxWriter')


workbook.close()
```

### Styling and Conditional Formatting

Styling makes reports visually appealing and easier to read.

You can use `openxl` to customize your Excel file’s appearance. You can set things like colors, fonts, and borders.

```
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side


wb = Workbook()
ws = wb.active


# write some data
ws['A1'] = "Sales"
ws['A2'] = 100
ws['A3'] = 250


# wet font color and bold
ws['A1'].font = Font(color="FF0000", bold=True)


# set cell fill color (yellow)
ws['A2'].fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")


# set thin border around cell A3
thin_border = Border(left=Side(style='thin'),
                     right=Side(style='thin'),
                     top=Side(style='thin'),
                     bottom=Side(style='thin'))
ws['A3'].border = thin_border


wb.save("styled.xlsx")
```

Conditional formatting highlights trends or important data automatically based on cell values. Use conditional formatting over styling to feature outliers, data thresholds or to make analysis more intuitive.

The conditional formatting below highlights all cells greater than 150.

```
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill


red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')


ws.conditional_formatting.add('A2:A10',
                              CellIsRule(operator='greaterThan', formula=['150'], fill=red_fill))


wb.save("conditional_formatting.xlsx")
```

## Automating Reports and Dashboards

Automation is a huge reason why developers love Python, and it translates well to Excel users.

### Scheduling Scripts

This is a familiar workflow for anyone who’s scheduled scripts before. You can simply use the cron for Mac/Linux or the Windows Task Scheduler on Windows. This will schedule Python scripts at set times.

### Emailing Generated Workbooks

[SMTP](https://thenewstack.io/how-to-write-your-own-email-server-in-rust/) and Python’s built-in `smtplib` library work together to send your workbooks as an email. They allow your Python script to connect to an email server and send emails with attachments. This integration makes your Excel workflows end-to-end automated.

The example below sends an Excel file as an email:

```
import smtplib
from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = 'Automated Report'
msg['From'] = 'you@example.com'
msg['To'] = 'team@example.com'
msg.set_content('Please see attached report.')


with open('report.xlsx', 'rb') as f:
    msg.add_attachment(f.read(),
                       maintype='application',
                       subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                       filename='report.xlsx')


with smtplib.SMTP('smtp.example.com') as s:
    s.login('user', 'password')
    s.send_message(msg)
```

## Performance and Security Considerations

### Managing Memory and Large Datasets

Similar to any other large file, when working with large Excel files, performance can degrade quickly if you load everything into memory at once. Since these Excel files are usually pretty large, here are some tips:

* **Read files in chunks:** `pandas` has good tools for this, like `pandas.read_csv(..., chunksize=50000)` and `pandas.read_excel()`. This will help process the data in smaller portions, reduce memory and prevent crashes.
* **Leverage databases:** You can offload heavy data processing or aggregation to a database (SQL, Postgres) instead of using Python. Then you can fetch summarized or filtered data into Python for analysis or reporting.
* **Avoid unnecessary copies:** Favor in-place operations over deep copies unless absolutely necessary when working with DataFrames.

### Sandboxing and Macro Security

Running Python scripts and macros in Excel introduces security risks, especially if the files come from unknown or untrusted sources. Here are some tips:

* **Validate and scan files:** Always scan Excel files for malicious macros or embedded scripts before running them.
* **Use virtual environments:** In corporate or shared environments, run Python code inside isolated virtual environments (`venv` or `conda`) to contain dependencies and reduce the risk of system-wide impacts.
* **Restrict macro settings:** Configure Excel’s macro security settings to disable or prompt before running macros from untrusted sources.

## Conclusion

After reading this tutorial, you can be well on your way to working with Python in Excel. Though we only scratched the surface of what Python and Excel can do together, this is surely a start. Now you can work smarter, handle bigger data, and create more insightful spreadsheets than ever before.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)