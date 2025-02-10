# US Blocks Open Source ‘Help’ From These Countries
![Featued image for: US Blocks Open Source ‘Help’ From These Countries](https://cdn.thenewstack.io/media/2025/01/9bc965e3-sarah-kilian-xit3ljrvkvm-unsplash-1024x683.jpg)
When I became a programmer many moons ago, the last thing I ever thought I’d need to know about was intellectual property (IP) law. Oh well, more fool me. Now, a generation later, a new generation of developers find themselves faced with government regulations, which will complicate their lives.

In response to this development, the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) has released a comprehensive guide to help [open source developers navigate the complex landscape of the U.S. Office of Foreign Assets Control (OFAC) sanctions](https://www.linuxfoundation.org/blog/navigating-global-regulations-and-open-source-us-ofac-sanctions).

OFAC sanctions are U.S. government regulations that restrict or prohibit transactions with certain countries, entities, and individuals, known as “sanctions targets.”

These rules, aimed at achieving economic, foreign policy, and national security goals, apply to various interactions, including those in the open source community. The total [Sanctions Programs and Country](https://ofac.treasury.gov/sanctions-programs-and-country-information) list amounts to over 17 thousand entries ranging from individuals to terrorist organizations to countries.

If that rings a bell, it’s because, in October 2024, the Linux kernel developers ran right into this issue. The Linux kernel’s leadership, including [Greg Kroah-Hartman](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/), the stable Linux kernel maintainer, and [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/), [Linux](https://thenewstack.io/learning-linux-start-here/)‘s founder, announced that eleven [Russian kernel developers had been removed from their roles working on the Linux kernel](https://www.zdnet.com/article/why-remove-russian-maintainers-of-linux-kernel-heres-what-torvalds-says/).

Why? Because, as Torvalds said, of “Russian sanctions.” This, he added, in a Linux kernel mailing list (LKML) message was because [“the ‘various compliance requirements’ are not just a US thing.” ](https://lore.kernel.org/all/CAHk-=whNGNVnYHHSXUAsWds_MoZ-iEgRMQMxZZ0z-jY4uHT+Gg@mail.gmail.com/)

For developers, this means exercising caution about who they interact with and where their contributions originate. The sanctions target specific countries, regions, and individuals or organizations, many of which are listed on the [Specially Designated Nationals and Blocked Persons (SDN) List](https://ofac.treasury.gov/faqs/topic/1631).

## What This Means for Developers
The Linux Foundation’s guide highlights several crucial aspects for open source developers:

- Beyond the SDN List: Developers are advised not to rely solely on the OFAC SDN list, as it’s not exhaustive. The guide emphasizes the “50% rule,” where entities owned 50% or more by SDNs are also subject to sanctions.
- Information Exemption: Most OFAC sanctions are exempted for “informational materials,” which generally include open source code. However, this only applies to existing code and not to requests for new code or modifications. So, for example, working with a Russian developer on a code patch could land you in hot water.
- Avoiding Two-Way Engagement: While reviewing unsolicited patches from contributors in sanctioned regions is generally acceptable, actively engaging them in discussions or improvements could cross legal boundaries.
- Indirect Contributions: Developers are warned to be cautious of sanctioned entities attempting to contribute indirectly through third parties or developers acting “individually.”
The Linux Foundation’s guide aims to help you balance legal compliance and the spirit of open source collaboration. While acknowledging the disappointing reality that open source communities cannot operate independently of international sanctions, the Foundation emphasizes the importance of understanding and adhering to these regulations.

This is not, in capital letters, easy. I asked prominent open source licensing attorney [Heather Meeker](https://www.linkedin.com/in/heathermeeker) for her take. She replied, “The world is becoming increasingly protectionist, and open source is the opposite — quintessential free trade. Just look at what happened this week with DeepSeek — [the hot, new open source-based AI program](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/) — and you can tell how well protectionism works.”

But what can you do? Meeker said, “Let’s be honest: Smaller companies usually ignore regulations like this because they just don’t have the resources to analyze them, and a government usually ignores smaller companies because it doesn’t have the resources to enforce against them. Big companies that are on the radar need specialized counsel. A general business lawyer can’t keep up with the pace of new regulations, much less best practices to comply with them.”

As the open source and government regulations landscape evolves amid global political tensions, this guide is a good resource for developers navigating the complex intersection of technology, law, and international relations.

Good luck, folks. I’m glad to be just covering these regulations and not trying to navigate them.

Countries[ currently sanctioned](https://orpa.princeton.edu/export-controls/sanctioned-countries) include:

- Cuba
- Iran
- North Korea
- Russia
- Syria
- The following regions of Ukraine: Crimea, Donetsk and Luhansk regions of the Ukraine.
Additional sanctions may block specific companies from other countries as well. Check before you accept.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)