Most AI developers are building products backwards. They start with a foundation model, wrap it in an interface, and then wonder why users aren’t getting the results they need.

I see this pattern everywhere. Developers treat models like APIs: Plug them in, configure some parameters, and ship. But foundation models aren’t utilities — they’re starting points that engineers need to shape, train, and align with the specific problems their users face every day.

## Why Generic Foundation Models Fail for Enterprise Applications

Consider a developer at a financial services company trying to use GPT-4 to [build an investment research](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) application. The model can analyze financial documents and answer questions about market trends. Still, it doesn’t understand the difference between a routine earnings call and one that signals a major [strategic shift for the business](https://thenewstack.io/why-businesses-are-rethinking-it-providers-and-shifting-to-strategic-partnerships/). It can’t distinguish regulatory filings that matter to your internal compliance teams from the ones that don’t.

OpenAI trained GPT-4 for broad capabilities across thousands of domains. But this financial services company needs a model that comprehends the nuances of financial analysis, regulatory requirements, and the specific workflows of the portfolio managers on the team.

The root problem: Two different design goals

Two completely different groups with different objectives design foundation models, and end-user AI applications — [researchers and product developers](https://thenewstack.io/why-businesses-want-to-enable-no-code-and-low-code-automation/). Researchers at major model labs optimize for broad capabilities across academic benchmarks. Often, they use the same training datasets as their competitors. But [developers build applications](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/) for particular customer and market needs — customer service for a food delivery app, generative graphic design for a productivity platform, automated competitor analysis for market research.

By design, these approaches are misaligned. The researcher at OpenAI, DeepSeek, Meta or Anthropic isn’t building a model so that when a Deloitte consultant says “analyze this report,” it knows to compare a client’s data with specific competitors; or a model that understands the difference between “urgent” for a customer service representative versus a physician making a medical diagnosis. Developers are.

The model is the raw material. Developers’ proprietary data is what shapes it into a product that matches user workflows and business requirements.

What does this [mean for your AI product strategy?](https://thenewstack.io/what-generative-ai-means-for-product-strategy-and-how-to-evaluate-it/)

To achieve model-product alignment, developers must prioritize:

## The Data Feedback Loop: Building Models That Actually Learn From Users

Applications that work create feedback loops where every user interaction makes the model better at a specific task. When a user corrects the application’s output, that correction flows back into model training. When users ignore certain suggestions, the model learns to stop making them.

A data feedback loop creates compounding advantages. More users [generate better training data](https://thenewstack.io/kumo-surfaces-structured-data-patterns-generative-ai-misses/), which improves model performance, which attracts more users. Instead of hitting performance walls as they scale, these systems improve.

This [approach requires treating model development as part of product](https://thenewstack.io/a-portal-as-a-product-approach-for-internal-developer-portals/) development, not vendor management. It means managing model [performance across different user segments and solving new problems](https://thenewstack.io/the-complexity-of-solving-performance-problems/) around model versioning and deployment.

## Model Composition: How Leading Companies Combine Multiple AI Systems

The most differentiated AI applications compose multiple models and modalities to solve problems rather than relying on a single model. A logistics company might combine computer vision for package scanning with natural language processing for customer communications, then predictive modeling for route optimization — all working as a unified system.

This requires engineers who understand model architecture and can make strategic decisions about when to use retrieval-augmented generation versus fine-tuning a specialized model.

The applications that will win aren’t those with privileged access to closed-source models. They’re the ones that have dedicated resources to tuning open source models into valuable end-products through careful alignment, data collection and iterative improvement.

Developers who solve this alignment problem early will build moats that are impossible to replicate. Those that don’t will compete on features that any competitor can copy by switching to the latest closed-source model API.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/4ab90f0d-cropped-20dc5a69-lin-qiao-main-scaled-1-600x600.jpg)

Lin Qiao is the CEO and co-founder of inference platform Fireworks AI, which empowers developers and businesses like Uber, Verizon, Cursor and Notion to build highly optimized and production-ready genAI applications. Prior to founding Fireworks, Lin was the co-creator and...](https://thenewstack.io/author/lin-qiao/)