Google Cloud announced it had put [Cloud Run sandboxes](https://cloud.google.com/blog/topics/developers-practitioners/google-cloud-run-sandboxes-are-in-public-preview) into public preview earlier this month at WeAreDevelopers World Congress in Berlin, a few weeks after AWS shipped its version. And both sandboxes answer the same question: *Where should the code an agent just wrote actually run?*

Here’s why it matters: Two hyperscalers launching sandboxes in the same quarter completes the group. Now, all four major clouds (AWS, Google Cloud, Microsoft Azure and Cloudflare) offer isolated code execution as a native primitive, and they expose materially different isolation stacks and lifecycle models.

## Four clouds, four isolation technologies, one product shape

AWS built [Lambda MicroVMs](https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/) on Firecracker, giving each session a dedicated virtual machine with up to eight hours of runtime and a suspend-resume cycle that preserves memory, disk, and running processes. Google went two ways, using gVisor kernel interception for the GKE Agent Sandbox, and Cloud Run adds a lightweight isolated execution boundary within an existing Cloud Run instance.

Microsoft got to this pattern first. Azure Container Apps [dynamic sessions](https://learn.microsoft.com/en-us/azure/container-apps/sessions) have run on Hyper-V boundaries since 2024, and Microsoft reported that Copilot alone consumes more than 400,000 of those sessions per day. Cloudflare built Sandboxes on top of Containers, with each sandbox isolated in its own VM and controlled through Workers and Durable Objects.”

Four vendors, four genuine architectural disagreements about where the security boundary belongs. The product each one sells is the same: send in untrusted code, and the platform runs it somewhere isolated from the calling application, with credential exposure governed separately.

## On Cloud Run, the sandbox became a flag

The Cloud Run implementation makes the shift plain. A `--sandbox-launcher` flag on the deploy command mounts a sandbox binary at `/usr/local/gcp/bin/sandbox` inside the container, and the application shells out to it through a normal subprocess call. Google charges no premium for the feature because sandboxes borrow the CPU and memory already allocated to the running instance. Google reported a demo where one Cloud Run service started, executed, and stopped 1,000 sandboxes at an average of 500 milliseconds each.

Google’s own announcement framed the alternative as building complex sandboxing infrastructure on container clusters or paying for specialized third-party microVM runtimes. That sentence is aimed at a category of vendors. They built real businesses in the gap between containers that share a kernel and virtual machines that take minutes to boot. Each of these four vendors now offers managed sandbox execution, though their packaging and pricing differ.

## Isolation is a containment boundary, not a governance layer

A Firecracker VM isolates generated code from the host and other sessions; credentials and network reach remain configuration decisions. It does nothing about what that code does with the credentials the developer deliberately handed it, and governance sits in an entirely separate layer. The containment boundary sets the ceiling on how much autonomy you can safely grant, and it is the cheaper half of the problem.

The vendor constraints also survive the commoditization, and they are specific. Lambda MicroVMs run on Graviton in five regions and cap at eight hours, so a team that needs x86 or a longer horizon still owns the orchestration. Cloud Run sandboxes share the parent instance’s CPU and memory, which means a runaway script competes with the service that spawned it. If those vendor-specific limits stay this sharp, the neutral multi-cloud sandbox keeps its pitch, and this reads as a commoditization that never finished.

Every cloud now agrees that agents should not run code on the host, which moves the argument to who governs what the code does once it is safely contained.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)