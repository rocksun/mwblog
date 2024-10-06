# Is Kubernetes Green?
![Featued image for: Is Kubernetes Green?](https://cdn.thenewstack.io/media/2024/10/48fc0054-is-kubernetes-green-2-1024x576-1.jpg)
The [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) launches its annual [Sustainability Week](https://tag-env-sustainability.cncf.io/events/cloud-native-sustainability-week/) on Monday. On Tuesday, [Brendan Burns](https://www.linkedin.com/in/brendan-burns-487aa590/), co-creator of Kubernetes, will be the highest-profile [speaker](https://community.cncf.io/events/details/cncf-cloud-native-sustainability-presents-virtual-mini-conference-cloud-native-sustainability-week-2024/).

The question is, what is he going to say?

Maybe Burns is going to demand that CNCF engineers eat less meat and put solar panels on their roofs. I have heard such well-meaning pleas for individual action in tech keynotes before.

Perhaps he’ll tell us to give up on modern technology and turn off all our AI projects? I rather hope not. I’m not sure going backward is an option many of us would enjoy in practice. Even more importantly, I don’t think the argument would be very effective.

Neither hand-wringing nor the heroic pairing of a couple of photovoltaic cells and a spicy bean burger will save the world. However, more collective action from Burns’ listeners just might.

The good news is he knows that better than anyone.

## What Should Techies Be Doing?
Calling for individual action would be a tragic waste of the power of an audience of CNCF engineers. They could have way more impact.

By now, most of us know the [tech sector causes ](https://thenewstack.io/why-software-developers-should-be-thinking-about-the-climate/)[greater carbon emissions](https://thenewstack.io/why-software-developers-should-be-thinking-about-the-climate/) than aviation. That was true even before ChatGPT came along and put its soulless, if cheerful, foot down on the accelerator. Changes to our industry are the priority, not ourselves.

The good news is tech’s footprint is ultimately avoidable, even with AI in the picture. Minimizing carbon emissions has benefits for system cost and resilience and tools already exist to help us do it, we just have to use them. Too many of us aren’t. Or aren’t using them well. That is the problem we need to fix.

To explain why sustainability, cost and resilience are so aligned, we need to look at [the origin story of Kubernetes](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/).

## Containers and Orchestration: Sustainable Concepts
To explain why the concepts behind Kubernetes are key to tech’s response to climate change, we need to go back in time over 20 years to a more youthful [Google](https://cloud.google.com/?utm_content=inline+mention). Back then, a group of plucky engineers decided to build one of the most powerful and visionary software operating platforms ever seen.

They called it [Borg](https://dl.acm.org/doi/10.1145/2741948.2741964).

The Borg team knew that Google needed vastly higher data center machine utilization, at scale, than anyone in the industry had ever achieved. That extreme operational efficiency was necessary to restrain the resource requirements (and thus costs) of what was the first hyperscale software system.

In addition, in order to keep that system up and running, the team members needed far better resilience and recovery than ever before. They also required the capacity to react to changing circumstances — such as power fluctuations or hardware failures — at machine speeds, not puny human ones. But how?

Their audacious idea was to attempt to deliver all of these together via a fundamental shift in how their software was operated. The Google team decreed that all jobs on their new platform must be wrapped up, together with their dependencies and information about how to run them, inside a new [Linux](https://thenewstack.io/linux/) feature called a [container](https://thenewstack.io/containers/).

The result was the jobs could be stopped, started or moved around at lightning speeds using scheduling algorithms rather than the hands of overworked and underpaid (scratch that — it’s Google we’re talking about) human sysadmins.

This radical approach was called [orchestration](https://thenewstack.io/what-is-container-orchestration/), which is the basis of modern software development and operational practice. Borg and the concepts behind it inspired [Kubernetes](https://roadmap.sh/kubernetes).

In a twist to the tale, it turns out that encapsulation and orchestration are also concepts that can allow us to deliver high-scale green software.

## Green Electricity: A Variable Power Source
To understand why orchestration platforms like Kubernetes are so relevant to the future, we need to turn our gaze forward in time.

The world is currently moving away from fossil fuels and toward renewables — a transition that will take decades to complete. Making that transition successful is not just about building more solar farms or wind turbines because that won’t be enough.

Renewably generated electricity, particularly from solar and wind, has different characteristics to electricity that comes from burning fossil fuels. It is cheaper, so that’s good, but it is also way more variable. Its availability depends on things that can be tricky to predict and manage. That’s a problem.

We can’t command how sunny or windy it is. The elements are nowhere near as controllable as driving a tanker full of liquid natural gas to a power station and firing up a turbine. The immediate future we have to plan for has much less power available at the (literal) flick of a switch. Is that a dystopia? It depends on what we make of it.

What renewably generated or green electricity means is far more, far cheaper power at some times and far more expensive power at others. When and where will be only somewhat predictable. If you can thrive in that world, it’s a utopia. If you can’t, it’s a dystopia.

So, what tools exist to help software systems operate in an environment like that? Systems will need to be able to react and adapt fast. We’ll want them to use fewer resources at times of carbon-intensive electricity. We’ll also need them to be able to move jobs in time to match green power availability.

Two decades ago, Google proved a way to create such systems was to break them up into small manageable chunks (aka distributed systems) and operate them on orchestration platforms. They have been doing so ever since.

Google’s original desire was for systems that could adapt to unpredictable, changing circumstances. That’s exactly the kind of situation that systems will be faced with when running directly on renewable power. Google’s orchestrated-distributed-system design is therefore well suited to handling the clean energy sources of the future.

That was a piece of luck. Let’s take full advantage of it.

## A Kubernetes Future?
To handle the variability of renewable power, a lot more of us will need to be running orchestrated distributed systems in future.

Kubernetes is a tried and tested example of an orchestrator for distributed systems. Does that mean we’ll all end up using it? Not necessarily. It is not the only option out there.

The wider tech world has also learned from Borg and there are now many orchestration platforms available: serverless ones like [Amazon Web Service’s](https://aws.amazon.com/?utm_content=inline+mention) Lambda, [server-side WebAssembly](https://thenewstack.io/webassembly-for-the-server-side-a-new-way-to-nginx/) ones, managed services like Google’s [Cloud Run](https://thenewstack.io/how-google-cloud-run-combines-serverless-with-containers/), spot or preemptible instance types available on all hyperclouds, as well as managed Kubernetes options like [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) [Azure’s AKS](https://thenewstack.io/introducing-aks-automatic-managed-kubernetes-for-developers/). They all take encapsulated tasks and programmatically move them around in space and time. Some use containers to encapsulate, some use lightweight virtual machines. The principle is the same.

Eventually, I suspect almost all of us will run our software on an orchestration platform. We’ll need that to handle a world where electricity is much more like bandwidth — a variable resource whose availability has to be actively adjusted for.

Resource unpredictability is not a bad thing. It’s the kind of environment the Internet grew in and parts of the tech industry already understand it well.

Designing for an environment of unpredictability is fundamental to building green software, i.e., software and systems that can run directly on renewables. As Google and others have found out, there are many knock-on benefits to doing that well — reduced hosting costs and increasing resilience being the most significant.

Orchestrated-distributed-system design is vital to tech’s adaptation to climate change. It is probably the best way we can make data centers a load-balancing grid asset rather than a power-hungry grid liability.

In our [O’Reilly book](https://learning.oreilly.com/library/view/building-green-software/9781098150617/) on the subject, my co-authors and I describe the tools and services that help build these green systems as green platforms — Kubernetes is one, but so is serverless, most managed services, and spot instances.

Unfortunately, most of these platforms — particularly Kubernetes — are still only potentially green. To be sustainable, they have to be used really well, which is hard. Using them poorly doesn’t win you any green prizes. Quite the reverse. You either have to be an expert at it or buy something managed.

Cutting carbon emissions also means leveraging our power as consumers to force these platforms to keep improving. They all have plenty of scope to get a heck of a lot better and the planet (or let’s face it, humanity) requires them to do so.

Most engineers still need to learn how to get their systems ready for the energy transition — how to build or operate green platforms. Hopefully, Burns will use his keynote to point us in the right direction.

Check out the author’s previous appearance on an episode of The New Stack Makers, talking about green software:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)