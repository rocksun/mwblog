# Neovim 的未来：人工智能与脑机接口

![Neovim 的未来：人工智能与脑机接口](https://cdn.thenewstack.io/media/2025/03/53f8c39d-novim-1024x768.jpg)

柏林的 Neovim 维护者 [Justin M. Keyes](https://github.com/justinmk) 在东京一年一度的 Vim 大会上，以一句奇怪的短语开场了他传统的“[Neovim现状](https://www.youtube.com/watch?v=TUzdcB_PFJA)”主题演讲。（[Neovim](https://neovim.io/) 是对[Vim文本编辑器](https://thenewstack.io/vim-after-bram-a-core-maintainer-on-how-theyve-kept-it-going/) 的现代重构。）这是他偶然听到一位体育迷说的，似乎蕴含着“某种象征意义”的话：

“巨人队没有暂停时间了。”

Keyes 对他的听众说：“他给我们发了一份备忘录。他告诉我们，我们需要加快速度。”因此，正如 Keyes 看到的那样，现在最关键的问题不仅仅是如何成为最好的[类似 Vim 的](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) 模态文本编辑器，而是 Neovim 如何与 VS Code 和 Zed 等其他项目竞争。

于是，在数千名 Neovim 粉丝的注视下，Keyes 分享了他多年来推动该项目发展的图表。它始于 Neovim 的技术架构（以及多线程支持），随着其势头的增强，项目管理更加自觉地“将精力导向有用的方向”。

但到了 2024 年，Neovim 已准备好考察所有文本编辑器的更大市场，“寻找信号——你知道，世界在告诉我们什么，宇宙在告诉我们什么。”

对 Keyes 来说，这意味着“思考脑机接口，思考 VS Code 和 Zed 等其他项目的架构，思考我们如何才能利用 Zig 之类的东西”。

Keyes 以令人难以置信的雄心壮志，向他的听众提供了对 Neovim 的前瞻性评估——同时也对整个计算领域发表了一些广泛的思考。着眼于未来，他不仅分享了他对 Neovim 新功能和即将发生变化的看法，还分享了他对人工智能在文本编辑器中的作用，甚至是对基于[WebAssembly](https://thenewstack.io/top-5-uses-of-webassembly-for-web-developers/) 的 Neovim 工件（可在其他软件中使用）的可能性。

是的，脑机接口不断出现。


## 超越键盘的世界

Keyes 事实上地说：“10 年后，脑机接口可能并不少见，键盘将成为一种更主要的备用输入方法。

“这对于 Vim 和 Neovim，以及 Zed 和[VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 和其他类型的开发工具来说，都很有趣。”

即使在遥远的未来，Keyes 认为类似 Vim 的编辑器，凭借其易于使用的宏编程功能和逻辑结构的界面，至少在“前几代脑机接口中仍然适用，即使键盘上的实际按键不再重要！”

在这个拥有脑机接口的世界里，“按钮和菜单将比基于键盘的界面更加过时。”因此，虽然类似 Vim 的编辑器允许用户为文本编辑选择不同的“[模式](https://www.warp.dev/terminus/vim-modes)”——例如用于选择文本块的“visual”模式——但 Keyes 对 Zed 和 VS Code 中似乎不存在模式感到惊讶。

当脑机接口出现时，它们将是需要的。


## IDE 中的人工智能

Keyes 意识到，像 VS Code 和 Cursor 这样的竞争对手编辑器正在包含一些 AI 功能，但他已经展望未来。“最终，如果我们以正确的方式设置，它有望进入 Neovim。而我们的工作是找出差距，以便我们可以帮助第三方扩展提供 AI 扩展所需的环境，或者如果需要的话，可以在我们的标准库中构建一些原语。”（Keyes 还认为人工智能“是一种功能；它不是一种产品。”）

我非常希望 neovim 能赢得 AI 竞赛。

— Benjamin Scott (@TheBenzend)

[2025 年 2 月 21 日]

但 Keyes 将自己描述为“对人工智能感到兴奋”，甚至举了一个他使用过的提示的例子，该提示成功地生成了 Neovim 函数的第一个版本。“这很有用，”他说，“这就是为什么我们的文档很重要。”

一张幻灯片完成了这个想法：

“如果你不为人类解释/记录事情，人工智能也会更弱。”

Keyes 深思熟虑地补充道，人工智能是“额外的头脑”。他对人工智能感到兴奋。


## 即将推出
展望 Neovim 更近期的未来，Keyes 阐述了他对明年的提案，“我明年真正、真正、真正想要解决的事情。” 他的首要任务是什么？“必须取消按 Enter 键，”他说道，指的是需要按下的按键组合以确认异常。Keyes 将这些强制确认称为“邪恶”，以及“人们认为其他项目更稳定的原因”。他补充道：“当 VS Code 中抛出异常时，VS Code 不会像发送电子邮件和打印传真一样。它只是记录它。我们应该这样做。”

你可以并且应该使用 Neovim 做的事情：

游标轨迹 [https://t.co/351IF6pCFT](https://t.co/351IF6pCFT) [pic.twitter.com/Zsg8Mym55i](https://pic.twitter.com/Zsg8Mym55i) — Justin M. Keyes (@justinmk) [2024年12月4日](https://twitter.com/justinmk/status/1733667506001403907)

另一个即将推出的功能受到 tmux（终端多路复用器）的启发。“很快你就可以只按一次 Ctrl+Z 并将你的 UI 从任何 Neovim 会话中分离出来。”

Keyes 还列出了“相对容易做的事情，我们应该去做。它使编辑器成为一个完整的答案，一个完整的应用程序。” 例如，当用户将文件拖放到 Neovim 中，或粘贴图像或 URL 时，“它应该做一些有用的事情”。他还想开始开发图像的 API。并且应该为 Lua 脚本语言提供性能分析和调试功能。

Keyes 将他的大部分列表描述为“抱负……除了演示模式”。当 Neovim 打开使用[Markdown](https://en.wikipedia.org/wiki/Markdown)格式化的文件时，Keyes 希望看到一种在格式化文本和非格式化文本之间轻松切换的方法。“我建议可能使用 Z+Tab 或 Backspace 作为按键，”Keyes 说。“也许甚至是帮助文档，我不知道还有什么——但至少是 Markdown。Markdown 是文档世界的 JSON。它只是……它无处不在。你需要支持它。”

## 如果？
Keyes 提醒听众他[最喜欢的下载 Neovim 插件的网站](https://dotfyle.com/neovim/plugins/trending)，同时补充说，甚至可能会有某种 Neovim 包格式，“希望明年”。

他稍后用一张只有一行文字的幻灯片再次提到它：

“**未来**: *packspec pkg.json*”

它指的是 Keyes 正在开发的新打包格式。

“我认为我们应该尝试一下这种包格式，看看会发生什么。这是一个低成本的尝试。规范还有大约 5% 的内容需要完成，然后我们可以看看会发生什么。”

但 Keyes 也花了一些时间来讨论一些假设性场景。如果 Vim 的模态文本编辑成为一个库，允许将其集成到项目中会怎样？Keyes 的回答？“这是一种可能的发展方向，”但另一个方向是 Neovim 本身可以被其他项目“使用”。也许 Neovim 可以拥有自己的 WebAssembly 工件，提供快速的模态文本编辑功能，“以及一般的文本编辑”。

这导致 Keyes 谈到一个有趣的题外话。“你需要交互式命令，任何没有从一开始就具备这个功能的项目最终都会以某种不完善的形式添加它。”

## 没有数据科学巫师
Keyes 提醒他的听众，VS Code 的文档[承认](https://code.visualstudio.com/docs/getstarted/telemetry)它“收集遥测数据，用于帮助了解如何改进产品。” 但 Neovim 却很受欢迎，“即使我们从未雇佣任何数据科学巫师来告诉我们用户想要什么。

“实际上，事实证明，你可以从问题跟踪器、社交媒体以及你自己的直觉中获得相当好的信号。”

作为证据，Keyes 分享了 Neovim 达到了另一个里程碑。“自去年以来，我们的 GitHub 下载量翻了一番。这是一个某种信号。”

“它甚至可能来自机器人，或者其他什么。没关系，因为猜猜怎么了？我们今年从 GitHub 下载的机器人数量是去年的两倍！”

对于 Homebrew 安装程序，“这是有史以来第一次，我们的安装量超过了 Vim 本身。” Keyes 的幻灯片显示 Neovim 下载量为 373,000 次，Vim 下载量为 296,000 次——而在 2023 年，Vim 的 238,000 次下载量比 Neovim 多 20,000 次。

所有这些似乎都证明了 Neovim 的状态良好。也许是健康状况的最终标志，甚至它的贡献者数量也在增长。“连续第四年，我们在 Stack Overflow 上获得‘最受喜爱’奖，”Keyes 补充道。“不管这意味着什么。我们不知道，但我们每年都在获胜，所以这非常重要。直到我们不再获胜！”

“这就是你所需要的一切。你不需要遥测。”

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)