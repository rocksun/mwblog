Open source has long been shaped by the tension between community ideals and commercial reality. This past week highlighted just how distinct those two forces remain.

On one side, activists and open-source advocates [published an open letter](https://keepandroidopen.org/open-letter/) on February 24 opposing Google’s plans to require all Android app developers to register directly with the company to distribute apps outside the Google Play Store. The signatories argue the requirement effectively centralizes control over who can publish software on the platform — even beyond Google’s own app marketplace.

“We urge Google to withdraw this policy and work with the open-source and security communities on less restrictive alternatives,” the signatories write.

On the other side, Meta formalized its plan to move React into a [dedicated foundation under the Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-react-foundation), shifting legal stewardship away from a single corporate owner — though much of the administrative transfer remains in progress.

At the center of both developments is the matter of control: who has it, how it’s structured, and what happens when a vendor-led open source project becomes foundational to how modern software is built and distributed.

## The rise of React

![React Foundation logo](https://cdn.thenewstack.io/media/2026/03/9fc5938c-reactfoundation-300x169.webp)

React Foundation logo

Developed internally at first for its own products, Meta (then Facebook) [open-sourced React](https://engineering.fb.com/2013/12/20/web/2013-a-year-of-open-source-at-facebook/) in 2013, quickly becoming one of the dominant tools for creating modern web apps. Over the past decade, React has become a foundational layer of the frontend ecosystem, with millions of developers and countless companies relying on it.

But its vendor-led governance has long prompted questions about whether a project of this scale should remain under the stewardship of a single company. And so in October 2025, [Meta announced plans](https://thenewstack.io/new-react-foundation-to-manage-framework/) to spin out React, [React Native](https://reactnative.dev/), and related technologies into the all-new [Reaction Foundation](https://react.foundation/), under the auspices of the Linux Foundation. Long-time React lead [Seth Webster](https://www.linkedin.com/in/swebster) was appointed as executive director.

Speaking to *The New Stack* at the time, [Webster said](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework/) React had “become an indispensable part of the way that the web is built and runs … It’s become more important than a single team should be responsible for maintaining.”

However, he also acknowledged that parts of the community have felt sidelined at times — a nod to past flashpoints such as the [2017 licensing controversy](https://www.theregister.com/2017/08/21/facebook_apache_openbsd_plus_license_dispute/), when React’s BSD + Patents license and its patent termination clause drew sustained criticism. The Apache Software Foundation, for example, [barred React](https://www.theregister.com/2017/07/17/apache_says_no_to_facebook_code_libraries/) from use in Apache projects before Meta [ultimately relicensed](https://engineering.fb.com/2017/09/22/web/relicensing-react-jest-flow-and-immutable-js/) the project under MIT.

Webster also pointed to the more general push-and-pull that comes with a project of React’s scale, where major architectural shifts and governance questions can leave some developers feeling unheard.

“There’s been a lot that we’ve done that’s alienated parts of the community and caused people to work on competing frameworks and so forth,” [he told *The New Stack*](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework) in October of last year. “That’s a huge part of what makes innovation so successful, having that pressure, so I’m really happy to see that. But, I also want to do everything we can to make sure that everybody feels as welcome and heard and a part of the React community as they should.”

## So what actually changes?

The React Foundation comprises a range of corporate power players. Alongside Meta, initial members include Amazon, Microsoft, Huawei, Vercel, Expo, Callstack, and Software Mansion — a mix of cloud providers, framework vendors, and React ecosystem specialists.

But neutrality, at least in the early phase, comes with notable caveats. Webster remains a Meta employee while serving in his new role at the React Foundation. That arrangement isn’t unusual in open source foundations, but it underscores that the institutional center of gravity has not abruptly shifted away from Meta.

As per *The New Stack*’s report from last year, Meta will also retain a supermajority on the foundation’s corporate governance committee for the first two-and-a-half years, meaning it will retain significant influence during the foundation’s formative stage.

> Neutrality, at least in the early phase, comes with notable caveats.

[Deb Bryant](https://www.linkedin.com/in/opengovernment/), interim executive director at the [Open Source Initiative](https://opensource.org/) (OSI) and former [Eclipse Foundation](https://www.eclipse.org/) board member, says foundation transitions rarely result in immediate technical upheaval.

In Bryant’s experience, projects that move to neutral governance structures tend to carry forward their existing roadmaps and core contributors, particularly when they have already reached significant scale and adoption.

“What usually stays in place is the near-term technology roadmap and participation by key technical contributors vital to the project’s success,” Bryant tells *The New Stack*. “A certain level of critical mass and interest in the project in its current status gives the single vendor confidence that prior bets placed will continue to grow; potential midterm changes in direction are usually understood as part of the ultimate decision to move the project to a neutral governance structure.”

For developers, the shift can mean a clearer division of responsibility. Business oversight moves to the board; technical direction stays with those writing and reviewing the code.

“Developers involved in projects that move to a neutral foundation … benefit from the separation of business … and technology in its governance,” Bryant says. “Business leadership and investment in non-technical concerns – legal, funding, marketing, community events, and so forth – are addressed, while developers are able to focus on collectively driving the technology roadmap and releasing code.”

Put simply, governance handles the overhead; engineers handle the engineering. Bryant also notes that foundation-backed projects often attract a broader contributor base over time and re-energize it.

“Rapid growth of the technical community has its challenges, but the infusion of new members offers new camaraderie, professional growth, and mentorship opportunities,” Bryant says. “This makes for a healthier, more sustained community with greater bench strength, which bodes well for the future of a project.”

## A strong foundation

The truth of the matter is, for many developers, project governance may not even register on their radar — until something goes wrong, that is. In open source, new foundations often emerge after tensions have already boiled over. [JP Caparas](https://jpcaparas.com/), software engineer and author of the [*Sulat* newsletter](https://sulat.com/), argues that React’s transition stands out precisely because it did not follow that pattern.

“React hasn’t had a governance crisis,” Caparas [writes](https://sulat.com/p/react-just-left-meta). “Nobody forked React over frustration with Meta’s stewardship. This move is preventive, not reactive, which is arguably the smarter play. Better to build the bridge before you need it.”

> For many developers, project governance may not even register on their radar — until something goes wrong.

Kubernetes is often cited as one of the major success stories in the foundation’s history. Originally created at Google, it was [donated early](https://www.cncf.io/blog/2018/03/06/kubernetes-first-cncf-project-graduate/) to the Cloud Native Computing Foundation, where it developed a broad, multi-vendor contributor base. Caparas argues that rival companies such as Microsoft and Amazon were far more willing to commit engineering resources once the project was no longer seen as belonging to a single competitor — a shift that helped accelerate Kubernetes’ growth and legitimacy across the industry.

“Neutrality opened the door to adoption that corporate ownership never could – that’s the single biggest lesson from Kubernetes,” Caparas says.

Node.js’s journey to a neutral foundation was less smooth. In late 2014, frustration with the project’s governance under Joyent prompted developers to [fork Node.js into a rival project](https://www.infoq.com/news/2014/12/iojs/) called io.js, forcing a reckoning that eventually [led to the creation](https://nodejs.org/en/blog/announcements/foundation-v4-announce) of the Node.js Foundation.

These examples show that foundation status can play different roles depending on timing. In Kubernetes’ case, neutrality helped unlock growth and rival investment early. In Node.js’s case, it arrived as a mechanism for repair after fracture.

> React hasn’t experienced a real governance crisis, nor has it faced a fork that forced Meta’s hand. But it is also no longer an emerging project seeking legitimacy.

React sits somewhere between those precedents. It hasn’t experienced a real governance crisis, nor has it faced a fork that forced Meta’s hand. But it is also no longer an emerging project seeking legitimacy — it is already entrenched across the industry. For Caparas, however, what ultimately determines whether a foundation delivers meaningful independence is those who are actually contributing.

“The pattern that separates success from failure is pretty specific,” Caparas [argues](https://www.linkedin.com/in/jpcaparas/recent-activity/all/). “It’s not who sits on the board, it’s who employs the core maintainers.”

In React’s case, Meta still employs most of the core team, and the foundation’s executive director comes directly from Meta’s React organization. Kubernetes, Caparas notes, took several years to genuinely diversify contributor employment after joining the CNCF.

“React should plan for the same timeline, and the community should be watching for it,” Caparas says.

And so the practical impact of the transition will depend on whether React’s contributor base diversifies beyond Meta in the years ahead.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)