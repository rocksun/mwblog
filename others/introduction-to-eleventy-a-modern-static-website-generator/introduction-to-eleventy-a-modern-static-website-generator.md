<!--
title: 一个现代静态网站生成器Eleventy
cover: https://cdn.thenewstack.io/media/2024/01/a95fa18f-marcel-eberle-imtfsr5vcas-unsplash-1024x683.jpg
-->

我们展示了Eleventy如何提供一种流畅的Web开发过程，与现有技术协同工作，同时引导您采用良好的实践。

> 译自 [Introduction to Eleventy, a Modern Static Website Generator](https://thenewstack.io/introduction-to-eleventy-a-modern-static-website-generator/)，作者 David Eastman 曾是一位在伦敦工作的专业软件开发人员，曾在 Oracle Corp. 和英国电信公司工作，还是一位顾问，帮助团队以更敏捷的方式工作。他写了一本关于 UI 设计的书，并一直在撰写技术文章...

我进入了 Jamstack 和静态站点生成器的世界，当时我使用 [Publii 和 Netlify](https://thenewstack.io/jamstack-style-build-a-website-with-netlify-and-publii/) 启动了一个页面。

从那时起，Jamstack 这个术语被 Netlify [推广了一番](https://thenewstack.io/is-jamstack-toast-some-developers-say-yes-netlify-says-no/)。尽管如此，大多数站点并不需要来自服务器的动态页面，只需要成为 Web 本应是的东西：由 HTML 和 CSS 构成的链接页面，再加上一点点 JavaScript 的帮助。

[Publii](https://getpublii.com/) 是一款全能的静态网站创建工具，如果你不想碰任何代码，它是一个不错的选择。但是，稍加努力，你可以使用现代 Web 组件制作更快、更精致的站点，并对整个过程有更多的控制。

所以 [Eleventy](https://www.11ty.dev/)（通常简称为 11ty）是奇怪命名的 JavaScript 工具包中的又一个。但作为静态站点生成器，它有什么优势呢？除了支持多种模板语言外，我注意到很多宣称的优点只有在你已经熟悉其他系统的限制时才有意义。所以我打算深入了解一下，一边了解一边解释。这篇文章假设你可能想要更新自己的站点，但你并不是专业从事这类工作的人。（我将不涉及将站点公开，因为我在 Netlify 的文章中已经介绍过。）

Eleventy 有一个我非常喜欢看到的[快速入门指南](https://www.11ty.dev/docs/get-started/)。它还直接使用 [Markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/)。首先，我以为我需要更新我的 Node.js，因为这似乎是我如今启动所有 JavaScript 事物的方式。令我惊讶的是，在打开我的 [Warp 终端](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)后，我已经有了超过版本 14 所需的版本：

```bash
> node --version
v18.15.0
```

好的，按照指示，我创建了一个目录，创建了一个空的 package.json，并让 npm 安装所需的内容：

```bash
> npm install @11ty/eleventy --save-dev
added 214 packages, and audited 215 packages in 18s
```

太好了。现在我们将创建两种不同类型的内容文件（或模板），并观察 Eleventy 处理它们的方式。按照指示，我在命令行上生成了这些内容。

```bash
echo '<!doctype html><title>页面标题</title><p>你好</p>' > index.html
```

这是第一个例子，是纯 HTML，就现在而言，不需要进一步处理。

```bash
echo '# Page header' > README.md
```

这是 Markdown。现在让我们执行 Eleventy 看它的处理：

![](https://cdn.thenewstack.io/media/2024/01/ea4b2b8f-untitled-1024x200.png)

*运行 11ty*

它创建了一个 _site **output**目录，将 Markdown 转换为 HTML，并将 index.html 直接放入其中。如果我们查看新的 _site 目录，可以确认：

![](https://cdn.thenewstack.io/media/2024/01/5e3ca6df-untitled-1.png)

所以它将我的 [README.md](http://readme.md/) 文件的输出视为一个新的路径，具有自己的默认索引页面。它似乎还使用了 [Liquid](https://www.11ty.dev/docs/languages/liquid/)，一种[模板语言](https://liquidjs.com/tutorials/intro-to-liquid.html)，来处理这些文件。

现在让我们在本地服务器上查看站点：

```bash
npx @11ty/eleventy --serve
[11ty] Writing _site/README/index.html from ./README.md (liquid)
[11ty] Writing _site/index.html from ./index.html (liquid)
[11ty] Wrote 2 files in 0.51 seconds (v2.0.1)
[11ty] Watching…
[11ty] Server at http://localhost:8080/
```

如预期，我们在 [http://localhost:8080](http://localhost:8080) 得到一个页面，上面只有一个简单的“Hi”；在 [http://localhost:8080/README](http://localhost:8080/README) 得到一个页面，其中包含用 \<h1> 包裹的“页面标题”。你可以让这个过程“热加载”新页面，并在想要重新启动时使用 Ctrl-C。

因此，启动和运行基本操作很容易，而且结果是一个合理的输出结构。而这一切都来自指南。（我们还可以创建一个输入源目录）。

## 模板语言和前置内容

现在进入有趣的部分。对于个人网站，我们希望页面共享一个布局。我们希望将内容保留在 Markdown 中，并让 Eleventy 为我们创建站点。Eleventy 使用两个有用的概念来实现这一点。

**模板语言**允许你在你的目标输出语言（网站的 HTML）中插入代码指令。通常我们需要区分“这是代码，不要动它”的行和“将这个的结果放在屏幕上”的行。正如我们所见，Eleventy 默认使用 [Liquid](https://shopify.github.io/liquid/basics/types/) 模板语言。

下面是一些简单的 Liquid 代码，展示了所有的要点：

```liquid
{% if username %}
Hello <b>{{ username }}</b>!
{% endif %}
```

这是一个简单的条件语句，包裹了一些 HTML，其中包含一个引用。因此，代码部分检查一个名为 username 的变量是否存在。如果该变量存在，我们按照 HTML 的建议将此用户名打印出来，使用双大括号表示我们希望在屏幕上看到结果。我可以直接将这段代码放入我的源模板文件 index.html 并运行它。

尽管是空白的，因为用户名不存在。但我可以分配一个：

```html
<!doctype html>
<title>Page title</title>
{% assign username = "David"%}
{% if username %}
Hello <b>{{ username }}</b>!
{% endif %}
```

如果你保存并且服务器仍在运行，你会在浏览器中看到这个：

![Zoom](https://cdn.thenewstack.io/media/2024/01/0b4d132d-untitled-2.png)

*一点 Liquid*

现在我们平稳地过渡到所有模板共享的另一个有用的概念：**前置内容**。这使我们能够在任何模板中定义变量（或元数据），就像我们为 Liquid 所做的那样。如果我们再次修改源文件 index.html，前置内容的声明也将 David 声明为一个用户名：

```html
---
username: "David"
---
<!doctype html>
<title>页面标题</title>
 
{% if username %}
你好 <b>—</b>！
{% endif %}
```

而且我们也可以在 Markdown 中实现这一点。

## 创建网站

好的，让我们回到我们的网站。提醒一下：

- 我们希望网站的页面使用一个布局。
- 但我们只想在 Markdown 中编写内容，而不是深入 HTML。

首先，我让 ChatGPT “创建一个带有漂亮猫图的 HTML 模板”。

结果如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nice Cat Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f8f8f8;
            margin: 0;
            padding: 0;
        }
 
        header {
            background-color: #333;
            color: white;
            padding: 10px;
        }
 
        img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin-top: 20px;
        }
 
        footer {
            background-color: #333;
            color: white;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
 
    <header>
        <h1>Nice Cat Page</h1>
    </header>
 
    <img src="https://placekitten.com/800/400" alt="A nice cat">
 
    <footer>
        <p>&copy; 2024 Nice Cat Page. All rights reserved.</p>
    </footer>
 
</body>
</html>
```

如果我用这个替换我们的 `index.html` 页面，我们立即就能看到一个漂亮的猫页面：

![Zoom](https://cdn.thenewstack.io/media/2024/01/3eea7275-untitled-3-1024x733.png)

但我们希望将其作为我们的布局页面。我们希望实际页面的标题出现在“漂亮猫页面”的位置，并且我们想在猫的下方放一些实际的文本内容。


因此，让我们将这个猫页面命名为 layout.html，并修改它以插入我们想要的 Liquid 模板变量。在这里...

```html
<header>
   <h1>中 UN 文</h1>
</header>
```

...以及在这里：

```html
..
<img src="https://placekitten.com/800/400" alt="A nice cat">
        {{content}}
<footer>
    <p>&copy; 2024 Nice Cat Page. All rights reserved.</p>
</footer>
..
```

与变量 title 不同，变量 content 是 Eleventy 正在追踪的一个特殊变量。它理解在使用布局时，任何页面内容都放在这个位置。

但如果我们仅使用这个，Eleventy 将认为布局页面只是一个类似 README 的路径。因此，我们将其放在一个名为 **_includes** 的特殊文件夹中，该文件夹不会被构建，但可以被引用。如果我们清理 _site 目录（旧页面将保留）并忽略庞大的 node-modules 目录，你应该有这个：

![Zoom](https://cdn.thenewstack.io/media/2024/01/f9776109-untitled-4-300x190.png)

由于没有打开的 index.html，什么都不会提供。我们只有旧的 README。

所以让我们创建一个 index.md，告诉它关于标题和内容，以及布局。我们使用前置内容进行此操作：

```markdown
---
layout: "layout.html"
title: "Davids Website"
---

Hi there, I like cats!!
```

简单。

构建的结果是这个作为首页：

![Zoom](https://cdn.thenewstack.io/media/2024/01/007a3a57-untitled-5-1024x624.png)

新的小猫，新的危险

请注意提供了一个不同的猫图片。

最终的目录布局是：

![Zoom](https://cdn.thenewstack.io/media/2024/01/aa60e3af-untitled-6-300x199.png)

这应该足以激发你对撰写自己的网站的热情，或许足以让你望而却步。然而，要获得现代网站的所有精彩组件，你需要深入了解，我将在以后的文章中详细介绍。目前的要点是，Eleventy为我们提供了一个良好的流程，与现有技术协同工作，同时引导我们遵循良好的实践。
