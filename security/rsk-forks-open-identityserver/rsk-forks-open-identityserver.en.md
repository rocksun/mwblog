[Developers weren’t happy](https://www.reddit.com/r/dotnet/comments/1isquvd/identityserver4_wiped_from_github_by_duende_team/) when identity and access control software company [Duende](https://duendesoftware.com/) commercialized its open source IdentityServer product in December 2022, while also initially deleting its supporting documentation from GitHub.

[Rock Solid Knowledge](https://www.identityserver.com/) (RSK), a software development company based in Bristol, UK, is a longstanding contributor to the IdentityServer community and is now dedicated to ensuring that open authentication infrastructure platform services continue to live on.

RSK decided to fork the project and maintain an open source identity security offering with the same (but now expanded) set of [authentication technologies](https://thenewstack.io/how-do-authentication-and-authorization-differ/) as the original project; the new [Open.IdentityServer](https://www.identityserver.com/products/openidentityserver) platform was released on Tuesday.

## Open source means adoption first, not monetization first

RSK’s founder, [Andrew Clymer](https://www.linkedin.com/in/andy-clymer/), tells The New Stack that “free software doesn’t have to mean abandoned software” and that IdentityServer4 left behind a huge community that still deserves a future.

“Open.IdentityServer gives those abandoned developers a modern, supported path without forcing a commercial decision on day one. [Open source succeeds](https://thenewstack.io/the-future-of-open-source-or-why-open-core-is-dead/) when adoption comes before monetization,” Clymer says. “Open.IdentityServer demonstrates you can have a professionally maintained platform that’s free forever while still building a sustainable business around commercial extensions and services. We think that’s a healthier model for everyone.”

A manifesto by RSK published this month states that Open.IdentityServer will remain free and open source. It said that commercial offerings will remain optional and will “finance the free core,” but that the open source community will “always have a voice” in the direction of the project.

> “Free software doesn’t have to mean abandoned software. Open.IdentityServer gives abandoned developers a modern, supported path without forcing a commercial decision on day one. Open source succeeds when adoption comes before monetization.” —Andrew Clymer, Rock Solid Knowledge.

Based on the Apache 2.0-licensed IdentityServer4 codebase, the platform provides an OpenID Connect and OAuth 2.0 framework for .NET applications, supporting token-based authentication, single sign-on, and API access control. The first release, Open.IdentityServer v1.0.0, was published on June 1.

## Why was IdentityServer4 decommissioned?

The [DuendeArchive page](https://github.com/DuendeArchive/IdentityServer4) on GitHub has stated that IdentityServer4 contains “multiple known security vulnerabilities and bugs” and has outdated documentation.

Head of customer success at Duende Software, [Maarten Balliauw](https://www.linkedin.com/in/maartenballiauw/), [blogged](https://duendesoftware.com/blog/20250306-identityserver4-public-again) on his company’s own pages to confirm that IdentityServer4 went out of support when .NET Core 3.1 reached its end-of-support date, as previously stated back in December 2022.

“IdentityServer4 contains several known security vulnerabilities and bugs, while at the same time providing outdated documentation and information,” writes Balliauw in a post published in March of last year.

According to Balliauw, the repository displayed a warning about these issues for many years alongside similar flags related to its NuGet packages (zip files containing compiled code and libraries used to share and reuse code in .NET applications). However, Duende saw that the “source code was still being cloned”, so the packages were being used by developers and put into production.

A [Duende IdentityServer Community Edition](https://duendesoftware.com/products/communityedition) with the same features as the Enterprise Edition remains available for use by individuals, not-for-profit companies with less than 1M USD projected annual gross revenue, and non-profits with less than 1M USD annual budget.

As admirable as this appears, RSK’s Clymer isn’t won over.

“This approach only works for a small number of organizations and early startups,” he says. “When your startup business starts to take off, you don’t want to get hit with a bill or face an expensive migration to another platform. Businesses need certainty, no large annual price rises. Open.IdentityServer provides this ‘for free, forever’, and that’s a pledge we’ve [made in our manifesto](https://www.identityserver.com/products/openidentityserver/manifesto); this is not a short-term initiative, we are here to invest in the platform, protect it and grow it.”

> “A fork is only viable if a team of developers is prepared to own it for the long term… and we are.”

## Going back to open source roots

RSK is buoyant about open source purity; the company says the launch of Open.IdentityServer brings the kernel of IdentityServer closer to its original open source roots. The open-source model provides organizations with a free, production-ready core that can be supplemented with optional commercial products, services, and enterprise support.

Should we take this [forking of a decommissioned](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/) [open-source project](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/) as an exemplar beacon to guide other scenarios of this kind, if and when they occur? Is this method now a viable long-term strategy for sustaining critical developer infrastructure in the face of proprietary lock-in?

“Absolutely, that’s what it is,” confirms Clymer. “A fork is only viable if a team of developers is prepared to own it for the long term… and we are. Open.IdentityServer isn’t a side project; it’s the foundation of our business, which gives us every incentive to keep it secure, modern, and actively maintained.”

## Migration frustrations, or foundation affirmation celebrations?

But Open.IdentityServer is bright, shiny, and new, so the team is naturally bullish about ease of use and platform purity. Teams currently locked into Duende’s commercial core license or still running unsupported IdentityServer4 might think it’s not a straightforward task to migrate their existing IdentityServer deployments to Open.IdentityServer primarily because there’s not usually such a thing as a free lunch.

“We’ve catered for that consideration, fully and comprehensively,” assures Clymer. “It’s super straightforward, and our team has produced explainer videos that show how it can be done in less than 10 minutes when software engineers migrate from Duende. Open.IdentityServer schema is compatible with Duende, so there are no database migrations; just change the NuGet packages, and you are pretty much done.”

Clymer asserts that these mechanics make it “very easy to evaluate” whether this platform is right for any given deployment. For new builds, there’s a template that gets developers up and running in less than 30 minutes, with a UI for managing configuration.

In terms of open-source model pedigree, RSK is also a longstanding contributor to ecosystems such as IdentityServer, [OpenIddict](https://openiddict.com/), and the [Umbraco](https://umbraco.com/flexible-cms/?gad_source=1&gad_campaignid=23799046955&gbraid=0AAAAADL94wSz4HntPz3WxgyLybTIgmmoP&gclid=Cj0KCQjwr4jSBhCSARIsAOX1E-J8ngbjabJcwfWyA6yrqPwe_rUxwT7b6OEZHhlSa8AE_BduxcvIc48aAmDKEALw_wcB) CMS.

Open.IdentityServer is [available on GitHub](https://github.com/RockSolidKnowledge/Open.IdentityServer), where Rock Solid Knowledge maintains the public repository and documentation and welcomes contributions from the wider community.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)