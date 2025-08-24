为什么要结合 [Python](https://thenewstack.io/what-is-python/) 和 [Excel](https://thenewstack.io/microsoft-puts-python-in-excel/)？ 简而言之，Python 消除了 Excel 内置公式的限制。Python 是应用程序开发人员最流行的语言之一，其原因同样适用于在 Excel 中使用 Python 的人。在 Excel 中使用 Python 将 Python 的高级分析库（`pandas`、`NumPy`）、自动化功能、数据可视化工具（`Matplotlib`）和可扩展性引入到 Excel 中。

## 前提条件和设置

### 安装 Python 和 `pip`

1. 从 [python.org](https://python.org) 下载最新版本的 Python。
2. 在安装过程中，选中“将 Python 添加到 PATH”的框。
3. 安装或升级 `pip`（Python 的包管理器）：

```
python -m ensurepip --upgrade
```

测试安装：

```
python --version
pip --version
```

输出：Python 和 pip 的最新版本

在您的机器上安装了最新版本的 Python 和 pip 之后，我们可以开始设置 Excel。

## 启用 Excel-Python 插件 (`xlwings`, `PyXll`)

### `xlwings`

`xlwings` 是一个免费的开源 Excel-Python 桥梁，允许您从 Excel 调用 Python 脚本。它非常适合自动化报告、清理数据和构建自定义函数，而无需 [Visual Basic for Applications (VBA)](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office))。

首先，使用终端在您的机器上安装：

```
pip install xlwings
```

然后从 Excel 启用它：

1. 打开 Excel，然后打开“开发工具”选项卡，然后打开“Excel 插件”，并选中“xlwings”。
2. 使用 `RunPython` 宏从单元格执行 Python 代码。

### `PyXLL`

`PyXLL` 是一种专业级（付费）Excel-Python 集成工具，专为生产环境而设计。它比 `xlwings` 更高级。它允许您在 Python 中创建自定义 Excel 函数，在工作簿打开时运行 [Python 代码](https://thenewstack.io/how-to-use-json-in-your-python-code/)，并与高级数据科学库集成。

1. 从 [pyxll.com](http://pyxll.com) 下载。
2. 安装并激活您的许可证。
3. 配置您的 `pyxll.cfg`（或 `.ini`）文件以设置 Python 路径和选项。
4. 重新启动 Excel 并直接从单元格开始使用 Python 函数。

使用 `xlwings` 进行免费、开源的 Excel 自动化和快速 Python 集成（例如，从 CSV 中提取数据，使用 pandas 清理数据并将其发送回 Excel）。选择 `PyXLL` 用于需要高性能、自定义函数和专业支持的高级生产级解决方案（例如，在 Excel 中创建具有实时计算的实时市场数据馈送）。

*本教程将使用 `xlwings` 而不是 `PyXLL`，因为 `xlwings` 是开源选项。*

### 尝试 Microsoft 365 “Excel 中的 Python”预览版

如果您需要立即访问 Excel 中的 Python 而无需任何安装，Microsoft 365 的“Excel 中的 Python”（测试版）非常有用。它不能真正替代 `xlwings` 或 `PyXLL`，因为这些工具具有更强大的功能。Microsoft 365 “Excel 中的 Python”的用例是：

* 任务简单或探索性。
* 在 Excel 中试验或学习 Python。

Microsoft 365 “Excel 中的 Python” 使您可以使用 `＝PY()` 函数立即访问 Python 库，如 `pandas` 和 `Matplotlib`。

如果您是 Microsoft 365 预览体验成员 Beta 频道的一部分，则可以试用该测试版。打开 Excel 并输入如下公式：

```
=PY("print('Hello from Python!')")
```

此函数将在单元格内运行。

## 从 Excel 运行 Python 代码

根据您的需求和偏好，有几种方法可以做到这一点。

### 内联 Python 单元格

使用 `＝PY()` 函数直接在 Excel 单元格中运行小型 Python 脚本。考虑轻量级计算和简单的数据转换。

```
=PY("sum([1, 2, 3, 4])")
```

### 用户自定义函数 (UDF)

[UDF](https://thenewstack.io/scylladbs-take-on-webassembly-for-user-defined-functions/) 是将 Python 逻辑集成到电子表格中的自定义函数。使用 `xlwings` 和 `PyXLL` 时，可以创建 UDF。UDF 非常适合实时数据集成、自定义财务计算以及数据验证和清理。

如何创建 UDF：

* 构建 Python 代码文件：
  + 打开文本编辑器或 IDE（例如，[VS Code，](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) [PyCharm](https://thenewstack.io/7-must-have-python-tools-for-ml-devs-and-data-scientists/)，Sublime 等）。
  + 保存一个新文件，例如 `py`。
  + 编写代码（例如，基本加法代码）。

```
import xlwings as xw


@xw.func
def add_numbers(a, b):
    return a + b
```

* 连接到 Excel（必须安装 `xlwings` 并在 Excel 中启用 `xlwings`）：
  + 在 Excel 的 `xlwings` 设置中，将插件指向您的 `udfs.py` 文件。
* 从 Excel 调用它：
  + 在任何单元格中，键入在 `py` 中定义的函数名称。

```
=add_numbers(5, 10)
```

Excel 将运行 Python 代码并返回 15。

### VBA 到 Python 的互操作性

如果您已经在使用 VBA 宏，则可以使用它们通过 `xlwings` 或 `PyXLL` 触发 Python 脚本。这允许您将 Python 引入 VBA 工作流程，而无需从头开始重建所有内容。

与上面的 UDF 示例类似，您需要安装 `xlwings`（或 `PyXLL`，具体取决于您使用的工具）并在 Excel 中启用 `xlwings`。

**创建 Python 代码文件**

该文件需要包含一个 `main()` 函数来匹配 VBA 调用。让我们将文件命名为 `vba_file.py`。

```
def main():
    print("Yay Python code")
```

在 `xlwings` 设置（或 VBA 代码中）配置路径，以确保 Python 知道脚本的位置。

在 Excel 中运行 VBA 宏时，它将使用 `xlwings`（或 `PyXLL`）。Python 执行代码后，可以将结果发送回 Excel 或用于更新工作簿。

## 数据分析工作流程

这些工作流程不会使用内联代码。它们将与上面的 UDF 示例密切相关（但并非所有这些函数都是 UDF）。这意味着您必须在 Excel 中将 `xlwings` 指向 Python 脚本文件的名称，或使用 VBA `RunPython` 调用正确配置它。

### 使用 `pandas` 导入数据

使用 `pandas` 库导入和分析 Excel 文件中的数据。下面的示例从 Excel 文件中读取数据，执行基本分析并将结果写回工作簿。

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

### 使用 `Matplotlib` 可视化

`Matplotlib` 是一种数据可视化工具。下面的示例从 Excel 文件中读取数据，生成条形图，将其保存为图像，并将图表插入到工作簿中。

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

下面的机器学习 (ML) 示例使用 `pandas` 来处理 Excel 数据，并使用 `joblib` 来加载预先训练的模型以进行预测。这些工具协同工作以从 Excel 文件加载数据。然后，它应用预先训练的模型来预测结果并将结果写回工作簿。

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

## 从 Python 读取和写入 Excel 文件

`openpyxl` 和 `xlsxwriter` 是用于处理 Excel 文件的流行 Python 库。

### `openpyxl` 基础

当您需要读取或修改现有 Excel 文件时，`openpyxl` 是一个很棒的工具。考虑编辑电子表格、使用公式、读取数据。

`openxyl` 可以处理磁盘上的 Excel 文件，这意味着它可以从计算机上保存的 `.xlsx` 文件读取或写入数据。您不需要 `xlwings` 就可以做到这一点。

下面的示例打开一个文件，更新它并保存更改。

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

### `xlswriter` 基础

`xlswriter` 创建具有高级格式和图表的新 Excel 文件。它不能修改现有文件。考虑从头开始生成报告或文件。

`xlswriter` 是一个独立的 Python 库。它将文件直接写入磁盘，但不与打开的 Excel 应用程序交互。

下面的示例创建一个格式化的 Excel 文件。

```
import xlsxwriter


workbook = xlsxwriter.Workbook('output_xlsxwriter.xlsx')
worksheet = workbook.add_worksheet()


worksheet.write('A1', 'Hello Excel with XlsxWriter')


workbook.close()
```

### 样式和条件格式

样式使报告在视觉上更具吸引力且更易于阅读。

您可以使用 `openxl` 自定义 Excel 文件的外观。您可以设置颜色、字体和边框等内容。

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

条件格式根据单元格值自动突出显示趋势或重要数据。使用条件格式而不是样式来突出显示异常值、数据阈值或使分析更直观。

下面的条件格式突出显示所有大于 150 的单元格。

```
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill


red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')


ws.conditional_formatting.add('A2:A10',
                              CellIsRule(operator='greaterThan', formula=['150'], fill=red_fill))


wb.save("conditional_formatting.xlsx")
```

## 自动化报告和仪表板

自动化是开发人员喜欢 Python 的一个重要原因，它可以很好地转化为 Excel 用户。

### 调度脚本

对于以前调度过脚本的任何人来说，这是一个熟悉的工作流程。您可以简单地使用 Mac/Linux 的 cron 或 Windows 上的 Windows 任务计划程序。这将按设定的时间调度 Python 脚本。

### 通过电子邮件发送生成的工作簿

[SMTP](https://thenewstack.io/how-to-write-your-own-email-server-in-rust/) 和 Python 的内置 `smtplib` 库协同工作，以将您的工作簿作为电子邮件发送。它们允许您的 Python 脚本连接到电子邮件服务器并发送带有附件的电子邮件。此集成使您的 Excel 工作流程实现端到端自动化。

下面的示例将 Excel 文件作为电子邮件发送：

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

## 性能和安全注意事项

### 管理内存和大型数据集

与任何其他大型文件类似，当处理大型 Excel 文件时，如果一次将所有内容加载到内存中，性能可能会迅速下降。由于这些 Excel 文件通常非常大，因此以下是一些提示：

* **分块读取文件：** `pandas` 有很好的工具可以做到这一点，例如 `pandas.read_csv(..., chunksize=50000)` 和 `pandas.read_excel()`。这将有助于以较小的部分处理数据，减少内存并防止崩溃。
* **利用数据库：** 您可以将繁重的数据处理或聚合卸载到数据库（SQL、Postgres），而不是使用 Python。然后，您可以将汇总或筛选的数据提取到 Python 中以进行分析或报告。
* **避免不必要的副本：** 除非绝对必要，否则在处理 DataFrames 时，优先使用就地操作而不是深度复制。

### 沙盒和宏安全性

在 Excel 中运行 Python 脚本和宏会带来安全风险，尤其是在文件来自未知或不受信任的来源时。以下是一些提示：

* **验证和扫描文件：** 在运行 Excel 文件之前，始终扫描 Excel 文件中是否存在恶意宏或嵌入式脚本。
* **使用虚拟环境：** 在公司或共享环境中，在隔离的虚拟环境（`venv` 或 `conda`）中运行 Python 代码，以包含依赖项并降低系统范围影响的风险。
* **限制宏设置：** 配置 Excel 的宏安全设置，以禁用或提示在运行来自不受信任来源的宏之前。

## 结论

阅读本教程后，您就可以很好地开始在 Excel 中使用 Python。虽然我们只了解了 Python 和 Excel 可以一起完成的工作的表面，但这肯定是一个开始。现在，您可以更智能地工作、处理更大的数据并创建比以往任何时候都更具洞察力的电子表格。