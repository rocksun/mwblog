**Anthropic [launched Claude Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/) on Tuesday** with a statistical signature embedded in its generated text, but developers shouldn’t expect that signature to appear equally strongly across everything the model produces.

Code is one place where the limits of [Anthropic’s watermarking system](https://thenewstack.io/anthropic-claude-text-watermark/) become obvious. Instead of adding metadata or hidden characters, the system changes the randomness Claude uses to choose between possible next tokens, which Anthropic says doesn’t affect the quality or content of its output.

Over a sufficiently long response, those token choices create a statistical pattern that can provide evidence that Claude was likely involved in writing or processing the text. That works better with natural language, where the model often has several ways to say the same thing, than with code, where choosing a different variable, operator, or function could change how a program behaves or break it entirely. Anthropic therefore doesn’t apply the watermark when a particular token is required for accuracy.

Developers will also have to adjust to a change in how Claude handles preserved thinking. With Fable 5.1, Anthropic is limiting when new API accounts can carry those thinking blocks into a modified conversation, a practice the company says has also been used to [distill its models at scale](https://thenewstack.io/glm-5-3-anthropic-distillation/).

> Over a sufficiently long response, those token choices create a statistical pattern that can provide evidence that Claude was likely involved in writing or processing the text.

## How the watermark works

Anthropic detailed its plan to meet those requirements on August 14, after signing the EU Code of Practice on Transparency of AI-Generated Content as one of roughly 190 other signatories. The company is applying the watermark worldwide because it says there isn’t a reliable way to limit it by region and plans to add it to older Claude models over the coming months.

The technology is based on Google DeepMind’s SynthID-Text. It doesn’t change the probabilities Claude assigns to the next token; instead, it changes the randomness involved in choosing among possible options. Over a long enough response, those choices leave behind a statistical pattern that can later be detected with the right key.

> Since the watermark is part of the text itself rather than attached as metadata, simply copying a response somewhere else won’t remove it.

Since the watermark is part of the text itself rather than attached as metadata, simply copying a response somewhere else won’t remove it. Anthropic says it can even survive some editing, although rewriting enough of the text will eventually erase the signal.

## Code’s low-entropy problem

Code is where the limits of watermarking become more obvious. If choosing a different token could make an answer incorrect or break the code, Anthropic doesn’t apply the watermark. The watermark can still appear in less-constrained parts of the output, such as comments, while short responses may not contain enough signal to be reliably detected.

Anthropic is beginning to make that detection available through an API in private preview. For now, access is limited to eligible groups, including regulators, law enforcement, media organizations, fact-checkers, and researchers, as well as enterprises that need it for their own AI Act compliance. Anthropic says it plans to make the API more widely available later.

## Thinking blocks and distillation

Another change in Fable 5.1 is aimed at model distillation. Claude’s Messages API can return encrypted thinking blocks that developers pass back in later turns, allowing the model to continue its reasoning across a conversation.

The problem, according to Anthropic, is that changing earlier parts of the conversation while keeping those blocks can cause Claude to decrypt and print its reasoning. That reasoning could then be used to train another model.

With Fable 5.1, Anthropic is closing that route by tying preserved thinking to the context that produced it. The restriction applies to new accounts created on or after Aug. 31 across Claude Platform, Amazon Bedrock, Google Cloud Vertex AI and Microsoft Azure Foundry.

Existing accounts can continue using Fable 5.1 without the restriction for now, but Anthropic says it will apply to everyone with future model releases.

## Agent harnesses face tradeoffs

The restriction creates a less obvious problem for developers building their own agent harnesses. Agent systems don’t necessarily keep their context static between every model call. A harness might remove old exchanges, summarize earlier history or reorganize a conversation as an agent works through a task. Those are normal [context-management techniques](https://thenewstack.io/claude-code-token-reduction/), but they also change the context associated with a thinking block.

Anthropic says developers should leave thinking blocks unchanged and keep the prior system prompt, tool definitions, and messages byte-for-byte unchanged. Applications that modify that context will need to change how they manage Claude’s reasoning state instead of carrying the same thinking blocks forward.

Only a small number of customers with custom integrations are expected to be affected, and existing Fable 5.1 API customers are getting time to make changes before the restriction becomes standard in future models.

The two changes address different problems, but both add protections without completely [limiting the flexibility](https://thenewstack.io/shopify-claude-code-agentsmd/) developers have when building with Claude.

> The two changes address different problems, but both add protections without completely limiting the flexibility developers have when building with Claude.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)