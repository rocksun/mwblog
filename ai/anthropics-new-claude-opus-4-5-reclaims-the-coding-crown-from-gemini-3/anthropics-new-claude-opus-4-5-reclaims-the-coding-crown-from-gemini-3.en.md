Anthropic today launched the latest version of its flagship Opus model: Opus 4.5.

The company calls it its most intelligent model yet and notes that it is especially strong in solving coding tasks, taking the crown from OpenAI’s [GPT-5.1-Codex-Max](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) and Google’s week-old [Gemini 3](https://thenewstack.io/google-launches-gemini-3-pro/) model with an SWE-Bench Verified accuracy score of 80.9%.

The company is also making Opus 4.5 significantly more affordable to use, with API pricing of $5 per million input tokens and $25 per million output tokens, down from $15/$75 per million input/output tokens.

Users on Anthropic’s subscription plans will also now see a bit more headroom to use Opus 4.5.

## Benchmarks

With the launches of OpenAI’s GPT-5.1 and 5.1-Codex-Max, Google’s [Gemini 3](https://thenewstack.io/google-launches-gemini-3-pro/) (and its hit Nano Banana Pro image model), it’s been a very active November for the large model builders. Gemini 3, especially, received a very positive reception.

Unlike Google, Anthropic has never focused on image manipulation or video creation, but has stuck squarely to its strength in coding and productivity use cases. This latest Opus is no different and Anthropic stresses that the model can now produce documents, spreadsheets and presentations “with consistency, professional polish, and domain awareness.”

But as usual, it’s coding where the Claude models shine. That’s reflected on the benchmarks, where Opus 4.5 bests the competition across the board, but benchmarks don’t always reflect real-world use cases, of course.

[![](https://cdn.thenewstack.io/media/2025/11/b1f343c5-claude-opus-4-5-swe-bench.png)](https://cdn.thenewstack.io/media/2025/11/b1f343c5-claude-opus-4-5-swe-bench.png)

Credit: Anthropic.

For this release, Anthropic also gave Opus 4.5 the same test it gives prospective performance engineering candidates who want to work at the company. This test, which solely focuses on technical ability, has a two-hour time limit and Opus 4.5 scored higher than any of Anthropic’s job candidates ever did.

As Alex Albert, the head of developer relations at Anthropic, also told me, he’s gotten the sense that the “model just gets it.” He noted that past models have often been very good at gathering data across different channels (like Slack and email), but have had a hard time synthesizing all of this information effectively.

“I’m finding that with this model, that is no longer the case,” he told me. “I can actually trust it to go straight from those Slack messages to a good output, and then I’m like, wow, it could have really just sent this. I still am reviewing it and things, but I really could have just been hands-off here.”

## Low, Medium, High Effort

One new feature of Opus 4.5 is that it features an “effort” parameter (low, medium, high), similar to some of its competitors’ models, which allows developers to control how much time (and how many tokens) the model will use to solve a given problem. Set to medium, the model is on par with Sonnet 4.5 on the SWE-bench Verified benchmark but uses 76% fewer tokens, and even at the high setting, where it beats Sonnet 4.5, it uses only about half the tokens of the Sonnet model.

That’s a trend we’ve been seeing and this efficiency is something OpenAI also stressed when it launched its latest [Codex-Max](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) model last week.

Overall, the model also improved upon the rest of the Opus family (and Opus 4.1) in other areas, including visual reasoning and math.

[![](https://cdn.thenewstack.io/media/2025/11/2ea75080-claude-opus-4-5-evals.png)](https://cdn.thenewstack.io/media/2025/11/2ea75080-claude-opus-4-5-evals.png)

Credit: Anthropic.

## Opus 4.5 for Computer Use

Opus 4.5 is also Anthropic’s best model for computer use cases yet, the company says. To put this to the test, Anthropic is now opening up its Chrome extension to all Claude Max subscribers (who pay $100/month+).

Computer and browser use still feels like it’s in its infancy and often feels rather slow and error-prone, but Anthropic is pushing the state of the art up a level here, with scores well above those of its previous models.

Anthropic had been in an interesting position lately, where the latest version of its mid-tier Sonnet model often outperformed the older Opus 4.1 model, giving users very few reasons to use the more expensive model in their day-to-day work. The idea, however, was always to have a three-tier model and Opus 4.5 restores the balance here.

“What’s interesting about this release, to me at least, is that it is not necessarily like: ‘Oh, everybody needs to now shift to Opus,’ but it does enable this new tier of possibilities,” Albert said. “Now we’re entering this landscape where you actually do have three models from us that all fit different needs along this curve: you have the Haiku model that we just released a month ago. You have Sonnet 4.5, which was a month and a half ago. And now this completes the fold.”

## Claude Developer Platform Updates

In addition to the new model, Anthropic is also announcing two updates to the Claude Developer Platform that go hand-in-hand with the Opus 4.5 release: An upgraded plan mode for Claude Code and Claude Code support in the desktop app.

The new plan mode now creates more precise plans for how to solve a problem or add a new feature and sticks to them more directly, Anthropic says.

And if you use the Claude [desktop app](https://www.claude.com/download), you can now start coding tasks in Claude Code on your desktop or in the cloud environment. This now lets you run multiple local and remote Claude Code sessions in parallel.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)