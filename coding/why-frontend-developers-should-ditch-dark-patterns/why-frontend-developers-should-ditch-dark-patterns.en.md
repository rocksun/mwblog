In September, [Amazon settled a lawsuit](https://www.wired.com/story/amazon-ftc-settlement-prime-dark-patterns/) filed by the Federal Trade Commission (FTC) that accused the e-commerce platform of using dark patterns in ways that were manipulative and deceptive in getting users to sign up for Prime. It cost them $2.5 billion in payouts to customers and the FTC.

Dark or deceptive patterns are [UX designs](https://roadmap.sh/ux-design) that trick or manipulate users into performing a forced action, according to [Selam Moges](https://www.linkedin.com/in/selamawit-moges/), a software engineer with Apella, which creates technology for surgeons. She spoke on “Deconstructing Dark Patterns: Ethical Design Principles for React Developers” at last month’s [International JavaScript Conference](https://javascript-conference.com/new-york/), held by Devmio.

“Granted, most developers aren’t waking up in the morning and deciding to trick users, but when we prioritize growth at all costs without questioning the design, we risk embedding manipulation into the product by default,” Moges said.

While it may seem like a design issue, web and application developers should be aware of dark patterns and raise concerns if they notice the pattern, Moges contended. Developers are the ones who have to fix the code when the pattern becomes problematic for users or regulators — or, as in the recent case of Amazon, both.

The Amazon lawsuit is a prime example. If Amazon had won, the lawsuit still would have affected its reputation and brand, potentially costing Amazon customers, Moges said. Losing, obviously, would have meant a hefty payout. And at $2.5 billion, settling certainly wasn’t cheap.

“It’s in the company’s best interest to avoid deceptive design that can land them into these tricky situations like this,” Moges added.

## Defining Dark Patterns

The term “dark patterns” was first used in 2010 by [Harry Brignull](https://www.linkedin.com/in/harrybrignull/?originalSubdomain=uk), an independent UX designer, advocate and author of [Deceptive Patterns](https://www.deceptive.design/book/contents/get-started). The Deceptive Patterns website identifies a number of these [problematic patterns](https://www.deceptive.design/types), including:

**Hidden Costs**, in which the user is enticed with a low advertised price but discovers unexpected fees and charges at checkout. For example, a trip site might automatically add on an insurance fee without the user selecting it.

**Visual Interference**, in which the user expects to see information presented in a clear and predictable way on the page, but it is hidden, obscured or disguised. For example, a “no” button is red and the “yes” is green, which subtly discourages people from choosing no.

**Hidden Subscription**, in which the user is unknowingly enrolled in a recurring subscription or payment plan without clear disclosure or their explicit consent. A similar pattern Moges identified is a **Subscription Trap,** which makes it easy to subscribe but requires multiple steps to unsubscribe.

Apple’s unsubscribe is perhaps an example — it’s easy to opt in, but opting out requires users to navigate a number of not-so-intuitive steps, such as going to the settings tab on their device, then to their Apple account, then into subscriptions, where users can (finally) find the unsubscribe button.

Such tactics aren’t new, of course. Moges noted that even before the internet, marketing practices could be unethical.

“Historical content starts before the internet, so before 1983 pre-internet sales tactics — so, long before the web — manipulative techniques were used in retail and advertising, things like bait and switch tactics, fine print in contracts and infomercials exploiting urgency,” she said.

But what changed is that in the mid-2000s, the A/B testing boom started. A conversion-obsessed culture led to UX being weaponized, she said. Growth measurements became time on site, retention and upsell at all costs, she said.

## Two Tales of Dark Patterns

Retrofitting inclusivity can also be costly when compared to embedding it in the product development pipeline itself, Moges said.

She pointed to the [Facebook/Cambridge Analytica](https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election) scandal, in which [Facebook](https://thenewstack.io/a-reason-to-not-hate-facebook-open-source-contributions/) allowed third-party apps to access user data, affecting around 87 million users, and their data was misused for political ads.

“Some users weren’t actually even aware that this was going on and it was only after news reports actually wrote about this, [it] unearthed this scandal,” she said.

Facebook had to retrofit privacy controls, overhaul [APIs](https://thenewstack.io/its-time-to-build-apis-for-ai-not-just-for-developers/) and change their consent model.

“This is all a lot of work that they had to do, but even from the financial side, there was a $5 billion fine from the FTC,” she said.

The brand took a massive hit to its reputation and user trust as well, she said.

“Ultimately, this sparked global scrutiny and regulation, the [GDPR (General Data Protection Regulation)](https://www.hrpo.pitt.edu/european-union-eu-general-data-protection-regulation-gdpr#:~:text=The%20General%20Data%20Protection%20Regulation,of%20individuals%20in%20the%20EEA.), enforcement, Congressional hearings and things like that,” she said.

Compare that to how Apple handled a dark pattern with [Apple’s App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency) framework.

“The core problem that Apple’s ATT was trying to address is that apps could track user behavior across other apps and websites without explicit permission, and most users didn’t know that this was happening, and trust in mobile apps began to erode,” she said.

In 2021, Apple made an ethical design decision to introduce ATT. Now there’s a pop-up when an app is first downloaded that explicitly asks the user and prompts them in a clear, non-coercive and respectful way, she added.

Apple’s actions boosted user trust, she said.

“The first is [a] user trust boost. Apple positioned itself as privacy-forward, gaining user trust — and even after ad companies were pushing back on it,” she said. “Secondly, adoption and retention — consumers increasingly saw Apple as a safe ecosystem.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)