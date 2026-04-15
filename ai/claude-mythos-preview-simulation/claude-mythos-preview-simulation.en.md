The UK-based AI Security Institute (ASI) this week [released](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) the results of its evaluation of Anthropic’s new Claude Mythos Preview, and the model, released just last week, is unlike anything that’s come before.

The evaluation, intended to benchmark the model’s cybersecurity capabilities, reveals that Claude Mythos Preview has shown marked improvement in capture-the-flag (CTF) and multi-step cyberattack simulations.

> Claude Mythos Preview has shown marked improvement in capture-the-flag (CTF) and multi-step cyberattack simulations.

> Claude Mythos Preview, in the hands of bad actors, could be used to carry out autonomous multi-stage attacks on vulnerable systems.

While the results can’t concretely say how the model would perform in real-world environments, they offer a warning: Claude Mythos Preview could be used to carry out autonomous multi-stage attacks on vulnerable systems.

## Claude Mythos Preview: Too hot to handle?

While Anthropic [launched](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) Claude Mythos Preview on April 7, the AI giant didn’t hand over access to just anyone. Only big-name players (i.e., Amazon, Apple, Broadcom, Cisco, CrowdStrike, the Linux Foundation, Microsoft, and Palo Alto Networks, along with about 40 other organizations) were given seats at the table via Project Glasswing, a new initiative Anthropic [describes](https://www.anthropic.com/glasswing) as “an effort to secure the world’s most critical software.”

Why did these teams get special access?

It seems Anthropic considers Claude Mythos Preview too powerful for public release, at least right now.

In a [run of bad luck for Anthropic](https://thenewstack.io/anthropic-claude-code-leak/) last week, an unsecured, publicly accessible data storage was leaked, revealing that the AI company was working on a new model called Mythos — “the most capable [model] we’ve built to date,” an Anthropic spokesperson told [*Fortune*](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform).

Now, the evaluation by ASI — a body run by the UK government’s Department for Science, Innovation and Technology — seems to give credence to that claim, stating in its announcement blog post that “our results show that Mythos Preview represents a step up over previous frontier models.”

## The first AI model to autonomously execute a 32-step corporate network takeover

ASI conducted a series of controlled evaluations, giving Claude Mythos Preview explicit directions and access to discover and exploit vulnerabilities, enabling it to execute multi-stage attacks on vulnerable networks.

Carrying out these kinds of attacks requires chaining together dozens of hosts and network segments. It’s an arduous process that can take human hands anywhere from hours to weeks to accomplish — and one bad actor would likely tap Claude Mythos Preview to tackle if and when they get their hands on the model.

To measure its ability to do so, the evaluation included “The Last Ones” (TLO), a 32-step corporate network simulation covering reconnaissance through full network takeover, which takes about 20 hours of human bruntwork, ASI estimates.

Claude Mythos Preview got the job done — and is the first model to do so.

It succeeded in solving the TLO from start to finish in three out of its 10 attempts. Across all 10 attempts, the model completed, on average, 22 out of all 32 steps.

Claude Mythos Preview’s performance is leaps and bounds ahead of the previous reigning champion, Claude Opus 4.6, the next best-performing model, which only completed 16 out of the 32 steps, on average.

## It completed expert-level tasks 73% of the time

The TLO simulation wasn’t the only test ASI put Anthropic’s model through.

Claude Mythos Preview also included CTF challenges, in which the model must identify and exploit system weaknesses to retrieve hidden “flags.”

Again, the new model outranked existing models. Particularly noteworthy is its performance on expert-level tasks: Claude Mythos Preview succeeded 73% of the time.

No other model could even complete these tasks before April 2025.

## What the results do — and don’t — mean

While ASI’s evaluation certainly reveals stunning results about Claude Mythos Preview’s cybersecurity capabilities, it doesn’t paint a crystal-clear picture of what could happen in the real world.

Yes, the results show the model is capable of autonomously attacking systems — but ASI points out that there are differences between its evaluation and real-world environments.

> “We cannot say for sure whether Mythos Preview would be able to attack well-defended systems.”

For one, ASI clarifies that its results mean Claude Mythos Preview can autonomously attack “small, weakly defended and vulnerable enterprise systems where access to a network has been gained.”

The body notes that real-world systems likely have security features in place, like active defenders or defensive tooling. Plus, in the real world, the model would likely trigger certain security alerts, another factor not accounted for in ASI’s tests.

And Claude Mythos Preview didn’t ace everything. The model was stumped by IT sections in the operational technology-focused cyber range, “Cooling Tower.”

There’s no ignoring that what Claude Mythos Preview did accomplish in ASI’s evaluation is unprecedented — and its capabilities will surely only evolve as other models also advance.

But even as its evaluation underscores the [growing cybersecurity threats AI models pose](https://thenewstack.io/ai-is-changing-cybersecurity-fast-and-most-analysts-arent-ready/), ASI also issues a disclaimer: “We cannot say for sure whether Mythos Preview would be able to attack well-defended systems.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)