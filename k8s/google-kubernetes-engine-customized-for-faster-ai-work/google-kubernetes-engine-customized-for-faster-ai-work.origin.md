# Google Kubernetes Engine Customized for Faster AI Work
![Featued image for: Google Kubernetes Engine Customized for Faster AI Work](https://cdn.thenewstack.io/media/2025/04/5f20cb6b-google-next-25-1024x768.png)
LAS VEGAS — Google Cloud is [gearing up](https://thenewstack.io/kubecon-europe-how-google-will-evolve-kubernetes-in-ai-era/) for massive AI workloads, and is using Kubernetes as the platform to make it happen.

This week, during the company’s [Google Cloud Next](https://cloud.withgoogle.com/next/25) conference in Las Vegas, [Google](https://cloud.google.com/?utm_content=inline+mention) unveiled a number of enhancements to the [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE) all aimed to streamline AI workloads.

The company has also unveiled its hosted GKE-based supercomputing service, with special accommodations for AI workloads.

Many companies already have some Kubernetes expertise onboard running their infrastructure, so it makes sense to use this same talent to embark on their AI journey as well, said [Gabe Monroy](https://www.linkedin.com/in/gabemonroy/), vice president and general manager for cloud runtimes at Google, in a TNS interview.

“Your Kubernetes knowledge and expertise aren’t just relevant, they’re your AI superpower,” Monroy said.

Many of its customers have already started down this path. Usage of the company’s AI-oriented GPUs and TPUs has grown by 900% in the past year. All 15 of its top GKE customers are now using the service for AI and machine learning (ML) workloads, Monroy boasted.

The company expects that AI will generate more than $200 billion in annual infrastructure cloud services alone by 2028.

The GKE augmentations include support for an emerging Kubernetes standard, called the [Gateway API Inference Extension](https://thenewstack.io/kubecon-europe-kgateway-aims-to-be-the-kubernetes-onramp/), which will help better pair AI workloads with Kubernetes resources.

And a new GKE supercomputing service, called Cluster Director, will also lash together GKE machines into monster supercomputing mode, allowing them to work on large AI modeling jobs.

And for when things go awry, the cloud company planted a version of its Gemini AI-based chat client, called Gemini Cloud Assist Investigations, onto the GKE admin dashboard, where it can debug issues.

## Set the Load Balancer to “AI”
Now in public preview, the GKE Inference Gateway provides intelligent routing and load balancing for AI inference workloads, using the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)‘s (CNCF) Gateway API Inference Extension, currently under development.

The CNCF’s [Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/faq/) turns any Kubernetes gateway into an “inference gateway,” enabling training model-optimized settings to better load balance.

Such an extension would be of special interest to inference platform teams using Kubernetes to run their large language models (LLMs).

Today, they must struggle with generic load balancers that don’t do well with the unpredictable nature of inferencing traffic. The culprit? Variable response times. Some short questions necessitate long answers. Or vice versa. Or neither. It drives the predictive powers of load balancers batty.

Another challenge: multiple models.

In any thriving AI environment, “you need to manage lots of different versions of models, and you’ve got to actually manage routing across all those different models,” Monroy said. “Today’s load balancing infrastructure just isn’t cut out for that kind of thing.”

Thanks to a tagging scheme, the gateway is “model-aware” and thus optimized for intelligent routing, able to distinguish between different versions of the models being hosted.

To pep performance, the gateway has a “request scheduling algorithm” that keeps track of node utilization rates and can adjust workloads accordingly, “avoiding evictions or queueing as load increases,” as the GitHub [docs note](https://github.com/kubernetes-sigs/gateway-api-inference-extension).

Some other benefits are added in the extension as well, such as end-to-end observability and workload isolation.

Monroy stakes the claim that GKE is the first to implement the CNCF inference extension. Rather ambitiously, the latest release — as of press time — is [0.40](https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/tag/v0.3.0).

But in this implementation, GKE’s inferencing gateway can increase throughput by 40%, reduce tail latency by up to 60% and reduce server costs by up to 30%, Google has estimated.

## Virtual Supercomputing
For Google Next, the company has officially launched its supercomputing service.

GKE’s Cluster Director is a new services platform that mimics the operation of a [supercomputer](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/) (it was formerly known as the [Hypercompute Cluster](https://cloud.google.com/ai-hypercomputer/docs/hypercompute-cluster)), allowing users to deploy multiple virtual machines — with compute, storage, and networking — as a single unit.

Users can put a cluster of up to 65,000 GPUs or TPUs on a single job. Automated repair remediates any nodes that go down during a job.

The Kubernetes orchestrator is made aware of faulty clusters and can move workloads to another instance if necessary. Using Google Cloud’s [NodeLabels](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeLabels), it can schedule workloads based on the best topology available.

Best of all, the supercomputer can be entirely run through GKE using standard Kubernetes APIs. To build an AI-optimized cluster with GKE, Google offers a set of configurable blueprints. Google itself uses GKE to power its recently launched [Vertix AI](https://cloud.google.com/vertex-ai) enterprise ML service.

Although the service has AI extensions, Google sees Cluster Director as a general-purpose replacement for stand-alone high-performance computers, [gigantic bare-metal machines](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/) that to date [have largely been ](https://thenewstack.io/sc500-microsoft-now-has-the-third-fastest-computer-in-the-world/)custom-built.

This is what Google is now calling the[ legacy supercomputer market](https://top500.org/). These are customers that require millions of cores that can be banded together to do a single task, such as financial services running large Monte Carlo simulations for risk calculation.

The company is focusing on “goodput,” an HPC for the amount of useful content provided to an application. In training terms, goodput equals the “percentage of time that forward progress is being made on training runs,” Monroy said.

With Cluster Director, Google is aiming for 99%.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)