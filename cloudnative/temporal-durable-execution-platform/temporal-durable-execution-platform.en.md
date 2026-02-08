Software reliability is a persistent problem for developers because IT systems are built on unreliable components: hardware degrades; software has bugs; networks drop packets; large language models (LLMs) hallucinate; power fails.

An executing program runs to completion unless:

**A.** The program or OS encounters a bug  
**B.** An external failure, such as a machine losing power or rebooting, occurs  
**C.** There’s a hardware failure

Here’s a small example that illustrates the problem.

As I’m writing this article, I have an electrician working on the fuse boards in my house, and the power has tripped multiple times. My youngest, who is at home modding *Minecraft*, just lost a bunch of work when the power went out. It’s maddening, and happens because RAM is volatile and needs constant power to hold data.

Losing work like this is frustrating enough at home, but imagine the aggravation on an enterprise scale, with thousands of people using the same unreliable systems.

## Reliability through defensive code and hardware redundancy

Traditionally, software engineers have tried to achieve reliability from unreliable components by using fault-tolerant hardware and by designing applications to recover from crashes and failures.

Common hardware approaches to improving reliability include RAID, network interface cards (NICs), redundant power supplies, and on higher-cost machines, hot-swappable CPUs. Disk mirroring with a two-disc array increases the mean time between failures (MTBF) since, while the individual drives still have their own limited MTBF, the array does not fail until both drives fail.

However, as [Tom Wheeler](https://www.linkedin.com/in/tomwheelerstl/), principal developer advocate at [Temporal](https://temporal.io/), tells *The New Stack* in an interview leading up to the company’s annual Replay conference, “As you scale up and move from one server to two, 10, 100, or 1,000 servers, the possibility that any one disk could fail goes up exponentially.” Moreover, hardware-based approaches only protect you from hardware failures.

For software, the most common way to improve reliability is to write code defensively. Senior developers tend to write more defensive code because they’ve seen so many things go wrong.

## Rethinking application development with Durable Execution

Durable Execution encourages a different approach.

Durable Execution platforms such as [Temporal](https://temporal.io/), [AWS Lambda durable functions](https://aws.amazon.com/blogs/aws/build-multi-step-applications-and-ai-workflows-with-aws-lambda-durable-functions/), [Azure Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=in-process,nodejs-v3,v1-model&pivots=csharp), [Cadence](https://cadenceworkflow.io/), [Cloudflare Workflows](https://www.cloudflare.com/en-gb/developer-platform/products/workflows/), [Flawless](https://flawless.dev), [Inngest](https://www.inngest.com), and [Restate](https://www.restate.dev) ensure that your application behaves correctly despite adverse conditions.

They do this by guaranteeing the application runs to completion, storing state information, and reconstructing it if it fails.

As Wheeler explains, the Temporal platform “completely reconstructs the state in a safe way following a crash. The execution continues from that point, so you don’t wind up duplicating steps that had been completed successfully before the crash.”

Durable Execution doesn’t do anything that you can’t build yourself — the concepts have existed in [messaging applications since at least 1990](https://dl.acm.org/doi/10.1145/93605.98721). But doing so is challenging. Developers spend substantial time writing code to store application state in a database and to use systems such as Apache Kafka to communicate state changes to other applications. There are patterns in software development, such as the [transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html) which exists to address problems that can occur when those efforts fail.

Durable Execution makes this unnecessary.

“Durable Execution is a very simple concept, but it has profound implications on the way software engineers approach development,” Wheeler says. “You don’t have to worry about a crash, in the same way that you don’t have to worry about packets being dropped or delivered in the wrong order.”

> “With Durable Execution, your application overcomes those problems, so you can accomplish the goal in a much simpler way.”

He believes this changes how developers view programming. “Developers are conditioned to reduce execution times because the longer a program runs, the more likely it is to encounter problems. With Durable Execution, your application overcomes those problems, so you can accomplish the goal in a much simpler way.”

He continued: “Imagine that you’re onboarding new users who sign up for a SaaS offering’s free tier. You need to track usage and periodically send customized upgrade offers until they cancel or subscribe to a paid tier.

Implementing that might involve a scheduler, an application database, and message queues. With Durable Execution, you don’t need that complexity, because time is no longer the enemy. You can implement it using a for-loop and sleep statements, with durations of days, months, or even years.”

## The mechanics of Durable Execution

A Durable Execution platform’s purpose is to manage state, handle retries, and ensure a sequence of tasks (often long-running) completes successfully even if the infrastructure fails. The core abstraction in Durable Execution platforms is most commonly referred to as a Workflow.

A Workflow is a function that defines the sequence of steps for achieving a specific goal. For example, an e-commerce order-processing Workflow might calculate the total, charge the customer’s credit card, and send a confirmation email.

Steps that could behave differently between invocations — such as calls to external systems — cannot be included directly in the Workflow. Instead, they must be placed in separate functions called Activities, which are referenced in the Workflow.

At runtime, Worker processes on your application servers execute these functions. Each Worker polls the Temporal Service for tasks specifying which function to run next, then reports back. The Temporal Service records details about each task, which includes the completion status and result reported by the Worker, to an append-only log known as the Event History.

If a crash occurs, another Worker can take over, reconstruct the pre-failure state from the Event History, and resume execution.

For this replay mechanism to work correctly, Workflow code must be deterministic — producing the same sequence of commands given the same input. Non-deterministic operations (e.g. conditional logic involving the current time or random numbers) may cause mismatches during replay.

Operations with side effects (e.g., database updates, notifications, disk or network I/O) must be wrapped in Activities. Instead of re-executing previously completed Activities during replay, the platform uses the result stored in the Event History.

Even with this careful approach, there is still a slight possibility that an Activity could be executed twice. Imagine that your Activity uses a payment service to charge a customer’s credit card, and a crash occurs in the milliseconds between the card being charged and the Temporal Service recording the result. The new Worker, unaware that the Activity previously completed, would execute it again.

For this reason, Activities should be idempotent so that repeated calls don’t cause undesirable behavior. Most payment services, as well as many other types of third-party API, allow callers to include an idempotency key along with requests. This key enables these services to identify and ignore duplicate requests.

## How Durable Execution handles persistent processing failures

Any platform that allows for retries risks duplicate transactions, and Durable Execution provides no inherent support for idempotency. However, the risk is reduced because completed activities are not retried.

Another class of errors are persistent processing failures, called “poison messages” in messaging applications. A poison message is one that a receiving application repeatedly fails to process — often due to bad data, an incorrect format, or an application bug — causing it to be rolled back to the queue and redelivered endlessly, potentially creating an infinite loop.

The same pattern can occur with Durable Execution, where an application crashes whenever execution reaches the last recorded event and switches to execution mode. These errors may be transient or persistent.

Transient errors can usually be resolved through backoff and retry, but that technique will not fix a persistent error. For example, if a call to a payment service fails because there’s not enough money in the account, a call two seconds later will probably fail for the same reason. Temporal allows you to designate specific message types and errors as non-retriable, which helps prevent pointless retry attempts.

In the case of a non-transient poison message style error, Temporal and most other Durable Execution platforms allow developers to fix an issue in a running application, also known as “hotfixing.” Applying the hotfix involves temporarily stopping all the Workers, deploying new code, then restarting the Workers. Execution resumes exactly as it would after a crash.

Wheeler explains, “Let’s say that you have an e-commerce application to which you have added some code to calculate a 10% discount for any order over $500. You have this in your workflow code, but let’s say that there’s a typo, so instead of dividing by 10, you divide by zero. That’s obviously an illegal operation, so it’s going to cause a divide by zero exception (or the equivalent in the language you are using). It’s going to fail, and each time you retry, it will fail again.

“But you can go in and fix the code, then redeploy the application. Since it reconstructs the state from before that failure, after you fix it, it will use the new code without the bug. This means that you can fix a live running system in production and enable the application to continue.”

Transient errors, on the other hand, might be caused by service throttling, temporary loss of network connectivity, or temporary service unavailability. Automatically retrying operations that fail due to transient errors improves the user experience and application resilience. However, frequent retries can overload network bandwidth and cause contention.

Exponential backoff is a technique in which wait times increase after a specified number of retry attempts. Temporal, for example, has a backoff coefficient of 2.0 by default, meaning it will retry in 2 seconds, then 4, 8, 16, and so on, up to a maximum of 100 seconds.

## Understanding the Temporal programming model

From a programming perspective, Workers are responsible for executing Workflow and Activity Definitions. The Worker implementation is provided by the Temporal Software Development Kits (SDKs). Temporal supports a wide range of popular programming languages through its SDKs, including Go, Java, Python, TypeScript, .NET, Ruby, and PHP. You can also mix and match different languages.

“You can have a Workflow written in Java that calls an Activity written in Go, and maybe calls another Activity that’s written in TypeScript, and so on,” Wheeler says.

The Temporal Web UI provides details about each execution, both current and previous, which helps developers locate the source of problems.

“When I was a software engineer at Boeing, users would call me to say, ‘The application failed yesterday.’ I would ask, ‘What was the error message?’ and they would respond, ‘I don’t remember. It was yesterday.’ With Temporal, I could just look at the execution that took place yesterday,” Wheeler says.

Temporal also allows you to download an event history in JSON format, and use that to replay an execution in a debugger such as your IDE of choice.

“Nearly every developer has lost countless hours trying to reproduce an elusive bug, the kind that seemingly happens one in a million times, at the most inconvenient time,” Wheeler says. “Instead of grasping at straws trying to reproduce what’s in the bug report, you can just search the Web UI to find the execution where it actually happened, download the JSON file, replay it in a debugger, and isolate the cause.”

Hotfixing enables you to fix and deploy the code. “Perhaps best of all, you can also prevent a regression by making that execution part of your automated tests,” Wheeler adds.

![Temporal Web UI screenshot displays running state with ChargeCustomer activity failing on third attempt due to payment service offline error. ](https://cdn.thenewstack.io/media/2026/02/b3f1e671-unnamed-1-1024x611.png)

Temporal workflow execution states: in a ‘Running’ state with a failing activity (ChargeCustomer)

![Temporal Workflow after successful completion](https://cdn.thenewstack.io/media/2026/02/afbbf4dd-unnamed-2-1024x612.png)

Temporal Web UI screenshot shows completed state with successful workflow execution and charge of $72.74 reflected in the Result panel.

## How Temporal grew from early work at Amazon, Microsoft, and Uber

Although barely six years old, Temporal is based on work that began at Amazon in the mid-2000s. Co-founders Maxim Fateev and Samar Abbas created Amazon’s Simple Workflow Service (SWF). Abbas later worked on the Azure Durable Task Framework at Microsoft, a key component upon which Azure Durable Functions was built. In 2015, they reunited at Uber, where they built a Durable Execution platform called Cadence.

> Temporal has become “increasingly critical” to the reliability of Netflix’s cloud operations since its adoption in 2021.

Due to growing demand for Cadence’s features from other companies, in 2019, they forked the Cadence codebase to create Temporal as a separate open source project. Since then, they’ve added security features, improved performance, added support for multiple programming languages, and enhanced the management interface.

Temporal is used in production by companies across industries, including financial services and retail. In the past two years, it has also been adopted for AI applications, particularly for managing reliability and human oversight in agent-based systems. As Durable Execution continues to mature, it promises to simplify how developers approach building resilient systems.

Netflix was one of Temporal’s early adopters. According to Netflix senior software engineers, Jacob Meyers and Rob Zienert, writing on the [*Netflix Tech Blog*](https://netflixtechblog.com/how-temporal-powers-reliable-cloud-operations-at-netflix-73c69ccb5953): Temporal has become “increasingly critical” to the reliability of Netflix’s cloud operations since its adoption in 2021. “Temporal helped us reduce the number of transient deployment failures at Netflix from 4% to 0.0001%,” they wrote.

For readers wishing to learn more, [the Replay conference](https://replay.temporal.io), hosted by Temporal, is running May 5-7 2026, in San Francisco. Replay is where developers come to push reliability beyond “good enough.” This year, the focus is on AI — everything from AI agents to teaching Claude and Cursor how to program Temporal, and beyond. Register today and make plans to attend.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)