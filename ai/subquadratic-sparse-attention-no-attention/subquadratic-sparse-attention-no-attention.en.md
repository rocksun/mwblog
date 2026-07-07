When Subquadratic [launched earlier this year](https://thenewstack.io/subquadratic-12-million-context-window/), it could build a sparse-attention model that could handle a 12-million token context window and be significantly faster than today’s [large language models](https://thenewstack.io/introduction-to-llms/). But it didn’t launch the model widely and it didn’t publish benchmarks.

Given the company’s large claims, that created quite a bit of skepticism. In June, Subquadratic published i[ts first model card and benchmarks for its small model, SubQ 1.1](https://subq.ai/subq-1-1-small-technical-report), supplied third-party verification from data firm Appen, and started talking about its first design partners who now have access to its model.

So far, however, few people have actually used its model. To talk about the company, why its model isn’t widely available yet, and what it has in store for the near future, we met up with Subquadratic co-founder and CTO [Alex Whedon](https://www.linkedin.com/in/alexander-whedon).

> “We’re not a sparse attention company either.” — Alex Whedon, Subquadratic.

One thing Whedon definitely wanted to clear up is that the company’s current model may be based on sparse attention, but that isn’t its full mission.

“We’re not a sparse attention company either,” Whedon tells *The New Stack*. “We’ve been working on non-attention architectures for quite a while as well. We think that we will be the first people to leapfrog ourselves in terms of the next model architecture.”

We’ll get back to that.

## What the model card shows

It’s the company’s SubQ 1.1 Small model that people are talking about now. This model is built on Subquadratic Sparse Attention (SSA), an attention mechanism the company says scales close to linearly with context length instead of quadratically.

“In the case of Subquadratic Sparse Attention specifically, which is one of a couple model architectures we worked with, the idea is that not all of the token relationships matter,” Whedon explains. “Token relationship compute is why you see this quadratic scaling law.” This means there are almost a million possible two-token relationships in a 1,000-token input in a full attention matrix.

For SubQ 1.1 Small, the strongest results are in long-context retrieval, which makes sense, given that this is where the architecture should have its biggest edge.

![](https://cdn.thenewstack.io/media/2026/07/bbd5dae2-screenshot-2026-07-02-at-9.38.13-am-1024x325.png)

Credit: Subquadratic.

On the needle-in-a-haystack test, SubQ 1.1 Small scores near-perfect from 1 million tokens out to 12 million, even though it was trained mostly at 1 million. It hits 99.12 percent on Nvidia’s harder RULER test, which asks the model to trace and aggregate facts across a 128,000-token context rather than just find one.

On general capability, it lands just below the mid-tier frontier models, at 85.4 on GPQA Diamond against 87.5 for [Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/). On the LiveCodeBench coding benchmark, it scores 89.7, below Opus 4.8 and GPT-5.5, but slightly better than Sonnet 4.6.

Efficiency is where the model shines, though. The company says that at 1 million tokens, SubQ uses 64.5x less compute than dense attention and runs 56x faster than FlashAttention-2 on a single attention layer. At the full 12-million-token window, it puts the attention compute reduction at close to 1,000x.

![](https://cdn.thenewstack.io/media/2026/07/959fdb2e-screenshot-2026-07-02-at-9.37.54-am-1024x241.png)

Credit: Subquadratic.

“Even in full dense attention, the relative importance of over 99 percent of tokens is very low, attention scores are below 0.1,” Whedon says. “We actually show this in our model card. So clearly we’re just wasting compute most of the time, and in fact we’re maybe making the modeling task harder, because we’re introducing noise.”

“Transformers are a brute-force approach to the problem of text modeling,” he says. “You could say, ‘I’m going to compare every single individual token to every other possible individual token.’ That’s what transformers do. Very brute force, very naive. It just assumes that the first needs to look at the second, the third, the 50th, and the 5,000th. That’s not how humans read text.”

SSA also differs from [retrieval-augmented generation](https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/), which drops chunks of text before the model sees them. “Every token of the text is being seen by the model,” he says. “It’s just not being redundantly compared to every other token of the text.”

On capability, SubQ 1.1 Small lands roughly in Sonnet 4.6 territory, sometimes a bit above, sometimes below. But its edge, the company says, is size and cost.

“What we posted publicly was fewer than 100 billion parameters,” Whedon says about the size of the model. “I would venture to say that our model is smaller than any of the models offered by OpenAI or Anthropic. But our next model will *not* be.”

## Smaller, cheaper, built for enterprises

Subquadratic is also making the pitch that its model’s capabilities will be especially interesting for enterprises.

“We think that’s a pretty interesting enterprise offering,” he says. “We’ve seen a lot of people in the enterprise space talking about using the mid-tier models as opposed to the frontier for large data-processing tasks, which is exactly where we’re trying to plug in.”

Given that a lot of enterprise problems start with searching through large heaps of data, this makes sense. You can pack a lot of documents into a 12-million token context window, after all. Most of today’s models break down well before the user fills their [million-token windows](https://thenewstack.io/anthropics-claude-sonnet-4-model-gets-a-1m-token-context-window/), but with its near-perfect retrieval scores, SubQ may be a good answer for these problems.

As Whedon noted, the model’s first users are design partners, not the public. “We’re giving access to the model to design partners now, and these are mostly enterprises, largely with eight- to nine-figure spend,” Whedon says. “This is a core market that we really care about. It has been since day one.” A limited individual-access release will follow before any general availability.

The launch led with claims instead of benchmarks by choice.

“We were announcing mostly research,” he says. “We could have maybe messaged the launch a little bit differently. There was some debate about how we were going to message it.”

## Built on an existing model

One question from May hasn’t gone away, though. The model card states that Subquadratic “started with an existing open-weight frontier model by replacing its dense attention with Subquadratic Sparse Attention (SSA),” and then ran roughly one trillion tokens of long-context continued pretraining on books, documents, and repository-scale code.

That confirms what some of the skeptics suspected at launch, when OpenAI researcher Will Depue [wrote](https://x.com/willdepue/status/2051727314539479499) that SubQ was “almost surely a sparse attention finetune of Kimi or DeepSeek.” What’s new here then is the SSA mechanism and the long-context training recipe, not a model trained from scratch. The company has not said which open-weight model it started from.

The biggest lever on long-context retrieval was pretraining on very long sequences, Whedon says, something SSA’s efficiency made cheap enough to run as routine.

“Nobody’s talking about multimillion-token pretraining,” he says.

![](https://cdn.thenewstack.io/media/2026/07/56704cc4-screenshot-2026-07-02-at-9.40.28-am-1024x343.png)

Credit: Subquadratic.

## Why hybrids don’t go far enough

There have, of course, been attempts to improve on quadratic scaling, but Whedon thinks most of those attempts only go — almost literally — halfway. Hybrid models such as Nvidia’s Mamba-based Nemotrons, Qwen’s Gated DeltaNet layers, and the various linear-retention designs swap out some of the attention layers, but they don’t go all the way.

“If 80 percent of the layers are not quadratically scaling, then your maximum payoff is like a 5x increase as you scale toward infinity,” he says. “We see a 60x increase at 1 million tokens, almost 1,000x at 12 million. That is the type of payout that you only get if you actually change the scaling law, as opposed to a scalar win.”

He actually credits DeepSeek’s own sparse attention mechanism with making his company’s pitch easier.

![](https://cdn.thenewstack.io/media/2026/07/4fcbd349-screenshot-2026-07-02-at-9.38.52-am-1024x481.png)

Credit: Subquadratic.

“They showed that you could dynamically select relationships without a significant quality trade-off,” Whedon says. “However, they did so by redundantly using a smaller but still full-attention model that ends up using the vast majority of the compute at scale.”

Subquadratic ran its own benchmark against GLM 5.2. “At 1 million tokens, 58 percent of the prefill latency comes from that selection mechanism,” Whedon says. “So that selection mechanism, which is supposed to be seen as cheap, actually dominates the compute, because it’s a quadratically scaling component.”

## Beyond sparse attention

It’s also why Whedon pushes back on the “sparse attention company” label. Subquadratic has been working on what he calls “zero attention,” architectures that drop the attention mechanism altogether.

“Attention is kind of similar to RAG in that you have queries, keys, and values that represent information about the tokens that you’re processing,” Whedon says. “There’s this discreteness of representation, where everything is represented within these nice little boxes. That’s super convenient. It’s easy to build a brute-force solution around it. But it also means your ability to compress information is limited. If you had a more continuous, abstract way of representing the information, then you could compress it further, which means you can make smaller models, or you could just scale things up again to create another leap in intelligence.”

He traces the idea to world models and to Yann LeCun’s work. “The stuff we’re doing takes a lot of inspiration from world models, not the video modality in this case, but some of the things LeCun is talking about,” he says. “Rethinking how to represent long-range dependencies, how to keep a long-range state, how to rethink the objective function.” He stops there. “That’s probably all I could say for now.”

Subquadratic has also marketed only one of the three kinds of efficiency it says it is chasing. “We care about compute, sample, and memory efficiency,” Whedon says. “We’ve done a lot of work on all three, but have only really talked about the compute efficiency publicly.”

## The near-term plan

The near term plan for Subquadratic, however, is more modest. “Over time, yes,” Whedon says, when asked whether Subquadratic could rival OpenAI and Anthropic on raw quality in the long run. “In the shorter term, we have to be strategic. If we try to boil the ocean on much less capital, it’s not going to go well for us.”

The next model, he says, will likely be a mid-tier size rather than a frontier-class one (think SubQ 1.2 Medium), that he expects to outperform most of the competition in its tier.

How the team will bring the model to market, though, remains to be seen. I wouldn’t be surprised if the team launched its model on one of the hyperscaler’s large model platforms, but Whedon remained tight-lipped about the company’s plans.

The fact that we met with the Miami-based Whedon in San Francisco, though, gives you a bit of a hint of what the team is currently up to.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)