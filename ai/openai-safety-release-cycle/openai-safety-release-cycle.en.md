**When David Robinson joined OpenAI in May 2023**, the day after Sam Altman first testified before the Senate, the company’s idea of shipping a new frontier model generally meant training one from scratch.

“We were going to bake a fresh cake with a new pretraining run, do the whole thing from scratch,” Robinson told Ezra Klein on [the latest episode of *The Ezra Klein Show,*](https://podcasts.apple.com/vg/podcast/the-ezra-klein-show/id1548604447) describing a process that took months and limited major releases to a few each year.

> “We were going to bake a fresh cake with a new pretraining run, do the whole thing from scratch,”

Robinson, who led the writing of the safety reports that accompany OpenAI’s frontier models, announced his resignation on Oct. 3 in an essay for [*The Atlantic*,](https://www.theatlantic.com/technology/2026/10/openai-safety-team-resignation/688881/) and OpenAI responded with a statement from CEO Sam Altman posting on X, saying it is [working to keep its models from outpacing its safety measures](https://x.com/sama/status/2089787807611195475?lang=en).

In his first interview since leaving, Robinson described a release cycle in which new capabilities no longer have to wait for a new pretraining run. Reasoning training layered onto existing base models, new tool integrations, and coding agents that accelerate OpenAI’s own research can all change what a system can do between major model releases.

## Reasoning training resets the clock

Back then, a new generation started with another massive pretraining run. Only after that came post-training and safety testing. Robinson recalled that OpenAI even made a point of talking about the “month or months” of safety work that went into GPT-4 after the model itself was finished.

That anchor has loosened because the base model is now only one layer of what ships. “You’ve got the pretraining; that’s the baking of the underlying model,” Robinson explained. “But then, in addition to post-training, you have reasoning training — and those steps are easier to do quickly, so you can redo them.”

That means OpenAI doesn’t necessarily have to start over to get a more capable model. A better reasoning recipe can be layered onto the base model it already has. And the gaps between releases are getting remarkably short; [GPT-6.1 Sol arrived at DevDay just a week after GPT-6 Sol](https://thenewstack.io/openai-gpt-6-1-sol/).

## Tuesday is the new launch day

The second accelerator sits outside training. “It’s not just a chat anymore,” Robinson said of the tools and affordances now wired into models, which can make a system more capable and change how it behaves, without any new training run beneath it. “All of those things are changing what the model can do and what the risks are, and we’re shipping new capability and risk every Tuesday,” he warned.

> “All of those things are changing what the model can do and what the risks are, and we’re shipping new capability and risk every Tuesday,”

The pace also strains the format Robinson spent years writing. System cards made sense when a frontier model arrived every few months, he told Klein, but now “we’re burying people in PDFs or these long reports,” and he argued the ideal would be a live dashboard that tracks a system’s safety properties from predeployment testing through its behavior after release.

## Coding agents accelerate OpenAI research

The third accelerator is AI itself. Robinson described the effect of coding agents inside OpenAI as “night and day,” with research teams now using more than 100 times as much agentic compute as they did at the start of the year.

OpenAI’s [September report on research acceleration](https://openai.com/index/research-acceleration-view-inside-openai/) offers another measure of that shift: by mid-August, the median researcher was using more than $600 worth of inference a day at API prices, while the organization as a whole was running 3.1 eight-hour agent workdays for every human workday.

And some of that work is pretty mundane. OpenAI’s research infrastructure is constantly changing and, in Robinson’s words, can be “pretty janky.” Researchers used to turn to an internal Slack channel when an experiment broke, or a cluster stopped working. Now, they’re asking Codex instead. OpenAI’s own report shows traffic to that channel falling as agent use climbed.

## Frontier fever

Competition gives OpenAI another reason to use that newfound speed. Klein pointed to a much more crowded field than the one the company faced a few years ago, with Anthropic, xAI, Chinese labs and increasingly capable open-weight models all competing for attention and enterprise customers. “All of these things push toward speed,” he said.

Slowing down comes with its own risk. Klein asked whether hitting the “fall-off-the-frontier button” could effectively become a “self-destruct button for the business” if rivals keep moving.

Robinson drew a line, though, between racing for national security and racing for market share. Building a potentially dangerous model because “Americans won’t be safe unless we do” is one argument, he said. Building it because “brand X will ship first” is “not the same kind of reason.”

## Safety testing can’t keep pace

A new model used to be an obvious signal that it was time to run the tests again. That line is getting blurrier as reasoning updates and new tools change what a system can do between major releases. Robinson noted that models can differ in architecture, safety performance, and even the tests used to measure them.

The stakes change once a model can take action. A slightly different summary is one thing; an agent that can call APIs, edit files, or execute code has a lot more room to go wrong. [Boundary issues in OpenAI’s Dots agent doubled in longer tests](https://thenewstack.io/openai-dots-agent-permissions/), while [a cheaper Claude Opus 5.5 broke four things agents depended on](https://thenewstack.io/claude-opus-agent-migration/).

The labs don’t have much time to adjust, either. When Klein asked whether safety testing could keep up with the faster release cycle, Robinson described it simply as asking how much time there is to kick the tires. “And the answer is not a ton,” he said.

That testing has already surfaced problems. OpenAI [shelved GPT-6.1 Astra the day before DevDay](https://memeburn.com/openai-devday-2026-recap/) after internal testing reportedly found [higher levels of deception and a tendency to continue tasks without user permission](https://dataconomy.com/2026/09/30/openai-launches-gpt-6-1-sol-at-devday/). Robinson also described models writing in their chains of thought that they wondered whether they were being evaluated. If a model knows it’s being tested, he said, “the tests we gave it early on before we deployed don’t actually tell us what it’s going to do out there in the world.”

> “the tests we gave it early on before we deployed don’t actually tell us what it’s going to do out there in the world.”

## Brakes, with boundaries

Robinson took care not to cast OpenAI as a train without brakes. “There are brakes. Things have been stopped,” he said, pointing to the pulled 6.1 launch and to training runs halted after researchers reviewed the results.

He went on to describe OpenAI’s public accounts of its pauses as accurate but “very carefully scoped.” And he pushed back on the industry phrase “pace the frontier.” Slowing down isn’t enough if the underlying safety bar hasn’t been met. “Running off a cliff and walking slowly off a cliff are just not that different,” he said.

His criticism wasn’t aimed at the people doing the safety work. Robinson described his former colleagues as deeply committed to getting it right. His concern is whether the systems around them can keep up with what they’re building.

## Lessons from the Challenger launch

Robinson returned to the release cycle near the end of the interview while recommending *[The Challenger Launch Decision,](https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html)* social scientist Diane Vaughan’s book on the shuttle disaster, in which the O-ring risk was documented and accepted launch after launch, and calling one flight unsafe would have reopened questions about every flight before it.

He worries AI is sliding into the same pattern as it moves from “a whole new world every few months” to “a little bit different every week,” warning that the industry could end up “going by shades into a level of risk that does not make sense.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)