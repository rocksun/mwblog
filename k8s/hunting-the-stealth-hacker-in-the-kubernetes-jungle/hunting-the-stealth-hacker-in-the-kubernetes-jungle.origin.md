# Hunting the Stealth Hacker in the Kubernetes Jungle
![Featued image for: Hunting the Stealth Hacker in the Kubernetes Jungle](https://cdn.thenewstack.io/media/2024/07/8bc09b6e-cncf-security-1024x684.jpg)
SEATTLE **— **At the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)‘s [CloudNativeSecurity Conference](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) last month, security experts [Stav Ochakovski](https://www.linkedin.com/in/stav-ochakovski) and [Ariel Szarf](https://www.linkedin.com/in/ariel-szarf-89b024197/?originalSubdomain=il) from [Mitga](https://www.mitiga.io/about/about-us), a cloud and software as a service (SaaS) security company, discussed how they use logs to track down threat actors in a [Kubernetes environment](https://thenewstack.io/Kubernetes).

After all, as Ochakovski said, the attackers are likely already in your cloud-based [Kubernetes clusters](https://thenewstack.io/managing-kubernetes-clusters-for-platform-engineers/). Indeed, Ochakovsk remarked, “It’s not about whether there is or isn’t a threat actor in a Kubernetes environment. It’s about where it is.”

They argue that you can’t be complacent about cloud security. That’s because as organizations increasingly migrate their [Kubernetes clusters to the cloud](https://thenewstack.io/using-prometheus-to-monitor-kubernetes-clusters-running-cloud-foundry/), lured by the promise of scalability and managed services, they all too often unwittingly open doors to sophisticated attackers.

Ochakovski and Szarf vividly described modern threat hunting as a high-stakes game of “Where’s Waldo?” Thus, they argue, you should aggressively search for attackers’ tracks even when you don’t see signs of them.

After all, “Sometimes, bad actors succeed in compromising an environment without triggering detection services,” Szarf said,

Their methodology is both systematic and intuitive. It begins with choosing a concrete hypothesis about potential attack vectors and motivations. For instance, an attacker might target sensitive data in cloud storage buckets.

The next step involves building a list of potential attack indicators, followed by a thorough investigation of any suspicious activities in the environment. Any anomaly may be a sign that an enemy is near.

How do you spot these? By closely looking at [your API](https://thenewstack.io/API-management/) server logs, scheduler logs, controller manager logs, audit logs and authenticator logs from Kubernetes, as well as cloud-specific logs such as [Amazon Web Services’ CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## How Your Kubernetes Cluster Could Be Breached
The presenters walked through a hypothetical scenario where an attacker gains persistent access to a Kubernetes cluster and uses it as a springboard to access sensitive data.

They highlighted three key indicators to watch for: the creation of persistent access to the cluster from an external account, [connections to the cluster](https://thenewstack.io/simplifying-cluster-connectivity-with-istio-service-mesh/) from unfamiliar sources and unexpected access to sensitive cloud resources.

Ochakovski and Szarf stressed the importance of enabling and collecting relevant logs from the [Kubernetes ecosystem and the cloud provider](https://thenewstack.io/kubernetes-autoscaling-q-a-with-fairwinds-cto-andy-suderman/) to find these silent precursors of an attack. These logs are the footprints that [security teams can follow](https://thenewstack.io/observability-is-shifting-left-following-security-and-ops/) to uncover potential threats.

“If there is one key takeaway we want you to take from this talk, it’s all about asking the right questions,” Ochakovski concluded. This sentiment encapsulates the essence of effective threat hunting – a proactive, curious mindset that assumes the presence of threats and actively seeks them out.

In short, it’s not enough to hope for the best. Organizations must proactively [hunt for threats](https://thenewstack.io/5-ways-to-automate-threat-hunting/) armed with the right tools, knowledge and, most important of all, the right, suspicious questions.

If that sounds paranoid, well, as the saying goes, “It’s not paranoia if they really are out to get you.” And, when it comes to [Kubernetes clusters on public clouds](https://thenewstack.io/private-vs-public-cloud-how-kubernetes-shifts-the-balance/), attackers really are out to get you.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)