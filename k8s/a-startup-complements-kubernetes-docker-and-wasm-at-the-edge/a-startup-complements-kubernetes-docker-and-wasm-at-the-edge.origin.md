# A Startup Complements Kubernetes, Docker and Wasm at the Edge
![Featued image for: A Startup Complements Kubernetes, Docker and Wasm at the Edge](https://cdn.thenewstack.io/media/2025/05/1ca9ac33-cloud-native-rejekts-2-1024x576.jpg)
[cDavid Aronchick](https://www.linkedin.com/in/aronchick/) looked around the historic room at [116 Pall Mall](https://www.116pallmall.com/) in central London for the [Cloud Native Rejekts](https://cloud-native.rejekts.io/) conference — a must-attend if you attend a [KubeCon conference](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/). What a space, BTW.
Aronchick is the CEO of [Expanso](https://www.expanso.io/), a startup that provides distributed computing to workloads. Instead of moving the data, the compute goes to the data itself — increasingly relevant as enterprise customers look beyond the cloud for their computing needs.

He pointed out that all the devices in the room will someday have some rich computing architecture. The recognition dawns that GPUs will come to these devices. They, of course, won’t be water-cooled, honking massive GPUs. These tiny GPUs might cost $500, $100 or even much less.

Distributed-compute workloads are emerging in a real way. As we know, GPUs can process data sets of the most complex order, used in AI and machine learning environments.

## Alice in Dataland
You start exploring the implications of these new data points, and it gets trippy. British author Lewis Carroll introduced us to the metaphor of looking down the rabbit hole. Down there in the land of distributed computing is an unknown world that may be more like Alice’s Wonderland than we care to realize.

But that’s the nature of computing everywhere: it’s like a wonderland. With trillions of devices, what will become of workloads? How will this trippy world get its compute?

Aronchick worked at [Google](https://cloud.google.com/?utm_content=inline+mention), where he [co-founded](https://thenewstack.io/kubeflow-co-founder-machine-learning-workflows-on-kubernetes-can-be-simple/) the [Kubeflow](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support/) project, which “was designed to help simplify the deployment of open source systems for [machine learning] applications on Kubernetes platforms at scale,” according to The New Stack’s 2018 post on the project.

For Aronchick, it’s about how we think of the different dimensions edge environments will require for developers to develop, deploy, and manage application architectures, whether standard software or [AI models](https://thenewstack.io/ai-at-the-edge-architecture-benefits-and-tradeoffs/).

He and his team have developed an open source architecture they call [Bacalhau](https://www.bacalhau.org/). It’s a distributed compute-over-data model that complements [Kubernetes](https://roadmap.sh/kubernetes), [Docker](https://www.docker.com/?utm_content=inline+mention) and [WebAssembly (Wasm)](https://thenewstack.io/webassembly/). It allows users to run compute jobs where the data is generated and stored.

Aronchick said the ability to network data gets a bit dicey when working with more than a single zone in a cloud network with Kubernetes clusters. The cross-zone stuff, regional data movement and working across clouds — Kubernetes architectures need a better way to do this.

You can see it with the use cases that Aronchick proposes. Logs, for instance, can be processed at the edge. Machine learning (ML) inference can happen at the data’s source. With a scheduler, the data runs on local nodes without centralized data lakes.

It’s about using a remote server or an Internet of Things (IoT) device, whatever that may be, to process the data at the source before it is sent to a central location. The data may undergo some inference at the source. It could use Wasm to isolate and process the data at the source.

## Bring On the Compute
Cloud development environments are the rule, not the exception. But with Kubernetes, Docker, and Wasm, the ability to use a server, let’s say, in a restaurant, becomes far more doable.

That still, however, leaves the challenge of getting compute to the data. According to its documentation, Bacalhau uses local storage, an S3 bucket, or other storage providers—reducing unnecessary data movement. A customer uses what Bacalahau calls jobs and executions. Jobs define the workflow, and executions run the jobs in parallel across the nodes. More [here](https://docs.bacalhau.org/overview/key-concepts).

Gartner estimates that around 10% of enterprise-generated data is created and processed outside a traditional centralized data center or cloud. By 2025, Gartner predicts this figure will reach 75%.

Aronchick thinks of it this way: “I am an enterprise with 100 nodes spread around the world. I already own them, and they may already be in the cloud, but they’re not under a single controller like Databricks, [Snowflake](https://www.snowflake.com/?utm_content=inline+mention), Kubernetes, etc. You want to get a job to them — a data processing job, a new ML model, a new configuration, whatever — and can’t reliably do it today because you don’t have a single controller.”

That controller? That’s where Expanso could enter the scene. A customer can place one of Expanso’s agents on or near one of these nodes to give it the sense of a single control plane.

“We can run on a phone, sure!” Aronchick said. “But there are 100 million servers worldwide, and every time a business needs one, or a virtual machine, that isn’t in their central data center, they’re going to add to the challenge.”

For context, it’s a 49-millisecond ping time between Los Angeles and New York. The speed of light will never get faster. There’s nothing we can do about it.

Content delivery networks get this very well. [Akamai](https://www.linode.com/?utm_content=inline+mention) now uses [Fermyon’s](https://www.fermyon.com/?utm_content=inline+mention) Wasm technology to isolate data streams. Still, there’s the need to move the compute.

But getting the compute to the data is a massive cost, wrote [Bogdan Kurnosov](https://www.linkedin.com/in/bogdan-kurnosov/), now senior engineering manager at [bunny.net](https://bunny.net/), [on The New Stack in 2024](https://thenewstack.io/why-we-chose-webassembly-wasm-for-our-edge-runtime/).

“Routing traffic in and out of data centers is a time and money drain,” he wrote. “Paired with the rising demand for increasingly personalized web experiences, we needed to explore a new approach to cloud computing. Fortunately, we’d already built a network of edge nodes with our content delivery network (CDN). Adding computation capabilities to our CDN nodes was the next logical step.”

Data will inevitably go to the edge, and that’s a shift from the super data center model. The compute will have to go to the edge, too.

Then, the question comes down to why a company like Expanso has a chance in this new world. For one, Bacalhau is an open source project. It can run across on [NVIDIA](https://www.nvidia.com/), [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention) or [AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention). It’s hardware agnostic. Expanso technology can harness the computing capabilities of distributed GPUs.

That’s clear to me why open source offerings like what Expanso provides have a clear path as a core service as we accelerate toward a network of trillions of devices.

There you go, my take from Cloud Native Rejekts. See you in Atlanta.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)