**Someone moves off the finance team at 9 a.m. on a Monday.** Your sync runs nightly at 2 a.m. For seventeen hours, that person can still pull finance documents out of your retrieval index, and nothing in the system knows it is wrong. I am [borrowing the example from Truto](https://truto.one/blog/how-to-maintain-document-level-rbac-in-enterprise-rag-pipelines/), but every team I talk to recognizes some version of it.

That is the version with a clock on it. The version people ask about in security review sounds different. The retrieval pilot works, the demo lands, the executive sponsor is happy, and then someone asks how you guarantee this thing will never summarize the CEO’s compensation review for an intern who asked an innocent question about salary bands.

Most teams do not have an answer. What they have is a filter.

I think the answer has to be structural. Permissions are not a filter you apply to context after you have assembled it. They are a property of how context gets assembled for a particular identity, because assembly is the last moment where refusing to include something still means the model never saw it.

> Permissions are not a filter you apply to context after you have assembled it.

The major platform vendors in this race are building some version of the same step, and nobody has really settled on a name for it. I run a company, Modus, that builds in this lane, so weigh the argument accordingly. In our product, we call it context composition. For this piece, I will call it context assembly. It is where a system decides which pieces of enterprise knowledge to hand a model for a specific person, in a specific moment, for a specific question. Everything upstream is storage, and everything downstream is inference. Assembly is where identity either lives or doesn’t.

## **Announced is not the same as shipped**

The reason to argue about this in September rather than in June is that platform vendors have stopped disagreeing about where the step goes, and the software most companies run has not caught up with them.

AWS made the most explicit version of the case in June, [announcing AWS Context](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/) at its New York Summit, [covered here at the time](https://thenewstack.io/aws-context-knowledge-graph-agents/). The design decision underneath it is the interesting part. The graph is governed by the same permissions as the lake through Glue [Data Catalog, SageMaker Unified Studio, and Lake Formation](https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/), and identity is checked again when someone asks. The people who would govern it are the ones already governing everything else, with the column-[, row-, and cell-level policies](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) that S3 object permissions alone can’t provide.

It is worth being precise about the tense, because the retelling has already blurred it. Every call is [“designed to inherit the calling user’s IAM and Lake Formation permissions, so an agent can only see and traverse the relationships its identity is authorized to access.”](https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/) Designed to. That is a roadmap language, and nearly three months later, AWS Context is still listed as coming soon, with no GA date, no regional list, and no pricing. [Amazon Bedrock Managed Knowledge Base](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-managed-knowledge-base/) did go generally available that day, which is most of why the two get conflated.

> Microsoft shipped identity-aware retrieval on June 16. AWS announced it on June 17, and you still cannot buy it.

The day before AWS announced Context, Microsoft’s[Work IQ API became generally available](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability). It runs [in the context of the signed-in user, honors Microsoft 365 permissions](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/work-iq), is billable through Copilot Credits, and an administrator can switch it on today. Two announcements one day apart, the same architectural position, and only one of them is something you can put in production.

Databricks reached the same slot from the other direction, [extending Unity Catalog to the agent](https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026). However,h partners in that ecosystem note that the protection is anchored to the Databricks Runtime rather than to the data, so it stops applying when a BI tool or an MCP server reaches the same source directly.

Teams did not wait for any of this. They shipped the flat-index version while the identity-aware version stayed on the slide.

The direction is consistent, and so is the limit. Each of those controls is strongest inside the system that issues it. The interesting problem begins when an agent needs context that crosses several of those systems at once, and that is the job assembly has to solve.

## **The lake is not the business**

Lake Formation enforces fine-grained permissions inside the lake it governs, and it does that well. Those permissions do not become the sharing rules in Salesforce, Slack, Google Drive, or Confluence.

AWS documents where its own boundaries sit. Its August [guidance on propagating user authorization context through AgentCore](https://aws.amazon.com/blogs/security/propagate-user-authorization-context-in-ai-agents-with-amazon-bedrock-agentcore/) walks through handing Salesforce a token scoped to the actual user, so Salesforce applies its own sharing rules. In AWS’s words, “the agent acts as an orchestrator, not a gatekeeper,” and “downstream services enforce authorization.”

That is a reasonable call. It is also an important product boundary. Lake Formation is not integrating with Salesforce, GitHub, Jira, Slack, Confluence, or Google Drive. Each of those decides who sees what on its own terms, or nobody does.

The most useful line is about the filter itself. In that same security post, AWS states plainly that [“metadata filtering is application-layer enforcement. The bedrock:Retrieve API doesn’t expose metadata filter content as an IAM condition key.”](https://aws.amazon.com/blogs/security/propagate-user-authorization-context-in-ai-agents-with-amazon-bedrock-agentcore/) I keep coming back to that sentence because it is a vendor calmly telling you where its guarantee ends and yours begins.

The same is true of your own stack. The tags on your chunks are not an identity boundary. They are a hint that your application code is trusted to honor.

## **What breaks when authorization arrives too late**

The failure is structural, which is why I keep running into the same few versions of it.

I want to be careful here. “Filters are bad” is not the argument. The problem is ordering. A retrieval system can search a mixed index, retrieve opaque IDs, authorize them, and hydrate only the documents the person is allowed to read. That is a filter, and it is fine, because nothing unauthorized ever left the retrieval boundary.

The version I see more often runs the check after the documents have already been fetched. Once restricted text has been hydrated, reranked, summarized, or cached outside that boundary, authorization is chasing the problem instead of preventing it. AWS’s own guidance calls the broad-credential version of this a single point of failure because a prompt injection or a bug in the filtering logic can expose the whole dataset. And if it reached a model, the model has already read something the person was never entitled to retrieve, with any bug or injected instruction in that window free to act on it.

The defense most teams reach for first can make things worse. Jiale Liu, Jiahao Zhang, and Suhang Wang at Penn State [red-teamed graph-based retrieval](https://aclanthology.org/2026.findings-acl.899/) and found that summarization reduces leakage in untargeted attacks but can increase it in targeted attacks. My read of why is that summarizing preserves the salient detail, and the salient detail is usually the sensitive one. A separate [2026 preprint](https://arxiv.org/abs/2602.08668) found cross-tenant leakage in pipelines that hand off from vector search to a graph, and eliminated it by re-checking authorization at every hop. Two individually secure components can still compose an insecure system when no one re-checks authorization at the transition between them.

> Two individually secure components can still compose an insecure system when no one re-checks authorization at the transition between them.

The seventeen-hour window at the top of this piece is the same failure in slower motion. Direct shares, nested groups, and public links all change independently, which is why Google built [Zanzibar](https://www.usenix.org/conference/atc19/presentation/pang) as a relationship model rather than a list. A list of allowed users stamped on each chunk is a snapshot of a graph that moved without telling you.

None of this is fringe anymore. The [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf) moved sensitive information disclosure from sixth place to second in its 2025 revision and added [LLM08, Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/), which names the risk of context leaking between users who share a vector database and recommends a permission-aware store as the fix.

The enterprise-scale version of this is Copilot. In the first year of its enterprise rollout, a 2024 Gartner survey of 132 IT leaders found that oversharing [led 40 percent to delay Microsoft 365 Copilot rollouts](https://www.computerworld.com/article/3542000/microsoft-365-copilot-rollouts-slowed-by-data-security-roi-concerns.html) by 3 months or more. What makes that example useful is that Copilot is not the one doing the wrong thing. Microsoft checks the user’s permissions at query time, and its own documentation says results are [trimmed to content the signed-in user has permission to access](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-apis-security-authentication). Copilot surfaces what those people were already allowed to open.

> A surprising amount of enterprise data stays private mainly because it is hard to find, and retrieval is very good at finding things.

The exposure was sitting there the whole time. A surprising amount of enterprise data stays private mainly because it is hard to find, and retrieval is very good at finding things.

## **Where identity has to arrive**

So the lesson from Copilot is that resolving identity at assembly is necessary and not sufficient. Assembly inherits whatever the permission graph actually says. If the graph is wrong, stale, or too broad, the retrieval system will faithfully enforce the wrong answer. Homegrown retrieval can inherit the same problem, often with less governance tooling.

That does not weaken the case for assembly. It locates it. Assembly is not what makes your permissions correct. It is the last place where correct permissions still matter, because after that point the model has read the document.

I am not claiming to have invented this. AWS is arguing a version of it by governing the graph with the permissions the lake already has. OWASP got to the same place from the security side, and its recommended fix for LLM08 is a store that knows who is asking rather than a check that runs after the fact.

The part I would add comes from watching enterprise products make the jump from pilot to production. Teams can postpone many architectural decisions during a demo. They cannot postpone this one for very long. Eventually somebody asks who can see what, who guarantees it, how quickly a permission change propagates, and who owns the answer when three different systems disagree. That is often the moment when an impressive AI pilot turns into a security project, and it usually starts with something like an intern’s question.

So there are four questions I would put to any team building this.

1. Whether identity gets resolved at assembly or after retrieval.
2. How much of your context lives outside the lake, in chat and tickets and docs, where IAM does not reach.
3. What your worst-case staleness window looks like when someone changes teams.
4. And whether you can re-check authorization at every step along the way, or only once at the door.

If those answers are uncomfortable, that is useful. I have not had many of these conversations where they weren’t.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/6499bc61-cropped-7ffccf0f-daniel-shimoni-600x600.png)

Daniel Shimoni is the CEO of Modus, the Context Warehouse for enterprise AI.

Read more from Daniel Shimoni](https://thenewstack.io/author/daniel-shimoni/)