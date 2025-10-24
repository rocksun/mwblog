<!--
title: Ray 重磅入驻 PyTorch 基金会
cover: https://cdn.thenewstack.io/media/2025/10/2b2503d6-a576b97e-89e1-43b6-b528-b93fb53b8e46-scaled.jpg
summary: Ray（分布式计算框架）加入PyTorch基金会，以整合关键AI组件，赋能大规模AI模型开发、部署和扩展。
-->

Ray（分布式计算框架）加入PyTorch基金会，以整合关键AI组件，赋能大规模AI模型开发、部署和扩展。

> 译自：[Ray Comes to the PyTorch Foundation](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/)
> 
> 作者：Frederic Lardinois

[PyTorch基金会](https://pytorch.org/foundation/)，一个基于Linux基金会的开源AI组织，今天宣布，它将成为[Ray](https://github.com/ray-project/ray)的主办方，Ray是一个流行的开源分布式计算框架，用于扩展AI和Python应用程序。Ray项目将加入PyTorch本身、vLLM推理引擎和深度学习优化库DeepSpeed等现有项目。

Ray最初是在加州大学伯克利分校的[RISELab](https://rise.cs.berkeley.edu/people/)孵化的。当时的博士生Robert Nishihara和Philipp Moritz于2016年启动了这个项目。他们与教授（也是Databricks的联合创始人）[Ion Stoica](https://www.linkedin.com/in/ionstoica/)共同决定[创立Anyscale](https://www.anyscale.com/press/founders-of-open-source-project-ray-launch-anyscale-with-usd-20-6m-in-funding-to-democratize-distributed-programmingfounders-of-open-source-project-ray-launch-anyscale-with-usd-20-6m-in-funding-to-democratize-distributed-programming)，以将其工作商业化。自那时起，Anyscale已筹集超过2.5亿美元，并围绕Ray推出了各种产品；与大多数开源公司一样，它也提供了一个托管平台，将这些服务中的许多整合到一个企业级平台中。

[Ray核心项目](https://docs.ray.io/en/latest/ray-core/walkthrough.html)本身为构建基于Python的分布式应用程序提供了基本原语（称为任务、actor和对象）。值得注意的是，Ray的核心部分不仅限于AI应用程序，还可用于扩展任何Python工作负载。但Ray项目还包括用于管理机器学习（ML）数据集和处理分布式训练的AI专用库，以及用于模型调优和服务的库。Ray还包括一个用于[扩展强化学习工作负载](https://docs.ray.io/en/latest/rllib/index.html)的库。

Anyscale联合创始人Nishihara表示：“在Ray，我们的目标是让分布式计算像编写Python代码一样简单。加入PyTorch基金会帮助我们忠于这一使命，确保Ray继续成为开发者及其组织的开放、社区驱动的支柱。”

自推出以来，Anyscale一直独立维护Ray开源项目（尽管它偶尔被错误地标记为“Apache Ray”）。

[![](https://cdn.thenewstack.io/media/2025/10/b898508a-ray-stack.png)](https://cdn.thenewstack.io/media/2025/10/b898508a-ray-stack.png)

*图片来源：Anyscale。*

对于PyTorch基金会而言，Ray的加入意味着它现在为AI生态系统提供了一些最基础的开源项目。基金会认为，有PyTorch用于模型开发，vLLM用于推理，以及Ray用于分布式执行。

Linux基金会AI总经理兼PyTorch基金会执行董事[Matt White](https://www.linkedin.com/in/mdwdata/)表示：“通过将Ray与vLLM和DeepSpeed等项目一同纳入PyTorch基金会的旗下，我们正在整合构建下一代AI系统所需的关键组件。Ray的加入强化了我们的共同使命，即为开发者提供工具，以高效地大规模训练、服务和部署AI模型。”