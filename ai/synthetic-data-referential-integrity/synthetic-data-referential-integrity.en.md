While enterprise leaders overwhelmingly believe in the promise of synthetic data, adoption lags. As a result, synthetic data has great, untapped potential. The answer? Enterprises need the right, high-quality approach that upholds [referential integrity](https://www.perforce.com/resources/pdx/referential-integrity) and earns their trust.

Our research shows the biggest barrier to adoption isn’t awareness, compliance, or governance. It’s data quality. Across industries, enterprise leaders increasingly recognize synthetic data’s value in protecting sensitive information, moving [at agentic speed](https://thenewstack.io/why-load-tests-lie-harsh-truth-about-ai-agent-performance/), and expanding data access without increasing risk.

However, only 38% of leaders believe synthetic data delivers sufficient realism and just 34% believe it preserves referential integrity, according to recent [Perforce Delphix research](https://www.perforce.com/resources/pdx/state-of-synthetic-data-report).

Synthetic data usage within software engineering and testing teams remains surprisingly limited, likely for this reason. As a result, enterprises are missing out on the opportunities that true, high-quality synthetic data can provide. The first step to tapping into these opportunities: Ensuring synthetic data meets your quality standards.

## The promise of synthetic data

[Synthetic data](https://www.perforce.com/products/delphix/synthetic-data) is getting so much attention for good reason. For years, organizations have struggled to balance two competing priorities: providing teams with the data they need while protecting sensitive information.

Traditional approaches often force teams to choose between access and risk. Data is either restricted, creating [bottlenecks for development](https://thenewstack.io/test-data-ai-bottleneck/) and testing, or distributed broadly, increasing compliance and security concerns.

By generating new, synthetic datasets that reflect production data characteristics without its privacy risks, organizations can increase test data availability while maintaining governance and compliance. More than half of enterprises (51%) already use synthetic data to protect sensitive data, alongside approaches such as static and dynamic masking.

It is a compelling vision, particularly as AI agents increase demand for readily available, high-quality data across the business. Of course, while it’s easy to generate synthetic data, not all synthetic data is created equal. Many organizations have experimented with synthetic data but didn’t see improvements in application development and testing because it lacked realism or failed to preserve relationships.

Adopting synthetic data comes down to whether organizations trust that certain synthetic data solutions are evolving and *can* maintain realism when they haven’t in the past. A modern, AI-first approach that prioritizes data quality at scale can address these legacy concerns.

## Developers need more than protected data

While executives often evaluate synthetic data through a governance lens, development teams evaluate it through a quality lens. Currently, 66% of software leaders report they aren’t using synthetic data in development and testing.

> “Developers and testers don’t primarily ask whether data is protected. They are asking whether it is useful.”

Developers and testers don’t primarily ask whether data is protected. They are asking whether it is useful, posing questions like:

* Can it accurately represent customer behavior?
* Can it support complex testing scenarios?
* Can it preserve relationships across interconnected systems?
* Can it provide confidence that applications tested today will perform correctly in production tomorrow?

These questions matter because development teams testing applications, business processes, workflows, integrations, and customer experiences need synthetic data to be more than fake. It needs to preserve the context, relationships, and realism that make data meaningful.

Here’s one example: Generating a random number in a credit rating field could be technically correct, but it wouldn’t reflect your real data. By generating data within real-world bounds and ranges, you uphold realism and quality.

If data lacks realism or doesn’t reflect actual system behavior, teams risk validating applications against scenarios that don’t exist in production. The result can be defects, failed releases, and inaccurate testing outcomes.

## What trustworthy synthetic data looks like

For synthetic data to support enterprise development at scale, it must behave like the systems it represents. Not every synthetic data tool can do that, but you can customize generation rules [to uphold referential integrity](https://www.perforce.com/blog/pdx/synthetic-series-referential-integrity) across different data environments.

Enterprise applications rarely operate within a single database. Customer information may live in one system, orders in another, and payment information in a third. Testing only works when those relationships remain intact across environments. When they don’t, teams aren’t testing real business processes. They’re testing disconnected components in isolation.

> “Enterprise applications rarely operate within a single database. Testing only works when those relationships remain intact across environments.”

Organizations evaluating synthetic data tools should therefore treat a few capabilities as non-negotiable:

* **Preserve relationships across databases and systems,** not just within a single schema. Enterprise applications depend on cross-system dependencies, and synthetic data must reflect them. For example, two charts like investor and investment account should always be linked.
* **Generate data in dependency order,** so parent-child relationships remain intact throughout the environment.
* **Validate realism and business logic** by ensuring generated data follows expected formats, ranges, distributions, and rules. A test dataset should never produce impossible scenarios such as invalid identifiers or nonsensical business outcomes.
* **Continuously evaluate data quality** as schemas evolve. If synthetic data requires extensive manual reconfiguration every time a source system changes, quality and trust inevitably erode over time.

By checking these boxes, synthetic data can remain useful for development while reducing data privacy risk.

## Why AI makes this challenge more urgent

The rise of [AI-assisted development](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/) is exposing a long-standing challenge that is now impossible to ignore: Software delivery can only move as fast as the data supporting it.

While code generation has accelerated dramatically, access to high-quality test data has not kept pace. Synthetic data can help bridge this gap. Unlike production data, synthetic data can be generated on demand.

This capability is especially valuable when teams need purpose-built data for [new applications](https://www.perforce.com/blog/pdx/synthetic-for-greenfield-app-dev), features, edge cases, and AI-driven initiatives where production data may not exist or may be hard to use. Synthetic data lets teams create realistic testing scenarios on demand and shift validation earlier in the development lifecycle.

> “Software delivery can only move as fast as the data supporting it.”

At the same time, synthetic data is not necessarily a replacement for every testing approach. Increasingly, organizations are finding value in combining both approaches: using masked data for known workflows while using synthetic data to expand coverage and test entirely new scenarios. Together, they provide both realism and flexibility.

The common thread is trust. Whether teams are testing new features, validating integrations, or supporting AI-assisted development, confidence depends on data that accurately represents the relationships and context of real-world systems. Referential integrity is no longer a technical nice-to-have. It’s becoming a prerequisite for meaningful adoption of synthetic data.

## The future of synthetic data depends on trusted data

The next phase of synthetic data adoption will depend on whether engineering teams trust the data enough to build, test, and innovate with it.

As software delivery accelerates toward agentic speed, trusted data becomes a competitive advantage. Organizations need data that can be generated quickly, but it must also accurately reflect real-world relationships, business processes, and system behavior.

> “Ultimately, synthetic data adoption isn’t an awareness problem. It’s a trust problem, and trust comes from data quality.”

Companies that bridge this gap won’t be the ones that simply generate more synthetic data. They’ll be the ones that generate realistic, referentially accurate, fit-for-purpose data that developers can confidently use to speed up their releases and keep pace with AI.

Ultimately, synthetic data adoption isn’t an awareness problem. It’s a trust problem, and trust comes from data quality.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/f43c26d3-mayank_headshot-600x600.png)

Mayank Ahluwalia is a Senior Product Manager at Perforce Delphix with experience in data management, data compliance, systems architecture, machine learning, and AI. He has spent much of his career as a hands-on engineer building and operating real systems, giving...

Read more from Mayank Ahluwalia](https://thenewstack.io/author/mayank-ahluwalia/)