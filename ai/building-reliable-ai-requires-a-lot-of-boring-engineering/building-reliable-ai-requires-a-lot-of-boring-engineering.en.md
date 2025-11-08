After a decade building everything from iPhone apps at early stage startups to medical AI systems at major tech companies, I’ve watched countless organizations rush headfirst into AI adoption only to stumble when reality hits. The numbers tell a sobering story: [74% of companies struggle](https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value) to achieve and scale value from AI, and [42% abandon](https://medium.com/@stahl950/the-ai-implementation-paradox-why-42-of-enterprise-projects-fail-despite-record-adoption-107a62c6784a) their AI initiatives before reaching production. The problem isn’t the technology itself, but the way we’re approaching it.

The core issue? Most AI projects fail because they’re treated as machine learning (ML) experiments, not engineering projects.

## **The Engineering Mindset Gap**

During my time as a senior generative AI (GenAI) engineer in medical tech and now as a founder, I’ve seen the same pattern repeat: Brilliant [data scientists build impressive models](https://thenewstack.io/automating-context-in-structured-data-for-llms/) that never make it to production because no one thought about reliability, maintainability or real-world deployment constraints.

Traditional software engineering solved these problems decades ago, yet we’re reinventing the wheel with AI. [Industry research](https://developers.google.com/machine-learning/guides/rules-of-ml) on production ML systems shows that the ML model code represents only 5% of a real-world production system. The other 95% is pure engineering: [data pipelines](https://thenewstack.io/how-industries-are-using-ai-agents-to-turn-data-into-decisions/), monitoring, testing, [deployment infrastructure](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/) and maintenance.

## **Why Software Engineering Principles Still Matter in AI**

The companies successfully scaling AI aren’t the ones with the fanciest algorithms. They’re the ones applying boring, well-established engineering practices to AI systems.

[Prompts](https://thenewstack.io/your-ai-prompts-are-programming-the-future-so-use-them-wisely/) need the same rigor as any other code. They require version control, testing, debugging and performance monitoring. The teams that recognize this early avoid the inevitable technical debt that kills AI projects later.

While traditional unit tests check whether functions return expected outputs, AI systems require testing for model drift, data quality and edge cases. Leading AI teams have learned that ML systems need [continuous monitoring](https://thenewstack.io/why-ai-demands-a-new-approach-to-observability/) because they degrade in ways traditional software doesn’t.

The most reliable AI systems I’ve built treat uncertainty as a first-class citizen. They’re designed to fail gracefully when models produce unexpected outputs, have fallback mechanisms and provide clear feedback to users about confidence levels.

## **The Startup Versus Enterprise Divide**

Major tech companies have the luxury of massive infrastructure and dedicated reliability engineering teams, but most companies don’t. And for many startups, every engineering decision has to account for limited resources and the need to move fast while maintaining quality.

The key insight is to start with engineering fundamentals, then add AI capabilities. Too many companies do the reverse, building impressive demos that can’t survive contact with real users and production environments.

> The companies winning with AI aren’t necessarily the ones with the best algorithms. They’re the ones applying decades of software engineering wisdom to a new problem domain.

Managing AI projects requires different skills than traditional software projects. Data dependencies create cascading effects that are harder to predict than code dependencies. Feature engineering often requires domain expertise that sits outside the engineering team. Model training can take days or weeks, which makes rapid iteration challenging.

The solution is not to abandon agile methodologies but to adapt them. We plan sprints around data availability, not just feature completeness. We budget time for model retraining and validation. We treat AI model updates with the same caution as database schema changes.

## **Skills Traditional Engineers Need for AI**

The [transition from traditional software engineering to AI development](https://thenewstack.io/embracing-ais-transformation-transitioning-from-a-software-developer-to-a-builder/) isn’t about learning complex mathematics or deep learning theory. It’s about adapting engineering discipline to handle uncertainty and probabilistic systems.

The biggest bottleneck in AI projects isn’t model architecture but [data quality and availability](https://thenewstack.io/finding-the-right-data-architecture-for-rag-pipelines/). Engineers who understand data pipelines, ETL processes and database optimization are more valuable than those who can implement the latest transformer architecture.

Traditional application monitoring tracks uptime and response times. AI systems need monitoring for model accuracy, data drift, bias detection and business metric correlation. The monitoring infrastructure often becomes more complex than the AI model itself.

Deploying AI models requires thinking about model versioning, A/B testing different algorithms, gradual rollouts and rollback strategies. These are classic software deployment challenges with AI-specific constraints.

## **Making AI Systems Sufficiently Reliable and Safe**

Reliability in AI systems means designing for the fact that your model will be wrong a percentage of the time. This isn’t a bug to fix but a fundamental characteristic to engineer around.

Building voice training systems that work reliably in production call centers requires designing for network interruptions, audio quality variations and edge cases that training data never covered. The AI model is just one component in a larger system that is designed to handle real-world messiness.

> The good news is that if you can build reliable software systems, you already have most of the skills needed to build reliable AI systems.

AI safety isn’t just about preventing harmful outputs but about building systems where failures are observable, debuggable and recoverable. This requires the same systematic approach to error handling, logging and incident response that we use in traditional systems.

The companies winning with AI aren’t necessarily the ones with the best algorithms. They’re the ones applying decades of software engineering wisdom to a new problem domain. As AI becomes more prevalent, the competitive advantage will belong to teams that can bridge the gap between ML research and production engineering.

The good news is that if you can build reliable software systems, you already have most of the skills needed to build reliable AI systems. The challenge is recognizing that behind every successful AI product is a lot of really good, boring engineering.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/7b0d1da7-cropped-865ed64d-andrew-prosikhin-scaled-1-600x600.jpeg)

Andrew Prosikhin is the CEO and founder of Blobfish AI, a startup that uses voice AI to train call center operators. With over 10 years of experience as a software engineer specializing in generative AI, he has worked at leading...

Read more from Andrew Prosikhin](https://thenewstack.io/author/andrew-prosikhin/)