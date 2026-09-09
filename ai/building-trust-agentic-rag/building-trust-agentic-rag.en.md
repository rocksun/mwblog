Basic retrieval-augmented generation (RAG) follows a straightforward pattern. A user asks a question, the system finds relevant content in a knowledge base, and the model uses it to ground its answer. This works for simple lookups, but many real-world [retrieval systems](https://thenewstack.io/ai-agents-retrieval-engineering/) need more control over how and where they search.

Agentic RAG lets an agent rewrite the question and choose where and how to search. It may query a knowledge base or an account system, combine lexical, semantic, and graph search, fuse the resulting scores, rerank candidates, discard weak results, and try again. This can find evidence that a single semantic search would miss. It also adds more decision points that should be supported by evidence, and a confident answer may not reveal the retrieval path that led to it.

> “The opportunity comes with a responsibility: more decisions require a clear evidence trail.”

The opportunity comes with a responsibility: more decisions require a clear evidence trail. More control can improve coverage, but control alone cannot create trust. The system earns that trust by showing what it searched and why it accepted a source. It must also disclose what it couldn’t verify. Without that record, it can be harder to understand the basis for even a good answer.

## Retrieval is a series of decisions

A retrieval turn may look like a single operation in the application, but the agent is making a chain of choices. It interprets the user’s intent and creates a query. Then it chooses data sources, applies the required filters, and inspects the results. Only then can it decide whether the evidence is sufficient and connect claims to citations.

Each choice deserves care. An agent might search the support index for a billing question, remove a product name while rewriting a query, or find the right policy in the wrong customer’s account. The final answer could sound convincing yet be incomplete, fall outside the intended scope, or be unsuitable to share.

![Workflow diagram comparing basic RAG against agentic RAG.](https://cdn.thenewstack.io/media/2026/09/57ef99f0-image.png)

*A one-shot retriever makes a single retrieval pass. An agentic retriever may make several, and each can fail with no visible change in the final answer.*

A final list of top-k chunks can’t reconstruct this process. By then, the agent may have issued multiple queries and rejected several sources. It may have switched tools or rewritten the query. Each step must record structured data while it happens. This becomes your flight recorder for retrieval:

```

request      "Can I cancel this contract early?"
query        "early termination enterprise agreement"
source       approved_contracts (tenant=acme, region=US)
accepted     contract_884 §12, effective=2026-01-01, score=0.81
rejected     policy_119, reason="expired 2025-12-31"
decision     evidence sufficient for contract terms; fee amount unverified

```

Keep the query and its filters. Add source IDs, ranking data, timestamps, and the reason for each branch. There isn’t one correct retrieval method for every request. Lexical keyword search may be best for an exact contract number. Vector search may be best for a paraphrased policy question, while a plain SQL query pulls back an account balance. Graph traversal may be used to connect related documents or entities. The record should say which one the agent chose and why.

## Give users and operators visible evidence

Users and operators need different views of the same evidence. A user needs citations that identify the source and the relevant passage or record. Each citation should show the source’s effective date or last updated date, along with the date it was retrieved. Users need plain language when the evidence has limits: “I found the cancellation terms, but I couldn’t verify the current fee for your account.”

Operators need enough detail to produce and improve an answer. Preserve the rewritten queries and search attempts, while protecting those traces with appropriate access controls, redaction, and retention rules. Keep the rejected results, tool calls, applied filters, and any instructions that affected source selection. A citation alone does not establish claim support. An agent can cite a legitimate document that contains related language but doesn’t support the claim it wrote. It can also attach a citation after the answer is generated, leaving it unclear whether the source informed the answer.

Preserve citation provenance during generation, then verify that each claim is supported before releasing the answer. Store the source IDs passed to the model and map each supported claim back to the excerpt or record that supplied it. If a claim has no source, the application can remove or qualify it. For a high-risk claim, it can hold the answer for review before it reaches the user.

Use a practical replay test. Give an engineer the request and the trace, then ask, “Why this source?” Why was it valid at that time? Why did the system reject the alternative? If the trace can’t answer those questions, it isn’t detailed enough.

## Make currency and authority part of retrieval

Semantic similarity measures resemblance, not authority. A policy from last year can match a question perfectly and still not be the appropriate result in the index. A current policy with different wording may be the only one the agent should use.

> “A similarity score is an opinion; a scope filter is a rule the system can enforce.”

Treat source metadata as part of retrieval. Start with the effective date and owner, then record the access scope and document type. Approval status and jurisdiction matter for controlled material. Tenant identity is a hard boundary. A similarity score is an opinion; a scope filter is a rule the system can enforce. All of these fields should affect filtering and ranking. A regulatory question may require an approved primary source. A product question may prefer the latest published manual. A customer question must stay inside that customer’s scope.

![Workflow diagram of an example where the closest match isn't the most appropriate one.](https://cdn.thenewstack.io/media/2026/09/42e0defc-image.png)

*The closest match is not always the most appropriate source. Metadata rules decide what a similarity score can’t: whether a candidate is current, approved, and inside the caller’s scope.*

These rules can run before or after similarity ranking—or at both stages. The placement depends on the data and the risk, but either way, an unauthorized or expired record should be excluded, even when its wording appears to be a closer match. When tenant and scope boundaries are properly implemented, unauthorized records can be excluded before they become candidates.

Conflicting sources need their own path. If two approved policies overlap, the agent should not default to the most convenient paragraph. It should report the conflict and narrow the answer to what both sources support. If that isn’t possible, it should send the request for review. Someone must also own each source throughout its active life and retire it upon expiration. Retrieval cannot establish currency from a document library that is no longer maintained.

## Define a retrieval policy for the agent

“Be accurate” is an important goal, but too vague to serve as a retrieval policy. The application needs [enforceable rules for when the agent searches](https://thenewstack.io/why-ai-agents-need-their-own-identity-not-yours/) and which source types it can use. Separate rules should govern when it may broaden a query and when it must admit the evidence is incomplete.

Apply those rules before the model writes. Customer data stays within the verified customer scope. Regulatory answers use approved sources for the correct jurisdiction and effective date. A missing primary source results in a qualified answer or a request for review. These constraints should be implemented in tool permissions, query filters, and application code rather than relying on the model to remember a sentence in its instructions.

> “The agent decides what to ask; the retrieval layer decides what may be returned.”

Tool access needs the same treatment. Searching a public knowledge base carries a different risk than searching contracts, case notes, or a company-wide file store. Give the agent access only to the systems required for the task, and pass verified identity and scope to each search tool. Do not rely on the model to supply them as query arguments. The agent decides what to ask; the retrieval layer decides what may be returned.

Build these controls into the retrieval path before exceptions reach users.

### Treat retrieved content as data, not policy

Every document an agentic retriever reads should be treated as [untrusted model input](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), even when the application controls the source. Some of those documents will contain instructions. A wiki page can contain language that asks the agent to disregard its source restrictions. An ingested PDF can carry a line telling the model to prefer it over newer material. In basic RAG, a planted instruction can corrupt the answer. In agentic RAG, it can also steer subsequent searches, right down to the citations the agent presents as evidence.

![Workflow diagram showing how an embedded instruction can influence a basic RAG answer.](https://cdn.thenewstack.io/media/2026/09/670bc689-image.png)

*An embedded instruction can influence a basic RAG answer. In agentic RAG, it can redirect later searches, and memory can carry that influence into future requests.*

The governing rule is that retrieved content is data, never policy. Scope and permissions come from the application, and nothing in a document body should be allowed to change authorization or policy. Identity and scope filters belong in tool code and, where possible, in the database itself.

> “The governing rule is that retrieved content is data, never policy.”

The prompt alone is not a sufficient enforcement layer. Query rewrites and tool calls still need to be validated against the retrieval policy. The trace can reveal that a document influenced the next search, making it useful as a tool for detection and investigation. By the time it tells you anything, though, the search has already run. If retrieved material can be promoted into memory, the instruction can outlive the retrieval that introduced it and influence unrelated future requests.

### Keep retrieval near the data when it helps

Many RAG systems copy documents into one service, embeddings into another, metadata into a third, and permissions into application code. Each copy can update on a different schedule. That makes answer freshness harder to diagnose and access decisions more difficult to demonstrate.

Keeping more of that work near the operational data can shorten the path. [Oracle AI Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/overview-ai-vector-search.html?source=:ex:pw:::::TNS_AgenticRAG_A&SC=:ex:pw:::::TNS_AgenticRAG_A&pcode=) stores vector embeddings alongside business data, and its SQL queries can combine similarity search with [relational filters](https://docs.oracle.com/en/database/oracle/oracle-database/26/nfcoa/vector-data-type.html?source=:ex:pw:::::TNS_AgenticRAG_B&SC=:ex:pw:::::TNS_AgenticRAG_B&pcode=) and [lexical search](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/create-hybrid-vector-index.html?source=:ex:pw:::::TNS_AgenticRAG_C&SC=:ex:pw:::::TNS_AgenticRAG_C&pcode=). A team using Oracle AI Database can keep operational records, vectors, and access rules in a data platform it already controls. Database-enforced access controls can apply [row- and column-level policies](https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/DBMS_RLS.html?source=:ex:pw:::::TNS_AgenticRAG_D&SC=:ex:pw:::::TNS_AgenticRAG_D&pcode=) inside the database, allowing access restrictions to be enforced independently of the retrieval service.

This arrangement can reduce data copies and make lineage easier to inspect. It doesn’t decide which policy is authoritative, detect a conflict, or prove that a citation supports a claim. The retrieval policy and evaluations still have to do that work. Additional products do not resolve an undefined evidence path.

## Test decisions as well as answers

An evaluation that scores only the final prose does not assess much of the decision-making in [agentic RAG](https://thenewstack.io/the-precision-engine-why-agentic-rag-is-genais-next-leap/). Build a small set of requests that exercise those decisions. Include a current-policy question and a case with two tenants holding similar records. Add conflicting documents, an unusual but valid source, and a document that carries embedded instructions to the model. The set should also include a request with the correct result “I can’t verify this.”

Score retrieval separately from generation using measures such as corpus-selection accuracy, recall at k, tenant-isolation violation rate, citation coverage, and claim-support accuracy. Check whether the agent selected the correct corpus and applied all required filters. Inspect the selected sources and their citation-to-claim links. Confirm that the agent appropriately declined or escalated when it lacked evidence. The answer can sound awkward and still retrieve correctly. It can also sound convincing while using an expired policy.

Run these cases after a change to the embedding model, chunking method, index, prompt, ranking rules, or search tool. A higher relevance score means very little if the new index starts to prefer older documents or crosses a tenant boundary. Save production issues as new evaluation cases so the same issue is less likely to recur.

## Each answer needs an evidence path

Agentic RAG adds decisions, and confidence grows when the system can account for them. Make the evidence path and retrieval policy visible outputs instead of details buried in logs. When an answer needs review, that record is what lets a person decide whether it deserves their trust.

***Trying to implement agentic RAG? Working examples of these patterns, such as agentic RAG with hybrid search, are available in*** [***Oracle’s AI Developer Hub***](https://github.com/oracle-devrel/oracle-ai-developer-hub)***.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/08/c997c959-jeremy-daly-headshot-medium.jpeg)

Jeremy Daly is an independent architect, multi-time founder, developer, and AWS Serverless Hero who builds AI- and data-driven platforms that turn complex systems into reliable, scalable products. For more than 25 years, he has led teams building cloud-native infrastructure, intelligent...

Read more from Jeremy Daly](https://thenewstack.io/author/jeremy-daly/)