**A diff is not evidence. It’s a statement of intent.**

The tests passed. The review’s done. The change is live. Then someone says the app is slow, or the answers are wrong, or both. You open the diff. Your assistant points at the function it changed and offers a plausible cause.

It sounds right. It might not be.

This is the observability gap that AI features expose. [Dynatrace’s 2026 State of SRE and Platform Engineering report](https://www.dynatrace.com/resources/the-state-of-sre-and-platform-engineering-17401248/) (919 enterprise leaders surveyed globally) found that while 77% of platform engineering teams embed observability in at least some services, only 40% have it fully integrated across all deployments. That gap was manageable when your services were deterministic. But with AI agents, it becomes a liability.

> A conventional service fails loudly… An AI agent fails quietly. It returns a 200. It passes faithfulness checks. And the customer still gets the wrong answer.

A conventional service fails loudly. A 500 error, a latency spike, a dependency that stops responding. An AI agent fails quietly. It returns a 200. It passes faithfulness checks. The customer still gets the wrong answer.

You can’t alert on “wrong.” You need evidence from the running system — and for AI features, that means something more than request traces and error rates.

Find the request first.

## One release, two symptoms

Say you run a support agent over product documentation. A customer asks how to configure export in version 2026.3. Your coding assistant helped rewrite the documentation lookup. CI passed. The existing evals passed.

After deploy, answers take longer. Some of them describe older product versions.

Start with one affected run. You want its release, retrieval config, and feature-flag state, so those need to be on the root span as attributes set at span start, not reconstructed later from a deploy log. Then put that run next to one for a similar question from before the change.

For an agent, that means the trajectory: every model call and tool call, in order, with arguments and results. A [distributed trace](https://opentelemetry.io/docs/concepts/signals/traces/) records those as spans and stitches them across service boundaries through context propagation.

Here’s one run, simplified, with its evaluation linked separately.

```

# Illustrative pseudotelemetry, not a captured incident.

# Names, IDs, timings, and labels are invented, not a standard schema.

# Selected spans shown in execution order; other work is omitted.

trace: example-run-a | session: example-session-7 | release: 2026.9.2

requested.product_version: "2026.3"

agent.run                                  12.4s

  model.choose_tool                         1.0s

  tool.search_docs                          0.9s

    args: {query: "configure export", product_version: null}

  tool.search_docs                          0.8s

    args: {query: "configure export", product_version: null}

  tool.search_docs                          0.9s

    args: {query: "configure export", product_version: null}

    returned.doc_versions: ["2024.1", "2024.1", "2023.9"]

  model.generate_answer                     8.1s

linked_evaluation:

  trace: example-run-a

  faithfulness: pass

  requested_version_answered: fail
```

Two things to chase. The repeated searches. The null version filter.

# Check the repeated work

Three identical searches cost 2.6 seconds. The trace shows the symptom. It doesn’t explain the cause.

But look at what sits between them. Nothing. One *model.choose\_tool* span at the top, and no model call between the second search and the third. The model didn’t ask for those retries. Something in the harness did: the code that runs tools, handles retries, and manages context. A *model.choose\_tool* span between each search would mean the opposite: a model that kept requesting the same tool, which is a prompt or tool-description problem. Same symptom, different file to open.

That still doesn’t make the retries wrong. Read the retry policy, then read the tool results. A 200 from a search backend can carry an empty hit list, or every hit under your relevance threshold, and retrying on that is legitimate.

The generation call is the bigger slice anyway, at 8.1 seconds. Compare its input tokens and duration against similar runs. If the harness appended all three result sets to the context, the retries inflated that prompt, and you paid for them twice, in latency and in tokens. Check downstream services and traffic too before you pin the slowdown on the release.

Bringing this back into the IDE? Bound the question. Give the assistant the service, the release, the time window, and the trace IDs. Have it line the changed code path up against the dependency calls in the affected trace. Then separate what the evidence supports from what it’s assuming.

Same workflow debugs a checkout service making three identical database calls. You don’t need to build an agent to use it.

## A grounded answer can still fail

Now read the answer.

In this example, it accurately repeats the retrieved documentation. *Faithfulness* passes, or *groundedness*, depending on whose vocabulary your tooling uses.

*The customer still gets instructions for the wrong version.*

Whether you call it faithfulness or groundedness, the metric only tells you whether the answer is supported by the sources you supplied. It says nothing about whether those were the right sources.

The obvious next move is a retrieval evaluator. It still won’t catch this. Those score whether the retrieved context is relevant to the query, and the 2024.1 export instructions are relevant to configure the export. They’re just invalid for the version asked. Those documents are relevant to the query. They are not valid for the version the customer requested. Relevance is not validity.

> Those documents are relevant to the query. They are not valid for the version the customer requested. Relevance is not validity.

So, this isn’t a generation failure. It’s a retrieval precondition nobody asserted, and the null filter names it: the requested version never reached the lookup. Reproduce that before you touch the prompt or the model.

Most of it is testable with ordinary code. Give the fixtures documents carrying version metadata, then assert on the lookup directly, no model in the loop:

```
def test_lookup_filters_to_requested_version(docs_fixture):

    hits = search_docs(query="configure export", product_version="2026.3")

    assert hits, "no hits for a version that has docs"

    assert {h.product_version for h in hits} == {"2026.3"}
```

Deterministic, cheap, belongs in CI. Then evaluate the answer separately, which is the part you can’t assert: does it give usable 2026.3 instructions, or say the available documentation can’t support one? Two tests, because they fail for different reasons and you want to know which one broke.

The assertion won’t catch every wrong answer. It catches this missing constraint every time, which is more than a judge scoring helpfulness one to five will do for you.

Which is why evaluation needs retained context. Record the prompt version, model ID, retrieval config, and document IDs and versions alongside the release. Keep enough permitted evidence to read the answer back later, sensitive content redacted before export.

Link results by trace and span ID. If scoring lands after the span closes, store a separate linked result. Don’t plan on writing attributes to a finished span: the [OpenTelemetry tracing API](https://opentelemetry.io/docs/specs/otel/trace/api/#end) says implementations should ignore updates after End.

GenAI semantic conventions are still evolving, and different instrumentation projects expose similar concepts with different attribute names.

## Make the failure part of the next release check

Confirmed the causes? Verify each fix against the behavior it’s supposed to change.

For the repeated searches, add a regression test that reproduces the repetition without killing legitimate retries. Don’t pin one exact tool sequence when several orderings finish the task correctly; a trajectory test that demands a single path fails on every valid refactor.

For the version mismatch, restore the filter. Add these cases: current version, an older supported version the customer names explicitly, irrelevant documentation, and no supportable answer. Run the answer evals repeatedly where output varies, because one pass isn’t a result.

Use code for anything you can assert directly. Use a model-based judge for answer quality, and validate that judge against examples people reviewed. An unchecked judge is one more model you’re taking on faith.

To run scoring against production traffic rather than fixtures, you’ll need a way to sample spans already in your environment, score them with a judge model, and link each result back to the source trace — the linked-result pattern above, not a write to a closed span. Whatever tooling you use, version the evaluator. A scoring change that looks like a product improvement isn’t one.

After the release, compare latency and task success on similar requests, and keep tool-call and token counts on the same screen. Read them together, or they’ll mislead you. Tool calls dropping from three to one can look like the fix is working, but it can also look like a lookup you removed by accident. Fewer output tokens look like a cost win, and it also looks like an answer that quietly stopped listing step four.

## Bring one debugging question

If you wouldn’t know where to start the investigation, you’re not done instrumenting.

For a conventional service, that’s the request path and dependency timing. For an AI feature, add what it retrieved, what it produced, and how you’ll decide whether that was the right answer.

***Dynatrace is sponsoring [WeAreDevelopers World Congress Americas, September 23-25, 2026, in San José](https://www.wearedevelopers.com/world-congress-north-america). Come with a debugging question from an AI-assisted release or from an AI feature you’re building, and we’ll work through it.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/09/c4852483-cropped-2ddd839d-1591025032978.jpg)

Sean O'Dell focuses on Developer Experience at Dynatrace, where he champions developers and modern application development practices. A reformed infrastructure administrator and architect, Sean brings deep experience from Infra, Cloud, Dev and Ops, with a passion for helping developers thrive...

Read more from Sean O’Dell](https://thenewstack.io/author/seanodell/)