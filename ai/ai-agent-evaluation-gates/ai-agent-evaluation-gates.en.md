A team builds an agent, gives it a few representative questions in a test chat, and watches it produce useful answers. Someone tries a slightly harder prompt, and that works too. The team records a demo, approves the change, and ships it.

Then the retrieval configuration changes. A model upgrade follows a few weeks later. The agent still answers the original questions, but now it skips a required citation on one task and selects an unintended customer lookup tool on another. The issue may not become visible until user feedback or monitoring surfaces it.

A good demonstration tells you that an agent worked once, under the conditions you happened to give it. It doesn’t fully establish whether the next version will consistently preserve the behavior your users and operators need. For that, evaluation has to become part of the delivery process.

> “If it can’t reproduce a run or a material regression in a high-risk workflow, the product isn’t ready to pass the release gate.”

A repeatable evaluation system runs fixed scenarios along the product’s execution path and records sufficient evidence to determine whether a release should proceed. It should exercise the code that assembles context, the tools the agent can call, and the permissions the runtime enforces. If it can’t reproduce a run or a material regression in a high-risk workflow, the product isn’t ready to pass the release gate.

## Define correct behavior before writing tests

“The answer was good” isn’t a requirement anyone can test twice. Before choosing an evaluation tool, write down the [jobs the agent performs](https://thenewstack.io/ai-agents-software-engineering/), the limits around each job, and the outcomes that fall outside the product’s accepted operating boundaries.

For a support agent, a useful job might be to answer a billing question using records from the correct account and cite the policy currently in force. Its limits may forbid changing a plan or exposing another customer’s data. When a policy can’t be found, the agent should acknowledge the gap and avoid presenting an unsupported answer as fact. The [agent may also need](https://thenewstack.io/why-ai-agents-need-their-own-identity-not-yours/) to request an account number before continuing, or route an exception to someone with the appropriate access.

Separate the result from the process that produced it. An agent can give the right answer after retrieving the wrong document, or complete a task after calling an unnecessary tool or searching outside the customer’s scope. It can even escalate a routine request it should have handled on its own. Those runs may look successful in a transcript while masking weaknesses that may appear under different requests.

Start with a few observable requirements for each job. Required facts must be supported by named sources, and writes must wait for confirmation. When data is missing, the agent should ask rather than guess. High-risk rules get exact assertions; the wording around them can tolerate some variation.

## Build scenarios from real user work

The first test set should be small enough for someone to maintain. Ten real tasks are more valuable than a large benchmark filled with prompts your users never send.

> “Ten real tasks are more valuable than a large benchmark filled with prompts your users never send.”

Support tickets and workflow logs are good raw material. So are incident reports and conversations with users. Include the ordinary requests that make up most of the workload, then add cases with unclear instructions or missing account data. Test what happens when a document is outdated or a tool times out. Some scenarios should require approval before the [agent can act](https://thenewstack.io/audit-trails-revenue-asset/), and a few should cover unusual but still perfectly valid requests.

Agents operate across turns, so some scenarios should too. Ask for an account change, provide the missing identifier in the next message, and confirm the proposed change in a third. The test should verify that the agent carries the account identifier and proposed change across turns without dragging unrelated details into the final action.

Each scenario also needs fixtures. Freeze the documents and tool responses used during the run, and pin the account state to a known snapshot. The policy version and the agent’s permissions matter just as much. A failure you cannot reproduce becomes a debate about what the agent may have seen. Fixed fixtures turn it into an engineering problem.

Production failures should be treated as permanent regression cases. Over time, the suite records the mistakes the team has already paid for and learned from.

## Test the entire execution path

Final-answer scoring misses much of what distinguishes an agent from a chatbot. An agent retrieves data and chooses which tools to call. It supplies the arguments, reads the results, and then decides whether to continue. Any step in that loop can diverge from the intended path even when the response appears convincing.

Capture the request and system instructions. Record the exact model and application build. Version the prompt and retrieval configuration, including the tool schemas. Then record every retrieved source with its version, as well as every tool call, its arguments, and its result. Permission checks and the final response belong in the trace too, along with latency, token usage, and cost. The trace should answer practical questions without requiring someone to reconstruct the run from unrelated logs.

> “Final-answer scoring misses much of what distinguishes an agent from a chatbot. Any step in that loop can diverge from the intended path even when the response appears convincing.”

When combined with server-side enforcement and audit records, the trace should show that a search remained within the correct tenant and customer account. It should also identify the approved policy source and the records cited in the answer. For a write, it should show that the user confirmed the change and that the server-side permission check passed. Those are deterministic checks: they either happened or they didn’t.

Clarity and usefulness are less deterministic. A human reviewer or model-based evaluator can score whether the response answered the request, explained a limitation, or asked a sensible follow-up question. Keep those judgments attached to the trace. When a score drops, the team should be able to find the step that changed.

This also makes evaluator failures easier to spot. A model-based evaluator may produce different judgments after an upgrade or respond differently to a revised rubric. Save the evaluator’s version and instructions with its result. Regularly compare a sample of those scores with human reviews.

![Side-by-side workflows of final-answer scoring and execution-path trace](https://cdn.thenewstack.io/media/2026/09/e20c284f-image.png)

*Both columns end in a convincing answer. Only one of them can tell you whether the agent was correctly grounded.*

## Keep fixed rules separate from variable scores

Agent quality doesn’t fit into one unexplained number. Track task completion and factual support separately from retrieval quality. Keep policy compliance distinct from user experience, latency, and cost.

Some of those signals have tolerances: a response that takes 200 milliseconds longer may still be acceptable, and a slightly longer answer may even be clearer. Others allow no failures. An unapproved update, cross-tenant retrieval, or missing approval should remain a release-blocking condition regardless of other scores.

Compare a candidate against a known baseline on the same scenarios and fixtures. Show the reviewer the changed answers and the records behind them, then let the tool paths and individual scores explain why. If the new version completes more tasks but doubles latency, that may be a reasonable product decision. If it improves the average score while bypassing one permission gate, it is not.

Repeat scenarios when behavior is variable. A task that succeeds inconsistently—for example, once in ten attempts—does not yet meet a reliable release threshold. Set thresholds based on risk, and reserve absolute gates for rules the system must obey every time.

None of this requires building your own tooling from scratch. Tools such as [Promptfoo](https://www.promptfoo.dev/docs/tracing/), [DeepEval](https://deepeval.com/docs/evaluation-llm-tracing), [LangSmith](https://docs.langchain.com/langsmith/evaluation-concepts), and [Braintrust](https://www.braintrust.dev/docs/evaluate/run-evaluations) provide capabilities for building evaluation workflows. Depending on the tool, that support can include running scenarios and capturing traces. Some also use models to grade the result.

The metrics vocabulary is worth learning too. Conceptually, [pass@k](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) asks whether at least one of k attempts succeeds, while [pass^k](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) asks whether all k attempts do. Pass^k is useful when consistent behavior matters, but it doesn’t replace exact gates for rules an agent must obey.

Evaluation also has a cost. Every live, end-to-end run that calls a model spends tokens. Judge models cost more than string checks, and a large suite on every commit adds up quickly. Save the expensive judgments for the scenarios that carry real risk.

## Make evaluation a release gate

Run the suite whenever the team changes a model or a prompt. A new retrieval configuration counts, as does any change to a memory policy or a tool interface. Use a fast set for ordinary changes and a broader set before a major release or model migration. When a behavior change is intentional, require a reviewer to approve the new expectation rather than rewrite the test.

The records behind this process need the same controls as the agent itself because evaluation inputs may contain customer data. Traces can include retrieved text and internal instructions. They may also capture tool arguments containing credentials or personal data. Version the records and scope access carefully. Consider redacting sensitive values before persistence and applying appropriate encryption, access controls, and retention policies based on the data involved.

Keeping more of that work near the operational data can shorten the path. [Oracle AI Vector Search stores vector embeddings alongside business data](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/ai-vector-search-users-guide.pdf?source=:ex:pw:::::TheNewStack_A&SC=:ex:pw:::::TheNewStack_A&pcode=), and SQL queries can combine similarity search with relational filters and lexical search. A team using Oracle AI Database can keep operational records and their vectors in a data platform it already controls.

The same platform can hold evaluation traces and enforce access rules. [Database-enforced access controls can apply row- and column-level policies within the database](https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/DBMS_RLS.html?source=:ex:pw:::::TheNewStack_B&SC=:ex:pw:::::TheNewStack_B&pcode=), providing another layer for enforcing data-access boundaries. The exact platform matters less than the invariant: the team needs durable evaluation cases, the inputs used for each run, and a record of why each build passed.

A release gate should prevent releases with known high-risk conditions while recognizing that some judgments require context. Exact checks block permission and policy regressions. Thresholds catch measurable quality drops, and human review handles the ambiguous changes scores cannot settle.

![Diagram showing the workflow of a release gate that runs on every model, prompt, retrieval, or tool change.](https://cdn.thenewstack.io/media/2026/09/b1be3624-image.png)

*Hard rules block on any failure; everything else gets a tolerance or a reviewer.*

## Start with ten cases and keep every important failure

Pick ten real tasks this week. Record the expected result and the evidence the agent should use. Note the actions it must not take. Freeze the fixtures, capture the trace, and run the cases before the next release.

> “Trust in an agent grows when the team can replay what happened and show that the next release still respects the boundaries users depend on.”

When an incident happens, add it to the suite. When a user finds a failure that nobody predicted, keep it. The suite will grow with the product.

Trust in an agent grows when the team can replay what happened and show that the next release still respects the boundaries users depend on. The evaluation system is part of the product that ships.

***Need help with agent evaluations? Working examples of these patterns in Oracle AI Database, including agentic RAG patterns with hybrid search, are available in*** [***Oracle’s AI Developer Hub***](https://github.com/oracle-devrel/oracle-ai-developer-hub/)***.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/08/c997c959-jeremy-daly-headshot-medium.jpeg)

Jeremy Daly is an independent architect, multi-time founder, developer, and AWS Serverless Hero who builds AI- and data-driven platforms that turn complex systems into reliable, scalable products. For more than 25 years, he has led teams building cloud-native infrastructure, intelligent...

Read more from Jeremy Daly](https://thenewstack.io/author/jeremy-daly/)