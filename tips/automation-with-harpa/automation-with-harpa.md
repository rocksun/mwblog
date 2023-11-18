<!--
title: 使用HARPA和AI轻松实现自动化
cover: https://img.youtube.com/vi/RrpTd6Nu4Is/hqdefault.jpg
-->

每天都要为[云云众生](https://yylives.cc/)整理一些文章，虽然 AI 对我帮助很大，但还是需要许多繁琐的手工工作。趁着周末有时间，试了一下 [HARPA](https://harpa.ai/) ，果然解决了我许多问题，ChatGPT 和 RPA 结合的威力凸显。

## 面临的问题

我发的文章是用 markdown 维护的，所有的文章开头都有这样的内容：

```markdown
<!--
title: 我理想中的多云架构
cover: https://cdn.thenewstack.io/media/2023/11/800f5433-multicloud-architecture.jpg
-->

多云不仅仅是一个流行词语，它为IT架构带来了显著的好处。以下是我的愿望清单。

> 译自 [Multicloud Architecture: What I Want to See](https://thenewstack.io/multicloud-architecture-what-i-want-to-see/)。作者Robert Sonders。

```

其中许多内容是从原始文章里获取的，例如 cover、原标题和原 URL，这些内容的处理比较简单，一般的 RPA 工具，或者直接写程序解析网页内容都可以很容易的获取。但是 title 还有摘要（多云不仅仅...）则是翻译而来。相对于传统的翻译工具，ChatGPT 和 Claude（我现在用的） 的效果更好，我要完成这个工作，就需要将原文复制到 Claude 里，然后再把翻译结果拷贝到 markdown 里。真的有点烦。

## 解决方案

于是我就搜索了一下，第一个出来的结果就是 HARPA，因为支持 Claude ，我立马决定安装试用：

![](https://yylives.cc/wp-content/uploads/2023/11/harpa-main.jpg)

因为 Claude 有免费额度，所以我选了使用 Claude。HARPA 最棒的就是不需要 API，只需要登录了 Claude 的 Web 界面就可以使用。看到有个 `Create`，于是我就创建一个自定义 Command ，看起来有戏。

## 实现

因为有着一些 RPA 和自动化的经验，我很快整理通过一些步骤实现了我的需求，此时的 Command 是这样的：

![](https://yylives.cc/wp-content/uploads/2023/11/harpa-command.jpg)

首先是利用 EXTRACT Step 来抓取网页的数据：

![](https://yylives.cc/wp-content/uploads/2023/11/extract-step.jpg)

通过这个步骤，可以获取文章的标题，并保存为 theTitle 变量。然后可以利用 GPT step 将这个标题发送给 Claude 翻译：

![](https://yylives.cc/wp-content/uploads/2023/11/gpt-step.jpg)

在返回结果格式的控制方面，Claude 不如 ChatGPT 听话，所以上面的提示词有一些啰嗦。结果存放到了 gpt 变量中。然后需要一个 RUN JS step 处理数据：

![](https://yylives.cc/wp-content/uploads/2023/11/run-js-step.jpg)

可以看到翻译后的标题存放到了 theCNTitle 变量中了。

其他数据也用类似的处理方式，最后通过 SAY Step 进行整合：

![](https://yylives.cc/wp-content/uploads/2023/11/say-step.jpg)

点击 Save 并 Confirm，然后退出来直接执行这个 Command，就是我希望的结果了。


## 资源

* HARPA Chrome 插件地址: https://chromewebstore.google.com/detail/harpa-ai-automation-agent/eanggfilgoajaocelnaflolkadkeghjp
* HARPT Commands 文档: https://harpa.ai/chatml/overview
