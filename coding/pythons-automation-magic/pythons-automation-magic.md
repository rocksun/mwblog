
<!--
title: Python的自动化魔法
cover: https://cdn.thenewstack.io/media/2025/03/601c3bf8-fachrizal-maulana-if2q10lld1m-unsplash.jpg
summary: Python自动化魔法！`os`模块轻松处理文件，`pandas`搞定Excel/CSV数据录入，`smtplib`实现邮件自动发送。`BeautifulSoup`助你网络抓取，`reportlab`一键生成PDF报告。告别重复劳动，拥抱高效`automation`！
-->

Python自动化魔法！`os`模块轻松处理文件，`pandas`搞定Excel/CSV数据录入，`smtplib`实现邮件自动发送。`BeautifulSoup`助你网络抓取，`reportlab`一键生成PDF报告。告别重复劳动，拥抱高效`automation`！

> 译自：[Python's Automation Magic](https://thenewstack.io/pythons-automation-magic/)
> 
> 作者：Jessica Wachtel

自动化是未来（也是现在）的趋势。一行自动化代码可以触发无数的操作——向 [CSV 文件](https://thenewstack.io/python-for-automating-apis-create-a-trivia-quiz-csv-file/) 添加数百万个数据点、重命名数千个文件，或者抓取网络以获取强大的信息。除了简化任务之外，自动化还降低了人为错误的风险，并显着提高了效率。[Python](https://thenewstack.io/python/) 以其自动化功能而闻名，它提供了各种内置方法和函数，以及丰富的库和工具生态系统，所有这些都旨在简化和增强任务自动化。

Python 可以自动化哪些内容，涉及哪些库？

## 文件处理

自动化的文件处理消除了开发人员手动重命名、移动或组织文件的需要。自动化文件处理可以节省时间，并且有助于有效地管理日志、报告和备份。

`os` 模块（Python 原生）提供了与操作系统交互的函数，例如处理文件和目录。

在下面的代码示例中，使用的自动化函数是 `rename()`。`rename()` 来自 `os` 模块，写作 `os.rename(old_path, new_path)`。这会自动重命名文件夹中每个带有给定前缀和编号的文件。其余代码循环遍历文件夹中的所有文件，并将 `rename()` 应用于每个文件。

```py
import os

def rename_files(folder_path, prefix):
    for count, filename in enumerate(os.listdir(folder_path)):  
        old_path = os.path.join(folder_path, filename)  
        new_path = os.path.join(folder_path, f"{prefix}_{count}.txt")  
        os.rename(old_path, new_path)  
        print(f"Renamed {old_path} -> {new_path}")

rename_files("C:/Users/YourName/Documents", "report")
```

## 数据录入（Excel 或 CSV）

手动将数据输入到电子表格中既耗时又容易出错。自动化此过程可确保准确性并节省宝贵的时间。

`pandas` 是一个数据分析库，提供了处理结构化数据的强大工具，例如 CSV 和 [Excel](https://thenewstack.io/excel-sharpies-gather-in-vegas-for-spreadsheet-showdown/) 文件。`pandas` 不是 Python 原生的，必须安装。
在此示例中执行自动化的方法是 `to_csv()`，写作 `df.to_csv(file_path, index=False)`。此方法自动将修改后的 [DataFrame](https://thenewstack.io/pandas-a-vital-python-tool-for-data-scientists/) 写入 CSV 文件，从而无需手动编辑。其余代码读取现有的 CSV，添加一列，然后将更新后的数据写回文件。

```py
import pandas as pd  

def add_column_to_csv(file_path, column_name, values):
    df = pd.read_csv(file_path)  
    df[column_name] = values  
    df.to_csv(file_path, index=False)  
    print(f"Updated {file_path} with new column: {column_name}")

add_column_to_csv("C:/path/to/your_file.csv", "new_column", [1, 2, 3, 4, 5])
```

## 自动发送电子邮件

我不认识任何想再发送电子邮件的人。手动发送电子邮件可能很乏味，对于定期报告或通知来说几乎是不可能的。自动化电子邮件可以提高效率，并从您的待办事项列表中删除该项目。

`smtplib` 模块允许 Python 使用 [SMTP](https://thenewstack.io/how-to-write-your-own-email-server-in-rust/)（简单邮件传输协议）发送电子邮件。

在此示例中执行自动化的方法是 `sendmail()`，写作 `server.sendmail(sender_email, to_email, msg.as_string())`。这会自动发送电子邮件，无需人工干预。示例正文的其余代码创建电子邮件消息并连接到邮件服务器。

```py
import smtplib  
from email.mime.text import MIMEText  

def send_email(sender_email, sender_password, to_email, subject, body):
    msg = MIMEText(body)  
    msg["Subject"] = subject  
    msg["From"] = sender_email  
    msg["To"] = to_email  

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)  
        server.sendmail(sender_email, to_email, msg.as_string())  
        print("Email sent successfully!")

send_email("your_email@gmail.com", "your_password", "recipient_email@gmail.com", "Test Subject", "This is the body of the email.")
```

## 网络抓取

我不确定手动网络抓取会是什么样子。幸运的是，我们不必担心这一点，因为我们可以自动化。自动化网络抓取允许用户快速收集大量数据。

`BeautifulSoup` 是一个网络抓取库，用于从 HTML 和 XML 文档中提取数据。`BeautifulSoup` 不是 Python 原生的，必须安装。
这里自动化任务的函数是 `soup.find_all()`，写作 `soup.find_all("h2")`。这会从网页中提取所有 `<h2>` 标题，从而无需手动复制它们。此示例中包含的其他代码加载网页的内容并解析它以获取所需的数据。

```py
import requests  
from bs4 import BeautifulSoup  

def scrape_headings(url):
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, "html.parser")  
    headings = [h2.text for h2 in soup.find_all("h2")]  
    print("Headings found:", headings)

scrape_headings("https://example.com")
```

## 自动化报告（PDF 生成）

手动生成报告可能导致结果不一致。以一种一劳永逸的方式来处理报告生成要容易得多。它不仅使任务更容易，而且还确保了一致性和效率。

`reportlab` 允许 Python 以编程方式生成 PDF。`reportlab` 不是 Python 原生的，必须安装。

这里自动化该过程的方法是 `canvas.drawString()`，写作 `c.drawString(100, 750, text)`。这会自动将文本放置到 PDF 上。代码的提示构建一个新的 PDF 文件并保存它。

```py
from reportlab.pdfgen import canvas  

def create_pdf(file_path, text):
    c = canvas.Canvas(file_path)  
    c.drawString(100, 750, text) 
    c.save()  
    print(f"PDF created: {file_path}")

create_pdf("output.pdf", "Hello, this is your PDF!")
```

## 最后的想法

自动化是一个游戏规则改变者。在当今快节奏的世界中，多任务处理已成为常态，从您的待办事项列表中删除即使是一项任务也是一种胜利。只需几行代码，您不仅可以简化任务，还可以更快、更少错误地执行它。Python 提供了内置功能，并受到庞大的第三方工具生态系统的支持，使自动化比以往任何时候都更容易。