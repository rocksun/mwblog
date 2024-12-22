# Year in Review: Containers Get Smaller, Faster, More Secure
![Featued image for: Year in Review: Containers Get Smaller, Faster, More Secure](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)
Yelp uses thousands of containers as part of its webscale operations. And one of its number one challenges with containers is security, said [Tom Robinson](https://www.linkedin.com/in/trobinso/), Yelp software engineer, [in a talk](https://www.youtube.com/watch?v=QeR3jeLs_l0&list=PLn5JwIxcXmNqDljfxkBKNY88sd8KYKCnY&index=3) at KubeCon+CloudNativeCon North America earlier this year about creating a [maturity model](https://thenewstack.io/why-maturity-models-are-fundamentally-broken/) for containers.

“If you are thinking about this from the perspective of an attacker, they are starting in the container,” Robinson said. Once inside, malicious attackers look around, and if they find a passage to your storage buckets, they will go for the valuable data.

For the developer, “the most difficult challenge is meeting the business needs while keeping your application secure,” he said. “There’s always this tension between developing product and developing it securely.”

Already, the organization has thousands of alerting mechanisms around its containers, but this data only leads to alert fatigue in its engineers. What Yelp truly needed, he explained, was a way to enforce security best practices at scale.

As a result, Yelp has built a model of container security maturity, a way to abstract and thereby understand the level of access, data sensitivity and levels of impacts.

Once the best practices are established, automated compliance checks can then be added.

Now that containers have been with us for more than 10 years now, powering webscale and at-scale enterprise applications for companies like Yelp, cutting-edge technology keeps moving forward.

Here are some of the developments in the world of containers in the year of 2024.

## Builds Beyond Distros
The original idea for Docker containers was that they would be built on a Linux distribution (Usually [Debian](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/)), which would provide the core components to run the application. This means, however, that each container image has been festooned with hundreds of MBs of useless libraries, which take up space and [pose security threats](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/).

So, there has been a lot of work over the past few years to strip out the unnecessary bits of the container, an approach sometimes called *distroless*.

In June, Canonical [debuted](https://thenewstack.io/canonical-offers-lts-distroless-containerized-apps-for-k8s/) containerized versions of [Docker](https://www.docker.com/?utm_content=inline+mention)-packaged open source software, built on the standardized Open Container Initiative (OCI) format, so the LTS containers should run in any OCI-compliant runtime environment.

These “distroless” containers would be ideal for Kubernetes environments, where they can be packed together in a pod for maximum computational efficiency.

In a Kubecon EU talk earlier this year “[Building Container Images the Modern Way](https://www.youtube.com/watch?v=nZLz0o4duRs&list=PLn5JwIxcXmNqDljfxkBKNY88sd8KYKCnY&index=2),” from [Adrian Mouat](https://www.docker.com/captains/adrian-mouat/), a technical community advocate from security firm Chainguard, offered an overview of other work going on to build minimal containers.

Containers are basically application packaging formats. It is a file system and metadata.

What should an image have? It should keep extra files to a minimum, be fast and reproducible, and be generic across different systems.

Docker and Google both offer alternatives to this approach, he noted, in an approach that involves multistage builds.

Multistage Docker builds, when combined with minimal runtime images, can be one of the best ways to build images, Mouat said.

![code for building the Go app containe.](https://cdn.thenewstack.io/media/2024/12/ddb380e2-mouat-01.png)
Building an Go app using the Go static image, resulting a file size only a few megabytes.

Both [Chainguard](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future) and [Google](https://github.com/GoogleContainerTools/distroless) offer minimal images from which to build. You can even use a [scratch image](https://hub.docker.com/_/scratch) if you want to run a static image, and you don’t need any OS functions such as TLS, Mouat said.

Another that can be used, at least for Go applications, is [ko](https://github.com/ko-build/ko). Built from the `go build`
command, Ko doesn’t even require docker to be installed.

![ko, a Go builder](https://cdn.thenewstack.io/media/2024/12/556e8e29-demo-1024x386.png)
ko in action.

Those who want to build their own distro-less images can use [Google Bazel](https://bazel.build/) or Chainguard’s [Apko](https://github.com/chainguard-dev/apko) (built on [Chainguard’s Wolfi](https://github.com/wolfi-dev)), though Mouat cautioned against this approach whenever possible.

“Bazel is phenomenally powerful,” though it can also be quite confusing, Mouat said. The help command produces nearly an entire book of information. Also, it has odd behaviors. For instance, it uses the Google base image rather than building its own for each new image.

“If you want to use Bazel, you have to know what you’re doing.”

Apko is not quite as powerful as Bazel in terms of features, though it offers bitwise reproducible builds, which means two builds of the exact same image will be identical when compared bit-by-bit (including the SHA-1 hashes).

In policy-heavy environments, bit-wise reproducibility is a major factor in ensuring security. Chainguard uses it to build minimal distroless runtime images,

Other approaches Mouat discussed include [BuildPacks](https://thenewstack.io/safer-image-builds-with-cloud-native-buildpacks-and-wolfi/), [BuildKit and Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/), and [Nix](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/).

## Zero Overhead Container Networking
Introduced in the [6.7 release](https://lwn.net/Articles/949960/) of the Linux kernel is support for Netkit, an [eBPF-programmable](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/) network device that shortcuts some of the travel up and down the stack network packets must do to move from one container to another (even in cases where both containers are on the same host).

Like other virtual network devices, the devices are added to both the host and the container’s namespaces, with the host being the primary.

In her talk at [ScyllaDB’s P99 Conf](https://thenewstack.io/p99-conf-3-ways-to-squash-application-latency/) earlier this year, Isovalent Chief Open Source Officer [Liz Rice](https://www.linkedin.com/in/lizrice/) called the approach “[Zero Overhead Container Networking](https://www.p99conf.io/session/zero-overhead-container-networking-with-ebpf-and-netkit/).”

With containers, applications are isolated from the host and from other applications with their own network namespaces, separate from that of the host. Connections are made through the virtual network devices.

“So, packets going to or from a containerized application actually have to pass through the network stack twice,” Rice explained. In addition, packets can get dropped and the congestion control algorithm kicks in, hobbling throughput even further.

An eBPF-based program is used to bypass ingress host routing by switching network packets directly into the container’s networking namespace, “so it appears that as if it were arriving over the virtual wire to virtual network device inside the container,” Rice explained.

For egress traffic, an eBPF helper function can consult the kernel forwarding information base to find the next routing hop.

Further performance gains are enjoyed by attaching eBPF function to the container’s own networking stack, which was achieved in a project called tcx (TC Express), [debuting in the 6.6 kernel](https://lore.kernel.org/all/20230719140858.13224-1-daniel@iogearbox.net/), cutting the number of CPU cycles it would take by approximately half for a packet to get to the BPF functionality (59 to 33 cycles).

As a result, “Netkit devices achieve the same throughput as you get with native host networks,” Rice said.

[Isovalent](https://isovalent.com/), whose engineers worked on the project, [added NetKit support](https://isovalent.com/blog/post/cilium-netkit-a-new-container-networking-paradigm-for-the-ai-era/) this year to its [Cilium cloud native networking platform](https://thenewstack.io/can-cilium-be-a-control-plane-beyond-kubernetes/).
## Dockerfiles Still Rule the Roost
Despite all these advances, on both the development and operations sides, most developers remain comfortable with traditional [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/), which are text files with instructions on how to build a container image.

“I famously hate Dockerfiles, but they have been such a pragmatic (and now ubiquitous) path to folks adopting containers that I don’t think they are going anywhere quickly,” said [Matt Moore](https://www.linkedin.com/in/mattmoor/), founder and CTO of [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention), speaking with TNS.

The company’s practices, such as maintaining Golden Images and strict pipelines, are very pragmatic, Moore noted.

Chainguard, as noted above, takes the “last mile” image-building approach with “distroless” images and tools such as ko, [Jib](https://cloud.google.com/java/getting-started/jib), and [CNCF buildpacks](https://www.cncf.io/projects/buildpacks/).

“We are seeing tremendous momentum at Chainguard of folks adopting our images, but we do still see a lot of folks dropping them into good old-fashioned Dockerfiles from Chainguard,” Moore said.

“While it’s good to see interesting and novel ideas surface again, I have a hard time imagining any gaining serious inroads against the now-ubiquitous format,” said [Matt Butcher](https://www.linkedin.com/in/mattbutcher/), CEO at [Fermyon Technologies](https://www.fermyon.com/?utm_content=inline+mention). “As interesting as many of those ideas were, it turned out that Dockerfiles were, on the whole, just easier.”

*TNS analyst Lawrence Hecht contributed to this report. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)