# DevOps 并未消亡，但也不健康

![Featued image for: DevOps Isn’t Dead, but It’s Not in Great Health Either](https://cdn.thenewstack.io/media/2024/04/e399a014-kristine-wook-e1_rw3hibuw-unsplash-1024x768.jpg)

西雅图——在 [北美开源峰会 (OSSummit)](https://events.linuxfoundation.org/open-source-summit-north-america/) 联合举办的 [持续交付基金会 (CDF)](https://cd.foundation/) 在其第五届年度 [CI/CD 状态报告](https://cd.foundation/state-of-cd-2023/) 中报告称，虽然 83% 的开发人员积极参与 DevOps，但部署指标中表现不佳的比例却令人担忧地增加。

这意味着什么？DevOps 的宗旨是让开发人员和系统管理员能够更快、更高效地完成软件工作。但事实并非如此。

在 [SlashData 的开发者国度](https://www.developernation.net/developer-reports/dn23) 对数万名开发人员进行的调查中，只有 14% 的开发人员能够在一天内将代码投入生产。这与 SlashData 在 2020 年第三季度开始提出这个问题时的情况大致相同。至于每天部署代码多次，实际上已经从 2020 年的 11% 降至 9%。

只有 11% 的 DevOps 用户报告称能够在不到一小时内恢复服务。

这不是持续集成/持续交付 ([CI/CD](https://thenewstack.io/ci-cd/)) 的全部意义吗？是的，没错。

我们使用 DevOps 的另一个原因是，当出现问题时——而问题总是会发生，通常是在老板盯着你时——你可以快速恢复并正常运行。但事实并非如此。

只有 11% 的 DevOps 用户报告称能够在不到一小时内恢复服务。好吧，这很难。但情况并没有比几年前好多少。更糟糕的是，如今，41% 的用户报告称需要超过一周才能恢复服务。在 2020 年，34% 的用户可以在一周多一点的时间内恢复正常运行。

那么，问题出在哪里？报告的作者推测，“可能是 DevOps 实践的普遍性使得开发人员和组织能够增加他们参与的项目的复杂性，从而抵消了对开发速度的益处。换句话说，DevOps 实践可能使复杂项目的开发速度与没有 DevOps 实践的简单项目相当。”

他们还指出：“随着 DevOps 的成熟，开发人员从探索空间转向只关注他们认为最有用的技术。然而，有用性并不总是与部署性能直接相关。”

这是一个需要解决的脱节。仅仅因为你喜欢，比如 [Jenkins](https://www.jenkins.io/)，但所有使用 [GitHub Actions](https://github.com/features/actions) 的团队都更有效率，就说明你需要重新考虑你正在使用的 DevOps 工具。

顺便说一下，报告指出，使用多个 CI/CD 工具是一个错误。“当使用相同形式的多个 CI/CD 工具时，部署性能会更差。研究人员推测，这是因为存在互操作性挑战。

另一个相关问题是，虽然使用更多 DevOps 工具的人的部署速度往往更快，但他们也增加了工作中的心理负担。一个特别令人困扰的例子是警报疲劳。当一个接一个的程序不断地用一个接一个的警报向你发出警报时，很容易停止关注，让真正的问题滑入你的生产管道。

话虽如此，不要把生产力这个孩子和 CI/CD 这盆脏水一起倒掉。掌握多种工具的开发人员往往比工具箱里没有多少程序的同行完成更多工作。

正确使用——请注意我说的是正确使用——CI/CD 管道的使用与所有 [DevOps 研究与评估](https://thenewstack.io/limitations-in-measuring-platform-engineering-with-dora-metrics/) (DORA) 指标的更好部署性能密切相关。使用不当；那就是另一回事了。

我还发现 CI/CD 使用率略有下降，这令人不安。在 2023 年第三季度，33% 的开发人员使用 CI 自动构建和测试他们的代码更改。在 2024 年第一季度，这一比例降至 29%。同样，2023 年第三季度有 29% 的开发人员使用 CD 自动化他们的代码部署。在 2024 年第一季度。这一比例为 29%。

这里发生了什么？

我认为现在是时候让公司开始问自己什么是正确的组合了。他们需要专门使用 DevOps 和 CI/CD 工具来最大限度地发挥它们的优势。它们是有帮助的。除了顽固不化的人之外，没有人会怀疑这一点。但是，它们似乎不像应该的那样有用。

也许 CIF 和其他供应商中立的 DevOps 组织应该认真思考一下我们如何使用这些程序。这里似乎有些不对劲。

[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等。

[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)