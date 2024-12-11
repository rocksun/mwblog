# DIY Kubernetes Is a Recipe for Mayhem
![Featued image for: DIY Kubernetes Is a Recipe for Mayhem](https://cdn.thenewstack.io/media/2024/12/229babb1-pexels-punttim-52608-1024x685.jpg)
[Tim Gouw](https://www.pexels.com/photo/man-in-white-shirt-using-macbook-pro-52608/).
Today, in late 2024, CTOs and other enterprise IT leaders view [Kubernetes](https://thenewstack.io/kubernetes/) as table stakes. Everyone knows that modern, container-based applications are portable, agile, and efficient — and that Kubernetes is the universally accepted solution to deploy and manage them at scale. Kubernetes is a highly popular open source project that suggests low cost and strong community support.

In fact, an amazingly helpful [open source community](https://kubernetes.io/) is one of Kubernetes’s best aspects, enabling novices to learn the framework quickly. But as with many things in life, the best aspect of something can also be what gets you into trouble.

A progressively lower barrier to entry has allowed many enterprises to run amok, nullifying some of Kubernetes’ key benefits. Enterprises must adopt a strategic, centralized approach to reign in scattershot Kubernetes implementations and get back on track.

**Kubernetes Plus Much, Much More**
With a wealth of tutorials, guides, and community forums, Kubernetes’ open source community does a great job of getting beginners up to speed on complex new technology. It has also developed new cloud native tools to reduce that complexity. Soon, new users grasp the foundational concepts — pods, services, volumes, controllers, and so on — and proudly launch their first distributed applications.

The problem is that to run Kubernetes effectively, and you need to understand not just the framework itself but [a whole ecosystem of related cloud native software](https://landscape.cncf.io/) — to handle such essentials as observability, logging, networking, security, storage, IAM (identity and access management), and more. Each component has its learning curve and release schedule, with integration and troubleshooting as part of the deal.

That’s a lot of upkeep for a solution intended to yield new levels of agility. Enterprises don’t want to waste developer or admin time on menial tasks, so they often seek outside help to lighten the burden.

**Why ‘Let the Cloud Do It’ Falls Short**
Many customers opt for a Kubernetes solution from a significant cloud like [Amazon](https://aws.amazon.com/?utm_content=inline+mention) EKS or Microsoft AKS. These have the advantage of one-click Kubernetes provisioning with automated updates and scaling in the background — and also provide an array of managed add-on capabilities. But going all-in with any one cloud has its pitfalls.

The first and most obvious is lock-in. These cloud Kubernetes offerings and their cloud-native companions are proprietary cloud services. The services external to Kubernetes itself are developed by the cloud provider rather than by the open source community, so employing them typically means the container-based applications a customer develops are no longer portable — to other clouds or on-prem Kubernetes implementations.

Another problem is cost. The big clouds offer Kubernetes and related services at low initial rates, but the total bill escalates as you add clusters, storage services, monitoring, and so on. Work is also required to integrate and automate these services, resulting in code that needs to be maintained — driving up cost and complexity in the process. If operational expenditures reach a tipping point, the human capital investment in learning proprietary cloud services will have been wasted, and the time, effort, and data migration costs required to switch platforms will be daunting.

**Stumbling Into DIY Mayhem**
At the other extreme are organizations that go the [open source route and try to manage](https://thenewstack.io/5-ways-that-open-source-benefits-api-management/) everything themselves. The [CNCF (Cloud Native Computing Foundation)](https://cncf.io/?utm_content=inline+mention) lists all the projects developers and DevOps personnel need to assemble their Kubernetes implementation. However, as previously noted, building and maintaining that stack from the ground up burns many [developer and admin cycles that could be more productively](https://thenewstack.io/bring-purpose-to-api-product-development-with-apiops-cycles/) applied elsewhere.

Worse, the DIY approach often breeds balkanization. Individual teams are left to hack together their own Kubernetes stack and workflows with no notion of standardization and no consistency with security policies across environments. In large organizations where broad adoption of Kubernetes is a mandate without a method, this has resulted in thousands of different implementations lacking interoperability. Kubernetes becomes entangled with the applications that run on it.

This unruly mess wrecks efficiency and application portability and precludes a futuristic Kubernetes advantage: resource optimization at scale. Today, only companies that have based their entire infrastructure on efficient container management fully benefit from this, where they can scale up the number of containers across platforms during peak hours and scale back to free up resources for batch processes during off hours. It’s an enticing possibility — and an impossible one without consolidated Kubernetes management.

**Toward a Centralized Solution**
The [way forward for enterprises](https://www.nutanix.com/theforecastbynutanix/podcasts/ai-cloud-native-and-hybrid-cloud-work-together) is to create their own centralized cloud-native engineering team. This crew must recognize that Kubernetes and its related cloud-native solutions will be deployed in a variety of environments — on-prem in VMs or bare metal, across multiple public clouds, and on-prem. The model should extend to hybrid or multicloud deployments, where a single Kubernetes application may be developed for one platform and run on another.

The team’s goal should be to establish a standard cloud native stack and provide pushbutton deployment and automated maintenance, much as the public could Kubernetes providers do, but with cloud native open source projects at the core. This requires selecting the right [platform and tooling for the cloud native engineering](https://thenewstack.io/kubecon-panel-how-platform-engineering-benefits-developers/) effort. One of the most important selection criteria is support for [Kubernetes’ declarative Cluster API](https://cluster-api.sigs.k8s.io/), which simplifies consistent deployment across private and public cloud platforms.

The standardized, centralized approach works great for greenfield deployments. But what is to be done when an enterprise already has a tangled mess of Kubernetes nodes? First, management must clarify that the fragmented approach is no longer acceptable. Then, bit by bit, that centralized team can begin refactoring and migrating existing Kubernetes applications to the new, canonical stack.

Some developers or DevOps engineers may balk at having their carefully hacked one-off stacks discarded. That’s why it’s important to invite those who’ve already gained expertise in the cloud native world to contribute to (or join) the centralized cloud native engineering team if they choose. Ultimately, developers will be more productive, and the entire enterprise will benefit from restoring the agility and efficiency that initially excited everyone about Kubernetes.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)