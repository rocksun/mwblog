# Infrastructure From Code: What Went Wrong
![Featued image for: Infrastructure From Code: What Went Wrong](https://cdn.thenewstack.io/media/2025/05/4e5c6ab7-ifc-control-1024x573.png)
The idea behind [Infrastructure from Code](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/) (IfC) is that you would simply write out all deployment and configuration steps in a programming language of your choice and be done with it — no more worrying about how your app would run in the cloud. It was a step forward from [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/) (IaC) tools such as [Terraform](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/) and [OpenTofu](https://thenewstack.io/opentofu-turns-one-with-opentofu-1-9-0/).

Best of all, no [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) was needed.

“Spoiler alert: It didn’t work,” said [Allen Helton](https://github.com/allenheltondev), an ecosystem engineer from cache platform provider [Momento](https://www.gomomento.com/company/about/), [speaking](https://www.youtube.com/watch?v=10mU9eqN7m4&list=PLocaoeyiLZlU1jkC6Kysu_IyD8h3wE3mL&index=11) at the virtual [IaCConf 2025](https://www.linkedin.com/showcase/iac-conf/) about the [short-lived trend](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom/) of IfC.

Helton had some ideas as to why the IfC did not work as advertised on the tin. And others at the conference, hosted by [Spacelift](https://spacelift.io/?utm_content=inline+mention), offered their own learned lessons on automating the deployment of infrastructure and keeping it as manageable as possible.

## Context Switch
The cloud made things complicated for application developers, Helton said. Gone were the days when you could hit F5 and send your code into production with nary a thought of how it would be run. They now had to worry about infrastructure.

With the cloud, “I’d always be context switching between my template file and my business logic, and that slowed me down,” he recalled.

IfC promised to eliminate all of this context switching.

![Klotho logo](https://cdn.thenewstack.io/media/2025/05/3bf95233-klotho-150x150.jpg)
Klotho, no more.

It seemed like a good idea, and a wave of vendors whipped up an impressive array of support tools: [Nitric](https://nitric.io?utm_content=inline+mention), [Klotho](https://klo.dev/ifc/), [Encore](https://encore.dev/docs/ts), [Wing](https://thenewstack.io/wing-the-startup-failed-but-the-language-has-potential/), [Shuttle](https://www.shuttle.dev/blog/2022/05/09/ifc), [Dark](https://blog.darklang.com/what-is-dark/) and [Ampt](https://www.getampt.com/docs/overview/).

Each took a slightly different approach. Wing offered its own [programming language](https://thenewstack.io/winglang-cloud-development-programming-for-the-ai-era/), allowing a compiler to convert it to code that would run infrastructure. Klotho used JavaScript, adding a set of annotations for infrastructure calls.

Yet, all these approaches had difficulty finding market traction, Helton recalled.

## Don’t Worry, Nothing’s Under Control
Many of the above-mentioned companies have gone out of business or stopped developing — Wing, Klotho — while others are pivoting or going into maintenance mode. Only Nitric and Encore seem to be still thriving.

In Helton’s opinion, the problem with the IfC approach was that developers weren’t quite ready to give up control.

With IfC, the vendors controlled what resources a developer could work with to keep things simple. So it was the vendors that decided how the customers’ infra would be configured.

That was a nonstarter for most developers.

The vendors promised best practices out of the box. But the best practices of the vendor would rarely be the optimal practices for the customers themselves. Many enterprises may have special needs around HIPAA or other external or internal mandates.

In a nutshell, IfC promised great rewards for those who were willing to give up a bit of control of their infrastructure.

“As abstractions get higher and higher, it makes us uneasy, because when you abstract and you take away configurability, we get out of our comfort zone.”

— Allen Helton, ecocsystem engineer at Momento
“The subtext there was, ‘Trust us, we got you, especially when something goes wrong,’ which means when something does go wrong, you’re really at the mercy of their SLAs [service-level agreements].”

And if devs and software engineers did not like to give up control, you can bet platform engineers and [DevOps folks](https://thenewstack.io/devops/) won’t be too keen on the idea either. In fact, DevOps engineers and platform engineers have the specific job of [controlling infrastructure](https://thenewstack.io/foundational-concepts-in-platform-engineering/). They were the ones who decided what cloud provider to use and how to meet various mandates.

In other words, IfC was doomed from the start, Helton said.

“Infrastructure from code is a genuinely fascinating topic, and I’m sad to see that it didn’t work,” Helton said. “It was really cool in demos, but I think in practicality, it was not the right fit” for where the industry was at.

## Adaptive Infrastructure, the Other AI
Turns out, managing infrastructure is a lot more of a dynamic job than can be easily handed over to a vendor and forgotten about.

Infrastructure is not a one-time deal. It needs to change as business requirements change, and as app needs change, Helton said. What we really need is adaptable infrastructure, driven by [artificial intelligence](https://thenewstack.io/ai-engineering/), that looks at current usage and suggests optimizations in real time.

Then, customers will balance between cost, latency and fault tolerance to their own liking: Services that rarely run at night can switch from containers to serverless to save money.

## Paved Road or Golden Path?
If IfC turns out to be a dead end, are there other ways forward to [provisioning infrastructure](https://thenewstack.io/terraform-1-0-reflects-what-hashicorp-has-learned-about-infrastructure-as-code/) in an [automated](https://thenewstack.io/iac-is-too-complicated-wheres-that-easy-button/) and [headache-free pattern](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/)?

In another [IaCConf talk](https://www.youtube.com/watch?v=iSK-6INXBYo&t=1347s), [Vega](https://www.vega-alts.com/) principal engineer [Joe Hutchinson](https://www.linkedin.com/in/joe-hutchinson-459681103/) offered a few other possible directions for IaC, with lessons that drew on [platform engineering](https://thenewstack.io/platform-engineering/).

Provisioning IaC with something like [Terraform](https://thenewstack.io/terraform-and-the-tooling-multiverse-in-the-future-of-iac/) seems great for the first project, but as more projects are added on, IaC looks increasingly chaotic and difficult to manage.

“At some point, you realize this is a tangled mess,” he told the virtual audience.

“A lot of the complexity that I’ve run into in my career has come from an IaC world that is well-structured trying to interface with parts of my company that are not configured as code, and maybe not as well structured,” he added.

In his talk for British fintech firm [Checkout](https://www.checkout.com/), Hutchinson described a few ways to get it right — or at least make it better.

First, what you do is to measure what you already do, and pick one metric to improve.

“If I was doing it again, I’d be measuring engineering efficiency,” he said.

Checkout had three DevOps engineers managing infrastructure to support 200 engineers working on various projects. The fast-growing company looked towards decentralizing operations to a “[Spotify model](https://thenewstack.io/platformcon-how-spotify-manages-infrastructure-with-gitops/).” It established a platform engineering team to “accelerate teams.”

The company had an opinionated platform, built from a [headless Backstage deployment](https://thenewstack.io/five-years-in-backstage-is-just-getting-started/), configured by Terraform to offer an array of tools. Product teams used the modules to enable the tools they needed.

“Being able to measure things and quantify the benefit would have been a much easier journey,” he said.

*Update (6/13/2025): All of the talks from IaCConf 2025 have now been posted on YouTube, so check ’em out.*
## Join our webinar for the latest insights on Infrastructure as Code
Key Webinar Takeaways:

- Why your IaC strategy is backfiring (and what to do about it).
- The essential capabilities your cloud platform needs, regardless of which IaC tools you use.
- Exclusive predictive insights on what cloud operations will look like in 2026.
- Practical solutions for the biggest issues uncovered by the 2025 State of IaC survey.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)