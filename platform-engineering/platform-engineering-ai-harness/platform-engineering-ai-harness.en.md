If most software will soon be built by machines, the job of software engineers will change: from writing software to building the machines that write it.

Soon, engineers won’t be classified as frontend or backend, but as product engineers, who build the customer-facing product, and platform engineers, who build the tools those product engineers use. And since more and more code will be written by machines, we’ll need more platform engineers to build and fine-tune those machines.

> “Call it harness engineering, call it loop engineering. It’s still platform engineering, and it’s building the tools every engineer depends on to write code at all.”

I’ve been thinking about it ever since the tokenmaxxing fiasco, and every time I read one of those reports showing that faster code generation, more often than not, just creates more friction downstream. Every team is wiring up its own prompts, its own guardrails, its own dashboard for tracking what the agent got wrong, none of it shared, all of it repeated across the org. Fragmentation, not speed, is what a hundred engineers each solving the same platform problem alone gets you.

Platform engineering, per its definition, means building the shared toolchains and workflows that let engineering orgs serve themselves, usually packaged into one [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") covering everything an application needs across its life cycle. In plain terms, it’s developers building tools for other developers so the rest of engineering can [ship with less friction](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness). If you’re helping developers ship software with less friction, congratulations! You’re already doing some form of platform engineering.

## Two teams converging into one

I recently [spoke to Vanitha Kumar,](https://www.aviator.co/podcast/ai-code-review-vanitha-kumar) a technology consultant at ThoughtWorks, who’d arrived at a similar realization from a different angle. She and a colleague were mapping a team topology diagram for a client and found themselves drawing two separate boxes labeled “platform”: the familiar one for CI/CD and delivery infrastructure, and a newer one named “agentic developer platform,” which frameworks and models developers are allowed to use, where AI cost controls live, and where the guardrails for agentic development sit. Partway through, they realized it wasn’t going to stay two boxes.

It converges into one platform that owns delivery infrastructure and agentic guardrails together, and that platform’s reach keeps moving earlier into the lifecycle. Platform engineering used to start at the first commit. Now it starts before any code exists.

For the last two years, AI coding tools have drastically changed the job of classic software engineers, the people writing application code by hand. Most platform engineering work was already automated: [infrastructure as code](https://thenewstack.io/amid-licensing-uncertainty-how-should-iac-management-adapt/), scripted pipelines, and not much manual coding for an agent to accelerate.

> “Every company that ships software is, in effect, becoming a dev tools company.”

Now that AI is generating application code at scale, the team that has to build the machinery to control, [**verify**](https://www.aviator.co/verify), and scale that code generation is platform engineering. Every company that ships software is, in effect, becoming a dev tools company: building the tooling its own engineers [need to work with agents safely](https://thenewstack.io/securing-ai-agent-systems/), with the same seriousness it builds anything it sells externally.

## Harness engineering is platform engineering for AI

Harness engineering, or building and maintaining the harness, the feedback loops, the guardrails, and the [context an agent needs](https://thenewstack.io/context-lake-ai-agents/) to work safely in a codebase, is just platform engineering with an AI-specific layer on top of what platform teams already know how to do.

We can invent new terms like harness engineering, loop engineering, or software factories – that’s all just platform engineering, the discipline of making the process of building software easier.

Platform engineering for AI engineering could, for example, mean working on building your engineering org’s [anti-AI slop register](https://www.aviator.co/blog/how-an-anti-slop-registry-stops-ai-generated-code-from-violating-your-engineering-standards/): a list of [Invariants](https://docs.aviator.co/verify/concepts/invariants?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness), a list of rules specific to your codebase that automatically apply to every matching change. That list usually captures something your team learned the hard way, usually as a recurring review comment, so reviewers don’t have to flag it again. Developers don’t need to include them in the specs because the system automatically loads the matching set.

A good harness does two things: it raises the odds the agent gets the task right on the first pass, and it gives the agent a way to catch and fix its own mistakes before a human ever sees them. Done well, that [cuts review toil](https://www.aviator.co/verify), raises the quality of what ships, and saves tokens.

If you skip that work, agents will keep making the same mistake forever, and you will only ever catch problems after they happen, not before. Frontier models give engineers the tools to generate code faster, but they still require platform teams to assemble, guardrail, and harness them, and to prevent them from becoming a faster way of shipping slop.

## What platform engineering now owns

The scope is bigger than keeping the agent tooling running. It includes which models and frameworks get approved because that decision carries security and cost implications. It includes usage and scaling because rolling agentic coding out to hundreds of engineers looks nothing like rolling it out to ten.

It includes cost because unmanaged usage gets expensive fast. It includes authorization because an agent acting on an engineer’s behalf isn’t the same as the engineer, and handing it identical access is a mistake a lot of orgs are already making.

And it includes the harness itself: the feedback loops that take what a security scanner or a linter finds and route it back into the agent instead of just failing a build.

None of that is product engineering’s job. It’s platform engineering becoming what a growing part of the industry has started calling the control plane: the layer that decides what every agent in the org is allowed to touch and how.

This is where the org charts will start to change. Building and maintaining the harness, the feedback loops, the guardrails, and the context an agent needs to work safely in a codebase is ongoing work, not a project with an end date.

Platform engineering was long seen as a supporting function, useful but never the center of gravity. That will change once the platform owns everything above. In plenty of orgs, more engineers will end up on the platform side, building and maintaining the harness, than on the product side, because the harness is now the harder part of the job.

> “Anthropic or OpenAI give you the raw agent, the ‘engine.’ But that engine has no idea what your codebase looks like.”

Anthropic or OpenAI give you the raw agent, the “engine.” But that engine has no idea what your codebase looks like, what conventions your team follows, how much risk you’re willing to take, or what your budget is. Turning it into something that respects those specifics is work only the platform team can do.

If nobody does that work deliberately, it still happens, just badly: each team builds its own patchwork version of the same governance layer, with nobody clearly responsible when it breaks.

## Building the factory that builds software

When machines write most of the code, the productivity gains come from how strong the machinery is, and broken tooling means you can’t ship quality software no matter how good the people running it are.

How productive an engineering org becomes with AI has nothing to do with which model it’s paying for, how strict the adoption mandate is, or how fast it chases whatever’s trending — loop engineering this month, graph engineering the next.

It comes down to one thing: whether the people building the tools, the platform engineers, are treated as a supporting function.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)