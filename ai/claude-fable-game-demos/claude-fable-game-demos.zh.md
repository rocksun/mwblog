![霓虹街机场景](https://cdn.thenewstack.io/media/2026/11/0fa0b84a-risky-ming-6qywiwfpzmu-unsplash-1024x698.jpg)

**Anthropic 的一位工程师给 Claude Fable 5.2 下达了一个提示词来构建**一个第一人称射击游戏，并让它在没有人类反馈的情况下运行了八小时。到最后，该模型处理了 4.45 亿个输入 Token，生成了 270 万个输出 Token，并以约 550 美元的 API 成本制作出了一款可玩的浏览器游戏。

最终的成果是 *[Saltline](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp)*，这是一款背景设定在被雨水浸湿的货运港口的射击游戏，玩家在其中与无人机和机器狗战斗，同时还要禁用通信中继。Anthropic 工程师 [Felix Rieseberg](https://www.linkedin.com/in/felixrieseberg/) 在周一 Fable 5.2 发布时分享了这款游戏，将其形容为一项关于模型仅凭一条指令能完成多少工作的实验。

这位工程师表示，Fable 是通过程序生成游戏的视觉效果，而不是依赖导入的资产。[公共镜像](https://github.com/realcodebear/saltline-fable-5.2)将游戏打包成一个约 1.4MB 的 HTML 文件，其中包含了捆绑的 Three.js 代码。

根据游戏标题画面上的说明，Rieseberg 花了大约两个小时来改进武器模型、声音和游戏玩法，同时保留了指向最初“一次性生成”版本的链接。

## 真正的价格标签

YouTuber [Matthew Berman](https://www.linkedin.com/in/matthewberman/) 将这项实验推向了更远，他要求 Fable 仅使用三行指令在 Unreal Engine 5 中重现《战争机器：E日》（Gears of War: E-Day）中的一个关卡。其结果是一个可玩的射击游戏，玩家可以在其中寻找掩体、与 AI 队友并肩作战，并使用游戏标志性的主动装填机制重新装填武器。

Berman 报告称，该项目在几天内消耗了大约 85 亿个 Token，预估的 API 等效成本接近 15,000 美元。

他的[浏览器版 Excel 克隆版](https://claude.ai/artifact/NPxoR5gnxVVsXnyPAkKpYS)配备了功能区选项卡、公式和数据透视表，耗费了近 50 小时，预估成本达 11,700 美元。

Berman 提前获得了该模型的访问权限，因此这些数字并不一定反映他实际支付的费用，但这很好地说明了[长时间运行智能体](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/)所涉及的计算资源。

## 不止 Fable 一家

并非所有归功于 Fable 的游戏都是单靠 Fable 构建的。创意开发者 [Kevin Ngo](https://kevintngo.com/) 在谈到他的项目 *[What the Water Keeps](https://x.com/kevin_t_ngo/status/2119868968307695818)* 时写道：“Claude Fable 5.2 制作了这个可在浏览器中游玩的的游戏演示。这是一段穿梭于 8 个梦幻般的世界的船程。”

Ngo 使用 Tripo 生成 3D 资产，使用 Suno v6 生成游戏的配乐，而 Fable 则使用免版税的乐器采样创作了预告片音乐。

HyperWrite 的联合创始人 [Matt Shumer](https://www.linkedin.com/in/mattshumer/) 花了相当多的时间[对该模型进行实验](https://somethingbig.ai/fable-5-2-review)。他使用 Fable 构建了一个基于浏览器的具有物理破坏效果的体素破坏引擎，然后转向了一个规模大得多的项目——一个未完成的地球模拟，包含真实地点、天气和交通系统。

> “它完美呈现了我一年来一直试图从几乎所有模型中获得的体素引擎，”

Shumer 在他的博客中写道：“它完美呈现了我一年来一直试图从几乎所有模型中获得的体素引擎，”并补充说 Fable 是从头开始构建它的，并且它在他的 MacBook 上运行。

据报道，他的“霍格沃茨大战堡垒之夜”大逃杀游戏大约花了两周时间开发。Shumer 最初尝试使用多个智能体，但发现单个智能体在经由少量干预的情况下能产生更好的结果。

“它作为拥有整个项目的单个智能体时效果最好，”他说，尽管他也承认这种方法可能会慢得令人沮丧。

Shumer 表示，Fable 仍然需要方向引导，特别是当它把项目做得比实际需要的更复杂时。“你仍然必须引导它。界定问题并让它保持在你的目标轨道上是你的责任。”

> “你仍然必须引导它。界定问题并让它保持在你的目标轨道上是你的责任。”

Shumer 在 [Spawn](https://www.spawn.co/@mattshumer/earth) 上托管他的演示，该平台也是他的投资对象之一。他在评论中并未提及这种联系，目前尚不清楚 Spawn 除了托管完成的项目之外是否还提供了其他帮助。

## Token 数学题

Fable 5.2 每百万输入 Token 收费 8 美元，每百万输出 Token 收费 40 美元，但当智能体运行数小时时，这些价格并不能说明全部情况。

Rieseberg 表示，*Saltline* 的 4.45 亿个输入 Token 中有很大一部分来自缓存上下文，Anthropic 对其处理收费较低。如果没有缓存，仅这些输入 Token 就将花费大约 3,560 美元，而他估计整个运行过程的花费约为 550 美元。

还有开发人员的时间需要考虑。总得有人决定构建什么、审查代码并修复任何出问题的地方。例如，当运行多个智能体产生令人失望的结果时，Shumer 不得不重新思考他的方法，而 Ngo 则使用了独立的工具来为他的游戏创建资产。

## 从演示到产品

这些演示留下了大量关于[在第一个可工作版本构建之后会发生什么](https://thenewstack.io/the-hidden-engineering-cost-of-ai-everywhere-product-roadmaps/)的问题。另一个开发人员仍然需要理解代码、在不破坏现有功能的情况下修改特性，并追踪性能问题。Berman 的电子表格面临着它自己的挑战，因为演示中的有效公式并不能保证在更大的数据集或更复杂的计算中获得准确的结果。

这些演示还引发了关于它们基于什么的问题。最引人注目的构建重现了已经存在的游戏，Berman 克隆了微软射击游戏特许经营权的当前作品《战争机器：E日》的一个关卡，而 Shumer 的大逃杀游戏则借鉴了魔法世界和《堡垒之夜》。

> “这是一个伟大的模型，很多事情都变好了，但并非所有事情都变好了，”

在 Arena 从事 AI 评估工作的 [Peter Gostev](https://www.linkedin.com/in/peter-gostev/) 测试了数十个提示词，并留下了深刻的印象，不过他还没准备好放弃 Opus。“这是一个伟大的模型，很多事情都变好了，但并非所有事情都变好了，”他[在 X 上写道](https://x.com/petergostev/status/2119873616170881192)，并指出其中一项实验花费了 2,618 美元。

*Saltline* 和 Berman 的项目表明，开发者现在可以[交出大量的实现工作](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/)，并在数小时后返回查看可玩或可用的成果。这项工作的成本变得越来越容易衡量，但返回成果的质量仍然需要人类的判断。

原文发布于 [The New Stack](https://thenewstack.io)：“[Anthropic 的 Claude Fable 5.2 仅凭 1 个提示词就造出了一款射击游戏——耗时仅 8 小时，花费 550 美元](https://thenewstack.io/claude-fable-game-demos/)”。