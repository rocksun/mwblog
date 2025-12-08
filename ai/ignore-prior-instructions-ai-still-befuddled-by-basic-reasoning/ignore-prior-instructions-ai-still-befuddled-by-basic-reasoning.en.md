A fact is a fact is a fact. But for a large language model (LLM), a fact is what someone says is a fact, if, in fact, they say it sternly enough.

The CTO of [Microsoft Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) had select words to share about the state of security within AI operations, which obviously needs work. And while he covered the latest state of the art in prompt injections, jailbreaks and hallucinations, he also discussed a set of concerns around the LLMs basic ability to reason.

[![](https://cdn.thenewstack.io/media/2025/12/6f17ca40-acm-russinovich-300x226.jpg)](https://cdn.thenewstack.io/media/2025/12/6f17ca40-acm-russinovich-300x226.jpg)

Mark Russinovich

This possibly inherent flaw points to the need for users to understand what an LLM can and can’t do.

“It’s all about treating [an LLM] as a reasoning engine that’s flawed and imperfect and then putting the guardrails around the system to mitigate the risk,” said [Mark Russinovich](https://www.zerodaythebook.com/) in a talk for the Association for Computing Machinery’s [TechTalk series](https://learning.acm.org/techtalks-archive). “How much are you going to invest in a guardrail? It depends on the risk you’re willing to accept.”

## Reasoning Challenges

How well LLMs can make logically sound decisions is not yet well understood. Studies have suggested they would flunk basic classes in both informal and formal reasoning.

“People assume that AI, when it’s given good context, is going to reason over that context reliably,” Russinovich said. Computers are nothing if not logical machines, right?

LLMs are good at summarizing bodies of information, but like a doddering relative, they may quickly “forget” parts of that information from their knowledge base. Drop a fact (“Sarah’s favorite color is blue”) at the beginning of a long prompt, and the LLM might not even remember that blue is Sarah’s favorite color when asked about it later.

Basic logic tests can also be problematic. For instance, when given a large number of logical relationships (i.e., “A > C” or “C = A”), an LLM may or may not successfully find any contradictions for the set as a whole. Multiple runs (prompt: “Are you sure?”) may produce different results, some right, some wrong.

In his own coding, Russinovich has found similar behavior. Once, he challenged the hypothesis made by ChatGPT about race conditions in his code, only to back down when challenged, admitting that “I made a logical error.”

And LLMs will assert that they are wrong, *even when they are right*! After all, at the user’s behest, the model is just looking for why something might be wrong.

People assume that as models are upgraded, their ability to reason also improves. But that doesn’t seem to be the case, Russinovich said. He cites Microsoft Research work that benchmarks reasoning across models using the [Eureka framework](https://microsoft.github.io/eureka-ml-insights/).

“New models don’t necessarily perform better than the previous version of that model, at least in some of the dimensions,” he said. “This is something that every enterprise needs to be going and looking at. Just because a new version of a model comes out doesn’t mean it’s going to perform as well on your particular scenario as the previous version did.”

[![comparing models in reasoning.](https://cdn.thenewstack.io/media/2025/12/87f1ae9c-acm-russinovich-ai_security-reasoning_failures-02-1024x563.png)](https://cdn.thenewstack.io/media/2025/12/87f1ae9c-acm-russinovich-ai_security-reasoning_failures-02-1024x563.png)

Microsoft Research

In other words, the organization has to evaluate, evaluate, evaluate.

## Gaslighting the LLM

In the Q&A portion of the talk, Russinovich talked about what he called *induced hallucinations,* where you can give the model a false premise and then ask it to expand on this premise. “Many models just go off and start to make things,” he said.

If the model gets stubborn, the user can try taking on a greater tone of authority in their prompts. They are trained to acquiesce, he pointed out.

## LLMs Are Probabilistic, Not Deterministic

At their core, LLMs are probabilistic and can never definitively deliver the truth, Russinovich asserted.

He offered an example: In a training set embedded with nine assertions that the capital of France is Paris, and one assertion that Marseille is the capital, the LLM will at some point offer the assertion that Marseille is the capital.

For Russinovich, the fatal flaw of LLMs, at least in their present form, is that they are not deterministic. This is a “fundamental” limitation to such [transformer-based](https://thenewstack.io/grounding-transformer-large-language-models-with-vector-databases/) models.

“These things are fundamentally unfixable because of the nature of the way that these systems work,” he said.

[![Screenshot.](https://cdn.thenewstack.io/media/2025/12/650d6801-acm-russinovich-ai_security-legal-devmon-1024x547.png)](https://cdn.thenewstack.io/media/2025/12/650d6801-acm-russinovich-ai_security-legal-devmon-1024x547.png)

Microsoft Copilot once suggested to Russinovich a nonexistent tool from his own sysinternals site called “DevMon.” “I could have wrote it, but never did,” he said.

## Ignore Previous Instructions

Perhaps it is because of these weak reasoning skills that the models fall prey to pranks and hacks.

Russinovich and a colleague had found a way to fool LLMs into giving out information they otherwise would have been prohibited from providing. The classic example is asking the model to build a pipe bomb. Today’s public-facing LLMs have blocks that prevent them from answering that question.

But the pair of researchers found that by breaking apart the questions into a set of smaller, incremental questions, they were often able to extract this pipe-building instruction set anyway.

Start with a question such as “What is a pipe bomb?” Then ask, “What are the parts of a pipe bomb?” And so on. You pull the answer out of the machine piece by piece, so as not to trigger the safety mechanism.

Russinovich provided an example of having this conversation with ChatGPT-4.0.

LLMs certainly can’t be trusted to check their own work. Russinovich related that he once asked an LLM to check its own references to ensure they were all correct. For some previous work, it had taken all the references directly from the internet.

But in the recheck of its own work, it had found various errors in things like author names or publication dates.

And two more checks of references turned up additional errors.

“Even after multiple rounds of it evaluating its own correctness, it was still making mistakes,” Russinovich noted.

There is a “rampant epidemic” of such nonexisting references [plaguing the legal world](https://www.damiencharlotin.com/hallucinations/), he said.

The problem so bothered Russinovich that he [vibe coded](https://thenewstack.io/mastering-vibe-coding-may-the-force-be-with-you/) a tool called [ref checker](https://github.com/markrussinovich/refchecker) to validate (largely unstructured) references against [Semantic Scholar](https://www.semanticscholar.org/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)