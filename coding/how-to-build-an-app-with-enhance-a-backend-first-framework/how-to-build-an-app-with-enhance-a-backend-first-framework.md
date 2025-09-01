<!--
title: 如何使用Enhance构建App：后端优先框架指南
cover: https://cdn.thenewstack.io/media/2025/08/7ab45279-enhance-graphic.jpg
summary: 本文介绍了 Enhance 框架，一个为简单和速度而设计的全栈框架。它与 Astro 等前端优先框架不同，Enhance 侧重于后端逻辑、API 端点和数据库交互。文章还演示了如何使用 Enhance 构建一个包含 SQLite 数据库的微型全栈 CRUD 应用程序，涉及数据库设置、API 功能、服务器构建和前端实现。
-->

本文介绍了 Enhance 框架，一个为简单和速度而设计的全栈框架。它与 Astro 等前端优先框架不同，Enhance 侧重于后端逻辑、API 端点和数据库交互。文章还演示了如何使用 Enhance 构建一个包含 SQLite 数据库的微型全栈 CRUD 应用程序，涉及数据库设置、API 功能、服务器构建和前端实现。

> 译自：[How To Build an App With Enhance, a Backend-First Framework](https://thenewstack.io/how-to-build-an-app-with-enhance-a-backend-first-framework/)
> 
> 作者：Jessica Wachtel

一度，前端框架领域有三巨头：[React](https://thenewstack.io/react-router-new-governance-and-react-server-component-apis/)、[Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/) 和 [Angular](https://thenewstack.io/angular-v20-advances-zoneless-adds-support-for-ai-development/)。 掌握这三个框架基本上是求职的金钥匙。 后来，轻量级应用、服务器端渲染以及再也不想构建 webpack 打包文件的愿望兴起。 突然间，三巨头变成了许多。 当涉及到选择使用哪种技术时，问题从“你是否知道如何使用 X？”转变为“哪种技术最适合这个项目？”

如今的众多选择之一是 [Enhance](https://enhance.dev/)，这是一个为简单和速度而设计的现代全栈框架。 如果你正在寻找快速原型设计，或者你正在做一个后端优先的小型项目，Enhance 是一个可靠的选择。 Enhance 提供了一种轻量级的方法，设置最少，让你能够快速连接 API 和数据库。

## Enhance vs. Astro

其他轻量级框架，[如 Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/)，往往是前端优先。 Astro 的主要重点是构建静态站点或服务器渲染页面，其中你传递给浏览器的 HTML、CSS 和 JavaScript 是主要关注点。 你可以添加后端逻辑，但这不是核心工作流程。

Enhance 是后端优先。 应用程序逻辑、API 端点和数据库交互首先出现。 你不必立即考虑静态 HTML 或页面组件。 你还可以使用“三巨头”框架之一作为前端，从而利用这些技能。

如果你无法在 Astro 和 Enhance 之间做出决定，这里有一种方法可以解决这个问题。

使用 Astro 构建时，你的优先级是：

* 优化前端渲染和页面加载性能。
* 为静态或服务器渲染页面构建布局组件。
* 最小化客户端 JavaScript 并管理水合。

使用 Enhance 构建时，你的优先级是：

* 设计后端逻辑、API 端点和服务器端函数。
* 轻松设置和与数据库交互。
* 快速原型设计全栈功能，无需样板代码。

## 构建一个 Enhance 应用

现在我们已经介绍了基础知识，让我们构建一个包含 SQL 数据库的微型全栈应用程序。 由于前端不是重点，我们将构建一个简单的 CRUD（创建、读取、更新、删除）应用程序，你可以在屏幕上的文本框中添加投票。 你将能够编辑和删除笔记。 由于我们将拥有一个可以正常工作的数据库，因此刷新页面不会影响你已经保存的笔记。

### 入门：文件和安装

创建并打开一个新的项目文件夹。

```
mkdir notes-app
cd notes-app
```

初始化一个 Node.js 项目（这将创建一个 package.json）。

```
npm init -y
```

安装 Enhance 和 SQLite 依赖项。

```
npm install enhance better-sqlite3
```

现在我们将创建我们的项目文件。 这些文件将非常基础。 结构如下所示：

```
notes-app/
├─ db.js          处理 SQLite 连接和设置
├─ api.js         定义创建、读取、更新、删除笔记的函数
├─ server.js      最小 HTTP 服务器，用于服务前端和端点
└─ index.html     前端 HTML + JavaScript，用于与应用程序交互
```

在执行下一步之前，请确保你在 `notes-app` 文件夹中。

确认你在正确的文件夹中后，我们可以创建我们需要的所有文件。

```
touch db.js api.js server.js index.html
```

你可以通过打开主 `notes-app` 文件夹来确认你是否正确地完成了此操作。

现在我们准备开始构建了。

### 构建 SQLite 数据库

我们要设置的第一件事是数据库 `db.js`。

数据库文件将连接到基于文件的 SQLite 数据库 (`myapp.db`)。 它还将创建一个包含 `id`、`title` 和 `content` 的 `notes` 表。 此文件就是你可以刷新页面而不会删除笔记的原因。

你可能会注意到，在此代码中，我们使用术语 `require` 而不是 `import`。 在本教程的其余部分中，我们将继续这样做，因为我们使用的是 CommonJS 语法而不是 ES Modules。 如果你的 `package.json` 包含 `”type”: “module”`，则可以切换到 ES Modules。 请注意，Enhance 的示例和文档通常显示 CommonJS，因为它​​是最简单的设置。

```
const Database = require('better-sqlite3');
const db = new Database('myapp.db');


db.prepare(`
  CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
  )
`).run();


module.exports = db;
```

### 添加 CRUD 功能

此页面 `api.js` 是应用程序的核心。 这些功能是：

`getNotes()`

这是一个 GET 请求。 它的主要目的是从数据库中获取所有笔记。

`addNotes()`

这是一个 POST 请求，因为它向数据库添加了一个新请求。

`editNote()`

这是一个 PUT 请求。 当用户指定时（通过我们稍后添加的编辑按钮），它将更新笔记。

`deleteNote()`

这是一个 DELETE 请求，当用户指定时（我们将稍后添加另一个按钮），它将使用其 `id` 删除笔记。

我们将构建 `async` 代码，以保持代码的整洁和非阻塞。

```
const db = require('./db');


async function getNotes() {
  return db.prepare('SELECT * FROM notes').all();
}


async function addNote({ title, content }) {
  const info = db.prepare('INSERT INTO notes (title, content) VALUES (?, ?)').run(title, content);
  return { id: info.lastInsertRowid, title, content };
}


async function editNote({ id, title, content }) {
  db.prepare('UPDATE notes SET title = ?, content = ? WHERE id = ?').run(title, content, id);
  return { id, title, content };
}


async function deleteNote({ id }) {
  db.prepare('DELETE FROM notes WHERE id = ?').run(id);
  return { success: true };
}


module.exports = { getNotes, addNote, editNote, deleteNote };
```

### 构建服务器

我们的 `server.js` 文件将包括构建一个基本的 HTTP 服务器。 此服务器上没有任何 Enhance 独有的内容。

```
const http = require('http');
const fs = require('fs');
const path = require('path');
const { getNotes, addNote, editNote, deleteNote } = require('./api');


const server = http.createServer(async (req, res) => {
  // Serve index.html
  if (req.url === '/' && req.method === 'GET') {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
    return;
  }


  // GET /notes
  if (req.url === '/notes' && req.method === 'GET') {
    const notes = await getNotes();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(notes));
    return;
  }


  // POST /notes
  if (req.url === '/notes' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      const note = await addNote(JSON.parse(body));
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(note));
    });
    return;
  }


  // PUT /notes/:id
  if (req.url.startsWith('/notes/') && req.method === 'PUT') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      const id = parseInt(req.url.split('/')[2]);
      const note = await editNote({ id, ...JSON.parse(body) });
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(note));
    });
    return;
  }


  // DELETE /notes/:id
  if (req.url.startsWith('/notes/') && req.method === 'DELETE') {
    const id = parseInt(req.url.split('/')[2]);
    await deleteNote({ id });
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ success: true }));
    return;
  }


  // Fallback for unrecognized routes
  res.writeHead(404);
  res.end('Not found');
});


server.listen(3000, () => console.log('Server running on http://localhost:3000'));
```

### 前端

最后，让我们构建我们的 `index.html`。 对于本教程，我们将只使用 HTML — 但你可以将更强大的前端框架连接到此后端以获得更多功能。

由于我们的 `notes-app` 使用 Node 的内置 `http` 模块，你可以使用以下简单命令运行开发服务器：

```
node server.js
```

当你访问 http://localhost:3000/ 时，你应该会看到带有两个文本框的主页，你可以在其中添加笔记。

继续，添加一个笔记。 单击“添加笔记”后，你将看到带有编辑和删除按钮的笔记弹出。

### 访问数据库

所有这些数据库命令都不是 Enhance 独有的。 你可以使用与其他应用程序相同的 SQL。

你可以使用以下命令在终端中访问数据库：

```
#open database
sqlite3 myapp.db


#view notes
.tables


#edit
UPDATE notes SET title = 'New Title', content = 'Updated content' WHERE id = 1;


#delete 
DELETE FROM notes WHERE id = 2;


#exit
.quit


```

就这么简单！

## 结论

Enhance 还有本教程未涵盖的其他更高级的功能。 这是一个不完整的列表：

* JSON 序列化：Enhance 自动处理请求/响应序列化，允许你返回转换为 JSON 的纯 JavaScript 对象。
* 函数作为端点：你可以编写充当 API 端点的纯 JavaScript 函数，而无需单独的服务器或框架。
* 默认情况下为零 JavaScript：你可以在需要时分层 JavaScript，但页面在不需要客户端 JavaScript 的情况下也能正常工作并可访问。

现在你有了使用 Enhance 构建和扩展实际应用程序的基础。 你会建造什么？