ATLANTA — Technology companies and developers are finally realizing that they’ll need to deal with the [European Union’s (EU) Cyber Resilience Act (CRA)](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/). Fortunately, as [Greg Kroah-Hartman](https://www.linkedin.com/in/greg-kroah-hartman/?originalSubdomain=nl), maintainer of the [Linux kernel](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/) stable branch, explained at [KubeCon + CloudNativeCon North America 2025](https://docs.google.com/document/u/0/d/1aKlGA2jFJQHcvj3HBYSa4zv5J1kCSuqHKDHP4cWLkBw/edit), if you’re an individual open source developer, you don’t have much to worry about. It’s a different story, however, if your code ends up in commercial products for the EU market.

## Understanding the EU Cyber Resilience Act (CRA)

Before diving into that, though, let’s have a quick refresher on what the [CRA is](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/) anyway, since, as the Linux Foundation pointed out in a recent survey, [62% of developers and their companies are largely clueless about the CRA](https://www.linuxfoundation.org/hubfs/Research%20Reports/lfr_cra_readiness_050125a.pdf?hsLang=en). The CRA is a sweeping set of regulations designed to establish unified cybersecurity standards for products with digital elements, hardware, software, and network-connected devices, sold or used in the EU.

The Act aims to significantly enhance cybersecurity and reduce vulnerabilities, while holding manufacturers, importers, and distributors accountable for the security of digital products throughout their entire lifecycle. That means all the way from design and development to deployment and decommissioning.

## CRA Stakeholder Groups and Responsibilities

The CRA mandates products to be secure by design, regularly updated, clearly disclose software dependencies, and provide mechanisms for secure default configurations. The legislation targets issues such as inadequate cybersecurity and a lack of timely security updates, which have made digital products vulnerable and difficult for users to assess and secure.

There are three different [stakeholder groups, each with unique responsibilities and levels of regulatory obligation, under the CRA](https://www.linuxfoundation.org/hubfs/Research%20Reports/lfr_cra_readiness_050125a.pdf?hsLang=en). These are:  

* **Manufacturers**: Companies or organizations that develop, assemble, or place products with digital elements (hardware, software, or firmware) on the EU market. Manufacturers bear the primary responsibility for CRA compliance, including ensuring cybersecurity throughout the entire product lifecycle, maintaining [Software Bills of Materials (SBOMs)](https://thenewstack.io/how-to-create-a-software-bill-of-materials/), addressing vulnerabilities, and promoting supply chain transparency.​
* **Stewards**: Organizations, often non-profits or foundations (such as the Linux Foundation, Apache, Eclipse), that maintain open source software projects intended for commercial use. Stewards have lighter obligations under the CRA, mainly focusing on establishing cybersecurity policies, managing vulnerability disclosures, and promoting security best practices within their project communities.​
* **Non-commercial developers**: Individuals or teams who develop open-source software not intended for commercial use. This group is largely exempt from direct CRA requirements, although confusion and uncertainty about applicability persist among contributors, highlighting the need for more explicit guidance and role clarification.

## CRA Implementation Timeline and Guidance

Now, the CRA entered into force on December 10, 2024, but, as with any such regulation, the devil is in the details. So, the CRA’s main obligations become mandatory as of Dec. 11, 2027. The European Commission is developing delegated acts and working with a [CRA Expert Group for detailed implementation and guidance](https://www.sgs.com/en-gb/news/2025/09/safeguards-13125-update-on-developments-relating-to-the-eu-cyber-resilience-act). Kroah-Hartman, who’s on that committee, knows what’s what about the CRA, and this is what he had to say. 

## CRA’s Positive Impact on Open Source Security

He opened by reassuring developers that the CRA “isn’t a bad thing” and, in fact, represents an overdue improvement in open source transparency and security practices. That said, “The Cyber Resilience Act in the EU is something that’s going to [affect everybody](https://thenewstack.io/the-cyber-resilience-act-fear-confusion-and-reassurance/) here in this room, because even if you’re not an EU member… other countries, other places in the world are adopting the same regulations.”

In addition, anything that incorporates code, which is pretty much everything these days, and is sold in the EU, falls under the CRA. It also doesn’t matter whether you’ve never left the States; if your code is in the EU, your program falls under the NDA.

Sounds scary, doesn’t it? Don’t panic. 

## Who the CRA Targets: Commercial vs. Non-Commercial Use

Kroah-Hartman emphasized that the law is not intended to target hobbyists, consultants, or anyone simply contributing to open source. “If you’re contributing to an open source project, you do not have to worry about it, not an issue… Non-commercial hobby products, not in scope, not an issue at all. Don’t worry about it, all right, until your software gets used.” Only those whose work is incorporated into commercial products for the EU need to give special attention to compliance.

For project maintainers operating under the umbrella of organizations, such as the Linux Foundation, Mozilla, or Apache, Kroah-Hartmann outlines minimal, yet clear, responsibilities: “As a steward, this is all you have to do: Provide a contact to somebody to tell you about security issues they find, and then when you fix the security issue, report it to somebody.

That’s it. That’s all you have to do… If you are actually running some infrastructure and you do have a security issue with your infrastructure, you do have to report that as well. That’s it. Nothing big at all, and that’s all you have to do.”

## Resisting Manufacturer Compliance Offloading

Kroah-Harman urges open source projects to resist manufacturers’ attempts to offload compliance requirements onto maintainers. “If manufacturers come to you and say, here’s this big checklist of things we want you to do, push back.”

This is a real concern. Emerson Electric has already attempted to get open source projects to do its legal work for them. In August, they demanded that the [Debian Linux project](https://www.debian.org/) provide them with [information about debianutils](https://lists.debian.org/debian-devel/2025/08/msg00110.html). 

## Don’t Fear the CRA: Raising the Bar for Software Security

He warns, however, “It’s going to get worse because the CRA deadline is coming soon for companies. In open source, we don’t have to worry about anything yet.  Manufacturers are going to start really caring in September of next year. They’re going to start panicking in the summer of next year, and things are going to start hitting the fan.” 

To this kind of demand, Kroah-Hartman said, “You have no responsibility to do that. They’re trying to get you to do your work for them. It’s going to get worse. Companies are coming after you. I will create a little form letter and say, ‘Here’s what you need.'”

Kroah-Hartman explained that the [Open Source Security Foundation (OpenSSF)](https://openssf.org/) is working to [help the open source community navigate and follow the CRA.](https://openssf.org/blog/2025/07/15/new-cyber-resilience-act-cra-brief-guide-for-oss-developers/) The OpenSSF is also collaborating on technical specifications, developing guides and training, and creating frameworks, such as the OSPS Baseline, to ensure that security is improved while the collaborative nature of open source is preserved. Eventually, the OpenSSF will have a form letter that can push back to them and say, “No, do your own work. We don’t have the responsibility they do.”

Kroah-Hartman continued, “We don’t have to do anything as open source stewards or contributors for another full year. We’re not responsible for anything; that’s the only point in time we have to put our ‘read me in the file and say, here’s how you contact us.’  He also pointed out, though, that businesses in a tizzy over the OpenSSF may prove to be profitable for open source projects. [Daniel Stenberg](https://www.linkedin.com/in/danielstenberg/?originalSubdomain=se), [cURL](https://curl.se/)‘s maintainer, for example, is already offering [commercial support for cURL CRA support](https://curl.se/support.html). 

The moral of his story: “Don’t be afraid. This law is okay.” The CRA will raise the bar for commercial software security, but open source contributors and maintainers with good practices in place are already well on their way to compliance.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)