A quiet revolution is brewing in the AI model space. The dominance of [proprietary closed frontier models](https://thenewstack.io/proprietary-ai-models-are-dead-long-live-proprietary-ai-models/) has been cemented by global public fascination, which has percolated upward to interest governments and regulatory bodies from the [US](https://thenewstack.io/openai-defense-department-debate/) to [Europe](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) and [China](https://uk.practicallaw.thomsonreuters.com/8-618-2325?transitionType=Default&contextData=(sc.Default)&firstPage=true).

Despite the dominance, the open-source community rarely shies away from battle ([remember Windows](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) and, now, Linux and Android?) with open advocates [saying that proprietary models are merely an enterprise wrapper](https://www.linkedin.com/posts/borisrenski_open-source-models-are-now-only-about-4-months-share-7481767295229317120-AihK/) around the model that has memory, observability controls, routing intelligence, and connectors).

That works out to be expensive wrapping paper if open-source models are roughly 10x less per token.

## Fearmongering factor from the big firms

[Boris Renski](https://www.linkedin.com/in/borisrenski/), founder & CEO at AI agent integration startup [Apelogic](https://apelogic.ai/), tells *The New Stack* that frontier labs are “hard at work pushing fear” about uniquely smart, dangerous models and imminent AGI.

“That fear factor is designed to distract from the benchmarks that show open-source models are only four months behind at a fraction of the cost,” Renski says. “That means most of the time companies are not paying OpenAI or Anthropic for intelligence, but for ‘commodity enterprise features’ around the model like [IDP integration](https://thenewstack.io/how-idps-and-ai-are-democratizing-platform-engineering-roles/), [MCP connectors](https://thenewstack.io/build-mcp-server-tutorial/) and observability.”

![](https://cdn.thenewstack.io/media/2026/07/ae37be15-1783792326753-1024x776.jpeg)

*Credit: Epoch AI*

> “Most of the time companies are not paying OpenAI or Anthropic for intelligence, but for ‘commodity enterprise features’ around the model like IDP integration, MCP connectors and observability.”

Renski’s consternation stems in no small part from his two decades building open-source infrastructure companies, where he says he has watched “open source always catch up and often supersede” vertically integrated, proprietary stacks in capabilities and adoption. It’s a recurring pattern that he identifies across Windows vs. Linux, Oracle vs. MySQL, Docker Enterprise vs. Kubernetes, and so on.

## Is this Oracle ownership overload, all over again?

“In a few years, enterprises will look at their multi-year LLM contracts with frontier labs the same way they look at their Oracle licenses today, but it will be too late. This is because the very fabric of their business will be so deeply interwoven with proprietary LLM vendors that migrating will be impossible,” Renski advises.

[Jonathan Bryce](https://www.linkedin.com/in/jbryce/), executive director at the [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) agrees with this narrative and tells *The New Stack* that paying ten times more for a four-month capability lead is “not an enterprise AI strategy” today.

“It’s clearly not a prudent approach or strategy,” Bryce says. “In reality, it’s a very expensive form of lock-in. The frontier keeps moving, so developers should build on open infrastructure that lets them change models and hardware without rebuilding the application every time the leaderboard changes.”

Renski’s forthright opinions (and Bryce’s agreement) on this matter coincide with Featherless, a serverless inference platform company, making some bold assertions. The organization claims it can “slash frontier AI costs” through native optimization of the [Z.ai GLM 5.2](https://z.ai) open-weight Chinese AI model.

## Wait, 100 billion tokens monthly is how much?

The company released a statement on Monday, which maintains that its native optimization GLM 5.2 model on AMD private cloud infrastructure substantially reduces frontier-class AI inference expenses by an estimated 94%. According to Featherless, for a development team that operates at maximum utilization and uses around 100 billion tokens monthly, the annual cost for GPT-5.5 is $1,557,600; using Claude Opus 4.8, an identical monthly workload comes to an annual cost of $1,506,000.

If 100 billion tokens sounds like a lot, reports this year citing a Deloitte study suggest that a healthcare enterprise consumed 1 *trillion* tokens over six months.

By contrast to its proprietary model cost estimates, the Featherless private cloud option absorbs these variable factors into a fixed annual rate of $90,000, saving more than $1.46 million per year for a fully utilized development team.

## There’s no difference in the inference

Are we really going to get to a point where the big frontier brands feel the weight of open-source and open-weight models such that, ultimately, the developer (and user) will never even think about what hardware their inference runs on?

[Isaac Gemal](https://www.linkedin.com/in/isaac-gemal/), developer relations lead at Featherless, tells *The New Stack* that open-weight models have often been considered inferior or not capable of real work, but now, “GLM 5.2 has flipped that narrative” on its head. So how easy was it to get GLM 5.2 running natively on AMD instead of Nvidia hardware and what pitfalls should developers look out for?

> “Big labs often say something along the lines of… ‘We won’t log your requests, except in XYZ’ and anything their own systems decide is ‘unsafe’ gets kept anyway, sometimes for years, completely up to their own discretion. Their distinction is often vague and very broad. We think that approach is backwards.”

“It wasn’t easy; demand for GLM 5.2 was even higher than we forecasted, which took us by surprise, so allocating GPU resources effectively was a challenge at the start,” Gemal says. “We have a very talented engineering team that works with Tensorwave directly to ensure that these large model deployments go great.”

There are indeed operational constraints and gotchas to look for. Gemal advises developers to watch out for the stipulations buried in logging privacy policies.

“Big labs often say something along the lines of… ‘We won’t log your requests, except in XYZ,’ and anything their own systems decide is ‘unsafe’ gets kept anyway, sometimes for years, completely up to their own discretion. Their distinction is often vague and very broad. We think that approach is backward – we take privacy very seriously,” Gemal says.

## What do real-world developers think?

The litmus test here obviously comes down to what real-world developers and data science practitioners think of the open alternatives.

Software engineer at Poland-based Screen Studio, [Kacper Michalik](https://www.linkedin.com/in/kacpermichalik/), tells *The New Stack*that he’s been testing an open-weight model (GLM 5.2, in fact) against closed models like Opus 4.8 in real work, i.e., researching a tech stack for data engineering, algorithm problems, and component generation.

“For tech research tasks, GLM 5.2 gave me results similar to or better than Claude Opus 4.8,” Michalik says. “It has a wide scope, proactively expands on related topics, and even produces useful visual graphs. On a coding interview problem, I compared GPT, Claude, and GLM. GPT explained the thinking steps well but gave no code; Claude was condensed and clear but brief on complexity; GLM landed in the middle, i.e., clear points, a solid step-by-step explanation in words, and a working Python solution.”

Michalik notes that given a clear prompt, he feels the results are great. GLM also built a React form component with Zod and TypeScript that works correctly, is well-typed, handles the fields properly, and shows clear validation errors. He explains that it defaults to Tailwind for styling, which is standard practice now.”

“It’s not flawless,” Michalik clarifies. “When I asked it to build a 3D scene with React and TypeGPU in a single file, it couldn’t render the result correctly – I’d expected something closer to v0 or Lovable for full project generation. I also hit usage-limit warnings in the late afternoon.”

## Open source AI model safety & the race to the finish line

With a number of these open AI models coming from China, the question of safety concerns has to be brought to the table.

[Phil Whittaker](https://www.linkedin.com/in/phil-whittaker-82481716/), staff engineer at the open-source CMS company [Umbraco](https://umbraco.com/flexible-cms/?gad_source=1&gad_campaignid=23799046955&gbraid=0AAAAADL94wTNyiM1ghOBggOiOIh0LCvMK&gclid=CjwKCAjwvNfSBhBiEiwAyaGMCfVq-ptCKy21PlVj215GDafnmSclji4wNnDYekrqDN2EOftBgXFWRRoCPkcQAvD_BwE), tells *The New Stack* that he agrees open-weight (not open-source) AI models are four to five months behind the frontier models, but that’s not the whole story.

“I’m not sure I agree that these models are 10 times cheaper, as that all depends on the scale and what the goal is,” Whittaker says. “But yes, the majority of the open-weight models are Chinese. Connecting to a provider’s AI endpoints directly has security and privacy implications. Using a third-party provider such as Ollama is better, but costs are token-based, and differences in tokenizers between models could mean as little as a 50% reduction in cost.”

Finally, qualifies Whittaker, self-hosting is an option, but that requires up-front capital expenditure (servers) and ongoing maintenance. He notes that benchmarks and experience show that GLM 5.2 is “approaching the level of intelligence” of Opus 4.8 from Anthropic. The caveat here is that, although it is not as quick, it is better suited to long-running and independent tasks than to agentic coding tools, where speed of inference counts.

“Results also come from the quality of the harness that is driving the model,” adds Whittaker. “As models become more commoditized and the needs of normal users can be completed by lower-quality models, the harness and how it is configured will become more important.”

There’s a large number of moving parts here, and it already sounds hackneyed and clichéd to talk about the AI “race” as we enter what might be the mid-furlong point. What we perhaps need to analyze is how many horses are in the race, what they’re being fed on, and who’s holding the reins.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)