一方面，我指出OpenClaw已识别的[安全问题](https://www.theregister.com/2026/02/02/openclaw_security_issues/)时，感到有些矛盾，尽管严肃的AI思想领袖们正在将他们的代理命名为“Arnold”并向它们大喊命令。我感到有责任认真对待他们的热情，同时也要强调整个领域仍然存在问题。

NanoClaw[登场](https://nanoclaw.dev/)。它不仅仅是一个[非常小的爪子](https://thenewstack.io/nanoclaw-minimalist-ai-agents/)。

首先，NanoClaw可以将每个代理隔离在自己的容器中。因此，代理循环启动时对其他代理一无所知，只了解你告知它的资源。

另一个有趣之处在于，这个应用程序并非一个与巨石应用通信的大型配置文件；它只是你需要的代码（以及适当的Claude技能）——Claude会根据需要自行修改。考虑到现在代码“便宜”，且Claude的编辑可靠，这确实有道理。而且它确实保持了代码量较小。

### WhatsApp？不了，谢谢。

我的第一个问题是……机器人如何访问WhatsApp？这是大多数OpenClaw用户（和NanoClaw）首选的联系方式。问题在于，除非你拥有商业账户，否则你肯定没有足够的平台股份来托管任意新用户。经仔细检查，WhatsApp连接似乎依赖于一个名为[Baileys](https://baileys.wiki/docs/intro/)的模块，它会扫描WhatsApp Web基于WebSocket的数据，而Meta强烈不鼓励这种做法。事实上，使用未经授权的方法连接WhatsApp的账户会被积极监控和限制。

我几乎不会鼓励使用这种方法，但幸运的是，我们不必如此。我确实为Slack工作区付费，虽然连接Slack有点痛苦，但至少它是完全合规的。

### 安装

我当然已经安装了Claude，并连接到“专业”账户。根据[说明](https://github.com/qwibitai/nanoclaw)，我做了通常的事情：

```
git clone https://github.com/qwibitai/nanoclaw.git
```

然后我在新目录中用`/setup`运行了Claude：

![](https://cdn.thenewstack.io/media/2026/03/1d768e10-image-1024x227.png)

我已经安装了Docker Desktop，因为这部分需要：

![](https://cdn.thenewstack.io/media/2026/03/441984c7-image-1-1024x167.png)

在Mac上，如果你没有自己启动它，你会在菜单栏中看到熟悉的Docker图标。

然后我们来看看你如何连接Claude：

![](https://cdn.thenewstack.io/media/2026/03/6b1ce776-image-2-1024x366.png)

通常，我必须记住关闭API密钥，因为它比订阅更昂贵。这是我第一次看到这两个选项并排提及——一个好兆头。

然后我们来到了有争议的部分：

![](https://cdn.thenewstack.io/media/2026/03/8e4f04e3-image-3.png)

正如我所指出的，我认为WhatsApp不合适，所以我将使用Slack。

然后我们接到了伟大的Slack支线任务：

![](https://cdn.thenewstack.io/media/2026/03/96178f0e-image-5-1024x554.png)

我现在必须找到两个令牌，但不是用我的剑和值得信赖的盾牌，而是通过Slack API。我只向经验丰富的冒险家推荐这场“战役”。继续。

### 在Slack中生成令牌

幸运的是，[Slack技能](https://nanoclaw.dev/skills/slack)有一些很好的说明，而且Claude很有耐心。首先，我们需要生成令牌和作用域。

在Slack上，我找到了相应的对话框：

![](https://cdn.thenewstack.io/media/2026/03/9f0bb9db-image-6-1024x510.png)

我们需要打开Socket模式：

![](https://cdn.thenewstack.io/media/2026/03/a629702a-image-7-1024x379.png)

然后我们需要订阅一组机器人事件：

![](https://cdn.thenewstack.io/media/2026/03/98b1369f-image-8-956x1024.png)

并为OAuth添加作用域——这些限制了NanoClaw应用程序在该账户中可以执行的操作：

![](https://cdn.thenewstack.io/media/2026/03/ad92906a-image-9-947x1024.png)

最后，你可以安装你的新应用并获取最终的~~地牢钥匙~~令牌：

![](https://cdn.thenewstack.io/media/2026/03/61d8d647-image-10-892x1024.png)

我屠龙了/找到宝藏了/击败了火箭人。嗯，不完全是。

Claude崩溃了。但我很快回到了之前的位置，Claude似乎修复了错误的Slack脚本，并接受了我的两个令牌用于其`.env`文件：

![](https://cdn.thenewstack.io/media/2026/03/d9d4b3a1-image-11-1024x221.png)

然后就是将NanoClaw引入我的Slack频道了。

我原以为我们已经完成了Slack的部分，但我们需要让它访问我的服务器文件夹。请记住，这就是我们使用[Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/)赋予它真正力量的方式：

![](https://cdn.thenewstack.io/media/2026/03/6a99c032-image-13-1024x399.png)

一种更好的选择文件夹的方式会很酷，但我添加了那些我乐意让NanoClaw看到的文件夹：

![](https://cdn.thenewstack.io/media/2026/03/4295839c-image-14-1024x122.png)

然后，在获取正确的Claude认证令牌后，我就可以在我的Slack频道上与NanoClaw通信了：

![](https://cdn.thenewstack.io/media/2026/03/afcaebd0-image-15-1024x378.png)

我最初尝试确认NanoClaw可以在我的Mac上看到我的文件夹失败了：

![](https://cdn.thenewstack.io/media/2026/03/af544214-image-16-1024x162.png)

这既是好事也是坏事。它证明了代理是存在于一个容器中，**而不是**单个应用程序的一部分。当然，我让Claude自行修复。我一直在跟踪日志，这样我就可以把所有问题反馈给Claude，它最终以NanoClaw代理能够理解的方式映射了文件夹：

![](https://cdn.thenewstack.io/media/2026/03/803bac9b-image-17-1024x141.png)

请注意它如何将“代理”称为一个独立的实体。因此，我与NanoClaw代理和Claude之间进行了反复沟通。我在这里仍然很像一名工程师——但控制分离是好的。这些错误都是我们常犯的，不理解Linux想要什么。没有人理解Linux想要什么。

最终，它修复了内部数据库并重启了容器所需的一切。通过新的映射，我可以看到我的Documents文件夹：

![](https://cdn.thenewstack.io/media/2026/03/b8585ee1-image-18-1024x155.png)

为了检查，我添加了一个新文件，以确认它确实实时映射到目录。最终，它确实反映了文件存在。

> “我喜欢Claude将容器中的代理视为独立于自身的存在，总的来说，如果你真的想成为一个‘高级用户’，只是需要一个可以呼来唤去的秘书，这无疑是一个更明智、更安全的设置。”

现在这并没有在我的橱柜下的Mac Mini上运行，而是在我的笔记本电脑上。所以，我不会在凌晨2点跑步时，要求根据收件箱中的报告来一份研究文件，但如果我喜欢那种事情，NanoClaw显然可以相当安全地提供。

虽然我确实需要扮演工程师来让一切正常工作，但实际上，我是在告诉Claude我的问题，然后Claude解决了它们。为此，我得到了从我的移动Slack应用程序到我服务器的直接连接。我喜欢Claude将容器中的代理视为独立于自身的存在，总的来说，如果你真的需要一个“高级用户”来呼来唤去，这无疑是一个更明智、更安全的设置。