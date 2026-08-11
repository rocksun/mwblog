**Doist CTO Gonçalo Silva doesn’t pretend** to know where AI is headed. The pace of change has made it harder to commit to one roadmap, model provider, or way of working.

“I can make predictions, but I feel like I can make 10 of those and they are all very different from each other, and they almost all have a similar probability of being right,” [Silva](https://www.linkedin.com/in/goncalossilva?originalSubdomain=pt) tells *The New Stack*. “So I’m operating in a space with more unknowns than ever.”

Rather than trying to predict which direction will win, [Doist](https://doist.com) — the company behind products like [Todoist](https://www.todoist.com) and [Twist](https://twist.com/home) — established three broad principles more than a year ago, Silva says: The first is that AI features should be purposeful; the second is that they should be private and secure, and the third is that they should be built to improve as models change.

> Doist has learned that just because a feature is now easy to build with AI, that doesn’t mean it’s worth shipping.

Through its early experiments, the Doist team also learned that just because a feature is now easy to build doesn’t mean it’s worth shipping.

Doist is currently testing Automations, a new service that is meant to take Doist from a company that focuses on helping users remember tasks to one that helps them execute them as well.

Automations uses AI to turn a user’s natural-language request into a manifest. Then, when a trigger fires or a scheduled job begins, ordinary code — not a large language model — executes those steps. Doist plans to launch Automations out of its closed beta in August or early September, Silva says.

“When you create an automation that you expect to run every time and to be consistent and predictable, you already have a problem because AI is not predictable and consistent by design,” Silva says.

## AI writes the workflow, but code runs it

As it turns out, models are great for interpreting what a user wants, Silva argues, but they become a problem once the same automation must run reliably for the 10th or 100th time.

“So we had this idea. What if we leverage the AI’s capabilities to generate a manifest, an automation that then we execute on some trigger-based or recurring basis?” Silva says. “So we do have AI in the generation phase where you need to figure out what the user is requesting and what that means in terms of execution, what should it actually do? But then the automation itself is predictable.”

A major advantage of keeping AI models out of the execution path whenever possible is that it is also far cheaper and faster to run code on a CPU than invoking an expensive model every time an automation runs. As a result, the model doesn’t have to reinvent the process every time it runs.

The idea here is that the user simply describes the intent and gets an automation back. “That’s it,” Silva says. “No configuration model, no tool call limits, no temperature settings, none of that.”

## “Subtraction over addition”

The automation system is part of a broader product philosophy Silva calls “subtraction over addition.” AI makes it easier to build and ship features, but that also makes it easier to fill a mature product with ideas that haven’t earned their place.

Todoist offered a recent example when it [retired its Goals beta on July 13](https://www.todoist.com/help/articles/goals-beta-retiring-on-july-13-VKe2PuGn5). Silva says the team had invested heavily in the feature, but usage data and the overall experience didn’t meet its standards.

The company took a similar, but less dramatic path, to launch [Ramble](https://www.todoist.com/help/articles/turn-your-scattered-thoughts-into-clear-tasks-ramble-jan-21-HhmP8ue8R), Todoist’s voice-based feature for turning a spoken brain dump into structured tasks. Before Ramble, Silva says, a small team prototyped at least 18 AI ideas, including project summarization, and discarded all of them virtually. Part of the problem, Silva argues, was that the company simply wasn’t ready to bring AI into production yet.

“What we knew at the time was that we were not primed to build with AI,” Silva says. “AI was a new building block. This was about a year ago, a little more actually. And we knew this was very powerful, but we did not have enough experience using it in real projects.”

For a product that [dates back to 2007 and serves millions of users](https://doist.com/), experiments also carry a cost beyond the engineering time. When the team removed Goals, for example, it prompted a bit of community backlash, even though the feature had only been an experiment.

“So if we just keep adding things, it’s not going to be very good for anybody very soon,” Silva says. “So we need to stay focused.”

![](https://cdn.thenewstack.io/media/2026/08/5d4b512a-todoist-1024x576.png)

*Credit: Todoist*

## Models change, but the quality bar shouldn’t

Doist is trying to preserve the same flexibility under the hood. The company doesn’t want its AI features tied to a single model provider, so it uses tests and evaluations to check whether a model change alters their behavior. Ramble’s test suite spans about 18 languages and dozens of scenarios for each, Silva says.

Those evaluations also give Doist a way to control inference costs. The team can first make a feature work with a large, expensive model, and then test smaller (and cheaper) models and adjust the implementation until it meets the same quality bar. That became important when an early beta of Automations with only a few hundred users produced a massive initial bill, Silva says.

Giving more people access to AI tools hasn’t erased the difference between producing something and judging whether it is good. Doist initially embraced the idea that product managers, designers, and engineers could move freely into one another’s work, Silva says, but this didn’t work out as expected.

“We rode that wave, but I feel like we eventually really understood a basic principle of great work, which is you do need the expertise, and you do need the taste,” Silva says. “It’s great that we have this tool that enables so much autonomy and independence. But we also need to realize that at the end of the day, the expert is the expert.

A product manager — just picking a random example — will not be able to tell the difference between a pull request with code that works and is maintainable long term, versus another pull request that also works but is much more questionable in the way it’s built. An engineer will.”

It feels like this is the common thread across Doist’s overall AI strategy. The team uses models to lower the barrier to creating a workflow or exploring an idea, but that newfound speed shouldn’t lower the bar for what eventually ships to users.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)