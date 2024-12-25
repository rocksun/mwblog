# Kubernetes, Rust, Linux and DOS? The Year in Open Source
![Featued image for: Kubernetes, Rust, Linux and DOS? The Year in Open Source](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)
The open source movement is vast, encompassing projects begun half a lifetime ago, and those launched (or relaunched) just months ago. So as fast away the old year passes, let’s pay a visit to some of 2024’s trendiest open source projects — checking in on their health and prosperity, and wishing them luck in the coming new year.

There were the obvious big stories. [“Elasticsearch Is Open Source. Again!”](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/) [Elastic](https://www.elastic.co/) [announced in August](https://www.elastic.co/blog/elasticsearch-is-open-source-again) after adding an [Open Source Initiative](https://opensource.org/)-approved license to counter criticism that its [2021 licensing restrictions](https://thenewstack.io/this-week-in-programming-the-elasticsearch-saga-continues/) made their product “[fauxpen” source](https://opensource.org/blog/the-sspl-is-not-an-open-source-license).

And when [Redis](https://redis.com/?utm_content=inline+mention) [changed licensing](https://github.com/redis/redis/blob/0b34396924eca4edc524469886dc5be6c77ec4ed/LICENSE.txt) for its NoSQL database, it suddenly faced a fork called Valkey [backed by well-funded heavy-hitters](https://thenewstack.io/valkey-is-a-different-kind-of-fork/) like [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) and [Oracle](https://developer.oracle.com/?utm_content=inline+mention).

But the open source movement is as far-reaching as the [Free Software Foundation](https://www.fsf.org/) itself, and as vast as a [Kubernetes](https://roadmap.sh/kubernetes) cluster. So what were the [open source](https://thenewstack.io/open-source/) movement’s other high points — for projects big and small — and the overlooked milestones in 2024?

## Kubernetes, Linux and Rust
As the year rolled along, 2024 found Kubernetes reaching its 10th anniversary with a special [three-hour celebration in June](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/) at Google’s Mountain View, Calif., campus. Looking back, Kubernetes co-creator [Craig McLuckie](https://www.linkedin.com/in/craigmcluckie/) remembered an era of concern that Amazon’s cloud offerings had “effectively created this incredibly disruptive way to commercialize open source.”

But, he added, the Kubernetes team had drawn inspiration from the success of open source container management platform [Docker](https://www.docker.com/?utm_content=inline+mention). “I don’t think Kubernetes exists without Docker,” [Kelsey Hightower](https://thenewstack.io/kelsey-hightower-on-whats-next-for-developers-after-genai/) said, in a special introduction for Docker creator [Solomon Hykes](https://thenewstack.io/google-thanks-docker-and-solomon-hykes-comes-home/).

So there was much to celebrate, and the [Kubernetes community joined in all over the world](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/).

![Snyk Container product director Hannah Foxwell blows out candles at OpenUK KuberTENes birthday bash in London (photo by Jennifer Riggins)](https://cdn.thenewstack.io/media/2024/06/2008cb45-snyk-container-product-director-hannah-foxwell-blows-out-candles-at-openuk-kubertenes-birthday-bash-in-london-photo-by-jennifer-riggins-1024x576.jpg)
Snyk Container Product Director [Hannah Foxwell](https://www.linkedin.com/in/hannah-foxwell) blows out candles at OpenUK’s KuberTENes birthday bash.

yall.

[#kubernetes]changed my life forever. i’m so thankful to the early founders and members of the community for being so intentional with the values and the organizational design. so exquisite, so beautiful. the secret sauce if you ask me.[#kuberTENes]forevaaaaa[pic.twitter.com/awlVpuYdc0]— @paris@hachyderm.io (@ParisInBmore)

[June 7, 2024]
But as Kubernetes developer [Eric Jalal](https://www.linkedin.com/in/eric-jalal/) likes to say, Kubernetes is just Linux providing an interface and wrappers for familiar Linux functionality.

In October, Jalal made the case in a delightful [episode of the KubeFM podcast](https://www.youtube.com/watch?v=XNd63YyFYNA) (hosted by [Bart Farrell](https://bartfarrell.com/), a [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) ambassador). Fortunately, in 2024, Linux was also going strong, celebrating its 33rd anniversary and setting a new record for the percentage of desktops where it’s installed. (4.55%, [according to StatCounter in August](https://gs.statcounter.com/os-market-share/desktop/worldwide), prompting jokes about the arrival of the long-awaited Year of the Linux Desktop.)

Still, as December began, Linux kernel maintainer [Greg Kroah-Hartman](https://www.linkedin.com/in/greg-kroah-hartman) saw signs of real progress ahead, [predicting](https://lore.kernel.org/lkml/Z0lG-CIjqvSvKWK4@kroah.com/) “a tipping point” that brings “way more Rust drivers” to the kernel after some crucial driver binders were added into upcoming Linux kernel 6.13.

[Rust](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/) itself is also [part of the open source family](https://github.com/rust-lang/rust/blob/master/COPYRIGHT), and is seen as a key tool in the years ahead for [bringing memory safety to codebases](https://thenewstack.io/rusts-expanding-horizons-memory-safe-and-lightning-fast/). So in February Google announced a [million-dollar grant to the Rust Foundation](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/) to support efforts “to improve the ability of Rust code to interoperate with existing legacy C++ codebases.” And in November, AWS and the Rust Foundation [announced new cash prizes](https://aws.amazon.com/blogs/opensource/verify-the-safety-of-the-rust-standard-library/) for completing challenges in an online initiative to verify the safety of Rust’s standard libraries.
## Funding for Developers?
The hunt for new funding sources continues to worry the open source community. [Bruce Perens,](https://www.linkedin.com/in/bruce-perens) an original co-founder of the Open Source Initiative, is even [developing an alternative license](https://thenewstack.io/what-comes-after-open-source-bruce-perens-has-some-ideas/) where software is free for individuals and smaller organizations while “[deep-pockets entities” must contribute](https://postopen.org/how-post-open-works/) to a fund supporting open source developers [in myriad ways](https://news.slashdot.org/story/24/12/04/0426220/ask-bruce-perens-your-questions-about-how-he-hopes-to-get-open-source-developers-paid).

![Bruce Perens, creator of the original open source definition, at an event in 2009(Source: Wikimedia Commons)](https://cdn.thenewstack.io/media/2024/11/c1fa6192-bruce-perens-2009-2.jpg)
Archival photo of Bruce Perens at an event in 2009, from Wikimedia Commons.

But some funding continues to materialize.

- In October, Germany’s Sovereign Tech Fund announced it has invested more than $24.9 million into 60 open technologies over the last two years,
[according to Phoronix](https://www.phoronix.com/news/STF-Two-Years-24.9M-USD). - The
[GitHub Secure Open Source Fund,](https://resources.github.com/github-secure-open-source-fund/)launched in November, promises to invest “in security for fast-growing dependencies that support larger projects” with $1.25 million in initial contributions from donors including[American Express](https://thenewstack.io/how-american-express-created-an-open-source-program-office/),[Microsoft](https://news.microsoft.com/?utm_content=inline+mention),[Shopify](https://www.shopify.com/)and[Stripe](https://stripe.com/),
And in December the Linux Foundation released a report on open source funding co-authored with [GitHub](https://github.com/) and Harvard University’s [Laboratory for Innovation Science](https://lish.harvard.edu/). They found that the 501 organizations they surveyed were investing $1.7 billion each year in open source, “which can be extrapolated to estimate that approximately $7.7 billion is invested across the entire open source ecosystem annually.”

However, 86% of that investment took the form of contributing labor from their employees, with only 14% (or $1.078 billion) in direct financial contributions.

To spur more contributions, billboards even began appearing around San Francisco shaming tech companies that didn’t fund open source maintainers.

Seeing these grotesque billboards in SF and asking WTF? Us too—Where’s The Funding? Join us in pledging $2,000 per dev to support the open-source projects your business relies on:

[https://t.co/uBZF3M19h0][pic.twitter.com/Z5GoCXnjUP]— Chris Jennings (@ckj)

[October 11, 2024]
“Our goal is to establish a new social norm in the tech industry of companies paying Open Source maintainers, so that burnout and related security issues such as those in XZ and Apache Log4j can become a thing of the past,” reads the [Open Source Pledge](https://opensourcepledge.com/about/) web site. Or, as [Chad Whitacre](https://www.linkedin.com/in/chadwhitacre/), project co-founder, [told the Register](https://www.theregister.com/2024/10/25/open_source_funding_ads/), “These billboards are obviously a cheeky way to get people’s attention, and they’re working,”

The Open Source Initiative issued a [statement of support](https://opensource.org/blog/the-open-source-initiative-supports-the-open-source-pledge) for the group.

## 2024’s Belated Open Source Releases
Open source software continues its long march, racking up milestones as the years roll by. In 2025 the Free Software Foundation will celebrate it 40th anniversary, with this year bringing some [celebrations for its 39th](https://www.fsf.org/blogs/community/fsf-turns-39). But in another entirely different kind of milestone, in April Microsoft finally [open sourced the 1988 code for MS-DOS 4.0,](https://opensource.microsoft.com/blog/2024/04/25/open-sourcing-ms-dos-4-0/) written long before the open source era even began, when Microsoft was a decidedly closed-source shop.

Perhaps even more meaningful was the fact that, in June, developer [Jim Hall](https://freedos.org/jhall/) celebrated 30 years of [FreeDOS,](https://www.freedos.org/) the open source MS-DOS alternative he’d launched back in 1994. Now coordinating a larger development community, Hall used the anniversary to share [what he’s learned from the last 30 years ](https://opensource.net/lessons-learned-open-source-30-years-freedos/)with a post on the OpenSource.net blog, starting by emphasizing that the projects “must be grounded in community,” and that they must have respectful communication.

“Three decades is a long time for any Open Source project, especially for a retrocomputing operating system like FreeDOS,” Hall wrote. “But it’s all because of the great developers and users in our community. In celebrating FreeDOS, we are celebrating everyone who has created programs, fixed bugs, added features, translated messages, written documentation, shared articles or contributed in some other way.”

Maybe it’s all proof that one of the beauties of the open source movement is the way it encompasses such a wide variety of projects both big and small. The lightweight Dillo web browser celebrated its 25th anniversary by resurrecting the project with [a new GitHub repository](https://github.com/dillo-browser/dillo/). Lead developer [Rodrigo Arias Mallo](https://github.com/rodarima) had been inspired when an Atari forum announced the 25-year-old browser had been [successfully ported to an Atari emulator](https://github.com/dillo-browser/dillo/issues/34), and soon tech news sites were [hailing](https://hackaday.com/2024/05/11/the-minimalistic-dillo-web-browser-is-back/) the [end](https://www.theregister.com/2024/05/07/dillo_browser_v3_1/) of a [nine-year hiatus](https://9to5linux.com/dillo-3-1-open-source-web-browser-released-after-9-year-hiatus).

There’s even an open source remake of the 1995 video game Transport Tycoon Deluxe, still under active development, and in March [celebrating its 20th anniversary](https://www.openttd.org/news/2024/03/06/happy-birthday). And Steam got [a reboot](https://store.steampowered.com/app/2330720/ChipWits/) of the 1984 educational game [ChipWits](https://en.wikipedia.org/wiki/ChipWits), along with [the open sourcing of its original 1984 code](https://github.com/chipwits/chipwits-forth).

March also saw the release of version 10.0 of the Unix-like open source OS NetBSD. First launched in 1993, NetBSD 10.0 arrived “after being in development since 2019,” [Phoronix reported](https://www.phoronix.com/news/NetBSD-10.0-Released), bringing automatic swap encryption, WireGuard support and “support for many newer Arm platforms including for Apple Silicon and newer Raspberry Pi boards.”

And September even brought a [new beta release candidate for Haiku](https://www.haiku-os.org/news/2024-09-13_haiku_r1_beta5/), the MIT-licensed operating system inspired by the 1985 operating system [BeOS](https://en.wikipedia.org/wiki/BeOS).

## Open Tools for Open Developers
One of the great joys of the open source movement is the ongoing creation of open source tools with which to do more open source coding.

Photoshop alternative [Gimp](https://www.gimp.org/) has been around since 1998. But this year saw [new release candidates for Gimp 3.0](https://www.gimp.org/news/2024/11/06/gimp-3-0-RC1-released/), its first major update since 2018, [according to LWN.net](https://lwn.net/Articles/998793/). (And Gimp also announced a restructuring of its development process “to decrease time between releases.”)

![New GIMP icon for Wilber mascot CC image by-sa 4 gimp-logo](https://cdn.thenewstack.io/media/2024/12/f560df4f-new-gimp-icon-for-wilber-mascot-cc-image-by-sa-4-gimp-logo.png)
Gimp’s logo.

And while GitHub stopped development on its [Atom](https://github.com/atom-community/atom) text editor [in 2022](https://github.blog/news-insights/product-news/sunsetting-atom/), this just led to more open source alternatives. 2024 saw continued development on [Pulsar](https://github.com/pulsar-edit/pulsar), which describes itself as “a true community-led project to modernize, update and improve the original Atom project into a contemporary, hackable and fully open editor.”

Meanwhile, three former Atom developers have also teamed up for a startup building “a more refined and fleshed out version” of Atom, and in January 2024, [open sourced the code for their Zed Editor](https://zed.dev/blog/zed-is-now-open-source). (“We’ll need all the help we can get,” their blog post declared, adding, “We also think going open source will be a lot more fun.”)

And 2024 saw yet another open source developer environment. The [Eclipse Foundation](https://www.eclipse.org/) announced general availability of its [open source Theia IDE](https://eclipsesource.com/blogs/2024/06/27/introducing-the-theia-ide/) for cloud and desktop — “compatible with VS Code extensions.”

So if there’s a message in the year 2024, maybe it’s just that the open source movement is everywhere, stretching across space and time with the inextinguishable power of a very good idea. Its influence echoes through the years gone by — and into the years yet to come — while leaving in its wake an ever-growing community of happy and satisfied users.

And we wish them all a very happy New Year.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)