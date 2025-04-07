# From BASIC to Vibes: Microsoft’s 50-Year Code Evolution
![Featued image for: From BASIC to Vibes: Microsoft’s 50-Year Code Evolution](https://cdn.thenewstack.io/media/2025/04/ffb2ddc3-frank-albrecht-lkgwaktioyq-unsplash-1-1024x683.jpg)
In honor of its 50th anniversary, Microsoft has released its very own [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) kit — GitHub Copilot agent mode and [Model Context Protocol (MCP) support](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/).

[Channeling Jay-Z](https://www.youtube.com/watch?v=9XEWVM1IhGY) in a blog post introducing the new solution, [Thomas Dohmke](https://www.linkedin.com/in/ashtom/), CEO of GitHub, wrote: “[Allow us to reintroduce ourselves](https://genius.com/Jay-z-public-service-announcement-lyrics): [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) is getting a whole lot more agentic with increased context of your tools and services, powered by the world’s leading models, starting today.”
And perhaps riding on that wave of hip-hop cool, Microsoft CEO [Satya Nadella](https://www.linkedin.com/in/satyanadella/) provided a video clip of himself vibe coding and using the technology at a Microsoft event commemorating the 50th anniversary of the company. You won’t find many CEOs bold enough to take the stage and vibe code. Nadella *is *cool. He can [rock a hoodie](https://seasonedgaming.com/2021/06/10/microsoft-ceo-satya-nadella-wears-halo-infinite-hoodie-in-latest-xbox-update/) with the best of them (and I hear he can cold rock a party, just kidding).

Microsoft rolled out [agent mode in Visual Studio Code](https://github.com/features/copilot?utm_source=Blog&utm_medium=GitHub&utm_campaign=proplus&utm_notesblogtop) to all users, now complete with MCP support. It also released a new open source and local [GitHub MCP server](https://github.com/github/github-mcp-server?utm_source=Blog&utm_medium=GitHub&utm_campaign=proplus&utm_notesblogtop), giving developers the ability to add GitHub functionality to any LLM tool that supports [MCP](https://modelcontextprotocol.io/introduction), an open source standard designed to streamline how AI models interact with APIs.

## AI That Takes Action
Meanwhile, regarding Nadella partying (all joking aside), Microsoft is quite serious about vibe coding. And what makes Agent Mode revolutionary is its ability to go beyond mere suggestions. While the original Copilot would offer code completions as you typed, agent mode takes a more proactive approach.

“Agent mode is fundamentally capable of taking action to translate your ideas into code,” Dohmke wrote in the GitHub announcement. This means the AI can suggest terminal commands, generate entire files, and even diagnose and fix runtime errors automatically.

Microsoft shared agent mode with [VS Code Insiders in February](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/), “enabling developers to perform a variety of tasks: from [autofixing code gen errors](https://x.com/d4m1n/status/1898759539303809436), to [building web apps](https://x.com/jorisroovers/status/1898647091469025301), to [yeeting commits](https://x.com/Will479242/status/1900306201906188341) — whatever that means,” Dohmke wrote.

One early user (@xthree) shared their experience on X: “I threw at it what I thought was going to be a monumental task, and it scanned 4-5 different files, figured out how it was working, and made modifications in all those files to work exactly how I wanted. First time.”

The technology is currently being rolled out to all VS Code users, with GitHub aiming for full availability in the coming weeks. Manual enablement is also available.

## The USB Port for Intelligence
GitHub describes MCP as “a USB port for intelligence.”

“MCP allows you to equip agent mode with the context and capabilities it needs to help you, like a USB port for intelligence,” the announcement said. This means developers can connect agent mode to various tools and services in their development stack, expanding its capabilities beyond what’s built into VS Code.

To accelerate adoption, GitHub’s open source local MCP server adds GitHub functionality to any LLM tool supporting the protocol. This allows the agent to search across repositories, manage issues, and even create pull requests — essentially turning it into a power user of the GitHub platform itself.

## Multimodel Power Under the Hood
GitHub isn’t limiting users to a single AI model. Agent mode will be powered by a choice of Claude 3.5 and 3.7 Sonnet, 3.7 Sonnet Thinking, Google Gemini 2.0 Flash, OpenAI o3-mini, and OpenAI GPT-4o.

Access to these premium models comes with a new pricing structure. GitHub is introducing premium requests, with Copilot Pro users receiving 300 monthly requests starting May 5, while Business and Enterprise customers will receive 300 and 1,000 monthly requests, respectively, beginning between May 12 and 19.

A new Pro+ tier, priced at $39 per month, will offer individuals 1,500 monthly premium requests and access to advanced models like GPT-4.5.

## From BASIC to a Billion Developers
The timing of this announcement — coinciding with Microsoft’s 50th anniversary — feels symbolic. As the company celebrates half a century of existence, this release represents both a reflection on its past and a bold statement about its future.

“From the creation of BASIC or MS-DOS, to the .NET Framework and VS Code, to the acquisition of GitHub — Microsoft has always been a developer company at heart. Half a century of dev love is no small feat,” Dohmke wrote.

Moreover, “Now, with GitHub Copilot — what started out as a developer platform company is a platform where anyone can be a developer. Together, GitHub and Microsoft fully intend on enabling a world with 1 billion developers.”

To illustrate this point, in a mic-drop moment, Nadella provided a staged demonstration showing him using Agent Mode to vibe code and recreate Microsoft’s first BASIC program “in a single shot” — a fitting tribute to the company’s origins and a showcase of how far developer tools have advanced.

“Satya’s video, where he creates an Altair BASIC emulator, was fun and nicely nostalgic for Microsoft’s 50th birthday, but seemed a little gimmicky to me, without much detail shown. So that played to my inner AI cynic,” Andrew Brust, CEO of Blue Badge Insights, told The New Stack.

“But the demo of GitHub Copilot in VS Code’s agent mode was a different story,” he added. “Yes, it dealt with a more mundane application maintenance task, but mundane stuff is realistic in the software world, and that was the case here. The prompt was reasonable, the task was well-bounded yet nontrivial, and the result was compelling.”

## Vibe Coding Is Fun
“Vibe coding is fun — but notice how much you need to know to write a useful prompt. Much less what to do when it doesn’t work,” [Richard Campbell](https://www.linkedin.com/in/richjcampbell/?originalSubdomain=ca), a Microsoft MVP and regional director, told The New Stack.

“And then there are all the other considerations, like deployment, security, infrastructure, etc… nothing is as simple as it seems,” he added. “When Andrej [Karpathy] coined the term, and he tried a few times — before calling it vibe coding, he called it coding in English, he was really talking about developers doing experiments.”

Indeed, anyone foolish enough to deploy code generated this way is likely someone who doesn’t understand the consequences of doing so.

This is “just a reminder that the job of a developer is not to write code — it is to understand problems sufficiently to be able to describe them to a computer to execute more efficiently,” Campbell said. “Efficiently might be faster, might be at a lower cost… depends on the circumstance. But also, in the context of what is safe and appropriate. It takes an expert to get that stuff right.”

## The Agent Awakening
GitHub refers to this release as “the agent awakening,” suggesting that it views this as just the beginning of a larger shift in how AI assists developers.

“The agent awakening doesn’t stop there,” Dohmke said. He also announced the general availability of the Copilot code review agent — which has been used by more than one million developers during its preview period — and the release of “next edit suggestions” that allow developers to “tab tab tab [their] way to coding glory.”

For many developers, the introduction of agent mode represents a significant evolution in their relationship with AI-assisted coding. What began as a controversial but useful autocomplete tool has transformed into something closer to a collaborative coding partner, capable of understanding context, making connections across files, and taking independent action to solve problems.

“To me, this is what AI-driven coding should be: a user supplies technically savvy requirements, the AI does the grunt work, presents its work product, and lets the user confirm its efficacy and approve its deployment,” Brust said. “This only works if the person generating the prompt knows what they’re talking about, but it alleviates a lot of effort. That syncs perfectly with the notion of AI not replacing people but making them far more productive.”

As vibe coding enters the mainstream, one thing is clear: the line between human and AI contribution to software development continues to blur. And with Microsoft and GitHub, among others, leading the charge, the next 50 years of programming will look very different from the last.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)