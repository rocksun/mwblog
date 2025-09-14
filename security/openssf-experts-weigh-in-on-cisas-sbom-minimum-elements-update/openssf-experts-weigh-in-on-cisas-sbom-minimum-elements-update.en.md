It’s been high time for an update to the government guidance on minimum elements for software bills of materials (SBOMs), according to [Josh Bressers](https://www.linkedin.com/in/joshbressers/), vice president of security at software supply chain security company [Anchore](https://anchore.com/).

The recently released [draft revision](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf), an update from the original 2021 version, is open for public comment until Oct. 3.

“We’re all very excited that they’re updating this document, just because, like, 2021 in this universe is 100 years ago in any other universe,” said Bressers, a member of the Open Source Security Foundation (OpenSFF) technical advisory council and co-lead of the [OpenSSF SBOM Everywhere](https://openssf.org/blog/2022/09/13/funding-python-spdx-development-with-the-openssf-and-sbom-everywhere/) project.

[![Michael Lieberman](https://cdn.thenewstack.io/media/2025/09/fb4c3898-lieberman-150x150.png)](https://cdn.thenewstack.io/media/2025/09/fb4c3898-lieberman-150x150.png)

Michael Lieberman

[![Josh Bressers](https://cdn.thenewstack.io/media/2025/09/1e4dbe4b-bressers-150x150.png)](https://cdn.thenewstack.io/media/2025/09/1e4dbe4b-bressers-150x150.png)

Josh Bressers

In interviews, he and [Michael Lieberman](https://www.linkedin.com/in/michael-lieberman-65786ba/), co-founder and CTO of supply chain security vendor [Kusari](https://www.kusari.dev/), pointed out the need for more clarity and granularity in SBOMs. Lieberman is also a member of the OpenSFF technical advisory council, as well as an [OpenSSF SLSA](https://openssf.org/projects/slsa/) steering committee member.

Lieberman says there’s long been a need to drill further down into exactly what a piece of software is made of, pointing to the [Takata airbag recall](https://www.nhtsa.gov/vehicle-safety/takata-recall-spotlight#:~:text=Overview,involves%20non%2Dazide%20driver%20inflators.) in the automotive industry.

“Every car that leaves a factory, they know exactly what went into that car,” he said. “They know exactly which batch of screws and every single bolt so that, if it turns out, ‘Hey, there was a bad batch of bolts … for these cars that were manufactured between these dates.’ Great, they know, they can recall all that.

“But that’s not the same case [with] stuff like medical devices, which is obviously scary, where somebody might say, ‘Do you have that vulnerable software in that pacemaker that, technically, somebody could do something and hack a pacemaker?’ It’s like, ‘Oh, I don’t know.’”

## **Getting Into the Weeds**

In 2021, the [Executive Order on Improving the Nation’s Cybersecurity](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) mandated the use of SBOMs for all software consumed and produced by government agencies. The use of SBOMs, a definitive list of all software components, libraries and dependencies that make up a piece of software, was originally required for just federal agencies, but has been pushed to software vendors as well. And more recently, it’s being advocated as a way to better secure any organization’s operations.

The National Telecommunications and Information Administration (NTIA), part of the Department of Commerce, originally laid out the [minimum elements to be included in SBOMs](https://thenewstack.io/creating-a-minimum-elements-sbom-document-in-5-minutes/). That work has since moved to the Cybersecurity and Infrastructure Security Agency (CISA) at the Department of Homeland Security.

This draft revision brings in four new data fields: component hash, its unique identifier; license, the license(s) under which the software component is made available; tool name, the name of the tool the SBOM author used to create it; and generation context, data about when exactly the SBOM was generated.

It provides major updates to five data fields: SBOM author, software producer, component version, software identifiers and dependency relationship.

Including the component hash is probably the most important addition, according to Lieberman. It’s a way to distinguish between seemingly identical versions that may have been built differently.

“In a lot of software today, your package foo version 1 could be different than my package foo version 1, depending on where did we get it from? Is it from, let’s say it’s part of Linux distribution. Did you get it from [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), or did you get it from Debian? Those things could actually end up leading you to get something that is like, yes, it’s technically 1.0 of this package, but it’s been built differently for the ecosystem that you’re kind of pulling it from, and that has often led to sort of a lot of confusion,” he said.

“If we go back to the [XZ situation](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) … that was a situation that mostly impacted certain Linux distributions, but not others. … You wouldn’t be able to know that, unless you could compare the hashes and check to say, ‘Did I actually pull in that specific built version of a thing?’”

He added, “When somebody says, ‘I have a particular version of OpenSSL or log4J,’ it can mean lots of different things. It can mean I downloaded a JAR file, if it’s Java, or I downloaded a Debian package or a Red Hat package or a container image, and all of those things are slightly different.

“If you buy it from one vendor, or pull it from one open source location, or pull it from a different open source location, they could have different hashes because they were built in slightly different ways. So you need to know exactly which one you have, by the hash, to remediate an issue — or to know you don’t have an issue.”

The addition of generation context, whether pre-build, during build or post-build, is also important. Those generated during the build tend to be the most complete, he said.

“The SBOMs you get that are part of your build process are the best, because dependency resolution happens during the build. So when you’re downloading those packages, you could literally capture the hash, the component hash. You can capture exactly what version you pulled in and all this other stuff. Because again, depending on what language you’re using, depending on what ecosystem you’re part of, saying that I’m downloading 1.0 of a thing, well, does it mean 1.0 with these patches? 1.0 without those patches? How do we really know?” he said.

Pulling in the hash while you’re pulling in the packages means you have an exact record of it, and if you later find it’s a bad hash, you can deal with that.

Knowing the tool used to produce the SBOM is also important because sometimes one tool is better than another for a specific use case, he said.

## **Regulation Is Fueling Adoption**

Snyk’s 2024 “[State of Open Source Report](https://view.snyk.io/the-state-of-open-source-report-2024/p/1)” found that 62.4% of organizations were implementing SBOM monitoring, while [Anchore’s 2024 survey](https://anchore.com/press/anchore-survey-shows-only-1-in-5-organizations-have-full-visibility-into-their-open-source-software-components) revealed that 78% planned to increase the use of SBOMs within 18 months.

Yet back at the beginning of 2025, [Dan Lorenc](https://www.linkedin.com/in/danlorenc/), co-founder and CEO of software supply chain security company [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention), predicted that [SBOMs would be duds](https://thenewstack.io/rust-will-explode-sboms-will-be-duds-open-source-predictions/) without a bigger regulatory push. A [Sonotype white paper](https://www.sonatype.com/resources/whitepapers/2023-sbom-survey-report) maintains that the 2021 executive order is among the drivers for 92% of large enterprises to have either already implemented or plan to adopt SBOMs, and that 60% require partners to.

According to Bressers, the real impetus fueling SBOM adoption is the EU’s [Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) (CRA). Open source developers will not directly be [subject to CRA](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/) unless they are actively making money from their software, TNS’s [Joab Jackson](https://thenewstack.io/author/joab/) recently pointed out. However, vendors using open source components will.

“I gave a talk about this a couple of months ago at a conference, and a bunch of the audience were like, ‘Oh, but we don’t sell into Europe.’ I’m like, ‘You don’t sell into Europe, but your customers sell into Europe. And guess what? They’re going to come ask you for [SBOMs].’ And so the CRA, the [Cyber Resiliency Act](https://thenewstack.io/lf-europe-chief-warns-developers-on-eus-cyber-resilience-act/), is basically saying, if you are selling into the European market, you’re selling software, you need SBOMs,” Bressers said.

## What OpenSSF Is Doing

The OpenSSF released a [mobilization](https://openssf.org/oss-security-mobilization-plan/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) plan in 2022 that included an initiative called “SBOM Everywhere: Improve SBOM Tooling and Training to Drive Adoption.” It has just begun discussion of how it will comment on the proposed new CISA minimum elements draft, Bressers said.

“So the work we’re doing at the OpenSSF right now, it’s super early, right? … For the most part, the new minimum elements [document] from CISA is pretty good. I think from the OpenSSF perspective, it’s going to be just a lot of making sure we clearly define terms and making sure that some of the maybe weird open source edge cases are accommodated for,” he said.

“I’ll give you kind of two examples. So there are two sections in the system RFC [request for comment] where they want to know SBOM author. That one feels like it makes sense. But software producer, what’s a producer, right? We don’t know. We need to work on the language to make sure we clearly define what that means in the context of generating SBOMs.”

Version presents other challenges.

“Version is, unfortunately, not as simple as it should be in open source because, let’s say you have a package, some open source project, and it might be version 1.6 now. When you put it into something like a Linux distribution, they have this thing called an [epoch](https://antfu.me/posts/epoch-semver) where it could add a one to the beginning. The purpose of the epoch is to say, like, this version is greater than any version without an epoch. And it sounds kind of complicated. … Versions can decrease. That sounds insane to say, but when it does, it’s a way for the Debian, the Linux distributions like Debian and Red Hat and Ubuntu, to kind of say, ‘Force this version greater than the last version, no matter what it says.’ And like, what about epochs? How do we deal with that stuff?” Bressers said.

“There are things in the NTIA minimum elements that, yes, we adhere to, but actually don’t really make sense anymore in this day and age, because … the way a bunch of this stuff was defined, it just didn’t make sense where they wanted pointers back to the originator of software. In the open source world, what does that even mean? You know, are we talking about Debian? Are we talking about the project it comes from? Are we talking about the guy who wrote it? Like, who knows?”

And while the document does go into AI to some extent, Bressers said he doesn’t think it will go very deep into it.

“And I think that’s OK, because the whole AI BOMs or SBOMs for AI or every which way you want to arrange the words, I think as an industry, we’re still figuring a lot of this out, and so that’s good, right? And I also don’t want to see government guidance, necessarily, for something this very new.”

At the same time, multiple countries, including India, Japan, Germany and others, are working on similar guidance. The challenge will be in aligning the various requirements.

“I feel like we’re reaching a point for a technology like SBOMs where we have to build these communities between industry and government and open source because I don’t think we’ve ever seen, I guess, the sort of problem space like this, right? Where it affects such a huge breadth of software. It’s literally all the software. And so I’m excited and terrified for what kind of comes next,” Bressers said. “And so, this is one of the reasons I want to make sure we have groups like the OpenSSF that are going to do their best to help keep everyone aligned, and we understand what’s going on.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/01/cabe83e0-susan-mug.jpg)

Susan Hall is the Sponsor Editor for The New Stack. Her job is to help sponsors attain the widest readership possible for their contributed content. She has written for The New Stack since its early days, as well as sites...

Read more from Susan Hall](https://thenewstack.io/author/susanhall/)