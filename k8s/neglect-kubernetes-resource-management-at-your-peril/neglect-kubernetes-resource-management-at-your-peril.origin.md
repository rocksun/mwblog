# Neglect Kubernetes Resource Management at Your Peril
![Featued image for: Neglect Kubernetes Resource Management at Your Peril](https://cdn.thenewstack.io/media/2024/06/f610ce37-neglect-kubernetes-resource-management-peril-1024x576.jpeg)
When I opened our first [Kubernetes](https://thenewstack.io/kubernetes/) cluster to hundreds of users in 2016 as the platform engineering manager of a large bank, I borrowed the phrase “benign neglect.”

That *supposedly* benign neglect was about managing Kubernetes resource primitives. While I understood that [migrating to Kubernetes](https://roadmap.sh/kubernetes) allowed us to constrain the minimum and maximum resources used by each container, something we could not do on our legacy grid computing system, it presented many new challenges. First and foremost, I needed to determine appropriate values to set for those constraints. Subsequently, I needed to educate users on how and why to use them.

I decided to set some loose defaults to start, and I hoped that the “Kubernetes invisible hand” would magically take care of the compute resources until someone came along with a better solution that would scale efficiently. It took only a few days for my plan to backfire, with users complaining that they could not schedule pods due to a lack of resources. Meanwhile, the internal virtualization team called me, confused about how the entire cluster had only 15% CPU utilization on the virtualization layer, yet hundreds of users were unable to access the available resources.

This was how I learned that my neglect was far from benign. My Kubernetes journey was off to a rough start.

## Why You Need to Manage Kubernetes Resources
Avoiding the widespread issues in my Kubernetes rollout required a nuanced approach to managing [Kubernetes resources](https://thenewstack.io/understanding-kubernetes-resource-types/). Specifically, I needed a different strategy for managing the two key settings that Kubernetes provides to constrain resources.

In Kubernetes configuration, requests are used to set the minimum resources a container is guaranteed to access, while limits constrain the maximum resources a container can consume on a node. Together, they allow users to isolate CPU and memory. While these are conceptually straightforward, finding the optimal values can be extremely challenging — especially at scale.

My experience in 2016 revealed a few major problem areas that result from not managing resource [requests and limits](https://thenewstack.io/kubernetes-requests-and-limits-demystified/) effectively. The first is poor reliability and unpredictable performance. When workloads request too few resources, they’re underprovisioned, leading to resource contention on nodes (which yields CPU throttling, out-of-memory kills and pod eviction). The second is high cloud costs. When workloads request more resources than they need, they’re overprovisioned, leading to low node utilization, which translates to cloud bills that are two to three times higher than necessary.

As I progressed down what I now see as the typical resource management journey, I discovered a third central problem area: overwhelming engineering teams with toil. At scale, manually tuning resources quickly overwhelms both developers and platform teams.

Learning about this the hard way was a messy experience. Let’s take a closer look at how these challenges played out for me as a [platform engineering](https://thenewstack.io/platform-engineering/) manager in the early days of Kubernetes adoption.

## Phase 1: The ‘Do Nothing’ Solution to Resource Management
Not bothering to set requests and limits at all is typically where people start their [Kubernetes resource management](https://thenewstack.io/optimizing-resource-management-using-machine-learning-to-scale-kubernetes/) journey. This becomes a problem because when workloads don’t have sufficient resources, applications suffer from poor reliability, unpredictable performance or outages.

When resource requests are too low or not set at all, the Kubernetes scheduler places pods on nodes too densely, preventing each pod from getting the CPU or memory resources it requires. I had already learned this lesson from my experience with grid computing, which was one reason I was chosen to lead the Kubernetes implementation. I knew that an inability to properly allocate CPU and memory could cause serious production issues.

Due to the grid computing platform’s inability to isolate CPU resources for individual workloads, we regularly experienced outages, processing delays and other major performance problems. With millions of tasks running every day, the impact was significant. But the lack of limits on memory utilization turned out to be worse. We experienced a snowball effect over time where a memory leak would cause a node to go down, sending all other tasks to the remaining nodes, which also had memory leaks. At one point, we were experiencing monthly outages on the grid due to the lack of isolation, with memory leaks and/or runaway processes resulting.

Because I got burned by those grid outages so many times, I effectively skipped this phase of the resource management journey and set requests and limits on “Day 1,” but most people don’t start out with this awareness.

## Phase 2: The ‘One-Size-Fits-All’ Solution
Understanding the performance impact of not setting requests and limits, I took a one-size-fits-all approach. I chose to set a generous default resource quota (3% of the entire cluster capacity per namespace), and started onboarding users.

While we successfully provisioned 120 namespaces in just a few days, we had onboarded users to consume up to 360% of the resources that we had (with only 10% CPU utilization and 30% memory). If we had been running in production at that point, we would have tripled the cost of our cluster in a few days.

When I released the first clusters, I naively assumed that setting generous requests and limits by default would provide a smooth onboarding experience. Soon after, developers would learn about pod usage and fine-tune them on a second pass. I was wrong.

Developers took the generous default values for granted and never looked back. If asked to pick a more appropriate resource level, they instinctively chose what the workload had required when running on virtual machines (VMs), which was typically much higher than needed. It was also more costly, but developers’ main priority is performance. There’s no incentive for them to avoid overprovisioning, which is why it’s such a widespread issue. It was quickly clear that I needed to find a different solution.

## Phase 3: The ‘Brute Force’ Solution
In the weeks after the initial Kubernetes rollout, a cyclical scenario played out. Users complained their pods were pending due to a lack of cluster resources. We reduced the default requests and limits and restarted all the workloads across the board to use the new values, which was very disruptive. During this process, some pods that were running were momentarily unscheduled due to the lack of cluster resources.

Although freeing up cluster resources was beneficial, specific workloads failed to start with the new default request and limit values. That caused a fire drill to fix them by hastily adding custom requests and limit values. Meanwhile, users called me asking what was happening. What a mess!

At the same time, more applications and users were onboarded because we now had resources, but we were promptly back to where we started with a lack of cluster resources, so users couldn’t schedule pods. Eventually, I set default requests and limits to really small values to motivate (or basically force) developers to deploy their [CPU and memory requests](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/).

This brute force solution was plagued on many levels. Manually optimizing requests is a tedious task on its own, but what makes it even more grueling is that you can’t just set them and forget them — they need ongoing attention. It’s essential to monitor resource consumption on pods to reconfigure settings as application usage changes. A continuous cycle of adjust-monitor-adjust ensures reliability and performance while [keeping cloud costs in check](https://thenewstack.io/how-platform-engineering-can-help-keep-cloud-costs-in-check/), but it amounts to a lot of manual work for developers. It’s like being trapped on a hamster wheel they can never get off.

Developers weren’t the only ones who felt the pain. At this stage, many users came to me asking for guidance on setting up their requests and limits, and they expected my platform engineering team to troubleshoot each application individually. This became a series of tedious conversations in which platform engineers asked developers some common sense questions about how their application is built and how it consumes resources.

To make matters even more complicated, some of the issues were so complex that solving them required multidisciplinary skills — morphing a platform engineer into a hybrid infrastructure site reliability engineer (SRE), software engineer and CI/CD specialist. I could see how the effect of this over time would be for platform teams to build extensive tooling to support these efforts, leading to ongoing development and operational burden for teams that are already stretched thin.

While this brute force solution kind of worked, it wasn’t scientific, and it required a ton of manual toil, which wouldn’t work at scale. I knew we needed a more automated solution, but it didn’t exist at the time.

## The Ultimate Solution: Machine Learning and Automation
A few years later, I finally found the solution to precisely setting all pod requests and limits without “guesstimation,” manual toil or complex operational burdens. I immediately recognized the value when I was approached to help build out a platform for discovering, aggregating and writing metrics to feed [machine learning that would be used to automatically apply Kubernetes](https://thenewstack.io/using-machine-learning-to-automate-kubernetes-optimization/) resource settings.

By continuously calculating and automatically applying optimum combinations of resource requests and limits, tools like StormForge [Optimize Live](https://www.stormforge.io/optimize-live/?utm_source=The%20New%20Stack&utm_medium=article&utm_campaign=Rafa-manifesto) help save platform teams from performance degradation, outages, high cloud costs and poor developer experience.

Neglecting Kubernetes resource management is not a choice you can afford to make. Now, it’s a choice that you no longer *have* to make. See how you can let machine learning and automation do it for you with a [free trial of Optimize Live](http://app.stormforge.io/signup?utm_source=The%20New%20Stack&utm_medium=article&utm_campaign=Rafa-manifesto) or play around in our [sandbox environment](https://www.stormforge.io/sandbox/?utm_source=The%20New%20Stack&utm_medium=article&utm_campaign=Rafa-manifesto).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)