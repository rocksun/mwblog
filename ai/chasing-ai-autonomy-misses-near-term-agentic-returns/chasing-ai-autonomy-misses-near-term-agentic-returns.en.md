Apple recently published a paper asking large reasoning models (LRMs) to solve some simple but lengthy algorithmic challenges, such as the Towers of Hanoi disc sorting puzzle. The models failed explosively. The models were able to solve the Towers of Hanoi challenge (in which discs are shifted across pegs according to simple rules) with three discs but failed at eight or more. The paper showed that the [models guess at the output of rules](https://www.anthropic.com/research/tracing-thoughts-language-model), even when the algorithm is provided.

Apple’s findings aren’t unique. In a paper titled “[Mind The Gap: Deep Learning Doesn’t Learn Deeply](https://arxiv.org/abs/2505.18623),” [Subbarao Kambhampati](https://www.linkedin.com/in/subbarao-kambhampati-3260708/) writes that inspection of models’ inner workings shows that models that are successful at algorithm challenges aren’t faithful to the algorithms internally. In other words, models that get to the right answer may be using “alternate strategies,” akin to my teenager cramming imperial dynasties the night before exams: *The correct answer is the name you recognize.* Kambhampati argues that [LRMs aren’t fundamentally different](https://arxiv.org/html/2504.09762v1) from the [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) they’re adapted from.

As statisticians say: All models are wrong, but some are useful.

## Less Inference, More Algorithm

As [Gary Marcus](https://x.com/GaryMarcus) has written, [LLMs](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) “are no substitute for good, well-specified conventional algorithms.” I was prompting [Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) to [output the algorithm](https://claude.ai/public/artifacts/b49e1119-c0f9-479b-9678-32b73af32658) for me. I asked it to write a validator for the algorithm. Then I asked it to give me a [demo application](https://claude.ai/public/artifacts/01d5ee53-84b7-41b0-acae-c16585844ce8) showing the solution.

The model solved the Towers of Hanoi on the first try.

![](https://cdn.thenewstack.io/media/2025/06/f4176d34-image1.gif)

The algorithm written by the LLM works better than calling the AI for the same result: It scales well, is more efficient than a machine learning (ML) model and should run as accurately as anything else in your browser. The model that wrote the code was aided by the many published reference solutions to this learn-to-code staple, which is also true of critical business questions like “Am I making money?” and “When does my pizza arrive?”

## Experimentation and Intuition

To get value from foundation models, we need to point them at appropriately scoped problems. In practice, the work of scoping AI problems is a combination of experimentation and developer intuition, and in an enterprise context, using developer platforms that make small batch experimentation safe to try. (Disclosure: I work on that at the [VMware Tanzu Platform](https://www.vmware.com/products/app-platform/tanzu).) You can label this combination of full stack dev and model awareness as “AI engineering.”

My teammate and AI engineer [Brian Friedman](https://www.linkedin.com/in/bryanmfriedman?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAADmNKcBbSK382e8_UxUekKinr4fh1hKSO4&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BJ14Bs90tTseEVQMNKJNt0Q%3D%3D) says: “Effort is required … you have to provide the specifics of your org in a narrow manner in order to solicit specific and accurate responses. We need to view things like retrieval-augmented generation not as stopgaps or anti-patterns, but as the way forward for safe and effective use of AI.”

## Agents: Less Bad Than What We’ve Been Doing

This gets us to agents, the reason that reasoning models exist. It would be really lovely if reasoning models could think through long workflows as zero-shot solutions: *Find me a flight, I don’t care how.* The more likely situation is that we’ll keep writing software.

We’ll identify small intermediate goals and store the results. We’ll call services and tools and validators. We’ll implement algorithms in Java and Python and Go. We’ll get feedback from humans along the way. We’ll worry about latency and security and carbon emissions.

It’s likely that coding assistants like Claude, Devstral and [Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) can do some of that work for us. But the slow work of figuring out what users want and testing product market fit still has to happen.

![](https://cdn.thenewstack.io/media/2025/06/da41945e-image3.jpg)

Foundation models solve hard problems. I’m skeptical by nature, so I’ve spent the last five years testing LLMs with real-world problems, building code analysis, search, summary, checkout and customer support gadgets. Within the scope of “transport a relevant bit of JSON from a database to a UI,” the reasoning models are proving stable, accurate and fast. Integrations are cheap now. Classification works. You can throw business rules into an application with natural language — “Do this thing, unless it’s one of the following situations” — and it works pretty well on Day 1.

As a developer, the delightful surprises are starting to outnumber the terrifying ones.

The recent influencer walkback from “agents” to “agentic applications” is an encouraging hype-cycle correction. As I’ve written previously, [existing software workflows](https://thenewstack.io/ai-agents-why-workflows-are-the-llm-use-case-to-watch/) are the near-term target for not-quite-agent adoption. We’ve solved natural language understanding in an incredibly general way. This is just now getting productized in high-value workflows (I’ll leave consumer chatbots like ChatGPT a topic for another day). Enterprises start with domains that are easy to measure as dollars (sales team prioritization, customer support, [site reliability engineering](https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/exploring-cloudhealth-new-experience-nx-intelligent-assist.html) [SRE]), but the next decade will see it creeping into places like pizza restaurants and retail stockrooms as small but useful process improvements. The users don’t need to know there’s a foundation model in there. They just want better software.

## Robots Do Laundry, but Only for Software Developers

The first wave of somewhat autonomous agents is running today on developer laptops. In a post modestly titled “[My AI Skeptic Friends Are All Nuts](https://fly.io/blog/youre-all-nuts/),” software engineer [Thomas Ptacek](https://x.com/tqbf) writes:

“​​People coding with LLMs today use agents. Agents get to poke around your codebase on their own. They author files directly. They run tools. They compile code, run tests, and iterate on the results. They also:

* pull in arbitrary code from the tree, or from other trees online, into their context windows,
* run standard Unix tools to navigate the tree and extract information,
* interact with Git,
* run existing tooling, like linters, formatters, and model checkers, and
* make essentially arbitrary tool calls (that you set up) through MCP.”

My experience and various [research](https://www.microsoft.com/en-us/research/publication/towards-effective-ai-support-for-developers-a-survey-of-desires-and-concerns/) [support](https://getdx.com/research/devex-what-actually-drives-productivity/) this. Ticketing, testing, code repos and deployment pipelines are represented as tools, often with the [Model Context Protocol](https://spring.io/blog/2024/12/11/spring-ai-mcp-announcement) (MCP) connecting them. Bots connected to a code editor are allowing developers to ask questions, like “Hey Tanzu Platform, what data infrastructure is approved for this use case?” and get answers that are contextually shaped by what they’re working on.

It’s a hint at what an “agentic” organization looks like for all knowledge workers: not a high autonomy robot but a steerable power armor wrapped around empowered humans, who can get started faster, work more safely and spend more time on the hard (or even fun) problems.

![](https://cdn.thenewstack.io/media/2025/06/6605e9c7-image2-1024x606.png)

Meanwhile, builders keep building. My former Sprout Social colleague [Kevin Stanton](https://www.linkedin.com/in/stantonk?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAABGMzoBFokCpvsb23c9PsRdBNjGFi1EXC8&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3B6zFW9BHaRKiGbmXJfqdJgw%3D%3D) [posts](https://www.linkedin.com/posts/activity-7336172175130882048-41OL?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACMg-oB-ggwAYzEbksUHvF-GZvbiThb9ZU), “Can’t wait for this hype cycle to end. The only way through is building real stuff and ignoring the chatter.”

Run small tests. Measure results. Use realistic data in realistic constraints, assembling your model’s context inputs by hand if you have to, or better yet, using a platform to wire up data, compute, inference and eval components quickly and safely. All this power is not aimed at impressing your bosses with vaporware prototypes, or throwing an AI press release at a slumping stock price, but to make better products. Try things. Show it to customers. Listen.

OK, but what about the big transformative changes? This is that. You’ll see it in hindsight.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/02/225ef326-jonathan-eyler-werve.jpg)

Jonathan Eyler-Werve has been launching products online for 15 years and has worked in product management, design and full-stack engineering roles. He mentors mid-career PMs, and advises startups and social ventures. He currently looks after app development teams at Broadcom,...

Read more from Jonathan Eyler-Werve](https://thenewstack.io/author/jonathan-eyler-werve/)