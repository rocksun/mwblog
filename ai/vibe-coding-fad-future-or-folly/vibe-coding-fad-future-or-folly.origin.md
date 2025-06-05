# Vibe Coding: Fad, Future or Folly?
![Featued image for: Vibe Coding: Fad, Future or Folly?](https://cdn.thenewstack.io/media/2025/06/42897c77-vibes-1024x576.jpg)
The software development landscape is perpetually shifting, and early 2025 brought a new tremor: [vibe coding](https://thenewstack.io/vibe-coding-and-you/). Coined by OpenAI researcher [Andrej Karpathy in February](https://x.com/karpathy/status/1886192184808149383?lang=en), he used the term to describe an experiment where he built a small project without personally writing a single line of code — or even touching a keyboard.

Karpathy [dictated application requirements](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) for an “amusing throwaway weekend project” to superwhisper, an AI voice transcriber. These instructions were then fed into [Cursor Chat](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/), an AI-powered multifile code editor, which generated a complete web app. Adjustments were made with surprisingly “dumb” prompts like “decrease the padding on the sidebar by half,” with Karpathy accepting changes without reviewing diffs. When bugs arose that Cursor couldn’t fix, his solution was to “ask for random changes” until the issue seemingly resolved itself. “It’s not really coding,” he conceded. “I just see stuff, say stuff, run stuff and copy-paste stuff, and it mostly works.”

The “vibes” took a different turn for Leonel Acevedo, CEO of EnrichLead. [In March 2025](https://x.com/leojr94_/status/1900767509621674109), he announced that he built a SaaS application with “zero hand-written code,” telling others to “continue to whine about it [AI] or start building.” Unlike Karpathy’s experimental project, Acevedo positioned the app as production-ready, implying robustness and real-world viability.

The triumph was short-lived. Days later, Acevedo [reported that the app was under attack](https://x.com/leojr94_/status/1901560276488511759). And because he is nontechnical, debugging the AI-generated codebase proved a slow, painful process. The culprit? His “vibed” code had exposed critical API keys, leaving the application wide open.

Karpathy’s experiment and Acevedo’s ordeal cast a stark light on the promise and peril of this emerging approach. While it’s still early days for vibe coding, it’s undeniably the latest iteration in the ever-evolving way we approach [software development in the era of AI](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/).

**So What Exactly Is ‘Vibe Coding’?**
At its core, vibe coding is an AI-dependent programming technique. A developer (or even a non-developer) describes a problem or desired outcome in natural language prompts to a large language model (LLM) specifically tuned for code generation. The LLM then interprets these requirements and attempts to generate a complete, functional application.

Two prominent IDEs are leading the vibe coding charge, both using Claude 3.5 Sonnet under the hood but offering distinct user experiences:

Cursor |
Windsurf |
|
AI approach and workflow |
Feature-rich AI integration, more manual context control, “Agent mode” | Simpler, automated AI agent (“Cascade”), strong automatic context handling |
User experience and complexity |
More features, potentially steeper learning curve | Cleaner, more intuitive, often easier for beginners |
Code generation and context |
Requires more explicit context (e.g., @codebase, @files) | Excels at automatic codebase analysis and multifile awareness |
**The Allure and Downsides of Coding with ‘Vibes’ **
The [rapid interest in vibe coding](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/) isn’t without reason. It promises several compelling advantages:

**Lower barrier to entry**: Got a great idea but limited coding chops? Well-crafted prompts can theoretically bridge that gap, turning concepts into code.**Increased development velocity**: Prototyping and iteration cycles can accelerate dramatically when the IDE handles the bulk of code generation.**Focus on higher-level problems**: By offloading boilerplate, CRUD operations and other routine tasks, developers can dedicate more brainpower to complex architectural and innovative problem-solving.**Bridging knowledge gaps**: Even the most experienced developer faces the challenges of learning new technology. Vibe coding can help speed up onboarding by providing the fundamentals.
However, as Acevedo’s incident demonstrates, the vibes can quickly turn sour. Developers need to be acutely aware of the disadvantages:

**Inconsistency and unpredictability**: LLM outputs are nondeterministic. This can lead to a codebase with disjointed styles, structures and approaches, making it a nightmare to understand, maintain and debug predictably.**Increased risk of bugs, errors and vulnerabilities**: AI predicts likely code sequences. This can easily introduce subtle bugs or glaring security holes (like exposed API keys) that an experienced developer would intuitively avoid.**Challenges in long-term maintainability and scalability**: Code generated without explicit architectural guidance or consideration for future needs can quickly become unmaintainable and difficult to scale.**Potential for reduced****developer productivity**: Poorly documented or convoluted “vibe” code can significantly increase developer toil during refactoring, debugging or extension. Wrestling with prompts to achieve a specific outcome can sometimes take longer than writing the code directly.
**AI Coding: A New Chapter in the SDLC**
The software development life cycle (SDLC) has always been a story of evolution, from waterfall to agile, from manual deployments to DevOps. Each iteration has reshaped the developer’s role, introducing new tools and methodologies to tackle emerging challenges. AI’s integration into coding, whether “vibe” or otherwise, is the latest chapter, presenting both opportunities and demands for adaptation.

To harness AI’s power without succumbing to its pitfalls, developers must evolve their practices:

**Explore and experiment**: Get hands-on with AI coding tools. Whether it’s Cursor, Windsurf or the next big thing, direct experience is invaluable for understanding capabilities and limitations.**Vibe, but verify**: This cannot be overstated. Treat AI-generated code as a first draft from a very fast, somewhat naive junior developer. Always meticulously review, test and refactor, and use code quality and security scanning tools.**Embrace architectural thinking**: With AI handling more low-level implementation, developers can — and must — elevate their focus to robust system design, component interaction and solving complex business problems with innovative, well-architected solutions.**Master prompt engineering**: The quality of AI output is directly proportional to the quality of the input. Learn to write clear, concise and unambiguous prompts. Strategically consider requirements, design patterns, testing implications and deployment/maintenance needs to inform your prompting strategy.
**The Developer Role Is Evolving, Not Evaporating**
While methodologies change, the core responsibilities of developers remain. We strive for efficiency, optimization, reliability and maintainability. We aim to build useful software and avoid those dreaded middle-of-the-night incident calls.

AI can be an incredibly potent tool, automating tedious tasks and freeing developers for more creative and strategic work. However, its inherent limitations mean that human oversight, critical thinking and a commitment to [quality have become more crucial than ever](https://thenewstack.io/code-quality-becomes-even-more-vital-in-the-ai-era/).

As the long-term impact of AI on the SDLC continues to unfold, one thing is certain: Code quality, code security and the indispensable role of skilled developer oversight will always be central to building meaningful, robust and reliable software.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)