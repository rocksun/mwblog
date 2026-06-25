Anthropic’s [rollercoaster ride](https://thenewstack.io/fable-ban-open-weights/) with Claude Fable 5 and [Mythos](https://thenewstack.io/openai-chatgpt-gpt-5-5-security/) 5 has left various deposits of fallout this year, but [the mêlée](https://thenewstack.io/anthropic-fable-mess-explained/) hasn’t stopped independent software application developers from testing the models’ purported powers via their own methods and channels.

Austin, Texas-based software developer Joe Cooper (aka swelljoe) has said he is skeptical about how well Mythos might find really challenging security bugs and cyber vulnerabilities.

## A rich enough blend for debugging – will it Mythos?

“The idea was to gather up bugs that were specifically found by Mythos, as covered by [Anthropic’s own](https://red.anthropic.com/2026/cvd/) documentation [and start to build a benchmarking service],” [wrote Cooper](https://swelljoe.com/post/will-it-mythos/), on his blog.

“[I wanted to] find the commit from before the bug was fixed, verify that a top-tier model ([Opus](https://thenewstack.io/claude-opus-48-release/), in this case) can identify and understand the bug if pointed right at it, and add that to our corpus for benchmarking whether models going in blind can accurately detect and describe the bug,” explained Cooper.

In homage to the [Will It Blend?](https://en.wikipedia.org/wiki/Will_It_Blend%3F#:~:text=Other%20technological%20devices%20were%20blended,shredded%20or%20the%20boxed%20iPad.) YouTube infomercial video series, which served as a marketing vehicle for the Blendtec line of blenders featuring founder Tom Dickson attempting to blend everything from a whole chicken to an iPhone 4, Cooper’s analysis piece this May was amusingly titled Will It Mythos?

The description of his process noted that he had previously built a tool called [Nelson](https://github.com/swelljoe/nelson) to automate bug hunting in his own projects. He noted that he had “already noticed there are surprising differences” among the various models (Nelson works with a variety of models via [Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), Gemini CLI, and OpenAI-compatible APIs) and in how effectively they identify bugs.

But he wanted hard numbers, and so he mostly used Claude to cook up a benchmark suite that borrows some code from Nelson and takes Mythos to task.

## Zero-day vulnerabilities in every major operating system

With his ambitions to test bug gathering according to “Anthropic’s own documentation”, let’s remember here that [Anthropic famously said](https://www.anthropic.com/research/mythos-preview?utm_source=tldrai) that during its testing, it found Mythos Preview was capable of identifying and then exploiting zero-day vulnerabilities in “every major operating system and every major web browser” when directed by a user to do so.

> “The toughest bugs are multi-file bugs. The models were free to look at all files, but one often needs to know the context to know that a given usage is a problem. This is a hard problem for any security reviewer, human or AI.”

Ultimately, he wanted to find out whether models going in blind can accurately detect and describe a bug. Cooper’s system was built so that the models used can look at the whole code repository and follow logic across file boundaries, but they’re not told what to look for.

“The toughest bugs are multi-file bugs. The models were free to look at all files, but one often needs to know the context to know that a given usage is a problem. This is a hard problem for any security reviewer, human or AI,” Cooper says.

He said he assumed Mythos has more advanced tooling and perhaps runs the software in a debugger or performs [fuzz testing](https://thenewstack.io/defend-autonomous-vehicle-from-threat-actors-with-fuzz-testing/).

## Some credence that Mythos is particularly good at this

“Guessing at everything Mythos might do is beyond the goals of this project for now. But there are bugs in this corpus that are extremely hard to find, giving some credence to the notion that Mythos is particularly good at this problem,” conceded Cooper.

> “It almost certainly leads in raw capability, so in that sense, Mythos is engineered to blend an expansive range of bugs. But it’s important to recognize the difference between simply leading a benchmark, versus gating all security progress on one model.” – Conor Sherman, Sysdig.

## Raw model capability is not the same as gate-all security

As opinions on Anthropic’s new model abilities start to crystallize, we will gradually gain more real-world insight into their working mechanics.

[Conor Sherman](https://www.linkedin.com/in/conordsherman/), global CISO at runtime security specialist [Sysdig](https://www.sysdig.com/) is a glass-half-full kind of guy, he tells *The New Stack* that Mythos stands apart from other AI models.

“It almost certainly leads in raw capability,” Sherman says. “So in that sense, Mythos is engineered to ‘blend’ an expansive range of bugs (but perhaps not a whole chicken or iPhone), and it has an inherent ability to perform well when hunting out the multi-file bugs that stump everything else seems to be where it’s most notably ahead.”

But there are caveats here: Sherman advises that it’s important to recognize the difference between simply leading a benchmark and gating all security progress on one model, like some kind of cyber wonder-panacea.

“A less capable but less expensive model wired into the right scaffolding can close most of that gap,” explains Sherman. “The edge that actually matters for defenders isn’t model-versus-model on a corpus of known bugs. Security in an age of AI-powered threats requires runtime context and real-time signals that equip teams to act at the speed at which today’s attackers move.”

[Fabien Renaudineau](https://www.linkedin.com/in/fabienrenaudineau/), co-founder and co-CEO at AI-native synthetic testing company [Mozark](https://www.mozark.ai/), tells *The New Stack* that in terms of pure capability, agentic testing and debugging tools are improving very quickly, and it “would be a mistake” to underestimate them.

“Systems in this class can already help engineers reason through larger code contexts, identify likely failure paths, and accelerate remediation,” Renaudineau says. “But whatever the benchmark, blend or breed… production reliability is not determined only by what an agent can do.”

Renaudineau draws a line here and says that debugging reliability can only ever be determined by how a tool’s output is verified, and by what we choose to base that verification on – and the first principle here is that an “agent itself cannot be the credible judge” of its own reliability.

“Verification has to be independent of the agent, reproducible and tested against real-world conditions of use – not only against the controlled environment in which the agent was developed or benchmarked,” Renaudineau adds.

## **What DevSecOps developers should think next**

As for the original Will it Mythos man himself, Joe Cooper, noted that on the core question of whether Anthropic’s model can identify really challenging bugs, his benchmark answers “with a resounding, maybe” in this test.

“Mythos, maybe, really is better than the other current models at finding security bugs, as it found four bugs that no model in this experiment found. But I’ll keep testing. It’s possible prompt or tooling or harness changes can enable better results from the current crop of publicly available models,” concluded Cooper. “Over time, I’ll evolve the corpus. It may become a more generic CVE-based benchmark if Anthropic stops bragging about specific bugs.”

With interest and anticipation in Anthropic’s latest batch so fervent and with the work carried out in areas such as [Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) being so cloak-and-dagger, the fact that the software engineering community is working to provide so much (hopefully always) impartial analysis must be a good thing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)