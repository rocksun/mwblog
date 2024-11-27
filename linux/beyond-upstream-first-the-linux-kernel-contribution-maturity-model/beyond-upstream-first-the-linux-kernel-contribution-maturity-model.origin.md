# Beyond Upstream First: The Linux Kernel Contribution Maturity Model
![Featued image for: Beyond Upstream First: The Linux Kernel Contribution Maturity Model](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)
NAPA, Calif. — [Theodore “Ted” Ts’o](https://en.wikipedia.org/wiki/Theodore_Ts%27o) knows a thing or two about the [Linux kernel](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/). After all, he was the first North American Linux kernel developer. On his personal desktop, Ts’o also ran the first FTP server to host the Linux kernel, which is where I downloaded my first copy of [Linux](https://thenewstack.io/learning-linux-start-here/) back in 1992. So, when he shared his insights on the [Linux Kernel Contribution Maturity Model (CMM)](https://docs.kernel.org/process/contribution-maturity-model.html) in a thought-provoking talk at the [2024 Linux Foundation Members Summit](https://docs.google.com/document/u/0/d/1CSVtpazPgbNxROho8ea5WNyktBJqKeSUsZ01CgE--Ms/edit), you should pay attention.

Ts’o began by explaining that since day one, Linux kernel development has always been about “[upstream first](https://thenewstack.io/how-to-keep-up-with-linux-bugs-jump-upstream/).” This means when you’re developing a new software feature, you add it to Linux upstream. “Counter-intuitively, T’so said, “This is more efficient than doing the engineering work against your product kernel, which might lag Linux upstream by years. This approach avoids rebasing out-of-tree patches and changing userspace interfaces when the functionality finally makes it upstream.”

While some companies, such as [Google with Android](https://arstechnica.com/gadgets/2021/09/android-to-take-an-upstream-first-development-model-for-the-linux-kernel/), have adopted the upstream-first approach, many others haven’t. To encourage them to get on the upstream-first bandwagon and to help Linux development, T’so pointed out, “Contributing upstream is important because it allows companies to influence the direction of kernel development.” He explained that this influence is not just about pushing a company’s agenda but about shaping the kernel to better serve diverse needs across the industry.

T’so added, “If you’re an engineering manager right now, one of the things that you’ve probably seen is that it is very, very difficult to get some critical feature upstream on a reliable and predictable time frame. That’s especially true today when you’ve got lots of companies that are all trying to get new AI products in, so you all want to try to get your features upstream as quickly as possible.”

This isn’t just a Linux problem, Tso explained. “it’s a common theme. I was talking to the lead for [OpenTelemetry](https://opentelemetry.io/). He was saying, ‘Yep, I see it there too.’ So this is not just Linux kernel.”

## Not Just a Linux Issue
That’s why T’so proposes that we go beyond “upstream first” for Linux. But what he’s calling, for now, “organizational-wide upstream.” It needs, he knows, a “more catchy title.” Companies must move beyond “simply getting your out-of-tree patches upstream and doing upstream-first development for all of your new features, and then hiring a couple of token upstream developers or upstream maintainers and calling it a day.”

“Instead,” he continued, “You encourage, or perhaps even mandate, that all of your engineers spend a certain amount of time doing upstream work.” And, this approach should be considered all your business’s mission-critical, open source projects.

Why? From a company’s engineering manager’s point of view, it’s in their own best interest to go upstream. Ordinarily, kernel maintainers are hesitant to accept new features until the patches are perfect and related technical debt is addressed. Unfortunately, once a new feature drop is landed, contributors often disappear. The engineering team is responsible for supporting the entire kernel, including parts of the kernel where there isn’t active investment by the company. By encouraging kernel engineers to develop their expertise by working upstream, they’re more likely to keep working on the kernel.

This has two advantages. First, a company is far more likely to get “their” features into the kernel sooner. Second, the Linux kernel gains more developers, reviewers and maintainers to help support it.

The last is not a small issue. The CMM’s roots can be traced back to the 2021 Linux Kernel Maintainers Summit. During this get-together of Linux’s top kernel developers, the challenges in recruiting kernel maintainers and ensuring maintainer succession was a hot topic. The CMM framework is meant to help with this problem.

The CMM, as Ts’o described it, outlines several stages of maturity for company involvement in upstream kernel development:

**Ad-hoc contributions:**Engineers contribute on their own time, often without company support.**Encouraged contributions:**Companies allow and encourage contributions during work hours.**Strategic contributions:**Organizations align contributions with business goals.**Community leadership:**Engineers take on maintainer roles and significantly influence kernel direction.
Ts’o stressed the importance of progression through these stages: “Moving up the maturity model is not just about the quantity of contributions but about the quality and strategic nature of involvement.”

According to Ts’o, companies that achieve higher levels of contribution maturity can expect several benefits:

**Cost reduction:**“By contributing upstream, companies can reduce the cost of maintaining out-of-tree patches,” Ts’o explained.**Improved product quality:**Upstream contributions lead to better integration and fewer bugs in the long run.**Enhanced reputation:**Active participation boosts a company’s standing in the open source community.**Talent attraction and retention:**“Engineers value the opportunity to work on upstream projects and grow their skills,” Ts’o noted.
Ts’o acknowledged the challenges companies face in implementing mature contribution practices. He quoted a common misconception: “‘We can’t afford to have our engineers spend time on upstream work.’ This short-term thinking often leads to higher costs in the long run.”

To overcome these challenges, Ts’o suggested:

- Educating management about the long-term benefits of upstream contributions.
- Implementing policies that support and reward open source participation.
- Developing mentorship programs to help engineers grow into community leadership roles.
“It’s crucial to create a culture where upstream contributions are valued and supported,” Ts’o emphasized. “The health of the Linux kernel ecosystem depends on companies maturing their contribution practices. By investing in upstream development and fostering a culture that values open source participation, companies can play a vital role in shaping the future of Linux while also reaping significant benefits for their own businesses and employees.”

Linux also badly needs to increase its pool of reviewers and maintainers. “Most maintenance work was done by very few engineers.” Thomas Gleixner, a leading Linux kernel developer who was also at this speech, reported that there are only 1,909 maintainers and reviewers. Of those, 653 have not performed any activities in two years. All together, 80% of these overall critical Linux activities were done by a mere 11% of the people. It’s no wonder that [Linux maintainer burnout is a critical problem](https://www.zdnet.com/article/what-linux-kernel-maintainers-do-and-why-they-need-your-help/).

T’so pointed out that while put that way it sounds like a ton of work, but it doesn’t have to be that bad. “if we could even get all of our various contributors to do one additional code review or one additional test or whatnot, it’d make a huge difference. If you can go from two maintainer activities a day to three maintainers a day, you’d really jump up high. It’s not that we actually need a lot of maintainers. We need to get a lot of people helping a little bit. Many hands make light work.” The result will be that “companies can better achieve their business plans” while Linux will grow stronger, and “this can be a win-win.”

I think he’s right. Ts’o’s talk is a compelling call to action for companies to reassess their approach to upstream kernel development and open source development. By moving to organizational-wide upstream, which I propose we call “universal upstream,” everyone in the open source software chain, from developer to end user, will mutually benefit.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)