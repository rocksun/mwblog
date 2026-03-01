[Andrej Karpathy](https://www.linkedin.com/in/andrej-karpathy-9a650716/) probably didn’t set out to retire “vibe coding” just a year after popularizing it, but time and [technological](https://thenewstack.io/why-there-might-be-something-to-vibe-coding-after-all/) advancement forced his hand. The developer community is at a crossroads — clinging to a label while navigating a landscape that has evolved beyond it.

[Karpathy recently suggested “agentic engineering”](https://thenewstack.io/vibe-coding-is-passe/) as a more accurate description of where [AI-assisted development](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/) has landed. A collection of tech industry voices responds here to [Karpathy’s reframing of “vibe coding” as “agentic engineering.”](https://x.com/karpathy/status/2019137879310836075)

“I think vibe coding is going to be the term that sticks — the genie is out of the bottle,” [Gene Kim](https://www.linkedin.com/in/realgenekim/), [author of the book *Vibe Coding*](https://thenewstack.io/devops-pioneer-vibe-coding-100x-bigger-than-devops-revolution/) and longtime observer of software development culture, tells *The New Stack*. Kim had his own naming debate with his co-author, [Steve Yegge](https://www.linkedin.com/in/steveyegge/), who had gone back and forth over what to call their book on the subject.

“I wanted ‘vibe engineering’ to be our book title, but the problem is that no one knew what that was,” Kim says. “Isn’t it funny and ironic that even Dr. Karpathy can’t put the genie back in the bottle, despite his incredible stature in the industry?”

Karpathy is one of the most respected figures in AI. He is a co-founder of OpenAI, a former Tesla AI director, and the person who popularized the term he is now reshaping.

## From prototype to production

This is not simply an issue of semantics. It’s that the practice itself has changed faster than the words used to describe it.

“Vibe coding is great for prototypes but not wonderful for brownfield or production code,” [Andrew Cornwall](https://www.linkedin.com/in/acornwall/), a Forrester Research analyst who tracks developer experience trends, tells *The New Stack*. Cornwall says he sees agentic development as the natural successor for professional developers. “Most developers have adopted GenAI assistance, and agents promise next-level benefits to the developers who can become proficient with them.”

Meanwhile, [Diego Lo Giudice](https://www.forrester.com/analyst-bio/diego-lo-giudice/BIO1769), an analyst at Forrester who has been researching the future of software development for years, notes that Forrester had anticipated Karpathy’s reframing in a Q4 2024 prediction.

“Vibe coding will transform into vibe engineering by the end of 2026,” Lo Giudice wrote at the time — nearly 14 months before [Karpathy’s recent tweet](https://x.com/karpathy/status/2019137879310836075).

For Lo Giudice, the transformation has two dimensions. “Companies can adopt vibe coding only if it is followed by a strong engineering productization process,” he tells *The New Stack*. But there’s also a skills dimension, he notes.

“There is an engineering art to vibe coding — which transforms it to Vibe Engineering — that only those who know about software engineering can really succeed with,” Lo Giudice says.

Vibe coding, as Karpathy originally defined it, is a loose, intuition-driven process: Describe what you want, accept what the model generates, and iterate quickly without deep concern for the underlying structure. That works for weekend projects. It breaks down at scale, experts say.

## The step change nobody expected

What has accelerated this terminology debate is a shift in what AI agents can do.

“There’s been a huge step change in agent coding capabilities in the last one to two months,” [David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of [Arcjet](https://arcjet.com/), tells *The New Stack.* “They’re now capable of completing complex tasks when just a few months ago it would still require multiple human/agent iterations.” Arcjet provides an AI-powered security platform for developers.

Moreover, Mytton notes that: “I’m finding that it only works when there are clear guardrails in place — good code documentation and comprehensive tests the agent can run. That’s what differentiates vibe coding from vibe engineering. ‘Engineering’ is about discipline and structure — then the AI agents can really run with it — otherwise you end up looping through ‘it still doesn’t work’ trial and error.”

The orchestration of AI agents is a step beyond vibe coding, says [Mayank Agarwal](https://www.linkedin.com/in/mayank-ag/), co-founder and CTO of [Resolve AI](https://resolve.ai/), which provides AI agents to help enterprises resolve incidents.

“Karpathy’s framing resonates. Agentic engineering more accurately captures the shift in how engineers are operating today. You’re not writing code directly, you’re orchestrating agents, and that takes real discipline,” Agarwal tells *The New Stack*. “The speed to produce code doesn’t match the speed to productively absorb it, and without proper engineering practices, agentic workflows just generate tech debt at machine speed. Vibe coding always felt sloppy as a label. What we’re seeing now requires more rigor, not less.”

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group who follows AI infrastructure closely, notes that the technology has made a significant leap in capabilities. He says he likes the term “agentic engineering”, as he has grown increasingly uncomfortable with the term “vibe coding” within the context of “proper” software development. Shimmin says vibe coding was an apt phrase a year ago, when agent tooling struggled to scale beyond one-shot, hobbyist endeavors.

However, “Fast forward to today, we’re talking about tools capable of building a fully working compiler in Rust via multiple agents working in parallel,” he tells *The New Stack*. “Talking about that scale and complexity leaps way beyond ‘feeling the vibes’ of agentic coding.”

Shimmin says he sees the field at an inflection point.

“We are right now rethinking and re-architecting the very toolchains humans use to build software, transitioning those systems — agent harnesses, code check-in/out, and so on — to both accommodate and empower the unique capabilities and limitations” of AI agents, he says. “That is engineering, not ’emotioneering.'”

## The harness is the differentiator

Meanwhile, [Randall Hunt](https://www.linkedin.com/in/ranman/), CTO of cloud-native services company [Caylent](https://caylent.com/), says we should not be so concerned about what to call the practice, but where the actual value lives.

“Karpathy’s ‘agentic engineering’ framing is useful because it shifts the conversation from the model to the system around it,” Hunt tells *The New Stack*. “At Caylent, we’ve always said that the model will trend towards a commodity. Our smartest customers and enterprises understand that the differentiator isn’t which LLM you picked, it’s the agentic harness.”

By “harness,” Hunt means the full system surrounding the model: tools, context management, evaluation, and observability infrastructure. “If you don’t engineer the harness, you don’t get compounding leverage; you get compounding cognitive debt.”

Hunt argues that in 2025, technical debt was the dominant burden on engineering teams. In 2026, he sees cognitive debt — the accumulated cost of poorly managed AI interactions, context loss, and unreliable agent behavior — taking over as the primary threat.

[Spiros Xanthos](https://www.linkedin.com/in/spiros/), CEO and co-founder of Resolve AI, says he agrees with Karpathy.

“Karpathy’s correct that LLMs are here to stay in software engineering,” Xanthos tells *The New Stack*. “Vibe coding has spread throughout engineering teams from startups to the enterprise, and as that AI-generated code makes its way into production environments, we’re realizing a new problem: running production. The bottleneck isn’t generating code anymore. It’s understanding what’s happening when that code breaks. If agentic engineering is about orchestrating agents to build, the next frontier is orchestrating agents to run and fix what they’ve built.”

Meanwhile, [Tanuja Korlepra](https://www.linkedin.com/in/tanuja-korlepra/), CTO of social impact technology provider [Bonterra](https://www.bonterratech.com/), describes what agentic engineering looks like inside her organization.

“With agentic engineering, our developers are not writing code manually most of the time,” she tells *The New Stack*. “We are using agentic AI coding tools, orchestrating the agents that write the code, and acting as managers of agents. There is a real art and science to doing this well, and our team is building deep expertise in it.”

Korlepra says Bonterra took that philosophy and put it in the hands of its customers through Que. Bonterra Que is an agentic AI platform built for nonprofits, foundations, Corporate Social Responsibility teams, donors, and volunteers.

“A nonprofit fundraiser can simply instruct Que the way a manager would instruct a capable team member,” Korlepra says. “Tell it to segment donors, draft an email, and build a donation form. It handles the operational heavy lifting so they can focus on their mission.”

## Long live vibe coding?

[Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research who tracks enterprise software trends, provides a pragmatic take. Vibe coding, he argues, was never really meant to be a permanent mode of professional development.

“Vibe coding as an activity was pretty much obsolete from the get-go, as it was clear that autonomous agents are going to be key for the [SDLC](https://thenewstack.io/how-generative-ai-is-reshaping-the-sdlc/),” Mueller says — pointing to [Google](https://cloud.google.com/?utm_content=inline+mention)‘s multi-agent demos from December 2024 as an early indicator.

“Vibe coding was a key aspect to gain the trust of developers to now run multiple agents in parallel, doing and helping with their work,” he tells *The New Stack*.

Mueller says he views vibe coding as an on-ramp — a way for millions of “developers” to get comfortable enough with AI assistance to graduate to something more rigorous.

Gene Kim, who spent a year debating book titles over this issue, acknowledges the advances in agentic technology and vibes with Mueller’s premise.

“Long live vibe coding,” he told *The New Stack* in a summation of our conversation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)