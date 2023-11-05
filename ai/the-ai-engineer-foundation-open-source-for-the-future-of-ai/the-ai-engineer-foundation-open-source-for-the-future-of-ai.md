<!-- 
# AI工程师基金会: 面向AI未来的开源
https://cdn.thenewstack.io/media/2023/11/fb310617-aifoundation_launch-1024x656.jpg
Sasha Sheng， founder of the AI Engineer Foundation， at the recent AI Engineer Summit; photo by Richard MacManus.
 -->

寻求加入Linux基金会的AI工程师基金会，通过启动一个与技术无关的AI代理协议（AI Agent Protocol）开始了它的工作。

> 译自 [The AI Engineer Foundation: Open Source for the Future of AI](https://thenewstack.io/the-ai-engineer-foundation-open-source-for-the-future-of-ai/) 。

[欧盟委员会](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2018:237:FIN)和[美国政府](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)都在着手制定AI法规。演员和作家的工会也在进行罢工，部分原因是为了保护他们的创作不被可能夺走工作岗位的AI所威胁。几乎所有人都认识到大规模[未受限制AI](https://thenewstack.io/qcon-keynote-why-generative-ai-is-harmful-to-earth-and-society/)的潜在风险。但政府和行业的节奏通常落后于技术进步 - 而人工智能的增长速度是前所未见的。

在监管机构和外部实体理清事情的时候，技术行业被留下来制定自己的标准。正如Spotify的Helen Gruel最近提醒我们的，[标准化的途径是通过开源](https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/)。

这就是[本月AI工程师峰](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)会宣布成立的[AI工程师基金会](https://www.aie.foundation/)的作用所在。该非营利组织致力于开源和标准化AI进步，使任何人 - 从单个开发者到大型组织 - 都可以以互操作、包容和社区驱动的方式参与理解和构建AI。 

“这里的目标是提升从事这项工作的所有行业人士，”AI工程师基金会创始人[Sasha Sheng](https://www.linkedin.com/in/sashasheng/)告诉The New Stack。但是这个组织是什么？它如何保持中立？到目前为止完成了哪些工作？请继续阅读以了解更多信息。

## AI代理协议

随着技术的成熟以及用例和采用的广泛应用，逻辑上的下一步将是AI标准化，以此欢迎人们在其基础上进行创新构建 - 就像HTTP在互联网早期实现的那样。Sheng说，这将“允许人们对[]如何通信达成标准......以便在这些共识的基础上进行构建。”

考虑到这一点，基金会的首个项目是与技术无关的[Agent协议](https://github.com/AI-Engineer-Foundation/agent-protocol)，这是一个OpenAPI规范，旨在为与AI助手交互创建一个通用接口。这些软件被称为智能代理，它们可以自主地推理下一步行动并执行任务。

Sheng解释说，Agent协议“是一个非常简单的规范，说明数据输入格式是什么，数据输出格式是什么，[以及]端点长什么样子。” 

早期的集成伙伴包括[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)和[LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/)，这是开发大型语言模型的流行平台，以便开发者可以开箱即用Agent协议。其他早期使用者包括正在开发类似虚拟助手工作流程的创业公司产品，如个人AI助手[GPT Engineer](https://github.com/AntonOsika/gpt-engineer)、[Smol Developer](https://github.com/smol-ai/developer)和[AutoGPT](https://auto-gpt.ai/)。

## 开源之路是包容性AI的道路

Agent协议并不是唯一的规范。它与[SuperAgent](https://www.superagent.sh/)、[AIWaves Agents](https://www.aiwaves-agents.com/)和微软的[AutoGen](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat/)等竞争，每一个都是一个具有自己专属通信协议的垂直集成框架。然而，这是一个高度碎片化的市场，而那些规范“由对其有财务利益关系的个别公司拥有”，Sheng解释道。 “因此，作为开发者，当他们开发工具时，可以选择使用任何自己想要的，但使用由营利公司拥有的规范的缺点是存在潜在的利益冲突。” 她提到，今年早些时候，以前开源的[Terraform更改了其许可证为闭源](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)。 “我们想避免这种由风险资本支持的锁定情况。” 

事实上，Agent协议最近被添加到了[AutoGen的路线图](https://github.com/microsoft/autogen/issues/49)中。

Sheng解释说，采用这种中立的开源策略也是为了给予开发者选择如何使用和构建自己的AI助手的自由 - 因为到目前为止，每个公司都有自己内部的助手通信方式。

“我希望通过推广Agent协议来实现这一点，这些各个框架也会逐渐采用Agent协议，所以我们可以拥有一个统一的接口，”她说。 但她也强调，“我没有资格说我们的Agent协议是最好的。我们要小心不要强制行业使用什么。”

相反，她继续说，AI工程师基金会旨在成为“标准和共识接口的家，以便我们可以进行更多协作”。他们致力于成为观察者，观察人们开始使用什么。

事实上，有兴趣使用它。 当我们与Sheng交谈时，AI工程师基金会刚刚结束其首次黑客马拉松(由AutoGPT团队运营)，其中有[600多名助手](https://github.com/Significant-Gravitas/AutoGPT/pulls?q=is%3Apr+entering+the+arena)参与竞争，创建可以通过自然语言输入处理任务的[最佳通用助手](https://autogpt.net/autogpt-arena-hacks-the-ultimate-guide-to-winning-the-ai-challenge/)。

黑客马拉松充当评估基准。“AutoGPT团队构建了一个基准评估工具，基本上可以调用各种不同实现的助手；但它能够调用的原因是[]所有助手都有一个统一的接口来接收请求，”Sheng解释道。“因此，基准不需要确切知道助手的内部实现方式，但是因为知道助手使用的语言，可以向它发起请求并获得响应，以评估它在任务上的表现。”

## AI工程师如何填补AI工程师岗位需求

AI工程师基金会也正在开发一系列课程，致力于培训传统软件工程师，以帮助填补[2700万AI工程师空缺](https://yylives.cc/2023/08/27/tech-works-how-to-fill-the-27-million-ai-engineer-gap/)。

这样的一个课程可能是帮助开发者培训成为代理工程师。Sheng解释说，这是AI工程师角色的一个子集，是非常人性化的代理角色的演变。从客户支持到旅行代理，许多角色的初级或次级接触形式已经或者很快就会被自动化代替，使用生成式AI回答常见问题。

“你可以把人类大致看作是一个代理，对吗?”她说。“我们认为下一步要做的就是让它能够像代理一样自主行动。”

它正在发展为人类加上代理共同执行任务，如呼叫中心实现混合运营。代理工程师将帮助构建自学习代理，然后提示工程师 - 其角色基于同理心和领域知识 - 将指出知识库中的空白。

这也可以应用于软件开发过程本身，如[Kubiya的平台工程](https://thenewstack.io/kubiya-launches-first-generative-ai-for-platform-engineering/)。

AI代理在[开发者生产力](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/)领域已经具有很大的潜力，特别是在[文档](https://thenewstack.io/documentation-is-more-than-your-thinnest-viable-platform/)方面。

“对于开发者来说，有很多资源可以用来执行相同的任务，”Sheng说。“调用LLM(大型语言模型)的简单行为，有多个不同的接口封装这个调用。因此对开发者来说，如果我们可以标准化接口，这实际上可以帮助他们提高效率。”

但AI还没有完全成熟。正如我们已经知道的，[生成式AI即使不知道答案也会回应](https://thenewstack.io/tech-works-when-should-engineers-use-generative-ai/)，所以用户需要谨慎。在这种过渡的混合世界中，Sheng说，当代理不知道答案时，人类代理将接管对话，而提示工程师将在代理表现不佳时进行调查和优化。

Sheng说，人类也需要观察代理内部的工作方式，这就是为什么对AI代理可观察性工具的需求很大，“当人类需要观察什么时候代理可以给出答案，然后相应地采取行动。”

代理工程师和提示工程师可能只是近期未来的过渡工作，但将帮助传统软件开发者拓宽业务范围并进入AI领域。随着AI的进步，主题专家 - 在软件开发之外可能根本不需要技术知识 - 将在未来训练这些模型。

## AI工程师基金会的下一步

AI工程师基金会正在[寻找开源软件项目](https://www.aie.foundation/#projects)申请加入该基金会，类似Linux基金会，将有三个阶段: 沙箱、孵化和毕业。Sheng说，他们特别渴望找到一个模式项目，希望捐赠以促进数据标注的标准化。该基金会还正在开发一个项目，旨在[标准化存储和共享模型定义](https://github.com/InterwebAlchemy/model-metadata-central)，包括上下文窗口和每个词元的成本。他们还在寻找向量数据库和inter-LLM互操作性方面的开源项目。代理可观察性是基金会渴望探索的另一个开源解决方案领域，因为如果不了解何时或为何，代理可能会陷入循环。

Sheng说，她的基金会已经启动了加入Linux基金会的流程，以获取对组织结构、法律和后台办公的声誉和支持，并获取访问其他开源社区的机会。

AI工程师基金会的所有项目将开源，并继续为AI研究做出贡献。基金会也在寻找赞助。

正如Sheng所说: “这样的项目可以帮助整个生态系统。”
