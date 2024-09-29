# Does Your Open Source Project Need Foundation Oversight?
![Featued image for: Does Your Open Source Project Need Foundation Oversight?](https://cdn.thenewstack.io/media/2024/09/38d69a92-does-your-open-source-project-need-foundation-oversight-2-1024x576.jpg)
If you’re developing an open source, cloud native project it might seem a no-brainer to one day move it under the auspices of the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention). After all, look at how the likes of [Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/) or [Falco](https://thenewstack.io/falco-is-a-cncf-graduate-now-what/) — or, of course, [Kubernetes](https://thenewstack.io/kubernetes/) — dominate the scene.

Of course, those projects have been part of the CNCF for years. Success in the past doesn’t guarantee success in the future. And there are other foundations, or models, for managing an [open source project](https://thenewstack.io/20-years-in-open-source-resilience-failure-success/).

But right now, “it’s the game in town that works,” according to [Edd Wilder-James](https://www.linkedin.com/in/wilder-james/), who has managed multiple open source projects during stints at [Google](https://cloud.google.com/?utm_content=inline+mention) and [Sysdig](https://sysdig.com/?utm_content=inline+mention). This is why CNCF has housed 192 projects, supplied by 252,000 contributors since it launched nine years ago.

Before applying for the CNCF, however, any project team needs to consider two big questions. Should they move their project into the CNCF? And if they do, who should be shepherding the project along the way?

## The Benefits of Foundation Oversight
When it comes to the first question, the answer depends on what you’re looking to achieve.

The CNCF sees itself as more than a holding area for code. CNCF CTO [Chris Aniszcsyk ](https://www.linkedin.com/in/caniszczyk/)points out that it has a professional staff — unlike other foundations, which are overwhelmingly volunteer-run. This means it can provide an array of services for members, including hard tech support, such as providing security audits.

In addition, he told The New Stack, “we have folks that assist with website, technical documentation. We have developer advocates on staff that help promote the project.”

And of course, CNCF hosts events, from specific project events such as [PromCon](https://promcon.io/2024-berlin/) (dedicated to [Prometheus](https://prometheus.io/)) to the beast that is [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america). And, said Aniszcyk, it’s very focused on “commercialization activities.”

CNCF project governance and technical governance is separate from budget governance, Aniszcsyk pointed out. The governing board members decide the overall allocation of the budget toward projects and things they care about. The technical oversight committees then make requests for budget.

The aim, he said, is that “money should be pooled for the common good of security audits, technical documentation, events, etc.”

But this is just one side of the equation. Equally important, said Wilder-James, is that large organizations – the ultimate users of most CNCF projects — will find it reassuring that the CNCF is responsible for a project’s governance.

“I think the enterprise market has been educated to believe that if something is in the foundation, it’s obviously guaranteeing itself as a safer bet for adoption. A single vendor, open source project could disappear overnight.”

This has become more of an issue over the last year. A number of previously open projects — [Terraform](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) and [Redis](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/), the most high-profile — have switched to less open, or outright proprietary, licenses, frustrating other contributors and causing uncertainty for business users. And the loss of a key business backer can put a project into peril.

At the same time, said Wilder-James, moving a project into the CNCF, or indeed any foundation, can provide an “antitrust umbrella” for technology that has the potential to become ubiquitous and dominate markets. As he described it, it’s the “only way people can talk without a zillion lawyers present.”

As one other veteran tells us, moving your project under the auspices of the CNCF doesn’t guarantee it will become standard, but it does raise the possibility. And, they add, when a company moves a project into the CNCF, its maintainers and backers gain influence within the organization.

[Kapil Thangavelu](https://www.linkedin.com/in/kapilvt/), co-creator of Cloud Custodian, and CTO of Stacklet, told The New Stack that his ultimate aim when moving the project into the CNCF was to remove as much friction as possible for its community of contributors and maintainers.
“The CNCF is both lightweight on process as well as open-ended to each project having some degree of its own notion of what the governance model is … that makes sense for that project,” Thangavelu said.

## The Challenges of Foundation Oversight
For all the undoubted benefits of [joining the CNCF](https://thenewstack.io/istio-applies-to-join-cncf-why-now/), it’s not a decision to take lightly. Companies or teams need to understand the challenges that come with moving their project under the umbrella of a foundation, said WilderJames.

This includes being clear on exactly what they’re giving up in return, says Wilder-James. “You need to have that notion from the beginning that you’re going to be a valid multivendor project. There’s a lot of projects that don’t, that don’t move on.”

For these reasons, he said, “You have to choose your timing. Because it becomes an anchor at this point. Fundamentally, the mature projects in the foundation are commoditized platform technology.”

So, if it’s cutting-edge innovation you’re interested in, a multivendor foundation environment might not be the best fit — at least not for now.

After all, “You’re essentially giving up that intellectual property because the project becomes copyright CNCF,” [Loris Degioanni](https://www.linkedin.com/in/degio/), Sysdig’s founder and CTO, told The New Stack. “The trademarks become owned by the CNCF.”

That can be hard for any project team or company, arguably much more so for a security firm.

For Sysdig, working through the ramifications of moving Falco into the CNCF was “scary” Degioanni said. “I remember several intense internal conversations, even conversations with our board.”

But the hard work doesn’t stop there. Progressing through the CNCF’s sandbox and incubation processes to the coveted graduated stage means garnering community support. In effect, says Degioanni, “You are requested by the CNCF to go out and recruit other companies to embrace the project, use it. So, you are essentially sort of going out and trying to create competitors.”

And throughout, individuals and teams have to operate in the open. “If you’re used to tracking your roadmap and development, internally, maybe using Jira or Asana, then moving all that to the public could be very challenging,” Aniszczyk acknowledged. “Hosting open meetings where you’re inviting everyone in, there’s this kind of cultural change. That’s hard for a lot of folks.”

In fact, Wilder-James suggested, “Whether you’re small or large, there is zero free lunch with having a large open source project.”

And for all the engineering effort that a team puts into a project, it still faces [the challenge of creating a business](https://thenewstack.io/whats-next-for-companies-built-on-open-source/), too. “In other words, if you’re trying to do it and monetize it, you have to pay twice, right?”

And then there’s simply the challenge of collaborating with others, or contributing to committees. This can be seen as a brake on development. Just playing well with others is hard work. So, says Wilder James. “You have to have [engineers with human skill](https://thenewstack.io/why-empathy-in-open-source-matters-more-than-you-think/).”

From Thangavelu’s point of view, in addition to technical skill, “perseverance, adaptability, would be the two [qualities] that are foremost.”

Moving a project forward means interfacing with the community in a truly hands-on way, Degioanni said, including making releases, “doing support on Slack, talking to contributors on GitHub.”

Keeping your hands dirty, in other words.

“At least in Falco,” Degioanni said, “the people that have actually driven this process is the [community of core developers](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/).”

That’s a formidable set of requirements for any team.

## Making the Decision
So, is it all worth it? From Degioanni, it does depend on the project. Some projects are best kept as independent entities — such as his previous project, [Wireshark](https://thenewstack.io/wireshark-celebrates-25th-anniversary-with-a-new-foundation/), which didn’t move to nonprofit oversight (the [Wireshark Foundation](https://wiresharkfoundation.org/)) until it had been around for 25 years

But where the project should be part of a broader ecosystem — cloud native, AI — he feels differently: “In that case, yeah, absolutely, I would go with the foundation, because there are benefits, and we are seeing the benefits.”

For Thangavelu, “If I do my foundation calculus again, I’d end up in the same place for sure.”

That said, his advice to “my younger self” would be to find someone else to “have that perseverance on the process.”

But that’s because he’s not entirely comfortable with the public-facing part of the assignment. He can do “social butterfly,” he said, but “I’m happy in my coding place.” That’s surely the case for many engineers.

And ultimately, while collaboration is hard, said Wilder-James, “I personally think there’s beauty in collaboration. I think there’s so much satisfaction, and that for me personally, it’s tricky and rare to do, and that for me makes it extremely satisfying.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)