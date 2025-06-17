# The Anti-Metrics Era of Developer Productivity
![Featued image for: The Anti-Metrics Era of Developer Productivity](https://cdn.thenewstack.io/media/2025/06/7f2a730c-metrics-1024x577.png)
The introduction of sophisticated [AI coding assistants](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/) has fundamentally altered the way developers work. What once took hours of concentrated typing and debugging can now be accomplished in minutes through well-crafted prompts and iterative collaboration with AI tools.

Today’s development process often looks like this:

- The developer gathers requirements for a task.
- The developer provides context, with clear step-by-step directions to an AI assistant.
- AI generates an initial code implementation.
- The developer reviews, edits and refines the AI-generated code.
- The developer and AI iterate until the solution is optimal.
This workflow bears little resemblance to the traditional coding process, where developers wrote every line manually. The skills that matter most have shifted from typing speed and syntax memorization to problem formulation, solution evaluation and effective collaboration with AI tools.

## Tech’s Obsession With Measuring Productivity
The old adage says that you cannot improve the things you cannot measure. But the tech industry has taken that out of context, becoming obsessed with measuring “everything we can” despite the fact that over two decades ago, [Martin Fowler](https://twitter.com/martinfowler), the architect of modern software development, wrote that [developer productivity cannot be measured](https://martinfowler.com/bliki/CannotMeasureProductivity.html).

[Developer productivity metrics](https://thenewstack.io/developer-productivity-whos-tracking-it-not-many/) are useful for understanding the bottlenecks in the engineering processes, but they are not the goal.
Metrics are still important. [DevOps Research and Assessment (DORA)](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) is an industry-standard set of metrics for [measuring and comparing DevOps performance](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/), developed by the DORA team, a Google Cloud-led initiative that promotes good DevOps practices.

But metrics are only a compass to identify what’s wrong in the engineering process, [not a solution](https://www.aviator.co/blog/everything-wrong-with-dora-metrics/). And definitely not a way to measure individual performance.

The need to measure everything truly spiked during COVID when we started working remotely, and there wasn’t a good way to understand how work was done. Part of this also stemmed from management’s insecurities about understanding what’s going on in software engineering.

However, when surveyed about the usefulness of developer productivity metrics, most [leaders admit](https://www.atlassian.com/software/compass/resources/state-of-developer-2024) that the metrics they track are not representative of developer productivity and tend to conflate productivity with experience. And now that most of the code is written by AI, measuring productivity the same way makes even less sense. If AI improves programming effort by 30%, does that mean we get 30% more productivity?”

## What Kills Productivity?
Developers are also pretty clear about what would make them more productive. [Atlassian’s State of Developer Experience](https://www.atlassian.com/software/compass/resources/state-of-developer-2024) report has revealed that 69% of developers lose eight hours per week — 20% of their time — to inefficiencies. The key friction points are technical debt (59%), lack of documentation (41%), build processes (27%), lack of time for deep work (27%) and lack of clear direction (25%).

Whether you call it DevEx or platform engineering, the lack of friction equals happy developers, which equals productive developers. In the same survey, 63% of developers said developer experience is important for their job satisfaction.

## The Anti-Metrics Approach: Automated Workflows
That’s why I believe in the anti-metrics approach to developer productivity and focusing on eliminating necessary but mundane tasks that developers confront every day.

Instead of building shiny dashboards, engineering leads should focus on developer experience and [automated workflows across the entire software development life cycle](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-home&utm_term=net-new&utm_content=awareness): [development,](https://www.aviator.co/stacked-prs?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-stackedprs&utm_term=net-new&utm_content=awareness) [code reviews](https://www.aviator.co/flexreview?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-flexreview&utm_term=net-new&utm_content=awareness), [builds](https://www.aviator.co/merge-queue?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-mergequeue&utm_term=net-new&utm_content=awareness), tests and [deployments](https://www.aviator.co/releases?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-releases&utm_term=net-new&utm_content=awareness).

This means focusing on solving real developer problems instead of just pointing at the problems.

Tracking engineering productivity metrics is still important. However, metrics are only a compass to identify what’s wrong, not the solution. Real impact on developer experience comes from balancing three key levers: people, practices and tools.

These tools should rely on five core delivery practices:

**Trunk-based development**
Trunk-based development, per[this definition](https://trunkbaseddevelopment.com/#one-line-summary), is “a source-control branching model, where developers collaborate on code in a single branch called ‘trunk’ *, resist any pressure to create other long-lived development branches by employing documented techniques. The foundational book in the field of software delivery, “[Accelerate](https://www.oreilly.com/library/view/accelerate/9781457191435/),” researched and documented that “developing off trunk/master rather than on long-lived feature branches was correlated with higher delivery performance … independent of team size, organization size or industry.”**Continuous delivery**
Continuous delivery is a practice where code changes are automatically built, tested and prepared for release to production. This approach enables teams to deploy code changes more frequently and reliably and is critical for high-performing engineering organizations. By automating the delivery pipeline, teams can maintain a constant flow of updates while ensuring quality and stability. As[Bryan Finster](https://www.linkedin.com/in/bryan-finster/), a passionate advocate for[continuous delivery](https://minimumcd.org/), put it: Continuous delivery is about always being deliverable, the ability to deploy the latest changes to production at any moment. By automating the delivery pipeline, teams can maintain a constant flow of updates while ensuring quality and stability. Note that continuous delivery is different from continuous deployment, and it’s more important to have a continuous delivery even if the deployment is triggered manually or at a preset cadence.**Monorepos**
A monorepo setup helps establish consistent standards across projects by centralizing build configurations, linting rules and development workflows. This standardization reduces cognitive overhead for developers moving between projects and ensures uniform quality controls. Having all code in one place also simplifies dependency management and cross-project changes.**Small reviews**
Small, focused code reviews help maintain high code quality and developer productivity. By breaking changes into smaller, digestible pieces, reviewers can provide more thorough feedback and catch potential issues earlier. This approach also reduces cognitive load on reviewers and speeds up the review process, leading to faster iteration cycles.**Clear and accurate ownership**
Universal ownership for developer assets promotes well-defined shared responsibility and knowledge sharing across the team. When everyone feels ownership over the codebase, it encourages collaboration, reduces knowledge silos and ensures that any team member can contribute to any part of the project.
While metrics frameworks and dashboards still have a role in engineering organizations, if we really care about developer productivity, we need to stop obsessing over dashboards and start focusing on what actually helps teams do their best work.

As a team of former Googlers, we started looking for tools to replace Google’s EngProd, a team focused on building tools and infrastructure to optimize the engineering process. Since Google builds everything in-house, not everything is easily replicable. That led us to create [Aviator](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-home&utm_term=net-new&utm_content=awareness) — rebuilding Google’s Engineering Productivity (EngProd) on the modern engineering stack to solve collaboration challenges at every stage of the development process, from code reviews to builds, testing, merging and deployment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)