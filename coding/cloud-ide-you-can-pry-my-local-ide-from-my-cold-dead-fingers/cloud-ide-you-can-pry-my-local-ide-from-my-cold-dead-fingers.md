<!--
# 用云替代我的本地IDE？除非你先杀了我
https://cdn.thenewstack.io/media/2023/11/e017d708-rb19-1024x521.jpg
 -->

我真的非常不想要一个在线集成开发环境(即云IDE)。为什么在一个痴迷于云的世界里，本地IDE仍然占据统治地位。

> 译自 [Cloud IDE? You Can Pry My Local IDE from My Cold, Dead Fingers](https://thenewstack.io/cloud-ide-you-can-pry-my-local-ide-from-my-cold-dead-fingers/) 。
作者 Liam Crilly是F5 NGINX的产品管理高级总监，他于1993年编写了第一个Web应用程序，从那时起一直热衷于互联网软件工作。Liam领导NGINX Unit孵化小组，这是一个开源应用服务器、Web服务器和反向代理。

我的朋友们知道我是一个汽车发烧友和改装迷。我确实如此。我喜欢钻研改装。我喜欢研究发动机。当我在赛道上时，我明白汽车为什么以这样的方式运行——以及我可以做些什么来优化或修改任何参数。

我的车是我的王国，是我开心的天堂。因此，即使你给我 Max Verstappen 驾驶的[一级方程式RB19赛车](https://en.wikipedia.org/wiki/Red_Bull_Racing_RB19)的方向盘，让我开一圈，我也会很高兴，但这种乐趣只会持续一小会。驾驶那辆车一定很刺激，但对我来说也更加危险。我可能会不习惯那么强大的性能，并且难以掌控这台机器。

这就是为什么我真的非常不想要一个在线集成开发环境(即[云IDE](https://en.wikipedia.org/wiki/Online_integrated_development_environment))。科技界的酷孩子们正在力推[开发的最后堡垒——IDE的云化](https://thenewstack.io/are-cloud-based-ides-the-future-of-software-engineering/)。虽然Visual Studio Code已经部分上云了相当长的时间，但新版本如[GitPod](https://thenewstack.io/the-goldilocks-cde-gitpod-fits-between-saas-and-self-hosted/)和Cloud9的云化程度更高。也就是说，零本地软件。零本地存储。零控制力。我只能在IDE规定的范围内进行自定义，但远不如我对本地开发环境的各种自定义。

换句话说，我只能在云上运行Nix。不要Nix。以下是你必须干掉我夺走IDE方向盘的原因。

## 本地IDE: 你个性化的舒适圈

就像大厨的厨房或机修工的工作台一样，你的本地IDE是一个经过个性化调教的神圣空间，让你感到舒适。作为一个周末竞速族，我特别理解这一点，尽管我的手指经常在机油下变脏。当然，我们都需要共享的工具和功能来获得完整高效的开发体验。但是IDE决不能成为一成不变的软件。我们需要自定义的快捷键、插件、脚本、命令行工具以及所有让我们舒适编码的东西。云正朝着错误方向发展。以下是三个原因。

### 本地控制: 对速度的需求

有很多任务你肯定希望本地运行 —— 格式化、语法检查、单元测试、构建测试以及所有[本地“无聊”运行不太有趣](https://thenewstack.io/automate-the-boring-stuff-with-kubernetes/)，但在云上更糟糕的东西。想象你被一个拥堵的云CI/CD系统排在后面。你会感觉像F1赛车手被安全车卡在后面。

### 宕机: 意想不到的维修站

宕机很少见，但确实偶有发生。无论是DDoS攻击、核心互联网基础设施故障，还是咖啡店Wi-Fi不稳定，本地运行意味着你永远不会被这些意外事故限制。就像F1赛车手准备好备用前翼，你可以继续无障碍工作。

### 复杂性: 控制的错觉

运行本地IDE看似更复杂。但实际上，[它与云IDE的复杂性相同](https://thenewstack.io/why-cloud-ides-are-shifting-to-a-platform-as-a-service-model/) —— 不同的是你控制它。你的DevEx团队可能仍会限制工具选择和控制版本，以使每个人看到相同的基本工具和输出，这样本地测试仍可广泛适用于整个团队或组织。然而，这与被强制快速大规模地切换到云IDE截然不同。

## 编码不是一成不变的。你的IDE也不应该是。

叫我老派。叫我云计算反对者。但我永远不会选择使用云IDE开发软件。拜托，拜托不要考虑夺走我的本地IDE来“同步”我的开发环境与团队其他人。

我理解平台团队为什么会被减少选择来设置规范的想法所吸引。我们在[NGINX](https://www.nginx.com/)这里也经常讨论这一点。但是一个云IDE基本上就像强迫我坐在一个陌生和不舒服的驾驶舱里。我会变慢，犯更多错误，并花费大量时间等待CI/CD作业在广袤的云数据中心运行。当不可避免的故障来临时，我的云IDE将停止响应，而我只能等待遥远的云服务器机械师来修复。
