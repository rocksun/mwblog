**Google Cloud launched Gemini Enterprise for Legal this week**, a purpose-built agentic AI solution to automate legal workflows, including contract review, regulatory monitoring, document drafting, and data discovery. It signals that the next phase of enterprise AI competition will hinge on who can best specialize the stack — not just who can build the strongest foundation model.

The release comes alongside [Gemini Enterprise for Financial Services](https://www.googlecloudpresscorner.com/2026-08-25-Google-Cloud-Launches-Gemini-Enterprise-for-Financial-Services), another agentic AI solution, this time geared towards financial professionals. Together, the two are the first offerings in what Google describes as “a series of specialized, packaged industry solutions built on top of the secure, fully governed Gemini Enterprise platform.”

[Gemini Enterprise for Legal](https://www.googlecloudpresscorner.com/2026-08-25-Google-Cloud-Launches-Gemini-Enterprise-for-Legal) came about 24 hours after the debut of [Thomson Reuters’ Thomson](https://thenewstack.io/thomson-reuters-ai-model/), its own AI model for legal, tax, and compliance work, which it spent $40 million developing.

While Gemini Enterprise for Legal and Thomson look similar on the surface — both aim to make AI more useful for legal workflows — they are structurally different. Google’s new offering is an agentic system built around its existing Gemini models. Thomson, on the other hand, is a proprietary model that the company further trained on its own proprietary professional content and input from subject-matter experts.

Still, in some important ways, the launches are two sides of the same coin. Both show companies are making a push to specialize AI for professional domains — but that specialization can come from different layers of the stack.

## Specialized AI doesn’t have to mean a specialized model

Google and Thomson Reuters are both making moves to build more specialized AI, but they’re attacking the beast from different angles.

Thomson Reuters made a splash by taking an existing open-source foundation and spending millions to train the model with expert evaluation and decades of content from its own collection, including Westlaw, Practical Law, Checkpoint, and Reuters. The resulting Thomson even beat Gemini 3.1 Pro, Claude Opus 4.8, and GPT-5.5 in some benchmark evaluations.

Google, meanwhile, is building much of its legal specialization around the model through agents, integrations, tools, and governance, though the company says its solution may also include model optimizations.

> Both show companies are making a push to specialize AI for professional domains — but that specialization can come from different layers of the stack.

Gemini Enterprise for Legal is built on Google’s own AI stack, which spans global infrastructure, custom silicon, foundation models, and an AI-ready data platform. While Thomson Reuters seems to be making the point that having proprietary data and using it to further model training can give it an edge, Google’s approach shows that specialized AI can also emerge by working above the foundation-model layer.

The solution centers on four core components: 1) purpose-built specialized skills to guide AI agents through legal tasks; 2) secure Model Context Protocol (MCP) integrations to connect with legal industry platforms, like DocuSign; 3) access to a specialized network of third-party agents, legal tech providers, and consulting partners, like Accenture and Deloitte; 4) a control plane for risk management, audit logging, and governance.

With these pieces working together, Google says Gemini Enterprise for Legal can automate and speed up a range of legal operations, such as automating data discovery and Data Subject Access Requests (DSAR) responses, and autonomously tracking legislative updates, court dockets, and supervisory bodies to update policy drafts. It can also speed up contract review and negotiations, draft NDA documents, prepare court filings, redact legal documents, and build and update contracting playbooks.

## Owning a model doesn’t necessarily mean going all in on it

A striking point in Thomson Reuters’ Thomson announcement was that the company’s independently trained model outperformed leading models on several professional and general-purpose evaluations.

But that doesn’t mean the company’s forgoing frontier models altogether. Instead, it’s opting for a pick-and-choose strategy based on which model works best for the task at hand.

Just look at CoCounsel Legal, Thomson Reuters’ AI assistant, built on Anthropic’s Claude Agent SDK, that helps legal professionals with research, analysis, and drafting. As its first deployment, Thomson will work within the Tabular Analysis product, the document-review tool that analyzes large volumes of documents. When Thomson gives a real advantage over other leading models, CoCounsel Legal will let it take the lead. But when other models are better suited for the task, the AI assistant will route work accordingly.

## Model selection is now only one piece of the puzzle

Much of the conversation around adapting AI for domain-specific tasks has looked like a model problem: Take the best general-purpose model available and feed it the right data and context. But these two launches show the picture is getting more complex.

> Moving forward, the competitive advantage may increasingly belong to whoever can bring something uniquely valuable that others can’t easily get their hands on.

Yes, the model is still a fundamental part of developing specialized AI, but it’s not the only way to differentiate. Moving forward, the competitive advantage may increasingly belong to whoever can bring something uniquely valuable that others can’t easily get their hands on.

For Google, that’s its integrated AI and cloud stack, which Gemini Enterprise for Legal extends with specialized skills, MCP integrations, governance, and tools. For Thomson Reuters, that edge looks like something different: a proprietary, specialized model built on decades of content and expert knowledge that works inside a multi-model system.

Neither approach does away with the importance of the underlying model. But both suggest that a strong model alone isn’t enough to spearhead specialized AI. For developers, that begs the question: What part of the stack is worth owning?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)