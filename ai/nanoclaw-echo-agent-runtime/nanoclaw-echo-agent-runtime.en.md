**When he’s asked about the intensifying contest** between rapidly advancing AI attackers and the software defenses meant to contain them, NanoClaw co-founder and CEO Gavriel Cohen answers this way:

“There’s been a clear vibe shift,” Cohen tells *The New Stack*. He may be putting it lightly.

One of the clearest signs of this paradigm came last week when OpenAI [disclosed](https://openai.com/index/hugging-face-model-evaluation-security-incident/) that [GPT-5.6 Sol](https://thenewstack.io/openai-gpt-56-live/) and an even more capable pre-release model — operating with reduced cyber refusals during an internal evaluation — had circumvented constraints in a highly isolated test environment. The models chained vulnerabilities across OpenAI’s research systems and Hugging Face’s production infrastructure, ultimately accessing a Hugging Face production database. OpenAI called it an “unprecedented cyber incident.”

***See also:*** [***What really happened in the Hugging Face breach***](https://thenewstack.io/openai-huggingface-sandbox-breach/)

**Against this backdrop**, Cohen’s [NanoClaw](https://nanoclaw.dev/), an open-source framework for AI agents, and [Echo](https://www.echo.ai/), a secure software infrastructure provider, announced a partnership on Wednesday to harden the software environment in which NanoClaw agents operate.

The companies say the hardened NanoClaw runtime ([available now on GitHub](https://github.com/nanocoai/nanoclaw)) extends protection into the browser, tools, and libraries that agents use. It is intended to close an attack surface that isolating an agent does not address.

“With Echo’s hardened version of the NanoClaw agent runtime, NanoClaw becomes the first open source agent framework to give its community a hardened agent environment, secured all the way down to the software it runs on,” the companies say in a joint statement.

The partnership builds on NanoClaw’s original security argument. In an [earlier interview with *The New Stack*](https://thenewstack.io/nanoclaw-openclaw-agent-security/), Cohen described OpenClaw’s roughly half-million-line codebase as its “fatal flaw,” so he built NanoClaw as a smaller, more auditable alternative and put agents in [isolated containers](https://thenewstack.io/nanoclaw-containerized-ai-agents/) so they could run commands without gaining unrestricted access to the host machine.

But isolation handles threats going in only one direction.

When asked what has changed, [Cohen](https://il.linkedin.com/in/gavrielco) points to a new generation of cyber-capable models.

“New models like Mythos are supercharging attackers,” Cohen tells *The New Stack*. “It’s now much easier to launch sophisticated attacks that string together many vulnerabilities into a working exploit. Living with known unpatched vulnerabilities used to be an accepted fact of life. That’s no longer acceptable.

> “New models like Mythos are supercharging attackers.”

“Sandboxes need to be sealed in both directions,” Cohen continues. “An agent shouldn’t be able to escape, and because agents are now doing real work, an outside attacker shouldn’t be able to get in through the tools the agent uses.”

## A runtime … hardened in *both* directions

With more people putting agents to work, security cannot be left entirely to the user to sort out. A rogue agent is a risk to the customer and the community. But an attacker who compromises an agent through its browser, a file parser, or another tool can be just as dangerous.

Cohen compares a modern prompt injection to a social engineering attack. An agent can be lured to an innocent-looking page, where a known browser flaw turns the visit into a compromise. A vulnerable parser can similarly turn opening a file into code execution.

NanoClaw and Echo say they built the hardened runtime together. NanoClaw defines the agent environment, isolation, and policy layer. Echo rebuilds the software in that environment from source, using only the essential components, and then applies patches for known vulnerabilities.

The companies say the process cuts the number of known vulnerabilities from thousands to near zero. The resulting runtime includes the components an agent commonly uses: Chromium, Node.js, Bun, pnpm, Corepack, Git, curl and unzip.

> Echo says every new disclosure is triaged within 24 hours, with critical and high-severity fixes shipped within hours under its enterprise service-level agreement.

Echo says its purpose-built AI agents monitor newly disclosed vulnerabilities, determine which software is affected, find or develop fixes, test compatibility and open pull requests for human review. The company says every new disclosure is triaged within 24 hours, with critical and high-severity fixes shipped within hours under its enterprise service-level agreement.

## Chromium *without* a fork

The Chromium browser would appear to be an obvious attack surface. Its large Common Vulnerabilities and Exposures count, however, also reflects the scrutiny directed at one of the world’s most widely deployed software projects.

[Eylam Milner](https://il.linkedin.com/in/eylamm), co-founder and CTO of Echo, tells *The New Stack* that the company does not plan to maintain its own Chromium fork.

“Rather than maintaining a fork, Echo rebuilds Chromium directly from source and feeds it through Echo’s automated CVE-patching pipeline,” Milner says. “The browser stays true to upstream and ships fully patched and hardened. This gives Echo users fast remediation without sacrificing compatibility.”

Milner says Chromium alone contains about 30 million lines of code and follows a relentless release cadence. Echo’s aim is to preserve modern browser capabilities while continuously patching known vulnerabilities, not to trade compatibility for a bespoke browser.

## A choice, not a mandate

The hardened runtime will not replace NanoClaw’s standard release. NanoClaw will continue to maintain and develop the project, while each release will have both a standard container image and a hardened version provided by Echo.

Milner says Echo independently rebuilds the hardened image from source in isolated environments, signs it, attaches a verifiable software bill of materials, and continuously patches it under the company’s CVE service-level agreement. Users can opt in to that image, while the unauthenticated path for building an agent runtime locally remains available.

NanoClaw will recommend secure configurations and make good defaults part of the open source project, but it will not mandate them.

> “NanoClaw is MIT licensed and built to be forkable.”

“NanoClaw is MIT licensed and built to be forkable,” Cohen tells *The New Stack*. “Anyone can adapt it as they see fit for their own needs.”

The frontier models complicate the picture because they can both identify vulnerabilities and exploit them. Cohen says NanoClaw uses Fable extensively in development, but that access to Mythos for defensive cybersecurity work is highly restricted.

That imbalance helps explain the urgency. NanoClaw has been positioning agents as safe, responsible tools rather than the [heroic outlaws seen earlier this year](https://thenewstack.io/openclaw-github-stars-security/). The partnership extends that logic from the agent’s behavior to the software beneath it.

Despite the close technical collaboration, Cohen says there are no plans for NanoCo and Echo to combine.

Is this an early shot in an arms race, or simply the cost of doing business in an insecure space? Cohen does not draw much of a distinction.

“The race is on, and getting defenders access to capabilities so they can stay ahead of attackers is the whole game,” Cohen tells *The New Stack*.

The walls are going up, and we know why.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)