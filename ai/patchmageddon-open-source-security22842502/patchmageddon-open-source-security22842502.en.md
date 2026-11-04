**Here’s how a vulnerability in a popular open-source library plays out in 2026:** A maintainer merges a fix and publishes an advisory. Within hours, someone points a model at the diff between the old and new versions and gets a working exploit back. Your scanner flags the CVE the next morning, a ticket gets filed, and the fix is scheduled into next week’s change window. By then the exploit has been circulating for days.

That was a fine enterprise lifestyle choice last year, but it’s considered out of fashion nowadays.

And for good reason, as Michael Cembalest goes over in his “[Patchmageddon](https://am.jpmorgan.com/wr/en/asset-management/liq/insights/market-insights/eye-on-the-market/patchmageddon/)” report from July 2026, which includes input from J.P. Morgan Asset Management’s cybersecurity leadership. Models such as Anthropic’s Mythos and OpenAI’s GPT–5.5 now find previously unknown vulnerabilities at a scale no human research team can match. Anthropic and its Project Glasswing partners found more than 10,000 new high- and critical-severity zero-days in the first month alone.

At the same time, the exploitation clock shrank. The note puts the median time from disclosure to first exploitation at roughly a year in 2021. Now it’s down to *one day* in 2026, and projected to be *one minute* by 2027. Almost 80% of exploitations now land on or before their public disclosure. Models can find vulnerabilities, and hackers can exploit them just as fast, if not faster.

## **Open source takes the first hit**

That pressure lands on open source first, because open source is what modern software is made of and because the source is, well, open for all to see. This is fantastic, and as it should be: it just means it’s the low-hanging fruit for hackers.

The people expected to absorb this flood of AI-driven vulnerabilities are mostly volunteers. Of 530 high- and critical-severity findings Anthropic reported to open source maintainers by May 2026, only 75 had been patched. This past summer was filled with open source maintainers closing down bug bounty programs and putting up the gone fishing sign to de-stress.

## **Your new security strategy**

Like it or not, corporate mindsets about security tend to shift when there’s urgency and a touch of, well, worry. Here’s some more freak-out fuel:

1. More models are getting better – Cembalest’s note expects capabilities now confined to a handful of nation-state units to be reproducible in freely available open-weight models within 12 to 24 months. Hamish Low at the Institute for AI Policy and Strategy [gives a Chinese Mythos-class model a 40% chance by February 2027](https://www.the-substrate.net/p/china-will-likely-have-its-own-mythos) and near-certainty by the end of that year.
2. You’re already running vulnerable code, probably – most of what you run was pulled from public registries months ago, if not years. Datadog’s February 2026 numbers put TK{spell this out in plainer language // the median dependency 278 days behind its latest major version}. That’s old code waiting for a one-day exploit.
3. The yardstick has changed – Cembalest is blunt that organizations will have to judge themselves on patching speed, not just accuracy. Programs built around 90-day disclosure windows are now measured against a clock that runs in hours.

If you own a platform, run application security, or sign off on technology risk in a regulated industry, this problem is circling you whether you act or not. Urgency without a plan is like listening to your seatmate on a five-hour-late flight rapidly text back and forth, with that duck quack at max volume for each message they receive. Annoying and a bit of a vibe killer.

To de-quackify, let us share the plan Oren has been sharing with platform and security leaders across financial services.

### **Stop building your security strategy around free beer**

Not enough people work on open source to patch it fast enough.

Cembalest spends serious time on maintainer concentration. In a Linux Foundation and Harvard study of the top 50 open source projects, 23% had a single developer responsible for more than 80% of lines added, and 94% had fewer than ten developers writing more than 90% of the code. At registry level, Anchore counted more than 18 million npm packages listing a single maintainer.

> “Enterprises have enjoyed decades of free beer – open source software – while being told it was sort of irresponsible of them.”

Most communities that write and support open source are doing the best they can, and many have burned out doing even more. But the promise of “free as in beer” was never that they’d keep you perfectly secure and deliver day-zero patches. The promise was, well, free beer. Enterprises have enjoyed decades of free beer – open source software – while being told it was sort of irresponsible of them. Now we’re seeing proof of that, in an entirely self-inflicted way. It’s time to pay for the beer.

This is where professional open source comes in. Yes, it means – take a deep breath and close your spreadsheets – paying to use freely downloadable software.

Professional open source is backed by a vendor with skin in the game, or a foundation with staffed security response, funded maintainers, and a release process that survives burnout. The team that creates and knows the code owns the fix and works under an SLA.

> “If you can’t name who maintains a package, you can’t count on anyone to fix it.”

J.P. Morgan’s own technology leadership, summarized in Cembalest’s note, is explicit: run current versions, and move off dependencies where you can’t identify who maintains them, where the maintainer looks like a one-person shop, or where the package appears abandoned. If you can’t name who maintains a package, you can’t count on anyone to fix it.

## **Applying security patches** ***is*** **keeping the business running**

Erik Scales, who leads platform engineering for Tanzu Platform at Charles Schwab, put it bluntly in [a VMware Explore talk this year](https://www.vmware.com/explore/video/6403821830112):

If you’ve ever tried to patch a server, no one wants to patch anything. No one wants to do anything. Now, everybody’s worried about being on the news and being fired.

The usual reason for putting off a patch is that the business has to keep running. A patch might break something, so it waits for the next change window, or the one after that. The J.P. Morgan note cites research finding that over 80% of security professionals have skipped a patch to avoid disrupting the business.

> “Now that they show up within a day of disclosure, the unpatched system is the bigger threat to keeping the business running.”

When exploits took months to show up, that trade was defensible. Now that they show up within a day of disclosure, the unpatched system is the bigger threat to keeping the business running.

That still leaves the disruption problem. Any fix that adds a second disruption on top of the risk will get deferred too, and deferral is exactly what a one-day clock punishes. Attackers are counting on waiting.

## **Make the right thing the easiest thing**

Control where your open source comes from, even more tightly than you do now.

We’re long past the days when enterprise developers could download anything from the internet and use it. A lot of hard work went into changing that habit. Most large companies now send every dependency download through an internal artifact proxy, like JFrog Artifactory or Sonatype Nexus. Developers point their builds at the proxy, and the proxy fetches from Maven Central, npm, or PyPI. Going through the slog of getting developers to change their habits again is not a good idea, nor, you know, fun.

You don’t have to. To change where your open source comes from, you change where the proxy fetches from, and nothing else. Point it at a supported source like [TrueSource](https://www.broadcom.com/products/software/truesource), and the build files, URLs, and pipelines all stay the same. Developers won’t notice a difference. What’s different is that the Spring libraries coming through now include fixes that often ship before the CVE is public.

The proxy can also do some of the patching for you. Set it to block known-vulnerable versions and serve the nearest patched one instead, and builds keep working without anyone filing a ticket. The patched package becomes the default, the one developers get without asking for it.

This is critical for how you address Patchmageddon. Changing developer habits is difficult once they are set in their ways. Because you can simply point the repositories at a proxy, you don’t have to change developer habits.

Oren has worked with large financial services platform teams that already run their dependencies through a proxy like this. For them, the conversation isn’t about pushing a new supply chain platform through the organization. It’s about pointing the proxy somewhere new, and that’s easy to do.

This is why we say the only acceptable change is no change.

## **The rest of the plan**

Those are the big ones, and for some, the most difficult. There are three more items to consider as well:

1. **Measure how fast fixes reach production.** Track the time from disclosure to a deployed fix for your top 50 dependencies. That’s the number the J.P. Morgan note says you’ll be judged on.
2. **Know who maintains your critical dependencies.** For each one, write down the organization behind it. Single-maintainer and abandoned packages go on their own list.
3. **Use AI to find and propose fixes, and keep people on the merge.** Ideally, those people are the code’s maintainers.

Security is different now, in a big, new way. Pay attention to it and adapt your organization’s security strategy. This is especially true if, like most large organizations and especially financial institutions, you develop and run a lot of your own software. We’ve shared what we think is a good plan to follow. Whether you like our plan or not, make sure you *do* something. And tell us how it goes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/06/821fe331-cropped-4bdc0901-oren-penso.jpg)

Oren Penso is a seasoned IT executive and senior product strategist with more than 25 years of experience in automation, security, observability, native public clouds and platform engineering. His leadership roles span across public financial companies and VMware. Beyond his...

Read more from Oren Penso](https://thenewstack.io/author/oren-penso/)

[![](https://cdn.thenewstack.io/media/2023/01/a4afb134-cropped-2f47e82b-michael-cote-e1674132550806.png)

Michael Coté studies how large organizations get better at building software to run better and grow their business. His books "Changing Mindsets," "Monolithic Transformation" and "The Business Bottleneck" cover these topics. He’s been an industry analyst at RedMonk and 451...

Read more from Michael Coté](https://thenewstack.io/author/cote/)