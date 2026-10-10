**Microsoft on Friday** launched Microsoft-Decision-1 in Foundry, three days after OpenAI [opened its Decisions API to every developer](https://thenewstack.io/openai-decision-models-deployment/) in public beta. Microsoft post-trained the decision model on Alibaba’s Qwen3.5-9B rather than anything its partner OpenAI built, though it plans to rebase it soon on its own MAI models as well as OpenAI’s.

[Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) costs $0.042 per million input tokens with free output, exactly what TypeSafe charges for [Jev](https://thenewstack.io/typesafe-jev-system-one/), and it arrived the same day TypeSafe announced an $870 million Series A at a $7.5 billion valuation led by a16z.

Microsoft is about three and a half weeks behind the startup that started this category, and in that time OpenAI, Upstage, Perplexity, Cloudflare, and AWS have all [shipped decision models of their own](https://thenewstack.io/decision-models-system-one/).

TypeSafe says nearly 30% of the Fortune 500 has tried Jev, though it hasn’t named any of them, and TypeSafe CEO [Diogo Almeida](https://www.linkedin.com/in/diogomda) posted on X that “29.4% of the Fortune 500 showed up” in the three weeks since launch.

Those are the same companies Microsoft sells Azure to, which makes TypeSafe’s early traction hard for Microsoft to ignore.

## Microsoft’s first customer is itself

Microsoft Chairman and CEO Satya Nadella announced the model on Friday on X, writing, “We’re already testing it across Microsoft,” and four internal teams back him up.

Xbox Research used it to sort more than 10,000 pieces of player feedback, the Copilot team graded chat and agent responses with it, on-call engineers used it to pull context during live incidents, and Microsoft Discovery used it to score experiments before an agent replans.

Microsoft’s numbers show it’s more than 14 times as fast as GPT-6 Sol at a fraction of the cost for Xbox, and 46 times more consistent in Discovery.

But the model may have a bigger job in mind. On Wednesday, the company said GitHub Copilot will soon [decide when to run a task on-device and when to send it to cloud-scale models](https://thenewstack.io/https-thenewstack-io-copilot-local-inference-routing/), though it hasn’t disclosed what Copilot sends to the cloud.

Model routing is among the use cases Microsoft lists for Decision-1, but the company hasn’t said whether the model will make those calls for Copilot. With routing decisions to make across Copilot, GitHub, and Xbox, Microsoft has an incentive to handle them in-house.

> With routing decisions to make across Copilot, GitHub, and Xbox, Microsoft has an incentive to handle them in-house.

## Decision models became cheap

Cognition’s vice president of engineering, [Jared Palmer](https://www.linkedin.com/in/jaredlpalmer/), [spent about $95 in Modal H100 time](https://runtimewire.com/article/jared-palmer-kev-qwen35-decision-models) porting his open-source Kev models to Qwen3.5, and Cloudflare [built Clef-flash](https://blog.cloudflare.com/clef-decision-models/) on the same Qwen3.5-9B base Microsoft picked.

Jev’s price is becoming the going rate: Palmer lists Kev-4B on OpenRouter at $0.042 per million input tokens, Perplexity charges $0.02, and OpenAI charges more than double Jev’s rate. At those prices, revenue from individual decision calls is minimal, and Microsoft’s bigger opportunity is keeping agent traffic, including the generative calls around each decision, running through Foundry. Plus, the OpenRouter listing could bring developers who aren’t using Azure into that ecosystem.

[Achint Srivastava](https://www.linkedin.com/in/achint/), vice president of software engineering in Microsoft’s Office of the CTO, [introduced Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) as a way to add decision-making to existing applications, agents and workflows “in a secure, trusted environment.”

## Text only, no weights

This shows where Decision-1 falls short of its rivals. Its Foundry listing says it accepts up to 32,768 tokens of text and returns JSON, but it doesn’t support images, unlike OpenAI’s Decisions API and Cloudflare’s Clef, which uses a vision encoder.

While Cloudflare [released Clef under Apache 2.0](https://blog.cloudflare.com/clef-decision-models/), Microsoft has yet to announce open weights. AWS, Upstage, and Ollama have also [adopted TypeSafe’s System One API](https://thenewstack.io/decision-models-system-one/), now a common interface across the category, but Microsoft hasn’t said whether Decision-1 is fully compatible, though its Foundry sample code calls a /systemone endpoint.

## Calibration under adversarial pressure

The company says Decision-1’s probabilities are calibrated, meaning a 90% prediction should be right about nine times in 10 on representative cases, but research on Jev shows how far a confident score can drift when the input is written to mislead. Microsoft’s own Foundry documentation advises customers to validate calibration on their own data.

> The company says Decision-1’s probabilities are calibrated, meaning a 90% prediction should be right about nine times in 10 on representative cases.

In the [JevOut preprint](https://arxiv.org/abs/2609.30243), USC computer science researcher Zixiang Xu and his co-authors found that short, natural-sounding additions to the context flipped 312 of Jev’s 508 initially correct decisions. In 229 cases, Jev assigned at least 70% probability to the wrong answer. Three other scoring systems showed flip rates between 64.9% and 73.2% under the same testing approach.

Microsoft tested Decision-1 with eight kinds of perturbations, including reordered options and paraphrased descriptions, which changed 1.3% of its answers on average. JevOut didn’t test Decision-1, so it’s unclear how the model would hold up against similar attacks. Microsoft also hasn’t confirmed whether Decision-1 fully supports the System One API competitors adopted, leaving questions about interoperability and how much trust to place in its confidence scores.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)