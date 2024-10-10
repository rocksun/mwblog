# 人工智能模型中克服灾难性遗忘的技术

![关于“克服人工智能模型中灾难性遗忘的技术”的特色图片](https://cdn.thenewstack.io/media/2024/09/e63683f1-shubham-dhage-ryeilkgiveo-unsplash-1-1024x576.jpg)

尽管[机器学习](https://thenewstack.io/how-machine-learning-works-an-overview/)模型取得了巨大进步，但专家们仍在努力解决确保[机器不会忘记之前学习的知识](https://thenewstack.io/lifelong-machine-learning-machines-teaching-other-machines/)的问题，尤其是在学习新知识时。

这个问题被称为[灾难性遗忘](https://towardsdatascience.com/forgetting-in-deep-learning-4672e8843a7f)或灾难性干扰。当人工神经网络的权重被优化以学习新任务时，就会发生这种情况，这反过来会干扰存储在相同权重中的先前知识。当人工智能模型解析新输入时，模型内部表示之间的统计关系可能会发生变化、混合或重叠，这可能导致性能下降（或“[模型漂移](https://c3.ai/glossary/data-science/model-drift/)”），或者（最糟糕的是）模型突然急剧地忘记其先前的训练。

## 灾难性遗忘的原因

导致模型“遗忘”的因素有很多。这些因素包括[过拟合](https://www.datacamp.com/blog/what-is-overfitting)模型到新的训练数据、模型容量有限、共享参数、使用不适合任务的训练技术以及缺乏[正则化](https://www.ibm.com/topics/regularization)。

然而，一些专家指出，灾难性遗忘背后的确切机制尚未完全了解。

“虽然在[持续学习](https://wiki.continualai.org/the-continualai-wiki/introduction-to-continual-learning)领域有很多[研究](https://paperswithcode.com/task/continual-learning)通过算法设计来研究如何实验性地解决灾难性遗忘，但人们仍然缺乏对哪些因素很重要以及它们如何影响灾难性遗忘的理解，”休斯顿大学计算机科学系助理教授[Sen Lin](https://www.linkedin.com/in/sen-lin-96821928b/)解释说，他也是最近一篇关于灾难性遗忘对持续学习影响的[研究](https://arxiv.org/pdf/2302.05836)的合著者。“我们的研究通过揭示三个重要因素：模型过度参数化、任务相似性和任务排序，以及它们对学习性能的影响，填补了这些空白。”

## 克服灾难性遗忘

总的来说，防止灾难性遗忘的方法可以分为三大类：正则化、基于记忆的技术和基于架构的方法。

**正则化技术**在训练模型以执行新任务时，保留对旧任务重要的有意义的权重参数。这些包括：

* **弹性权重合并 (EWC)**：一种[技术](https://pub.towardsai.net/overcoming-catastrophic-forgetting-a-simple-guide-to-elastic-weight-consolidation-122d7ac54328)，它量化了模型先前学习的任务中每个权重的重要性，并对这些关键权重的任何重大变化进行惩罚，从而激励模型保留现有知识。
* **突触智能 (SI)**：这种方法通过计算每个权重对模型性能的影响并保护对新任务至关重要的权重，从而构建了一种自适应的防遗忘保护机制，从而在旧知识和新知识之间取得平衡。
* **不遗忘学习 (LwF)**：这是最早缓解灾难性遗忘的方法之一，它是一种[增量学习方法](https://arxiv.org/pdf/2107.12304)，它结合了蒸馏网络和微调，以便在学习新任务期间保留原始知识。

**基于架构的技术**是对模型架构的修改，可以帮助“冻结”旧任务的关键参数以适应新任务学习，或者在需要更多模型容量时增加模型大小。这些方法包括：
**渐进式神经网络 (PNN 或 ProgNets)**：一种[基于列的方法](https://towardsdatascience.com/progressive-neural-networks-explained-implemented-6f07366d714d)，其中为每个任务训练单独的神经网络列，使用横向连接将新信息从先前学习的任务转移到新任务，而不是覆盖它们。**专家门模块**：这种“网络中的网络”概念利用一个基本网络，该网络通过其他子网络为每个任务增强，每个子网络都配备了一个自动编码器，使其成为其任务的“专家”。训练后，每个模型的参数被“冻结”，只有相关的“专家”解决它被设计解决的任务，并保留一个共享的“主干”或知识库。**动态可扩展网络 (DEN)**：这种[技术](https://arxiv.org/pdf/1708.01547)允许模型决定其需要的网络容量，为每个新任务添加新的神经元和连接，并“修剪”任何冗余链接。

**基于记忆的技术**有助于将有关旧任务的信息存储到某种记忆存储中，然后模型可以使用该存储在当前任务学习期间“重放”信息。

**记忆重放**：模型保留先前训练数据的子集，这些子集用于将来对模型进行定期重新训练，这有助于“提醒”它们过去的信息。**生成式重放**：合成样本由[生成对抗网络](https://thenewstack.io/deepprivacy-ai-uses-deepfake-tech-to-anonymize-faces-and-protect-privacy/)(GAN)生成，这些网络模仿以前的数据集，并用于强化模型的先前学习。一个缺点是，生成的数据通常比原始数据质量低。**记忆增强网络**：模型配备了[外部记忆模块](https://medium.com/data-science-in-your-pocket/neural-turing-machines-explained-9acdbe8897de)，增强了它们存储和检索先前学习的能力，从而防止遗忘。**清醒-睡眠合并学习 (WSCL)**：根据最近[研究](https://arxiv.org/pdf/2401.08623)的一位作者，卡塔尼亚大学 PeRCeiVe.AI 实验室的教授[Concetto Spampinato](https://www.linkedin.com/in/concetto-spampinato-40652110/)，这是一种受生物学启发的“模仿大脑清醒-睡眠周期的”方法。在睡眠阶段，WSCL 不仅重放记忆，而且还做梦——模拟新的体验——帮助模型更有效地适应未来的任务。这种梦境功能是独一无二的，使我们的方法比简单地存储旧数据更具动态性。”

还可以通过使用**混合方法**进一步定制这些技术，其中将上述两种或多种方法组合起来，以绕过任何一种方法的局限性。例如，[变分持续学习 (VCL)](https://arxiv.org/abs/1710.10628)集成了弹性权重巩固 (EWC) 和生成式重放 (GR)，既可以规范模型权重，又可以通过变分自动编码器重放旧的训练数据。

尽管有如此众多的潜在解决方案，但尚未找到灾难性遗忘的通用解决方案。随着人工智能模型变得越来越大、越来越复杂和越来越通用，灾难性遗忘仍然是持续学习中需要克服的关键障碍。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)