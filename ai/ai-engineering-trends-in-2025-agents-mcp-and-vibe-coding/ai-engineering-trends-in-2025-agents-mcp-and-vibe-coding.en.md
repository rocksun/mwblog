When I went to the [first AI Engineer Summit](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/) in October 2023, AI agents were a joke. At that point, agents hadn’t proven they could consistently do even basic tasks. But fast forward just two years, and agentic technology has made big strides — albeit it’s still relatively unproven as completely autonomous software. Regardless, agents were the biggest development story of 2025 and “agentic” was the word of the year ([again](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/)).

In terms of AI technologies in full blossom now, the Model Context Protocol (MCP) was everywhere in 2025 — running an MCP server has become almost as popular as running a web server. Other AI developments in 2025 included the rise of AI coding tools (and yes, “coding agents” are a trend now too), the massive influx of developers thanks to vibe coding, and AI infrastructure becoming developer-friendly.

Let’s take a closer look at five of the biggest AI development trends of 2025.

## 1. The Rise of Agentic Technology in Software Engineering

Although agents had been talked about last year, 2025 was when talk became action. It probably started when [OpenAI launched Operator](https://openai.com/index/introducing-operator/) as a research preview on January 23, 2025. It was pitched as an AI agent capable of using its own web browser to perform tasks like filling in forms, making purchases, and scheduling appointments. Operator was followed in July [by ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/), which boasted of an internal “virtual computer” for task execution.

Meanwhile, enterprise IT departments began to get a handle on agentic technology. In February, [I profiled a company called Orby](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/) that was promoting its Large Action Model (LAM). CTO [Will Lu](https://www.linkedin.com/in/will-dongxu-lu-9b9b972b/) explained that LAMs take *actions* as input — giving as examples application screenshots, webpage HTML content, user interactions (such as mouse clicks and keyboard inputs). He told me that Orby’s LAM can use that context to automate complex enterprise workflows.

However, enterprises are being cautious about rolling out agentic systems. [Brian Wald](https://www.linkedin.com/in/brianwald/), who heads up GitLab’s Field CTO team and is in regular contact with enterprise IT departments, told me in May that enterprises are [focused on structured implementations of agents](https://thenewstack.io/the-field-cto-view-ai-vibe-coding-and-developer-skillsets/), rather than open experimentation. Enterprises are not letting every developer freely use AI agents, he said. Instead, they’re forming centralized “AI enablement” teams, which often overlap with platform engineering or DevOps teams.

Wald added that enterprise IT teams typically have strict policies around data privacy, IP protection, and model hosting.

In terms of frameworks and tools to build agents, we saw a flurry of launches over 2025: OpenAI’s [AgentKit](https://openai.com/index/introducing-agentkit/) and [Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/), Anthropic’s [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), Google’s [Agent Development Kit](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/) (ADK) and [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder). We’re also seeing experiments happening with distribution — such as [MIT’s decentralized Project NANDA](https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/) and Microsoft’s [Magentic marketplace](https://thenewstack.io/microsoft-launches-magentic-marketplace-for-ai-agents/).

## 2. MCP Becomes the Standard for LLM and API Integration

Last November, Anthropic launched the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers), an open source protocol designed to streamline how AI models access data, tools and services. The goal was to make MCP the universal method for AI agents to trigger external actions — and that’s basically what happened over the course of 2025, as nearly every company adopted the protocol.

With such broad support, this month Anthropic moved MCP into a newly founded open source foundation under the Linux Foundation: [the Agentic AI Foundation (AAIF)](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/).

In March, [I interviewed Speakeasy CEO Sagar Batchu](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/), whose company provides a tool called [MCP Server Generation](https://www.speakeasy.com/post/release-model-context-protocol) to automate the creation of MCP-compatible servers. He pointed out that until MCP arrived, integrating an API with an AI model had been challenging. Many AI-based API integrations failed, he said, because models lacked the necessary schema information to make sense of API responses. MCP solves this by structuring API interactions in a way that AI can understand, making integrations more reliable.

That said, we have to also acknowledge the security risks of MCP. According to [Gil Feig](https://www.linkedin.com/in/gilfeig/), CTO of agentic tool provider [Merge](https://www.merge.dev/), “developers learned the hard way that rapid adoption can pose serious security and reliability challenges, and no trend exemplified this more than the popularity of MCP servers.” He added that “MCP’s flexible architecture created a Wild West of potentially untrusted code, where community-published servers could be backdoored or abandoned, and blanket access to sensitive services like email and CRMs became common.”

## 3. The Evolution of AI Coding Tools into Coding Agents

As agents and MCP became the hot technologies this year, developer tools quickly adapted. By the end of the year, coding tools had moved on from “mere” autocomplete functionality to full-on agentic coding. Although, as my colleague David Eastman pointed out in [his review of AI coding tools in 2025](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era), “we still want to limit what an agent can do (especially on your machine) and where they can do it.” So agentic coding software isn’t fully trusted at this point.

Nevertheless, tools like [Warp](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/), [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) and [Verdent](https://thenewstack.io/tiktoks-ex-algorithm-chief-launches-verdent-ai-coding-tool/) (created by TikTok’s ex-algorithm chief) all aimed to convert developers to agentic systems this year. But even the people running these companies acknowledge that they won’t be replacing developers any time soon.

“This was supposed to be the year AI replaced developers, but it wasn’t even close,” Warp CEO [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/) told The New Stack. “What actually happened is developers became orchestrators of AI agents — a role that demands the same technical judgment, critical thinking, and adaptability they’ve always had. Prompt engineering doesn’t cut it.”

[Bob Walker](https://www.linkedin.com/in/bobjwalker/), Field CTO at [Octopus Deploy](https://octopus.com?utm_content=inline+mention), added that AI coding tools are no excuse for lack of development expertise. “Developing a critical thinking skill set has become more important than ever,” he told us. “The same is true with understanding the fundamentals of how the language or framework of choice works.”

## 4. The Influx of New Developers Known as ‘Vibe Coders’

The fourth trend somewhat undercuts the points made by Lloyd and Walker. Vibe coders aren’t necessarily skilled programmers — in fact, the whole idea of vibe coding is to let the AI system do the coding for you.

Yet both [Vercel](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/) and [Netlify](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/) (two of the leading web developer platforms) have let it be known that their [user bases have massively increased](https://webtechnology.news/when-everyones-a-developer-how-do-we-promote-the-web-platform-over-react/) this year. And it’s all because of vibe coders. What’s happened over 2025 is that the definition of a “developer” has expanded to include people who rely on prompting rather than programming.

One key problem with vibe coding is that the code generated isn’t necessarily reliable. When [OpenAI launched GPT-5](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) in August, the company claimed it “excels at front-end coding.” But GPT-5 didn’t necessarily live up to the hype for developers. In an update to its [State of Code Report on LLM personalities](https://www.sonarsource.com/sem/the-coding-personalities-of-leading-llms/?utm_medium=paid&utm_source=newstack&utm_campaign=ss-state-of-llms25&utm_content=newsletter-TNS-newsletter-stateofllm-x-x&utm_term=ww-psp-x&s_category=Paid&s_source=Paid%20Other&s_origin=newstack&utm_content=inline-mention), the code security company [Sonar](https://www.sonarsource.com/sem/the-coding-personalities-of-leading-llms/?utm_medium=paid&utm_source=newstack&utm_campaign=ss-state-of-llms25&utm_content=newsletter-TNS-newsletter-stateofllm-x-x&utm_term=ww-psp-x&s_category=Paid&s_source=Paid%20Other&s_origin=newstack&utm_content=inline-mention) concluded that GPT-5 was not, according to its tests, the leader in coding performance. It noted that GPT-5 generates a “larger and more complex volume of code than any other model,” which makes it “a serious challenge to review and maintain.”

The other issue that GPT-5 highlighted was its tendency [to default to React code](https://thenewstack.io/is-gpt-5-a-coding-powerhouse-or-maintainability-nightmare/), simply because it’s the most popular frontend framework. But React code is notoriously [bloated and complex](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) — meaning vibe coders are even less likely to understand it.

## 5. The AI-ification of DevOps and Developer Infrastructure

DevOps tooling also adapted well to the AI era this year, with new [AI serverless products](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/), container technologies, and other “[AIOps](https://thenewstack.io/sre-report-retrospectives-have-aiops-predictions-held-up/)” solutions.

In January, I wrote about a company called Replicate, which sells a solution that [wraps AI models into containers](https://thenewstack.io/simplify-ai-development-with-machine-learning-containers/). One of the founders was previously the creator of Docker Compose, [Ben Firshman](https://www.linkedin.com/in/bfirsh/). A key benefit of Replicate is that it allows developers to customize, fine-tune and tinker with open source LLM models. As Firshman explained [on the Latent Space podcast](https://www.latent.space/p/replicate), “the whole point of open source is that you can tinker on it and you can customize it and you can fine-tune it and you can smush it together with another model.”

In November, Replicate was acquired by Cloudflare. So, consolidation of AI devops tooling has already started to happen.

We’ve also seen middleware enterprise solutions emerge for agents. In August, I interviewed [Oren Michels](https://www.linkedin.com/in/omichels/), CEO of a new AI company called Barndoor. Michels’ bet is that [managing AI agents is the new API management](https://thenewstack.io/managing-ai-agents-the-new-api-management/) — and he should know, as he was previously founder of Mashery, an API management company during the Web 2.0 era.

## Conclusion

A lot happened in the relatively new field of AI engineering in 2025, but there’s also a sense that the tools and development practices are a little fragile and immature. From MCP’s security risks to the not entirely believable claims that fully autonomous agents are just around the corner, AI development still has a lot to prove.

It’s also unclear at this point how viable “vibe coding” will be in the long term, with issues around code quality and code maintainability leaving plenty of room for skepticism.

All that said, AI clearly became the biggest disruptor in software engineering over 2025 — and the ructions will continue well into 2026.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)