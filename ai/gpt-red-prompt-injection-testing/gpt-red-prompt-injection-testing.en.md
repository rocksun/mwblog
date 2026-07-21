Now that AI agents are performing real tasks rather than just generating text, the old methods of manual security testing can no longer keep up. Relying on human researchers to manually discover vulnerabilities one by one is too slow for the agents. Enter GPT-Red.

OpenAI on Wednesday unveiled an automated red-teaming system designed to find prompt injection vulnerabilities at a scale that would be impractical for human testers alone.

While human red teaming is highly creative, it is inherently slow and episodic. GPT-Red is designed to be relentless. By using one AI system to continuously and exhaustively probe another, brute-forcing thousands of exploit variations in seconds helps to map the exact boundaries of a vulnerability. OpenAI says GPT-Red is already helping to improve GPT-5.6’s resistance to prompt-injection attacks.

> By using one AI system to continuously and exhaustively probe another, brute-forcing thousands of exploit variations in seconds helps to map the exact boundaries of a vulnerability.

## Self-play trains the attacker

GPT-Red is trained through self-play reinforcement learning, where an attacker model repeatedly attempts to compromise AI systems while defender models learn to withstand those attacks. The attacker is compensated for inducing failures such as prompt injections, while defenders earn rewards for safely completing their tasks.

---

### More OpenAI reporting in TNS

---

OpenAI built a range of simulated environments that expose the models to realistic attack surfaces, such as emails, local files, API and tool responses, and other untrusted external inputs that agentic systems increasingly rely on.

## Benchmarks show a sixfold improvement

According to OpenAI, GPT-Red was able to generate successful prompt-injection attacks against nearly every model it evaluated, including internal research systems and production models up to [GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/). The resulting attack corpus was then incorporated into GPT-5.6’s training pipeline to harden the model against those failure modes.

OpenAI reports that GPT-5.6 experiences six times fewer failures on one of its most challenging direct prompt-injection benchmarks than the strongest production model it released four months earlier. In a broader evaluation with GPT-Red as the adversary, the company reports that GPT-5.6 Sol failed in 0.05% of direct prompt-injection attempts.

## Agents exploited in production

OpenAI didn’t limit GPT-Red to benchmark testing. The company also turned it loose on live agentic systems to see how well it could manipulate AI models that were capable of taking real-world actions.

One target was an AI-powered vending machine developed by Andon Labs. After training in a simulated environment, GPT-Red convinced the production agent to slash the price of items priced above $100 to just $0.50, bought one at the discounted price, and canceled another customer’s order.

OpenAI also tested GPT-Red against a Codex CLI agent running GPT-5.4 Mini in a series of data exfiltration exercises. According to the company, the specialized attacker found more successful attack paths than a prompted GPT-5.5 baseline while using fewer tokens — a sign that purpose-built offensive models can outperform general-purpose frontier models at security testing.

OpenAI says it has disclosed the vulnerabilities identified during these evaluations and is developing additional mitigations before deploying the techniques more broadly.

> GPT-Red convinced the production agent to slash the price of items worth more than $100 to just 50 cents, bought one at the discounted price, and canceled another customer’s order.

## Safer without sacrificing performance

Security improvements often come with a cost: models become more cautious and refuse legitimate requests. OpenAI says that didn’t happen with GPT-5.6. After integrating GPT-Red into its training pipeline, the company evaluated the model on both capability and over-refusal benchmarks. The result, according to OpenAI, was a model that became more resistant to prompt injection attacks without sacrificing overall performance.

GPT-Red signals that traditional, static security protocols are no longer enough. Now that agents are actively parsing untrusted emails, scanning PDFs, and browsing web pages, developers must assume all external data is a potential breach vector. Passing a one-time security audit before launch is effectively obsolete. Instead, engineering teams will need to follow OpenAI’s lead by moving adversarial testing upstream — weaving automated, adversarial LLMs directly into their deployment pipelines to relentlessly probe for edge cases before release.

OpenAI describes GPT-Red as a way to continuously feed newly discovered attack techniques back into model training, creating an automated cycle in which one generation of models helps improve the security of the next. The company says it plans to further scale the system by increasing training data and algorithmic improvements. A technical preprint detailing the research is expected later this week.

> Passing a one-time security audit before launch is effectively obsolete.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)