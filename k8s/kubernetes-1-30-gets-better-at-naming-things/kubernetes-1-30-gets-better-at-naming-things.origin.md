# Kubernetes 1.30 Gets Better at Naming Things
![Featued image for: Kubernetes 1.30 Gets Better at Naming Things](https://cdn.thenewstack.io/media/2024/04/22cfa2f9-kubernetes-1-30-1024x683.png)
Passport, please!
Following public word of a container leakage last January, the release of Kubernetes 1.30 offers a few more security checkpoints, tightening up the permissions and access controls. No longer will errant processes be able to wander about K8s-managed containers and pods namelessly.
Thanks to
[KEP 24](https://github.com/kubernetes/enhancements/issues/24) (“AppArmor support”), Kubernetes containers and pods can be secured through [AppArmor](https://apparmor.net/), a Linux security module for enforcing policies during runtimes. It confines what an application can do to a system based on the application’s profile.
Users specify AppArmor profiles
[via API](https://thenewstack.io/API-management/).
The enhancement proposal has been kicking around for about three years. Permission enforcement is difficult stuff.
Another enhancement: Pods can now have user names, thanks to
[KEP 127](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/127-user-namespaces#summary) (“Support User Namespaces”), [work on which was pushed](https://kubernetes.io/blog/2024/04/22/userns-beta/) through in a hurry after [a series of critical container vulnerabilities](https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv) were found in January that took advantage of this lack of access designation.
This feature “allows you to isolate pods a little bit better,” said
[Kat Cosgrove](https://github.com/katcosgrove), who was the release lead for this latest release of Kubernetes.
Also for security,
[KEP 3488](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/3488-cel-admission-control#summary) (“CEL for Admission Control”) introduces a richer expression language for admission control, providing “a slightly more dynamic and expressive way of evaluating any admission requests,” Cosgrove said.
“You can have some pretty complex policies defined and enforced within your Kubernetes API that make security and governance capabilities a little bit easier to control without compromising performance.”
## Team Lead: Wrangling Required
This release, nicknamed “Uwubernetes” was fairly routine. Nothing notable was deprecated, and it comes with a few very timely security enhancements. Overall, v1.30 brings 45 enhancements — 17 that are stable, 18 as Beta, and 10 as Alpha.
Being a Release Lead for the
[ Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)‘s Kubernetes is a bit like “herding cats,” [Cosgrove](https://github.com/katcosgrove) said.
“There’s a lot of politicking” to do.
Cosgrove led a large team, with nine direct reports, and 35 reporting to them. They were all spread out, globally, across five different subteams.
## Kubernetes Enhanced
Getting a feature into the next release of Kubernetes involves multiple hurdles.
A proposed feature begins as a
[Kubernetes Enhancement Proposal](https://www.kubernetes.dev/resources/keps/), (KEP). A Special Interest Group must sponsor a KEP for consideration in the next release. Those nominated make it into the enhancement freeze, after which no new KEPS would be considered for the release.
The resulting heap of new features can be a “complete crapshoot,” given the random nature in which they are nominated. After the enhancements freeze, the code freeze is enacted, “and this is where a lot of KEPs drop off,” Cosgrove said. Perhaps many found it would be
[more work](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/) to get their code to the production level than anticipated.
In this last round, 95 KEPS made it to the enhancement freeze, but only 45 made it to the code freeze.
“People are very optimistic at enhancements freeze about their abilities to get something done. And that’s okay, that’s totally normal,” Cosgrove said. “And then we face reality at code freeze.”
Testing has been done along this whole time frame, and a few alphas and beta releases might have also been issued of the upcoming release (which aren’t widely used). So the release candidates will start coming shortly after.
After all this corralling, the SIG usually requires the team release lead to take off a cycle before heading back into the fray.
“I’m ready to take some time,” Cosgrove said.
## Kubernetes 1.30: Who Are You?
Beyond security, other features also brought nuance to operations. For instance,
[KEP 1610](https://github.com/kubernetes/enhancements/issues/1610) (“Container Resource based Pod Autoscaling “) brought the ability to automate pod autoscaling based on the use of container resources.
“This lets you configure automatic scaling based on the resource usage for individual containers, rather than for the like total resource use across an entire pod,” Cosgrove said.
Such fine-tuning could help cloud costs, for instance. No longer will a whole pod be scaled up just to meet the demands of a particularly resource-hungry container.
This one caught the eye of
[Sergey Pronin](https://www.linkedin.com/in/sergeypronin/?originalSubdomain=ru), group manager for database service provider [Percona](https://www.percona.com/?utm_content=inline+mention).
To date, database systems have not worked well with Kubernetes pod autoscaler, due to data constraints.
“With the growing interest in data technologies that decouple storage and compute (like
[Neon](https://thenewstack.io/neon-branching-in-serverless-postgresql/), [Xata](https://thenewstack.io/automatically-generate-types-for-your-postgresql-database/)), this feature might enable users to scale properly,” Pronin noted, in an e-mail.
Pronin also pointed to (
[KEP-4381](https://github.com/kubernetes/enhancements/issues/4381) “DRA: structured parameters”) as “a very important addition to the k8s ecosystem.” It’s another feature to better scale resources, Dynamic resource allocation provides an API for requesting and sharing resources between pods and containers inside a pod.
It was added to Kubernetes as
[an alpha feature in v1.26](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/), though the inclusion of structured parameters introduced in Kubernetes 1.30, appears to make it easier to use.
“Structured Parameters for dynamic resource allocation offers a framework that would allow drivers to manage resources themselves, “using a specific ‘structured model’ pre-defined by Kubernetes,” the docs note.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)