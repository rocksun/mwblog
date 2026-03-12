Agentic AI development company [Tetrate](https://tetrate.io/) has launched [Built on Envoy](https://builtonenvoy.io/), a free and open source extensions marketplace for Envoy.

Envoy is an open source edge and service proxy for cloud-native applications. Tracing its origins back to [ride-hailing service Lyft](https://thenewstack.io/lyfts-envoy-provides-move-monolith-soa/), Envoy’s service proxy ability enables it to act as an intermediary server to manage network traffic between services for better security.

Described by the [Envoy project team](http://envoy) as a “universal data plane for microservices,” Envoy runs alongside every application and abstracts its network services by providing common features in a platform-agnostic manner.

The company says it now offers a way to overcome deployment pitfalls that slow teams down; it has packaged those best practice processes as ready-to-use extensions and made them available to everyone in the community at no cost.

But what has the potential to make Envoy troublesome?

## Why is Envoy a killjoy bad boy?

Common barriers to Envoy adoption include security and authentication hurdles, such as [Web Application Firewall (WAF)](https://thenewstack.io/waf-securing-applications-at-the-edge/) integration, OAuth2 token exchange, Security Assertion Markup Language (SAML) issues, and broader authorization workflow nuances.

Rarely a plug-and-play task for any software engineer, WAF integration gets complex when developers use it to apply security rules to their code that block some data, but still allow legitimate user traffic through; all of which is fine, but WAF rules need to be updated when the developer’s codebase changes — and codebases clearly do change. SAML can encounter attribute-mapping challenges when one software system labels a common entity (such as email) in a different format than another system, leading to missing claim errors. You get the picture, encryption handshakes are not always warm.

Other Built on Envoy marketplace extensions are designed to handle AI governance requirements, like checking LLM requests against [Azure Content Safety](https://thenewstack.io/microsoft-adopts-openinfra-kata-containers-security-on-azure/) (an AI service for detecting and filtering harmful text and image content) and caching model requests, as well as operational needs, including proxy configuration for data platforms and routing zone pinning.

A file-server extension service rounds out the initial set of marketplace stalls on offer here. This is technology that allows teams to serve static assets such as HTML pages, dashboards, and documentation directly from Envoy without deploying a separate web server.

Built on Envoy includes a CLI package manager that lets developers run Envoy with extensions on their local machines using simple commands, reducing the time required to experiment, prototype, and iterate.

## Custom extensions apprehensions

Tetrate aims to validate its work on this new offering by reminding us that Envoy’s advanced capabilities have traditionally been accessible only to teams with deep, specialized expertise. The company says that many software engineering teams end up building custom extensions behind closed doors, duplicating effort and missing the chance to share what they have built.

Based on the above, an open source marketplace for developers to download and deploy proven extensions feels timely. Creator of Envoy [Matt Klein](https://www.linkedin.com/in/mattklein123/) says he’s excited about the whole project.

“To date, writing extensions for Envoy has been a laborious process that involves writing C++ and compiling a fully custom build of the entire proxy. The rise of dynamic modules and allowing either Go or Rust to be used for extensions is going to unlock Envoy extensibility to way more people,” says Klein.

> “Too many teams are solving the same problems independently. Built on Envoy gives the community a way to share those solutions openly, so every Envoy user can move faster.”

## Wait, haven’t we been here before?

Tetrate has provided a [detailed walkthrough](https://tetr8.io/builtonenvoy) of the available extensions and their use cases. Company CTO [Varun Talwar](https://www.linkedin.com/in/varuntalwar/) says his team has seen enterprise customers deploying Envoy at scale for years, so he has seen the same challenges arise again and again.

“Too many teams are solving the same problems independently. Built on Envoy gives the community a way to share those solutions openly, so every Envoy user can move faster. We built this for the ecosystem, and we are inviting everyone to come use it and contribute back,” says Talwar.

Envoy today handles millions of machine learning predictions daily. The proxy’s security has been hardened through participation in [Google’s Vulnerability Reward Program](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/google_vrp). Today, Netflix processes billions of API requests daily, while Airbnb handles over 1 million user events per second, with both organizations relying on Envoy for mission-critical traffic management.

## Community spirit, free to use

Built on Envoy, released under the Apache 2.0 open-source license, is free to use. Tetrate has seeded the marketplace, but the long-term vision is a community-sustained ecosystem where organizations across industries share what they have built and collectively accelerate Envoy adoption.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)