**AI coding agents still struggle with large-scale refactoring, with the best model achieving only a 41.2% resolve rate on a new refactoring-focused benchmark** developed by[researchers](https://arxiv.org/abs/2608.09802) at Shanghai Jiao Tong University, Peking University, Douyin Group, and other institutions.

It’s no secret that [AI benchmarks aren’t perfect](https://thenewstack.io/enterprise-ai-benchmarks-are-broken). A recent [audit](https://arxiv.org/abs/2608.09802) cited by the researchers shows how misleading AI coding agent benchmarks can be, with nearly 60% of unsolved SWE-bench Verified instances containing flawed tests.

> “We don’t have LLMs that would be able to read a large codebase and see it in its entirety and ‘understand’ it all at once,” he says. “That level of capability is still far out of reach.”

For AI coding agents, specifically, evaluation quality is considered to be on the decline, as frontier models can end up sailing through benchmarks if solutions have leaked into training sets. But when models can manage impressive-looking scores without really doing all the work, it raises the question of whether those benchmarks are truly a good indication of real-world agent capabilities.

As [Vojtěch Pavlík](https://www.linkedin.com/in/vojtechpavlik/), senior director of technical strategy, core infrastructure, [SUSE](https://www.suse.com/), tells The New Stack, many sought-after capabilities are still a ways away:

“We don’t have LLMs that would be able to read a large codebase and see it in its entirety and ‘understand’ it all at once,” he says. “That level of capability is still far out of reach.”

A new benchmark attempts to clear things up. [SWE-Bench ProMax](https://arxiv.org/abs/2608.09802) is a multilingual code refactoring benchmark of 170 instances from real commits across seven programming languages (Python, Java, TypeScript, Go, C, C++, and Rust). Per its creators, every instance underwent multi-stage curation to address the quality problems found in other benchmarks: They wrote issue descriptions to make them more precise; manually reviewed test suites to remove overly narrow or broad tests; and filtered out tasks with insufficient complexity or limited cross-file scope.

The result is a benchmark that frontier models struggle to solve.

## Why large-scale refactoring stumps coding agents

By focusing SWE-Bench ProMax on large-scale refactoring, researchers say the new benchmark “presents a meaningful and unsaturated challenge for current AI coding agents.”

That’s because refactoring is hard. “Strict refactoring demands zero tolerance for error, zero tolerance for behavior changes, and complete reversibility,” [Shane Warden](https://www.linkedin.com/in/shane-w-0aa569116/), principal architect, [ActiveState](https://www.activestate.com/), tells *The New Stack*. For him, the question of whether or not current AI tools can successfully handle large-scale refactoring depends on whether source code is considered plain prose or a deterministic, structured graph of information:

> “I don’t believe that premise. I believe that token proximity does not guarantee structural understanding.”

“Engineers who view LLMs primarily as text-processing engines treat refactoring as a text-generation task,” he says, explaining that developers who take this approach feed an entire codebase into a large context window, prompt the model, and then wait for a series of multi-file diffs.

But he’s not buying that take. “This approach relies on the premise that current LLMs express a deep understanding of large systems,” continues Warden. “I don’t believe that premise. I believe that token proximity does not guarantee structural understanding.”

Pavlík adds another problem, saying that attention — or a lack thereof — also complicates large-scale refactoring:

“For very large LLMs, a highly optimized attention algorithm, like DSA [Deepseek Sparse Attention] and similar others are basically a requirement to get any usable performance,” he says. “For changes in a large, complex, or convoluted codebase that maxes out the context window, this can easily result in missing important observations and generally getting confused.”

Beyond context and attention woes, Pavlík calls out time as a fundamental factor in software that further trips up LLMs, pointing to race condition errors, loss of idempotency, loss of atomicity, and incorrect retry handling as problems that emerge when parallel tasks execute in different orders, i.e., what he says happens “where code meets time.”

“People live in a world based on time,” he says. “LLMs, not so much. You get code that passes all tests and works on a sunny day if the user does the tasks exactly as described in the contract/manifest/spec, but fails miserably when a user clicks a button twice in a quick succession, when a connection times out on a network, or when two tasks finish at nearly the same time, overwriting each others results.”

With all these factors at play, it’s easy to see why many benchmarks overlook large-scale refactoring — but that’s precisely why they need it. Without tests on complex, cross-file work, how can developers judge what agents can really do?

## What SWE-Bench ProMax tests that most benchmarks miss

Most coding agent benchmarks are designed to run quickly and produce reasonably deterministic, verifiable solutions. “This rules out large-scale refactoring tasks,” Pavlík tells *The New Stack*.

He also says it’s why most LLM benchmarks today are compromised, as they often exercise models on only small contexts where they’re at their best. Plus, “many current frontier LLMs know the answers to most common benchmarks by heart by now,” Pavlík adds. “The more ubiquitous a benchmark becomes, the less reliable the results are.”

With this new refactoring-focused benchmark, Pavlík sees it as a sign that tests are becoming more complex and less learnable upfront so they can better expose where agents struggle:

“SWE-Bench ProMax is an example of how benchmarks are moving, from the ‘we need to measure how good the LLM is’ approach to ‘we need LLMs to improve on a particular task’ approach.”

## What will it take to make agents better at refactoring?

Building a benchmark that can identify holes in agent performance is one thing. But what will it take to plug them up?

For his part, Pavlík calls for a multi-layered approach, where developers first analyze and map the codebase to create detailed specifications, use retrieval-augmented generation to recall relevant parts of the code, rather than leaning purely on attention, and bring humans in for validation. He also advises implementing a fully detailed test suite for the original codebase to make sure it’s correct before starting refactoring.

Warden puts forth a similar idea: “To me, the most promising research focuses on LLMs driving deterministic, structurally aware developer tooling instead of LLMs writing out raw multi-file diffs.”

He describes an architecture where the LLM recognizes code smells, evaluates design trade-offs, and queries Language Server Protocols (LSPs) and code graph tooling to analyze explicit code structures, dependencies, and data flows, issuing small, zero-entropy commands to execute changes and rolling back those changes if tests fail.

Benchmarks are never going to provide a perfect measure of real-world performance, but leaving out difficult tasks like refactoring paints an overly rosy picture of agent capabilities. SWE-Bench ProMax may just bring in some realism.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)