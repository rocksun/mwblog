Dropbox is entering the AI infrastructure space in a big way, announcing plans on Thursday to acquire [Tigris](https://www.tigrisdata.com/), a startup that provides object storage for AI applications.

The cloud-storage giant tells *The New Stack* that it’s paying $350 million for Tigris, a move designed to accelerate Dropbox’s own ambitions in selling storage infrastructure to developers and businesses. Indeed, alongside the acquisition news, Dropbox also announced DBX Agent Cloud, an upcoming offering that will initially let developers purchase object storage directly from Dropbox.

Dropbox, it’s worth noting, is no stranger to building storage infrastructure itself. Kicking off in 2015, the company [moved more than 90%](https://www.wired.com/2016/03/epic-story-dropboxs-exodus-amazon-cloud-empire/) of its user data off Amazon’s S3 cloud storage service onto an in-house system dubbed [Magic Pocket](https://dropbox.tech/infrastructure/how-we-optimized-magic-pocket-for-cold-storage), in a bid to improve performance and reduce costs. But as Dropbox chief business officer [Eric Webster](https://www.linkedin.com/in/eric-webster-70a08b5/) explains, selling storage infrastructure to *external* customers presents an entirely different set of challenges.

“Operating infrastructure for Dropbox and offering a storage product to developers involve different requirements,” Webster tells *The New Stack*. “Tigris brings a working commercial product, an experienced team, developer relationships and early customer traction.”

> “Tigris brings a working commercial product, an experienced team, developer relationships and early customer traction.”

That “customer traction” includes a slew of companies such as Amplified, Railway, Runpod, and Replicate, spanning everything from developer hosting platforms to GPU infrastructure and AI model deployment. Precisely the kinds of businesses that need fast, reliable access to large volumes of data, often while running applications and AI models across different environments.

## Eye of the Tigris

![Chief architect Yevgeniy Firsov flanked by CTO Himank Chaudhary (left) and CEO Ovais Tariq](https://cdn.thenewstack.io/media/2026/11/3c97d500-team-photo-97abcf36bb0b26ba8e461bf4df5664fd-1024x683.jpg)

*Chief architect Yevgeniy Firsov flanked by CTO Himank Chaudhary (left) and CEO Ovais Tariq* (Credit: Tigris)

Founded in 2022 by former Uber engineers [Ovais Tariq](https://www.linkedin.com/in/ovaistariq/) (CEO), [Himank Chaudhary](https://www.linkedin.com/in/himankchaudhary/) (CTO), and chief architect [Yevgeniy Firsov](https://www.linkedin.com/in/efirsov/), Tigris has built an S3-compatible storage platform that allows developers to keep their data accessible across different cloud and compute environments.

For developers training AI models, that could mean storing large datasets in one place while renting computing power from multiple providers. Using Amazon S3 in such situations can incur additional data-transfer costs, known as egress fees, and delays, particularly when the computing happens outside AWS. Tigris addresses this by automatically keeping data close to where it’s needed, while charging no egress fees for transfers out of its storage service.

The company announced a [$25 million Series A round of funding](https://www.tigrisdata.com/blog/series-a/) in October 2025, with investors including Spark Capital and existing backer Andreessen Horowitz.

While much of Tigris’s appeal lies in its existing product, customers and developer relationships, Dropbox sees an opportunity to turn that foothold into a much bigger business in the commercial storage infrastructure market.

“Combining those strengths with Dropbox’s experience operating storage at scale would give us a faster path into this market,” Webster says. “The acquisition lets us build on what both teams have already developed and learned from their customers.”

And so one of the clearest expressions of that ambition is DBX Agent Cloud, a service through which Dropbox plans to sell storage infrastructure to developers building AI applications, with Tigris expected to provide the underlying object-storage technology if the acquisition passes the usual array of regulatory approvals.

But why is Dropbox making this push into AI infrastructure? And why now?  
  
“AI applications are creating and working with growing volumes of content, from images and video to training datasets and model artifacts,” Webster says. “As models and compute providers change, that content needs a consistent home.”

> “AI applications are creating and working with growing volumes of content, from images and video to training datasets and model artifacts.”

Founded in 2007, Dropbox has spent the best part of two decades dealing with the challenges of storing and managing vast amounts of customer data, from consumers through the enterprise. And it now hopes to put that experience to work for developers building their own applications.

“DBX Agent Cloud extends that expertise to companies and developers building applications, starting with standalone object storage,” Webster says.

The plan, ultimately, is to add filesystem and content-processing capabilities next, allowing AI applications to work with different types of content, track files, and pick up where they left off across sessions.

Dropbox has yet to provide a launch date for DBX Agent Cloud, or explain exactly how the two companies’ technologies will be integrated.

“We’ll share more about the technical integration and availability as those plans develop,” Webster says.

As for existing Tigris customers, well, Dropbox is promising business as usual, at least initially. Webster says they won’t “need to migrate or change how they use the service” when the acquisition closes, and will “continue to receive support for the Tigris product.”

What happens further down the line is less certain, particularly as Dropbox builds out its own filesystem and content-processing capabilities around Tigris’s foundation.

“As the product evolves, we’ll communicate directly with customers before any changes that affect them,” Webster adds.

## Dropbox puts AI to work on files

Alongside the acquisition news on Thursday, Dropbox also announced what it’s calling a “major evolution” of its main product, one that “brings AI-powered capabilities directly to customers’ existing files and workflows,” the company says.

Back in 2023, Dropbox [debuted Dash](https://blog.dropbox.com/topics/product/introducing-AI-powered-tools), an AI-powered search tool that allowed users to find information scattered across services such as Google Workspace, Microsoft 365, and Dropbox itself. Now, the company is taking things further, allowing users to instruct AI to work directly on their files, from editing PDFs and images, to reorganising folders, transcribing recordings, and completing multi-step tasks.

“Customers told us they wanted these AI-powered features directly in the product where their content and workflows already live,” [Mike Torres](https://www.linkedin.com/in/miketorreshq), Dropbox’s chief product officer, tells *The New Stack*.

![Dropbox AI proposes a plan to organise files](https://cdn.thenewstack.io/media/2026/11/bec4012b-product-static-proposed-plan-600x700-1.png)

*Dropbox AI proposes a plan to organise files*

The company had already begun [integrating Dash into Dropbox](https://blog.dropbox.com/topics/news/fall-2025-release-dropbox-dash-context-aware-ai-teammate) last year, bringing AI-powered search, document summaries, and the ability to ask questions about stored content into the core product.

“The new experience builds on that foundation and what we’ve learned from customers, helping them move from finding and understanding information to organizing files, editing content, and completing supported multi-step tasks,” Torres continues.

> “We want customers to have the freedom to use the AI tools that work best for them.”

Dropbox says more than 70,000 teams have received access to the new capabilities, although it hasn’t disclosed how many are actively using them. As for pricing, Torres says that eligible Standard and Advanced plans include a certain allocation of AI credits, with customers able to purchase more as needed.

![Model-picker inside Dropbox](https://cdn.thenewstack.io/media/2026/11/c4dbf5f6-product-static-model-picker-600x700-1.png)

*Model-picker inside Dropbox*

The company is also giving users a choice of AI models within Dropbox, alongside integrations with third-party tools including ChatGPT and Claude. These connections allow customers to work with their Dropbox files through external AI services without repeatedly uploading them, with the resulting content saved back to Dropbox.

“We want customers to have the freedom to use the AI tools that work best for them,” Torres says.

Behind that, perhaps, lies a similar philosophy to the Tigris acquisition: allowing developers to choose *where* they run their AI applications while keeping the underlying data accessible. Dropbox is betting it can turn that proposition into a substantial new infrastructure business, although with the acquisition still to close and no launch date for DBX Agent Cloud, it remains to be seen how that ambition translates into a product developers actually want to use.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=dropbox-acquires-tigris-s3-alternative)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)