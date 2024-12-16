# What Comes After Open Source? Bruce Perens Has Some Ideas
![Featued image for: What Comes After Open Source? Bruce Perens Has Some Ideas](https://cdn.thenewstack.io/media/2024/11/c1fa6192-bruce-perens-2009-2-1024x576.jpg)
Is there a better development model than open source software? One man thinks so — and ironically, it’s the same man who wrote the [original open source definition](https://web.archive.org/web/20131004221206/http://ldp.dvo.ru/LDP/LGNET/issue26/perens.html) back in 1997.

[Bruce Perens](https://www.linkedin.com/in/bruce-perens/) is now developing an alternative he calls “[Post Open](https://postopen.org/),” and it seems to be coming along. “We’ve started to build the team,” Perens told The New Stack via email. On Thursday, Perens even [posted](https://postopen.org/2024/11/14/legal-progress-new-code-of-conduct-version/) a new update at PostOpen.org: that he’s discussed with attorneys the structure of the future organization, along with its proposed Zero-Cost License. “It’s not done, but a lot closer to the legal solidity we need before people should use it.”
So is the programming world headed for a paradigm shift — one that corrects some of the [funding shortfalls](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/) in the development world of today? Could we create a stronger enforcement mechanism for the open-licensing requirements of code — while also making our [software supply chains more secure](https://thenewstack.io/2023-the-year-open-source-security-supply-chain-grew-up/)?

Perens believes it’s all possible, and he’s building that alternative in plain sight. It’s a hopeful vision for the future — but maybe it also offers us something else: an enlightening look at our current status quo, and some of the problems that we’d like to fix.

## The Road to ‘Post Open’
In February 1998, Perens [co-founded the Open Source Initiative](https://opensource.org/history) with [Eric S. Raymond](https://x.com/esrtweet). But in early 2020, Perens left that group in a dispute over its new [Cryptographic Autonomy License](https://opensource.org/license/cal-1-0), complaining [on the OSI mailing list](https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2020-January/004598.html) that they were “rather enthusiastically headed toward accepting a license that isn’t freedom-respecting.”

Perens was already concerned that the OSI had created over 100 different software licenses, urging [on the mailing list](https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2019-September/004412.html), “Let’s scrap the Tower of Babel.”

In [a comment published in 2020 on Slashdot](https://news.slashdot.org/story/20/01/05/208249/open-source-initiative-co-founder-bruce-perens-resigns-citing-move-toward-license-that-isnt-freedom-respecting#perens_coherent), Perens decried a world where “each additional license does not bring a high value in innovation or new functionality — at least in a way that supports the community rather than some company.”

So what happened next? The OSI carried on, although recently [facing fresh criticism](https://thenewstack.io/osis-definition-of-open-source-ai-raises-critical-legal-concerns-for-developers-and-businesses/) about its [newly-released definition for open source AI](https://thenewstack.io/the-open-source-ai-definition-is-out/). But “Fortunately, there’s a path for open source to grow without concerning themselves with OSI’s issues,” Perens told The New Stack this week. He reminded us that, “I’ve been working on what comes after open source for a couple of years.”

And then he referred us to [PostOpen.org](https://postopen.org/), a site making the case that the present problems of Open Source “have become obvious to everyone.”

Its first link points to [a page stressing the Software as a Service problem](https://postopen.org/how-post-open-works/) — where “a developer with the entire Fortune 500 for customers is often completely uncompensated and under severe economic pressure.” Writing later of the “almost-universal diversion of funds,” which should go to that open source developer, it warns of a need to “encourage more developers to take this path, or eventually lose them and their innovation.

“Post Open provides a way to pay for their work. We believe that Post Open can address the issues of Open Source and build a much healthier community that addresses these problems and meets goals that Open Source fails at today.”

## What Does ‘Post Open’ Mean?
A big goal was to “redirect funding to developers through dis-intermediation,” according to the site.

As Perens said in our interview, “You can think of it as ‘open source with teeth’. It keeps the freedoms of open source for individuals and smaller companies, the ones we *should* be helping … It requires that deeper-pocket entities, ones with more than [$5 million in] revenue per year, to pay a small percentage of that (it ramps up to 1% as they grow) to support the developers. And we instrument git repositories to apportion that to the developers of the software the paid users are using.”

While PostOpen.org proposes that a portion would be withheld “for taxes and operational purposes,” Perens is excited about the possibility of revenue finally reaching developers. “So, we would stop running the world’s biggest corporate welfare program, as open source does today. And developers would be able to afford to maintain their software.”

PostOpen.org points out there’s already software that can scan git (though “we may wish to develop our own”). But beyond that, “a software infrastructure for apportionment must be built, including a way for developers to register their git ID and cryptographic identification.” (“There are many services for doing this,” the site points out. With cryptographic passkey devices costing as little as $14 apiece, these could be offered to developers at no cost.)

But this brings another big bonus. By reliably identifying developers — with cryptographic-hardware-backed authentication and secure software chain-of-custody — you [dramatically improve security](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/), since “any bad actors can be traced and prosecuted.” (Not to mention the security and quality gains to be had by “providing proper funding for developers to maintain their software.”) Of course, files made available for download “will be cryptographically signed, to further support integrity of the chain-of-custody.”

And finally, the software infrastructure will provide ways for developers to designate how they’ll be paid. (The site notes that “In the case of programmers who work for an employer who pays them a salary to work on Post Open software, the payment will go to the employer.”) And with payments coming in, there are some other interesting details. The PostOpen.org site notes the possibility of paying not only developers but also “creators of documentation” — adding that “payment for other roles will be developed later.”

Meanwhile, for those deep-pocketed entities, the licensing contract would also require “a machine-readable accounting of what Post Open software the company uses, embeds in products, and performs as a service,” as well as an accounting of “the degree of use (for example, the count of products sold that contain the software)…” Compliance is simple — everyone settles up once a year. (The requirement to pay would also apply to companies “that include the software in a paid-for product,” [according to PostOpen.org](https://postopen.org/how-post-open-works/), and also to any companies “that wish to keep modifications private.”)

But to protect the privacy of data on customer software usage and annual revenue, “all compliance information and the amount of the payment from companies is under [a non-disclosure agreement],” the site reads — with payments even handled by a certified public accounting firm so “the public organization sees totals (use of a program, revenue, etc.) rather than your private data…”

And there’s one more scenario that instead rewards good behavior, according to the site: Deep-pocketed entities would continue their developer-supporting payments “*unless* they publish enough contributions to the Post Open Collection, in which case *we pay them*.”

## Compliance Support for Developers
Another big goal was to simplify the inevitable dual-licensing of projects, under both open source and Post Open licenses. “I’ve made it easy for open source projects to get on the bandwagon and start getting their developers paid without abandoning their old licenses and the users who depend on them,” Perens told TNS.

But the site also talks ambitiously about “the Post Open Collection, a body of software that is licensed to users.” It envisions an official (and “canonical”) git repository for “exclusively Post Open licensed software,” made available for free to the world’s open source developers (who today, it notes, “mostly use a for-profit git operator who uses their work to train AI”).

There would also be help for developers complying with new laws like the European Union’s Cyber Resilience Act, the site reads. Under our current system, if a developer doesn’t have the resources to comply, it gives wealthy higher-up-the-food-chain intermediaries a chance to “divert funds from the Open Source developer, because they can vend a regulation-compliant copy of the developer’s software, while the developer can not.”

So, part of the Post Open pitch would be handling all the requirements of such new laws “on behalf of all developers in the Post Open Collection.”

In our email interview, Perens stressed one of the biggest advantages of a Post Open world. Developers “won’t have to tolerate the rampant license violation we have today. We’ll put aside some of the income to go to court for them.”

The site argues that the Post Open Operating Agreement “will include authorization of the Post Open Administration to enforce on behalf of any developer of a work in the Post Open Collection.”

And as more money is collected, it hopes to address another hole in the developer world. Currently, the Linux Foundation is “one of the few Open Source organizations that can consistently afford to lobby.” But as the Open Source collective collects more revenue, it can be used to develop “representation of the developers for lobbying and other purposes.”

And in a possible swipe at the Linux Foundation, the Post Open site emphasizes that their organization’s governance “is exclusively by individual software creators, as it always should have been with Open Source.” Specifically, the plan is to operate as a nonprofit corporation owned and controlled by the software developers.

One of the stated goals of Post Open is to “apportion payment to developers based on software use by paid users and the size of their contribution to that software.” But it also states its motivation clearly: “Pay developers fairly for their work.

Hopes are already high. “Imagine a world in which Open Source developers aren’t supplicants any longer,” Perens said in our email interview. “They don’t have to *beg* companies to do their fair share. They don’t have to be exploited by big companies and the organizations those companies create.

“They can stay at home and program, and make a living from programming all day, and not have to run a company to do it … Their software will be more secure, and better able to handle all of the legal challenges that Open Source is starting to face, like the EU Cyber Resilience Act.

“We’ve started to build the team. I think we can make that happen.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)