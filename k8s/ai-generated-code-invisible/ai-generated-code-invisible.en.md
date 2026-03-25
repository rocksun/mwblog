For this edition of *The New Stack Makers*, I sat down with Brendan Burns, one of the co-founders of Kubernetes, to talk about how AI is changing the infrastructure he helped create. After his work on Kubernetes at Google, Burns joined Microsoft a decade ago and now runs Azure’s container infrastructure and resource management organization of about 1,400 engineers and PMs.

And unlike many developers who climb the corporate ladder, he still maintains several Kubernetes client libraries himself. “I’d rather write code than watch YouTube,” he says.

VIDEO

> “Did you forget that 100% of your code was machine-generated if you used a compiler? We stopped caring about that code.”

In this wide-ranging conversation, we talk about how AI workloads are forcing Kubernetes to adapt in ways its creators didn’t anticipate, why monitoring AI apps means rethinking what “working” even means, and why Burns believes AI-generated code will eventually be treated the same way we treat assembly: as a transient artifact nobody reads.

## GPU scheduling is more than “another resource type”

When Burns built Kubernetes, the scheduler cared about two things: CPU and memory. GPUs have added a third, but they aren’t just another fundamental resource to allocate. They come with additional hardware requirements, such as fast interconnects, that make co-location essential.

“It’s not just ‘I want one thing on this machine,’” Burns says. “It’s ‘I want these two things to land on the same machine. I don’t care which machine, but land them on the same machine.’”

That’s gang scheduling, one of several adaptations Kubernetes has had to make for AI workloads. To surface GPU topology to the scheduler, Microsoft partnered with Nvidia and others on Dynamic Resource Allocation, a Kubernetes primitive that lets hardware vendors describe what’s available on a given node in a generic way.

The overall workload profile has changed, too, Burns says. Kubernetes was built for online, stateless services. If one container (or its underlying hardware) failed, that was ok, because others could just be spun up and take over. AI model training is also batch workload, but as Burns notes, it’s checkpoint-sensitive. Even a basic hardware failure can often mean rolling back hours of compute that potentially cost a lot of money. Burns says AI training workloads “treat failure as a really bad thing” in ways the original stateless Kubernetes model didn’t account for.

Then there’s utilization when it comes to putting those models into production. Inference spikes during the day and drops at night, but those high-end GPUs don’t stop costing money when they go idle. Teams want to use them for training and fine-tuning during off-hours, which means the scheduler needs to preempt and reschedule, another capability Kubernetes wasn’t designed for.

Burns’ team is adding AI-native primitives on top of Kubernetes through projects like [KAITO, the Kubernetes AI Toolchain Operator,](https://learn.microsoft.com/en-us/azure/aks/ai-toolchain-operator) which handles distributed inference and fine-tuning orchestration via custom resources.

The pattern here is similar to how service meshes came to Kubernetes, Burns says: new capabilities layered on through the extension model. This pattern is also part of the overall reason why Burns thinks Kubernetes is so successful: “Vendor-neutral open source is critical to success. You have to have that ability to have multiple different companies bet on a single solution.”

## AI monitoring has to be different

Building models and running them isn’t what most companies will do, though. What they want to do is build applications on top of those models. And that creates its own set of new challenges, especially when it comes to observability.

“Now suddenly, your monitoring has to shift — your monitoring has to have a human component,” Burns says. “It can’t just be error rates. It has to be saying, ‘did I give a good answer back?’ Not just did I get an answer back, but did I get a good answer back?”

One way Microsoft and others do this is by asking users for feedback with basic thumbs-up/thumbs-down buttons. What happens here is that teams often get dismayed by a high thumbs-down rate, Burns says. But the reason for that is pretty straightforward: users who get a good answer don’t click anything.

“It’s a relative metric, not an absolute metric,” Burns says. “If you take your thumbs-down rate from 50% to 40%, that’s a good thing. If it goes from 10% to 20%, that’s a bad thing, even though you’d say, well, 20%, it’s not bad.”

For testing, Burns borrows a model from his web search days at Google: you don’t test one query, you test 10,000. The same principle applies to Ai apps. You have to run thousands of prompts through the system and then evaluate whether the responses improved. To do that at scale, using another LLM as the evaluator is often the only option and while this signal isn’t perfect, it’s good enough to tell you which direction you’re heading.

Another way of testing, by using 1% experiments, used to be the domain of user experience teams. But Burns argues that this kind of testing now needs to be run across the entire stack. For engineers working on AI apps, it’s the only way to see how their changes perform against real user behavior.

“[Users] are trying to get something done. If they’re chatting with this thing for 10, 15, 20 iterations, you might not be giving them the right answer,” Burns says. “But even getting access to the chats is tricky. People need to opt in to sending us the data for us to be able to see the interactions. So there are all of these complexities that weren’t there when you were just like: did my shop page render? Did I send the HTML back correctly or not?”

## Code review is just a phase

Much of the current discussion around coding agents centers on whether all of this code can even be reviewed before it goes into production. Burns says many senior leaders tell him that they need more principal engineers to handle all the AI-generated code that needs reviewing.

“I think you’re doing it wrong,” he tells them.

Burns pushes back on two levels. The first is practical: if AI is producing more code, then reviewing code is no longer an implicit skill picked up after a few years of grunt work — it’s something junior engineers need to learn on the job, just as a previous generation had to learn version control.

“The job is actually changing so that everybody’s job is to review code,” Burns says.

But Burns also thinks the current focus on code review is itself a phase.

“I see these stats that are like, 97% of our code is machine-generated or whatever,” he says. “And I’m like, did you forget that 100% of your code was machine-generated if you used a compiler? And we stopped caring about that code.”

Nobody reviews compiler output anymore, Burns says. The test suite validates it, and developers implicitly trust the compiler to get it right. Burns argues that as AI testing frameworks and specifications improve, AI-generated code simply becomes a transient artifact that is regenerated on every run and never intended for human review. “What’s important is the spec and the tests,” he says.

And then there’s the question of the languages themselves. Burns compares the current state of AI coding to “building a self-driving car by building a robot to hang on to the steering wheel.” AI today writes in languages designed for human readability. But programming languages with stricter formal guarantees have always existed. Humans didn’t like writing in them because the ergonomics felt restrictive, Burns argues, but AI won’t have that problem.

“What does the programming language of the future look like? And is it really intended for humans to write?” Burns asks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)