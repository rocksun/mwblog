
<!--
title: 超越Git：AI/ML开发的新协作模式
cover: ./cover.png
-->

Git 经过优化，可处理大量小文件，例如文本文件。仅此一项就使得 Git 不适用于管理此类数据集。

> 译自 [Beyond Git: A New Collaboration Model for AI/ML Development](https://thenewstack.io/beyond-git-a-new-collaboration-model-for-ai-ml-development/)，作者 Gorkem Ercan。

在该领域工作了一段时间的人可能会回忆起数据科学家开始参与项目时，提出了有关与应用程序开发团队协作的问题。

已经建立工作流程的开发团队[使用了 Git](https://thenewstack.io/getting-legit-with-git-and-github-the-art-of-the-commit-message/)，拥有一个精细的 CI/CD 管道，并且可以随意部署到生产环境。

然而，这些团队没有明确的策略与数据科学家协作，后者常常忙于紧迫的功能开发。

该团队紧急审查了数据科学家的工作，仅仅将其视为代码。因此，他们建议数据科学家使用 Git 在各组之间进行协作。这一仓促建议的后果给该行业带来了痛苦。在那个时候，应用程序开发人员对 AI/ML 的了解更少——因此，我也建议使用 Git。

快进近十年，[Git](https://thenewstack.io/git-for-managing-small-projects/) 仍然是数据科学家、应用程序开发人员和[DevOps](https://thenewstack.io/devops/)工程师协作的重要组成部分。然而，这是一次不安的协作。据 Gartner 称，至少 50% 的 AI/ML 模型从未投入生产。而当它们想这么做时，平均需要九个月才能投入生产。

## 为什么我们不能将 Git 用于 AI/ML ？

有许多原因导致[Git 不足以用于 AI/ML 项目](https://thenewstack.io/beyond-code-control-git-for-everything/)。AI/ML 项目需要更多代码才能重现。与直接执行代码的应用程序不同，AI/ML 模型从训练数据中获取其功能。ML 代码用于促进训练。此外，模型的训练和验证需要不同的数据集。因此，AI/ML 需要自动数据版本控制和代码。

说到数据，大部分 AI/ML 项目使用大型非结构化数据集（图像、视频、音频）进行训练，这带来了巨大的存储挑战。另一方面，Git 经过优化，可以处理大量小文件，例如文本文件。仅此一项就使得 Git 不适用于管理此类数据集。

Git 与[应用程序 CI/CD](https://thenewstack.io/ci-cd/) 一起植根于构建易于重现的事实。CI/CD 流水线可以轻松且精确地为应用程序重现给定的工件。对于 AI/ML，情况并非如此。训练 AI 可能既昂贵又耗时，而且是非确定性的。因此，版本系统可能必须携带经过训练的模型工件以进行验证、集成并最终进行生产部署。

在内循环开发（这是开发人员在编写、测试和调试代码时经历的迭代过程）中，AI/ML 与其他应用程序之间也存在差异。AI/ML 内循环由一系列具有不同参数的实验组成。这需要记录和比较实验的背景和细节，以便找到满足验证指标的候选模型。这不仅需要我们选定的模型（冠军模型），还需要候选模型及其实验结果的可用性。

## 介绍 Kitops 及其 ModelKits

我们一直在开发一个名为 kit 的新命令行界面和一个我们称之为 ModelKits 的打包系统；这些工具有助于解决一些常见的痛点。以下是 Kitops、kit 及其 ModelKits 如何改进 AI/ML 协作和部署。

[Kitops](https://github.com/jozu-ai/kitops) 通过 kit CLI 和 ModelKits 引入了一种新颖的协作模型，简化了数据科学家工作与应用程序开发和部署工作流程的集成。

通过采用 ModelKits，团队可以轻松地将 AI/ML 模型、数据集和基本配置封装到标准化、可移植的格式中。这确保了在不同计算环境中无缝共享和协作，促进了数据科学家和开发人员之间的团结和效率。

Kitops 认可 AI/ML 项目对同时进行代码和数据版本控制的独特要求。kitfile 是 AI/ML 项目的中心蓝图，它促进了代码和数据集的版本控制，确保了实验的可重现性和一致性。

ModelKits 旨在管理和分发大型非结构化数据集，而不会受到 Git 面临的限制。通过将数据、代码和序列化模型打包为不同的层，ModelKits 为 AI/ML 项目的存储挑战提供了实用的解决方案。

ModelKits 的不可变性保证了模型从训练到部署的完整性，促进了快速验证、集成和生产准备。这解决了整个行业面临的部署周期冗长的挑战。

该工具包文件允许详细记录 AI/ML 元数据，包括参数和指标，使数据科学家能够比较和选择最适合部署的模型。这种记录保存简化了对性能最佳模型的选择过程，简化了从实验到验证的路径。

## 基于标准的方法

通过将 ModelKits 作为 OCI 工件实施，Kitops 确保了广泛的兼容性，并简化了在任何 OCI 兼容注册表中的共享。这种通用方法允许利用现有的基础设施（例如 DockerHub 或 Quay.io）来存储和检索 AI/ML 工件。ModelKits 的不可变性进一步确保了开发、测试和生产环境的一致性，使 AI/ML 项目像传统软件应用程序一样易于管理。

花点时间熟悉 Kitops，了解它如何简化和丰富您的 AI/ML 项目。Kitops 为管理和协作 AI/ML 开发提供了新的视角。随时访问 kitops.ml，深入了解其功能，或许可以开始您自己的 Kitops 之旅。
