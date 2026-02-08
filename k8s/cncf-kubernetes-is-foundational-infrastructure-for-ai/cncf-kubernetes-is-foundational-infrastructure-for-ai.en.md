The latest [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) [Annual Cloud Native Survey](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) has been released, and with “82% of container users running Kubernetes in production, cloud native has crossed a defining threshold,” it boasts.

“What was once experimental is now foundational.”

Or, as [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk), CNCF’s CTO, put it, “[Kubernetes is no longer a niche tool](https://www.cncf.io/blog/2026/01/20/kubernetes-fuels-ai-growth-organizational-culture-remains-the-decisive-factor/); it’s a core infrastructure layer supporting scale, reliability, and increasingly AI systems.” Indeed, he continued, “98% of organizations surveyed have now adopted cloud native technologies, making it the near-universal standard for modern enterprise infrastructure.”

None of this is surprising. What is interesting is that AI is driving Kubernetes adoption. Wait, you might say, but doesn’t AI depend on GPUs, Tensor Processing Units (TPUs), and custom AI application-specific integrated circuits (ASICs), none of which live in your typical cloud datacenter? True, but those are used for training AI, not using AI.

As [Jonathan Bryce](https://www.linkedin.com/in/jbryce/), the CNCF’s Executive Director, wrote in the introduction to the Cloud Native Report, “66% of organizations are already using Kubernetes to host their generative AI workloads. But the real story isn’t the one in the headlines. It’s not about training LLMs. Most enterprises do not build or train their own models — they are consumers. The real challenge is deployment.”

## Cloud native for development

By the CNCF’s count, [59% of organizations are now using cloud native for “much” or “nearly all” development.](https://www.cncf.io/wp-content/uploads/2026/01/CNCF_Annual_Survey_Report_final.pdf)

How that breaks down is something like this. There are four levels of cloud native adoption, starting with Explorers (8%), Adopters (32%), Practitioners (34%), and leading up to Innovators (25%). The CNCF describes this in the report as “a predictable progression model,” with [GitOps](https://thenewstack.io/gitops-in-the-real-world-barriers-and-best-practices/) serving as the “North star metric: Not one of the explorers has implemented it, while 58% of innovators run GitOps-compliant deployments.”

The CNCF also stated that [Continuous Integration/Continuous Deployment](https://thenewstack.io/ci-cd/) (CI/CD) is nearly universal at the top end. That means 91% of mature organizations use CI/CD tools in production, while 74% of innovators check in code multiple times per day.

At the same time, [containers](https://thenewstack.io/containers/), as you’d expect, are also moving steadily into production. Application containers in production have risen from 41% in 2023 to 56% in 2025. Simultaneously, pilot-only container deployments are down to a mere 6%. People no longer play with containers; they move them straight to deployment.

Marching along with this, other graduated CNCF projects, such as Helm, etcd, CoreDNS, Prometheus, and containerd, are now being used by 75% and up of those surveyed. These aren’t the only ones adopted. In particular, incubating projects such as CNI (52% in production), OpenTelemetry (49%), gRPC (44%), and Keycloak (42%) are standing out for their rapid adoption.

## Challenges ahead

Some technologies that have gotten a lot of attention aren’t faring as well when it comes to being deployed. In particular, [Web Assembly (Wasm)](https://thenewstack.io/webassembly/webassembly-what-beginners-need-to-know/) isn’t living up to its hype. 65% of those surveyed reported they had no Wasm experience, and just 5% have deployed it in production.

With its popularity, AI will bring its own uses.

As those gigawatt AI datacenter factories start to come online, “We will need to greatly decrease the difficulty of serving AI workloads while massively increasing the amount of inference capacity available across the industry. I believe this is the next great cloud native workload.”

That’s a prediction we can all see coming to fruition.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)