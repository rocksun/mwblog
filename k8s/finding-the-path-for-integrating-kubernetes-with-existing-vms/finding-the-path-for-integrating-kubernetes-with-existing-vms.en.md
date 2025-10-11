Kubernetes has emerged as the platform of choice for deploying new enterprise applications, including the wave of AI apps expected to come online in the next few years. But for the foreseeable future, enterprises will largely continue to run existing apps atop virtual machine architectures. Finding a way for Kubernetes and virtual machines to coexist will be critical to maintaining agility and efficiency in the enterprise.

In just 11 short years, [Kubernetes](https://thenewstack.io/kubernetes/) has gone from a ground-breaking, almost experimental [container](https://thenewstack.io/containers/) orchestration platform into the dominant deployment method for new applications in enterprise IT. Today, four out of five organizations use Kubernetes, according to [The Cloud Native Computing Foundation’s 2024 survey](https://www.cncf.io/blog/2024/06/06/the-voice-of-kubernetes-experts-report-2024-the-data-trends-driving-the-future-of-the-enterprise/). Among those self-identified Kubernetes adopters, about 40% of their new apps are running under Kubernetes, a figure that’s expected to increase to 80% within three years.

That’s as close to ubiquitous as you’re going to get in the enterprise IT space. But no matter how quickly new technologies emerge, they must still compete for mindshare and budget with older technologies. For Kubernetes, the biggest alternative is still the virtual machine (VM).

VMs emerged in the early 2000s as a way to separate the operating system from the underlying hardware, enabling workloads to move and scale independent of the hardware. While VMs gave enterprises certain operational advantages at the server level, they didn’t fundamentally change the way applications were developed and shipped. Developers still developed software using the three-tiered or client-server architectures, which in turn frequently required extensive manual labor for testing and deployment.

That’s where containerization stepped in. Instead of building each enterprise environment separately, containerization enables developers to build a standard environment one time, test it to ensure compatibility, freeze the code changes and then essentially clone it — or contain it — for repeated downstream use.

These “containers” could then be deployed in a cookie-cutter fashion and run within a management system. This reduced the need for painstaking integration and testing work by the developers, and it also simplified the process of scaling applications to support growing workloads. These advantages allowed early Kubernetes adopters like Google, Twitter and Airbnb to innovate faster and scale farther than they could using VMs.

After [Google open sourced Kubernetes](https://thenewstack.io/kubecon-europe-how-google-will-evolve-kubernetes-in-ai-era/), developers around the world adopted it. Instead of being limited by the capacity of administrators to deploy software to production clusters, [Kubernetes allowed developers to deploy](https://thenewstack.io/a-look-at-kubernetes-deployment/) their own work, vastly reducing their dependence on administrators and letting them work more quickly and efficiently. Kubernetes helped spawn the cloud native computing architecture that has become the dominant paradigm.

While cloud native computing leads the way today, it’s sometimes at odds with existing paradigms, including VMs. Enterprises have invested hundreds of billions of dollars into building and deploying enterprise apps in VMs over the past 20 years, and they’re not inclined to rip them out and replace them with the more modern cloud native computing architecture.

New development is often done in the cloud native fashion, but most existing applications are running in VMs. As a result, VMs and containers are going to need to coexist for the foreseeable future. However, that’s easier said than done. The challenge for IT decision-makers, then, is to chart a path that allows them to work with both virtualized and containerized applications without incurring extraordinary costs.

Finding common ground between the Kubernetes and VM architectures is paramount for enterprise efficiency. Companies committed to using both Kubernetes and VM environments must figure out how they can run and manage these environments together. Adopting Kubernetes and cloud native computing is not enough; it must be integrated with the rest of the enterprise application portfolio, still running on VMs.

The good news is that Kubernetes and VMs can coexist. For starters, with the right platform choice, Kubernetes and VMs can actually both live on the same industry-standard x86 machines. Although many enterprises run VMs and Kubernetes on separate physical machines, running them together on the same hardware brings several benefits, including better hardware utilization, improved manageability, streamlined integration, strengthened security, and simpler troubleshooting.

There are two primary ways to combine [virtualized and containerized workloads on the same hardware:](https://thenewstack.io/state-of-virtualization-report-reflects-shifting-strategies/) either run Kubernetes within VMs, or run VMs with Kubernetes on bare metal using technology like Kubevirt.

While running Kubevirt to schedule VM-based workloads may seem like catapulting into the future, there are certainly some downsides. While there are enterprise hypervisors that have developed ecosystems, user bases and feature sets for over a decade, Kubevirt doesn’t yet have broad, mainstream adoption. It also exacerbates the [Kubernetes skills gap](https://thenewstack.io/overcoming-the-kubernetes-skills-gap-in-edge-computing/). Many companies say they have a hard time finding enough skilled people to run their cloud native workloads; if running any workload needs Kubernetes expertise, it will make that problem much worse.

Enterprises that seek a co-existence strategy may prefer a gradual transition that allows IT professionals with VM skills to continue to manage those environments while building up their in-house Kubernetes skills. Running Kubernetes in VMs gives companies the benefit of having an enterprise solution for their VMs and a pure, cloud native solution for their containers. It also gives access to the full spectrum of Kubernetes features, including dynamic sizing and ephemeral clusters, concepts that just don’t make sense when running Kubernetes on bare metal.

Kubernetes clearly represents the future path of enterprise IT environments. It’s a higher level of whole-system virtualization that addresses many of the pain points of earlier-generation VM systems. As companies build their Kubernetes environments, making the right choice for their enterprise can mean the difference between getting squeezed by the Kubernetes-VM transition or squeezing more utility out of existing clusters.

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/97a08e14-cropped-c870a71e-dan-ciruli-scaled-1-600x600.jpeg)

Dan Ciruli is vice president and general manager of the cloud native product team at Nutanix. His career in product management includes stints at Google, Zuora and EMC, and in open source he was a founding member of the OpenAPI...

Read more from Dan Ciruli](https://thenewstack.io/author/dan-ciruli/)