As fast as the technology industry is formalizing the term Human-In-The-Loop, the global automation lobby is seeking to push the term into obsolescence in as many aspects of AI as possible.

This March saw French generative development specialist [Mistral AI](https://thenewstack.io/codestral-a-step-closer-to-ai-driven-coding-for-the-masses/) launch [Leanstral](https://mistral.ai/news/leanstral), an open source code agent designed to pop the cork on the “human review bottleneck” in software engineering. Before we ask how effective this tool might be and question its possible unknowns and future trajectory, let’s remind ourselves how it works.

## Formal verification, mathematical proof

Leanstral uses a process of formal verification to mathematically prove that any given piece of code is capable of performing exactly as specified, with zero subtle (or inconsequential) bugs hidden between the lines. The agent uses the [Lean 4 programming language](https://lean-lang.org/#:~:text=Lean%20Programming%20Language,Copy) and interactive theorem prover to act as the logic engine behind its ability to construct machine-checkable proofs.

“We envision a more helpful generation of coding agents to both carry out their tasks and formally prove their implementations against strict specifications. Instead of debugging machine-generated logic, humans dictate what they want,” stated the Mistral AI team.

Whirring away inside Leanstral, Lean 4 uses a highly sparse architecture and makes use of parallel inference (where multiple computations occur concurrently), which makes it suitable for high-stakes mission-critical deployments in areas such as aerospace, cryptography and frontier mathematics. Its output is not just plausible, but mathematically guaranteed and it is trained to operate in realistic formal repositories.

Architecturally, Leanstral employs a [Mixture-of-Experts](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/) (MoE) model with 119 billion total parameters, but only 6.5 billion active parameters for efficiency’s sake. Released under an Apache 2.0 license, developers can access the technology via a free API and through Mistral AI’s own platform. The team has claimed Leanstral outperforms open source models, including [Qwen](https://thenewstack.io/runpod-ai-infrastructure-reality/), Kimi and GLM – and further stated that it [outstrips Claude 4.6](https://thenewstack.io/claude-sonnet-46-launch/), at less cost.

## Blowing in the wind?

As mathematically exacting as Mistral AI’s Leanstral is purported to be, just how perfect is this technology likely to be in real world deployments? Named after the [famous French wind](https://francetoday.com/culture/le-mistral-the-wind-of-provence/) that whistles through Provence, can Mistral guarantee to keep a steady footing once applied to working live production environments?

Let’s perhaps remember, this is not a promise to create perfect code; this is a promise to create perfect code if the perfect application specifications have been laid down by the human developer (humans, remember them?) in the first place. Application specifications can be rigorously formal, but equally, they can be flaky.

> “Formal verification can prove that code matches a specification, yet AI risk rarely lives just in the math; it lives in whether the specification is complete, contextual, and aligned with reality.” – Judah Taub.

## X-ray (application) specs

More brittle specs might arise because the users have failed to convey application or data service requirements in enough detail, or in situations where the developer requirements team didn’t communicate with enough stakeholders to ensure the product build is fit for purpose. Specs can also fall down due to lack of version control and scope creep i.e. developers should be building to a current and correct mandate, not to outdated notional instructions that fail to take edge-case handling (where uncommon error states may occur) into account.

Set even the most mathematically perfect code-building agent out in the wrong type of boat on the wrong course and you end up in the perfectly wrong location.

Mistral AI tells us that the Lean4 proof assistant is capable of expressing complex mathematical objects such as perfectoid spaces (complex arithmetic geometry spaces that link different fields), but those perfectoids need to be aligned to the right North Star.

[Judah Taub](https://www.linkedin.com/in/judah-taub-3773247b/), founder and managing partner of [Hetz Ventures](https://www.hetz.vc/) is a former Israeli intelligence officer and adviser to governments on AI, cybersecurity and defense strategy. Taub tells *The New Stack* that Leanstral is a real step toward faster, more automated software development, but it doesn’t eliminate the need for human judgment.

“Formal verification can prove that code matches a specification, yet AI risk rarely lives just in the math; it lives in whether the specification is complete, contextual, and aligned with reality. In production, edge cases, shifting requirements and unintended consequences still matter. This isn’t the end of human-in-the-loop, it’s a shift to higher-level oversight where humans define what ‘correct’ actually means,” Taub says.

## Switching languages, mind the gap

Charles Jasthyn De La Cueva explains and clarifies a very key consideration, [writing on Open-TechStack](https://open-techstack.com/blog/mistral-leanstral-open-source-ai-agent-proves-its-own-code/) this March, a site he founded. Importantly, De La Cueva reminds us that when it comes to Leanstral DNA, the domain is Lean 4… so if a development team’s codebase is written in Rust, Python, or TypeScript, Leanstral doesn’t directly verify the code.

“You write the spec and implementation in Lean, get the verified version, then translate to your target language. The proof gives you confidence, but there’s a gap between ‘proven correct in Lean’ and ‘correct in your production language’ going forward,” he wrote.

> “As we increase the volume of code, we’re increasing the surface area of risk. I suspect developers and businesspeople alike are going to need a lot of human judgment in the near term to figure out how to think about these risks in any complex system.” – Alation CEO Satyen Sangani.

The reality of the situation on the ground is that, given the sheer volume of machine-generated code out there now, companies are already making use of agents for code review. [Satyen Sangani](https://www.linkedin.com/in/ssangani/), CEO and co-founder of data intelligence platform company [Alation](https://www.alation.com/) tells *The New Stack* that the reliability of these agents depends entirely on the context they have available to them.

“This core context requirements means agents need to know what business-specific rules an agent needs to follow (and that includes those that are not in the original product requirements document),” Sangani says. “The agent also needs to know what possible risks are that this new code introduces – and what other agents exist. As we increase the volume of code, we’re increasing the surface area of risk. I suspect developers and businesspeople alike are going to need a lot of human judgment in the near term to figure out how to think about these risks in any complex system. Engineers might not have to do as much detailed code review, but they absolutely will have to constantly think about the risks and feed the systems more and more context.”

## Redefining Human-In-the-Loop

Perhaps the question we need to come back to is, is Human-in-the-Loop applicable to all scenarios? [Eric Avery](https://www.linkedin.com/in/eric-m-avery/), global head of infrastructure and data at [Sumo Logic](https://thenewstack.io/why-sumologic-embraced-the-opentelemetry-standard/) tells *The New Stack* that Human-in-the-Loop should be viewed as a “set variable” today. This means the question has to become ‘where is the Human-in-the-Loop’, not is there ‘Human-in-the-Loop’?

“While we might get there one day with true neural networks mirroring the human mind, we are not there yet,” Avery says. “Until that day comes, there will always be a human involved, whether it is to set up the agent’s functionality, monitor and maintain the agent, or guide it at set intervals in the process for functional or compliance requirements.”

He further muses that AI consumption is driven by use, even if we would like to imagine we operate in a world of mature AI adoption. Avery underlines the fact that many users are still in the process of reskilling, upskilling, and making mistakes in their individual AI journeys leading to inflated consumption, no matter the tool, data architecture, or infrastructure.

## Future factors & frailties

Mistral AI has been initially open about its free tier of access, but the company may have been more economical with any insight as to how it will change its pricing structure if and when the wind whips up (last breeze-related pun there, apologies) around and throughout the Leanstral user base.

The more circumspect observer might also suggest that, as we stand today in the early stage with this toolset, there will logically be a gap between mathematically proven and securely deployed in a fully compliant manner at scale across complex, real world distributed compute environments.

Mistral AI claims that the time and specialized expertise required to manually verify code has become the “primary impedance of engineering velocity” today. But for many, the human-in-the-loop will be regarded as more of a lynchpin than a bottleneck in the world of AI-driven code generation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)