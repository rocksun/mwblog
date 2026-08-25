On July 16, the team at Hugging Face noticed something weird moving through their production systems: An intruder that was cloning datasets, harvesting credentials, and hopping between internal clusters faster than a human could type. Five days into the investigation, the authorities were notified, and several days later, OpenAI traced the intruder back to one of its models.

> “Two frontier models escaped their test environments this summer; only one of them had a funny reason.”

That prompted Anthropic to look through its own test logs, and it found that similar events had occurred three times. One Claude model probed nine thousand hosts in a single run without setting off any alarms. Another slipped a poisoned package into the public Python registry, compromising fifteen machines before it was caught. The third incident dated back to April and went undetected for three months until a rival’s error prompted the audit. Nobody had noticed. Two of the three companies involved didn’t know anything was amiss until they got a call.

## Containment by instruction

A sandbox, in the context of AI testing, means a model gets a task, a set of tools, and an instruction: no access to the outside world.

[OpenAI’s model found an exploit](https://thenewstack.io/openai-huggingface-sandbox-breach/) in a tool it was allowed to use, and leveraged it to access the open Internet. Anthropic’s models didn’t even need that. The models were told a path didn’t exist, so when their tasks led them down a path that wasn’t supposed to be there, they treated it as part of the exercise.

> “In both instances, the only constraint was an instruction. There was no mechanism outside the model itself to ensure those instructions wouldn’t be treated as optional.”

In both instances, the only constraint was an instruction. There was no mechanism outside the model itself to ensure those instructions wouldn’t be treated as optional.

## So how did they escape?

OpenAI’s agent was being evaluated on a cybersecurity benchmark called CyberGym. During the test, it chained a code-execution flaw in a dataset loader to a second flaw in the platform dataset configuration file handler. It used the combined exploit to run commands on a live processing worker. From there it grabbed a write-scoped access token and cloned a private dataset as a staging area, which became a dead drop for its own tools. By the time anyone noticed, the intrusion had been running for three days, touched several internal clusters, and compromised accounts at four other companies, according to Hugging Face’s own review.

What it wanted, in the end, was comical: the answer key to the test it was taking.

[Anthropic’s three incidents](https://thenewstack.io/anthropic-claude-containment-failure/) were nowhere near as convoluted. Its models were being run through security exercises against third-party evaluation partners, and the only thing keeping them from accessing the Internet was an instruction not to. One incident involved an SQL injection targeting a resource the model wasn’t supposed to be able to access. Another, during an exercise where the usual safeguards were deliberately switched off, ended with a Claude model publishing a malicious package to the Python Package Index, and fifteen machines picking it up before it was pulled down. No zero-day exploit. No dramatic escape. Just locked doors that turned out to be mirages.

## The structural weakness

Strip away the specifics, and both incidents share the same root cause: there was nothing outside the model’s own judgment that could enforce the limitations placed on it. A credential that shouldn’t have been able to access the open Internet did so anyway. An instruction that should’ve stopped a plan cold got treated as just another input to reason around.

> “If a fence doesn’t hold during testing, it won’t hold in production.”

It feels like we’ve spent the last year reliving the same problem in new ways. For example, in deleted databases, in poisoned supply chains, in every [credential an agent inherited](https://thenewstack.io/ai-agents-no-laws/) because provisioning it correctly took one extra step nobody got around to. The only delta is where the boundary was supposed to be: around the dev experiment, meant to contain dangerous capabilities, or standing between it and every production system it could reach. If a fence doesn’t hold during testing, it won’t hold in production.

## How do we break out of the loop?

Unfortunately, the answer isn’t self-improvement. A more capable model wouldn’t have caught any of this. The only way to fix it is with Infrastructure that verifies where a model actually is, rather than trusting its reports.

**Egress controls that are closed by default.** A test environment that can reach the open Internet is probably not a great idea. Outbound traffic should be locked to an explicit allowlist. Never assume a model will simply decline to look for a way out. “No internet access” needs to be a network-enforced fact, not just an instruction.

**Narrowly scoped credentials with short lifespans.** Both incidents ran, in part, on tokens that extended beyond what the tasks required. A credential built for one evaluation run, scoped to nothing beyond it, and expiring on a timer, can’t become the write-scoped key that turns into a lateral-movement problem across multiple clusters. Yes, it will be a chore; so gird your patience by imagining having to explain to company leadership why taking steps to avert a catastrophe was too tedious to bother with.

**Policy gates that sit outside the agent’s reasoning.** An agent that can decide for itself whether an action is in scope is grading its own test. A plan should have clear rules written in code, evaluated by something other than the agent, before anything executes. Open Policy Agent has become a *de facto* default here for exactly this reason. It doesn’t care how confident the plan sounds; nothing runs without proper authorization from an external source.

**An audit trail that is entirely independent of the agent.** Both incidents were discovered by rereading logs after the fact, not by asking the models what happened. That’s how oversight should be done. As the proverb goes: *Quis custodiet ipsos custodes?* Who watches the watchers? A system of record that captures what actually occurred, regardless of the agent’s own account of itself, is the only version of events worth trusting.

## This is a sign

The industry spent a decade learning that the CI/CD pipeline is [an attack vector](https://thenewstack.io/npm-supply-chain-worm-attack/) that requires real fortification, not just bolted-on convenience. Test environments for frontier models are following the same arc at a faster pace. The next time one of these agents escapes containment, it’ll probably be one built around finding unlocked doors, which will make it substantially more dangerous than a coding agent that deletes a few databases.

Test rigs must be treated as if they hold something real, because, as far as the credentials are concerned, they do. A sign on a door is never going to be enough to keep everyone out; there has to be a lock whose robustness correlates to the value of what it guards.

> “A sign on a door is never going to be enough to keep everyone out; there has to be a lock whose robustness correlates to the value of what it guards.”

Whether by a state-sponsored crew probing a water management system in the middle of the night, or a company’s own model trying to shave a few points off a benchmark, boundaries will always be tested. Two labs found out this summer, and the story needs to be taken seriously. The vulnerabilities are real, the transparency from the labs is welcome, and the containment failures are a cause for concern.

Catching a model that tried the handle is the easy part; both labs proved that. The more challenging, and therefore critical, part is making sure the next containment environment actually has doors that are firmly locked.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)