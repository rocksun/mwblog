[Neel Sundaresan](https://www.linkedin.com/in/neel-sundaresan-a964a2/) doesn’t answer three questions. One of them, he says with some amusement, is why IBM Bob is named Bob.

That particular deflection is telling. Sundaresan — GM of Automation and AI at IBM Software, founding engineer of [Microsoft GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/), and former researcher at [IBM](https://thenewstack.io/ibm-tackles-shadow-ai-an-enterprise-blind-spot/) before that — is not a product marketing guy. He’s a researcher who became a builder who became an executive, and the through line across all three roles is the same obsession: What does it take to [make software developers more productive](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/), and what keeps getting in the way?

He’s been working on that question since 2000, before transformers, before [large language models](https://thenewstack.io/introduction-to-llms/), before anyone outside the then-mall research community thought AI and developer tooling belonged in the same sentence. The arc from there to IBM Bob — [**announced this week and already running at 80,000 users inside IBM**](https://thenewstack.io/ibm-bob-agentic-development/) — is longer than the launch press release suggests.

## Starting before anyone was watching

The first system Sundaresan built for developer productivity wasn’t anything like what we’d recognize as an AI coding tool today. It was a recommender system for API calls.

“30% of developer code is API calls,” he tells *The New Stack* in a wide-ranging interview. “If you do a class dot something, you get a long list of functions to call, and you gotta pick from there. That itself is a friction point.”

![](https://cdn.thenewstack.io/media/2026/05/428cd83c-screenshot-2026-05-02-at-08.18.19-1024x487.png)

*Sundaresan stands next to the IBM Bob mascot. (Credit Sundaresan’s LinkedIn profile)*

The goal wasn’t to generate code. It was to surface the right function call at the right moment — essentially a search ranking problem applied to a developer’s autocomplete experience.

The model wasn’t a transformer. It wasn’t even a deep learning model in the modern sense. But developers loved it, he says. And that early signal — that reducing friction at a specific, small moment in the development workflow produced outsized satisfaction — shaped how Sundaresan thinks about the problem to this day.

“Coding is an analytical task. It’s different from shopping [online],” he says. “If the system makes a wrong recommendation, or if it makes a recommendation that kind of interferes with my thought process — that matters.”

The user experience, he argues, is orthogonal to whatever the AI is doing underneath. You can have a better model and a worse product if you get the surface wrong.

He watched the model world evolve from there: Long Short-Term Memory models, early encoder-decoder architectures, the [Google transformer paper](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf), and the first GPT. At each stage, his team had already seen the problem they were trying to solve. The models just weren’t powerful enough yet. “If you go back and look at our publications, we have publications in all of this,” Sundaresan says. “Every paper would say, here’s the model for this, here’s the model for that.”

> “Even our customers were not comfortable sending over data to our own cloud. They wanted the data on the client. So, we would actually have the model run on the laptop — a lot of engineering had to be done to make sure it can work within the laptop.”

When frontier models finally arrived with enough capability to make the bigger bets pay off, Copilot was the result, he says. But by then, Sundaresan had also spent years watching what the models got wrong — and what the product design around them got wrong. The training cutoffs produced confident misinformation. The tendency to reach for the most powerful (and most expensive) model for every task, regardless of whether it warranted it. The difficulty of running capable models in the constrained environments in which enterprises actually operate.

“Even our customers were not comfortable sending over data to our own cloud,” he says of the early Microsoft years. “They wanted the data on the client. So, we would actually have the model run on the laptop — a lot of engineering had to be done to make sure it can work within the laptop.”

## Why IBM?

The obvious question, when Sundaresan describes this history, is why he took that accumulated knowledge to IBM rather than somewhere flashier. He’s direct about it: he was looking for a change after a decade at Microsoft, and IBM made a compelling case.

But the less obvious answer is that, for his particular problem, IBM’s liabilities are actually assets.

“Within software, we have almost 20,000 people. We have infrastructure, we have consulting. There are a large number of users within IBM,” he says. “If I could create something that could benefit them, that itself is a giant product.” The internal deployment — what IBM calls “client zero” — gave him something no external product launch can: a massive, diverse, captive user base willing to absorb early friction in exchange for genuine productivity gains.

The other asset is the workload mix. IBM’s internal developer population writes [Python](https://thenewstack.io/python/) and [Rust](https://thenewstack.io/rust-programming-language-guide/), yes — but also [PL/I](https://www.ibm.com/docs/en/zos-basic-skills?topic=zos-pli), [COBOL](https://thenewstack.io/cobol-everywhere-will-maintain/), [mainframe JCL](https://www.ibm.com/docs/da/zos-basic-skills?topic=collection-basic-jcl-concepts), and languages Sundaresan described as “custom languages, like slang.” If Bob could handle that range, it could handle anything an enterprise customer would bring.

“Before we even go knock on the doors of a client, we have a story to tell,” he says.

He was also direct about what he was building against. Not a horizontal tool for any developer doing any task, but a system optimized specifically for the enterprise conditions that most AI coding tools treat as edge cases: legacy codebases, strict compliance requirements, hybrid environments, and the very real cost of [AI-generated code](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) that looks production-ready but isn’t.

## The cost problem nobody talks about

One of the more candid moments in a conversation with Sundaresan is when he describes how most developers use AI coding tools left to their own devices.

> “It’s like taking your Ferrari to go buy milk. You don’t need to.”

“People will just say, ‘What model do you want to use?’ And people will pick the latest Sonnet 4.7 or whatever. And they might be running a simple prompt, but it will cost $40 for a million tokens,” he said. “It’s like taking your Ferrari to go buy milk. You don’t need to.”

Bob doesn’t expose the underlying model to users. It routes tasks automatically — to Anthropic Claude, Mistral open-source models, IBM Granite, or one of several proprietary, fine-tuned models built specifically for Bob’s environment — based on what the task actually requires.

That routing intelligence is where Sundaresan thinks the real architectural work is. “It’s not slapping on a model into the system,” he says. “It is bringing the model, bringing the experience, but also bringing the architecture that provides a great experience. All three have to come together. The model is only one part of the equation.”

He described running A/B experiments on IBM’s internal user base — testing frontier model variants against one another, monitoring usage patterns, and identifying where costly models were used for tasks that cheaper ones handled equally well. The internal deployment made that kind of experimentation possible at a scale no early-stage product could afford.

## On where the agentic market is actually going

Ask Sundaresan about the hype cycle around agentic AI, and he’ll give you the researcher’s answer, not the GM’s.

“There’s no smoke without fire,” he tells *The New Stack*. “If hype is the smoke, there is fire somewhere. It may not be as big as the smoke. But there is fire.”

His read is that agent-based development is real, but it’s not new. Service-based development, API-based development, agent-based development — all of it existed before. What’s changed is that the interface is now probabilistic and conversational rather than deterministic and programmatic. That shift creates genuine new capability, but also genuine new risk.

> “We could be afraid and not do anything at all, or we could go forward bravely but systematically.”

“You can also distract it,” he says of agent systems. “You can ask questions you’re not supposed to ask, or reveal information that it’s not supposed to reveal.” The 91% AI project failure rate he’s seen cited, he argues, comes down to discipline — or the lack of it. Companies assume that signing a deal with a frontier model provider is sufficient. It isn’t. “You need the discipline that you’re following before you incorporate them into your software product,” Sundaresan says.

The direction he’s watching, and which he thinks demands more attention than it’s getting: agents that talk to other agents, eventually in machine-native languages that humans can’t directly read. “If there are errors in those derivative languages, that error could explode,” he says. “There are lots of things to come. We could be afraid and not do anything at all, or we could go forward bravely but systematically.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)