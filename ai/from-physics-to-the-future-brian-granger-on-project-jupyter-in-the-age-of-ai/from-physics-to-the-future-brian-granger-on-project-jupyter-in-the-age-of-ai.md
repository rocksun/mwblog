<!--
title: 从物理到未来：Brian Granger洞见AI时代的Jupyter项目
cover: https://cdn.thenewstack.io/media/2025/11/491cff03-thumbnail-22.png
summary: Jupyter联合创始人Brian Granger谈开源可持续性。Jupyter基于物理学模块化理念，AI赋能项目快速迭代，重塑技术债务管理。获ACM奖项后，团队更关注用户需求和未来发展。
-->

Jupyter联合创始人Brian Granger谈开源可持续性。Jupyter基于物理学模块化理念，AI赋能项目快速迭代，重塑技术债务管理。获ACM奖项后，团队更关注用户需求和未来发展。

> 译自：[From Physics to the Future: Brian Granger on Project Jupyter in the Age of AI](https://thenewstack.io/from-physics-to-the-future-brian-granger-on-project-jupyter-in-the-age-of-ai/)
> 
> 作者：Michelle Gienow

如果你能在短短30分钟内，从零开始重写一个备受喜爱的、经过实战检验的开源服务器，并配备全新的测试套件，会怎么样？对于Project Jupyter的联合创始人、[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)的高级首席技术专家Brian Granger来说，这不再是一个思想实验，而是正在从根本上改变我们对开源可持续性思考方式的现实。

在本期《The New Stack Makers》的“在路上”节目中，Granger在圣地亚哥的JupyterCon会议上与TNS主编Heather Joslyn坐下来，讨论了Jupyter的起源、该项目获得的ACM软件系统奖，以及AI如何改变大型开源项目的可能性。

## 灵活架构的物理学

Granger在科罗拉多大学攻读博士学位时首次接触计算笔记本，在那里他还与研究生同学、[iPython交互式shell](https://ipython.org/ipython-doc/3/interactive/index.html)的创建者Fernando Pérez成为了朋友。

Granger回忆说：“我们俩都是在物理学背景下成长起来的，使用Mathematica，当[Python](https://thenewstack.io/what-is-python/)出现时，我们真的希望在Python中也能拥有相同的笔记本体验。”

几年后的一次深夜谈话中，Granger和Pérez提出了构建iPython Notebook的愿景，这是一种Python形式的基于网络的笔记本，最终演变为Jupyter Notebooks。

他们共同的物理学训练塑造了Jupyter的架构。Granger说：“牛顿方程非常模块化和可扩展。你可以使用牛顿定律模拟宇宙中几乎任何经典系统。量子力学或狭义相对论也是如此。我们想要少量能够解决大量问题的构建块。我认为我们做对了。”

这些模块化、灵活、可扩展的构建块——笔记本格式、内核消息协议以及Jupyter Server和JupyterLab扩展的高级API——已被证明异常耐用，即使[它们周围的生态系统](https://thenewstack.io/jupyter-ai-v3-could-it-generate-an-ecosystem-of-ai-personas)已经[显著演变](https://thenewstack.io/deepnote-a-successor-to-jupyter-notebook-goes-open-source/)。

## 重写技术债务规则

Jupyter是在数据科学、人工智能（AI）和机器学习（ML）刚刚兴起的世界中构建的——但这可能正是它长寿的秘诀。

Granger说：“Jupyter并非为软件工程或应用程序构建而设计。它是为了解决需要人类推理和思考复杂、混乱场景的难题。对于我们现在所处的时代，我们所有人——字面上是每个人——都在试图弄清楚‘我们如何利用AI？’，最初的用例只会变得更强大。”

该团队现在正在使用AI来构建Jupyter，这带来了“更多的乐趣和速度上的显著变化”。

Granger描述了最近一项实验，在AI编码代理的帮助下，将Jupyter Servers从Python重写为Go。

他说：“大约半小时后，我就有了一个全新的实现，它遵循这个开放API规范，并且有一个覆盖率达到70%的测试套件。以前，一想到要从头重写Jupyter Server，我们就会立即将其视为彻头彻尾的疯狂之举。我们有更重要的事情要做，它久经考验，别碰它。但现在，突然之间，它成为一个选项。”

Granger说，这种速度的转变正在从根本上改变团队处理[技术债务](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/)、沉没成本和优先级的方式。“对于像Jupyter这样的大型开源项目的技术可持续性而言，AI将发挥非常重要的作用。”

## 认可带来责任

2017年，Granger获得了美国计算机协会（Association for Computing Machinery）的软件系统奖——这使得Jupyter与Unix、Java和万维网齐名。这伴随着一个清醒的现实检验。

Granger指出：“这部分也是承认Project Jupyter不再是我们的爱好，尽管我们许多人像对待爱好一样享受它。在学术研究和教育领域，有整个行业每天都依赖Jupyter。”

这种认可带来了关于可持续性和竞争的问题，使得他将重心集中在社区的未来。“如果有什么事情让我们彻夜难眠，那就是Jupyter因为人们开始使用其他东西而缓慢消亡，”他说。“我们非常积极地去了解用户的需求，为他们服务，并构建他们喜欢的东西。”

观看完整节目，了解更多Jupyter的起源故事，治理挑战为何让团队措手不及，以及该项目如何在AI时代航行，同时坚守其赋能思考、协作和知识共享的使命。