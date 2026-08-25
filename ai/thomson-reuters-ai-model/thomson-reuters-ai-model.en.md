Thomson Reuters has developed its own AI model for legal, tax and compliance work, trained on the company’s proprietary professional content and designed to power features inside products such as CoCounsel. Early benchmarks show Thomson competing with models from OpenAI, Anthropic and Google across several professional and general-purpose evaluations.

But Thomson wasn’t built from the ground up. The company started with an existing open-source foundation and spent approximately $40 million training the model, including compute and talent, the company tells *The New Stack*.

“Most of our investment went into further training on decades of proprietary content and expert-driven evaluation, not pre-training a foundation model from scratch,” Thomson Reuters tells *The New Stack*.

For companies sitting on years of proprietary data, that approach opens another option other than relying entirely on models from OpenAI, Anthropic or Google and spending billions trying to build their own.

## Proprietary data as moat

The model was trained using content from Thomson Reuters’ own collection, including Westlaw, Practical Law, Checkpoint, and Reuters. Hundreds of subject-matter experts were involved in evaluating outputs and finding places where the model failed. Thomson Reuters says it has used less than 10% of the content available to it for Thomson’s training so far.

Thomson Reuters still uses frontier models elsewhere in its products. Its new CoCounsel Legal, for example, is built on Anthropic’s Claude Agent SDK. That same SDK is regularly showing up across industries — [Spline recently rebuilt its entire 3D editor and opened it to Claude Code through MCP](https://thenewstack.io/spline-v2-mcp-agents/), letting coding agents work directly inside live design files. Thomson Reuters is using the same agentic plumbing for a very different purpose: legal research and document analysis at scale. But Thomson the AI model, gives the company its own model for jobs where specialized training makes sense.

The first is Tabular Analysis in CoCounsel Legal, which can work across as many as 10,000 documents and answer up to 100 questions about them. Thomson is becoming the default model for that feature.

For now, customers won’t be buying access to Thomson directly.

“Thomson is built for legal, tax, and compliance professionals; the people who use products like CoCounsel Legal every day,” Thomson Reuters tells *The New Stack*. “It powers specific capabilities inside our own products, starting with Tabular Analysis in CoCounsel Legal, and a smaller, open-weight version is also available to researchers on Hugging Face.”

The company said it is looking at ways it could commercialize Thomson in the future.

## Trained to flag uncertainty

Legal work is an obvious place to want more control over a model. A made-up citation or confidently wrong answer can become a much bigger problem once it makes its way into actual legal work.

Building Thomson didn’t make that problem disappear.

“There’s no guarantee any AI model, including Thomson, is error-free,” Thomson Reuters tells *The New Stack*.

Owning the training process gives Thomson Reuters more control over how the model handles uncertainty.

“Because Thomson Reuters trains the model directly, it can shape tradeoffs that general-purpose models don’t optimize for in the same way, including how the model weighs helpfulness against accuracy,” the company said.

Thomson is specifically trained to admit uncertainty rather than produce an answer simply because the user asked for one.

“Thomson is trained to flag uncertainty rather than force a confident-sounding answer, even when that’s less satisfying to the person asking,” Thomson Reuters said. “That’s a deliberate choice: a model that always tries to please the user is a model more prone to hallucination, sycophancy, and other failure modes that matter far more in professional work than in casual use.”

Even with that training, the company hasn’t done away with retrieval.

Thomson can pull from sources such as Westlaw and Practical Law so its responses can be grounded in material a legal professional can check. The company is effectively using the two approaches together: train the model for the domain, then give it access to authoritative information when it needs to answer a question.

“It’s not one approach instead of the other,” Thomson Reuters said. “It’s a model trained to reason more carefully, combined with retrieval that keeps it anchored to source material a professional can check.”

> “Thomson is trained to flag uncertainty rather than force a confident-sounding answer, even when that’s less satisfying to the person asking.”

## Traceability has its limits

That raises another problem for an AI system being used by lawyers: knowing where an answer came from.

If an attorney uses AI to help prepare a brief, knowing the model was trained on Westlaw isn’t enough. The attorney needs to know whether the cases and statutes supporting the argument actually say what the AI claims they say.

Thomson Reuters says many Thomson outputs can be connected to specific Westlaw or Practical Law sources. It doesn’t promise that every piece of an answer can be traced back to a particular passage.

“We wouldn’t claim every output can be traced line by line to an exact statute or ruling,” Thomson Reuters tells *The New Stack*.

Instead, the company says Thomson is designed to make its reasoning checkable where possible, while leaving the final verification to the professional using it.

Thomson is the model doing the work. CoCounsel is the product around it, where Thomson Reuters can add citations, verification and review before that work goes any further.

The latest version of CoCounsel Legal, released Aug. 20, moves further in that direction. The agentic system can move between research, analysis, drafting and verification, while Deep Research Verify checks whether Westlaw and Practical Law sources actually support the claims being made.

> “We wouldn’t claim every output can be traced line by line to an exact statute or ruling.”

## The benchmarks need some context

Thomson Reuters says Thomson is competitive with much larger frontier models, and its early results back that up in some areas.

In Thomson Reuters’ published comparison with Gemini 3.1 Pro, Claude Opus 4.8 and GPT-5.5, Thomson came out on top in three of seven reported categories, including PRBench Legal Hard, an instruction-following composite and long context.

Other models led elsewhere. Gemini 3.1 Pro scored higher on Stanford LegalBench and the reasoning composite, while Claude Opus 4.8 led the Harvey Legal Agent Benchmark and coding.

There are some important differences in how those results were produced. Thomson used test-time scaling, Gemini and Opus were run in reasoning modes, while GPT-5.5 was tested in non-reasoning mode. Some of the evaluations in Thomson Reuters’ composites are also internal benchmarks.

Thomson Reuters gave the models 53 legal research questions written by its own subject-matter experts. Thomson could search Westlaw and Practical Law through an internal agentic system. The competing models searched the web using Brave. Thomson performed better.

> “It’s not one approach instead of the other … It’s a model trained to reason more carefully, combined with retrieval that keeps it anchored to source material a professional can check.”

## Owning the right layer

Thomson Reuters makes a compelling case for being selective about which layers of the AI stack are truly worth owning. For most companies, trying to match OpenAI, Anthropic or Google across every task would make little sense. But a company with proprietary data, deep domain expertise and millions of professional workflows has something the frontier labs don’t.

That question — which layers to own, and which to rent — is playing out across the industry. [Cloudflare is making a similar bet on the infrastructure side](https://thenewstack.io/cloudflare-ai-web-economics/), positioning itself as the economic layer between publishers and AI companies rather than trying to build the models themselves. And on the compute side, [five European companies recently committed to buying AI compute that doesn’t even exist yet](https://thenewstack.io/mistral-third-party-open-models/), wagering that securing capacity matters more than which model sits on top. Thomson Reuters is making the opposite play: it already has the data and the workflows, and it’s building in-house only where that proprietary edge justifies the cost.

Thomson Reuters can leverage third-party models where they fit best while building in-house only where its proprietary data provides an edge. The question is whether that specialized slice of the business is large enough to make owning the model worth the investment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)