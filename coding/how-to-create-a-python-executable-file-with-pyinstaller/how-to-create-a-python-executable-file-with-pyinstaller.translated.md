# 如何使用 PyInstaller 创建 Python 可执行文件

![Featued image for: 如何使用 PyInstaller 创建 Python 可执行文件](https://cdn.thenewstack.io/media/2024/07/3fe1deff-emmanuel-ikwuegbu-_2alim-f6pw-unsplash-1-1024x684.jpg)

您已经花费时间创建了一个 [Python 应用程序](https://thenewstack.io/how-to-create-a-python-gui-app-with-pyqt5/)，您希望使用它或将其分发给可以从其强大功能中受益的人。您可能认为唯一的方法是将代码发送给他们，确保他们在机器上安装了 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/)（以及代码所需的任何依赖项），并指示他们使用命令 *python3 appname.py* 运行代码。

当然，这可以工作，但并不高效。如果您与可能不太了解 Python 的人共享应用程序，这可能会很麻烦。或者，即使他们了解 Python，您肯定也不希望将代码发送给他们并期望他们从命令行运行它。

相反，为什么不从您的 [Python 代码](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/) 创建一个可执行文件，这样用户只需双击它即可运行应用程序，或者将文件复制到其 $PATH 中的目录并从文件系统层次结构中的任何位置运行命令。

这就是我今天要向您展示如何做的事情。我们将使用我们之前创建的 Python 应用程序的代码（用于获取用户的输入并使用 [GUI](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/) 将其写入文件）并从中创建一个方便的可执行文件。

这是一种从 Python 代码创建便携式应用程序的好方法。目标机器唯一的要求是安装 Python（这是一个相当容易克服的障碍）。

好的，让我们开始吧。

## 您需要什么

要使此方法有效，您需要一台安装了 Python 的机器以及我们上次创建的示例代码。我会在这里添加代码，这样您就不必搜索它。我将在 Ubuntu 22.04 上演示此方法，但该过程适用于任何 Linux 发行版（或任何支持 Python 的操作系统）。如果您使用的是其他发行版或操作系统，则需要相应地调整 Pip 安装过程。

## 安装 Pip

要安装 PyInstaller，您必须首先确保安装了 Pip（Python 包管理器）。您可以使用以下命令检查 Pip 是否已安装：

```bash
pip –version
```

如果您在控制台中看到版本号，则说明您已准备好。如果您收到错误，则需要安装 Pip，这可以通过以下命令完成：

```bash
sudo apt-get install python3-pip -y
```

当上述命令完成后，您就可以继续了。

## 安装 PyInstaller

接下来，我们需要安装 PyInstaller，它会读取您的 Python 代码，发现您的应用程序运行所需的每个模块和库，收集所有必要的东西（包括 Python 解释器），并将它们与您的代码组合成一个单独的文件夹或一个单独的可执行文件。

要安装 PyInstaller，请执行以下命令：

```bash
pip install pyinstaller
```

就是这样。您已准备好。

## 将所有内容捆绑在一起

我将首先向您展示如何使用 PyInstaller 为您的应用程序创建捆绑包。所有这些都将包含在一个文件夹中，其中包含一个可执行文件和一个包含依赖项的文件夹。

请记住，我们用于输入 GUI 的代码如下所示：

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class UserInputApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('User Input App')
        self.setGeometry(100, 100, 400, 200)
        self.label = QLabel('Enter text:')
        self.text_input = QLineEdit()
        self.save_button = QPushButton('Save to File')
        self.save_button.clicked.connect(self.save_to_file)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def save_to_file(self):
        text = self.text_input.text()
        with open('user_input.txt', 'a+') as file:
            file.write(text + '\n')
        print('Text saved to file.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserInputApp()
    window.show()
    sys.exit(app.exec_())
```

让我们使用以下命令创建一个新目录：

```bash
mkdir INPUT_APP
```

使用以下命令更改到该目录：

```bash
cd INPUT_APP
```

使用以下命令创建 Python 文件：

```bash
nano input.py
```

*将上面的代码粘贴到该文件中，然后保存/关闭它。然后，您可以使用以下命令创建捆绑文件夹：*

```bash
pyinstaller input.py
```

当命令完成后，使用以下命令更改到 dist 目录：

```bash
cd dist
```

### EDITOR'S RESPONSE
在这个文件夹中，你会找到一个名为 input 的子文件夹，其中包含可执行文件，以及一个名为 _internal 的文件夹。使用 *cd input* 命令进入 input 文件夹，然后你可以使用以下命令运行你的应用程序：

*./input*

输入 GUI 将会打开，你可以使用该应用程序。

如果你想以这种方式分发应用程序，你需要将 INPUT_APP/dist/input 文件夹复制给任何需要它的人，他们就可以像你一样运行它（只要他们的机器上安装了 Python）。

有一个更简单的方法。

## 创建单个文件可执行文件

最好的方法是使用 PyInstaller 创建单个文件可执行文件。这里唯一的区别是你在（INPUT_APP 文件夹内）运行的命令，它是：

*pyinstaller –noconsole –onefile input.py*

–noconsole 选项指示 PyInstaller 抑制应用程序启动时不可避免地打开的终端窗口，而 –onefile 则告诉 PyInstaller 创建单个文件可执行文件。

当此命令完成时，你将在 dist/input 目录中找到单个文件可执行文件。然后，你可以将该文件复制到你的 $PATH 中的目录（例如 /usr/local/bin）或复制给任何需要该应用程序的人。

这就是从 Python 代码创建可执行文件的所有步骤。使用这种便捷的方法，你的应用程序不仅更容易运行，而且更容易分发给其他用户。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。