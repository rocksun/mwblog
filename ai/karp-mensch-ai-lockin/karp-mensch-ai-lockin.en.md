Palantir CEO Alex Karp went on CNBC’s *Squawk Box* last week to discuss a new partnership with Nvidia to deploy open-weight AI models in sovereign government environments. But viewers got a nearly 20-minute broadside against the entire frontier AI model industry, calling it “effing insane” and accusing companies like OpenAI and Anthropic of overcharging enterprises while harvesting their proprietary data.

Days later, Mistral CEO Arthur Mensch made a strikingly [similar case on LinkedIn](https://www.linkedin.com/posts/arthur-mensch_of-course-you-need-to-use-open-source-models-share-7479219202114002944-RlRk/), warning that closed AI providers are gaining “immense leverage” over enterprise customers as organizations connect proprietary workflows to hosted models. He suggests open-weight models, open data systems, and enterprises building their own training flywheels.

The two executives are approaching this from opposite ends of the market, yet their convergence on the same message within the same week underscores architectural control.

## **Two pitches, one argument**

Karp runs a company that sells an application and ontology layer designed to sit between enterprises and the models. The [Palantir-Nvidia deal](https://thenewstack.io/palantir-nvidia-sovereign-ai/) pairs Nvidia’s open Nemotron models with Palantir’s Sovereign AI Operating System, built on AIP, Foundry, Ontology, and Apollo, enabling government agencies and critical infrastructure operators to deploy, fine-tune, and audit AI models within their own air-gapped environments.

When CNBC’s Becky Quick told Karp he sounded angry, he pushed back, saying, “This is the voice of American business that is being channeled through me,” and urged the panelists to call any CEO privately to verify.

> “This is the voice of American business that is being channeled through me.”

Mensch’s company sells open-weight models, and he has a custom training platform called Forge, which frames the problem differently but reached the same conclusion. He argues in the post that closed providers have a track record of going after their most successful customers once they learn what those customers are building. His program runs from open models to open data stores, strict access controls, and a continuous training flywheel that improves systems on internal interactions.

## **Lock-in gets an upgrade**

If you’ve been building software at scale for any length of time, you already know that when new technology arrives, enterprises can’t help but rush to adopt it. But the dependency problem becomes impossible to ignore.

We saw the same problem with cloud computing when companies went all-in on a single hyperscaler’s proprietary services, only to later discover that the cost of switching providers could exceed the cost of staying, even when staying meant overpaying. It’s one of the reasons the industry spent years building abstraction layers, portability tooling, and multi-cloud strategies in response.

Foundation models are raising the same questions, but there’s a twist. When an enterprise connects a model to its internal data, including customer records, proprietary processes, and domain-specific knowledge, the dependency becomes informational. Karp’s argument is that model quality is converging across providers, but the operational leverage accrues to whoever controls the deployment layer and the data flowing through it.

Mensch’s claim has a concrete referent that enterprise architects will recognize. In 2025, Anthropic cut off model access to coding startup Windsurf while building its competing product, Claude Code. The Brookings Institution has separately warned that model providers increasingly compete with their own customers as they chase application-layer revenue.

## **When access disappears overnight**

When the U.S. government ordered Anthropic to suspend [access to its most advanced models](https://thenewstack.io/anthropic-claude-mythos-fable-5/) for foreign nationals, the company cut access across the board, including to enterprise customers in Europe who had built workflows on top of those models.

Access has since been restored, but for CIOs and enterprise architects who had treated model APIs as stable infrastructure, it was the same as if a cloud provider pulled compute resources without warning. It’s probably why the incident sent European policymakers into overdrive. Mensch, whose company had open-weight alternatives ready, seized the moment.

Enterprise teams need a plan for when a critical dependency is modified, repriced, or revoked by a provider whose incentives may not always align with their own.

> Enterprise teams need a plan for when a critical dependency is modified, repriced, or revoked by a provider whose incentives may not always align with their own.

## **Architecture shifts toward portability**

Enterprise AI architecture is now essentially this: don’t marry a single provider, build for portability, keep your most sensitive data and logic under your own control.

In practice, this is showing up in three ways.

Firstly, we’re seeing a portfolio [approach](https://thenewstack.io/agentic-ai-token-costs/)**.** A powerful closed model is maintained for complex reasoning and customer-facing work, while an open-weight model is used for repetitive, high-volume tasks. For businesses handling sensitive information, the appeal is that an open model can be run entirely on their own infrastructure, so data never has to leave the organization.

The second is the rise of the **model-routing layer**, abstraction frameworks that let organizations swap models without rewriting their applications. Palantir’s ontology pitch sits here as does the emerging crop of agent orchestration tools that treat the LLM as a pluggable component behind a standardized interface.

The third is the **open-weight movement itself**. Nvidia [shipped Nemotron 3 Ultra](https://blogs.nvidia.com/blog/palantir-secure-ai-us-agencies-nemotron-open-models/) in June under a permissive Linux Foundation license. Meta’s Llama continues to expand. Mistral’s Forge platform lets enterprises train custom models on their own data. And Mistral is [teasing an upcoming open-weight model](https://techcrunch.com/2026/07/04/what-is-mistral-ai-everything-to-know-about-the-openai-competitor/) this summer, with early access opening in July.

## **Follow the commercial incentives**

It would be naive to ignore the commercial interests at play. Karp’s Palantir sells the deployment and governance layer; it benefits directly if enterprises treat models as interchangeable commodities. Mensch’s Mistral sells open-weight models and a training platform, and it benefits directly if enterprises distrust closed providers. Zoho’s Sridhar Vembu, who endorsed Karp’s position publicly last week, has his own reasons for wanting enterprises to own their AI infrastructure rather than rent it from Silicon Valley.

But the fact that multiple executives across different market segments are saying companies need to own their data, maintain deployment flexibility, and not hand their competitive advantage to a provider who might become their competitor suggests the argument is resonating.

## **What developers should watch**

> If your most sensitive data is flowing through a third-party API with terms of service that can change, you’ve made a governance decision that your compliance team may not have fully evaluated.

For the engineering teams actually building on foundation models, the takeaway is that if your most sensitive data is flowing through a third-party API with terms of service that can change, you’ve made a governance decision that your compliance team may not have fully evaluated.

The engineering choice, to abstract the model layer, to evaluate open-weight options alongside closed APIs, to think about deployment portability the same way you think about cloud portability, is increasingly strategic.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)