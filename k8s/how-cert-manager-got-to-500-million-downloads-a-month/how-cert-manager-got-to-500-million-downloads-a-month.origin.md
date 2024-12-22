# How cert-manager Got to 500 Million Downloads a Month
![Featued image for: How cert-manager Got to 500 Million Downloads a Month](https://cdn.thenewstack.io/media/2024/12/7228606c-kccnc-na-24_matt-barker_ashley-davis_featured-1024x576.png)
SALT LAKE CITY — Tech job interviews are notorious for [making hiring candidates jump through hoops](https://thenewstack.io/how-to-make-tech-interviews-suck-less/). But years ago, at startup-stage Jetstack, an engineering challenge given to a job seeker turned into [cert-manager](https://cert-manager.io/), an open source success story.

Jetstack had started early in [the Kubernetes boom](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/), aiming to help other organizations use K8s and containers. But “because we were so early, this is almost 10 years ago, now, not much existed around Kubernetes at the time, and we had to do things the hard way,” recalled [Matt Barke](https://www.linkedin.com/in/mattbarks/?originalSubdomain=uk)r, Jetstack co-founder, in this On the Road episode of The New Stack Makers, recorded at [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/).

Add-ons, Barker said, largely needed to be built from scratch. Meanwhile, he said, customers were requesting an easy way to manage certificates inside or with [Kubernetes](https://roadmap.sh/kubernetes).

While hiring its first engineer, Barker said, “We thought, well, everyone’s using [Let’s Encrypt ](https://letsencrypt.org/)these days. Why don’t we create a little bit of an interview challenge, and we’ll get this prospective engineer to automate Let’s Encrypt inside Kubernetes?

“We asked him to do it on a Friday. He came back on Monday with a working prototype, and he said, I’ve called it kube-lego: Kubernetes Let’s Encrypt Go binary, and this is what it does. And me and my co-founder looked at each other and were like, Wow, how’s he managed to do this? This is absolutely amazing. So we hired him, obviously.”

Not only that, but kube-lego became cert-manager, an open source project that, in September, graduated from the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention).

In this episode of Makers, Barker — now vice president and global head of workload identity architecture at [Venafi, a CyberArk company](https://venafi.com/) (which had purchased Jetstack) — and his colleague [Ashley Davis](https://www.linkedin.com/in/ashleydavis10419/), a staff software engineer at Venafi, told how cert-manager grew from a job-interview puzzle to a CNCF graduate.

The project, which now manages certificates for [Red Hat OpenShift](https://www.openshift.com/try?utm_content=inline+mention) users as well as for Kubernetes, is now [downloaded more than 500 million times a month](https://www.cncf.io/announcements/2024/11/12/cloud-native-computing-foundation-announces-cert-manager-graduatio), according to CNCF figure released in November.

## How CNCF Helped cert-manager
Cert-manager’s journey to CNCF graduation began four years ago, when [it was donated to the foundation](https://thenewstack.io/jetstacks-certificate-management-project-joins-the-cncf-sandbox-of-cloud-native-technologies/), a process that Barker said occurred “organically and naturally.”

The project, he said, was made certificate authority agnostic (or CA agnostic) and relaunched as cert-manager. “And the baton was passed to another engineer called [James Munnelly](https://www.linkedin.com/in/munnellyjames), and he then grew it from there. And it was a point where it just became the de facto standard for doing specific life cycle management.”

A sign that pointed toward CNCF stewardship, Barker said, was the community that was already growing around cert-manager. “We had amazing feedback from the community,” he said. “We had a lot of contributors; lots of companies built connectors for cert-manager. And so there was already a really strong ecosystem around it.”

The CNCF has helped the maintainers navigate a perennial challenge with popular projects, Davis said: “With such a huge community of people using the project, you inevitably have differences of opinion on how to handle things.

“Say, for example, if we find something that we might be able to call a security vulnerability, but it’s not the most critical thing in the world. Do we make a breaking change to do that? Do we interrupt other people’s workflows to to fix the problem and make sure it won’t be a problem, or do we accept it, document it, move on? There’s no good answer to that, necessarily. And with so many people in these conversations, it can be hard to reach a consensus. But usually, we do get there.”

## Post-Graduation Plans for cert-manager
Now that cert-manager has reached graduation status, it’s got a lot of plans on its roadmap to fulfill. For starters, there are a number of sub-projects, Davis said.

Among them is [trust-manager](https://github.com/cert-manager/trust-manager), “a small Kubernetes operator which aims to help reduce the overhead of managing TLS trust bundles in your clusters,” according to its [GitHub](https://github.com/) documentation. It has a certificate signing request (CSR) that integrates with the [Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) service mesh.

“A lot of the new stuff and the new work that we do in these subprojects is solving other issues relating to certificate management,” Davis said. “So [the] manager can issue these certificates and get the certificate that you need.”

Bigger picture, Barker said he’s focused on solving the problems faced by teams running cert-manager at enterprise scale. “Cert-managers’s already part of the stack. It’s already part of the furniture, as it were, and we’re starting to see companies now adopt and deploy to Kubernetes as if it’s become the operating system of the cloud,” he said. “So where else would you build your next application if it wasn’t on cloud native technology using Kubernetes, and therefore cert-manager.

Which means, of course, looking at hybrid, multicloud and edge use cases. As deployments get more complicated, he said, “it starts to become quite painful to manage and run. And that’s where I’m thinking about how we can assist those enterprise users on actually making that process a little bit easier.

Another item on the roadmap: Helping security professionals get up to speed with a project that was built with developer velocity and workflows in mind.

“Right now, what we’re doing, and spending a lot of time doing, is educating security teams on the impact of what using cert-manager does for an organization, and then also how to properly control it, manage it, and yet get and discover all of those certificates and all those instances of cert-manager. Matching all of the speed that’s happening on the developer side, but with the safety that an InfoSec team can apply.”

Check out the full episode to learn more about cert-manager, including how to get involved as a contributor.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)