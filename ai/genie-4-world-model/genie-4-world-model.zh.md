**Google DeepMind于周二推出了Genie 4**，这是一个能够通过模拟物理学、人类运动和原生音频实时渲染交互式环境的世界模型。这些逼真的演示令人印象深刻，但对于任何[构建AI智能体](https://thenewstack.io/ramp-laminar-agent-harness/)的人来说，真正的吸引力在于Genie 4为它们提供了一个在正式执行前运行多步骤任务的场所。

Google DeepMind的研究总监[Tejas Kulkarni](https://www.linkedin.com/in/tejas-kulkarni-56042214/)在[新闻发布会](https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/)上将这种方法描述为迈向“这些混合世界模型”的一步，其中Gemini负责编写代码和文本，而Genie则将其转化为运行中的场景。这为开发人员提供了一种按需生成测试环境的方法，尽管这些模拟在多大程度上反映了现实世界的条件仍然是一个关于[可靠性](https://thenewstack.io/liquid-ai-reward-hacking/)的开放性问题。

> 它为开发人员提供了一种按需生成测试环境的方法。

## Gemini如何引导Genie 4

[Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)使用多个Gemini模型来保持模拟的运行。[Gemini Omni](https://deepmind.google/models/gemini-omni/)帮助塑造环境，而Gemini 3.8 Flash则负责跟踪正在发生的事情、规划下一步并在发生变化时进行调整。

Genie 4不会生成一个成品的视频，而是让用户在世界生成的同时与其进行交互。他们可以用键盘在其中移动、改变摄像机角度或使用文本提示来改变环境，而无需重新启动模拟。

> Genie 4不会生成一个成品的视频，而是让用户在世界生成的同时与其进行交互。

## 在模拟中排练机器人

谷歌最清晰的例子是让Apptronik的Apollo人形机器人参与[西洋棋游戏](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)，Gemini 4 Argon规划每一步行动，而Genie 4则在字幕引导场景的同时渲染结果。

该公司还在探索该技术如何支持其[Gemini Robotics](https://deepmind.google/models/gemini-robotics/)研究，该研究使开发人员能够在不断变化的环境中测试智能体，而不必从头开始重建每个模拟。

## 物理学在哪里崩溃了

问题在于，Genie 4并不能总是保持这些环境的一致性。在较长时间的会话中，物体可能会发生位置偏移或表现出不可预测的行为，谷歌也承认物理学并不总是准确的。

这使智能体评估变得复杂，特别是当任务涉及[记住位置或返回早期状态](https://thenewstack.io/letta-frontiermemory-agent-harness-benchmark/)时。一次失败的运行可能反映出智能体本身或模拟本身的问题，而且谷歌尚未证明Genie 4能够在高风险测试中取代传统的物理引擎。

游戏开发者正在使用Genie 4在编写引擎代码之前探索原型和测试游戏机制，而企业合作伙伴则在寻找生成自己的测试场景的方法。

> 该公司尚未发布基准测试，以展示Genie 4在重复智能体测试中的表现。

该公司尚未发布基准测试，以展示Genie 4在重复智能体测试中的表现。这包括相同的提示是否会产生一致的结果，这使得开发人员在决定是否将其用于自动化测试时几乎无据可依。

## 谁能获得Genie 4的访问权限

目前，只有受信任的测试人员才能访问。谷歌计划通过Project Genie向Google AI Ultra订阅者扩大可用性，并向通过Gemini API和Google AI Studio选择的合作伙伴开放。目前还没有关于定价、更广泛发布或性能保证的消息。