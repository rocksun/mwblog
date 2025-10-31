曾几何时，Node.js 是 JavaScript 的首选运行时。无论是好是坏，如果你想构建一个 JavaScript 应用程序，你都会在后端使用 Node.js。由于习惯以及支持 Node.js 的大量工具、库和框架，它仍然是一个被广泛使用的选择。但近年来，新的运行时陆续出现，以解决开发者在使用 Node.js 时面临的一些挑战。

其中一个新后端运行时是 Bun，它于 2021 年推出。Bun 的简要介绍是它“像 Node.js，但专为速度、现代工作流设计，并且安装的工具更少”，这解决了开发者在使用 [Node.js](http://node.js) 时遇到的许多痛点。这一点很重要，因为 2025 年的网络与 2009 年 [Node.js](http://node.js) 最初创建时大不相同。

[Hono 于 2021 年 12 月由日本开发者 Yusuke Wada 创建](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/)。根据其 GitHub 仓库，Hono 是一个“基于 Web 标准构建的小型、简单且超快的 Web 框架”。它最初是为 Cloudflare Workers 构建的，但现在“可以在任何 JavaScript 运行时上”运行，包括 Node.js、Deno、Bun 和 Vercel（尽管 Node 支持需要适配器，并且 Node 版本 ≥ 18）。

## 为什么用 Bun 和 Hono 构建 API？

在我们深入构建无服务器 API 之前，让我们先了解一下现在市场竞争更加激烈的一些类似工具。

### 经典之选：[Node.js](http://node.js) 和 Express

这是一种比 Bun 和 Hono 更“重”的架构——更多的样板代码、更慢的启动时间和更大的内存占用。

### 竞争对手：Deno 和 Oak

在所有选项中，Deno 和 Oak 最接近 Bun 和 Hono。Deno 是一个现代运行时——安全的默认设置、内置工具、性能优化——并提供一流的 TypeScript 支持，旨在兼顾安全性和开发者友好的默认设置。

那么，你为什么要用 Bun 和 Hono 构建应用呢？

即使在竞争日益激烈的市场中，这种组合也具有明显的优势。首先是速度。Bun 专为性能而构建，使得 API 响应速度极快。其次是简洁性。设置最小化，让你能专注于逻辑而非配置。这种架构也支持 TypeScript，使类型安全开发更加容易。最重要的是，它对无服务器友好，提供了 Cloudflare、AWS Lambda 和其他平台的模板。

让我们来实际体验一下。

我们将构建一个简单的无服务器 API，它将：

*   从浏览器接收两个数字；
*   计算它们的和；
*   将结果存储在内存和应用程序中。

## 本教程的先决条件

开始之前，你的机器上应该安装以下软件：

## 设置你的 Bun 和 Hono 项目

在开始构建之前，我们需要进行一些安装和基本设置。在你的 IDE 中，在一个新项目的终端窗口中，让我们安装 Bun 并初始化一个新的 Hono 项目。

首先，我们需要安装 Bun。

```
bun install
```

成功安装后，我们就可以初始化 Hono 项目了。

```
bun create hono hono-api
cd hono-api
```

在这里你可以看到 Hono 提供的所有模板。我们将选择“bun”模板，然后选择“Y”以安装项目依赖，并选择 Bun 包管理器。

对于这个项目，我们只需要两个文件：

*   `src/index.ts` — 这是我们刚刚安装的包的一部分。这个文件将作为我们的 API 后端。
*   `test.html` — 你必须在 `hono-api` 文件夹中添加这个文件。这是我们的浏览器界面。

## 构建 `index.ts`

所有以下代码块都可以按照相同的顺序添加到同一个文件中。我将其拆分，以便深入探讨我们无服务器 API 的功能。

### 导入和初始化

CORS 是我们将使用的中间件。这允许 API 从浏览器访问，防止跨域问题。

```
import { Hono } from 'hono'
import { cors } from 'hono/cors'


const app = new Hono()
```

接下来，让我们启用 CORS。下面的代码将把 CORS 应用于所有路由。

```
app.use('*', cors())
```

我们要做的下一件事是创建内存存储。当我们从浏览器提交数字时，这段代码将允许一个结果数组也显示在终端中。尽管我们将它们保存在终端中，但它们仍然是临时的，当你重新启动服务器时它们将被清除。

```
const results: { a: number; b: number; sum: number }[] = []
```

### 构建路由

我们将添加的第一个路由是根路由。这是针对 `/` 端点的基本 GET 请求。

```
app.get('/', (c) => c.text('Hello, world!'))
```

下一个路由将是另一个 GET 路由，这次带有一个 URL 参数。你可以通过在浏览器中 URL 末尾添加一个词来测试功能。这个词将显示在浏览器页面中。

```
app.get('/api/greet/:name', (c) => {
  const name = c.req.param('name')
  return c.json({ message: `Hello, ${name}!` })
})
```

我们现在准备添加 POST 路由 `/api/sum`。

这段代码将从浏览器接收两个数字，验证它们的类型，计算它们的和，然后将其存储在 `results` 数组中。它将在终端中记录内存内容。这段代码以 JSON 格式返回和。

```
app.post('/api/sum', async (c) => {
  try {
    const { a, b } = await c.req.json()
    if (typeof a !== 'number' || typeof b !== 'number') {
      return c.json({ error: 'Both a and b must be numbers.' }, 400)
    }


    const sum = a + b
    results.push({ a, b, sum }) // store in memory
    console.log('Stored sums:', results) // debug log to terminal
    return c.json({ sum })
  } catch (err) {
    return c.json({ error: 'Invalid JSON body.' }, 400)
  }
})
```

我们将构建的最后一个路由是一个 GET 路由，`/api/sum`。

这将以 JSON 格式将代码发送到浏览器。

```
app.get('/api/sum', (c) => {
  return c.json(results)
})
```

最后一步是导出应用程序。

```
export default app
```

这里是代码的一键复制/粘贴选项：

```
import { Hono } from 'hono'
import { cors } from 'hono/cors'


const app = new Hono()


app.use('*', cors())


// STORAGE
const results: { a: number; b: number; sum: number }[] = []


// ROOT
app.get('/', (c) => c.text('Hello, world!'))


// GET
app.get('/api/greet/:name', (c) => {
  const name = c.req.param('name')
  return c.json({ message: `Hello, ${name}!` })
})


// POST
app.post('/api/sum', async (c) => {
  try {
    const { a, b } = await c.req.json()
    if (typeof a !== 'number' || typeof b !== 'number') {
      return c.json({ error: 'Both a and b must be numbers.' }, 400)
    }


    const sum = a + b
    results.push({ a, b, sum }) // store in memory
    console.log('Stored sums:', results) // debug log to terminal
    return c.json({ sum })
  } catch (err) {
    return c.json({ error: 'Invalid JSON body.' }, 400)
  }
})


// GET
app.get('/api/sum', (c) => {
  return c.json(results)
})






// Export
export default app
```

## 构建 `test.html`

`test.html` 是一个简单的网页界面，用于连接前端和后端。由于它是基本的 HTML，我们不会深入讲解。你可以在这里输入两个数字并将它们相加，结果将显示在页面上。它还会将存储的结果记录到你的终端。

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Test Sum API</title>
</head>
<body>
  <h1>Sum API Test</h1>
  <input id="num1" type="number" placeholder="Enter first number" />
  <input id="num2" type="number" placeholder="Enter second number" />
  <button onclick="callSum()">Calculate Sum</button>
  <p id="result"></p>


  <script>
    async function callSum() {
      const a = Number(document.getElementById('num1').value)
      const b = Number(document.getElementById('num2').value)


      const response = await fetch('http://localhost:3000/api/sum', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a, b })
      })


      const data = await response.json()
      document.getElementById('result').innerText = JSON.stringify(data)
    }
  </script>
</body>
</html>
```

## 如何运行你的无服务器应用程序

构建完成后，你可以使用命令 `bun run src/index.ts` 运行应用程序。

你可以在项目文件夹中双击 `test.html` 文件（在 Mac 上，我使用 Finder 找到它），手动在浏览器中打开它。

浏览器将看起来像这样：

[![](https://cdn.thenewstack.io/media/2025/10/8d376771-sum3-1024x280.png)](https://cdn.thenewstack.io/media/2025/10/8d376771-sum3-1024x280.png)

每次你点击“Calculate Sum”（计算和）时，你的终端都会更新，显示类似这样的内容：

[![](https://cdn.thenewstack.io/media/2025/10/75da9cc6-terminal-resize.png)](https://cdn.thenewstack.io/media/2025/10/75da9cc6-terminal-resize.png)

就这样！你现在拥有一个功能齐全的无服务器求和 API，带有一个简单的网页界面。