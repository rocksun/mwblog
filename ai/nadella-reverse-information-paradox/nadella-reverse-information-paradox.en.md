Microsoft Chairman and CEO Satya Nadella took to the internet to share his thoughts about the hidden cost of enterprise AI.

In a lengthy post on X (formerly Twitter) on Sunday, Nadella describes the problem as a “reverse information paradox,” arguing that AI flips Nobel Prize-winning economist Kenneth Arrow’s classic information paradox on its head.

Arrow’s paradox focused on the seller’s dilemma of how to demonstrate the value of information without disclosing it. Nadella argues enterprise AI shifts that burden to the buyer, who must share proprietary processes and institutional expertise to get the strongest results from a model.

“You essentially pay for intelligence twice, once with money, and again with something even more valuable: the proprietary knowledge you must reveal to make that intelligence useful,” he writes. “The better you want the model to perform, the more of that knowledge you have to feed it.”

> “You essentially pay for intelligence twice, once with money, and again with something even more valuable: the proprietary knowledge you must reveal to make that intelligence useful.”

## When “exhaust” becomes a competitive advantage

According to Nadella, every engagement with an enterprise AI system generates what he describes as “exhaust” that gradually captures how an organization operates.

“Every correction is distilled into institutional know-how,” Nadella writes. “It’s the kind of knowledge a competitor could never buy, and the kind that leaks almost imperceptibly: trace by trace, correction by correction, eval by eval.”

> > “Every correction is distilled into institutional know-how. It’s the kind of knowledge a competitor could never buy, and the kind that leaks almost imperceptibly: trace by trace, correction by correction, eval by eval.”

Over time, those thousands of interactions create an internal corpus of organizational knowledge that may be more valuable than the original documents that seeded the system. The more employees use AI, the more an organization’s expertise becomes embedded in how those systems operate.

## Redefining the trust boundary

In practice, those troves of knowledge could push enterprises toward model-agnostic AI stacks in which prompts and memory stores remain under their control — even as the underlying foundation model changes.

In his post, Nadella also took aim at current AI business practices, arguing that model providers claim broad rights to learn from public data while limiting how customers can reuse or build on the knowledge created inside their own organizations.

Some observers may see an irony in the argument coming from Microsoft’s CEO. Nadella warns that enterprises risk losing valuable organizational knowledge to AI systems, yet Microsoft sells Copilot, a product whose value depends in part on wide access to enterprise data. Copilot works by traversing Microsoft Graph, allowing it to reason over documents, emails, chats, and other information that a user is already authorized to access.

Security researchers have raised concerns about the amount of sensitive information such systems can expose if organizations have overly permissive access controls. [Research from Concentric AI](https://www.techradar.com/pro/microsoft-copilot-has-access-to-three-million-sensitive-data-records-per-organization-wide-ranging-ai-survey-finds-heres-why-it-matters) showed that Copilot accessed nearly three million confidential records per organization during the first half of 2025, while [EPC Group audits](https://www.myworkdrive.com/blog/microsoft-365-copilot-oversharing) found that roughly 80% of enterprise Microsoft 365 tenants had significant oversharing risks, including salary information, merger documents, and customer data that could be surfaced through Copilot. The [U.S. House of Representatives also banned staff — but later reversed that ban — from using Copilot](https://www.reuters.com/technology/us-congress-bans-staff-use-microsofts-ai-copilot-axios-reports-2024-03-29/) over data security concerns.

## The Microsoft distinction

Microsoft, however, draws a distinction between *accessing* enterprise data to answer user requests and *using* that data to train foundation models. The company says information retrieved through Microsoft Graph is [not used to train its AI models](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection), and that Copilot [respects existing permissions, identity controls, and sensitivity labels](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy).

Still, the commercial strategy here is hiding in plain sight: Nadella’s Sunday “[reverse information paradox](https://x.com/satyanadella/status/2076323181154230284?s=46)” post is effectively a roadmap to Azure. Everything Nadella recommends building runs on cloud infrastructure. Essentially, enterprises can swap out the foundation model, but they’re not going to swap out the cloud.

## Owning your AI learning loop

To counter the perceived shift toward giving over information to frontier labs, Nadella outlined several priorities for enterprise AI architecture. Among his recommendations:

* Keeping organizational memory inside the enterprise tenant.
* Building private evaluation and learning systems.
* Decoupling orchestration layers from any single foundation model.
* Preserving the ability to switch models without losing accumulated organizational knowledge.

Taken together, Nadella’s argument comes back to the idea that enterprises should own their learning loop rather than handing pieces of it to the companies that provide their AI models.

Nadella reinforced that idea by quoting Palantir CEO Alex Karp, [who has similarly argued](https://thenewstack.io/karp-mensch-ai-lockin/) that enterprises want complete ownership over their AI infrastructure.

## Model-agnostic orchestration emerges

In the end, by maintaining control over their means of production, enterprises can finally ensure that when they invest in AI, the compounding value stays inside the business where it belongs. Tools like LangChain and Haystack are gaining traction specifically because they let engineering teams treat foundation models as plug-and-play commodities, rather than hardcoded dependencies.

“What the technical customers want is control over their compute, their models, their data stack, and their alpha,” Nadella quoted Karp. “They want to know they own the means of production, and it’s not being transferred to someone else.”

> “They want to know they own the means of production, and it’s not being transferred to someone else.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)