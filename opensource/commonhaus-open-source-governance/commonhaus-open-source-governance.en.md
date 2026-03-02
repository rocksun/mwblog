**In 2024, a backdoor was discovered hidden inside** [**XZ Utils**](https://www.youtube.com/watch?v=9NUOiL48hbo&t=2072s), a compression utility woven into many popular Linux distributions. This backdoor could have handed hackers full administrative control over millions of systems worldwide. It had been inserted into the utility by project lead and bad actor [Jia Tan](https://www.wired.com/story/jia-tan-xz-backdoor/).

The backdoor was spotted more or less by chance. A lone Microsoft engineer, Andres Freund, wondered why there was a strange delay in the remote connection protocol SSH on Debian.

Tan first appeared in November 2021under the GitHub username JiaT75, contributing to other open-source projects. By January 2023, their code was being integrated into XZ Utils. Over the next year, they would [gradually take over the project](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know#:~:text=to%20action%20items-,Backstory,-XZ%20Utils%2C%20and) from Lasse Collin, a solo maintainer stretched thin and feeling unsupported and alone.

Despite significant investigation by security researchers and journalists, Tan has never been definitively unmasked. Many analysts suspect a state-sponsored actor, with fingers often pointed at Russia or China. Collin had received several emails from users complaining about slow updates. It seems plausible that they were part of the same attack, putting pressure on Collin to hand over the reins.

For [Erin Schnabel](https://www.linkedin.com/in/erinschnabel/), co-founder of the [Commonhaus Foundation](https://www.commonhaus.org), it was a moment that still haunts her. Like other open source organizations, the Commonhaus focuses on governance paperwork and legal scaffolding. But it also wants to make sure the next exhausted maintainer has someone to call before it’s too late.

Commonhaus is a two-year-old nonprofit Schnabel launched with Ken Finnigan and Cesar Saavedra. They are trying to address deep-rooted problems in open-source software.

“When I’m thinking about what I want the foundation to do, it’s very much, what can I do that will benefit everyone?” Schnabel tells *The New Stack*. “But part of what I wanted to do is provide a better home for solo maintainers who otherwise don’t really have one. And I have the solo maintainers in mind because I feel like they need the most support.”

In 2024, at its launch, Schnabel [emphasized](https://thenewstack.io/commonhaus-foundation-launches-at-critical-time-for-oss/) that Commonhaus was championing a non-conventional approach, one that prioritizes succession planning, minimal governance, and financial assistance for member projects, including the ability to receive donations without seeking individual nonprofit status.

This strategy has proved popular, with the foundation almost doubling the [number of projects](https://www.commonhaus.org/#our-projects) under its auspices during 2025, from 14 to 25. Projects include Debezium, Hibernate, JReleaser, Quarkus, SDKMAN!, SlateDB, and WildFly. Quarkus competitor [Micronaut is the latest to join](https://micronaut.io/2026/01/12/micronaut-announces-plans-to-join-the-commonhaus-foundation/) and is currently going through onboarding.

## Breaking the rules of order

Commonhaus’ voting procedures are designed to give project leads an easy way to influence how the policies work. During the first year of the foundation’s existence, Schnabel researched various parliamentary voting procedures and settled on an adapted version of [Martha’s Rules](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1825&context=sociologyfacpub#:~:text=In%20their%20study%20of%20consensus,issues%20in%20large%20group%20meetings.). Not to be confused with Martha’s Rule in the UK, a patient safety initiative, Martha’s Rules were developed in the 1970s by a housing co-op in Madison, Wisconsin. It is a five-step, consensus-based alternative to Robert’s Rules of Order, designed for more efficient, collaborative meetings, focused on speeding up decisions by allowing a ‘sense’ vote to determine if a time-consuming full consensus is necessary.

> “I want the people running each project to ‘drive their own car,’ but I do require transparency. Developers hate paperwork, so I check in with them to make sure they have their decision processes written down…”

Commonhaus uses [GitHub Discussions](https://docs.github.com/en/discussions)’ thumbs-up/thumbs-down mechanism for the sense vote and opens a discussion only if there is disagreement. “It makes it easy to participate,” Schnabel says. “You don’t have to respond to a mailing list, and no one has to count the responses as it happens automatically. The participation level is good because it’s low friction.”

Maintaining the ethos doesn’t happen accidentally, as [SDKMAN!](https://sdkman.io) lead, [Marco Vermeulen](https://www.linkedin.com/in/marco-vermeulen-1645421/), tells *The New Stack*. “Erin [Schnabel] is extremely forward-thinking. She’s been in this game for a long time, and she’s been on the other side, so she understands how it works,” he says.

As the foundation grows, its unconventional ethos persists: “At other foundations, there are conventions with voting and decision-making that I have tried to break,” Schnabel tells *The New Stack* in an interview.

## Who takes care of the people who take care of open source?

By design, Commonhaus has a low-touch set of processes compared with Apache or the Cloud Native Computing Foundation, which suits more mature projects and maintainers. “I want the people running each project to ‘drive their own car,’” Schnabel tells me, “but I do require transparency. Developers hate paperwork, so I check in with them to make sure they have their decision processes written down, even if it is a blatant message that ‘I’m the benevolent dictator for life; all decisions run through me.’”

The foundation provides a functional code of conduct and steps in if disputes arise. “If you’re a benevolent dictator and someone disagrees with you, that appeal can be brought to the foundation, and we can help resolve it,” she explains.

The most common problems that require mediation are personality differences and communication issues. “In this world of neurodivergent behaviour, text communication creates the biggest challenges,” she says. For solo maintainers especially, the foundation provides invaluable support.

Schnabel is hoping to set up coaching and mentoring between project leads to help less-experienced maintainers feel more connected — a lesson learned from XZ Utils, where the aforementioned maintainer was struggling and clearly needed additional support.

The Commonhaus approach isn’t the only option. “GitHub has a great maintainers community, for example,” Schnabel says. “I think we are seeing more of this because there’s a growing awareness that maintainers feeling isolated is a huge contributor to burnout.”

There’s been less progress on other factors that contribute to burnout, although it remains a top priority for Schnabel, whose current focus is on reducing the [bus factor](https://activecollab.com/learn/glossary/bus-factor). “We encourage solo maintainers to train a replacement, store credentials in 1Password, have good documentation, and so on. Our bigger projects already do that.”

Succession planning was a major reason that [JReleaser](https://jreleaser.org) project lead [Andres Almiray](https://andresalmiray.com) chose to work with Commonhaus. JReleaser is a release automation tool that aims to simplify creating releases and publishing artifacts across multiple package managers, including Homebrew, Scoop, Chocolatey, and Snapcraft. It supports any project, regardless of the source language (Java, Go, Node, Rust, Perl, Python, C/C++, C#, Elixir, Haskell, etc.), though it provides additional benefits for Java-based projects. It was also one of the founding projects for Commonhaus.

“This is my sixth year working on the project, and I still have a lot of energy for it, but in the future I might want to do something else, and someone else will have to step up,” Almiray tells *The New Stack*. “Commonhaus helps me to nurture the next generation of developers who will eventually take over.”

> “Commonhaus helps me to nurture the next generation of developers who will eventually take over.”

Schnabel is also looking to tackle CVE support and maintenance on the older end-of-life branches of projects. “I’d like to establish a program to allow solo maintainers to focus on forward development and reduce the pressure to focus on CVEs,” she said. She encourages projects to have an explicit policy on CVEs and whether they will handle embargoed code.

“Strictly speaking, a solo maintainer doesn’t need to deal with embargoes,” she said. “If you are transparent about it, a company that feels a sense of urgency realizes that they have to contribute if they want it turned around quickly.”

## More freedom, more responsibility

Since its launch, Commonhaus has been very Java-focused. “I’d like to attract more non-Java projects,” Schnabel tells me, “but nearly all our current projects are Java and my network is very Java-oriented.”

[SlateDB](https://slatedb.io), an embedded key-value database built on object storage, is one exception; it’s written in Rust. The light-touch approach favoured by the foundation makes it a natural home for seasoned open source maintainers like its lead, [Chris Riccomini](https://www.linkedin.com/in/riccomini/). He has used open-source projects for more than 30 years and contributed to about 20 of them. His first interaction with an open-source foundation was with Apache, when he began working with Apache Hadoop in 2008. Since then, he has contributed to many Apache projects, created Apache Samza, and served as a mentor and project champion for Apache Airflow.

“I established SlateDB around the same time that Commonhaus began working with a few different startups,” Riccomini says. “It quickly became clear that we needed some structure for the project, governance-wise and security model-wise, plus other scaffolding such as a Contributor License Agreement (CLA).”

Apache would be the obvious choice, but one of the paradoxes of Apache is that it does such a good job educating developers that they eventually outgrow it.

“I treat Apache the same way as book-writing. Whenever I finish an interaction with it, I feel like, ‘I will never do that again,’ but inevitably I end up doing so,” says Riccomini. “Looking for a foundation I could use to run a lot of processes for SlateDB, I didn’t want it to be Apache as I found them to be heavy on the process side, and their infrastructure is fairly old and brittle.”

Riccomini applied to the CNCF, he told me, his experience was “not terribly positive.” He later [withdrew](https://github.com/cncf/sandbox/issues/114) SlateDB’s CNCF application and donated the project to Commonhaus.

“The CNCF had even more processes than Apache, and they were very cloud-native-centric. I wasn’t sure how to navigate that. My takeaway was that CNCF is like Apache, with better infrastructure. There’s nothing wrong with that, but it’s not what I wanted.”

For its part, Chris Aniszczyk, CTO, Cloud Native Computing Foundation, tells *The New Stack* via email that “CNCF does not mandate a single development path, but is more of a ‘[bring-your-own-governance](https://www.cncf.io/blog/2019/08/30/cncf-technical-principles-and-open-governance-success/)‘ foundation because we believe maintainers are the best judges of what their own communities need. What we do provide is a [structured maturity framework](https://contribute.cncf.io/community/governance/) — from Sandbox to Graduated — which acts as a roadmap without the friction of rigid, one-size-fits-all governance.”

> “It feels a bit like the nuts and bolts are on the floor, and we’re still putting this thing together. That doesn’t bother me, but I could see it being a challenge for some folks.”

It was Gunnar Morling, whose Debezium project joined the Commonhaus Foundation in 2024, who introduced Riccomini to Commonhaus. “It was exactly what I was looking for — lower touch, more flexible, and with more autonomy, which I really appreciated,” he said.

The autonomy requires maintainers to be self-motivated, so the onboarding process doesn’t drag on. “There’s no one pushing you, no quarterly board meeting. If you’re not on top of things, you can find yourself a year into the process and no further forward. So you need to take responsibility for navigating Erin [Schnabel]’s checklist.”

As a young foundation, Commonhaus has faced its share of growing pains. “Sometimes the process changes or there’s missing documentation, or the GitHub link doesn’t work because things got moved around. It feels a bit like the nuts and bolts are on the floor, and we’re still putting this thing together. That doesn’t bother me, but I could see it being a challenge for some folks.”

The Streamlined approach was also what drew Vermeulen to Commonhaus. “I didn’t want heavyweight governance and red tape to block me from moving ahead with what I’m doing, because it’s a fast-moving project under active development. Commonhaus has a completely different mindset; it’s about supporting the community, without getting in our way.”

## Nobody buys the maintainer a coffee

With an interest in helping projects financially, Schnabel is particularly keen to encourage small financial donations for project maintainers.

During our conversation, I was reminded that when I was chief editor at InfoQ, we adopted [AsciiDoc](https://asciidoc.org) as one of our formats for book publication. The first time we used it, the production process was fraught, and we had to work with the project maintainer to dig us out of a hole. He was very kind and generous with his time. When the book came out, I suggested to the rest of the executive team that we donate. I recollect that the response was fairly lukewarm, and I ended up making a personal donation instead.

That lack of willingness to pay for things you can get for free, whether it’s code, design work, or documentation, is something Schnabel finds deeply concerning and helps explain why Commonhaus members are individuals rather than companies.

“I’m in another community that’s interested in supporting content creators. If you create something that other people like, they will buy you a coffee or chip in seven or eight bucks. It feels good to have that support when you’re working on something. Whereas with Enterprise Java, that willingness to just chip in a few bucks is not there. I really want to change that.”

“Most of us working on open source would like to make a living out of it,” Almiray says. “Some of us have been lucky to be hired by a company that is very open to working on open source, but others haven’t. Commonhaus provides transparent financial responsibility, which means that the sponsors can send money to the foundation and see that it does not disappear; there is no black hole with this foundation.”

Commonhaus asks individuals who use its projects for small contributions; companies that rely on them can also sponsor and serve as advisors. With more funds, Schnabel would like to pay designers and tech writers. “I know some projects that would like to redo their logo. And others that would like help with their website to improve documentation, or coaching on how to organize your information to make it more accessible.”

Riccomini expressed some reservations about the foundation’s financial independence. “They are very reliant on IBM, but being able to survive independently would be really good.” There’s nothing unusual about this. At its inception, the CNCF was heavily dependent on Google, as Google not only contributed to the foundational [Kubernetes](https://thenewstack.io/kubernetes/) project but also played a major role in its governance and early financial support.

IBM/RedHat are the largest donors to Commonhaus, but the foundation also has several smaller contributors: [Gradle](https://gradle.org) (the company behind the Gradle Build Tool) is providing a dedicated instance of Develocity, the company’s observability and acceleration platform; [1Password](https://1password.com) provides password vaults and infrastructure for storing credentials; and [scarf.sh](https://about.scarf.sh) are supplying a tier of access for central metrics and analytics. Nevertheless, more financial independence would be welcome.

Riccomini has found Commonhaus a very positive experience. “I think Commonhaus is a great home for projects where the creators are a little more seasoned and know how to run an open source project, but still want support and scaffolding around trademark management, legal, and so on. It strikes a good balance for that cohort,” he says.

Whether Commonhaus can ultimately shift the culture around open source sustainability remains to be seen, but the foundation’s two-year track record suggests it has found a genuine niche. It won’t replace Apache or the CNCF for projects that need centrally imposed governance, such as rules around multi-vendor cooperation, and it probably isn’t the right home for early-stage projects that need more hand-holding.

But for the experienced maintainer who wants legal scaffolding without bureaucratic suffocation, a community without a committee for every decision, and a foundation that treats them as a professional rather than a supplicant, Commonhaus may be exactly what the ecosystem has been missing.

The harder question is whether that model can grow fast enough, and diversify beyond its Java roots, to make a meaningful dent in the burnout and abandonment quietly hollowing out the open source communities that so many depend on, and so few think to pay for.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)