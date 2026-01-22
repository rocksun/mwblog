<!--
title: AI验证瓶颈：开发者负担不减反增
cover: https://cdn.thenewstack.io/media/2026/01/793aeeb7-toil.jpeg
summary: 生成式AI虽提高代码生成速度，但引发验证瓶颈。开发者不完全信任AI代码，导致验证负担增加，技术债务风险上升。需自动化持续验证，实现“先快速生成，后验证”。
-->

生成式AI虽提高代码生成速度，但引发验证瓶颈。开发者不完全信任AI代码，导致验证负担增加，技术债务风险上升。需自动化持续验证，实现“先快速生成，后验证”。

> 译自：[The AI Verification Bottleneck: Developer Toil Isn't Shrinking](https://thenewstack.io/the-ai-verification-bottleneck-developer-toil-isnt-shrinking/)
> 
> 作者：Anirban Chatterjee

软件开发中生成式AI的最初几年，感觉像是一系列越来越令人惊叹的魔术。我们提出复杂的问题，似乎完美的L代码瞬间出现。这种大开眼界的惊叹和早期成功已演变为行业标准：根据Sonar最新的“[代码开发人员调查报告](https://www.sonarsource.com/the-state-of-code/developer-survey-report/)”，72%尝试过[AI编码工具](https://www.sonarsource.com/solutions/ai/)的开发人员现在每天都在使用它们。

AI不再是辅助项目工具；它是生产软件的主要驱动力，58%的开发人员将其用于关键任务工作。

[![72%的开发人员尝试过AI并每天使用它。](https://cdn.thenewstack.io/media/2026/01/02d6820a-image1-1024x495.png)](https://cdn.thenewstack.io/media/2026/01/02d6820a-image1-1024x495.png)

然而，当我们进入AI关键任务实施时代，一个新的风险已经出现，威胁着工程势头：验证瓶颈。我们正在目睹一个根本性的转变，价值不再由编写代码的速度定义，而是由企业部署代码的信心定义。

## **从魔术到关键任务现实**

现代软件工程的核心矛盾在于AI[生成代码](https://thenewstack.io/ai-code-generation-trust-and-verify-always/)的速度与我们人类验证代码的能力之间存在巨大差距。当前生成代码量的爆炸式增长正以惊人的速度推进，开发人员预测，到2027年，他们代码库中[AI辅助代码](https://www.sonarsource.com/solutions/ai/ai-coding-assistants/)的份额将从目前的42%激增至65%——短短两年内增长超过一半。

[![开发人员提交的AI辅助或生成代码的平均份额 — 42%](https://cdn.thenewstack.io/media/2026/01/986bdc64-image3-1024x406.png)](https://cdn.thenewstack.io/media/2026/01/986bdc64-image3-1024x406.png)

然而，这种加速创造了一个许多领导者才刚刚开始面对的叙事：代码量的增加并未直接带来最初所吹嘘的巨大生产力提升。相反，行业已经遭遇瓶颈，代码生成速度加快，但代码审查能力却基本保持不变。

这个瓶颈不仅仅是开发人员速度的问题，更是信任的根本问题。Sonar的研究发现，96%的[开发人员不完全信任AI生成的代码](https://thenewstack.io/ai-and-the-future-of-code-developers-are-key/)在功能上是正确的。这种怀疑根深蒂固于日常经验：61%的[开发人员同意AI经常生成“看起来正确但不可靠”的代码](https://thenewstack.io/arming-developers-with-the-power-of-clean-code/)。

这造成了一种欺骗性的复杂性，未经验证的代码可能会溜入生产环境，因为[开发人员承受着跟上AI驱动速度的压力](https://thenewstack.io/bad-code-stalls-developer-velocity/)。当信任度低但代码量大时，审查过程就变成了一场艰苦的马拉松；38%的[开发人员报告说，审查AI生成的代码](https://thenewstack.io/unraveling-the-costs-of-bad-code-in-software-development/)比审查人类同事编写的代码需要更多的精力。

## **繁琐工作悖论的持续存在**

这种验证的负担正在从根本上重塑开发人员的体验。AI的承诺是消除开发人员的苦差事。尽管75%的开发人员认为AI减少了他们花费在“繁琐工作”上的时间——那些耗费生产力或增加挫败感的任务——但客观数据显示了不同的情况。至少到目前为止，无论开发人员使用AI的频率如何，实际花在繁琐任务上的时间仍保持在每周工作时间的约24%不变。

实质上，AI并未消除繁琐工作；它只是将其性质从代码的创建转移到了代码的验证。这种转变在AI最频繁的用户中尤为明显。这些每天多次使用AI的“高级用户”，更有可能报告与管理技术债务相关的繁琐工作（44%对不常用用户的34%）以及纠正或重写AI工具创建的代码的耗费精力工作（25%对15%）。

[![繁琐工作并未因AI而减少，而是改变了性质：AI的更频繁用户更有可能报告不同领域的繁琐工作。](https://cdn.thenewstack.io/media/2026/01/76d4fb2c-image2-1024x772.png)](https://cdn.thenewstack.io/media/2026/01/76d4fb2c-image2-1024x772.png)

尽管不常用AI的用户仍然与调试遗留代码等传统障碍作斗争，但那些严重依赖AI的用户已经用新的挫败感取代了旧的挫败感。

这种动态表明，我们已经清除了旧的[开发障碍，只是将压力转移到下游](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/)的代码管理和验证。行业必须超越节省繁琐工作的幻想，并认识到起草代码所节省的时间现在正用于[审查和调试AI输出](https://www.sonarsource.com/solutions/ai-code-quality/)以确保其符合生产标准的必要工作中。

## **技术债务困境**

AI代码生成的激增对代码库健康而言，正被证明是一把双刃剑。十分之九的开发人员报告称AI对其技术债务至少产生了一个负面影响，其中主要担忧是创建不必要或重复的代码，以及引入不可靠或有缺陷的结构。

管理技术债务已经是核心开发任务中最大的繁琐工作来源，41%的开发人员将其列为他们最大的挫败感之一。如果不加管理，AI可能会成为加速剂，生成大量具有欺骗性、难以阅读的代码。

欺骗性复杂性的风险尤其有害。因为61%的开发人员同意AI创建的代码看起来正确但不可靠，这可能会产生一种虚假的安全感，导致团队跳过彻底的测试。这种验证债务是AI时代的隐性成本。

[![61%的开发人员同意AI经常生成看起来正确但不可靠的代码。](https://cdn.thenewstack.io/media/2026/01/f58e873a-image4-1024x537.png)](https://cdn.thenewstack.io/media/2026/01/f58e873a-image4-1024x537.png)

相反，十分之九的开发人员也看到了AI对公司技术债务的积极影响。工程师们正在使用AI来解决繁琐的债务任务：57%报告文档得到改进，53%看到更好的测试覆盖率，47%使用AI重构现有代码。数据表明，当AI被明智地使用时，它可能是一个强大的清理工具，同时也会制造新的、更微妙的混乱。

## **打破瓶颈：先快速生成，后验证**

2026年工程领导力的前进道路需要清晰地迈向对所有代码（无论是开发人员生成还是AI生成）的[自动化](https://www.sonarsource.com/solutions/automated-code-review/)、持续验证。成功的团队正在平衡AI生成代码的速度与[维护代码健康所需的严格监督](https://thenewstack.io/ai-generated-code-requires-a-trust-and-verify-approach/)。为了充分发挥这些工具的潜力，我们必须将对它们的评估范围从简单的性能基准扩展到包含[安全性](https://www.sonarsource.com/solutions/security/)、[可靠性](https://www.sonarsource.com/solutions/reliability/)和[可维护性](https://www.sonarsource.com/solutions/maintainability/)等关键属性。

在下一个时代，赢家将是那些成功采用“先快速生成，后验证”工作流程的团队。这不仅仅是向流程中添加更多人工审查员；而是要建立一个系统，在不损害代码库长期健康的情况下，从AI的速度中提取价值。这不再是谁能发布最多代码的问题，而是谁能将快速生成与确保安全、可维护软件所需的自动化和全面的保障措施相结合。