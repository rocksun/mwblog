AMSTERDAM — If your organization generates revenue from open source software, whether directly or indirectly, you should at least be aware of the coming implications of the [Cyber Resilience Act](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/) (CRA).

While the [CRA](https://thenewstack.io/open-source-development-threatened-in-europe/) goes into effect in 2027, many organizations do not realize that the timeline for preparation is measured in months. This applies both to the legislation, which continues to be hashed out — adding to the confusion — and to knowing how to prepare for when it takes effect.

Before going into an update on the CRA, what you can do now is prepare through the different available programs out there. If somebody says they can charge you to ensure compliance and you pay them for that, they are not telling the truth, because nobody knows exactly what you must do yet to be compliant with the CRA, since it has not been finalized.

## No Known Vulnerabilities

The CRA mandates “no known vulnerabilities” at the time a “product with digital elements” is “placed on the market.” What this means is that the first time the product is sold within the EU, it must have been checked and scanned to have no current vulnerabilities, [OpenSSF](https://thenewstack.io/openssf-boosts-software-supply-chain-security-with-slsa-1-0/) Chief Security Architect [Christopher Robinson](https://www.linkedin.com/in/darthcrob/) told me during the [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) here in Amsterdam.

When a product is shipped, suppliers and creators must disclose vulnerabilities that are being actively exploited, or if they have a cybersecurity incident that interrupts service or could leak exploitable vulnerabilities. The supplier — or “manufacturer” in European Commission parlance, referring to software suppliers as well — must have a process to provide security updates “in a timely manner” for traditional vulnerabilities, but no exact time frame is dictated for these “regular” vulnerabilities, Robinson said.

While the general description of the mandate might sound straightforward, it is anything but, especially considering that the mandate has yet to be finalized. While the OpenSSF is one of the parties involved in helping to shape the mandate by providing technical and other guidance, what exactly it will cover and how remains a work in progress. Robinson described its current 90 pages of text as  “90 pages of nuance.”

The idea of fixing and reporting every single vulnerability in open source code would be absurd, of course. But for a discovered vulnerability that an attacker could theoretically exploit, compliance could, in theory, still be required under the [CRA mandate](https://thenewstack.io/how-linux-kernel-deals-with-tracking-cve-security-issues/). A report must be issued, and it needs to be fixed.

Again, while the mandate has yet to be finalized, compliance may not be as onerous as many fear. Only those vulnerabilities that are known need to be fixed, prioritized based on how easily they can be exploited and how severe they are, as it stands now. “The requirements are reasonable. Industry and open source are not being asked to fix everything, and this is understood,” [Timo Perala](https://www.linkedin.com/in/timoperala/), head of software and internet standardization at Nokia Networks, told me during OSS Europe. “At the moment, it is not very granular, but the focus is on the most severe and the most damaging issues, working through the list from there.”

After describing what is at stake during his OSS talk, “Where Are We Six Months After Its Approval,” Perala told me that ambiguity still remains about the mandate’s implications, in line with what Robinson described. “It’s still not quantitative, because how do you determine where the limits are? Above this threshold, everything is immediate; below, not so urgent,” Perala said. “Below that, maybe sometimes. At that level, this understanding exists, but then engineers, of course, want quantitative measures.”

The key term stated was “monetized.” Broadly, the mandate excludes open source maintainers unless profit is involved. A very specific phrase applies: selling a support contract. Meanwhile, [upstream open source](https://thenewstack.io/open-source-development-threatened-in-europe/) is broadly excluded.

A hypothetical example illustrates the impact: an organization, manufacturer, or entity selling a product with digital elements on the European market, Robinson described. In this case, a car company. It could also be a toy, a Wi-Fi router or a switch. The product, including all components inside — hardware, firmware, and software — is considered the responsibility of the vendor. The person designing and using open source for a project, while adding specific code for a router, would also be held accountable, Robinson said.

## Free Class

To help the open source community adapt, the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) and the OpenSSF created a free class on the CRA. The course covers upstream maintainers, open source stewards and manufacturers. The class lasts 90 minutes and provides an overview of what the law entails. Additional resources are available through a [GitHub](https://thenewstack.io/github-loses-its-ceo-and-independence/) repository and other sources.

The OpenSSF serves as the security subject matter experts for the Linux Foundation. With 30 foundations under its umbrella, OpenSSF plays a central role. OpenSSF also maintains a dedicated website on the CRA, with plans to expand to cover NIST 2, the Digital Operational Resilience Act (DORA) and other compliance regimes within the European Union and internationally.

Guidance will be provided to members and other foundations once standards are available. Commercial services may emerge, but any claims of guaranteed compliance are premature, as no one currently knows the definitive requirements, Robinson said. Final approval from the European Parliament and Commission will not occur until October 2027, two months before enforcement.

“The overall impact is expected to slow European progress, but for those selling internationally, the regulations present both a challenge and a significant market opportunity,” Robinson said. “Compliance will be mandatory for access to the market.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)