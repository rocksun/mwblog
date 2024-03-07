# eBPF Profiling: The Key to System Insights
Unreliable data becomes a thing of the past when you learn how to unlock detailed insights with eBPF profiling. Discover how to monitor CPU, memory, and network data granularly and efficiently.
Conventional monitoring and observability tools are like the algorithm that estimates how much battery time you have left on your phone: they're good at keeping track of how many resources your phone (or server) is using in total. They can also provide some basic projections about when you might run out of resources and suggest changes you can make (like shutting off idle apps on your phone, or moving a workload to a different node in the case of observability) to increase resource consumption efficiency.
But they're not so good at providing detailed, specific, granular data. Your phone can't tell the minute and second when it's going to run out of power. In most cases, it can't even tell you with precision exactly which apps are sucking up the most power. Likewise, traditional observability tools only give you an overview of what's happening in your system; they don't generate detailed profiling data or insights.
Fortunately, there's a better approach: eBPF profiling. Using eBPF, a neat little technology built into modern Linux kernels, you can perform continuous profiling for a variety of resources. Even better, eBPF-based profiling imposes minimal overhead on your applications, so you don't end up wasting lots of memory and CPU just to figure out what's happening with your memory and CPU.
Allow us to explain by walking you through how profiling via eBPF works, why it's beneficial and how to get started with eBPF as an alternative to traditional profiling tools.
## What is eBPF Profiling?
eBPF profiling is the use of the eBPF framework to collect granular data about the use of CPU, memory, network data and other resources. (If you're not familiar with eBPF, check out our blog post that answers the question "
[what is eBPF?](https://www.groundcover.com/ebpf)")
To understand what that means in more detail, let's step back and talk about profiling in general. In the world of monitoring and observability, profiling is a method for determining which resources are being consumed by individual applications or processes.
Thus, instead of monitoring just the total memory usage or CPU utilization of your system (which you could do using Linux tools like
**free** and **mpstat**), profiling allows you to determine how much memory, CPU or other resources a specific process or application is using. That data comes in handy if you want to figure out whether an app or process is hogging more resources than it should or identify a workload that you should migrate to a different node to free up more resources â to name just two examples of why you might want to perform profiling.
Most monitoring and observability tools don't profile applications and processes by default; they just track total resource consumption. But there are ways to perform profiling via conventional tools. For example, you can use the
**top** command in Linux to get some profiling insights:
As you can see, the output of
**top** in this case reports the memory and CPU utilization levels of specific processes (in this case, slack and kubelet) that are running on the system.
## Traditional Profiling vs. eBPF-Based Profiling
Tools like
**top** get profiling insights by looking at the /proc directory of the Linux file system, where the operating system reports data about running processes. Thus, they don't profile workloads as much as they pull the limited amount of data that the Linux kernel supplies by default about active processes. They rely entirely on data that is available in the user space stack.
With eBPF, however, a different approach becomes possible. eBPF can actually perform profiling directly for any application or process running on the system by monitor stack traces. And it can do so via special programs that run in kernel space, which makes profiling much faster than it would be if you relied on requests that execute in user space.
## Types of eBPF-based Profiling
eBPF's ability to interact with the kernel in a low-level manner means you can use the
[eBPF tracing](/ebpf/ebpf-tracing) framework to perform multiple types of profiling.
â
### CPU Profiling
As a CPU profiling solution, eBPF allows you to monitor stack traces to watch the CPU utilization levels of individual processes or applications. This is useful if you want to track which workloads (or parts of workloads) are consuming the most CPU and possibly depriving others of the compute resources they need to run efficiently. You can also use CPU profiling to pinpoint processes that are sucking up large amounts of CPU due to bugs.
### Memory Profiling
Similarly, you can use eBPF to profile the memory allocation and utilization of individual processes or workloads. Memory profiling helps you ensure that memory is properly distributed between different workloads. It also helps troubleshoot issues like memory leaks, which happen when applications consume more and more memory over time, usually due to poor memory management within an app or microservice.
### Network Profiling
It's not just internal resources that you can profile with eBPF. You can also track connections to the network by mapping processes or applications to individual packets. This level of fine-grained network visibility offers tremendous benefits for troubleshooting network performance issues like high latency rates or dropped packets. It can also help surface malicious network requests and allow you to understand how your workloads react to them.
â
![Illustration of network profiling, showing how eBPF enables fine-grained network visibility](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/64fa066ece55fc48932e5970_ZXnHFiKYomYssUh6dgvGKmVQ2aZZ-mAHUuhaNTZDBu5FPLDGCpm7zOmkUfmYRkR80juDm9j_JHKcBF1bLU2LKS2ognps8I9w4cRyazJVbQKP8GmZSeyq0WQzk75ug3JhTwCJqcvKc40NNNZ-xW5QEJU.png)
## Significance of eBPF Profiling in Gaining System Insights
Now that you know how eBPF can be used as a profiling tool, let's talk about why you'd perform eBPF profiling.
The simple answer is that eBPF-based profiling and stack traces monitoring is a hyper-efficient way of gaining fine-grained visibility into what's happening inside your operating system and workloads. By profiling the resource consumption of individual processes and applications, you can answer questions such as:
Â â¢ Which process inside my application is consuming the most resources?
Â â¢ Â Did a spike in resource consumption by a particular process correlate with a performance issue I've noticed within my application?
Â â¢ Â Do I have sufficient CPU, memory and other resources to keep my workloads running smoothly?
Â â¢ Â I just added more nodes to my cluster and want to migrate some applications to them. Which applications are the best candidates for migration based on their resource consumption levels?
This is just a sampling of the reasons why eBPF profiling is useful, of course. Using eBPF, you can answer virtually any question you might have about the resource utilization status or trends of any application or process.
## Benefits of eBPF for Profiling
We noted above that you can use other types of monitoring and
[observability tools](https://www.groundcover.com/blog/observability-tools) (like, again, the venerable **top** command) to profile applications. So why would you want to use eBPF for profiling instead?
The answer is that with eBPF, you get a variety of distinct benefits.
### Improved performance analysis
Because eBPF programs run in kernel space, they can collect data from the kernel about resource utilization more efficiently than a monitoring application that runs in user space. As a result, you devote fewer resources to profiling and leave more resources available for your actual workloads to consume.
### Improved visibility
With eBPF, you can write custom programs to collect profiling data in a highly customizable way. You're not limited to the generic information available in /proc.
As a result, eBPF-based profiling gives you a deeper level of visibility than you would get from conventional approaches.
### Enhanced Security and Compliance
eBPF programs run in sandboxed environments, and they must pass validation by the kernel before they can execute. These controls minimize the risk that a buggy eBPF profiling routine could place the system at risk.
### Simplified Deployment
You can use eBPF for profiling without making any modifications to your kernel or having to insert kernel modules. As long as your node is running Linux kernel version 4.16 or later, eBPF is built in. (To be fair, some Linux distributions come with user space profiling tools installed by default, too, but this isn't the same as having profiling capabilities built directly into the kernel.)
## Challenges of eBPF for Profiling
On balance, it's worth noting that eBPF as a profiling solution is not without its challenges.
The biggest is that writing and
[deploying eBPF programs](https://medium.com/@megawan/writing-compiling-and-loading-ebpf-program-7b0efa014142) takes some effort. You need to know how to code in compiled languages like C, and you must be able to compile your programs and load them into the kernel in a way that allows them to interface with eBPF (you can also use interpreted languages, like Python, for eBPF programming, but only with help from a wrapper). Learning how to do these things isn't particularly challenging if you're already familiar with Linux and programming, but the process is more complex than running a traditional monitoring tool that doesn't require custom coding or specialized deployment.
eBPF programs are also subject to the limitation of having to be verified before they can run. This is a feature, not a bug, because (as we noted above) verification helps prevent buggy code from causing issues for the system. But it does mean that you must master the intricacies of eBPF's verification process to ensure your code will be allowed to run.
The fact is that eBPF remains a relatively new technology and is still evolving. As a result, different kernel versions offer different versions of eBPF, and an eBPF program may run a bit differently on one kernel versus another. This can present challenges if you want to use eBPF for profiling across multiple nodes that are provisioned with different versions of Linux.
## Getting Started with eBPF for Continuous Profiling in Kubernetes
The process for leveraging eBPF as a profiling solution in Kubernetes is straightforward. It boils down to:
- Ensure that every node in your cluster is provisioned with a Linux kernel that supports eBPF.
- Deploy eBPF agents on each node to collect continuous profiling data.
- Push the data to an analytics tool where you can make sense of it.
The exact steps for this process will vary depending on which profiling data you want to collect and which eBPF agent you use to interact with the framework. But as an example, here's a simple approach to CPU profiling on Ubuntu using eBPF. (This example assumes that your Kubernetes nodes are provisioned with Ubuntu 20.04 or later.)
### Step 1: Install bpfcc-tools
First, install
[bpfcc-tools](https://manpages.ubuntu.com/manpages/focal/en/man8/profile-bpfcc.8.html) version 0.12.0-02 or later:
This package provides a tool called
**profile**, which profiles CPU utilization via eBPF.
### Step 2: Profile CPU
Next, run the tool to collect profiling data:
If you don't pass any arguments,
**profile** will continuously profile stack traces from across your system and print profiling and tracing data on the command line. If you want to profile specific processes or control the frequency of profiling, check out the tool's man page for the appropriate CLI arguments.
### Step 3: Analyze the data
To move the data into a location where you can analyze it, you can redirect the output of
**profile** to a file or data stream:
From there, aggregate the data in an analytics or visualization tool of your choice to make sense of it.
This is a pretty basic example of profiling with eBPF. For more complex use cases, you'd probably want to write your own custom eBPF program instead of relying on a generic tool like
**profile**, which doesn't provide as much control over which data you collect and how you collect it.
But if you're just looking for a fast and easy way to get started with eBPF for profiling in Kubernetes, an approach like the one we just walked through will get the job done.
### Using eBPF for Continuous Profiling in Kubernetes with groundcover
As an alternative to deploying your own eBPF agents and managing profiling data manually, you can also use groundcover, which leverages eBPF under the hood to monitor stack traces and collect this data. With groundcover, you get the efficiency of eBPF-based profiling without the hassle of having to set up and manage your own tooling.
## Profiling for Fun and Profit
eBPF is not the only way to collect profiling data, but it's a more efficient and secure way than traditional profiling methods. eBPF gets you more data with lower overhead and fewer risks of causing problems for your server. If you haven't already turned to eBPF as a way of supercharging your approach to profiling, now's the time.
### eBPF Academy
## Related content
[eBPF: What is it, Best Practices, and Use Cases](/ebpf)