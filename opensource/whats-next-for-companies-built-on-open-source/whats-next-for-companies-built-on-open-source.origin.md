# What’s Next for Companies Built on Open Source?
![Featued image for: What’s Next for Companies Built on Open Source?](https://cdn.thenewstack.io/media/2024/04/78e9352d-what-now-open-source-2-1024x576.jpg)
PARIS — In late 2023,
[DataCebo](https://datacebo.com/), a three-year-old startup, launched the enterprise version of its product, which helps organizations create synthetic data from relational and tabular databases.
The company aimed to solve a common problem for organizations: garnering data to test applications, a tedious and time-consuming process and one that’s hard to scale. A bank, for instance, might have more than 1,000 applications that each require test data.
The obvious downsides are security risks and the lack of flexibility because data can’t be gathered quickly, said
[Kalyan Veeramachaneni](https://www.linkedin.com/in/kalyan-veeramachaneni-9861b821/), DataCebo’s co-founder.
Synthetic data, by contrast, “has a very close resemblance to the real
[data](https://thenewstack.io/data/), both in format structure and statistical quality,” Veeramachaneni told The New Stack at [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-europe-webassembly-ebpf-are-huge-for-cloud-native/), in March. “But it’s not the real thing. And it’s not connected to the real data.” ![](https://cdn.thenewstack.io/media/2024/04/c03959d4-datacebo-300x284.jpg)
Kalyan Veeramachaneni, DataCebo’s co-founder.
Such technology — which Veeramachaneni and
[Neha Patki](https://www.linkedin.com/in/nehapatki/), DataCebo’s co-founder, began developing in 2016 as coworkers at [MIT’s](https://web.mit.edu/) AI lab — might once have been an obvious candidate for open source status, the type of project KubeCon was designed to celebrate. But in 2023, DataCebo pulled back the project’s [open source license](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/); it’s now source available, a distinction that restricts usage.
It’s always been
[tough to make open source pay](https://thenewstack.io/closure-is-open-source-licensing-suddenly-unsustainable/). But the past several months have seen some high-profile companies move critical projects from [open source licenses to more restrictive ones ](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)(see: [HashiCorp and Terraform](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/), [Buoyant](https://buoyant.io/)’s decision in February to [offer new releases of Linkerd service mesh exclusively commercial](https://thenewstack.io/buoyant-revises-release-model-for-the-linkerd-service-mesh/), and [Redis’](https://redis.com/?utm_content=inline+mention) announcement during KubeCon of its [plans for future releases and their licensing](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/)).
And yet, keeping your code open source and encouraging developers to tinker and tweak and contribute upstream —
[to build a community around your product](https://thenewstack.io/entrepreneurship-for-engineers-how-to-build-a-community/) — has historically been the best way to speed its adoption.
At KubeCon, The New Stack heard lots of debate over whether the open source business model really leads to return on investment,
[whether more companies are likely to follow the lead](https://thenewstack.io/the-open-source-markets-in-flux-how-can-it-managers-cope/) of [HashiCorp](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/) and Redis (spoiler alert: yes), and why the open source ethos remains important to innovation.
## Too Many ‘One-Offs’?
DataCebo changed its license because “we saw a lot of people are using it to compete” with the startup, using the tech to spin up products in direct competition, said Veeramachaneni, who also runs the
[Data to AI](https://dai.lids.mit.edu/) lab at MIT.
“The license change was also because I think
[AI is such a noisy area](https://thenewstack.io/ai/),” he said. “Coming from my background in AI, what we started to notice is not just company competition. People also were just building one-offs.”
A proliferation of “one-offs,” he suggested, could hurt the long-term commercial benefits of AI. They won’t “get AI adopted in a way that it generates ROI.”
[Lightbend](https://www.lightbend.com/), provider of a cloud native [microservices](https://thenewstack.io/microservices/) platform, [announced in September 2022 that it was moving the Akka framework,](https://www.lightbend.com/company/news/lightbend-changes-its-software-licensing-model-for-akka-technology) its flagship product, to a [BSL v1.1 (Business Source License)](https://www.lightbend.com/akka/license).
“I think every company has a different motivation for why they needed to do this,”
[Tyler Jewell](https://www.linkedin.com/in/Tylerjewell/), Lightbend’s new CEO, told The New Stack. “Our motivation was one of sustainability … what we had was an extremely permissive license that pretty much permitted any sort of behaviors.” ![](https://cdn.thenewstack.io/media/2024/04/5f19e22b-lightbend-jewell-boner-1024x625.jpg)
Lightbend CEO Tyler Jewell (left) and Jonas Bonér, the company’s founder and CTO.
There was also, he added, the eternal problem of making open source play. “Just to be honest, the economics we’re working out,” said Jewell, formerly of
[WSO2](https://wso2.com/), [Dell](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention) and [Oracle](https://developer.oracle.com/?utm_content=inline+mention).
“Our customers were basically leaving us and willing to just use it for free and not give anything back. And so we went to the BSL model, which is a model that says it’s free for development, it’s free for production if you’re under $25 million in revenues as a company.”
The change, he said, gives small companies a break while making larger customers that can afford to do so buy subscriptions. “And that’s brought us back into equilibrium with the community,” Jewell said. The Akka research and development team, he said, has tripled in size, enabling the company to invest in improving the product.
“We’re gonna see more of these things, as companies look for equilibrium, on a balance between how do you fund open source, but yet maintain it in a viable way.”
## No ‘Walled Garden’
Among the more than 19,000 software developers who work at
[Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention), thousands are contributing to more than 300 open source projects on a regular basis, according to [Arun Gupta](https://www.linkedin.com/in/arunpgupta/), vice president and general manager for the open ecosystem at the company.
Among the projects its devs contribute to are
[PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/), [TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/), [OpenJDK](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/) and of course [Kubernetes](https://thenewstack.io/kubernetes/).
In March, Intel released
[Continuous Profiler](https://github.com/Granulate/gprofiler), an optimization agent developed by Intel Granulate that combines multiple profilers into a single flame graph, enhancing observability.
Intel’s commitment to open source is strong, and Gupta’s commitment to the open source community is too: he’s currently serving as chairperson of the OpenSSF governing board.
The company continues to build products on top of open source projects. Early in 2024, Intel received
[Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) certification for its Intel Kubernetes managed service, part of its Intel Developer Cloud. “It is primarily targeted toward running AI workloads within the cloud native ecosystem,” Gupta told The New Stack at KubeCon.
He understands why more companies are starting to rethink their project licenses. “Businesses have to do what makes sense for them, right?” Gupta said. “There is no one model … For some businesses, that works very well. But for some, it doesn’t work. And particularly for companies that are backed by venture capitalists, there’s a lot of pressure for them to make money.”
But moving projects to more restrictive licensing can also exacerbate inequity and hamper innovation, he cautioned
“Intel’s belief is that an open ecosystem creates a level playground for everybody. And it should not be locked in a walled garden,” he said. “You can say that ‘we are creating a new product that is a business-only license,’ but changing your licenses midstream is break of trust.”
The collaboration and creativity unleashed by the open source community he added, is “the way we can take the world forward, because these are global challenges. So it really requires global collaboration. And you can only get global collaboration through an open source license.”
## Strategies: OpenTofu, Terraform, Cilium
[Harness.io](https://www.harness.io/) was among the first companies to support [OpenTofu](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/), the open source fork of HashiCorp’s Terraform, the ubiquitous [Infrastructure as Code (IaC) ](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)tool, which the company shifted to a Business Source License in August.
Harness.io uses both Terraform and OpenTofu in its own products,
[Martin Reynolds](https://www.linkedin.com/in/martinreynolds/), the company’s field CTO, told The New Stack at KubeCon, and is rooting for the success of both projects. “just to kind of have that ongoing open mic about open infrastructure as code.”
He expects to see more companies follow HashiCorp in moving their products to a BSL but points to the CNCF’s role in keeping essential projects open source.
![](https://cdn.thenewstack.io/media/2024/04/2232e166-martin-reynolds-300x295.jpg)
Martin Reynolds, field CTO of Harness.io.
Take, for instance, the case of
[Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/), the platform developed by Spotify and donated to the CNCF. Backstage, a platform that enables organizations to build customized internal developer portals, [has been a key enabler of the platform engineering trend](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/).
“If Spotify had taken that and made it that same Business Source License, then I think that would have impacted a lot of organizations that run their own Backstage,” Reynolds said.
[Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547), co-founder of [Isovalent](https://isovalent.com/), knows a thing or two about open source projects and commercial pressures: He’s co-creator of Cilium, which provides advanced networking and security controls, leveraging the [Extended Berkeley Packet Filter (eBPF)](https://thenewstack.io/what-is-ebpf/). Late in 2023, [Cisco](http://cisco.com/?utm_content=inline+mention) [announced it was acquiring Isovalent](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/).
At KubeCon, Graf was talking up the latest open source version of
[Cilium](https://cilium.io/) and its then-pending enterprise-grade release of the project. And he also looked back at the early days of the project and the company built around it.
“Our strategy from the beginning was always making it very clear, what is open source, and what is the enterprise portion,” Graf told The New Stack.
![](https://cdn.thenewstack.io/media/2024/04/2caff0c4-thomas-graf-300x278.jpg)
Thomas Graf, co-founder of Isovalent.
Thinking of the open source and enterprise versions as having unique needs, he suggested, helped his organization grow: “It’s not just click and install, and you have an enterprise-grade solution.”
Companies built on open source face tough choices when they don’t think through their commercial offerings from the outset, he said: “I think some projects have been a little bit more, ‘I’m all open source. And then I will figure out the monetization strategy later on.’ And then this switch is needed.”
Being acquired by Cisco, he said, won’t change the project’s relationship to open source.
“We found a strong partner that is truly committed to continuing our open source strategy, as we had it before while making it clear what are the monetizable paths, which is a little bit more on the enterprise legacy sites,” he said.
“The strategy will not be to try and make something that’s open now closed or change licenses.”
## Seeking More Transparency
[NGINX](https://www.nginx.com?utm_content=inline+mention), built on an open source application-delivery product and under the auspices of F5 for five years, is no stranger to the tensions between community and commerce.
“We’re adjusting the product strategy a bit,”
[Liam Crilly](https://www.linkedin.com/in/liamcrilly/), senior director of product management at F5, told The New Stack at KubeCon. “In the past few years, we tried to grow the business from having this core NGINX product that people know and love, generally. And then we tried to build more and more wrappers around that, to meet the needs of our enterprise customers. That’s been a rocky road.”
The new strategy, Crilly said, is to move many of the management, observability and orchestration tools NGINX has built to F5’s Distributed Cloud Console.
[NGINX One](https://thenewstack.io/nginx-melds-open-source-tools-into-an-enterprise-platform/), the new pay-as-you-go Software as a Service offering, is in early access status, Crilly said, moving toward general availability at the end of summer.
As far as open source goes, he said, NGINX intends to be more, well,
*open*.
“One of the major things is that we’re being a lot more transparent about the governance of source projects, and NGINX,” he said. The goal, he added “is that NGINX is seen as a modern, multiprojects organization.”
Embracing what he calls “modern, open governance” includes educating the developer community about
[which projects NGINX supports](https://github.com/nginxinc/): not just the core NGINX project but also a Kubernetes ingress controller, a gateway fabric, and more.
To do that, NGINX has hired a community manager and team, who are currently reaching out to open source developers through community Slack channels; it’s also looking at other ways to reach the rising generation of devs.
Open source still holds advantages for businesses seeking product adoption, Crilly said. “I think we’ll continue to see businesses use leverage open source, there’s no better way of reaching developers. So if that’s your market, you have to do it.”
But he also foresees changes in how tech companies approach the open source business model. “I think we’ll see people be a bit more explicit upfront about their intentions and maybe their charter. So it’s a lot more transparent.”
Crilly added, “There are numerous ways that organizations or corporations can monetize open source. But there’s no one size fits all. The ideal monetization strategy is not always available. Given market conditions and timing, I think right now it’s really hard.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)