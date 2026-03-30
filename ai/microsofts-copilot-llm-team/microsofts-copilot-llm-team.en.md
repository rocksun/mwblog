Microsoft’s AI strategy has, for the most part, been about using third-party large language models (LLMs). First this was mostly about using OpenAI’s GPT models, but more recently, this also included Anthropic’s Claude — and now Microsoft is using both of them in tandem to improve [Copilot’s Researcher agent](https://learn.microsoft.com/en-us/copilot/microsoft-365/researcher-agent).

The Researcher agent, which Microsoft recommends for problems where deeper reasoning or problem solving across multiple sources is necessary, now includes an optional ‘critique’ feature. With this, GPT will write the draft, which Claude then reviews. As Microsoft notes in its announcement, this review will include checks for “accuracy, completeness, and citation integrity.”

In the future, Microsoft says, it may also give users the option to switch this flow around and have Claude write and GPT check.

## Claude and GPT: Better together?

This workflow may feel a bit hacky at first, but it’s also not all that different from how developers sometimes use one model to write the code and another — from a different model family — to do the code review.

At least in Microsoft’s benchmark, this approach also shows some clear advantages. Using Perplexity’s [deep research DRACO benchmark](https://research.perplexity.ai/articles/evaluating-deep-research-performance-in-the-wild-with-the-draco-benchmark), Anthropic’s Claude Opus 4.6 scores 42.7 by itself and 50.4 within Perplexity’s Deep Research mode. Copliot’s Researcher with Critique turned on scores 57.4, higher than any of the individual models.

![](https://cdn.thenewstack.io/media/2026/03/df1112e3-image002-1024x615.png)

Credit: Microsoft.

Sadly, we don’t have benchmarks for OpenAI’s GPT-5.4 yet, but chances are its score would be in the same range as Opus 4.6’s.

Another new feature for research with Copilot is the so-called ‘council.’ This allows users to compare how different models handle a query side-by-side.

## Cowork is now in the M365 Frontier Program

Recently, Microsoft also [announced](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/) that it would bring Anthropic’s [Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/) tool — essentially Claude Code for knowledge workers who need long-running agents who can complete multi-step workflows — to Copilot.

Imaginatively named Copilot Cowork, this feature is now available in the early-access Microsoft 365 [Frontier program](https://adoption.microsoft.com/en-us/copilot/frontier-program/).

![](https://cdn.thenewstack.io/media/2026/03/f000b995-copilot-cowork-hero-1024x576.webp)

Credit: Microsoft.

Microsoft’s advantage here is that many of its customers would be worried about using Cowork if they had to upload their data to Anthropic. But since these companies already use Microsoft 365 and the Copilot Cowork data stays within their control (Cowork runs in a sandboxed cloud environment), this now enables them to take advantage of these new tools.

“This isn’t about generating content or answers. It’s about taking real action – connecting steps, coordinating tasks, and following through across everyday workflows,” says Barton Warner, SVP of  
Enterprise Technology at Capital Group. “Because Cowork operates on our enterprise data and within our security and risk boundaries, we can experiment, learn, and scale with confidence. That allows us to move faster and focus AI in places where it actually delivers value.”

## Why is Microsoft doing this?

Having to bring in Anthropic to ship features like Cowork and Critique does say something about the position Microsoft finds itself in now: it is diversifying away from its early reliance on OpenAI, but in doing so, it is also deepening its relationship with yet another model provider. For customers paying premium prices for Copilot, one question on their minds is surely whether the value in using Microsoft’s services lies in the models it orchestrates or in the enterprise data and trust layer that makes those models useful in the first place.

Microsoft is clearly betting it’s the latter, while for Anthropic, this partnership is yet another step in its play to become the AI vendor for the enterprise.

When Microsoft first announced Cowork, its president of business applications and agents Charles Lamanna noted that “it is this multi-model advantage that makes Copilot different.” If Microsoft had its own frontier models, it would likely take a different approach, but as things stand, this is the best approach it can take.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)