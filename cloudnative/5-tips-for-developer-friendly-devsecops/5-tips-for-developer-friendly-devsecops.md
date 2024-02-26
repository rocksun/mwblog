<!--
title: 5个开发者友好型DevSecOps提示
cover: https://cdn.thenewstack.io/media/2024/02/d8e10650-dice-765525_1280-1024x602.jpg
-->

以下是五个提升开发者DevSecOps体验的技巧，重点是使安全工具更易用，以解锁更快发布更安全产品的能力。

> 译自 [5 Tips for Developer-Friendly DevSecOps](https://thenewstack.io/5-tips-for-developer-friendly-devsecops/)，作者 Nick Liffen 是 GitHub 的 GitHub 高级安全主管。他认为“向左转”并不足够，但在 GitHub 所做的一切都以开发者为先是推动可行成功的关键。

DevSecOps 将安全放在[软件开发生命周期](https://thenewstack.io/googles-duet-ai-launches-genai-across-full-sdlc-in-the-cloud/)（SDLC）的核心，提供了诸如减少风险、降低补救成本（[IBM](https://www.ibm.com/?utm_content=inline-mention) 报告指出，采用高度 DevSecOps 的组织可节省多达 [168 万美元](https://www.ibm.com/reports/data-breach?utm_content=SRCWW&p1=Search&p4=43700077724063991&p5=e&gclid=CjwKCAiAu9yqBhBmEiwAHTx5pxBHz4SuILQAVmxIm2_f4iWKGnZtXURRY1mZrnv7TSDLFH7vXUo7MxoCHMkQAvD_BwE&gclsrc=aw.ds)）以及更快、更安全的产品发布等好处。然而，尽管 DevSecOps 的优势很多，开发者在日常 DevSecOps 实践中经常面临来自碎片化工具整合和额外责任的挑战，这使得 SDLC 看起来更加复杂和具有挑战性。

[DevSecOps](https://thenewstack.io/meet-the-new-devsecops/) 策略旨在将安全责任分散到团队，而不是将其孤立，因此确保安全是开发者体验的自然组成部分至关重要，才能充分利用其优势。以下是五个增强开发者 DevSecOps 体验的建议，重点是使安全工具更易用，以解锁更快发布更安全产品的能力。

## 1. 将安全性融入现有工作流程中

许多安全工具是为[安全专业人员](https://thenewstack.io/why-testing-must-shift-left-for-microservices/)构建的，因此简单地将它们添加到现有的开发者工作流程中可能会产生摩擦。当希望将新工具集成到 SDLC 时，考虑[从安全工具中提取所需数据，并将其原生集成到开发者的工作流程中](https://thenewstack.io/adding-security-to-the-developers-workflow/) —— 或者更好的是，寻找已经嵌入到流程中的工具。这样可以减少上下文切换，并帮助开发人员更早地检测和修复漏洞。此外，在集成开发环境（IDE）中利用人工智能工具进一步简化了流程，使开发人员可以在不离开编码环境的情况下处理安全警报。

## 2. 设置警报优先级

将[安全引入开发过程还意味着纠正警报](https://thenewstack.io/automated-security-alert-remediation-a-closer-look/)，但仅要求开发人员纠正所有安全警报是不现实的。一连串的警报，特别是误报，可能会削弱开发人员对工具的信任，影响其生产力。一个良好集成的安全工具应该有一个警报系统，直接向开发者显示高优先级的警报 —— 例如，基于自定义和自动分类规则的警报设置、可过滤的代码扫描警报以及解除警报的能力有助于构建更有效的警报系统。这确保开发人员可以迅速解决紧急的安全问题，而不会被不必要的噪音所淹没，并有助于最终清理组织的安全债务（如果随着时间的推移积累，修复起来可能变得更加困难和昂贵）。

## 3. 与人工智能和自动化保持友好

嘈杂的警报、系统复杂度增加、资源有限以及威胁迅速演变，使得开发人员难以跟上漏洞。好消息是，人工智能和自动化可以通过减少误报、实现一致的安全检查和扩展安全实践来提供帮助。人工智能生成的代码修复和漏洞警报将补救措施整合到开发人员的工作流程中。此外，人工智能可以增强对开源框架的建模，使漏洞检测更加准确。自动化功能，包括分支保护规则和状态检查，进一步赋予开发人员主动解决安全问题的能力。

## 4. 让开发人员参与安全决策

为了确保工程团队和安全团队之间的顺畅合作，将开发人员纳入[安全流程和政策决策](https://thenewstack.io/tutorial-create-a-kubernetes-pod-security-policy/)的制定过程至关重要。在实施新工具或更改政策之前，从开发者的角度寻求反馈至关重要。询问有关当前安全实践的有效性、工具对工作流程的影响以及工具或实践的建议，可以提供改进的见解。这种协作方式培育了更加面向开发者的安全环境。

## 5. 设定关于安全编码的明确期望

DevSecOps 不应只是引入更多工具，而应该是确立清晰的期望和有效使用现有工具的过程。对[政策和安全编码实践的清晰沟通](https://thenewstack.io/accurics-secures-cloud-infrastructure-through-policy-as-code/)确保了在整个 SDLC 过程中对安全的一致性处理。组织应该创建安全编码标准，然后选择倡导者来清晰地在团队之间传达政策。这种方法消除了模糊性，增强了开发人员对安全的意识，并在整个组织中培养了 DevSecOps 文化。

随着开发人员在 DevSecOps 模式下承担更多的安全责任，改善他们的用户体验变得至关重要。投资于理解和解决开发人员的痛点的组织将收获工程和安全团队之间增强的合作关系，从而实现安全代码的快速交付。通过赋予开发人员作为第一道防线的权力，企业可以充分发挥 DevSecOps 的优势。
