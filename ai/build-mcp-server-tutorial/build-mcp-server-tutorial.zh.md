Claude 默认了解互联网上所有公开可用的信息。但它对你或你的数据一无所知。是的，你总是可以复制粘贴包含公司月收入的 Excel 表格，但如果你要处理五年历史的企业销售数据，输入这些文件就不那么容易了。

模型上下文协议 (MCP) 服务器通过将你的数据直接连接到 Claude 来改变这一点。通过 MCP 服务器，Claude 可以突然将其推理、判断和分析能力应用于你的数据，而无需你参与任何令人沮丧的变通方案。（如果你曾在一个“如此简单”的变通方案上花费了太多时间，请举手。）

人们正在采用 AI。那么，为什么要让客户加载他们自己的数据呢？Anthropic 让公司构建 MCP 服务器变得非常容易。生态系统也因此迅速发展。

构建你的第一个 MCP 服务器并不难——我们将在 IDE（我使用 VS Code）中创建一个计算器应用程序，并通过 MCP 服务器将其功能直接连接到 Claude Desktop。

为什么是计算器应用程序？我想构建一些简单的东西，将重点从连接外部 API 或复杂的业务逻辑转移开，而是放在这里真正重要的事情上：构建 MCP 服务器的规则和最佳实践。然后，你可以将在这个简单应用程序中学到的技能应用到接下来更复杂的事情中。

> Claude 默认了解互联网上所有公开可用的信息。但它对你或你的数据一无所知。

我们将使用 TypeScript SDK ([开源](https://github.com/modelcontextprotocol/typescript-sdk) [文件在此](https://github.com/modelcontextprotocol/typescript-sdk)) 构建我们的 MCP。TypeScript 和 [Python SDKs](https://github.com/modelcontextprotocol/python-sdk) 是最常用的 MCP SDK。

你需要以下内容才能开始：

我们开始吧。

## 构建连接到 Claude 的 MCP 服务器

我们首先需要做的是设置文件结构并在连接到 IDE 的终端中安装软件包。

创建一个新文件夹并进入它：

初始化一个 Node 项目：

安装 MCP SDK：

安装允许你在本地编译和运行 TypeScript 的依赖项：

安装 Zod 用于输入验证和模式生成

构建 `tsconfig.json`

Node 无法直接运行 TypeScript。`tsconfig.json` 告诉 TypeScript 编译器如何将 TypeScript 代码转换为 JavaScript。

将 `tsconfig.json` 添加到你的项目根文件夹并粘贴以下代码到其中：

```json
{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true,
    "outDir": "./dist"
  }
}
```

如果你正在使用 VS Code，你的 `tsconfig.json` 中可能会出现错误，提示 `no inputs were found in config file…..`。这是我在使用 VS Code 时一直遇到的一个奇怪问题。解决方案（这本身似乎也是个问题）是删除你的 `tsconfig.json`，然后重新创建文件，并粘贴相同的代码。我也不喜欢这样（耸肩）。

更新 `package.json` 以包含此扩展的 `scripts` 对象：

```json
{
  "name": "calculator-mcp",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "npm run build && npm run start"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.1.0",
    "zod": "^3.22.4"
  },
  "devDependencies": {
    "@types/node": "^20.11.16",
    "typescript": "^5.3.3"
  }
}
```

创建 `src` 文件夹和 `[index.ts](http://index.ts)`。

你的文件结构应该如下所示：

```
.
├── dist
│   └── index.js
├── node_modules
├── src
│   └── index.ts
├── package-lock.json
├── package.json
└── tsconfig.json
```

### 构建 MCP 服务器

我们将在一个文件 `src/[index.ts](http://index.ts)` 中构建所有内容。我将首先粘贴完整的代码，然后详细说明每个部分的功能，供那些想要跳过的人参考。

**第一部分：导入 MCP SDK**

这些是你的导入语句。
* `McpServer` 创建服务器。
* `StdioServerTransport` 处理与 Claude 的通信。
* `z` 验证 Claude 发送到我们应用程序的输入。

**第二部分：创建带有名称和版本的服务器**

此部分创建并命名你的服务器。Claude 将使用名称和版本来识别它正在与之通信的服务器。本博客中最重要的概念之一就在此部分。`server.tool()` 的名称、描述、Zod 模式和处理函数是 MCP 的核心。

**第三部分：定义计算器工具**

在这里，我们将构建 `calculate`，告诉 Claude `calculate` 的功能、它期望的输入以及要运行的逻辑。我们将使用 Zod 模式来定义数据的形状。

**第四部分：Claude 调用工具时运行的逻辑**

业务逻辑。此部分接收 Claude 的输入，执行请求的数学运算，并处理边缘情况。

**第五部分：将结果作为文本上下文返回**

这会将结果以 MCP 期望的格式发送回 Claude。Claude 在其对用户的响应中使用此值。

**第六部分：通过标准输入/输出连接**

用于启动服务器并通过标准输入/输出将其连接到 Claude Desktop 的逻辑。

我们已准备好构建项目。运行以下代码，你很快就会在文件树中看到 `dist/` 文件夹出现。

### 连接到 Claude

打开 Claude Desktop，然后转到“设置”>“开发者”>“编辑配置”。这将打开一个名为 `claude_desktop_config.json` 的 JSON 文件。将我们的新服务器添加到 `mcpServers` 对象。此文件可能会在你的 IDE 中启动。像编辑和保存任何其他文件一样进行操作即可。

然后退出 Claude Desktop 并重新启动。这是必要的一步，因为 Claude Desktop 只在启动时读取配置。

重新启动后，打开顶部的“聊天”部分（不是“协作”或“代码”）。然后点击聊天输入框左下角的“+”图标。

![](https://cdn.thenewstack.io/media/2026/04/99fb5484-screenshot-2026-04-06-at-2.36.31-pm.png)

然后将鼠标悬停在“连接器”上，它应该会弹出一个带有计算器的新菜单。确保计算器已开启。

![](https://cdn.thenewstack.io/media/2026/04/26f45fbe-screenshot-2026-04-06-at-2.38.05-pm.png)

在运行计算之前，告诉 Claude 在聊天窗口中使用计算器。它会弹出一个菜单，包含“始终允许”、“允许一次”或“拒绝”。选择“始终允许”或“允许一次”。

现在你已准备好运行计算。在进行中，你可以看到它正在使用你的工具，因为在橙色 Claude 标志下方，“calculate”字样下方会显示“request”字样。

![](https://cdn.thenewstack.io/media/2026/04/8473d4e3-screenshot-2026-04-06-at-2.41.21-pm.png)

你可以判断 Claude 正在使用你的工具，因为它会在显示答案之前显示“Calculate >”字样。

![](https://cdn.thenewstack.io/media/2026/04/a6850985-screenshot-2026-04-06-at-2.41.49-pm.png)

如果你能走到这一步，就可以正式地说你构建了第一个 MCP。从这里开始，它只会变得更复杂，但定义具有清晰模式的工具、编写返回结构化响应的处理程序以及通过配置文件将服务器连接到 Claude 等基本原理保持不变。

你现在拥有将你构建的任何应用程序连接到 Claude Desktop 所需的工具。