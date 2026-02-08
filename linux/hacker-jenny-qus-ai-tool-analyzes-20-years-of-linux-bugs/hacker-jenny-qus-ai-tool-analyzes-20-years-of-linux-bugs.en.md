Can we develop a better bug-finding tool by analyzing the Linux kernel’s last 20 years of commits using AI?

In [a recent blog post](https://pebblebed.com/blog/kernel-bugs), security researcher [Jenny Guanni Qu](https://github.com/quguanni) analyzed 125,183 bug fixes in the Linux kernel — going all the way back to April of 2005, the month [Git](https://thenewstack.io/beyond-code-control-git-for-everything/) was first released to the world.

And then Qu used that research to prototype an AI-assisted tool to predict which new commits are likely to introduce a bug…

Qu told The New Stack that “We’re planning to release the trained model and inference code after validation experiments complete, likely within the next few weeks.”

And the New Stack tracked down Linux kernel developer [Greg Kroah-Hartman](https://github.com/gregkh) for a reaction, who provided reminders of what Linux is [already doing](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/) to search and destroy bugs, and to fine-tune their patching processes.

It’s all proof that the developer community is serious about eliminating bugs — and has invested lots of time building the best possible tools to identify them before they’re committed. But are there new ways to approach it?

With a conscientious (and growing) community reviewing the Linux kernel’s code, one researcher decided to launch their own R&D effort to see if they could come up with something even better.

## Key findings from Linux kernel bug research

It took six hours for Qu to mine the kernel’s 20-year commit history on Git. (Qu [released the dataset on GitHub](https://github.com/quguanni/kernel-vuln-data) and [HuggingFace](https://huggingface.co/datasets/quguanni/kernel-vuln-dataset) under the MIT license) Qu’s first takeaway? Today’s bugs have trouble hiding from Linux’s kernel developers.

“We’re simultaneously catching new bugs faster *AND* slowly working through about 5,400 ancient bugs that have been hiding for over five years.”

In fact, Qu’s research shows that by 2022, 69% of bugs were being found within one year. (That’s up from 0% in 2010.) Qu believes this demonstrates “real improvement from better tooling,” according to her blog post. By 2025, the median lifetime for bugs (before they were found, fixed, and closed) was just 0.7 years. And only 13.5% of the bugs were more than 5 years old.

This is partly because here in 2026, we now have more contributors reviewing the Linux kernel’s code, Qu believes. But she also attributes it to the increasing use of high-quality testing tools over time, including:

* The Syzkaller fuzzer (released in 2015)
* Dynamic memory error detectors like the KASAN, KMSAN, and KCSAN sanitizers
* Better static analysis

Also, just 158 of the 125,183 bugs analyzed had a CVE — barely 0.12%.

Qu adds one caveat. Git actually shows 448,000 commits for the Linux kernel, mentioning some kind of “fix”, but only 28% of that large set uses the *Fixes:* tag on Git, which Qu used to identify commits for her analysis. So “My dataset captures the well-documented bugs aka the ones where maintainers traced the root cause.”

But Qu saw a clear message. “I found that security bugs hide for an average of 2.1 years before anyone catches them,” she told The New Stack. Some persist for over 20 years. That’s not a tooling problem but a pattern recognition problem….”

Could these insights be used to develop a new kind of bug-finding tool?

## The hacker behind the AI bug detection tool

Qu’s research took place at VC firm Pebblebed Ventures (whose [investments include the genAI image startup](https://pebblebed.com/portfolio) [Krea](https://pebblebed.com/blog/krea)). “We back the foundational layers of progress,” promises their home page.

Qu describes it as “technical investors backing technical founders,” offering a “fairly unstructured” residency targeted at research “that could become the foundation for a company. In my case, autonomous vulnerability discovery.” (Pebblebed’s webpage says “we let researchers loose on ideas too weird for a roadmap.”) And Qu was the perfect person to explore AI-powered tools for bug hunting. Pebblebed’s homepage says Qu “trained AI to solve math at Caltech” and “is one of the best competitive hackers in the world.”

Qu’s team SuperDiceCode placed 3rd at DEF CON CTF 2025 — “I’ve been doing CTFs competitively for years,” Qu told The New Stack — and this real-world experience inspired her investigation. “The same classes of vulnerabilities keep appearing in the kernel decade after decade. Use-after-frees, race conditions, missing bounds checks. I wanted to understand why these bugs persist and whether we could catch them earlier.”

Qu’s CalTech studies had even included reinforcement learning for math AGI, as well as studying math, physics, and CS at UC Davis (according to [a homepage that simulates a Linux command line](https://quguanni.com/)). So as Qu puts it…

“Pebblebed gave me money to build AI that finds zero days first, and I am locked in.”

Qu’s research showed that the hardest bug to find was a race condition, which lasted an average of 5.1 years (with a median for race-condition bugs of 2.6 years). “They’re non-deterministic and only trigger under specific timing conditions that might occur once per million executions. Even sanitizers like KCSAN can only flag races they observe.”

![Screenshot from Jenny Guanni Qu blog post at PebbleBed Ventures — stats on 20 years of Linux bugs](https://cdn.thenewstack.io/media/2026/01/0a435cd2-screenshot-from-jenny-guanni-qu-blog-post-at-pebblebed-ventures-stats-on-20-years-of-linux-bugs.png)

Qu believes other bugs are harder to find because they’re not detected as often by today’s fuzzing tools.

And here her own experience came into play. “The difference between a great hacker and a great programmer is mostly exposure. Hackers have seen thousands of vulnerable programs, so we develop intuition for when code looks suspicious. That’s just pattern matching on a large dataset which is exactly what ML is good at.”

So Qu set out to transmute this insight into a tool.

## Developing the AI-assisted bug prediction tool

Qu’s research first identified patterns in long-running bugs, including reference-counting errors, missing NULL checks after dereferencing or an integer overflow in size calculations. Then Qu created a tool that looks at the code before and after a fix, using both neural pattern recognition and some “handcrafted” checks.

Those handcrafted checks used regular expressions and an AST-like analysis to spot 51 potentially problematic code structures — everything from error-handling statements to memory-allocation statements — watching for key patterns like an “unbalanced” number or references or pointers without a null-check (suggesting a memory leak). The neural network then learns what conditional relationships actually suggest a bug, Qu writes, “Neither neural networks nor hand-crafted rules alone achieve the best results. The combination does.”

And Qu was impressed by its results.

* “Of all safe commits, we incorrectly flag 1.2%.”
* “Of commits we flag as risky, 98.7% actually are.”
* “Of all actual bug-introducing commits, we catch 92.2%.”

Qu’s blog post acknowledges possible shortcomings in her dataset. (For example, the system was only trained on the 28% of bugs with a *Fixes:* tag — meaning they were well-documented bugs, which tend to be more severe.) And among the model’s limitations are the fact that it was only trained on bugs that were *found* — so, not on bugs following new and unique patterns.

Qu’s blog post concludes this makes her tool VulnBERT “a triage tool, not a guarantee. It catches 92% of bugs with recognizable patterns. The remaining 8% and novel bug classes still need human review and fuzzing.” Qu believes the data shows the tool is production-ready.

## Linux kernel developer’s perspective on AI bug tools

In the blog post, Qu says she’d also like to see an agent trained with reinforcement learning while exploring code paths so it could *identify* bugs. (And if a fuzzer like Syzkaller actually finds a crash in a flagged code path, maybe that could be incorporated as a positive signal.)

“The goal isn’t to replace human reviewers but to point them at the 10% of commits most likely to be problematic, so they can focus attention where it matters.”

And already since publishing her blog post, “A few kernel developers have reached out,” Qu tells The New Stack, “which has been encouraging.” And she also reports “solid engagement in security research circles.”

But Linux kernel developer Greg Kroah-Hartman has seen similar investigations. “There’s been other researchers digging into our commit history over the years as well, doing many research papers,” he tells The New Stack in an email interview, “as we have loads of public data that ‘traditional’ closed source operating systems don’t provide at all.”

So while he enjoyed Qu’s blog post as “a cool report”, Kroah-Hartman also feels “we have been doing this type of reporting for over a decade now.” (He cited the [annual talks by Linux kernel security engineer Kees Cook](https://www.youtube.com/watch?v=c_NxzSRG50g) at Linux security conferences, “and the many reports from Jon Corbet on [lwn.net](https://lwn.net/%20) that [track this same thing](https://lwn.net/Articles/914632/).”

VIDEO

So while Qu’s blog post described prototyping a new tool, Kroah-Hartman points out they’re already always watching vigilantly for commits that could introduce new bugs. “We have tools that are running on kernel patch submissions *BEFORE* they are accepted to try to find these types of things.

“Running them on the commits already in our tree would also be good, *BUT* we have tons of people already just doing that on the code itself. That’s what the static analysis checkers have always done, right?”

And that’s just the beginning. “We also have been running LLM tools on our commits for over a decade now, with many papers and presentations about the tools and processes being used. This isn’t a new thing, it’s how we work to properly backport patches to older kernel trees.”

Although in his email Kroah-Hartman reiterated that they always welcome new bug reports…

![Greg Kroah-Hartman (Linux kernel maintainer) responds to kernel bugs blog post — screenshot from email January 20, 2026](https://cdn.thenewstack.io/media/2026/01/5bcf7a53-greg-kroah-hartman-linux-kernel-maintainer-responds-to-kernel-bugs-blog-post-screenshot-from-email-january-20-2026.png)

His verdict? “The report was cool, but we have a bit better data already, in our public tools we use for CVE reporting (and the database it generates). No need to mess with any ‘AI tools’ for the information, just normal SQL will work just fine…”

But Qu’s work on the tool is still continuing. “I’m presenting at BugBash 2026 in April and hoping to connect with more of the kernel security community there.

“The real test will be prospective validation: can we catch vulnerabilities in new commits before they’re discovered?”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)