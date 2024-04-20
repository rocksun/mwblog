# Linus Torvalds on Security, AI, Open Source and Trust
![Featued image for: Linus Torvalds on Security, AI, Open Source and Trust](https://cdn.thenewstack.io/media/2024/04/855ce6ac-torvalds-hohndel-02-1024x768.jpg)
SEATTLE–Linux creator
[Linus Torvalds](https://thenewstack.io/linus-torvalds-on-community-rust-and-linuxs-longevity/) sat down Wednesday for a “keynote interview” at the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)‘s [Open Source Summit North America](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/) in Seattle. Torvalds was interviewed by [Dirk Hohndel](https://www.linkedin.com/in/dirkhohndel/), an early [Linux contributor](https://thenewstack.io/linus-torvalds-on-why-open-source-solves-the-biggest-problems/) (and currently the head of Verizon’s Open Source program office) — in what was billed as a “fireside chat.”
But what came through clearly was Torvalds’ lifelong love of open source development — and how that’s been playing out in the real world filled with upstream security issues, overhyped AI, and other people’s hardware bugs.
Although their conversation started with a humorous exchange…
**Hohndel:** We all know kernel development does include a lot of drama and a lot of high-stakes discussions… For example, a really important topic that once again has reared its ugly head is [tabs versus spaces](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go/). **Torvalds:** Oh, Christ…
## Problems Beyond Your Control
![](https://cdn.thenewstack.io/media/2024/04/6579aabe-torvalds-03-225x300.jpg)
Linus Torvalds
Hohndel said
[technology](https://www.phoronix.com/news/Linux-Kconfig-Tabs) [news](https://www.theregister.com/2024/04/16/torvalds_complicates_his_indents/) [sites](https://arstechnica.com/gadgets/2024/04/linus-torvalds-reiterates-his-tabs-versus-spaces-stance-with-a-kernel-trap/) covering Torvalds [inserting tabs](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?utm_source=anzwix&id=d5cf50dafc9dd5faa1e61e7021e3496ddf7fd61e) (to catch parsing tools that can’t properly convert them to whitespace) are a kind of triumph for the open source project — a “sign of the maturity and health of Linux, that a small comment could generate news articles.”
But then Hohndel segued to the topic of “problems that are outside of your control, that you end up dealing with anyway” — and specifically, “
[yet another round of hardware bugs](https://www.bleepingcomputer.com/news/security/new-spectre-v2-attack-impacts-linux-systems-on-intel-cpus/).” Torvalds agreed things like the newly discovered Spectre v2 exploit were frustrating — but not for the obvious reason.
“I got into doing kernels because I’m interested in the hardware,” Torvalds pointed out. But he also loves
[Open Source development](https://thenewstack.io/whats-next-for-companies-built-on-open-source/), and “The thing that is very, very frustrating is that you have these technically interesting problems, but then they are made to be a horrendous experience by all the secrecy…”
“My fear is that RISC-V will do all the same mistakes that everybody else did before them.” — Linus Torvalds
![](https://cdn.thenewstack.io/media/2024/04/f12b24e5-torvalds-04-225x300.jpg)
Linus Torvalds
And Torvalds said it’s frustrating for fast-reacting software developers to then face the slower pace of hardware development. (“Oh, we have five generations of hardware that we can’t fix after the fact, and it will take another couple of years before the actual new hardware that can help you work around the problem comes out.”) “That ends up being very frustrating — with the whole added side of all the PR that goes along with any security issues.”
Hohndel asked if things would get better with Open Source hardware — especially after five years of RISC-V development. But Torvalds isn’t convinced. “My fear is that RISC-V will do all the same mistakes that everybody else did before them… When RISC-V becomes more of a big, widely-deployed platform, they’ll have all the same issues we had on the ARM side, and that x86 had before them. And it will take a few generations for them to say, ‘Oh, we didn’t think about that’ — because they have new people involved.”
But if hardware is developed out in the open, won’t that make it easier for software developers to warn them against repeating past mistakes?
“There’s a fairly big gulf between the Verilog [the standard hardware description language] and even the kernel,” Torvalds responded, “much less higher up the stack, where you’re working so far away from the hardware, that you really have no idea how the hardware works. So it’s really hard to work across this very wide gulf of things.”
Hohndel then made an interesting observation. Ten years ago it was hard even just to move from x86 to a new platform, but “Today most people don’t even know when they’re running on a [AWS] Graviton… or an AMD or an Intel chip. In the cloud, it all looks exactly the same, with the same software specs. Just the price point is different.”
And Torvalds says “That was one of the promises of open source. And people were saying that this was true 10 years ago.
“And it wasn’t true 10 years ago. But it’s certainly reaching that point now.”
## Relying on Trust
![](https://cdn.thenewstack.io/media/2024/04/1a7b36eb-torvalds-hohndel-03-300x225.jpg)
Torvalds and Hohndel
But recently the open source community faced a stark reminder that security issues can come from the other direction too — from the community of maintainers. When asked about the recent
[xz Util exploit](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/), Torvalds shared his own perspective — starting by emphasizing that even proprietary software has its own reliance on trust. “[Users] depend on the trust in the company. But also within the company you depend on trust — in your employees. And that trust can be violated.”
“And how to figure out when it’s being violated is an open problem.”
Torvalds spoke from decades of experience. Even a long-standing open source project like Linux has “seen this before,” Torvalds said, remembering a
[2021 incident](https://thenewstack.io/university-of-minnesota-researchers-tried-to-poison-the-linux-kernel-for-a-research-project/) where University of Minnesota researchers tested how easy it would be to upstream bad kernel patches. (“That’s actually an interesting study. They just didn’t do it very well. They didn’t tell a third party about this, and they just sent us bad patches.”) But now the open source ecosystem has seen an actual malicious attempt to upstream bad code — and in a world where, as Torvalds puts it, “nobody really had any explicit gates in place to try to catch this.”
Yet Torvalds also sees a hopeful sign. Whether it’s xz or those bad patches that the students tried to upload for the kernel in 2021, “In both cases, they were actually really caught fairly quickly.” And that fact “does seem to imply a fairly strong amount of stability — and that these things do get caught.”
![](https://cdn.thenewstack.io/media/2024/04/86056b62-torvalds-05-225x300.jpg)
Linus Torvalds
Even with that, Torvalds acknowledges that “Clearly it’s a wake-up call — there’s no question about that… I think we’re going to see a lot of work being put into some kind of trust model, where people see, ‘Oh, this is a new person’, or ‘This is a person that is acting differently from before.”
Hohndel pointed out that deep within the Linux developer community, signature requirements include a face-to-face meeting — and government-issued ID. And Torvalds agreed with Hohndel’s idea that the best defense is a healthy community.
Hohndel went on to note that “The Linux kernel has this incredibly big, but also incredibly deeply entwined and connected community, where there are multiyear, multidecade relationships at the core of all this.”
But this prompted a reminder from Torvalds — that Linux’s kernel is an atypical open source project. “A lot of open source projects, even very central ones, are basically run by one or two or three people… ”
## AI for Open Source?
![](https://cdn.thenewstack.io/media/2024/04/9c30582a-torvalds-02-225x300.jpg)
Linus Torvalds
At one point, Hohndel introduced the topic of AI, noting dire predictions it will someday eliminate programmers, authors, movie creators, and jobs. “So you are going to be replaced by an AI model.”
“Finally!” Torvalds joked.
Responding more seriously, Torvalds added “No… I hate the hype… My personal opinion is, let’s wait 10 years and see where it actually goes before we make all these crazy announcements of ‘Your job will be gone in five years.”
But what about AI in coding tools? Torvalds admitted he was “optimistic” about AI, and “looking forward to the tools to actually find bugs.” With kernel developers (and other projects) already religiously using the tooling they have, “making the tools smarter is not a bad thing.”
He called smarter tools “just the next inevitable step… But I don’t think it’s necessarily the gloom and doom that some people say it is, and I definitely don’t think it’s the promised world that people who are having their hand out for cash say it is.”
There was a funny exchange when Torvalds warned his audience, “You need to be a bit cynical about this whole hype cycle in the tech industry… Before AI it was crypto, before crypto, it was whatever.”
“Cloud native,” suggested Hohndel. (Later adding that he’d heard “That’s not hype!” from a “loud voice in the front.”)
But Torvalds reiterated his call to judge the news carefully. “I mean, the hype? There’s always like a grain of reality behind it. But you need to be careful about all the BS around that grain.”
## The Point of Open Source
![](https://cdn.thenewstack.io/media/2024/04/00b72265-hohndel-01-225x300.jpg)
Dirk Hohndel
Throughout the half-hour interview, there were glimpses of what motivates Torvalds personally, after more than 30 years of Linux kernel development. When Hohndel said
[Open Data](https://thenewstack.io/linux-foundation-overture-maps-the-globe-with-open-data/) was almost the more interesting question, Torvalds reflexively responded “No It’s not,” before adding “Not to me.” But the Linux Foundation has Open Data projects, and “to other people it’s more interesting. And that is, I think, the whole — for me, the point of Open Source is that different people are interested in different things… I was always interested in the low-level nitty-gritty of how the CPU actually works. Which is why I’m working on the kernel still.”
Towards the end, Torvalds said he didn’t plan to start any new projects. “Linux for me solved all the problems I had, way back in ’92, maybe ’93. And if it wasn’t for the fact that others came around and said ‘Hey, I need this,’ I would not have continued.”
The things that keep is projects going are “the fact that ‘Hey, this is actually useful to other people’. Because if it’s only something for me, it’s not really interesting in the long run.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)