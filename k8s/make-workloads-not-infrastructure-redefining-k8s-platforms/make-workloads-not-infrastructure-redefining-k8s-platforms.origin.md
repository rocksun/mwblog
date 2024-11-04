# Make Workloads, Not Infrastructure: Redefining K8s Platforms
![Featued image for: Make Workloads, Not Infrastructure: Redefining K8s Platforms](https://cdn.thenewstack.io/media/2024/10/157865ae-redefiningkubernetesplatforms-1024x576.jpg)
As [Kelsey Hightower](https://www.linkedin.com/in/kelsey-hightower-849b342b1/) said in 2017, [Kubernetes is a platform for building platforms](https://opensource.com/article/18/1/kelsey-hightower-kubernetes-community). Kubernetes is for operators, not developers. Grabbing a big cloud-hosted flavor of Kubernetes is sure to delight your ops team, but it’s just as likely to leave your dev team grumbling. The reason? [Kubernetes](https://roadmap.sh/kubernetes) is not the platform developers need. It’s a complex set of primitives misaligned with their primary focus: building applications.

Platforms are defined by your ability to build on them. If you’re a [platform engineer](https://thenewstack.io/platform-engineering/), Kubernetes really is a platform. You can build what you need on top of it. If you’re an app developer, Kubernetes is overwhelming. And if you’re a platform engineer, it’s overwhelming for you, too! That might be why so many [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) (IDP) projects built on Kubernetes go sideways and get replatformed. Despite all the good that Kubernetes does, we still lack a post-commit platform that developers love.

Getting to a place where both operations and development are happy is a problem that other platforms have struggled with. As we head into [KubeCon Salt Lake City 2024](https://thenewstack.io/event/kubecon-cloudnativecon-north-america/), let’s revisit it and some of the other platforms that led to Kubernetes.

## In Search of a Rails Moment
In 2019, [Bryan Liles](https://www.linkedin.com/in/bryanliles/) keynoted KubeCon with his talk “[In Search of the Kubernetes ‘Rails’ Moment](https://www.youtube.com/watch?v=ZqQTEdHVaCw).” He made a bold point by saying that [YAML kind of sucks](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/). In the world of Kubernetes, YAML manifests mean screens full of undefined fields and a dizzying array of tasks. That’s a far cry from an experience like `rails new blog`
. In other words, YAML is the wrong abstraction for app developers.

Ruby on Rails was a platform built in an era where [LAMP](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/) (Linux, Apache, MySQL and PHP) was a dominant stack. Like Kubernetes, the problem with LAMP was figuring out how to make it usable for software engineers.

Today, Kubernetes feels akin to the L in LAMP. Both Linux and Kubernetes are platforms that other components build on. Linux is definitively an operating system (OS), and Kubernetes is the OS for the cloud. It’s wild to think of an app developer wrangling kernel-level Linux APIs. But with Kubernetes, wrangling is the status quo.

Platform engineers need a platform that not only abstracts away the complexities but also frees developers to focus on writing the code they get paid for.

## Cloud Foundry Was Almost the Platform
Pivotal’s [Cloud Foundry](https://www.cloudfoundry.org/?utm_content=inline+mention) (PCF) was an early attempt at providing a sophisticated platform as a service. They nailed the vision of simplifying application deployment and enabling the “you build it, you run it” ethos. PCF had easy onboarding like Rails; instead of `rails blog new`
there was `cf push`
. The experience felt similar, but the big leap Cloud Foundry made was supporting nearly every language and framework (not just Ruby). Developers just needed to commit their code. PCF is what drove everything post-commit.

Yet, the platform still required large teams to maintain and operationalize alongside a hefty hardware investment that took months to provision. Because of the effort required to adopt PCF, it didn’t quite live up to its full potential, nor did it adapt fast enough to a cloud-native era. Remember how the missing piece of Kubernetes was good developer experience? The missing piece of Cloud Foundry was an adaptable and pleasant operations experience.

The cloud-native ecosystem is much more robust, as is the size of the problem, considering how many more software engineers are shipping workloads — with considerable effort and sometimes unsuccessfully — compared to a decade ago.

Cloud Foundry rose to prominence in the early 2010s, around the same time as Apache Mesos. Mesos was on the other end of the spectrum from PCF. It focused heavily on operational experience, but never quite found its footing. Heroku was from a similar era, but focused on developer experience while hiding the operational aspects.

## Kubernetes Became the OS for the Cloud
When Kubernetes rose to prominence, its success was partly fueled by its flexibility. There are many reasons why Kubernetes succeeded over other platforms. K8s gave the cloud a standard API, it was declarative and its focus on containers abstracted nicely over virtual machines (VMs). Another reason Kubernetes succeeded is because ingredients can be swapped in and out. As an example, the [K3s](https://k3s.io/) distribution swaps out [etcd](https://thenewstack.io/about-etcd-the-distributed-key-value-store-used-for-kubernetes-googles-cluster-container-manager/) for a more traditional relational database.

The emergence of [Amazon](https://aws.amazon.com/?utm_content=inline+mention) Elastic Kubernetes Service (EKS), [Google](https://cloud.google.com/?utm_content=inline+mention) Kubernetes Service (GKS) and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Kubernetes Service (AKS) cemented Kubernetes as the definitive OS for the cloud — each with its own flavors and challenges.

It’s worth remembering that application abstraction is still a task left to platform builders. It’s easy to see why. How do you want to get your code from Dev to Prod? Every team and organization will do that a little bit differently. That’s an important detail to keep in mind when recalling the “Kubernetes is a platform for building platforms” mantra. Finding the right digital experience (DX) is quite a challenging task.

## Defining the Future: A Platform Devs and Ops Love
So, what should a platform actually look like? Most platform engineers share an overarching vision: Everything post-commit is abstracted by the platform. That kind of abstraction frees developers to ship their workloads in a self-service way. They should be able to build, deploy and scale their workloads without being infrastructure experts. As long as the controls and levers are still available for tuning APIs below the surface of the platform, we’ve got a winning solution.

That broad vision translates into design philosophies — and ultimately requirements. Here are the philosophies and requirements that have guided me as I’ve built the [Northflank platform](https://northflank.com/):

**IaC is a starting point:**Infrastructure as Code (IaC) is essential, but it’s too static, and the release process is inherently dynamic. It leaves open questions like “How do I get code from Dev to Staging to Prod?” and “How do I restore production in another region or cloud?” The platform should provide a golden path that answers that question.**Automate CI/CD pipelines:**CI/CD is where the post-commit journey begins. Minimize manual intervention, and live the GitOps dream.**You build it, you run it:**Developers must be able to deploy and scale their applications with a few clicks or commands.**Polyglot is standard:**Most businesses making software are too big to not build with[multiple languages and frameworks](https://thenewstack.io/programming-languages/). The platform must be polyglot — not just for ephemeral, but also stateful and scheduled.**All workloads:**A platform should be agnostic about the workload’s complexity and be able to support all containerized frameworks.**Make troubleshooting easy:**One of the largest headaches when running software is troubleshooting. All the APIs hidden from app developers need to still be accessible to site reliability engineers (SREs).**Bidirectional, real-time interfaces:**If I update the workloads in Git, the user interface (UI) should reflect those changes, and vice versa. Don’t make your teams guess where info about their workloads lives. Don’t accept stale information in cloud UIs.
In essence, the future platform should empower teams to “make workloads, not infrastructure.”

By embracing a platform that prioritizes developer experience without compromising operational flexibility, organizations can accelerate their delivery cycles, reduce overhead and stay competitive. A good platform frees developers to do what they do best — write code — while operations ensures that the supporting infrastructure continues to run smoothly.

## Conclusion
DevOps is about uniting developers and operations. Platforms aren’t really platforms if they cater to one over the other. That’s something I’ll keep in mind as we head into KubeCon 2024. There are over [a dozen talks about platforms](https://kccncna2024.sched.com/overview/type/Platform+Engineering) at the main event, and a whole [colocated platform engineering day](https://colocatedeventsna2024.sched.com/overview/type/Platform+Engineering+Day), as well.

What I’ve shared here flows from my experience building platforms on Kubernetes at [Northflank](https://northflank.com/). If you spot me wandering around KubeCon, I would love to hear what you think. Is it possible to make a successful platform that deprioritizes either half of DevOps? What philosophies guide you as you build your IDP? What do you see as the major challenges while platform engineering?

*To learn more about Kubernetes and the cloud native ecosystem, join us at **KubeCon + CloudNativeCon North America**, in Salt Lake City, Utah, on November 12-15, 2024.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)