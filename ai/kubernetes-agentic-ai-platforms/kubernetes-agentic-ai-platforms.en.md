**AI workloads, including those using agentic AI**, will only add to and change the questions Kubernetes teams have to answer. It’s no longer merely enough to ask if the pods are running. Or how long it takes a model to produce its first token. Or what happens when inference traffic spikes and no additional GPU capacity is available.

Increasingly, questions like those are becoming platform questions that sit next to the already familiar work of upgrades, recovery, and security.

That’s why *The New Stack* has just published ***[Kubernetes in 2027: Building Platforms for AI, Autonomy, and Scale](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)****,* a new ebook by Chris J. Preimesberger, in partnership with HPE.

[![](https://cdn.thenewstack.io/media/2026/10/3c198509-screenshot-2026-10-26-at-15.38.15.png)](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)

This ebook starts with the work *before* launch — before the launch. We ask teams to stress-test model-serving systems under realistic loads, rehearse failures, and measure more than GPU utilization.

It also takes a clear-eyed look at agents. Giving an agent access to a cluster is a consequential decision, even if its task sounds routine.

The guide calls for identifiable owners, narrow permissions, approval gates, and audit trails that connect tool calls to the task that prompted them. It asks teams to evaluate AI output quality. A fast answer offers little comfort when it’s wrong.

And the ebook doesn’t treat AI as a reason to forget the rest of the platform. The checkpoints cover policy across clusters, visibility into services outside Kubernetes, upgrade and restoration drills, operational ownership, and developer self-service.

**The [checklist](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/) gets specific** about the work that can fall between teams.

Can you see which clusters follow a shared access and network baseline? (And who approved the exceptions?)

Also: When an application slows, can you look beyond pod metrics to the database, virtual machine, network, or external service it depends on? Before the next upgrade, have you checked for removed APIs and practiced restoring both cluster state and application data?

Then there’s the work after deployment: Who renews an ingress certificate? Who signs off on a capacity change? If a developer requests an environment through a service catalog, does it come with an owner, a review date, and a way to see what it costs?

They’re practical prompts for conversations among platform teams, application teams, security teams, and business teams. **[Download the ebook now before you start the conversation](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)**.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/b0ce81f3-cropped-5f5868db-nick-luchessi-2-600x600.png)

Nick Lucchesi serves as the editor-in-chief of The New Stack, where he directs editorial strategy and oversees coverage of the technologies and professionals driving software development, deployment and management at scale. Before joining The New Stack, Lucchesi held the position...

Read more from Nick Lucchesi](https://thenewstack.io/author/nick-lucchesi/)