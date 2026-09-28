As organizations invest in AI, many are discovering a new bottleneck: obtaining data that is both protected and useful. Engineering teams need realistic, production-like data to validate AI-generated changes, train models, test applications, and generate business insights. Yet, privacy initiatives can sometimes make that data harder to access, less representative of real-world conditions, or unable to preserve critical relationships between records.

The [Perforce Delphix](https://www.perforce.com/) [“2026 State of AI and Data Privacy Report](https://www.perforce.com/resources/pdx/state-of-ai-and-data-privacy-report)” highlights this challenge. Among surveyed organizations, 26% say privacy controls make production-quality data harder to obtain, 25% struggle to preserve relationships across data entities, and 51% cite data quality challenges.

> “Protecting data isn’t enough if it can no longer support the systems that depend on it.”

Protecting data isn’t enough if it can no longer support the systems that depend on it. For engineering teams, the question is whether their data protection strategies can preserve the qualities that make data valuable in the first place. You need a well-rounded data strategy with tools that maintain referential integrity and relationships across your environments.

## What these statistics mean for practitioners

At first glance, statistics from the report, like “51% of enterprises cite data quality challenges,” may sound like a purely governance issue.

In practice, they represent engineering problems. Low-quality datasets can produce:

* Inaccurate analytics.
* Poorly trained AI models.
* Incomplete test coverage.
* Increased rework.
* Delayed releases.
* Reduced confidence in [data automation](https://www.perforce.com/resources/pdx/test-data-automation).

> “When an AI model is trained on incomplete or distorted data, its outputs become less reliable.”

When an AI model is trained on incomplete or distorted data, its outputs become less reliable. When test environments contain unrealistic data, defects can escape into production. When analytics datasets lack consistency, teams spend more time validating results than acting on them.

## Data protection and utility are not opposing goals

A common misconception is that organizations must choose between privacy and innovation, but the most successful organizations know that compliance, quality, and speed *can* and *need to* work together.

Protected data still needs to be:

* Realistic enough for testing and validation.
* Representative enough for analytics.
* Accessible enough for engineering teams.
* Governed enough for [regulatory requirements](https://www.perforce.com/resources/pdx/data-privacy-regulations).
* Connected enough to preserve referential integrity.

There’s a two-fold goal in the AI era: reduce sensitive data exposure while also creating trusted data that remains valuable after protection. All too often, enterprises sacrifice compliance for innovation or speed. That’s a big reason 84% of respondents in our report have a data privacy exception in their non-production environments.

> “There’s a two-fold goal in the AI era: reduce sensitive data exposure while also creating trusted data that remains valuable after protection.”

Organizations can only move at AI speed when they have access to trustworthy data that accurately represents production conditions. When privacy controls degrade quality, limit realism, or restrict access to representative datasets, the data layer becomes the new bottleneck.

## Why referential integrity matters more than ever

Many discussions about data privacy focus on masking sensitive fields. However, masked data that loses [referential integrity](https://www.perforce.com/resources/pdx/referential-integrity) between entities can create a different kind of risk.

A customer, order, or payment record may still exist, but if the relationships connecting those records break during protection processes, the data no longer resembles reality. Take billing validation, for example. It needs referential integrity when a customer has multiple products, charges, and invoices across several database tables to produce the correct products or make accurate charges.

Broken relationships are especially problematic for [modern AI and analytics](https://thenewstack.io/data-telemetry-is-the-lifeline-of-modern-analytics-and-ai/) systems. Analytics pipelines depend on consistent identifiers to join information across sources. AI and machine learning workflows depend on complete business context to identify patterns and make predictions. Software testing depends on realistic relationships between records to validate application behavior accurately.

### When referential integrity is lost:

* Analytics can produce [incomplete or misleading results](https://www.perforce.com/blog/pdx/cost-of-software-defects).
* AI models can learn from flawed datasets.
* Testing environments can fail to expose production issues.
* Teams lose trust in protected datasets.

Importantly, these failures are often difficult to detect. Pipelines may continue running successfully while quietly producing degraded outcomes, which can be a very costly mistake.

This helps explain why 25% of surveyed organizations cited preserving relationships across data entities as a significant challenge. For practitioners, that statistic is a warning that privacy controls can unintentionally undermine the quality of AI and analytics initiatives if they fail to preserve business context.

Keep in mind that not all data protection solutions are created equal — enterprise-grade masking algorithms are key to preserving relationships. When applied [consistently and at scale](https://thenewstack.io/consistency-at-scale-unifying-temporal-and-yugabytedb/), these algorithms ensure the same input produces the same masked output across your systems and environments. Other masking approaches might be done piecemeal, resulting in broken relationships.

## What engineering teams should measure

Many organizations measure privacy success through compliance metrics alone. However, AI-driven environments require a broader definition of success. Engineering leaders should evaluate privacy initiatives against several dimensions:

* **Data quality:** Does the protected dataset accurately reflect production conditions?
* **Realism:** Can developers, data scientists, and analysts use the data confidently for their intended purpose?
* **Referential integrity:** Do relationships remain consistent across applications, tables, environments, and data sources?
* **Accessibility:** Can teams obtain compliant data without introducing delays?
* **Provisioning speed:** How quickly can trusted datasets be delivered when needed?

These measurements help organizations determine whether privacy efforts enable AI outcomes or create new obstacles.

## Designing for governance by default

As AI adoption grows, privacy cannot remain a separate process that occurs after development begins. Organizations should instead map the entire data lifecycle, from data request and discovery to reuse and retirement.

This approach helps ensure governance is built into workflows rather than applied as a late-stage checkpoint. It also provides stronger auditability, reduces compliance exceptions, and gives teams greater confidence that protected datasets remain fit for purpose.

Most importantly, it aligns privacy objectives with business outcomes instead of treating them as competing priorities.

## Trusted data will become a competitive differentiator

The need for test data — in volume, coverage, and scale — is booming [as agentic development continues to rise](https://thenewstack.io/enabling-autonomous-agents-with-environment-virtualization/). AI has also increased the volume of change enterprises can generate, but the challenge of validating that change remains unsolved.

That responsibility still belongs to data. The organizations that gain the most value from AI will not necessarily be the ones with the most advanced models. They will be the ones with the most trustworthy data foundations — using a portfolio approach that combines data virtualization for speed, masking for security, and synthetic data for coverage as needed.

> “In the AI era, trusted data, not fast model output, may be the ultimate competitive advantage.”

The research points to a clear lesson: If privacy controls uphold realism, quality, relationships between records, or access to representative datasets, they can enable AI success.

As enterprises continue investing in AI and data privacy, the real objective should be ensuring protection and utility coexist. Because in the AI era, trusted data, not fast model output, may be the ultimate competitive advantage.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/f43c26d3-mayank_headshot-600x600.png)

Mayank Ahluwalia is a Senior Product Manager for Perforce Delphix. He has experience across data management, data compliance, systems architecture, machine learning, and AI. He has spent much of his career as a hands-on engineer building and operating real systems,...

Read more from Mayank Ahluwalia](https://thenewstack.io/author/mayank-ahluwalia/)