[Sentry](https://sentry.io/welcome/), the application monitoring and error tracking service, on Tuesday launched Seer Agent, a natural-language debugging tool that lets developers investigate production problems by querying across a company’s full observability stack.

The tool, available in open beta for all Sentry customers with Seer enabled, fills a gap that became clear as the company watched how developers actually used its platform.

Indragie Karunaratne, Sentry’s senior director of engineering and the head of the company’s AI efforts, tells The New Stack that users kept running into problems that Sentry’s existing AI tools weren’t built for. Sentry had the data to investigate them, but the problems weren’t the traditional bugs most developers would typically associate with a platform like Sentry.

![](https://cdn.thenewstack.io/media/2026/04/5025e36e-seer-agent_video.gif)

Sentry’s Seer Agent. Credit: Sentry.

“What we noticed over the course of watching people use Autofix — and use Sentry as a product in general — was people wanted something that was more open-ended, because there are types of issues that Sentry might not be aware of yet — a customer reports something via a feedback channel, or you see some metric on a dashboard that’s going wrong,” Karunaratne says. “None of those are exactly issues in the Sentry sense; they haven’t been identified as an issue in any way.”

Sentry says the Seer Agent requires no additional setup and is available from any page in the Sentry dashboard. It provides context for whatever the developer is currently looking at and can query all the telemetry Sentry has collected about an application.

## From Autofix to open-ended investigation

Seer Agent is the second major product under Sentry’s [Seer](https://sentry.io/product/seer/) umbrella. The first, [Autofix, launched in March 2024](https://thenewstack.io/sentry-founder-ai-patch-generation-is-awful-right-now/) as a human-in-the-loop debugging tool. At the time, Sentry compared it to a junior engineer who could take a known issue, perform root cause analysis, and generate a code fix, but it needed human guidance along the way.

But to get started, Autofix needs an issue that Sentry has already detected. Seer Agent is different in that developers can simply describe a symptom (maybe a slow page or a customer complaint), and the agent gets to work investigating the problem.

Karunaratne notes that Agent and Autofix are “just two workflows built on the same foundation, same data, same agent architecture. Autofix is just more scoped to one particular, well-defined problem that Sentry has found, whereas [Seer Agent], you can make it go as broad or as narrow as you want.”

![](https://cdn.thenewstack.io/media/2026/04/b95d2dca-original_seer-agent-result-783x1024.png)

Sentry has been running Seer Agent internally for several months, and Karunaratne says it has changed how the team handles incidents. “Whenever Sentry goes down, or there’s some serious alert, engineers start digging in with Seer Agent, and they’re able to usually root-cause an incident within a few minutes compared to what it would usually take for a human to work through the problem and find the data and everything,” he says.

> “Whenever Sentry goes down, or there’s some serious alert, engineers start digging in with Seer Agent, and they’re able to usually root-cause an incident within a few minutes compared to what it would usually take for a human to work through the problem and find the data and everything.”

In one recent case, the Sentry team writes in its announcement that Seer itself started failing. Karunaratne used Seer Agent to investigate while waiting for on-call engineers to come online. The agent identified that calls to a specific model were failing in specific regions due to an [upstream infrastructure issue](https://blog.sentry.io/seer-fixes-seer-debugging-agent/) on the provider’s side. Diagnosing this issue would have normally required quite a bit of sleuthing.

## Traversing the telemetry graph

Sentry notes that Seer Agent doesn’t search telemetry the way a generic LLM with a search tool would. Sentry’s telemetry is already ‘trace-connected,’ as the company calls it. The system knows the trace where the error occurred, and the agent can then use that to look into the logs and other related data.

“It isn’t guessing at time ranges and hoping the right rows show up in a text search; it’s traversing a graph that was built at ingest,” Sentry writes in its announcement.

> “It isn’t guessing at time ranges and hoping the right rows show up in a text search; it’s traversing a graph that was built at ingest.”

For the agent to do its job well, it needs access to all of this data, but [context management](https://blog.sentry.io/want-ai-to-be-better-at-debugging-its-all-about-context/) is key here, Karunaratne explains.

“If you overdo it, if you pull all the context in, the agent performs poorly. If you pull in too little context, it also performs poorly in a different way,” Karunaratne says. “The right balance of pulling in only the useful things and narrowing down on what that grouping of data looks like is a very common problem.”

## The case for a dedicated debugging agent

Given how good coding agents have become, are dedicated debugging tools even necessary? Karunaratne acknowledges that developers (and those paying for their tools) may ask themselves this question.

“For simple debugging, you could take a stack trace from Sentry and paste it to a coding agent and have it debug it,” he says. “But we find that most problems in production have very complicated failure modes — problems that occur across multiple repositories, complex distributed systems with a lot of different components, the telemetry is very complicated — so you need some knowledge of how to steer the agent to leverage that telemetry correctly. And all of that is baked into Seer.”

So rather than compete with coding agents, Sentry is integrating with them. The company has already built integrations for Cursor and Claude Code, so developers can hand off Seer’s root cause analysis to a coding agent in their own environment. Sentry plans to expand those integrations to GitHub and other developer tools.

The longer-term direction is toward proactiveness. Karunaratne says the team wants Seer to “behave like an engineer that is always on, 24/7, triaging things for you, looking at a symptom, and then deciding to dig into it further. Ideally, this just works in the background, and finds issues, alerts you to problems, fixes problems — and that’s through a combination of the agent and the Autofix workflows.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)