I’ve spent most of my career believing that technical sophistication was the key to solving complex problems. As an AI founder turned AI product leader, I was convinced that the most advanced model, the most intricate architecture, would always win. But my experience scaling AI solutions at [Apollo.io](https://www.apollo.io/) taught me a radically different lesson: The most critical factor in AI success isn’t technology — it’s a deep understanding of the human workflow you want to augment with AI.

My career path began in the trenches of outbound sales, watching teams struggle with hours of manual research and outreach tasks. Sales professionals were drowning in data but lacking meaningful connections. Traditional automation tools felt like blunt instruments: fast, but fundamentally disconnected from the nuanced art of human communication.

After growing Apollo’s AI functionality to 54,000 weekly active users (a 5x increase in 2024), our team made a surprising discovery. The success of our AI implementation had little to do with which models we selected or the sophistication of our architecture. Instead, the determining factors were our organizational structure, evaluation methodologies and integration of domain expertise from sales professionals.

## **The Quality Evaluation Infrastructure Gap**

The most surprising reality we uncovered during our AI journey? Building successful AI applications requires an evaluation infrastructure that most teams completely overlook.

Like many teams, we started by shipping on vibes: If it looked good in testing, we shipped it. This approach inevitably fails once you scale beyond internal users or early adopters. At Apollo, we developed a four-dimension scoring system, evaluating each AI output on:

* **Accuracy:** Does it align with verified information?
* **Relevance:** Does it address the specific use case?
* **Clarity:** Is it concise and understandable?
* **Tone:** Does it match the appropriate communication style?

Each dimension is scored on a 1-3 scale by domain experts. Nothing ships without hitting a minimum composite score of 2.5/3. This evaluation framework became our competitive advantage, ensuring consistent quality as we scaled from hundreds to tens of thousands of users.

## **The Organizational Pattern That Works: Domain Experts Lead, Engineers Support**

Through painful iteration, we discovered a counterintuitive truth: Engineers are the wrong people to write prompts, despite their technical expertise with AI systems.

[Machine learning](https://thenewstack.io/category/machine-learning/) (ML) engineers excel at system architecture and API integrations but struggle with capturing domain-specific knowledge in prompts. The magic happens when subject matter experts lead prompt creation.

This insight led us to create a dedicated “prompt writer” role filled by domain experts in sales rather than engineers. User satisfaction jumped 1.34x after this organizational shift.

The hybrid team structure that proved most effective for us:

|  |  |
| --- | --- |
| **Role** | **Primary Responsibility** |
| Engineers | Infrastructure, APIs, monitoring |
| Prompt Writers | Domain-specific prompt creation |
| Quality Team | Evaluation frameworks and metrics |
| Domain Specialists | Real-world testing and annotation |

## **The User Experience Challenge: Trust Through Transparency**

Despite what technical leaders might hope, users don’t trust AI systems by default. When our initial AI product required prompt engineering skills, adoption stalled completely.

We realized that AI adoption follows a trust curve, not a capability curve. Users need to verify outputs before they’ll rely on them.

We rebuilt with:

1. Plain English prompting
2. Source citation for all claims
3. Confidence indicators for outputs
4. One-click manual override options

These changes led to 3x growth in weekly active users, not because the underlying AI capabilities improved, but because the interface created trust.

## **Implementation Learnings: Three Patterns for Success**

After scaling our AI platform to 54,000 weekly active users and working with hundreds of companies implementing AI, we’ve identified three consistent patterns that differentiate successful implementations:

**Earn the right to automate.** Most engineering teams rush to build fully autonomous AI systems, but our data shows users consistently prefer having manual review options. When we implemented one-click override mechanisms and confidence indicators, user adoption increased 3x. Build trust mechanisms first, then gradually increase automation as user confidence grows.

**Prioritize domain expertise over technical sophistication.** The alpha in AI product building isn’t found by adopting the latest agent framework or [large language model](https://thenewstack.io/llm/) (LLM) — it comes from having subject matter experts imbue best practices into your system. Our blind model testing revealed that Claude Haiku 3.5 consistently outperformed much larger models for our specific sales use cases, despite being faster and cheaper. The model matters less than how well your team understands the problem domain.

**Operationalize your definition of quality.** Most teams use subjective “vibes” to evaluate AI outputs early on, but this approach collapses at scale. By implementing our four-dimension scoring system (accuracy, relevance, clarity, tone) with specific thresholds (2.5/3 minimum), we created an objective quality framework that enabled consistent results even as our user base grew by 5x. Without quantifiable quality metrics, AI products inevitably drift toward inconsistency.

## **What’s Next for AI Engineering Teams**

The emerging reality? AI implementation isn’t failing because of technical limitations, but because organizations haven’t structured their teams to bridge the gap between capabilities and domain expertise.

The next wave of successful AI products won’t be built by teams racing to implement the latest model architecture. They’ll be built by teams that create the right organizational structure, evaluation frameworks and trust mechanisms to deliver consistent value at scale.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/7ff46a33-tyler-phillips-600x600.jpeg)

Tyler Phillips is a seasoned product leader who specializes in going zero-to-one and scaling AI products for GTM teams. As a Principal Product Manager at Apollo.io, a $1.6B AI-powered sales platform, he is developing Apollo’s AI Sales Assistant and AI...

Read more from Tyler Phillips](https://thenewstack.io/author/tyler-phillips/)