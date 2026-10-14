If you run a Kubernetes platform, you’ve probably got at least one Grafana dashboard for resource visibility on your workloads. It shows what a container asked for versus what it used, making it relatively easy to point at the deployment that requested four cores and is only using half of one. If you break it down by namespace you get a rough idea which team is consuming what, which is what teams have been doing for CPU and memory for years and it mostly works.

Then people started putting workloads on GPUs and a lot of what we assumed would carry over didn’t. Almost every piece of visibility you take for granted on CPU and memory, GPUs make you build yourself. Your own metrics, your own accuracy, your own rules for splitting the bill. Which is what stings the most, since the GPU is the most expensive line on the bill.

## **Bring your own metrics**

With CPU and memory, the kernel already tracks usage per container for you, so getting a per-pod number is basically free. GPUs on the other hand, don’t give you that. The tool everybody starts with, NVIDIA’s DCGM exporter, reports at the physical device level by default. This is fine when one pod has a GPU to itself, but the second you start sharing a GPU across pods, with time-slicing or MPS, DCGM gives every pod sharing that GPU the same value. So if three pods are sharing one GPU, all three look like they’re using the whole thing, and when you add it up you get 300% of a GPU that doesn’t exist. With time-slicing or MPS, the driver exposes a single set of counters for the whole GPU, so DCGM has no per-pod data to attribute and cannot distinguish which workload consumed what.

The numbers still plot nicely on a graph, but teams build full dashboards and reports on values that are blatantly wrong but hard to notice.

## **Bring your own rightsizing math**

On the CPU side we’re all used to millicores, overcommitting, bursting, a CPU limit that just throttles you, a memory limit that gets you OOM killed but GPUs throw most of that out. A GPU shows up as a whole-number resource, nvidia.com/gpu: 1. You ask for whole GPUs, your request and your limit have to match, and there’s no overcommitting at the scheduler. The fractional sharing you need for inference happens underneath the scheduler through time-slicing or MIG, and Kubernetes requests don’t fit in neatly.

So the basic rightsizing premise, comparing what a workload requested against what it’s using and reclaiming the difference, barely exists for GPUs when you start. You end up having to work out how much of a GPU’s capacity a workload got before you can even have the waste conversation.

## **Bring your own guardrails**

The NVIDIA container runtime looks at an environment variable called `NVIDIA_VISIBLE_DEVICES`, and the base CUDA container images ship with it set to all. In a normal setup the device plugin overrides that and injects only the GPUs a pod was actually allocated. But if nothing overrides it or the container runtime is configured to honor the env var from the container, a pod can end up seeing and grabbing every GPU on the box no matter what Kubernetes thinks it handed out. So what the scheduler recorded as allocated and what ran on the hardware can diverge significantly. If you want the real number, you have to look at what’s happening at the process level and line it up against what Kubernetes thinks it did.

## **Bring your own definition of utilization**

When a CPU graph says 80%, you pretty much know what you’re looking at, but GPU utilization is squishier. The usual metric tells you a kernel was running on the GPU for some slice of the sample window. It won’t tell you how much of the actual compute or memory bandwidth you burned. You can watch GPUs sit at 100% utilization while the compute is barely doing anything. And a lot of the time the thing that runs out first is memory, because frameworks like vLLM grab most of the GPU at startup whether they need it or not. Work out early which signal means something for your workloads, whether that’s compute occupancy, memory footprint, bandwidth, or power. If you rely on that big headline number, you can reach the wrong conclusion.

## **Bring your own attribution**

NVIDIA’s NVML library will tell you, per process on a GPU, how much memory it’s holding, and you can trace each process back to the pod and team that owns it. The numbers are dependable, with one asterisk: they won’t quite add up to the card’s total, because the driver reserves a slice of memory for itself that doesn’t belong to any workload.

Compute is where it falls apart and it’s worth understanding why. Picture a shared kitchen: memory is counter space, you can look and see what ingredients are sitting where. Compute is the stove and everyone’s taking turns in bursts of milliseconds. What NVIDIA gives you isn’t “how much stove time did each cook get.” It’s closer to a flag that gets checked many times a second asking “was this cook doing something right now?” If two people are both working, both flags read yes almost all the time, so you get two jobs that each look 90% busy, which is true and also tells you nothing about who got more done.

That measurement is usable in one setup, when the GPU is strictly taking turns between jobs one at a time, where polling something like DCGM’s accounting mode or nvidia-smi’s PID-level sampling can approximate each job’s share. It breaks in the setup where jobs genuinely run side by side, which is also the setup people pick when they want better utilization. If two teams share a GPU, nothing available today will tell you which one burned 70% and which one burned 30%.

So the practical decision is to bill on memory, where the data holds up, and treat compute as a signal, something to drive chargeback. The reality is, fairness through accuracy between teams actually matters when you want to move beyond showback and GPU memory is the most accurate way to attribute with existing tooling.

## **Bring your own sharing paradigm**

Sharing a GPU turns out to mean a handful of different things and each one changes the math underneath. There’s time-slicing, which round-robins the GPU with no isolation and lets you oversubscribe it. Then MPS lets kernels from different processes run at the same time. MIG is quite popular and splits the GPU into fixed hardware partitions, though it’s worth noting that most clouds still charge you for the whole physical GPU even when you’re only using a slice, and on A100/H100-class GPUs you can only slice it up to 7 instances. And then there’s DRA, Dynamic Resource Allocation, which has been maturing over the last few Kubernetes releases and is clearly where things are going, but the ecosystem around it, including autoscalers like Karpenter, is still catching up. Every one of these changes what “allocated” even means, so visibility depends on which mode a given node is in.

## **Bring your own splitting rules (and the bill is brutal)**

GPU costs run far higher per hour than CPU costs and are much harder to split per workload. The cloud provider bills a GPU node as one line item with the CPU, memory, and GPU all lumped together. To get to a real dollar number per workload, you have to break that line apart and weight the GPU piece by model, because a T4 and an H200 are nowhere near the same price. Then you split it across whatever workloads were sharing the GPU. On AWS, the cheapest MIG compatible A100 GPU is $22/hr, about ~$14/hr on spot, whereas a comparable CPU-only instance of that size runs about $5/hr. Even on spot that’s quite the difference.

## **So what does this actually cost you?**

Add this all up and the real cost isn’t just the GPU bill but the engineering time and toil you sink rebuilding visibility you used to get for free. The metrics, the expected accuracy, the guardrails, the attribution, the splitting rules, every layer is something you now have to own and maintain.

The upside here, is the space is moving quickly. DRA is maturing and adoption growing with it, hardware partitioning is getting easier, and the tooling gap narrows every release. So be deliberate about which layers you build now versus what you let the ecosystem catch up on, and definitely don’t go in expecting your CPU and memory playbook will carry straight over.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/ef632ec9-cropped-6af8874c-7xl80xrcanikrplucbevvxfkjuymwyrfsehjbhuxqui-600x600.png)

Yasmin Rajabi is the Chief Operating Officer at CloudBolt Software. She is a recognized leader in the FinOps and Kubernetes communities, and her background as an engineer, product leader, and operator gives her a holistic perspective on the challenges facing...

Read more from Yasmin Rajabi](https://thenewstack.io/author/yasmin-rajabi/)