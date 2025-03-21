# Eclipse Theia: The ‘DeepSeek’ of AI Tooling?
![Featued image for: Eclipse Theia: The ‘DeepSeek’ of AI Tooling?](https://cdn.thenewstack.io/media/2025/03/2ba92d47-planet-volumes-w1hqljythcm-unsplash-1024x644.jpg)
Can the [Eclipse Foundation](https://thenewstack.io/alternative-to-visual-studio-marketplace-gains-momentum/)’s recently released [Theia AI](https://theia-ide.org/docs/theia_ai/) platform become the “[DeepSeek](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)” of [AI tooling](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/)?

Well, it’s possible that the vision of Foundation Executive Director [Mike Milinkovich](https://www.linkedin.com/in/mikemilinkovich/?originalSubdomain=ca) will come to be.

Eclipse last week launched a production release of its platform for building AI-enabled tools — Theia AI, plus an alpha release of an AI-powered IDE ([Theia IDE](https://theia-ide.org/)) that demonstrates the platform’s capabilities.

## DeepSeek Moment
In an interview, Milinkovich and [Jonas Helming](https://www.linkedin.com/in/jonas-helming-76303b28/), CEO of [EclipseSource](https://eclipsesource.com/) — who is heading up the Theia AI project, positioned Theia as potentially the “DeepSeek moment for AI tooling,” referring to how DeepSeek challenged conventional wisdom that frontier AI models required massive capital investment. Similarly, Theia aims to show that high-quality AI developer tools can be built using open source rather than proprietary solutions, Milinkovich said.

“We’re not saying that Thea is the DeepSeek of AI tooling, but it could be in the sense that it will need investment and participation from the community and from companies that want to build products on top of it in order to make it, to get it to and keep it at feature parity,” he said.

EclipseSource, an IT services company and founding member of the Eclipse Foundation, contributed the Theia technology to the foundation.

Milinkovich and Helming identify this moment as a critical juncture where the industry must decide whether AI tooling will be predominantly open source or proprietary. They position Theia against well-funded competitors like the wildly popular AI-powered code editor, [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/), created by [Anysphere](https://anysphere.inc/) — that is seeing a [valuation approaching $10 billion](https://www.bloomberg.com/news/articles/2025-03-07/ai-startup-anysphere-in-talks-for-close-to-10-billion-valuation) – and [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/).

Helming called Anysphere (with Cursor) “the darling in that space” and said most tooling startup projects “are basically starting off by forking VS code and working that way when they could actually use the Theia framework and lower the cost of building those kinds of tools because it’s way better and faster and smarter, rather than starting with your own fork of VS code,” he said.

Secondly, he added, “Rather than buying into a world where there’s a single vendor for AI tools down the road, you could have an alternative solution that would have some amount of investment going into a collaborative project like Theia to match feature-for-feature with what’s happening with these well-funded startups, but at a vastly reduced cost and basically a different style of business model around a collaborative project, rather than doing this as a single vendor solution.”

## Looks Like a Fork
[David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of Arcjet, told The New Stack that the Theia IDE looks like a VS Code fork, but it’s actually not.
“It has an independent codebase, with some crossover in components like the [Monaco editor](https://microsoft.github.io/monaco-editor/) and VS Code extension compatibility,” Mytton said. “They’ve taken a similar approach with Theia AI, which is their framework for building AI features where the model and UX can be swapped out.”

Indeed, Thea AI offers flexibility, transparency, and freedom of choice for developers, unlike proprietary solutions. It also allows developers to use any LLM, including local models, providing significant advantages for transparency and flexibility. Tool builders can integrate LLMs of their choice (cloud-based, self-hosted, or local) into custom tools and IDEs.

Eclipse built AI into the Theia IDE using the Theia AI framework, such that “it’s really a collection of specialist agents — code completion, architecture assistant, terminal command assistant — and the ability to create your own. This makes sense for developers because they want to see the behind-the-scenes details and customize things,” Mytton said. “See how much time people spend customizing Vim, for example. The models powering AI tools are a commodity, so the differentiation has to come from what’s built on top of them. I think this is similar to how most IT infrastructure is open source, so the commercial value comes from the applications built on top of it.”

## A Notable Innovation
Meanwhile, “Ever since ChatGPT first came out, the storyline around AI and LLMs was very much around, ‘you needed a huge capital investment in order to be able to produce a frontier model…’ and DeepSeek — which by the way, claims itself is to be an open source LLM and its code is available under the MIT license — really very dramatically changed that conventional wisdom by demonstrating that it was possible to build a very high functioning LLM at a much lower cost,” Milinkovich said.

[Arnal Dayaratna](https://www.idc.com/getdoc.jsp?containerId=PRF004946), an analyst at IDC, gets it.
He believes Eclipse Theia AI marks a notable innovation in developer tooling because it recognizes the transformative role of large language models in modern software development.

“By offering flexible LLM integration and customizable AI-driven workflows, Theia empowers developers to harness AI capabilities seamlessly within their IDE,” Dayaratna told The New Stack. “This capability is crucial as the development stack evolves given that AI, and generative AI in particular, are central to contemporary coding and testing workstreams. Theia’s open framework allows developers to choose and configure their preferred LLMs, ensuring that AI assistance aligns with the needs of specific projects as well the associated regulatory and compliance requirements of the organizations for which they work.”

In addition, the Theia IDE includes features to:

**Integrate with External Tools and Contextual Data**: Through[Model Contextual Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)integration, developers can connect AI-driven workflows with external tools, services, and contextual data, enhancing automation and interoperability within the development environment.**Ensure Open Source License Compliance**: The[SCANOSS](https://www.scanoss.com/)integration analyses AI-generated code for open source licensing compliance, helping developers mitigate legal and operational risks when incorporating AI-generated code.
“It’s nice to see the Eclipse Foundation team focus on MCP, which basically serves as a plug-in protocol for supportive data sources. Eclipse isn’t the first to bring MCP into their tooling, mind you,” said [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at The Futurum Group.

Across the entire software industry, AI-assisted development has quickly become the norm with AI augmentation and automation ranging from basic type-ahead tools to entirely hands-off [“vibe” coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) tools like Cursor, Shimmin noted.

“Basically, every IDE on the market has jumped headlong into this opportunity, led by mainstay IDE developers Microsoft and JetBrains along with newcomers Zed and open source mainstays Vim — well, Neovim — EMACS, and Eclipse,” he told The New Stack.

## Building Agentic AI Solutions
Moreover, the Eclipse Foundation’s newly released IDE does a great job of bringing AI to the foreground, Shimmin stated.

“But what’s interesting about this release isn’t just that the tool is using AI — GenAI in particular — to generate any old code. Instead, the Eclipse Foundation open source community has decided to tackle the difficult task of building agentic AI solutions,” he said. “This means helping developers wrangle models, tools, context, and supportive data assets. The latter of which is most important. GenAI models and agentic AI processes are nothing without data. But timely access to high-quality data continues to serve as the biggest challenge for enterprises looking to build GenAI outcomes — agentic or otherwise.”

## Eclipse History Repeats Itself
For his part, Helming noted that the Theia AI and the Theia IDE move is “in some ways, a replay of history, in the sense that if you think back 24 years ago, the original Eclipse IDE was a platform for building tools that was very successful,” he said. “Then they built the team built an IDE on top of it to demonstrate that that platform could be used to build that professional-quality IDE.”

Indeed, it’s good to see the Eclipse Foundation not leaving developers stranded, according to Holger Mueller, an analyst at Constellation Research.

“AI changes how code is being written, managed and reviewed. To keep and increase developer velocity — developers want and need to use the AI tools of their choice, notably models,” he said. “Being able to choose these to their liking is a key capability of an IDE, and it is good the Eclipse Foundation provides that ability with Theia.”

## Stiff Competition
However, Arcjet’s Mytton said the problem is there are a lot of editors now.

“It’s gone from VS Code being the only one of interest to a sudden explosion of competition. It’s a difficult space to be playing in,” he said.

Still, to be sure, “It’s too early to tell whether it [Theia] has the ability to displace well-known code editors and IDEs, but it does directionally represent the future of developer tooling because of its recognition of the centrality of foundation models to contemporary development,” Dayaratna summarized.

Yet, Theia has a permissive license that allows companies to build proprietary solutions on top of it if they choose.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)