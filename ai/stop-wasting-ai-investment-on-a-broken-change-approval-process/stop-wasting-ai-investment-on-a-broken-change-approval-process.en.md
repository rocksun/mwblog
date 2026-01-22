Change approval has been a constraining force on software delivery for decades. With teams adopting AI coding assistants and agents, the quantity, size and complexity of changes is making a bad problem worse.

For many organizations, [investments in AI for developer productivity](https://thenewstack.io/developer-productivity-in-2025-more-ai-but-mixed-results/) are failing to yield meaningful returns, and committee-based approval is often a contributing factor. Where organizations are unwilling to streamline their change approval process, investments in improving productivity elsewhere are a total waste.

Streamlined change approval relies on a combination of peer review during the development process and automation to detect bad changes early and prevent them from progressing through the delivery pipeline.

## A Simple, Pivotal Idea: Working in Small Batches

There’s a simple idea at the heart of modern software delivery that drives all the other things you can do to improve throughput, stability, quality and compliance. It’s called “working in small batches.” The idea is so simple, yet many organizations dismiss it.

“Perhaps a small company or a startup can work in small batches,” they say. “But we are regulated!”

The idea that [regulation requires large batches is nonsense](https://thenewstack.io/stop-blaming-regulation-for-poor-software-delivery-performance/). If you review proposed rules on cybersecurity, you’ll see that small batches and short lead times will be a significant compliance advantage. Small batches achieve safety, security and compliance far better than large batches.

Large batches are like a virus. When any part of your software delivery pipeline moves in large batches, it forces the batch size across the entire pipeline. That means you end up with a pipeline sized to the largest batch in the delivery process. This is often the time it takes to test a software version manually or the cadence of change approvals.

To deliver software in small batches, you must identify where the batch size is being set and reduce it at that stage by improving the process, automating steps and finding ways to minimize friction. This is where continuous delivery has so much power. It encourages testing to become a continuous activity, and it demands that approvals are a continuous part of the delivery pipeline.

## Proven By Research and Experience

There’s a wealth of research that examines how batch size affects software delivery throughput, quality and risk. [Google’s](https://cloud.google.com/?utm_content=inline+mention) long-running [DORA (DevOps Research and Assessment](https://dora.dev/research/)) program includes small batches in its capability model alongside streamlined change approvals. You can see how these relate to each other, as we know that the number of changes will be forced to increase if the change approval process is slow and heavy.

Lightweight change approvals are broken down further in [Octopus Deploy’s](https://octopus.com?utm_content=inline+mention) “[Compliance through Continuous Delivery” report](https://octopus.com/publications/compliance-through-continuous-delivery), which defines them as having four qualities:

* **A healthy approval chain**: When a chain of approvals is required, it should include sign-off from both the team and the direct manager.
* **Few manual approvals**: Having many manual approvals creates a compound delay in the change approval process.
* **No cross-team committees**: Change approval boards and committees are the worst approach to change approval.
* **Approvals captured in deployment/ITSM tools**: Capturing approvals within deployment and ITSM (information technology service management) tools reduces approval friction.

Lightweight change approvals, combined with reliable deployments, increase software delivery throughput and the attainment of governance, risk and compliance goals.

[![](https://cdn.thenewstack.io/media/2026/01/e3596b21-image1-1024x599.png)](https://cdn.thenewstack.io/media/2026/01/e3596b21-image1-1024x599.png)

While Fred Brooks, author of “The Mythical Man-Month,” warned us that there are no silver bullets, it’s fair to say that software delivery is overrun with supernatural monsters. These can be effectively banished with the silver bullet of small batches. When you decide to shrink your batch size, you must resolve inefficiencies throughout your software delivery pipeline, and change approvals is one beast that haunts this particular forest.

While the statistics are valuable evidence for small batches and lightweight change approvals, we also have three decades of experience from practitioners that confirm this. This experience has been documented in many software approaches, by [Kent Beck](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658) (extreme programming), [Dave Farley and Jez Humble](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912) (continuous delivery), [Mary and Tom Poppendieck](https://www.amazon.com/Lean-Software-Development-Agile-Toolkit/dp/0321150783) (lean software development) and [David Anderson](https://www.amazon.com/Kanban-Successful-Evolutionary-Technology-Business/dp/0984521402) (Kanban).

## Zooming In On Code Review and AI

Within the broader topic of change approval, we also have the small but mighty [problem of code review](https://thenewstack.io/the-anatomy-of-slow-code-reviews/). Large change sets, heavyweight code review processes, asynchronous reviews and failing to run [test automation before check-in all reduce delivery speed](https://thenewstack.io/cloud-based-automated-testing-increases-speed-in-a-flash/). [Problems in code review are detrimental to software delivery performance](https://thenewstack.io/ai-wont-fix-your-software-delivery-problems/) and undermine the benefits of approaches like GitOps.

If you use AI to generate more code in a short period, the existing bottleneck of code review will become significantly worse. You’re likely to increase batch sizes, triggering a vicious cycle that leads to longer waits, more extensive reviews and significant quality issues. When you have to wait longer to receive feedback on a review, you start saving up more changes for each review, which amplifies the problems even further.

In the “[State of AI vs. Human Code Generation Report](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report),” released in December, [CodeRabbit](https://www.coderabbit.ai/) analyzed 470 open source pull requests to compare AI-generated changes with those made by humans. AI made 1.7 times more mistakes than developers, with a higher rate of major and critical errors. That means that, as we increase the burden of code review, it has also become even more crucial.

Many organizations are responding to this by adding tools, like [Gemini Code Assist](https://codeassist.google) or CodeRabbit, to speed up code review. This is only part of the solution to addressing a bottleneck like this. Adding tools isn’t enough, and we need to think systematically about constraints.

Eli Goldratt, the business management guru, said there can only ever be a single constraint in your system. It’s the weakest link in the chain, so no matter what you do to the other links, the chain can never be stronger than that single weakest link. There are five focusing steps to manage constraints:

* **Identify**: You must find the one true bottleneck.
* **Exploit**: Get the most value from what you have.
* **Subordinate**: Pace everything else to the bottleneck.
* **Elevate**: Invest in expanding capacity at the bottleneck.
* **Repeat**, as the bottleneck may have now moved.

If you’ve identified code review as your bottleneck, you should first exploit it. You must determine how to maximize the value from the code review process. This may be as simple as prioritizing the most valuable changes in the code review queue.

Next, you subordinate the software delivery pipeline by setting the pace of all stages to match the speed at which you can process code reviews. Stages after code review are naturally limited because work can only begin once the review is complete, so you should limit the introduction of work in the stages preceding code review to match its pace.

If a developer can’t start new work due to work-in-progress limits, they may be able to take on some of the code review workload, and the whole system improves as a result.

Finally, you elevate the constraint, which means improving the rate at which you can complete code review. At the top of your list should be working in smaller batches, as this means smaller code reviews, which are easier to understand and review.

You can also automate many tasks to lighten the load on the human reviewer. You can use linting tools, automated tests and static analysis to give [faster feedback to developers](https://thenewstack.io/the-future-of-secure-development-faster-and-safer-code/) without needing human review. That means the scope of the code review is narrower and more focused. The AI code review tools for summarizing and checking changes may be helpful at this stage.

The crucial wisdom within the five focusing steps is that if you skip to the elevating stage, you end up automating things that you could have removed or solved without investment.

## It Really Is About Smaller Batches

Everything ultimately comes back to working in small batches. Reducing batch size is a substantial positive driver of improvement. Automation makes sense when it enables tiny change sets that are deployable on demand. Small batches guide your tool choices and process improvements, and the results in terms of product, team and organizational performance will show you that it works.

When you examine your change approval process, you may be tempted to think that it doesn’t make sense to work in such small batches, as each one requires assembling the entire change approval board. In reality, a change approval board doesn’t make sense when you can work in such small, low-risk batches.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a six-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)