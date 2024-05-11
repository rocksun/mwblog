## 如何使用 Pyscript 创建 Python Web 应用

![如何使用 Pyscript 创建 Python Web 应用的特色图片](https://cdn.thenewstack.io/media/2024/05/40cb9c0f-line-1184810_1280-1024x690.jpg)

在考虑 Web 开发时，你很可能会自动想到 [JavaScript](https://thenewstack.io/javascript/). 这有充分的理由，因为 JS 是市场上最流行的语言之一。JavaScript 如此流行的原因之一是它可以在 Web 浏览器中本机运行，因此无需额外的运行时。

但随后出现了 [WebAssembly](https://thenewstack.io/webassembly/), 这是一种类似于低级汇编的语言，它使用紧凑的二进制格式和接近本机的性能，允许 C、[C++](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/), [Rust](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/) 和 [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 等语言在 Web 上运行。

然而，这并不意味着你可以简单地编写传统的 Python 代码并在 Web 浏览器中运行它。要实现这一点，你必须 [使用 PyScript](https://thenewstack.io/python-in-the-browser-free-pyscript-saas-launches/). 借助 [PyScript](https://pyscript.net/), 你可以使用 Python 为 Web 开发丰富的前端，甚至可以使用各种 Python 模块，例如 [NumPy](https://numpy.org/).

PyScript 提供了一个简单而干净的 API、可插入且可扩展的组件以及对 HTML 的扩展支持。虽然 PyScript 并非旨在取代 JavaScript，但它是你开发人员工具包的绝佳补充。

我想通过演示如何创建一个在 Web 浏览器中运行的简单 Hello, World! 应用程序，向你展示 PyScript 如何实现这一点。

## 你需要什么

我将在 Ubuntu Server 22.04 的实例上演示这一点，这样你就可以使用 Apache Web 服务器。你还需要一个文本编辑器和一个 Web 浏览器。要安装 Apache，你还需要一个具有 sudo 权限的用户。

就是这样。让我们开始吧。

## 安装 Apache

我们要做的第一件事是安装 Apache。为此，请登录你的 Ubuntu Server 实例，并发出以下命令：

```
sudo apt-get install apache2 -y
```

当上述命令完成后，Apache 应该已启动并正在运行。你可以通过打开一个 Web 浏览器并将其指向 http://SERVER（其中 SERVER 是托管服务器的 IP 地址）来验证这一点。你应该会看到 Apache 欢迎页面。

## 创建 HTML 文件

现在服务器已启动并正在运行，你可以创建将容纳 PyScript 代码的 HTML 文件。首先，让我们使用以下命令创建一个基本的 HTML 文件：

```
sudo nano /var/www/html/pyscript.html
```

基本文件的内容如下所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>New Stack: PyScript</title>
</head>
<body>
  <body>Hello, World!</body>
</body>
</html>
```

保存并关闭文件。如果你将 Web 浏览器指向 http://SERVER/pyscript.html，你将看到 *Hello, World!* 打印出来。这很好，但这只是直接的 HTML。我们如何使用 PyScript 来实现这一点？

让我们使用以下命令再次打开 pyscript.html 文件进行编辑：

```
sudo nano/var/www/html/pyscript.html
```

我们要做的第一件事是将 PyScript 链接到我们的 HTML 文件。如果没有此链接，我们的 pyscript.html 文件将无法访问 PySript 接口。

为此，我们在 <head> 部分的底部添加两行。第一行链接到 pyscript.net 中的 CSS 文件，如下所示：

```html
<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
```

如果你在浏览器中打开该文件（地址为 [https://pyscript.net/alpha/pyscript.css](https://pyscript.net/alpha/pyscript.css)），你会注意到它是一个相当长的样式表。

在下一行中，我们将添加指向 pyscript.js JavaScript 文件的链接，如下所示：

```html
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
```

我们的 <head> 部分现在如下所示：

```html
<head>
  <meta charset="UTF-8">
  <title>New Stack: PyScript</title>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
```

最后，我们必须添加将在浏览器页面中打印 Hello, New Stack! 消息的代码。

如果你还记得，用于打印字符串的 Python 代码很简单：

```python
print("Hello, New Stack!")
```

运行上述代码，你将看到正确的输出。

我们如何将该代码添加到 HTML 文件中，方法是使用以下行：

```html
<body> <py-script> print("Hello, New Stack!!") </py-script> </body>
```

在 <body></body> 标记内，我们使用 <py-script></py-script> 标记来指示我们的代码。

现在，我们的整个 HTML 文件如下所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>New Stack: PyScript</title>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
  <py-script> print("Hello, New Stack!!") </py-script>
</body>
</html>
```
### Corrected Markdown Text

* `<script defer src="https://pyscript.net/alpha/pyscript.js"></script>`
* `</head>`
* `<body>`
* `<body> <py-script> print("你好，New Stack!!") </py-script> </body>`
* `</body>`
* `</html>`

保存并关闭文件。在浏览器中刷新页面，您将看到运行时执行其操作，并最终在页面上打印出“你好，New Stack！”。

让我们找点乐子。我们将创建一个简单的网络应用程序，将英语翻译成海盗语。

为此，我们需要创建三个文件：

- pirate.html – 包含我们的 HTML 和 Pyscript 代码的主文件。
- pyscript.json – 向浏览器告知应用程序的某些配置。
- main.py – 定义应用程序的行为。

创建 pirate.html 文件并粘贴以下内容：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>海盗语 PyScript</title>
<link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core." />
<script type="module" src="https://pyscript.net/releases/2024.1.1/core.js">
</head>
<body>
<p>输入一个英语短语，然后点击翻译</p>
<input type="text" id="english" placeholder="在此输入英语…" />
<button py-click="translate_english">翻译</button>
<div id="output"></div>
<script type="py" src="./main.py" config="./pyscript.json"></script>
</body>
</html>
```

如您所见，我们在 `<head>` 部分链接了一个样式表和 JavaScript 核心，并在 `<body>` 部分调用了我们的 main.py 和 pyscript.json 文件。我们还添加了一个输入部分，允许用户输入要翻译的短语。

创建 pyscript.json 文件并粘贴以下内容：

```json
{
"packages": ["arrr"]
}
```

此文件的作用是调用 arrr.py，它是 [Python arr 包](https://arrr.readthedocs.io/en/latest/)。

最后，创建 main.py 文件并添加以下内容：

```python
import arrr
from pyscript import document

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
```

前两行定义了我们正在导入的内容。下一个块定义了一个名为 `translate_english()` 的函数，该函数获取输入的文本并将其从英语翻译成 arrr 语。

这三个文件都应放在 `/var/www/html/` 目录中。对于较大的项目，您需要将它们添加到自己的目录中。

保存所有文件后，将您的网络浏览器指向 `http://SERVER/pirate.html`。您应该看到 “输入一个英语短语，然后点击翻译”。在下面，您将找到一个文本字段和一个翻译按钮。输入一个短语并点击翻译，您将获得您输入的短语的海盗语翻译。

Arrr matey。

这就是使用 PyScript 和 HTML 创建简单的 Python Web 应用程序的方法。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。