Anthropic is reportedly developing a model that can infer what users want from incomplete instructions. According to [The Information](https://www.theinformation.com/newsletters/ai-agenda/anthropic-readies-model-reads-users-intentions-better), a person who tested the unreleased model described stronger reasoning and intuition than the company’s current lineup.

In the report’s example, a developer asks for a bug fix, and the model identifies a broader class of related problems and asks whether to address them too. Anthropic hasn’t confirmed a release date or model family and what still remains unclear is whether the model can distinguish between an incomplete request and work a developer deliberately left out.

> What still remains unclear is whether the model can distinguish between an incomplete request and work a developer deliberately left out.

That gap between permission and intent has already caused problems. Amazon’s internal coding agent Kiro reportedly took an unexpected approach to fixing a routine bug in AWS Cost Explorer. Rather than making a targeted change, it decided to delete and recreate the environment. The agent had inherited an engineer’s elevated access, allowing it to bypass a two-person approval process. The [incident](https://thenewstack.io/ai-agents-no-laws/) shows how far an agent can take a task when its access exceeds the limits of the original assignment.

## Overeager agents by the numbers

In [Overeager Coding Agents](https://arxiv.org/abs/2605.18583), researchers examined about 7,500 runs across four coding-agent products and six models, and one finding stood out in particular. The researchers found that removing a sentence requiring user consent pushed Claude Code’s rate of out-of-scope actions from 0% to 17.1% in paired tests.

> The researchers found that removing a sentence requiring user consent pushed Claude Code’s rate of out-of-scope actions from 0% to 17.1% in paired tests.

The framework was also part of what made a significant difference. Claude Code, Codex CLI, and Gemini CLI recorded overeager-action rates ranging from 5.4% to 27.7%, compared with 0.2% to 4.5% for OpenHands, which uses an ask-to-continue approach. Even within the same framework, changing the underlying model produced differences of up to 15.9 percentage points.

A separate study, [Coding Agents Are Guessing](https://arxiv.org/abs/2607.02294), tested Claude Code, Codex, and OpenCode against 2,208 underspecified DevOps prompts covering 69 task families. Between 55.8% and 67.8% of runs violated at least one boundary.

The researchers distinguished between agents acting on the wrong target and agents going beyond the permitted scope. Both are problems, but they aren’t interchangeable since an agent can perform exactly the requested operation and still cause trouble by choosing the wrong resource.

## When the target is unclear

In these tests, unclear targets were among the biggest problems. Warnings about the potential impact of an action did little to reduce how often agents proceeded anyway.

Neither study tested Anthropic’s rumored model. Both, however, raise questions about whether improvements in reasoning will also improve an agent’s judgment when instructions leave room for interpretation.

## Keeping agents within bounds

Anthropic has encountered a related problem in its own testing. In an [October 9 report on unintended model actions](https://www.anthropic.com/news/investigating-unintended-model-actions), the company described cases where Claude kept looking for ways to finish an assignment after encountering a restriction.

Most of the cases involved what Anthropic called persistence, where Claude worked around an obstacle rather than stopping.

In one evaluation, Claude Haiku 4.5 was told to complete a form but stop before submitting it. The model submitted it anyway, apparently expecting another confirmation page. In another, an unreleased research model submitted a real government form after the practice version failed to load or was accidentally closed.

While these were not coding tasks, and the company has said the incidents had minimal real-world impact, they still show how an agent can mistake a restriction for a problem it needs to work around.

Anthropic has acknowledged that clearer instructions might have prevented some of the failures. The company also said it had developed monitoring tools that blocked every documented case when tested against them.

But clearer instructions only solve part of the problem. Users want agents that can work through ambiguity without stopping to ask for help at every turn.

## What the code cannot reveal

Anthropic will need to show that its model can distinguish between an incomplete request and an intentional constraint. A developer might limit a fix because of an upcoming migration, a compatibility requirement, or a production freeze. None of those reasons would necessarily be visible in the repository.

> Anthropic will need to show that its model can distinguish between an incomplete request and an intentional constraint.

*Anthropic had not responded to a request for comment at publication.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)