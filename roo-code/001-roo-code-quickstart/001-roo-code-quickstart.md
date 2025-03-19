<!--
title: Roo Code快速入门
cover: ./cover.png
summary: "本文提供了一个使用 Roo Code 的快速入门指南。Roo Code 是一个 VSCode 扩展，可以帮助开发人员更高效地编写代码。本文介绍了安装过程、配置 provider (Gemini AI Studio)，以及使用 Roo Code 为文章中提到的工具添加链接的首次尝试。"
-->

前一段时间试用了 [WindSurf](https://windsurf.ai) 和 [Trae](https://trae.ai)，充分体验了指挥式编程的乐趣。[WindSurf](https://windsurf.ai) 看起来更加的完善，但是当我想要大展拳脚时，免费的额度已经用完了。于是便转向 Trae，正好我有个 AWS 上部署资源的任务，于是就用 Trae 帮我来编写 Pulumi 代码。效果不错，虽然不时有一些小错误，但是比我自己写要快太多了，这个后面可以详细讲讲。不过，对于很多程序员来讲，追求的是更自由地做事方式，于是我决定开始尝试 [Roo Code](https://marketplace.visualstudio.com/items?itemName=rooveterinaryinc.roo-cline)。

## 安装

打开 VSCode，按下 Ctrl+Shift+X ，在搜索框输入 Roo Code，看到 Roo Code，点击 Install 即可。

安装完成后，VSCode 的左侧边栏就会出现一个小火箭图标，点击就看到了 Roo Code 的界面。此时，会要求你配置一个 Provider。

## 配置一个 provider

也就是配置一个大预言模型的 API。Roo Code 是推荐 Claude 3.7 Sonnet，但对于我来说，虽然 Claude 非常的棒，我还是想先试试免费的，你还是我们的 Gemini。

到 [Gemini AI Studio](https://ai.google.dev/) 注册一个账号，创建一个 API key ，然后到 Roo Code 的配置界面录入，然后选择 gemini-2.0.flash-001 作为模型。点击 Save 保存。

当然，使用 Gemini 还有个障碍还是网络，需要让 VSCode 走代理。很遗憾，Roo Code 应该是不支持通过环境变量或 VSCode 配置设置代理，所以我设置了个 VPN 代理。

## 第一个尝试

我想，这个 Roo Code 应该可以帮助我编写这篇文章，这也是我目前使用 VSCode 最多的地方，于是在 Roo Code 的聊天界面，选择 Code 模式，然后输入：

```
帮我把文章中出现的工具加上链接
...
```

然后我的 Markdown 文件中的：

```
前一段时间试用了 WindSurf 和 Trae
```

就变成了

```
前一段时间试用了 [WindSurf](https://windsurf.ai) 和 [Trae](https://trae.ai)
...
```

很不错，给的链接很准确。

## 生成总结

下面，我的文章还需要有一个总结，还需要一个配图，按照 Roo Code 的配置界面，似乎配图也是没问题的。我输入：

```
请根据本文的内容，生成一个可以当作封面的图，并增加一段可以作为文章引文的 summary 。
```

结果如下：

```
Okay, the task has changed. Now I need to generate a cover image and a summary for the article "001-roo-code-quickstart.md".

Since I cannot directly generate images, I will create a placeholder for the cover image in the markdown file. Then, I will generate a summary based on the content of the article and add it to the markdown file.
```

Roo Code，你竟然不能文生图？Gemini 2.0 是可以的啊？总结倒是出来了，不过是英文的，所以我要求用中文。我在文章开头有一些预留的字段：

```
<!--
title: Roo Code快速入门
cover: 
summary: 
-->
```

Roo Code 很智能的修改成了：

```
<!--
title: Roo Code快速入门
cover: image.png
summary: "本文提供了一个使用 Roo Code 的快速入门指南。Roo Code 是一个 VSCode 扩展，可以帮助开发人员更高效地编写代码。本文介绍了安装过程、配置 provider (Gemini AI Studio)，以及使用 Roo Code 为文章中提到的工具添加链接的首次尝试。"
-->
```

很棒，是我想要的。

但是图片怎么办，我看了一下 [Roo Code Tools 列表](https://docs.roocode.com/basic-usage/using-tools)，确实没有生成图片的 Tool。

## 生成封面图？

按照我能想到的，别人就能想到的原则，我找了一下有没有文生图的 MCP Server，还真有一个 [Gemini Flash MCP](https://github.com/jezweb/gemini-image-generation-mcp)。

按照说明我试了一下，又看了下代码，严重怀疑这个项目不能用。在 [Model Context Protocol servers](https://github.com/modelcontextprotocol/servers) 上有几个，不过要求都稍微有点高，所以，本文封面还是我到 Gemini 界面上生成。

使用 MCP Server 才是 Roo Code 的精髓，所以下一篇文章，我将会尝试将一个图片 MCP Server 集成到我的 Roo Code 中。