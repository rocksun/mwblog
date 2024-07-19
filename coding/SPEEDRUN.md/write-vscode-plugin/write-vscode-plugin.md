
<!--
title: brisk-extension/SPEEDRUN.md 在 main · brisktest/brisk-extension
cover: https://opengraph.githubassets.com/80eee679676797934ca8abd803f273972f680623d2c8d1a67d48bd53ac3b9fe4/brisktest/brisk-extension
-->

VS Code Brisk 扩展。通过在 GitHub 上创建帐户，为 brisktest/brisk-extension 开发做出贡献。

> 译自 [brisk-extension/SPEEDRUN.md at main · brisktest/brisk-extension](https://github.com/brisktest/brisk-extension/blob/main/SPEEDRUN.md)，作者 Brisktest。


VS Code 扩展程序，用于 Brisk

Brisk 可以非常快地运行您的测试，并且可以在您的开发环境中运行，在每次保存时在云端运行您的整个测试套件。我们使用的 React 演示在 12 秒内完成，这足够快，可以在您每次保存时运行您的测试套件。

让我们制作 Brisk VS Code 扩展程序来启用此行为，并在此过程中了解一些关于 VS Code 扩展程序的工作原理。

它们非常棒！

`npx --package yo --package generator-code -- yo code`
这将启动 vscode 扩展程序创建器，它将创建一个包含扩展程序所需的一切的新项目。我选择了 Typescript、esbuild 和 yarn。yarn 发出了很多关于内存泄漏包的警告，我将来可能会或可能不会调查这些警告。

在扩展程序生成器结束时，它会提示您在 Code 中打开项目 - 请执行此操作。

在编辑器中，打开 src/extension.ts 并按 F5 或从命令面板 (⇧⌘P) 运行命令调试：启动调试。这将在新的扩展开发主机窗口中编译并运行扩展程序。

从新窗口的命令面板 (⇧⌘P) 运行 Hello World 命令：

因此，此处的过程是转到扩展程序并运行它 - 这将创建一个新的 vs code 窗口，您的扩展程序在其中处于活动状态。然后，您可以调用您在命令面板中指定的命令（在本例中为 hello world），它将在底部显示为通知 - 请执行此操作。这将是我们接下来一段时间内的开发循环。

我们将对输出进行一些小的更改，以确保所有构建系统都在工作，并且我们在加载扩展程序时所做的修改正在被构建和执行。

`vscode.window.showInformationMessage('Hello Peaceful World from Brisk!');`
现在我们重新启动并转到第二个窗口，并在命令面板中运行“Hello World”。

现在我们想更改命令名称

我将把它改为“helloPeacefulWorld”

因此我更改

` let disposable = vscode.commands.registerCommand('brisk.helloPeacefulWorld', () => {`
在扩展程序中

以及在 package.json 中

```
"commands": [
{
"command": "brisk.helloPeacefulWorld",
"title": "Hello World"
}
]
```
让我们看看是否有效？

不..

命令仍然是 Hello World...

..好的

也许我还需要更改 package.json 中的标题

```
"commands": [
{
"command": "brisk.helloPeacefulWorld",
"title": "Hello Peaceful World"
}
]
```
是的！

因此，我们现在要做的两件主要事情。

- 弄清楚如何运行命令而不是打印
- 弄清楚如何在保存时执行我们的命令
```
"commands": [
{
"command": "brisk.run",
"title": "Run Brisk"
}
]
```
以及在 extension.ts 中

```
let disposable = vscode.commands.registerCommand('brisk.run', () => {
// 您在此处放置的代码将在每次执行您的命令时执行
// 向用户显示一个消息框
vscode.window.showInformationMessage('Hello Peaceful World from Brisk!');
});
```
显然，我们感兴趣的是 Terminal，而“sendText()”会将内容发送到 Terminal。让我们将其合并。

```
vscode.window.onDidChangeActiveTerminal(e => {
console.log(`Active terminal changed, name=${e ? e.name : 'undefined'}`);
});
// 该命令已在 package.json 文件中定义
// 现在使用 registerCommand 提供命令的实现
// commandId 参数必须与 package.json 中的 command 字段匹配
let disposable = vscode.commands.registerCommand('brisk.run', () => {
// 您在此处放置的代码将在每次执行您的命令时执行
// 向用户显示一个消息框
vscode.window.showInformationMessage('Hello Peaceful World from Brisk!');
const terminal = vscode.window.activeTerminal || vscode.window.createTerminal(`Brisk ${NEXT_TERM_ID++}`);
terminal.sendText("echo 'Sent text immediately after creating'");
const workspaceFolder = getWorkspaceFolder();
terminal.sendText(`cd ${workspaceFolder} && brisk`);
terminal.show(true);
terminal.processId.then(pid => {
console.log(`Terminal process ID: ${pid}`);
}
);
});
```
现在让我们将设置代码添加到激活中

```
export function activate(context: vscode.ExtensionContext) {
// 使用控制台输出诊断信息 (console.log) 和错误 (console.error)
// 此行代码仅在您的扩展程序激活时执行一次
console.log('Congratulations, your extension "brisk" is now active!');
// 定义默认设置
const defaultSettings = {
"brisk.configFile": "brisk.json",
};
// 加载用户设置
const config = vscode.workspace.getConfiguration();
let configFile = config.get(
"brisk.configFile",
defaultSettings["brisk.configFile"]
);
// 监听用户设置的更改
const disposableConfigUpdater = vscode.workspace.onDidChangeConfiguration(
(event) => {
if (event.affectsConfiguration("brisk.configFile")) {
// 用户设置已更改，相应地更新您的扩展程序
const updatedSetting = config.get(
"brisk.configFile",
defaultSettings["brisk.configFile"]

```javascript
// Load user settings
let config = vscode.workspace.getConfiguration();
let configFile = config.get(
"brisk.configFile",
defaultSettings["brisk.configFile"]
);
console.log("Brisk: the config file is ", configFile);
// Listen for changes in user settings
const disposableConfigUpdater = vscode.workspace.onDidChangeConfiguration(
(event) => {
if (event.affectsConfiguration("brisk.configFile")) {
let config = vscode.workspace.getConfiguration();
// User setting changed, update your extension accordingly
const updatedSetting = config.get(
"brisk.configFile",
defaultSettings["brisk.configFile"]
);
console.log(
`Updated setting: ${updatedSetting} - we will use it on the next run`
);
configFile = updatedSetting;
}
}
);
console.log("Brisk: the config file is ", configFile)
// When your extension is deactivated, clean up your resources
context.subscriptions.push(disposableConfigUpdater);
vscode.window.onDidChangeActiveTerminal((e) => {
console.log(`Active terminal changed, name=${e ? e.name : "undefined"}`);
});
// The command has been defined in the package.json file
// Now provide the implementation of the command with registerCommand
// The commandId parameter must match the command field in package.json
let disposable = vscode.commands.registerCommand("brisk.run", () => {
// The code you place here will be executed every time your command is executed
// Display a message box to the user
vscode.window.showInformationMessage("Hello Peaceful World from Brisk!");
const terminal =
vscode.window.activeTerminal ||
vscode.window.createTerminal(`Brisk ${NEXT_TERM_ID++}`);
terminal.sendText("echo 'Sent text immediately after creating'");
const workspaceFolder = getWorkspaceFolder();
terminal.sendText(`cd ${workspaceFolder} && brisk`);
terminal.show(true);
terminal.processId.then((pid) => {
console.log(`Terminal process ID: ${pid}`);
});
});
context.subscriptions.push(disposable);
}
```
```typescript
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from "vscode";
import * as childProcess from "child_process";
var NEXT_TERM_ID = 1;
var latestRun = 0;
export function activate(context: vscode.ExtensionContext) {
  console.log('Congratulations, your extension "brisk" is now active!');
  // Define default settings
  const defaultSettings = {
    "brisk.configFile": "brisk.json",
  };
  let runningTerminalProcess: number | undefined;
  let disposable = vscode.commands.registerCommand("brisk.run", () => {
    let config = vscode.workspace.getConfiguration();
    latestRun++;
    let myLatestRun = latestRun;
    console.debug("Starting run " + myLatestRun);
    setTimeout(() => {
      if (myLatestRun !== latestRun) {
        console.debug("Skipping run because a new run was started.");
        return;
      }
      vscode.window.terminals.forEach((oldTerminal) => {
        oldTerminal.processId.then((pid) => {
          if (pid === runningTerminalProcess) {
            console.debug("Killing old process " + pid);
            oldTerminal.sendText("exit");
          }
        });
      });
      const terminal =
        vscode.window.activeTerminal ||
        vscode.window.createTerminal(`Brisk ${NEXT_TERM_ID++}`);
      const workspaceFolder = getWorkspaceFolder();
      // Load user settings
      let configFile = config.get(
        "brisk.configFile",
        defaultSettings["brisk.configFile"]
      );
      terminal.sendText(
        `cd ${workspaceFolder} && brisk -c ${configFile}`
      );
      terminal.show(true);
      terminal.processId.then((pid) => {
        console.log(`Terminal process ID: ${pid}`);
        runningTerminalProcess = pid;
      });
    }, 100);
  });
  context.subscriptions.push(disposable);
}
// This method is called when your extension is deactivated
export function deactivate() {}
function getWorkspaceFolder(): string {
  const folders = vscode.workspace.workspaceFolders;
  if (folders) {
    return folders[0].uri.fsPath;
  }
  const message =
    "Brisk: Working folder not found, open a folder and try again";
  vscode.window.showErrorMessage(message);
  return "";
}
```
```javascript
if (pid === runningTerminalProcess) {
  console.debug("Killing old brisk run");
  oldTerminal.dispose();
}
});
});
const terminal = vscode.window.createTerminal(`Brisk ${NEXT_TERM_ID++}`);
const workspaceFolder = getWorkspaceFolder();
// Load user settings
let configFile = config.get(
  "brisk.configFile",
  defaultSettings["brisk.configFile"]
);
terminal.sendText(
  `cd ${workspaceFolder} && BRISK_CI=true brisk -c ${configFile}`
);
terminal.show(true);
terminal.processId.then((pid) => {
  console.log(`Terminal process ID: ${pid}`);
  runningTerminalProcess = pid;
});
}, config.get("brisk.delay", 100));
});
context.subscriptions.push(disposable);
}
function getWorkspaceFolder(): string {
  const folders = vscode.workspace.workspaceFolders;
  if (folders) {
    return folders[0].uri.fsPath;
  }
  const message =
    "Brisk: Working folder not found, open a folder and try again";
  vscode.window.showErrorMessage(message);
  return "";
}
// This method is called when your extension is deactivated
export function deactivate() {
  console.log('Extension Brisk is now deactivated!');
}
```

我们还希望在工作目录中存在 brisk 配置文件时激活扩展。

我们在 `package.json` 中添加以下内容：

```json
"activationEvents": [
  "onCommand:brisk.run",
  "workspaceContains:**/brisk.json"
]
```

看起来一切正常，让我们看看如何发布它。

[https://code.visualstudio.com/api/working-with-extensions/publishing-extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)

我需要在 Azure DevOps 中创建一个组织并生成一个安全令牌。

事实证明，我们需要使用一个名为 `vsce` 的工具，我们可以使用以下命令安装它：

`npm install -g @vscode/vsce`

然后我们使用以下命令：

```bash
$ cd brisk-extension
$ vsce package
# myExtension.vsix generated
$ vsce publish
# <publisher id>.myExtension published to VS Code Marketplace
```

在使用扩展一段时间后，我发现使用 Ctrl+s 的快捷键会导致其他人无法使用该快捷键，从而导致保存被中断。因此，我修改了它，使用工作区的 `onSave` 处理程序，这实际上是一个更好的解决方案。我添加了一个配置设置来指定可接受的语言，然后在保存这些语言之一时，我们调用该命令。以下是相关代码：

```javascript
workspace.onDidSaveTextDocument((document: TextDocument) => {
  const config = vscode.workspace.getConfiguration();
  if (config.get("brisk.languages",defaultSettings["brisk.languages"]).includes(document.languageId) && document.uri.scheme === "file") {
    vscode.commands.executeCommand("brisk.run");
  }
});
```

现在，`defaultSettings` 变为：

` "brisk.languages": ["javascript","javascriptreact", "typescript", "python","ruby","haml","html","css","scss","sass"],`

我还更新了 `package.json`，添加了新的默认设置并删除了旧的快捷键。

- Brisk 可以对构建服务器运行一次性命令，例如对代码库运行 linter 或 tsc。添加此功能。