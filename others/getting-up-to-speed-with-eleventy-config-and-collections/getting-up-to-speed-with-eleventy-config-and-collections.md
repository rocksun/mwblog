<!--
title: Eleventy配置和Collection快速上手
cover: https://cdn.thenewstack.io/media/2024/01/972d7bfb-john-cameron-w1k9ug_pjxw-unsplash-1024x789.jpg
-->

继续他的Eleventy教程，David Eastman展示了如何配置该系统、利用模板、介绍什么是 Collection 等等。

> 译自 [Getting up to Speed with Eleventy: Config and Collections](https://thenewstack.io/getting-up-to-speed-with-eleventy-config-and-collections/)，作者 David Eastman。

上周，我们[设置](https://yylives.cc/2024/01/15/introduction-to-eleventy-a-modern-static-website-generator/)了一个静态站点生成器 Eleventy，并对其进行了一些基本操作。我使用 [Warp 命令终端](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)和 [Zed 编辑器](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/)来创建了一个以猫为主题的索引页面。在继续阅读本文之前，请先快速浏览一下上周的文章。确保你了解 Eleventy 是如何获取最小的 index.md 文件，并使用 layout.html 模板在 _site 目录下创建 index.html 文件的。我们将在本文中继续扩展上周的内容。

现在，我们已经接受了 Eleventy 进入我们的生活，我们应该创建一个稍微改进一点的工作环境。在上周我结束的时候，"输出"目录被称为 _site(Eleventy 的默认名称)，但是没有"源"目录，所以模板文件就栖息在项目的根目录中:

![放大](https://cdn.thenewstack.io/media/2024/01/aebd7959-untitled.png)

*我们上周结束时的样子*

想要搞清网页项目中什么在做什么已经够糟糕的了，所以让我们至少创建一个源目录，以便我们可以区分生成网站的模板和其他区域的机制。

是时候在项目的根目录下开始一个 Eleventy 配置文件了。我习惯了一个叫 src 的源目录，大多数网站都将他们的输出保存在 public 中，所以让我们使用这个约定:

```js
module.exports = function(eleventyConfig) {
  // Return your Object options:
   return {
    dir: {
      input: "src"，
      output: "public"
    }
  }
};
```


由于我们更改了配置，我们需要重新启动服务器。当我们这样做时，在我们适当地移动源 material 并删除旧站点之前，什么也不会发生。这包括 _includes。

当我们进行必要的文件移动并运行时，我们的小猫咪(好吧，是另一只小猫咪)回来了。目录结构现在看起来像这样，忽略 modules 目录但包括配置文件:

![放大](https://cdn.thenewstack.io/media/2024/01/1383fed6-untitled-1-300x235.png)

如果你是从我们的网站上阅读这篇文章的，你会在文章结尾看到我的一张漂亮的圆形图片。我想在我网站的标题左边放上这张图片。通过反向工程，我可以看到我的图片被包裹在一个 “post-author-avatar” 类中。像大多数黑客一样，我通过“借鉴”来学习。

制作小圆圈的技巧似乎在这里:

```css
.author-profile-photo-column img
{
  display: block;
  width: 100%;
  aspect-ratio: 1/1;
  -o-object-fit: cover;
  object-fit: cover; 
  border-radius: 30px
}
```

首先，我复制了我的图片 photo-of-me.png 并把文件放到新的 src 目录下。在调整了 layout.html 中的 JavaScript 后，我得到了:

```css
..
header {
            background-color: #333;
            color: white;
            padding: 20px;

            h1 {
                display: inline-block;
                vertical-align: middle;
            }
            img {
                width: 5%;
                border-radius: 30px;
                display: inline-block;
                vertical-align: middle;
                float: left;
            }
}
..
```

然而，如果你试图构建这个，它就不会工作。图片不会被自动复制到 public 目录中。如果你也制作了一个单独的 style.css 文件，情况也是一样的。Eleventy 知道转换和复制它识别为模板文件的内容，但是除非你告诉它这样做，否则它不会接触其他文件:

```js
module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy('./src/*.css');
  eleventyConfig.addPassthroughCopy('./src/*.png');

  return {
    dir: {
     input: "src"，
     output: "public"
    }
  }
};
```

只要我们保存，一切就都好了:

![放大](https://cdn.thenewstack.io/media/2024/01/eba4b54b-untitled-2-1024x720.png)

*猫咪回来了*

目录看起来像这样:

![放大](https://cdn.thenewstack.io/media/2024/01/e5459138-untitled-3-300x259.png)

提醒一下，索引页面是通过 index.md 生成的:

```markdown
---
layout: "layout.html"
title: "David's Home Page"
---

Hi there, I like cats!!
```

现在要指出的是，我并不像那么喜欢猫咪，但我已经开始了这个主题，所以我注定要完成它。所以我要假装我想添加关于著名猫咪的页面。

我们的[主线](https://www.rubick.com/steel-threads/)是，我们希望用 Markdown 写内容，并让 Eleventy 来生成网站。在维护网站时，我们不想处理 HTML。

所以我们会在 src 中做一个 cats 目录，并在其中创建我们的第一只猫 [garfield.md](http://garfield.md/):

```markdown
---
layout: "layout.html"
title: "Garfield"
---

Garfield doesn't like Mondays.
```

如果你已经运行服务器(我在另一个 Warp 标签页中运行它)，你会看到 Eleventy 在幕后处理它。

而且如果我们按照创建的浏览器路径，我们会看到以下内容:

![放大](https://cdn.thenewstack.io/media/2024/01/77ab4026-untitled-4-1024x633.png)

*这不是加菲猫*

好吧，这张图片不是加菲猫。而且，我在左上角漂亮的头像也不见了。另外，我们还想在索引页面上链接到这个页面。

首先，如果我们想展示加菲猫的图片，那么我们需要在**前言**中提到它。但首先我们也需要修改布局。所以让我们把我们的 placekitten 的源地址放入 index.md 的前言中:

```markdown
---
layout: "layout.html"
title: "David's Home Page"
catimage: "https://placekitten.com/800/400"
---

Hi there, I like cats!!
```

并修改我们的布局来使用新的 catimage 变量:

```html
.. 
<body> 
 <header> 
  <img src="photo-of-me.png"> 
  <h1>{{ title }}</h1> 
 </header> 
 <img class="cat" src="{{ catimage }}" alt="A nice cat"> {{content}} 
 <footer> 
  <p>&copy; 2024 Nice Cat Page. All rights reserved.</p> 
 </footer> 
</body> 
..
```

现在，让我们从维基百科上添加一张图片到我们的 garfield.md 文件中。

```markdown
---
layout: "layout.html"
title: "Garfield"
catimage: "Garfieldand_friends.png"
---

Garfield doesn't like Mondays.
```

差不多了。但它还不会工作。看看目录:

![放大](https://cdn.thenewstack.io/media/2024/01/4d2bf07e-untitled-5-266x300.png)

我的加菲猫图片没有进入 public 输出目录。我们从上面的配置中知道为什么，所以让我们调整配置文件，以便猫咪也可以直接通过:

```js
module.exports = function(eleventyConfig) {
  // Return your Object options:
 
  eleventyConfig.addPassthroughCopy('./src/*.css');
  eleventyConfig.addPassthroughCopy('./src/*.png');
  eleventyConfig.addPassthroughCopy('./src/cats/*.png');
 
  return {
    dir: {
      input: "src",
      output: "public"
    }
  }
};
```


现在，加菲猫加入了猫咪们:

![放大](https://cdn.thenewstack.io/media/2024/01/6e8a93ea-untitled-6-281x300.png)

好吧，实际上图片在一个目录之下，不是吗？所以我们再对 Garfield 文件做一个小调整:

```markdown
---
layout: "layout.html"
title: "Garfield"
catimage: "../Garfieldand_friends.png"
---

Garfield doesn't like Mondays.
```

最后我们终于得到了我们的猫咪:

![放大](https://cdn.thenewstack.io/media/2024/01/f738d1d1-untitled-7.png)

使用相同的逻辑，我们也解决了头像的问题。它总是准备好坐在同一个地方，为每个页面共享，但相对于调用页面的位置不同。通过在前面加上一个斜杠，我们指出我们是在根目录中查找它:

```html
.. 
 <header> 
  <img src="/photo-of-me.png"> 
  <h1>{{ title }}</h1> 
 </header> 
..
```

这应该能让你对发生的小问题有所了解，以及在解决问题时应坚持的地方。但你会注意到，Eleventy 相当宽容和透明——使错误比较容易修复。  

好的，所以我们需要从首页链接到我们的猫咪。但如果我们要添加其他猫咪，我们会立即不得不开始黑客布局以添加新链接——而我们不想那样做。我们想让 Eleventy 收集新猫咪并为我们构建链接。

## Collection 和 Tag

幸运的是，Eleventy已经解决了这个问题。它有页面收集的概念。我们在前言中使用标签来标记一个页面作为收集的一部分:

```markdown
---
layout: "layout.html"
title: "Garfield"
catimage: "../Garfieldand_friends.png"
tags: cats
---
 
Garfield doesn't like Mondays.
```

然后我们可以循环遍历我们的猫咪，并制作某种形式的索引:

```html
.. 
 <div class="listcontainer"> 
  <ul> 
   {% for cat in collections.cats %} 
    <li> 
     <a href="/cats/{{ cat.data.title}}">{{ cat.data.title }} </a> 
    </li> 
   {% endfor %} 
  </ul> 
 </div> 
..
```

现在我们可以看到，Eleventy通过data方法为每个猫咪的前言提供了Liquid访问权限。除此之外，我只是做了一个假设文件名与标题相同的链接。(我们可以改进这个)。  

在CSS的帮助下，结果是:

![放大](https://cdn.thenewstack.io/media/2024/01/58b94ba3-untitled-8-1024x749.png)

*猫咪列表*

这为我们提供了到正确页面的链接。从现在开始，我应该能够用 Markdown 添加其他猫咪，它们将自动出现在列表中。我们的下一个目标是为猫咪页面制作一个单独的布局；总是有一件事要做，但目前足够了。

所以现在去玩吧，用 [Eleventy](https://www.11ty.dev/) 创建你自己的网站。你会发现在这个过程中你学到了常见的网页技巧，迭代开发也不会受到惩罚。享受它。
