<!--
title: 微软刚刚开源了让 Comic Sans 一举成名的那个应用
cover: https://cdn.thenewstack.io/media/2026/07/8953b4eb-miika-laaksonen-nul9apggvgm-unsplash-scaled.jpg
summary: 微软正式开源了90年代经典的 IRC 客户端 Comic Chat。该软件曾通过将对话转化为漫画形式而普及了 Comic Sans 字体。此次开源旨在保护互联网历史，并邀请社区探索其在现代系统上的潜力及与现代 AI 代理的关联。
-->

微软正式开源了90年代经典的 IRC 客户端 Comic Chat。该软件曾通过将对话转化为漫画形式而普及了 Comic Sans 字体。此次开源旨在保护互联网历史，并邀请社区探索其在现代系统上的潜力及与现代 AI 代理的关联。

> 译自：[Microsoft just open-sourced the app that put Comic Sans on the map](https://thenewstack.io/microsoft-comic-chat-open-source/)
> 
> 作者：Paul Sawers

Comic Sans 自问世以来，在企业传播中就一直受到嘲讽、恶搞和限制，但大多数人可能不知道，它实际上是在 20 世纪 90 年代一款名为 [Comic Chat](https://en.wikipedia.org/wiki/Microsoft_Comic_Chat) 的 IRC 客户端中崭露头角的，该客户端能将输入的对话变成连环漫画。

现在，微软宣布将 Comic Chat 客户端开源，将代码库移交给社区进行探索和构建。

在周四发布的一篇[博客文章](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/)中，微软 Copilot 加速团队首席项目经理 Robert Standefer 和微软/GitHub 副总裁兼技术人员 Scott Hanselman 解释说，此次发布是为了保护一段互联网历史，这段历史诞生于在线交流规范尚在形成之初的时期。

“它诞生于互联网还在探索自己想要成为什么的时期，”他们写道。“许多规则尚未制定，这使得开发人员可以尝试一些即使在今天看来也不同寻常的大胆概念。”

> “它诞生于互联网还在探索自己想要成为什么的时期。”

## 漫画时机

微软于 1996 年推出了 Comic Chat，作为体验互联网中继聊天 ([IRC](https://en.wikipedia.org/wiki/IRC)) 的一种新颖方式，这是一种在现代聊天应用出现之前的实时群聊纯文本协议。

客户端不是滚动显示文本，而是读取人们输入的内容，然后实时在周围构建漫画风格的面板——选择匹配的插画角色、对话气泡、姿势和面部表情。讲个笑话，角色可能会咧嘴一笑并拍打膝盖；变得好斗，它可能会交叉双臂并皱眉。

![Comic Chat + Comic Sans](https://cdn.thenewstack.io/media/2026/07/eda00d75-fasf-1024x656.png)

*Comic Chat 与 Comic Sans 的邂逅*

这些对话气泡需要看起来像是手写而非打字的字体，这就是 [Comic Sans](https://en.wikipedia.org/wiki/Comic_Sans) 的用武之地。微软字体设计师 Vincent Connare 早在 1994 年就设计了这种字体，并作为 Microsoft Windows 附加包的一部分首次引入。然而，事实证明，Comic Chat 的漫画书风格是它更自然的展示平台，这比它后来出现在办公室生日传单上并成为设计界最喜欢吐槽的对象要早得多。

Comic Chat 并非独立下载，而是搭乘了那个时代微软最大的软件。该客户端最初随 1996 年的 Internet Explorer 3 一起提供给用户，随后随着 Windows 98 将其作为默认组件内置，它获得了更多的受众，使 IRC 漫画生成器出现在数百万台台式机上。

像许多早期的互联网应用程序一样，随着网络的成熟，Comic Chat 逐渐被更复杂的在线交流形式所取代——即时通讯工具、论坛，以及我们今天使用的各种聊天应用。

三十年后，微软现在认为这个客户端值得重温，但更多是将其作为一段历史交给那些可能仍能从中发现价值的人。

## 让 Comic Chat 在现代系统上重获新生

[GitHub 仓库](https://github.com/microsoft/comic-chat)包含了基本未改动的原始 Comic Chat 源代码，以及微软称之为“AI 驱动的现代化尝试”的一些更新。这些更新使得古老的代码可以在当前版本的 Visual Studio 中构建，连接到现代 IRC 服务器，并修复了它在当今高分辨率屏幕上的显示问题。

> “这些不是精修后的重新发布版，而是展示 Comic Chat 仍能在现代系统上运行的范例。”

微软谨慎地将这些更新定位为演示，邀请社区在此基础上进一步推动代码的发展。

“这些不是精修后的重新发布版，而是展示 Comic Chat 仍能在现代系统上运行的范例，”作者写道。“我们很高兴看到社区接下来会带来什么改进、移植、实验以及全新的形式。”

同样值得记住的是，Comic Chat 的语气解读是基于规则的：一组固定的触发器映射到一组固定的姿势和表情，背后没有任何花哨的 LLM。这种差距是一个很好的比较点，说明了今天的 AI 驱动聊天代理和头像与昔日的美好时光有何不同，因为现代模型可以推广到它从未见过的文本，而 Comic Chat 只能对开发人员预先预期的线索做出反应。

> “它预见了一种概念，即软件可以解读对话并赋予头像表现力行为，而不仅仅是显示文本。”

当被问及 Comic Chat 的引擎与当今 AI 驱动的头像和代理之间是否有任何概念上的相似之处时，Scott Hanselman 告诉 *The New Stack*，虽然他确实看到了其中的脉络，但并没有合法的理由将那种早期技术描述为生成式 AI。

“它预见了一种概念，即软件可以解读对话并赋予头像表现力行为，而不仅仅是显示文本，”他说。

此外，Scott Hanselman 特别指出了 Comic Chat 最初是如何实现其表现力的：人类绘制的艺术作品，辅以一套简单且清晰可见的规则，任何人都可以检查。

“这既是一个美妙的怀旧版本，也是以人为本的计算创造力的一个重要例子，”Scott Hanselman 继续说道。“在某些方面，它与其说是图像生成的祖先，不如说是富有表现力的头像和代理的祖先。”