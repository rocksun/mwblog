
<!--
title: GenAI故障，精细编排保障持续运行
cover: https://cdn.thenewstack.io/media/2025/11/62a9e245-cars.jpeg
summary: GenAI生产化挑战重重，需左移思维、持续验证与跨职能协作。金融机构尤需关注幻觉、风险。领导者应及早定义负责任的使用规范。
-->

GenAI生产化挑战重重，需左移思维、持续验证与跨职能协作。金融机构尤需关注幻觉、风险。领导者应及早定义负责任的使用规范。

> 译自：[When GenAI Breaks, Rigorous Orchestration Keeps It Running](https://thenewstack.io/when-genai-breaks-rigorous-orchestration-keeps-it-running/)
> 
> 作者：Manish Gupta

任何在生产环境中成功运行的事物都应完全按预期运行：可靠、透明，并在高压下不会崩溃。对于生成式AI (GenAI) 来说，情况也应如此。你构建应用程序，测试它，并对其进行压力测试。但将其投入生产环境却很少简单。只有大约 [5% 的试点项目](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) 能够投入生产。开发和生产环境常常不匹配。

较早的 [AI 模型](https://thenewstack.io/what-is-real-artificial-intelligence/)（传统AI）更容易测试和部署。相比之下，今天的GenAI系统需要更多的协作、持续的验证以及强大的CI/CD流水线才能投入生产。随着复杂性增加，团队需要“左移”思维，以便更早地测试、持续监控并像管理代码一样管理模型。

对于金融机构而言，挑战更大。许多机构有很有前景的概念验证，但很少有机构掌握了生产所需的运营严谨性。GenAI带来了许多新风险，例如幻觉、不可预测的行为和责任不清。这就像自动驾驶汽车：即使事故更罕见，每个人仍然会问谁是驾驶员。将GenAI投入生产需要纪律、合适的人才、明确的角色和监督，以确保其 [在现实世界中发挥作用](https://thenewstack.io/beyond-the-code-the-real-work-of-scaling/)。

## **从构建到生产**

当组织 [将GenAI扩展到试点项目之外](https://thenewstack.io/3-reasons-tech-execs-are-slowing-down-genai-projects/) 时，首先崩溃的往往不是技术，而是处理它的准备程度。如果没有合适的人才、组织结构以及谁来领导转型的明确性，就很难进入生产阶段。

团队常常 [构建模型](https://thenewstack.io/how-block-got-12000-employees-using-ai-agents-in-two-months/) 后就认为它已准备好部署。然后，有人会因为风险担忧而提出警告，或者评估失败，组织就会退缩。这是一个足够大的变革，也是一个足够大的利益，不能半途而废。投资正在增加，但尚未深入或统一到足以解决GenAI生产化所需的全方位转型问题。

早期的 [GenAI项目在集成](https://thenewstack.io/why-kubernetes-security-is-critical-for-genai-integrity/) 和监督方面也面临困难。因为该技术触及数据、风险、运营和合规等每一个职能，所需的协调/协作比大多数团队所准备的要多。

GenAI改变了工作方式。通过 [自动化以前的手动流程](https://thenewstack.io/stage-a-productivity-revolution-with-process-automation-ai-and-data-fabric/)，角色和职责发生转变。成功的部署取决于团队的跨职能协调以及重建工作流程的意愿。例如，苹果、摩根大通、三星等众多公司禁止员工使用公共聊天机器人，原因是担心数据泄露，这表明风险出现的速度有多快。

在组织层面，许多团队忽视了可复现性以及系统之间的相互依赖性。传统的机器学习 (ML) 流水线更线性且易于控制。相比之下，GenAI系统涉及多个代理、数据流水线和并发反馈循环。这使得编排和可追溯性不仅有用，而且对于生产环境的可靠性至关重要。

## **如何确保GenAI平稳运行**

编排需要一个共享环境，团队可以在其中独立工作，同时在整个生命周期中保持可见性。数据科学家、工程师、监管人员和合规官员都需要自己的独立空间来贡献，但整个系统必须保持可审计和互联。目标不是自动化一切，而是为团队提供提高效率同时保持监督的工具。这种环境对于大规模编排GenAI至关重要。

当然，仅凭技术无法解决组织挑战。真正的变革必须从整个公司层面发生。工具无法弥补人才缺口，但它们可以赋能 [团队更快地学习](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/) 并更有效地协作。在大型公司中，当每个人都可以访问并借鉴他人已学到的知识时，知识管理就成为一种最佳实践。

鉴于GenAI的新颖性，[人工干预](https://thenewstack.io/human-on-the-loop-the-new-ai-control-model-that-actually-works/) 是一种最佳实践。人工监督应贯穿每个阶段。在构建与客户交互的解决方案时，专家需要在构建过程中对其进行压力测试并提供实时反馈。这被称为“红队演练”。

在部署GenAI时，了解 [大型语言模型 (LLM) 的反应方式](https://thenewstack.io/what-is-a-large-language-model/) 将非常重要。这能暴露出弱点并验证防护措施。一旦部署，系统应持续监控，并进行频繁检查。每次检查都应在系统中记录，以建立信任和问责制。

## **长期博弈**

[GenAI的魅力在于](https://thenewstack.io/harness-genais-power-without-sinking-in-technical-debt/)，强大而全面的模型对所有人开放。过去，要做一些新的事情，你必须从头开始构建模型。这就是为什么现在是一个如此具有变革性的时刻。

在生产中维持GenAI意味着使其与业务目标和道德标准保持一致。领导者需要及早定义负责任的GenAI使用方式：如何衡量风险、可接受的错误水平以及何时需要人工审查。这些讨论不能在部署之后进行。它们现在就需要发生，与监管机构、行业同行乃至客户协作，以确保收益大于风险。适当的反馈循环有助于持续改进GenAI。

## **领导力与前进之路**

未来几年将是变革性的。[LLM正以](https://thenewstack.io/openai-aims-to-make-chatgpt-the-operating-system-of-the-future/) 即使是最有经验的团队也感到惊讶的速度发展，两三年可能感觉像永恒。不再有“快速追随者”这种说法。GenAI采用的领导者将是那些将技术执行与组织远见相结合的人。

领导者必须预先解决治理和组织挑战。及早将合规和风险官员纳入流程，不是作为审查员，而是作为合作伙伴。工程和合规领导者共同学习至关重要。信任GenAI工作流程就是这样建立起来的。

这趟列车正在快速行驶。如果你现在不开始学习、迭代并让你的团队参与进来，你就会被甩在后面。