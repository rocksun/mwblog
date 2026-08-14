**Autonomous coding agents ignore contribution rules in open source communities**, finds a new [study](https://arxiv.org/abs/2607.26819) from researchers at Peking University.

That’s not great news for maintainers who are fast [becoming overrun by sloppy AI-generated contributions](https://thenewstack.io/ai-slop-open-source/). If coding agents aren’t even following contributor guidelines, then a simple rewrite isn’t going to do much good for reining in agent activity.

The study experiments on four frontier models, curating 106 issues from 49 repositories containing AI contribution rules and then judging each run against the repository’s rules. Researchers measured four forms of compliance: 1) refusal to contribute; 2) truthful disclosure of its assistance; 3) clearing verification gates; 4) escalation to humans.

How’d the agents perform? Not well. As the researchers wrote, “today’s agents almost never proactively retrieve the contribution rules.”

With some prodding via reminder prompts, quoted policies, and verifier feedback, the agents did improve on disclosure and verification — but they never refused to contribute to AI-banned repositories.

[Cristian-Alexandru Staicu](https://www.linkedin.com/in/crstaicu/), senior security researcher, [Endor Labs](https://www.endorlabs.com/), describes the conflict as an “ethical dilemma” for the agent:

“Imagine that an agent is asked to ‘fix an annoying bug and make a pull request’ to a project that has the clause listed in Figure 1 of the study, ‘This project does not accept pull requests that are fully or predominantly AI-generated,’” Staicu tells *The New Stack*. “Now the agent is in an ethical dilemma. Should they comply with the user’s request or with the policy?”

## Agents aren’t not listening. They’re just hyper-focused on the task at hand.

Pointing to the recent [Hugging Face incident](https://thenewstack.io/openai-huggingface-sandbox-breach/), where autonomous AI systems escaped a sandbox and breached the production infrastructure, [Mike McNeil](https://www.linkedin.com/in/mikermcneil/), CEO, [Fleet Device Management](https://fleetdm.com/), and founder, [The Sails Company](https://sailsjs.com/studio), reminds developers that agents don’t always follow prompts, which is why they might fail to respect repository-specific contribution rules.

> “Disclosure and verification are additive: The agent can complete the user’s task and comply. A ban requires the agent to abandon the task, which collides head-on with the user’s explicit instruction and with the agent’s training to be helpful.”

“The AI is very focused on trying to do its prime directive,” he tells *The New Stack*. “It wants to get the task that it’s been given done, and as we saw with Hugging Face, it’s willing to do anything to get that done.”

Analyzing contribution policies is simply not part of how agents are typically built and trained, says Staicu: “Agents almost never open the policy files on their own, so the rules never enter their reasoning at all.”

Still, why do reminders, quoted policies, and feedback help push agents to respect disclosure and verification requirements but not those for AI bans and escalation? Staicu tells *The New Stack* the difference is in the rule’s ultimate impact on the task:

“Disclosure and verification are additive: The agent can complete the user’s task and comply. A ban requires the agent to abandon the task, which collides head-on with the user’s explicit instruction and with the agent’s training to be helpful.”

In other words, the agent doesn’t abide by some rules that tell it to give up because it’s so hard-wired to get the task done.

[Timo Bozsolik-Torres](https://www.linkedin.com/in/timobozsolik/), head of AI, [SandboxAQ](https://www.sandboxaq.com/), agrees, saying that the behavior isn’t a question of whether or not the agent understands the rules: “If this were a comprehension problem, a stronger model would close the gap. Instead, the opposite happens; GPT-5.5, the best model tested, is also the most stubborn refuser.”

## Does this mean rewriting contribution policies is a waste of time? What else maintainers can do

In a move to curb AI slop, Godot Engine, the open-source game engine, is [rewriting its contribution policy](https://thenewstack.io/godot-bans-ai-coding-agents/) to bar most AI-generated code from its repositories. It’s not alone. Programming language Zig and terminal emulator Ghostty are also updating policies to control AI use in contributions.

But if the Peking University study shows that coding agents, when acting autonomously, largely ignore contribution guidelines, then simply rewriting policy may not be enough.

Instead, experts advise putting controls outside the agent.

“Stop expecting the model to remember to go read CONTRIBUTING.md and instead make policy discovery part of the harness, as opposed to the model’s judgment call,” says Staicu.

That may help agents proactively retrieve contribution rules, but what about AI bans, which agents dismiss, even when reminded? “Labs would need to go further,” Staicu acknowledges, “and fine-tune models with reinforcement learning, explicitly penalizing policy violations.”

Bozsolik-Torres suggests a simpler control: “Don’t give the agent a create\_pr tool call it’s allowed to make against a repo flagged as banned.” He also says maintainers can route AI-flagged PRs for heavier reviews by default.

Another common strategy is to include an AGENTS.md file in repositories to tell agents how to behave, but some poo-poo this idea, too. [Jeffrey Paul](https://www.linkedin.com/in/jeffpaul/), VP of open source solutions, [Fueled](https://fueled.com/), tells *The New Stack*: “Sadly, these instructions tend to be regurgitated from other human-based files in repos,” he says, “which means that documentation for humans and agents is duplicated and requires maintainers to update things in multiple places.”

Instead, he’s been experimenting with a different approach, using an ~/.agents/AGENTS.md file locally and then copying that content directly into whichever agentic tool he’s using. “This way, I maintain a single local file,” he explains, “and then as I shift tools, I ensure that I update that tool’s specific user-level agent instructions file.”

Paul admits that this approach doesn’t have a 100% success rate but says it does a better job of ensuring the agent looks for and respects repo-specific contribution guidelines.

## Existing SDLC controls should do most of the heavy lifting

When asked for his take on what maintainers can do to enforce contribution rules, McNeil indicates that enforcement doesn’t need to be overly complicated, pointing to code owners as a longstanding way to control merges.

> “At the end of the day, the repository is already protected if you have a proper SDLC in place.”

“That’s a classic control that we’ve used pre-AI for humans, [where] only approved people can merge in code,” he says. “And those are truly deterministic,” he adds. “You can’t break them without an admin login to GitHub.”

In this way, McNeil seems to be advocating for a return to basics to control AI-generated contributions, explaining that linting and CI/CD processes already act as checks to control merges. “The SDLC [software development lifecycle] continues to be the same systems that we’ve already used and trusted for other kinds of non-deterministic contribution from the humankind,” he says. “At the end of the day, the repository is already protected if you have a proper SDLC in place.”

Though the Peking University study’s findings may startle maintainers, they’re also a helpful reminder. If your SDLC is already doing its job, then you don’t need to count on autonomous agents policing themselves.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)