**Ask a general-purpose language model to summarize a contract,** and it will probably do a reasonable job. Ask it to calculate what a company owes a supplier, accounting for three amendments, a revised pricing schedule, and an internal procurement policy, and it’s a different story.

Enterprise AI agents need to know more than what’s written in a document. They need context about which contracts belong together, which terms still apply, and when a decision needs human approval.

It’s a problem Docusign is tackling as it expands beyond electronic signatures into an [Intelligent Agreement Management (IAM)](https://www.docusign.com/intelligent-agreement-management?utm_source=thenewstack&utm_medium=content&utm_campaign=NAM_US_COM_AWA_2610_FY27Q3GEOIAMContent) platform.. [Introduced in April 2024](https://www.docusign.com/blog/new-docusign-intelligent-agreement-management) and available in the U.S. to customers that May, the IAM platform helps organizations create, commit to and manage agreements.

![](https://cdn.thenewstack.io/media/2026/10/5e11eb07-docusign-cto.jpeg)

*Docusign CTO Sagnik Nandy*

At the center of that effort is [Docusign Iris](https://www.docusign.com/blog/docusign-iris-agreement-ai), the contract AI engine that powers Docusign IAM and its AI features across the agreement lifecycle. It combines Docusign’s contract management expertise, agreement-centric data, and AI models to help teams surface insights and take action across contract workflows.

“General LLMs are great. It’s just that you need more around it to really unleash its full power,” [Sagnik Nandy](https://www.linkedin.com/in/sagnik-nandy), Docusign’s chief technology officer, tells *The New Stack*.

> “Context is one of the things that really differentiates a generic solution from a solution that speaks your language.”

“Context is one of the things that really differentiates a generic solution from a solution that speaks your language.”

## **Four kinds of context**

Nandy breaks context into four categories: within-agreement, cross-agreement, organizational, and user.

In Nandy’s account, the first is relatively straightforward: following a term defined on page two and referenced again on page 20 of the same contract. When that term appears across several contracts and amendments, working out which version applies becomes harder.

> “…To an LLM, they look like three or four independent PDF files.”

“Imagine you have a single agreement that’s gone through two or three amendments, or a price change. To an LLM, they look like three or four independent PDF files,” Nandy explains.

In practice, those documents form a single contractual relationship. If someone asks about pricing, the system needs to identify the terms currently in force, not simply retrieve every price mentioned.

“You really have to bring them together. You need custom logic to even group them the right way,” he says.

That requires recognizing relationships between documents and understanding how amendments change the original terms. Retrieval alone isn’t enough to establish which version of a clause applies.

An AI contract agent also needs to understand the company’s internal policies. Legal might have a playbook spelling out which terms it will accept, while procurement and sales have different rules about who can approve what. Without that information, the agent wouldn’t know whether a contract meets the company’s requirements or needs sign-off.

The fourth category is user context, including someone’s language preferences, previous questions, and feedback.

According to Nandy, general-purpose LLMs may handle much of the first category, but the other three are considerably harder.

## **Building agreement intelligence**

Iris combines several [AI contracting capabilities](https://www.docusign.com/products/platform/ai) rather than relying on a language model to do everything.

“Iris has a lot of pieces to it. It has everything from intelligent extractions. It has semantic search. It has a rich agentic layer. It has the ability to build agents. It has rich context,” Nandy says.

Finding a renewal date is one thing. Knowing whether the contract needs attention, based on its history and the company’s rules, is another.

Iris uses extraction to identify contract information, semantic search to find relevant agreements, and agreement-specific logic to connect contracts, amendments, and parties. Agents can then use that information to carry out tasks.

Consider a procurement manager asking which software contracts worth more than $1 million are due for renewal in the next three months.

Nandy says answering that question often previously involved multiple people gathering information, consolidating spreadsheets, and reconciling supplier names that appeared differently across agreements.

Iris can help find those contracts, identify upcoming obligations, and check agreements against organizational playbooks. It can also flag issues that might need attention before renewal.

Even a question about payment obligations to a particular supplier involves several steps. Iris needs to recognize the supplier as a company, find its agreements, account for amendments, and establish how the obligations have changed.

“While it seems like a straightforward question, to make it truly happen, you need rich search functionality. You need a repository,” Nandy says.

“You need this context of how these agreements are combined to create single entities, and then you need to make the search give the answer and the ability to iterate.”

> “The beauty is to hide the complexity and make it look easy to the end user. But there’s a lot going on behind it.”

He estimates that answering such a question could involve five or six tools, drawing on Docusign’s contract-specific data and bringing the results together. “The beauty is to hide the complexity and make it look easy to the end user. But there’s a lot going on behind it.”

## **Knowing when to involve a human**

Giving agents more context raises another question: how much should they be allowed to do?

Docusign combines agentic capabilities with business rules and approval processes, letting organizations decide which parts of a contract workflow to automate and where people remain in control.

For smaller renewals below a company’s spending threshold, an Iris-powered agent could gather and assess the agreement information, while a configured workflow applies the routing and approval rules. Higher-value contracts, or those with exceptions, could go to a person for review.

Nandy describes how “renewals below a certain threshold” might follow standard procedures, while more expensive or sensitive agreements would bring a person into the process.

Getting that wrong could mean approving terms that should have gone to legal, or overlooking obligations buried in an earlier agreement.

Docusign’s ready-to-deploy agents can be invoked through the Iris AI assistant in a chat experience or used as steps in Workflow Builder to retrieve agreement information, apply playbooks and monitor obligations.

Teams can also create custom AI contract agents in Docusign Agent Studio. [Workflow Builder combines agent reasoning with rule-based routing and approvals](https://www.docusign.com/blog/developers/developers-guide-docusign-iris-agentic-capabilities); the agent returns a result, and the workflow uses it to determine the next step. Availability varies by plan, region and language; Docusign currently lists the assistant and Agent Studio agents as part of eligible IAM plans in North America data centers, in English.

## **From documents to business decisions**

Electronic signatures address one part of the contract process, but much of the work happens before and after signing.

Nandy splits the agreement lifecycle into three stages: creating an agreement, committing to it and managing it afterward.

For a new contract, that could mean knowing which templates to use and which terms the company typically agrees to. If negotiations lead to changes, the agent needs to check previous agreements and work out who has to approve them. Once the contract is signed, it should help teams track what they’ve agreed to and when the deal comes up for renewal.

Some Docusign customers are reporting improvements from bringing agreement information into their business processes, although those results aren’t necessarily attributable to autonomous agents.

In its [2026 Customer Awards](https://www.docusign.com/blog/docusign-customer-awards-2026), Docusign reports that Experian cut contract cycle times from roughly 10 days to hours and made contract data easier to access and understand by connecting Docusign with its configure-price-quote (CPQ) solution.

For developers building enterprise contract AI agents, Nandy’s examples show why the language model is only part of the job. The system also needs reliable contract data, a way to connect related documents, an understanding of company rules, and clear limits on what it can do without approval.

Reading a contract is relatively easy. Knowing what it means for the business is where the real engineering work begins.

### More Docusign in *The New Stack*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)