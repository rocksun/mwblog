# Tackling the Fears and Risks of Cloud Abstractions
![Featued image for: Tackling the Fears and Risks of Cloud Abstractions](https://cdn.thenewstack.io/media/2025/05/774cba08-strings123-1024x576.png)
Cloud development has evolved rapidly, bringing ever more services, configuration files and complexity. In response, a new generation of intent-based, developer-first [cloud abstractions](https://thenewstack.io/microservices/the-future-of-microservices-more-abstractions/) has emerged to simplify the way we build in the cloud. These frameworks let you declare what you need at a high level, and they handle how to provision it.

Yet many [cloud developers and engineering leads hesitate to embrace these abstractions](https://thenewstack.io/abstracting-cloud-sdks-starting-with-the-runtime/). Why? Often it boils down to a fear of losing control and from past experiences with “leaky” tools, performance worries, sticking to one’s comfort zone or Not Invented Here (NIH) syndrome.

It’s natural to be cautious. After all, we’ve spent years mastering [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/) tools (Terraform, CloudFormation, raw SDKs, YAML) to have full control. Handing the keys to an automation layer can feel like a risky leap.

Oftentimes we discuss the benefits of abstraction without acknowledging or addressing the fears and risks. Let’s tackle some of the most common fears about cloud abstraction head-on.

## 1. Fear of Losing Control
“If I’m not configuring every resource myself, am I really in control?”

This is a common concern when moving from raw Terraform or CloudFormation to higher-level tools. Traditional IaC gives you control over (almost) every knob, but with that comes a mountain of complexity. The real fear isn’t about control, but about transparency. Engineers worry that abstraction will hide important details, making infrastructure harder to trust or debug.

But a good abstraction doesn’t take control away; instead, it shifts your focus to the things that matter. Rather than handcrafting every single IAM policy, you express what the application needs, and the framework handles the glue.

Take this simple example using Nitric:

12345678910111213 |
from nitric.resources import api, bucketfrom nitric.application import Nitricfrom nitric.context import HttpContextmain_api = api("main_api")images = bucket("images").allow("reading")@main_api.get("/file/<name>")async def get_file(ctx: HttpContext): url = await images.file(ctx.req.params["name"]).download_url(expiry=3600) ctx.res.json({"download_url": url})Nitric.run() |
That small snippet has enough information for us to know how to set up an API endpoint, a storage bucket, permissions, routing and compute. Although hidden, the control is still there, because you can override the Terraform used to generate the resulting [IaC](https://thenewstack.io/no-terraform-no-iac-are-you-looking-for-disaster/) without ever touching your application code.
For example, let’s say you look at this code, and your first question is, “How do I set API gateway timeouts?” My responding question would be, “How often do you change this setting per project?” If the answer is, “A lot,” then the abstraction should be able to elevate this configuration to your application configuration or config. However, if the answer is, “Rarely/never,” then having it live as a default setting in a module would be more appropriate.

This is what “real” control looks like: making high-impact decisions while automating the boilerplate, and allowing you to customize the underlying infrastructure only when needed.

## 2. Past Experiences With Leaky Abstractions
Many of us carry scars from past attempts at abstraction that didn’t go so smoothly. Perhaps you tried a PaaS or a fancy new framework that promised to handle everything, but when something went wrong, you had to dig through layers of complexity anyway. This is the classic “leaky abstraction” problem.

“All non-trivial abstractions, to some degree, are leaky.”

— Joel Spolsky, CEO and co-founder of Stack Overflow
No abstraction is perfect and ultimately, at scale and in edge cases, some of the underlying details will seep through. For cloud developers, this manifests as those painful moments when your high-level tool doesn’t support a specific config or throws an opaque error, and you’re forced to troubleshoot the raw infrastructure blind. It’s no wonder people get wary.

However, it’s important to realize why earlier abstractions leaked and how modern approaches address this. A lot of first-generation cloud abstractions (think early serverless frameworks or overly simplistic GUI-based cloud builders) were essentially thin wrappers over cloud APIs. The moment you stepped outside the happy path, you hit a wall.

Modern developer-first platforms have learned from those lessons. They tend to be open source and transparent. You can usually inspect what the abstraction is doing under the hood. For instance, Nitric will generate a Terraform configuration (via the Terraform CDK) that you can export and review if needed. This means if something isn’t behaving as expected, you’re not debugging a black box; you can actually see the intermediate IaC that the framework produced. That’s a huge improvement in trust.

Good [abstractions provide escape hatches](https://thenewstack.io/how-escape-hatches-make-abstraction-more-powerful/) and extension points (as we saw above with overriding modules). The goal is that when the abstraction doesn’t directly support an edge case, you can extend it rather than abandon it. Contrast this with a leaky abstraction that forces you to break abstraction entirely (such as manually patching something outside the tool). With the ability to extend or inject custom logic, the abstraction itself isn’t “broken” by new requirements; it bends to accommodate them.

## 3. Not Invented Here (NIH) Syndrome
Not Invented Here syndrome isn’t a technical fear so much as a cultural one. Engineering teams, especially very capable ones, often believe that their needs are unique and that they can build a superior solution in-house rather than using an external abstraction or platform. You might hear sentiments like, “Why use this framework? We can just script all this ourselves and tailor it perfectly to our environment.” Or, “We don’t want to depend on an external tool; let’s build our own lightweight version.” It’s the instinct to roll your own, stemming from pride, control or sometimes skepticism that a generic tool can fit your special case.

“Many companies suffer from Not Invented Here syndrome, coming up with custom solutions instead of choosing a third-party tool.”

— Mykyta Protsenko, Netflix
While the DIY approach can be useful in some truly unique scenarios, more often it leads to reinventing wheels and wasting time solving solved problems. This tendency can trap teams in endless maintenance of internal tools that never quite get finished or documented. If your developers spend months building an internal deployment framework, that’s months they weren’t delivering business features.

“Stop spending money (and time) on undifferentiated heavy lifting.”

— Werner Vogels, Amazon
When it comes to cloud infrastructure, think about the core competency of your team. Is writing and maintaining an internal cloud platform really a differentiator for your business? If you’re a cloud provider or selling developer tools, maybe? Otherwise, probably not. For most product companies, the differentiator is the application or service they offer, not the bespoke scripts that deploy it.

So why invest heavy effort there when you could leverage an existing framework and get back to building product features? Using an abstraction, especially an open source one, also means you benefit from a community of users. Bugs are found and fixed by others, new features get added by contributors, and you can hire engineers who might already be familiar with it. With a proprietary internal tool, you carry the full burden alone.

To be clear, “Not Invented Here” isn’t about blindly accepting any off-the-shelf tool. You should still evaluate the maturity and community of a solution. When an abstraction meets 80% to 90% of your needs, it’s usually wiser to build on it than to create your own from scratch.

“I much prefer other people solving my problems for me”

— Linus Torvalds, creator and lead developer of the Linux kernel
## Conclusion: Embrace Abstraction To Gain Leverage
Think of abstraction as leverage. Just as high-level programming languages and libraries let us accomplish more with fewer lines of code, cloud abstractions let us accomplish more with less YAML and scripting. They free us from reimplementing the same patterns over and over. They shift our focus from the plumbing to the product.

When you no longer have to worry about which knob to turn to enable an integration or how to format an IAM policy, you can devote that mental energy to innovating in your domain. As a result, teams move faster, deploy more confidently and suffer fewer “it works on my machine” headaches because the platform takes care of consistency across environments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)