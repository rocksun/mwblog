On a large enough GPU cluster, something is always breaking. That’s just a fact of life. The standard fix is rolling back to the last checkpoint and recomputing everything since, which is both slow and costly. <https://clockwork.io/> wants to make that fix obsolete — and it’s willing to put a guarantee on it.

The basis for Clockwork’s ability to prevent failures from stopping the training run is TorchPass, [Clockwork’s fault tolerance product](https://thenewstack.io/clockworks-fleetiq-aims-to-fix-ais-costly-network-bottleneck/), which reached general availability in March. When a GPU or a whole node fails, TorchPass can move the training job’s in-memory state, including model weights, gradients, and optimizer state, onto a healthy spare GPU — or one that is running a lower-priority job — and keep the job running, typically recovering in just a few minutes.

On Wednesday, the company launched its YOCO Guarantee, short for “You Only Compute Once.” The company guarantees that 90 percent of failures on a supported training run will be resolved with no lost progress, no checkpoint rollback, and no recompute. If Clockwork falls short in a given contract year, the customer gets a 25 percent credit toward their next renewal or expansion.

> “AI teams need their models to be done, not their nodes to be up.” — Suresh Vasudevan, CEO of Clockwork.

[Suresh Vasudevan](https://thenewstack.io/keeping-gpus-ticking-like-clockwork/), the CEO of Clockwork, says, “AI teams need their models to be done, not their nodes to be up. The industry has been measuring node uptime and calling it reliability. YOCO holds us accountable for the only thing that matters — your model, done.”

![](https://cdn.thenewstack.io/media/2026/07/416b318b-screenshot-2026-07-01-at-9.40.11-am-1024x567.png)

TorchPass vs. TorchFT. Credit: Clockwork.

## Live migration instead of rollback

Dan Zheng, Clockwork’s chief business officer and co-founder, tells *The New Stack* what the current status quo looks like: “If you take checkpoints periodically and something fails, you have to go back to the previous checkpoint, which can be an hour, two hours ago. You have to recompute.”

None of that recomputed work is free, of course. Teams have to pay for the expensive GPU time to redo work they already did.

TorchPass gets around these rollbacks by moving the job while it’s still running. “On a very high level, I like to think of it as almost like a vMotion, but this is for GPU, so sort of like a gMotion,” Zheng says, referring to VMware’s term for [shifting a running virtual machine](https://blogs.vmware.com/cloud-foundation/2019/07/09/the-vmotion-process-under-the-hood/) between physical hosts without downtime.

But this replacement has to come from somewhere, of course. “If one of the GPUs fails and you have access to a spare node, this can be a standby node, or it can be a node that’s running low-priority jobs,” Zheng says.

A team can set aside idle nodes as dedicated spares, or, to avoid paying for idle GPUs, let TorchPass pull one from lower-priority work, shutting that job down, bringing the node into the training cluster, and rebuilding the connections between GPUs so the run resumes at the next step instead of the last checkpoint.

TorchPass also doesn’t have to wait for something to break. It can move a job before a failure, when the warning signs are already there. “If the temperature is exceeding a certain threshold, you know the GPU is going to fail at some point,” Zheng says. “Why don’t I do something about it while I still have access to the GPU memory?”

![](https://cdn.thenewstack.io/media/2026/07/3f700120-screenshot-2026-07-01-at-9.40.43-am-1024x567.png)

Credit: Clockwork.

## How to enable Torchpass

TorchPass comes in two modes that differ mainly in how much state each has to move and how fast it can recover because of that.

The fast option is model-aware and, as Zheng describes it, only takes a few lines of extra code. This allows TorchPass to know exactly what to grab, so it can move less data and recover in tens of seconds.

The other is what the team describes as ‘model-transparent.’ To use it, the training teams don’t have to change anything in the training code. “We’re able to take a system-level snapshot,” Zheng says. That’s an easier way to use TorchPass, but in exchange, it moves more data and takes a few minutes to recover.

A sudden crash is still an issue, though. TorchPass can’t snapshot a node that’s already dead, after all. For that case, Clockwork says it rebuilds the lost worker’s state from the healthy data-parallel replicas the job is already running, the copies that exist for parallelism in the first place.

TorchPass has its limits, and Zheng acknowledges as much. “If the whole network goes down, there’s nothing you can do about it,” he says. “It’s like the power goes out completely — there’s nothing anyone can do about it.”

![](https://cdn.thenewstack.io/media/2026/07/852d9fe9-screenshot-2026-07-01-at-9.41.35-am-1024x567.png)

## What a failed run really costs

Failures are not rare events at scale. Research from Meta’s FAIR team, cited in Clockwork’s announcement, puts the mean time to failure on a 1,024-GPU cluster at 7.9 hours; at 16,384 GPUs, it drops to 1.8 hours. The result, Clockwork says, is that GPU clusters effectively run at 30 to 50 percent of their theoretical performance. But the hardware isn’t the bottleneck, the team argues, it’s the reliability model around it that assumes failures are far rarer than what these clusters actually see.

Clockwork estimates that failure-driven restarts drain more than $6 million a year in wasted compute on a typical 2,048-GPU H200 deployment.

## ‘Not for Anthropic and OpenAI’

“This solution is not for Anthropic and OpenAI, because they have the engineering bench strength,” Zheng says. “It’s not for Google. It’s really for everyone else.” He means the AI-native startups, enterprises, and quant and biotech shops that want what he calls “Frontier AI Lab level of resilience” without building it themselves.

That market is growing as more of the work shifts from pre-training to post-training and reinforcement learning, which is putting more teams in front of large training jobs than a year ago. Clockwork says its customers already include neoclouds Nebius, Nscale, and WhiteFiber, along with DCAI and enterprises such as Uber and Wells Fargo.

Awareness is still catching up, though. “A lot of people we talk to are so used to checkpoint-restarts, they don’t even know there’s something else available,” Zheng says.

## What the testing showed

The most common alternative is just the status quo, Clockwork says. Teams checkpoint often and eat the recompute when something breaks.

The other is [TorchFT](https://github.com/meta-pytorch/torchft), the open-source framework Meta released in late 2024, which keeps a job going by dropping an entire replica group when a GPU fails and continuing without it until it’s replaced. Clockwork says that approach carries a per-step overhead, even when nothing is failing, and the company is positioning TorchPass as the lighter-weight option for more modest jobs that run on hundreds or low thousands of GPUs where failures don’t happen every couple of minutes.

SemiAnalysis ran some independent benchmarks on TorchPass.

“There’s a big difference between a vendor making a slide that says their product works and them writing it into a contract,” says Jordan Nanos, a member of technical staff at SemiAnalysis and lead author of its ClusterMAX benchmark. “In our testing, TorchPass delivered the fastest and most efficient fault-tolerant performance for a GPT-OSS-120B training run on a 64x H200 cluster when compared to checkpoint-restart on job completion time. TorchPass also outperformed TorchFT (in terms of MFU and tokens/sec/GPU) for this job, while matching its recovery time. The YOCO Guarantee just reflects what we saw in testing, and makes it contractual.”

## Reliability as a software layer

“I like to think back on my early Google days, like the Google File System,” Zheng says. “You have commodity spinning hard disks, but from a developer perspective, you want to write once and make sure your data is persisted. You don’t care if someone needs to swap a disk in the data center.”

“We need to have that resiliency layer at the software level too,” he says, “so that as a developer or an AI researcher, you have a higher level of confidence. You just focus on training, you don’t have to worry about infrastructure.”

## Observability

Clockwork was born out of a project that had quite a different mission from where the company is now: synchronizing server clocks. But because that also involved very precise measurements of the latency between those servers, the team realized it could learn a lot about a cluster just from doing that. The company has expanded on this ever since and it’s worth noting that observability is still a core part of what Clock work does.

Zheng says TorchPass and Clockwork’s monitoring tools are complementary. “It goes hand in hand with TorchPass in a way that, if you identify problems, you can migrate,” he says.

Much of the company’s newer work is actually going into observability. Its fleet-monitoring tools can now trace a fabric problem down to a specific link or switch, Zheng says, and Clockwork is piloting that capability with a couple of large cloud operators. Catch a degrading GPU or a congested link early enough, he says, and TorchPass can move the job before the failure ever lands.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)