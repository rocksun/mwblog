AI agents are already inside the enterprise, but the rules for controlling them haven’t caught up yet.

Some 86% of respondents in a survey released on Tuesday are already using AI agents embedded in applications, but just 12% said the risks addressed by sovereign AI are widely understood inside their organizations.

That’s a significant gap, as agents can now reach [beyond text generation to interact directly with company systems and data](https://thenewstack.io/go-language-ai-agents/). The [IDC survey](https://cohere.com/blog/the-state-of-sovereign-ai-adoption-in-2026) was commissioned by the [Canadian AI company Cohere](https://cohere.com/blog/state-of-sovereign-ai-adoption-2026).

“The main way this creates problems is in terms of observability and guardrails around who in an organization can access what info, including sensitive data,” a Cohere spokesperson tells *The New Stack* in response to questions about the research. “Any enterprise deploying AI and agentic systems wants to be able to monitor agent activity, to provide predictability in terms of both spend and security.”

For Cohere, that control [starts with the architecture underneath the agent](https://thenewstack.io/codex-async-developer-messaging/).

[Joelle Pineau](http://linkedin.com/in/joelle-pineau-371574141/), Cohere’s chief AI officer, tells *The New Stack* that “sovereignty is fundamentally an architectural question. If AI is tied to a single provider or governed by terms that can change, you don’t have control; you have dependency.”

## Agents outpace sovereignty awareness

IDC defines sovereign AI as the ability to exercise free choice and control over the design, development, deployment, accessibility, operation, maintenance, and governance of AI systems and applications, as well as the underlying technology they depend on.

> “Sovereignty is fundamentally an architectural question. If AI is tied to a single provider or governed by terms that can change, you don’t have control; you have dependency.”

The survey included 508 IT and business decision-makers responsible for AI purchasing decisions at organizations with more than $1 billion in annual revenue across the U.S., Canada, the U.K. and Germany. Respondents were screened for familiarity with AI and came from industries including healthcare, financial services, the public sector, energy, manufacturing, and telecommunications.

Only 13% said sovereign AI concepts were widely or very widely understood across their organizations, while one in three respondents had difficulty describing sovereign AI in their own words.

At the same time, AI adoption within this deliberately AI-aware sample is already high. Ninety-nine percent reported using generative AI, while 86% said they use agents embedded in applications.

Agent adoption is expected to advance considerably. Thirteen percent currently use prebuilt or third-party agents, but 67% expect to do so within the next 12 months. Internally developed agents are expected to jump from 5% to 44% over the same period.

Cohere said the sample was intentionally designed to focus on large enterprises already engaged with AI to determine whether gaps around sovereign AI remained among organizations already investing in the technology.

## What does a sovereign AI stack actually look like?

The company tells *The New Stack* that customers can run its complete platform, including its models, retrieval-augmented generation and North’s agents and tool use, on their own infrastructure without any external connection. That includes fully air-gapped and classified environments.

“Licensing is offline, with no phone-home requirement,” the company tells *The New Stack.* “Updates, patches, and new model versions arrive as signed packages the customer transfers in through their own approved process and validates before deploying. Changes in the environment are initiated only through client action.”

That means an outside AI provider can’t simply push a new model or software update into the environment. The customer determines what enters it and when.

[Nick Frosst](https://www.linkedin.com/in/nick-frosst-19b80463/), Cohere’s co-founder, argues that this becomes particularly important when AI is embedded deeply enough in an organization that losing access would disrupt other systems.

“As sovereign AI becomes more widely adopted, we need to be clear about what it actually means,” Frosst tells *The New Stack*. “Sovereignty is about control, the ability to build and run your AI exactly the way you want.”

“With model access restrictions and rising cybersecurity risks, organizations are seeing the cost of relying solely on hegemonic big tech providers,” he continued. “If access changes, your entire stack can be disrupted, and that is not a foundation you can build on.”

Cohere’s proposed alternative is an agentic platform that can operate within the customer’s own environment, including sensitive data, without ever leaving it.

> “With model access restrictions and rising cybersecurity risks, organizations are seeing the cost of relying solely on hegemonic big tech providers. If access changes, your entire stack can be disrupted, and that is not a foundation you can build on.”

## More control means more responsibility

There is a trade-off to taking that control back.

In an air-gapped Cohere deployment, updates, patches, and new model versions don’t simply arrive as they would with a hosted AI service. Cohere signs and packages them, but the customer is responsible for transferring them into the environment, validating them and deciding when to deploy them.

That’s part of what makes the system sovereign. It also shifts work that would otherwise fall to the AI provider back to the enterprise.

IDC’s findings suggest that some organizations are already struggling with the infrastructure and expertise required to make that shift. When respondents were asked for their single biggest barrier to sovereign AI readiness, infrastructure was the most common response at 17%. Skills and talent accounted for another 9%, while cost and budget accounted for 10%.

The survey doesn’t measure whether sovereign deployments actually lag hosted frontier models in capability, so it can’t answer how significant that trade-off becomes in practice.

## Data fears overshadow agent risks

Of the 508 organizations surveyed, 420 already have someone responsible for sovereign AI, but few have clearly defined what that responsibility actually involves. Only 8% said those roles were well-defined, while just 0.4% said they were fully formalized and governed.

Cohere said those results came from separate questions: Respondents were first asked whether someone owned sovereign AI requirements, then how clearly that responsibility had been defined.

“Organizations are assigning ownership faster than they’re formalizing it, so accountability often sits with individuals rather than organizational structures,” the company tells *The New Stack*.

Among organizations with dedicated sovereign AI responsibility, the chief AI officer or head of AI leads in 51.7% of cases, followed by the CIO or CTO at 36.9%.

Germany stands apart, with CIOs and CTOs leading 70% of sovereign AI initiatives among respondents with dedicated ownership, compared with 24% in the U.S., 33% in the U.K. and 32% in Canada.

Line-of-business and IT leaders also have different priorities. Business leaders put more emphasis on data security and privacy, while IT leaders focused more heavily on regulatory compliance and meeting national or regional requirements.

> “Organizations are assigning ownership faster than they’re formalizing it, so accountability often sits with individuals rather than organizational structures.”

## Enterprises are still worried more about data than agent actions

That difference in priorities becomes especially interesting when looking at what respondents actually fear about generative and agentic AI.

IDC asked respondents to rank their top three concerns. Data leakage or privacy breaches led by a wide margin, selected by 76%, followed by compliance, regulatory, or legal risks at 59%.

Only 24% selected improper or unintended autonomous actions by AI agents.

The survey doesn’t explain why autonomous actions rank so much lower, and it would be a stretch to conclude that enterprises aren’t aware of the risk. But the results show that their concerns remain heavily centered on data even as agent adoption accelerates.

An agent introduces a different set of control questions than a model that only responds to prompts. It may be able to retrieve internal information, call APIs, invoke tools, or take actions inside another application.

Keeping that agent inside an organization’s infrastructure can determine where its data goes and who controls the underlying system. It doesn’t, by itself, determine what the agent should be allowed to do once it’s there.

## Control beyond model deployment

Cohere argues that [keeping AI inside an organization’s own environment](https://thenewstack.io/manus-meta-data-deletion/) is only part of the equation. Enterprises still need to control what agents can access and see what they do once they start taking action.

Pineau said those controls need to be built into the system from the start.

“Control has to be engineered into the system itself: how the model is built, how it’s sized, and how it’s deployed,” she said. “This research reflects what we hear from customers every day: a growing demand for real ownership across the AI stack.”

“True sovereignty requires a platform where privacy, security, and deployment choice are defaults, not add-ons,” Pineau added. “That is the standard we build for at Cohere.”

Cohere has a stake in that argument. The company commissioned the IDC research, and private deployment is a central part of how it positions its models and North agentic platform.

Still, the problem goes beyond Cohere. Organizations in the survey are already deploying agents and expect to use many more over the next year, while the rules and responsibilities around those systems are still catching up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)