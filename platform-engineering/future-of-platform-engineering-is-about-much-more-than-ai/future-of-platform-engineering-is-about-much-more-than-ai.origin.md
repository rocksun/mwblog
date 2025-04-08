# Future of Platform Engineering Is About Much More Than AI
![Featued image for: Future of Platform Engineering Is About Much More Than AI](https://cdn.thenewstack.io/media/2025/04/4a26ecbf-viktor-farcic-mauricio-salatino-kubecon-2025-1024x576.jpg)
LONDON — “All I had to do, all I knew how to do, was write code, and then everything else that needed to be done, was done always by somebody else,” said [Viktor Farcic](https://www.linkedin.com/in/viktorfarcic/), developer advocate at [Upbound](https://www.upbound.io/?utm_campaign=2022_Q3_EVER_GBL_The-NewStack-GENERAL&utm_medium=The-New-Stack&utm_source=referral&utm_content=inline-mention), to kick off his talk at Platform Engineering Day here.

“Realistically, I spent most of my time in those early days waiting for something to happen, waiting for somebody to do something that somehow enabled me to continue writing code.”

For his talk at Platform Engineering Day on Tuesday, ahead of [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/), Farcic was joined by [Mauricio Salatino](https://www.linkedin.com/in/salaboy/), author of “[Platform Engineering for Kubernetes](https://www.manning.com/books/platform-engineering-on-kubernetes?utm_source=salaboy&utm_medium=affiliate&utm_campaign=book_salatino2_continuous_9_18_21&a_aid=salaboy&a_bid=b7ac598c&chan=mm_conference1)”and open source software engineer at Diagrid. The pair started sharing their history and future of [platform engineering,](https://thenewstack.io/platform-engineering/) reflecting the beginnings of their software development careers.

Similarly, when he started out as a [Java](https://thenewstack.io/introduction-to-java-programming-language/) application developer, Salatino said, he was “always using a very strong development perspective. I really cared about the applications that we were building more than how they were running in production.”

To save time, they both started automating some of their repeat work, like [testing](https://thenewstack.io/introduction-to-software-testing/), and embracing [test-driven development](https://thenewstack.io/a-next-step-beyond-test-driven-development/) and behavior-driven development — all done manually.

“That eventually led to other people starting to use what I’m doing,” Varcic said. “Then the question comes along, if you create a bunch of tools, no matter which technology you’re using, and those tools happen to be used internally by everybody else, or many people in your organization, would you consider that a platform?”

Salatino created Java application server capabilities so he didn’t have to write other functions, and built libraries to reuse functionalities across applications, which he also ended up sharing with colleagues. Was that application server a platform?

Did the first [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) emerge naturally as a result of collaborative teamwork? Or is platform engineering something intentional? When does a platform turn into an IDP? Knowing these answers, what is the future of platform engineering in the face of [AI](https://thenewstack.io/ai/)? Read on and come along for the journey.

## The First ‘Golden Paths’
About 15 years ago, the [API](https://thenewstack.io/api-management/) arose as the standard way to interact with, build on top of, or extend anything. And thus were laid down the first bricks of the future internal developer platform’s [golden paths](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/).

The API continues to be the scaffolding for the internet and is still the standard way to enable extensibility on top of your platform.

Next came [Docker](https://www.docker.com/?utm_content=inline+mention), which Farcic said was never related to building platforms, but rather it was about how to package applications in some kind of standard way and then run them anywhere but production.

“What made Docker really, really special, is that it is the first time that I saw engineers from different areas all get interested in the same thing,” Farcic said. “The first time that everybody said, ‘Oh, this is cool. We all want to use this.’”

All different kinds of engineers could indeed do cool things with Docker around packaging and runtime, but, he said, it wasn’t really available in production.

What really changed everything was [Kubernetes’ launch in 2014](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/).

“We all agreed that this is where we’re going to put our stuff, whatever our stuff is — databases, applications, infrastructure, whatever,” Farcic said. “We finally got industrywide agreement of where we are going to build stuff on.”

Companies just had to work out how to get there. And, [especially for developers](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/), that hasn’t been an easy ride.

Still, all along this journey, platforms have existed.

“Companies have been building platforms and failing to build platforms for 30 or 40 years now. We’re not doing anything new in terms of what we want to accomplish,” Varcic said. “The technology and some patterns are what’s new. That’s what’s changed recently.”

That — and the industry coalescing around the term “platform engineering.”

## The Patterns of Platform Engineering
The common patterns for platforms aren’t new, either. It’s always [Kubernetes](https://thenewstack.io/kubernetes/) and APIs, with controllers in the middle.

For example, [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) has always been a public platform, Farcic argued. “They own it, they develop it, they manage it [on behalf of] service consumers — those are all the users of that service that are somehow consuming it and doing something with it.”

There have always been service owners and service consumers, but lately the industry has turned its eyes more on treating internal developers as first-class consumers, following a [Platform as a Product mindset](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/), with APIs remaining as the preferred way to deliver that desired experience. Add to that, Kubernetes has become that de facto base the platform sits on top of — and abstracts away its complexity.

It then becomes less defined whether organizations are going [build or buy](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/) controllers. In both Farcic and Salatino’s experience, organizations usually start with a third-party controller — most often open source tools found in the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) [landscape](https://landscape.cncf.io/).

Then, Salatino said, you need a bunch of capabilities to add onto your platform, like [Knative](https://github.com/knative/serving) for request-driven compute and [ArgoCD](https://github.com/argoproj/argo-cd) for declarative continuous deployment. And no matter what kind of custom IDP you build, he said, you need certain things built in early on, like security and observability.

“Six years ago, most of us at that time we were choosing what third party we were going to use or contribute to,” Farcic said.

And then, Salatino continued, it was about figuring out the next step: How do you make your platform your own for your own domain needs? His role went from working in infrastructure to helping other engineers write the mechanisms for his job.

The [platform engineer role](https://thenewstack.io/how-to-hire-a-platform-engineer/) evolved organically from there, even before it had the name.

The final pattern or best practice in this current age of platform engineering is working to make your IDP more user-friendly with dashboards, [GitOps](https://thenewstack.io/streamlining-kubernetes-implementation-with-gitops-best-practices/) and more.

For Salatino, this is achieved by hiding the Kubernetes complexity behind the platform, extending it via APIs and providing services to users.

## Platform Engineering: Building for Speed
Now that the basic patterns for platform engineering success are settled on, everything has to be optimized for speed.

Over the last three or four years, in the face of the CNCF landscape complexity and in response to organizations sharing their experiences, platform engineering blueprints have emerged that mix and match different third-party toolsets in a cadence.

The three most common platform engineering blueprints right now are:

[BACK Stack](https://github.com/back-stack):[Backstage](https://thenewstack.io/new-spotify-portal-for-backstage-eases-platform-engineering/), ArgoCD,[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/)and[Kyverno](https://thenewstack.io/using-the-kyverno-cli-to-write-policy-test-cases/).[CNOE](https://thenewstack.io/building-an-idp-with-help-from-the-open-source-cnoe-framework/): Kubernetes, ArgoCD, Backstage, Crossplane and[Keycloak](https://github.com/keycloak/keycloak).[KusionStack](https://github.com/KusionStack): Kusion, Karpor and Kuperator.
“I think that this is a huge step, showing that the community is moving forward. We have these blueprints, and definitely we are trying to reduce the time that it takes for organizations to get started,” Salatino said.

Each, he added, is “a different blueprint, a different combination of tools that you can swap components out, depending on what you want to use — but again, showing the way how to get there without figuring out all the combination of possible tools that you can use.”

There’s still more to do to get nascent platform engineers up to speed, which is why the CNCF is launching a [platform engineering certification program](https://training.linuxfoundation.org/platform-engineering-programs/). And to make sure all of this platform engineering momentum doesn’t come with ignoring the end users or consumers — the internal developers — KubeCon Europe 2025 even includes an application development track for the first time ever.

That move, Salatino said, is not only intended to share platform engineering experiences and advances but to get feedback from app developers on how to build a better platform — including on how much Kubernetes really has to be abstracted.

## What’s AI’s Role in Platform Engineering?
Finally, unsurprisingly, [AI](https://thenewstack.io/ai/) has its role to play in the next step of improving platform engineering strategies.

“How do we bring AI functionality inside of our platforms without just calling [a [large language model](https://thenewstack.io/llm/)] from our applications?” Salatino said. “Because, if we do that, then we’re just wasting away all the platform stuff, all this conversation that we are bringing.”

In March, the CNCF announced the extension of its graduated [Dapr](https://thenewstack.io/dapr-graduates-cncf-and-connects-to-webassembly/) project with the release of the [Dapr AI Agent Framework](https://github.com/dapr/dapr-agents), which aims to build autonomous, resilient and observable AI agents with built-in workflow orchestration, security, statefulness and telemetry.

“If you want to access LLMs, you need to make sure, as platform engineering, that your security is integrated with all the other security policies that you have in your company, that you can govern this access in a consistent way, that you have resiliency and observability,” Salatino said. “We want to make sure that no matter what kind of data are you using, no matter the language that you’re using, you always need to provide workflows integration with governance.”

A strong emphasis of Dapr is that, no matter what LLM developers use, and even what agentic AI framework they choose to use, he said, these crosscutting concerns are carried throughout:

- Security: access control, secure credentials and personally identifiable information obfuscation.
- Resiliency: automatic retries, request timeouts and circuit breaker.
- Observability: request tracing, network metrics and error logs.
Like all things open source, even AI, it comes down to how communities build together.

As Salatino reminded his audience, “Cloud native platforms are not built in isolation. If you are building a platform inside your company, make sure you talk to other companies, make sure you share your knowledge.”

Are you ready to get started on your platform engineering journey? Get a free copy of our ebook: “[Platform Engineering: What You Need to Know Now](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)