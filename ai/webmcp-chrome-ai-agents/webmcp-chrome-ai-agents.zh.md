大约两周前，我发表了一篇关于[返回Markdown的网站](https://thenewstack.io/intent-engineering-ai-agents/)的文章，旨在让AI代理的生活更轻松。尽管代理已经非常擅长使用浏览器，但这个过程仍然可能很繁琐、耗时且费力。我提到在HTML中添加微数据作为导航线索，但如果允许它们直接在页面上使用MCP呢？

所以你看，[WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/)几乎是水到渠成。当代理访问DOM时，它们可以很好地通过使用HTML声明中可识别的组件来执行操作。像Selenium这样的旧式网页测试工具就是这样工作的。当页面相当规则时（当然，这正是网络演变为消费者商店前端后的样子），导航并不困难。但随着人类逐渐为AI代理让路，以及代理与人类协同工作，简化它们的通行就变得很有意义。

因此，通过一个Chrome扩展程序，网页现在可以像MCP服务器一样运行。这种方法去年由[微软和谷歌](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/)共同推动。这与OpenAI正在通过其[Apps SDK和ChatGPT Atlas](https://thenewstack.io/openais-apps-sdk-a-developers-guide-to-getting-started/)所做的工作并非不无关系。但使用WebMCP，操作是在客户端进行的。

## 人类网络用户依然参与其中

当我第一次读到这个的时候，我以为它纯粹是为了让AI代理能够“绕过”网络，以结构化的方式直接与页面进行对话。但也许是因为谷歌仍然需要人类来获得广告收入，人类仍然深度参与其中。

因为你可能正在浏览一个网站，并想向代理提问关于该页面的问题，所以代理需要在你提问之前和期间了解一些上下文。你可以想象一个用户在页面旁边打开AI聊天，并询问屏幕上的内容。因此，不要只想象一个代理为了某个任务去访问一个无头浏览器，还要想象一个用户中断自己的浏览会话来查询网站。

此外，正如[MCP和**安全启发**](https://thenewstack.io/model-context-protocol-evolution/)一样，代理必须能够返回给用户以提出澄清问题。

完整的[提案](https://developer.chrome.com/blog/webmcp-epp)提到了两个API：**声明式API**用于页面内标准的HTML风格操作，以及**命令式API**用于需要JavaScript的复杂操作。

## 在Chrome中使用WebMCP

虽然Chrome的示例是最近才出现的，但一些[好奇的用户已经开始尝试](https://ricmac.org/2026/03/11/webmcp-ai-agents-interact-website/)了。

我将以谷歌[当前文档](https://docs.google.com/document/d/1rtU1fRPS0bMqd9abMG_hc6K9OAI6soUy3Kh00toAgyk/edit?tab=t.0)中的一个示例为例。显然，你正在使用谷歌的尖端技术，所以请先注册他们的计划以获取更新。第一步是通过[此邀请页面](https://developer.chrome.com/docs/ai/join-epp)加入谷歌Chrome早期预览计划（EPP）。

你需要Chrome版本`146.0.7672.0`或更高。在查看“关于”框中的版本后，它开始自动更新，就像在看薛定谔的猫一样，我发现我的版本符合要求：

![](https://cdn.thenewstack.io/media/2026/03/40465af5-image-1024x200.png)

然后我们需要翻转“WebMCP for testing”的标志（即服务默认是关闭的），你可以通过内部导航到`chrome://flags/#enable-webmcp-testing`来完成。

![](https://cdn.thenewstack.io/media/2026/03/121a10e1-image-1-1024x723.png)

然后用你的新选择重新启动，检查更改是否生效。如果你不知道，这一切都还在实验阶段：

![](https://cdn.thenewstack.io/media/2026/03/8351caa3-image-2-1024x448.png)

然后你可以安装[检查器，它能让你看到WebMCP](https://chromewebstore.google.com/detail/model-context-tool-inspec/gbpdfapgefenggkahomfgkhfehlcenpd)工具（即已注册的功能）的内部工作。

安装完成后，你可以访问[实时演示页面。](https://googlechromelabs.github.io/webmcp-tools/demos/react-flightsearch/)

你会看到模拟航班搜索页面（我猜是模拟的）和右侧面板中的检查器，它有效地提取了可用的MCP工具，例如“searchFlights”：

![](https://cdn.thenewstack.io/media/2026/03/62d40e31-image-3-1024x790.png)

因此，例如，我们可以在左侧“手动”浏览，并使用表单获取以下航班的信息（我目前绝对不推荐这个航班）：

![](https://cdn.thenewstack.io/media/2026/03/c6a94a0e-image-4-1024x1011.png)

遗憾的是，这个查询不被支持：

![](https://cdn.thenewstack.io/media/2026/03/79d69f18-image-5-1024x578.png)

很自然地，我礼貌地向模拟应用程序提供了所需的示例数据（所以，这不是一个真正的航班搜索），并如预期地得到了一个模拟结果屏幕：

![](https://cdn.thenewstack.io/media/2026/03/f959726d-image-6-1024x832.png)

所以我们现在可以在检查器工具中使用这些详细信息：

![](https://cdn.thenewstack.io/media/2026/03/ec0e2c31-image-7.png)

这会返回相同的模拟HTML页面。

现在，如果我们有一个真正的代理，我们就可以看到结构化的回复。我从Google AI Studio生成了一个Gemini API密钥，在检查器中设置了该密钥，并向代理查询了航班页面：

![](https://cdn.thenewstack.io/media/2026/03/8a18c1d5-image-8.png)

“与页面交互”这一点很有趣，因为对于用户来说，这是一个稍微新颖的操作上下文——向代理询问他们正在查看的页面。另外，介绍网站[webmcp.dev](https://webmcp.dev/)上的页面提到（并显示）页面右下角有一个小蓝色方块，表示WebMCP可用。谷歌Chrome的示例中没有这个，但现在还处于早期阶段，因此实现方式可能会有所不同。

发送我的英文查询后，我得到了以下结构化结果：

```
User prompt: "What flights are available?"
AI calling tool "listFlights" with {}
Tool "listFlights" result:
[
 {
  "id":7,
  "airline":"Spirit Airlines",
  "airlineCode":"NK",
  "origin":"LHR",
  "destination":"JFK",
  "departureTime":"08:49",
  "arrivalTime":"07:05",
  "duration":"22h 16m",
  "stops":0,"price":932
 },
 {
  "id":8,
  "airline":"Southwest Airlines",
  etc
```

这看起来是上面模拟HTML航班结果页面的JSON等效结果。因此，我们可以看到我们不仅可以获得专为AI代理工作流设计的结果，还可以让代理与人类一起，并返回一个网站。在这个例子中，查询前端会整齐地呈现数据，并可能要求添加过滤器来细化结果。

作为快速检查，该工具在普通页面（例如The New Stack）后面没有发现WebMCP：

![](https://cdn.thenewstack.io/media/2026/03/e3752daf-image-9-1024x410.png)

所以，至少目前看来，人类网络的“死刑”被暂缓了。人类可以使用WebMCP来增强他们的网络体验，而不仅仅是依靠AI代理。