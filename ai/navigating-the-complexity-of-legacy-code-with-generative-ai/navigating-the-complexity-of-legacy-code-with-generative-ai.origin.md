# Navigating the Complexity of Legacy Code with Generative AI
![Featued image for: Navigating the Complexity of Legacy Code with Generative AI](https://cdn.thenewstack.io/media/2024/12/f91d08d3-legacy-1024x576.jpg)
It’s no secret that the software industry grapples with a higher employee turnover rate compared to other industries. A 2022 LinkedIn [analysis](https://www.linkedin.com/business/talent/blog/talent-strategy/industries-with-the-highest-turnover-rates) of its global user data found that technology companies experienced employee turnover rates of 12.9% percent, compared to an average turnover rate for all industries of 10.6%.

While this might seem volatile to outsiders, those within tech recognize it as a natural byproduct of an industry defined by constant change and adaptation. Workers often prioritize opportunities to engage with cutting-edge technologies or roles offering greater flexibility. Meanwhile, companies adjust workforce strategies to remain agile, competitive and responsive to evolving business priorities.

This churn often leaves teams grappling with legacy code: [work that remains unfinished or inadequately documented](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) once developers depart. The software developer tasked with picking up months or even a year later where their colleague left off faces a most daunting challenge.

When legacy code is inherited, developers rely on documentation and inline comments to understand its intended purpose. When these are missing or incomplete, they may spend an excessive amount of time deciphering or even reverse-engineering the code. Over time, the effects compound. Institutional knowledge dissipates. Backlogs become disproportionately weighted toward [fixing technical debt](https://thenewstack.io/how-to-persuade-your-organization-to-pay-down-technical-debt/) instead of building new features. Frustration sets in.

SAP’s experience with this phenomenon offers a uniquely international perspective. Some of the company’s core business logic was written in the late 20th century, back when its development organization was centralized in its German headquarters. It was common at the time for business objects and technical constructs to be named in German: BUKRS for *Buchungskreis* (company code), GJAHR for *Geschäftsjahr* (fiscal year), and EKPO for *Einkaufspositionsdaten* (purchasing document item).

As the company [evolved its workforce internationally](https://www.sap.com/canada/about/company.html) to over 107,000 employees across more than 157 countries, this became one of many examples highlighting how legacy systems can inadvertently complicate modern workflows.

**Artificial Intelligence as a Game Changer**
Lately, SAP has joined many other tech companies in looking to generative AI as a strong potential remedy for managing legacy code. This confidence stems from the architecture, design principles and training methodologies underpinning [large language models (LLMs)](https://thenewstack.io/llm/). While originally designed to process human language, these models are highly effective in understanding code syntax and structure, as well as in inferring the underlying intent and context.

Trained on vast data sets of code, technical documentation and natural language, LLMs can identify patterns and conventions that are often implicit within legacy codebases. They excel at analyzing both individual lines of code and broader system interactions. This helps them map dependencies and reveal critical relationships. Their ability to contextualize extends beyond syntax, equipping them to infer domain-specific business logic and intent, even in poorly documented systems.

For developers, this means generative AI can provide natural language explanations for obscure functions and even [suggest ways to optimize refactored code](https://thenewstack.io/how-to-use-self-healing-code-to-reduce-technical-debt/). By bridging gaps in institutional knowledge, it can reduce the time and effort required to update legacy code. More importantly, it helps [development teams move quickly beyond maintaining older systems](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/), accelerating innovation and delivering greater value.

SAP has trained [Joule](https://thenewstack.io/ai-agents-and-co-pilots-sap-introduces-deeper-integrations/), its generative AI copilot, on its cloud development model and on ABAP, its proprietary programming language. In 2025, Joule developer capabilities will be seamlessly integrated into the ABAP Development Tools plugin within the Eclipse integrated development environment. Similarly, generative AI capabilities available through Joule have been added to SAP Build, a unified application development and automation solution combining low-code and pro-code tools.

From a developer’s perspective, a new modular window will let them chat directly with Joule throughout the course of their work. Code explanations can be generated as easily as directly asking what a specific function, method or business object does. Alternatively, [developers can request a detailed explanation of a block of legacy code](https://thenewstack.io/the-machine-learning-building-blocks-developers-require-to-do-mlops/) that was copied and pasted into the Joule chat window. Developers can also generate RESTful business objects, services and unit tests for classes and views.

The challenges of turnover and legacy code have long weighed heavily on the software industry, demanding time and resources that could otherwise fuel innovation. The introduction of generative AI marks a turning point, offering a practical, scalable way to bridge knowledge gaps and maintain development momentum. As solutions like SAP Build continue to evolve, they promise not just to resolve today’s [challenges but also redefine how software teams build](https://thenewstack.io/a-quantum-challenge-building-a-skilled-workforce/), innovate and thrive in an ever-changing environment.

Visit our [website](https://www.sap.com/canada/products/technology-platform/build/trial.html) to start your own free trial of SAP Build.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)