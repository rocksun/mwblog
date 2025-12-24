在开源软件 (OSS) 领域工作有时感觉像在永不停止的跑步机上奔跑。你所依赖的项目不断前进，但如果你错过一步，就会被甩到后面。对于许多开发者来说，这是一场无休止的竞赛，以跟上不断变化的依赖项、紧急的常见漏洞和披露 (CVEs) 以及新功能。

但并非所有开源项目都以这种速度发展。它存在于一个从快速发展、功能丰富的项目到悄然废弃的项目之间的光谱上。介于两者之间的是最被忽视的类别：[那些“已完成”](https://thenewstack.io/chainguard-takes-over-maintenance-of-aging-oss-projects/)并准备进入长期维护阶段的软件。

“已完成”的软件应该受到赞扬。它最终让开发者能够摆脱跑步机，而无需担心脚下的地面会发生变化。

## **“已完成”软件被低估的价值**

并非每个开源项目都需要永远冲刺。有些项目达到核心功能完成、设计稳定且用户群满意的程度。“已完成”的项目成为可靠、可预测的安静基础设施，只需要偶尔的维护。

[Ingress-nginx](https://github.com/kubernetes/ingress-nginx/) 是一个早在社区意识到之前就已经“完成”的项目的例子。它是 Kubernetes [最流行的开源 Ingress 控制器](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/)之一，为全球数据中心和家庭实验室的数十亿请求提供支持。尽管其被大规模采用，但该项目从未有超过一到两名维护者在业余时间为其贡献。就在上个月，Kubernetes 社区[宣布决定在 2026 年 3 月归档该项目](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)。

当一个项目达到“完成”阶段时，这是一项成就。代码稳定，设计合理，社区依赖于它。这些项目是健康、持久生态系统的基础，这意味着它们仍然需要偶尔的维护，以便依赖它们的社区可以安全地使用它们。

## **扩展对“已完成”项目的支持**

如今，数量惊人的开源项目[只有一名或极少数维护者](https://anchore.com/blog/open-source-is-bigger-than-you-imagine/)。当维护者想要离开时，人们仍然依赖该项目，但没有人正式负责其长期维护。

去年的 [xz-utils 事件](https://arstechnica.com/security/2024/03/backdoor-found-in-widely-used-linux-utility-breaks-encrypted-ssh-connections/)向我们展示了当没有安全地移交项目的途径时会发生什么。当 xz-utils 的原始维护者——一个尽职尽责管理其维护长达 20 年的个人——想要离开时，一个新的贡献者逐渐获得了信任，却[差点植入了一个复杂的后门](https://thenewstack.io/unzipping-the-xz-backdoor-and-its-lessons-for-open-source/)。如果那次攻击成功了，它几乎可以瘫痪所有主要系统。

我们需要一种方式，让开源维护者即使在不再有重要的功能路线图时，也能优雅地[移交“已完成”的项目](https://chainguard.dev/unchained/introducing-chainguard-emeritoss)。我们需要为他们提供一个这样的地方：

*   成熟项目可以从个人维护者过渡到负责长期维护的受信任组织。
*   即使没有新功能开发，CVEs 也能持续得到修补。
*   在没有每周提交的情况下，可再现性和信任依然存在。

这种“毕业”应该表明该项目是稳定的、有价值的，并已准备好在共同责任的支持下长期存在。

## **分叉是开源的关键优势**

对废弃的软件进行分叉是社区将其恢复到“完成”状态的方式。[Kaniko](https://thenewstack.io/kaniko-lives-on-chainguard-forks-googles-dumped-tool/) 是这方面最清晰的例子之一。当 Chainguard [分叉并接管其维护](https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back)时，我们继承了一个已经运作良好、数千人依赖的工具。我们承担了对一个实际上已完成的项目进行长期托管的角色。Kaniko 需要可预测、负责任的监督，每年进行偶尔的更新和小修补。它不需要新功能。如今，当团队想要新功能时，他们可以从受信任的来源分叉 Kaniko 并自行构建这些功能。

分叉为团队提供了一条在稳定基础上进行构建的途径，而不会扰乱项目的核心目的。它们保留了用户选择，防止倦怠，并在不破坏核心稳定性的情况下允许创新。最重要的是，它们确保开源保持开放，并可以自由发展到社区需要它去的任何地方。

## **构建可持续的未来之路**

开源总会有向前冲刺的项目和落后的项目，但健康生态系统的未来是确保成熟软件有一个安全的归宿。通过为“已完成”的软件建立毕业路径，赋能维护者安全地离开，并鼓励组织承担长期托管角色，我们可以预防下一次 xz-utils 式的恐慌。

如果在 OSS 中工作有时感觉像在跑步机上奔跑，那么“已完成”的软件就是节奏终于放缓的难得时刻。通过采纳可持续的维护和将分叉作为开源生命周期的一部分，我们可以建立一个未来，在那里，从跑步机上走下来是成功的标志，而非失败。