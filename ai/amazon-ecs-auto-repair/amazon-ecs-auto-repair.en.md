Running applications in production means maintaining an “always-on” posture through disruptions. Infrastructure fails; dependencies slow down, and networks partition, not as rare exceptions but as a normal condition of running at scale. Withstanding and recovering from those disruptions is a core requirement, not an afterthought.

In practice, that requirement shows up as a set of moments you may already know. A customer notices an outage, or a page fires, and the underlying cause could be any number of things: a GPU throwing hardware faults that fail the tasks on an instance, an Availability Zone having a networking event, or a logging backend you depend on slowing down and quietly dragging your application with it. None of this is unusual, and none of it waits for a convenient time. What matters is what happens next, and how much of it falls to you.

> “Infrastructure fails; dependencies slow down, and networks partition, not as rare exceptions but as a normal condition of running at scale.”

On Amazon ECS, we aim to handle most of it for you. Failure recovery is a key consideration in how we design and build ECS features. That means you shouldn’t need to build your own detection loops and remediation runbooks for failures ECS can handle itself. For more ambiguous cases, where the right response depends on your workload, we expose the same controls so you can make that call yourself.

This builds on the resilience principles behind ECS that we covered in [A deep dive into resilience and availability on Amazon ECS](https://aws.amazon.com/blogs/containers/a-deep-dive-into-resilience-and-availability-on-amazon-elastic-container-service/): static stability across Availability Zones, pre-scaling capacity, and isolating workloads. Here we focus on the recovery mechanisms that sit on top of those principles and the controls you have over each.

Under the AWS shared responsibility model, AWS is responsible for resilience *of* the cloud, the infrastructure your workloads run on, and you are responsible for resilience *in* the cloud, the way your application is designed to withstand and recover from failure. Much of the work we describe here is ECS taking lessons and patterns from the “of the cloud” side, where we rely on them to keep our own systems healthy, and making them available on the “in the cloud” side, often as sensible built-in defaults that simplify the [operational posture of your systems](https://thenewstack.io/operations-shift-assistants-to-autonomous-multiagent-systems/).

ECS Managed Instances is one example: ECS takes over responsibility for the resiliency of the instance infrastructure your tasks run on. It applies operating system, kernel, and GPU driver patches without compromising your applications’ availability: it fans updates out gradually, watches for failures as it goes, and rolls back when it detects a problem.

AWS Fargate follows a similar pattern: you don’t operate the instance there either, so a bad instance, a bad OS update, or a driver regression is ours to detect and recover from, not a failure mode you design around. From here, we look at how ECS detects and recovers from specific failures: an unhealthy instance, an Availability Zone event, a container or task failure, and a degraded dependency.

## When the instance under your tasks goes bad

Some of the most disruptive failures start below your tasks, at the instance they run on. When an instance degrades, every task scheduled on it is at risk, and the longer it stays in service, the more the failure spreads. For this reason, you want to detect an impaired instance and take it out of rotation as quickly as possible to contain the blast radius.

For example, consider a GPU inference workload running on a fleet of accelerated instances. If a GPU on one of those instances starts throwing correctable ECC errors that escalate into faults, then the tasks on that instance slow down or fail. Or if an instance becomes impaired because of a network partition, a thermal event, Amazon EBS volume degradation, etc., then its tasks [keep running in place with no orchestration](https://thenewstack.io/when-genai-breaks-rigorous-orchestration-keeps-it-running/) behind them and eventually become impaired themselves. Dealing with such impairments yourself would mean building additional automation for detecting impaired instances, draining their workloads, and eventually cycling them, and then maintaining and [operating that automation](https://thenewstack.io/flowai-gives-agents-a-greater-role-in-infrastructure-automation/) reliably at scale. ECS now does this for you automatically.

> “To detect them directly, ECS integrates with NVIDIA’s Data Center GPU Manager (DCGM)… and watches for error classes that indicate a genuine hardware fault.”

On Managed Instances, [GPU health monitoring and Auto Repair](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-ecs-gpu-auto-repair/) close a gap that is easy to miss. Because a GPU is passed through to the instance, most GPU faults that occur inside it aren’t visible to the Amazon EC2 instance status checks that catch ordinary hardware problems so that they can surface only as unexplained task failures or latency. To detect them directly, ECS integrates with NVIDIA’s Data Center GPU Manager (DCGM) on the instance and watches for error classes that indicate a genuine hardware fault rather than transient or non-critical ones.

ECS also monitors the broader health of the data plane instance. This includes EC2 status checks and on-instance data plane components such as the ECS agent and the container runtime. The ECS agent manages the tasks on an instance and keeps them connected to the ECS control plane. When the agent can’t reach [the control plane](https://thenewstack.io/agentic-ai-control-plane-production/), the local state of tasks can drift from their desired state in the control plane, and that drift affects those tasks in ways that are easy to miss. The agent can no longer publish metrics, logs, or health, so the instance becomes a black box. And ECS can no longer reliably stop or replace the tasks on it, so for a service the tasks stranded on the disconnected instance count against its limits and hold up healthy replacements. On Fargate as well as Managed Instances, ECS automatically [detects a sustained loss of agent connectivity](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-agent-connectivity-health/) and treats the instance as impaired; a brief blip that recovers on its own doesn’t trigger a recycle.

In both cases, ECS runs the same continuous monitor-and-repair loop, shown in Figure 1.

![Diagram showing ECS's continuous monitor-and-repair loop ](https://cdn.thenewstack.io/media/2026/10/aa30578a-image.png)





***Figure 1:*** *ECS continuously monitors instance health and, when it finds an impaired instance, drains its tasks, replaces the capacity, and deregisters the instance.*

GPU auto repair and agent-connectivity repair are on by default on the platforms that support them, at no additional cost. You can also track instance health yourself: ECS exposes it through the *DescribeContainerInstances* API and publishes an Instance Health Change event to Amazon EventBridge for Managed Instances and ECS on EC2. That event is most useful when you run ECS on EC2 a your own capacity, where you can consume it to trigger your wn Auto Scaling health checks and instance-replacement workflows, based on [container instance health](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-health.html).

## When an Availability Zone has a bad day

Availability Zones give you fault isolation within a Region, but that isolation only pays off if your workload can absorb the loss of one. Consider a service running across three Availability Zones when one is impaired. Two things tend to go wrong at once. Your surviving tasks are no longer evenly spread, so recovery piles load onto the wrong zones. Traffic between tasks may also cross zone boundaries in ways that widen the blast radius. Rebalancing tasks and steering traffic back to healthy paths by hand is slow and error-prone at exactly the moment you can least afford it.

ECS considers Availability Zone health when it decides where to run your workload. When it detects signs of trouble in a zone, such as elevated task or instance launch failures or health events from other AWS services, it automatically steers new task and instance placements away from that zone until it recovers, rather than adding work to a zone that is already struggling. Furthermore, when an event leaves your tasks unevenly distributed across zones, [Availability Zone rebalancing](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-ecs-az-rebalancing-speeds-mean-time-recovery-event/) corrects it.

ECS continuously monitors how a service’s tasks are spread across Availability Zones, and when the distribution becomes uneven, it starts tasks in the zones with the fewest and, once those are healthy and running, stops tasks in the zones with the most, until the spread is even again (Figure 2). This is on by default for eligible services: those whose first placement strategy is Availability Zone spread, or that set no placement strategy.

Finally, if your service uses Service Connect, you can enable [Zone-Aware Routing](https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/) to route each call to an endpoint in the caller’s own Availability Zone, which keeps traffic within a zone in normal operation and reduces cross-zone exposure when a zone is degraded.

![Diagram showing Availability Zone rebalancing](https://cdn.thenewstack.io/media/2026/10/aa30578a-image-1.png)





***Figure 2:** Availability Zone rebalancing restores an even task distribution after a zonal event, starting new tasks before stopping existing ones.*

For ECS services, ECS spreads tasks evenly across Availability Zones by default, so rebalancing maintains an even distribution. You can ensure enough capacity headroom across zones to handle an Availability Zone outage by pre-scaling: with tasks spread across at least three zones, losing one removes roughly a third of your capacity instead of half, so provision the surviving zones to carry that load. You can refer to the [2023 resilience and availability deep dive](https://aws.amazon.com/blogs/containers/a-deep-dive-into-resilience-and-availability-on-amazon-elastic-container-service/) for this and the other design principles behind resilient ECS services.

## A crashed container shouldn’t cost you the task

Failures can often be localized to a single container inside an otherwise healthy task. When that happens, you’d rather keep the task running and repair it in place than tear it down and reschedule it. A reschedule throws away mostly healthy work and pushes churn onto the scheduler and the rest of your fleet, so recovering in place is the less disruptive choice.

Consider a task that runs a main application container alongside a couple of sidecars, such as a metrics agent and a proxy. If one sidecar crashes, you don’t want to lose the whole task. With a [container restart policy](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-ecs-restart-containers-task-relaunch/), ECS restarts the failed container in place without relaunching the task, so the task keeps serving while the container recovers and you avoid an unnecessary reschedule.

> “A reschedule throws away mostly healthy work and pushes churn onto the scheduler, so recovering in place is the less disruptive choice.”

You choose which containers are eligible and can list exit codes that should not be retried, so a container failing for a non-recoverable reason surfaces instead of restarting in a loop. This matters most when capacity is already under pressure, such as during an Availability Zone event: keeping a task alive by restarting a container in place avoids giving up capacity you would then have to rebuild.

You see the same principle at task launch. On Managed Instances, ECS still tries to pull each image so it picks up any update to the tag, but if that pull fails and the image is already cached on the instance from an earlier task, it falls back to the cached copy and launches the task anyway, rather than failing it over a transient registry or network problem. On ECS on EC2, you can opt into similar behavior with the *ECS\_IMAGE\_PULL\_BEHAVIOR* agent setting. Either way, a transient failure in a dependency you don’t control, a throttled registry or a network blip, doesn’t cost you a task you could have launched from the copy already on the instance.

## Safer defaults, chosen for you

Most of this post is about ECS recovering from infrastructure failures. How your application itself behaves when something it depends on fails is normally your side of the shared responsibility model: resilience *in* the cloud. But in a few cases, we have seen a default work against customers often enough that ECS changed it on your behalf, moving the safer choice into the platform, so you inherit it rather than having to discover and configure it.

Logging is the clearest example. ECS originally supported only blocking log delivery: when the logging backend is slow, throttled, or unavailable, writes to stdout and stderr block, and if the application logs faster than it can deliver, that back pressure can stall or crash it. A large-scale outage in a logging destination could take the application’s availability down with it, even though logging isn’t on the application’s critical path. We later added non-blocking delivery to avoid this, dropping logs that can’t be delivered rather than blocking the container, but it remained opt-in and most customers never enabled it.

So ECS changed the default carefully. Because a minority of workloads genuinely depend on blocking mode, we made the switch in stages rather than overnight: we first shipped the account setting so anyone who needed blocking could opt into it, gave advance notice ahead of the change, and only then moved the default, so customers who required guaranteed delivery had time to preserve it.

> “In effect, the workload now fails open when its logging dependency degrades: It keeps serving and drops the logs it can’t deliver, rather than failing closed.”

Non-blocking is now the default log driver mode, applied to existing and new services without requiring any action, so a logging outage no longer stalls your application by default. In effect, the workload now fails open when its logging dependency degrades: It keeps serving and drops the logs it can’t deliver, rather than failing closed by blocking until the backend recovers.

This is a real durability-versus-availability tradeoff, and the default now favors availability, which is the right choice for most workloads. Customers who must guarantee delivery, for billing, audit, or regulatory reasons, can still choose blocking mode through the [log driver account setting](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-ecs-set-default-log-driver-blocking-mode/) or per task definition.

This is not unique to logging. It is the same reasoning behind spreading tasks across Availability Zones by default for services, starting replacement tasks before stopping existing ones during draining and deployments, and, during a rolling deployment, [replacing a failed task from the version it already belongs to rather than the new version that may still be failing to launch](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-ecs-service-availability-rolling-deployments/). Where a better default helps most customers without taking away control, we make it the default and leave you the option to override it.

## Test it yourself

ECS is integrated with [AWS Fault Injection Service (FIS)](https://docs.aws.amazon.com/fis/latest/userguide/ecs-task-actions.html), which lets you test how resilient your applications are against a range of failure conditions. Its ECS task actions let you run controlled fault experiments against your running tasks, from stopping tasks to injecting resource and network faults, so you can see how your workload and your recovery settings hold up before a real event tests them.

For network faults in particular, we [enabled network fault injection across ECS launch types, including AWS Fargate](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-ecs-network-fault-injection-experiments-fargate/). You can inject latency, packet loss, or a black hole into your tasks and confirm that your timeouts, retries, and fallbacks behave the way you expect when a dependency becomes slow or unreachable. The [sample network faults on ECS Fargate with the FIS project](https://github.com/aws-samples/sample-network-faults-on-ECS-Fargate-with-FIS) is a good starting point.

The approach is the same across every failure in this post, whether a failing instance, an impaired zone, a crashed container, or a degraded dependency: ECS takes on the undifferentiated heavy lifting of detecting it and recovering from it for you, and where the right response depends on your workload, it leaves you the control to decide. You inherit the safe default, and you keep the override.

ECS aims to make it easier for you to design for failure. By handling the routine, mechanical parts of recovery, it frees your effort for the resilience that is specific to your application, and its integration with FIS lets you put that resilience to the test. Treat the defaults and controls in this post as a starting point, tune them to what your workload actually needs, and tell us where the defaults should be smarter.

For the principles behind these mechanisms, see the [2023 resilience and availability deep dive](https://aws.amazon.com/blogs/containers/a-deep-dive-into-resilience-and-availability-on-amazon-elastic-container-service/). To tell us what to build next, see the [AWS Containers Roadmap on GitHub](https://github.com/aws/containers-roadmap).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/10/70f54aac-cropped-4666a336-anirudh_aithal-scaled-1-600x600.jpeg)

Anirudh Aithal is a Principal Engineer at Amazon Web Services, where he works on Amazon ECS and Amazon EKS. He has worked on Amazon ECS since its earliest days, building fundamental pieces of the platform such as IAM roles for...

Read more from Anirudh Aithal](https://thenewstack.io/author/anirudh-aithal/)