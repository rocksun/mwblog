<!--
title: 2025 AI工程新趋势：智能体、MCP与Vibe编程
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1.png
summary: 2025年AI工程五大趋势：代理技术大爆发，“代理式”成年度词汇；模型上下文协议MCP普及；AI编码工具向编码代理演进；“氛围编程者”涌入；DevOps和基础设施AI化。AI开发虽有进步，仍存挑战。
-->

2025年AI工程五大趋势：代理技术大爆发，“代理式”成年度词汇；模型上下文协议MCP普及；AI编码工具向编码代理演进；“氛围编程者”涌入；DevOps和基础设施AI化。AI开发虽有进步，仍存挑战。

> 译自：[AI Engineering Trends in 2025: Agents, MCP and Vibe Coding](https://thenewstack.io/ai-engineering-trends-in-2025-agents-mcp-and-vibe-coding/)
> 
> 作者：Richard MacManus

2023年10月，当我参加[首届AI工程师峰会](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)时，AI代理还是个笑话。那时，代理甚至无法持续完成基本任务。但仅仅两年后，代理式技术取得了巨大进步——尽管作为完全自主的软件，它仍然相对未经证实。无论如何，代理是2025年最大的发展新闻，“代理式”是年度词汇（[再次](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/)）。

就目前蓬勃发展的AI技术而言，模型上下文协议（MCP）在2025年无处不在——运行MCP服务器已变得几乎和运行Web服务器一样流行。2025年其他的AI发展包括AI编码工具的兴起（是的，“编码代理”现在也是一个趋势），得益于氛围编程带来的大量开发者涌入，以及AI基础设施变得对开发者友好。

让我们仔细看看2025年五大AI发展趋势。

## 1. 软件工程中代理式技术的兴起

尽管去年代理技术已被提及，但2025年是它从讨论走向行动的一年。这可能始于[OpenAI于2025年1月23日推出Operator](https://openai.com/index/introducing-operator/)作为研究预览版。它被宣传为一种AI代理，能够使用自己的网络浏览器执行填写表格、购物和安排约会等任务。7月，Operator之后是[ChatGPT代理](https://openai.com/index/introducing-chatgpt-agent/)，后者声称拥有一个用于任务执行的内部“虚拟计算机”。

与此同时，企业IT部门开始掌握代理式技术。2月，[我介绍了一家名为Orby的公司](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/)，该公司正在推广其大型动作模型（LAM）。首席技术官Will Lu解释说，LAM将“动作”作为输入——例如应用程序截图、网页HTML内容、用户交互（如鼠标点击和键盘输入）。他告诉我，Orby的LAM可以利用这种上下文来自动化复杂的企业工作流程。

然而，企业在部署代理式系统方面持谨慎态度。GitLab现场首席技术官团队负责人Brian Wald与企业IT部门保持定期联系，他于5月告诉我，企业[专注于代理的结构化实施](https://thenewstack.io/the-field-cto-view-ai-vibe-coding-and-developer-skillsets/)，而不是开放式实验。他说，企业不会让每个开发者随意使用AI代理。相反，他们正在组建集中的“AI赋能”团队，这些团队通常与平台工程或DevOps团队重叠。

Wald补充说，企业IT团队通常对数据隐私、知识产权保护和模型托管有严格的政策。

在构建代理的框架和工具方面，2025年我们看到了一系列发布：OpenAI的[AgentKit](https://openai.com/index/introducing-agentkit/)和[Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/)、Anthropic的[Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview/)、Google的[Agent Development Kit](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/)（ADK）和[Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder/)。我们还看到了分发方面的实验——例如[MIT的去中心化Project NANDA](https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/)和微软的[Magentic市场](https://thenewstack.io/microsoft-launches-magentic-marketplace-for-ai-agents/)。

## 2. MCP成为LLM和API集成的标准

去年11月，Anthropic推出了[模型上下文协议（MCP）](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers)，这是一个开源协议，旨在简化AI模型访问数据、工具和服务的方式。目标是使MCP成为AI代理触发外部动作的通用方法——这基本上是2025年发生的事情，几乎每家公司都采用了该协议。

由于获得了如此广泛的支持，Anthropic本月将MCP移交给了Linux基金会旗下新成立的开源基金会：[代理式AI基金会（AAIF）](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/)。

3月，[我采访了Speakeasy首席执行官Sagar Batchu](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)，他的公司提供一个名为[MCP Server Generation](https://www.speakeasy.com/post/release-model-context-protocol)的工具，用于自动化创建MCP兼容服务器。他指出，在MCP出现之前，将API与AI模型集成一直是一个挑战。他说，许多基于AI的API集成失败，因为模型缺乏必要的schema信息来理解API响应。MCP通过以AI可以理解的方式构建API交互来解决这个问题，使集成更加可靠。

话虽如此，我们也必须认识到MCP的安全风险。据代理工具提供商[Merge](https://www.merge.dev/)的首席技术官Gil Feig称，“开发者们通过血的教训认识到，快速采用会带来严重的安全和可靠性挑战，而没有任何趋势比MCP服务器的普及更能体现这一点。”他补充说，“MCP灵活的架构创造了一个潜在不可信代码的狂野西部，社区发布的服务器可能存在后门或被遗弃，并且对电子邮件和CRM等敏感服务的全面访问变得普遍。”

## 3. AI编码工具向编码代理的演进

随着代理和MCP成为今年的热门技术，开发者工具迅速适应。到年底，编码工具已从“单纯的”自动完成功能发展到全面的代理式编码。尽管，正如我的同事David Eastman在[他2025年AI编码工具的评论](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/)中指出的，“我们仍然希望限制代理能做什么（尤其是在您的机器上）以及它们在哪里可以做。”因此，代理式编码软件目前并未完全获得信任。

尽管如此，[Warp](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/)、[Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/)和[Verdent](https://thenewstack.io/tiktoks-ex-algorithm-chief-launches-verdent-ai-coding-tool/)（由TikTok前算法主管创建）等工具今年都旨在将开发者转向代理式系统。但即使是这些公司的运营者也承认，它们在短期内不会取代开发者。

Warp首席执行官Zach Lloyd告诉The New Stack：“本该是AI取代开发者的一年，但它甚至都还没有接近。”“实际发生的是，开发者成为了AI代理的协调者——这个角色需要他们一贯具备的技术判断力、批判性思维和适应能力。提示工程还远远不够。”

[Octopus Deploy](https://octopus.com?utm_content=inline+mention)的现场首席技术官Bob Walker补充说，AI编码工具不能成为缺乏开发专业知识的借口。“培养批判性思维能力比以往任何时候都更加重要，”他告诉我们。“理解所选语言或框架基本工作原理也同样如此。”

## 4. 被称为“氛围编程者”的新开发者的涌入

第四个趋势在某种程度上削弱了Lloyd和Walker的观点。氛围编程者不一定是熟练的程序员——事实上，氛围编程的整个理念就是让AI系统为您完成编码。

然而，[Vercel](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/)和[Netlify](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/)（两个领先的Web开发者平台）都表示，他们[的用户群今年大幅增长](https://webtechnology.news/when-everyones-a-developer-how-do-we-promote-the-web-platform-over-react/)。这都归因于氛围编程者。2025年发生的变化是，“开发者”的定义已经扩展到包括那些依赖提示而不是编程的人。

氛围编程的一个主要问题是生成的代码不一定可靠。当[OpenAI在8月推出GPT-5](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/)时，该公司声称它“擅长前端编码”。但GPT-5并未完全达到开发者对它的期望。在其[关于LLM个性化代码报告的更新](https://www.sonarsource.com/sem/the-coding-personalities-of-leading-llms/?utm_medium=paid&utm_source=newstack&utm_campaign=ss-state-of-llms25&utm_content=newsletter-TNS-newsletter-stateofllm-x-x&utm_term=ww-psp-x&s_category=Paid&s_source=Paid%20Other&s_origin=newstack&utm_content=inline-mention)中，代码安全公司[Sonar](https://www.sonarsource.com/sem/the-coding-personalities-of-leading-llms/?utm_medium=paid&utm_source=newstack&utm_campaign=ss-state-of-llms25&utm_content=newsletter-TNS-newsletter-stateofllm-x-x&utm_term=ww-psp-x&s_category=Paid&s_source=Paid%20Other&s_origin=newstack&utm_content=inline-mention)得出结论，根据其测试，GPT-5并非编码性能的领导者。它指出，GPT-5生成的“代码量比任何其他模型都更大、更复杂”，这使其“在审查和维护方面面临严重挑战”。

GPT-5凸显的另一个问题是它[倾向于默认生成React代码](https://thenewstack.io/is-gpt-5-a-coding-powerhouse-or-maintainability-nightmare/)，仅仅因为它最受欢迎的前端框架。但React代码出了名的[臃肿和复杂](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)——这意味着氛围编程者更不可能理解它。

## 5. DevOps和开发者基础设施的AI化

DevOps工具今年也很好地适应了AI时代，推出了新的[AI无服务器产品](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/)、容器技术以及其他“AIOps”解决方案。

1月，我撰写了一篇关于Replicate公司的文章，该公司销售一种将AI模型[封装到容器中](https://thenewstack.io/simplify-ai-development-with-machine-learning-containers/)的解决方案。其中一位创始人Ben Firshman曾是Docker Compose的创建者。Replicate的一个主要优势是它允许开发者自定义、微调和修补开源LLM模型。正如Firshman在[Latent Space播客](https://www.latent.space/p/replicate)上解释的那样，“开源的全部意义在于你可以修补它、定制它、微调它，并将其与其他模型结合。”

11月，Replicate被Cloudflare收购。因此，AI DevOps工具的整合已经开始发生。

我们还看到代理中间件企业解决方案的出现。8月，我采访了新AI公司Barndoor的首席执行官Oren Michels。Michels的赌注是[管理AI代理是新的API管理](https://thenewstack.io/managing-ai-agents-the-new-api-management/)——他应该很清楚这一点，因为他曾是Web 2.0时代API管理公司Mashery的创始人。

## 结论

2025年，AI工程这个相对较新的领域发生了许多事情，但也有人觉得这些工具和开发实践有些脆弱和不成熟。从MCP的安全风险到关于全自主代理即将问世的不完全可信的说法，AI开发仍有很多需要证明的地方。

目前还不清楚“氛围编程”的长期可行性如何，代码质量和可维护性问题留下了很大的质疑空间。

话虽如此，AI显然成为2025年软件工程领域最大的颠覆者——这种动荡将持续到2026年。