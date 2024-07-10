# 使用 Python 自动化 API：创建琐事问答 CSV 文件

![使用 Python 自动化 API：创建琐事问答 CSV 文件的特色图片](https://cdn.thenewstack.io/media/2024/07/cb8acd7b-trivia2-1024x575.png)

技术正在改变工作范围，自动化是更快地完成任务，减少时间和精力的方式之一。

借助 Python 等高级工具和编程语言，可以学习自动化诸如文件操作、电子表格、电子邮件、文件和目录管理等操作，甚至可以与不同的 API 交互以获取所需信息，例如 JSON、XML、CSV（逗号分隔值）等结构化数据。

开发人员一直在寻找方法来改进软件开发生命周期并使其更高效。Python 凭借其简单的语法和处理复杂任务的能力，是实现此目的的便捷工具。

## 自动化的作用

自动化涉及创建脚本和应用程序，这些脚本和应用程序可以在没有人为干预或协助的情况下自动执行重复性任务。

如果您处理大型数据集或执行手动任务来计算数据，自动化对于以下方面很有价值：

- 软件开发
- 营销专业人员
- 数据科学
- 商业分析师和财务分析师

以下指南将帮助您了解如何与 API 交互，将自动化提升到一个新的水平。它还将帮助您将 API 集成到程序中，以获取其数据源并根据需要生成 CSV 琐事问题列表以及答案，使用 [Trivia API](https://opentdb.com/api_config.php)。

## 设置和安装

为了确保您的脚本能够处理与网站和 API（服务器）的连接和检索信息，需要 Python `requests` 模块：

```bash
pip install requests
```

requests 模块是一个用于通过互联网交换信息的 HTTP 库。

其他模块，`csv` 和 `html` 作为 Python 标准库的一部分预先安装。

- 此模块创建 CSV 文件。**csv**
- 这有助于将 HTML 实体或 ASCII 字符解码或取消转义为纯文本中的原始字符。**html**

## 构建琐事问答项目

首先，让我们通过在您选择的任何代码编辑器中创建一个名为 main.py 的文件来设置程序。此程序将在您的终端的 CLI 中运行。

确保该文件位于文件夹中。

这三个库将完成程序的所有工作，包括发送 HTTP 请求并将响应写入 CSV 文件。

接下来，让我们使用 `input` 函数提示用户执行以下操作：

```python
num_questions = int(input("请输入您想要查看的琐事问题的数量： "))
```

这允许用户输入他们想要查看的琐事问题的数量。

此外，提示用户指定问题的难度：

```python
difficulty = input("请输入问题的难度（easy、medium 或 hard）： ")
```

**定义 API 端点**

使用 Open Trivia Database，如 URL 变量所示：

```python
api_endpoint = "https://opentdb.com/api.php"
```

## 设置请求参数

请求参数提供了一种结构化方式，通过附加到 API URL 问号后的键值对来发送附加信息或可选信息。因此，请求参数允许客户端和服务器进行更具体的交互，使服务器能够返回更符合客户端或用户需求的数据。

将以下请求参数定义并设置为 `request_params` 变量：

```python
request_params = {
    "amount": num_questions,
    "difficulty": difficulty,
    "category": 18,
    "type": "multiple",
    "encode": "url3986"
}
```

`request_params` 中每个键的值代表 Trivia API 中的信息，例如数量、难度和类别。设置为“18”的类别值与“科学：计算机”问题类别相关。

## 使用 Python 请求 JSON 并提取数据

为了从 Web 服务器获取数据，`GET` 请求与 Trivia API 配对，使用 `requests` 库：

```python
response = requests.get(api_endpoint, headers={"Accept": "application/json"}, params=request_params)
```

`response` 变量接受 API URL、`headers`（将服务器的数据格式化为 JSON）和参数字典。

要提取琐事数据，请使用响应对象的 `.json` 方法将响应解析为 JSON：

```python
trivia_data = response.json()
```

![从 Python 提取琐事问答 CSV 文件的数据](https://cdn.thenewstack.io/media/2024/07/88878d65-image1a.jpg)

生成的数据

## 初始化列表

在此阶段初始化列表对于稍后在保存的 CSV 中保存问答对很重要。

标题行以问题和答案开头。

```python
qna = [["问题", "答案"]]
```

## 循环遍历琐事数据

使用 `for loop` 处理数据中的每个项目，如下所示：

```python
for item in trivia_data["results"]:
    question = html.unescape(item["question"])
    answer = html.unescape(item["correct_answer"])

    if item["type"] == "boolean":
        question = "True or False? " + question

    qna.append([question, answer])
```

此安排有助于使用 `html.unescape` 方法取消转义问题和答案中的 HTML 实体。例如，`< &` 将转换为 `<, &`，其中出现此类情况。

此外，如果问题类型是布尔值，请在问题前面加上“True or False?”。

现在，使用 `qna` 变量将每个问题及其正确答案附加到列表中以创建一个新行：

## 创建 CSV

最后一步是使用以下代码将问答对写入名为“tech_trivia.csv”的 CSV 文件：

```python
with open("tech_trivia.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(qna)
```

```python
print("琐事问答 CSV 文件已成功创建！")

This code block opens the file in write mode and sets the newline character to an empty string. After that, it uses the CSV library's writer method to create a CSV writer object and uses the `writerows` method to write rows to the file.

When the file is executed using the command `python main.py` in the terminal, the message "File created" will be displayed, indicating that the file has been created!

## Conclusion
Automation makes simple tasks autonomous. For example, using Python code and APIs, you can generate a file containing [trivia questions and answers](https://drive.google.com/file/d/1oFpW5WVlPlWxcIe8v_yJuPARGUDNzPcO/view).

With this knowledge, you can do more by making tedious tasks enjoyable, everyone will benefit from it without having to manually calculate data.

As technology continues to evolve, businesses are increasingly reliant on software, and Python development has become one of the most sought-after skills in the job market. However, finding the right Python developer for your company can be a daunting task. Read this guide to learn about [the process of hiring Python developers](https://www.andela.com/blog-posts/how-to-hire-a-python-developer-a-guide-to-finding-the-right-fit?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=hire-python-developers&utm_term=writers-room), including defining your project requirements and evaluating and hiring candidates.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss a beat. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)