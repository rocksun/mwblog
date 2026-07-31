**If you’re building traditional software**, you write the product requirements document. If you’re building frontier AI, you run an evaluation. That’s the reality inside Anthropic right now.

[Dianne Penn,](https://www.linkedin.com/in/dianne-na-penn/) the company’s Head of Product for AI Research and Labs, recently explained on [*Lenny’s Podcast*](https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on) that the evaluation suite is effectively killing off the traditional PRD. Moving from deterministic code to probabilistic models means engineering teams have to throw out their old playbooks for defining success and instead focus on hunting down bugs.

## Evals replace the PRD

At Anthropic, the research PM team treats the eval set as their primary artifact. Penn’s team generates 30 to 40 representative examples for every major feature, encoding them as prompts paired with expected outputs that serve as ground truth. Developers must build the [continuous integration pipelines and automated testing infrastructure](https://thenewstack.io/why-cicd-fails-llms/) to run those expected outputs programmatically against new model builds at scale.

The underlying scaling curves are smooth, but what the models can actually do improves in sudden jumps. A capability like reliable math reasoning can seemingly appear overnight. “Unless you have the evals, unless you have the systems to test, these jumps might actually happen, and you don’t know,” Penn said. Without [effective automated evaluations](https://thenewstack.io/your-ci-cd-pipeline-is-not-ready-to-ship-ai-agents/), engineering teams may never realize those new abilities are there—creating what Penn describes as “product overhang.”

> “Unless you have the evals, unless you have the systems to test, these jumps might actually happen, and you don’t know.”

Capturing those abilities also changes how teams QA their products. Instead of tracing code execution, teams often find themselves reading through conversations to understand why a model made a particular decision.

A hallucination, an overconfident assumption, or a failed tool call can all produce similar-looking failures, but each requires a [completely different fix](https://thenewstack.io/debugging-probabilistic-ai-systems/). Penn said another challenge is [sycophancy, where a model reinforces an incorrect premise instead of correcting it](https://thenewstack.io/silent-llm-hallucination-loop/). Left unchecked, that behavior can slip through testing and show up in production.

This also changes what good engineering leadership looks like. Managers need hands-on experience with the models they’re overseeing. If they aren’t using them regularly and seeing firsthand what works and what doesn’t, they risk losing the intuition needed to make the right architectural calls. Penn put it bluntly: “If you’re not building yourself, you’re not gonna make it.”

> “If you’re not building yourself, you’re not gonna make it.”

That way of building products also shaped one of Anthropic’s biggest strategic bets: developer tools. Back in 2023, Anthropic wasn’t associated with coding at all. As Penn recalled, “[Before 2023] nobody said Anthropic and coding in the same sentence.” But the company saw people trying to tackle programming tasks with competing models, and it responded by making coding a major focus for [Claude 3 Opus](https://www.anthropic.com/news/claude-3-family), which launched in March 2024.

Penn noted that the move reflected a deeper shift in Anthropic’s thinking. For models to evolve from conversational bots into genuine assistants, they had to cross the gap from talking to doing, which eventually led to [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) and, later, [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5).

Claude Code had already [gained momentum](https://thenewstack.io/ai-coding-tool-stack/) after its research preview in February 2025 and general availability in May. But when Opus 4.5 arrived that November, adoption accelerated. Penn sees the two launches as deeply connected, asserting that one without the other wouldn’t have had the impact.

## Small teams chase big bets

Penn also shed light on how Anthropic’s R&D is set up to catch those sudden leaps in AI capability. In mid-2024, the company spun up its Labs team specifically to chase down experimental ideas that don’t fit into the normal product roadmap. Their job is to take a basic concept and figure out what the 10x, 100x, or 1,000x version of it looks like. This approach relies on keeping engineering pods extremely small. “Really large teams pursuing very ambiguous, large ideas end up being slowed down,” Penn said.

One early validation of this model came from an unlikely place. Anthropic’s researchers dialed up a particular activation feature and found that Claude became obsessed with the Golden Gate Bridge. Within 24 hours, a cross-functional team shipped a live consumer experience on claude.ai. It reached only about 2,000 people, but Penn called it a turning point: “That was one of those hidden inflection points of finding our identity.”

> “A thinking partner doesn’t just agree with you. It should add to you, and you should come away having better ideas because you worked with Claude.”

## People become more vital

Penn said she regularly uses research versions of Claude to challenge her own product ideas because she’s looking for disagreement, not validation. If the model points out a flaw in her thinking, that’s a sign it’s doing its job. “A thinking partner doesn’t just agree with you,” she said. “It should add to you, and you should come away having better ideas because you worked with Claude.”

The core challenge is shifting from how to write code to deciding what to build in the first place. Penn sees the human role becoming even more vital.

“The role of people who are user-centric, who go into the details of understanding what users are trying to accomplish, bubbling that up in an actionable manner, and doing the relentless work to do that. That to me is the core of a product person,” she said. “And we actually need more of that.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)