# Curl Fights a Flood of AI-Generated Bug Reports From HackerOne
![Featued image for: Curl Fights a Flood of AI-Generated Bug Reports From HackerOne](https://cdn.thenewstack.io/media/2025/05/2a944577-sky-2713230_1280-1024x768.jpg)
Earlier this month, Curl maintainer [Daniel Stenberg](https://www.linkedin.com/in/danielstenberg/) [complained on LinkedIn](https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAy0NmwBik8M9HA68ZGPBUrhjbXeEOFFBaA) about a flood of “AI slop” bug reports that had been coming in. “That’s it. I’ve had it,” he wrote. “I’m putting my foot down on this craziness.”

The project was “effectively being DDoSed,” he wrote. And the culprit was volunteers for the bug bounty site [HackerOne](https://www.hackerone.com/).

Stenberg’s LinkedIn post drew over 250 comments — and over 600 reposts. The incident kicked off a larger discussion around the web about the AI-powered era we’ve stumbled into — and how exactly we should be responding to AI-assisted humans.

So while Stenberg still appreciates the crowd-sourced security reports from HackerOne, he’s made it clear that he hopes to see some changes going forward — both small changes and big ones.

## Outcomes Not Origins
Two things happened last week. On Friday, May 16, HackerOne Co-founder/CTO/CISO [Alex Rice](https://www.linkedin.com/in/alexrice/) reiterated its stance that HackerOne’s Code of Conduct “does not prohibit the use of AI to assist in writing reports” — but it does prohibit spam. “Reports that contain hallucinated vulnerabilities, vague or incorrect technical content, or other forms of low-effort noise will be strictly treated as spam and result in enforcement actions under our Code of Conduct.”

In response to questions from The New Stack, Rice stressed that reports need to be “clear, accurate, and actionable” — but that HackerOne remains officially focused on outcomes, not origins. “We believe AI, when used responsibly, can be a powerful tool for researchers, enhancing productivity, scale, and impact. Innovation in this space is accelerating, and we support researchers who use AI to improve the quality and efficiency of their work.

“On the question of quantity, we’re actually seeing an aggregate increase in report quality as AI helps researchers bring clarity to their work,” Rice added. “While we have not surfaced widespread evidence of AI-generated hallucinations, these reports can be frustratingly difficult to validate and therefore is a concern we are actively addressing.”

Stenberg isn’t opposed to AI that identifies vulnerabilities for Curl. “I am convinced there will pop up tools using AI for this purpose that actually work (better) in the future, at least part of the time,” he [wrote in early 2024](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/), “so I cannot and will not say that AI for finding security problems is necessarily always a bad idea.

“I do, however, suspect that if you just add an ever-so-tiny (intelligent) human check to the mix, the use and outcome of any such tools will become so much better. I suspect that will be true for a long time into the future as well.”

This month, Stenberg said on LinkedIn that, “We still have not seen a single valid security report done with AI help.” But it’s possible AI-generated reports may have helped other projects. On LinkedIn, Stenberg had identified the “AI slop” report that “really pushed me over the limit.” But software engineer [Randy Clinton](https://www.linkedin.com/in/raclinton/) [pointed out](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324823934531432448%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324923922045411328%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324823934531432448%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287324923922045411328%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) that the same reporter seemed to have already earned over $1,900 in bug bounties from other HackerOne participants, including Adobe and Starbucks.

In his comments to The New Stack, Rice added his perspective. “Overall, we’re seeing an aggregate increase in report quality as AI helps researchers bring clarity to their work, especially where English is a second language… The key is ensuring that AI enhances the report rather than introducing noise.”

In short, he said, the goal of HackerOne “is to encourage innovation that drives better security outcomes, while holding all submissions to the same high standards.”

## Stenberg Takes Action
Meanwhile, on Thursday, May 15, Stenberg [announced](https://mastodon.social/@bagder/114511780991862687) Curl’s [new guidelines for AI usage](https://curl.se/dev/contribute.html#on-ai-use-in-curl) by contributors, making clear exactly what he’d like to see in the future. “If you asked an AI tool to find problems in curl, you must make sure to reveal this fact in your report.” (And answering “yes” guarantees a “stream” of follow-up questions to prove there’s some actual human intelligence on the other side of the report, Stenberg warned [on Mastodon](https://mastodon.social/@bagder/114450295029056683).)

By January 2024, [Curl](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/) had already paid out $70,000 in bug bounties (for 64 confirmed security problems), Stenberg [wrote in a blog post](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/). But a “crap” security report means “we missed out time on fixing bugs or developing a new feature. Not to mention how it drains you on energy having to deal with rubbish.”

So this month’s new AI usage guidelines warn contributors that “You must also double-check the findings carefully before reporting them to us to validate that the issues are indeed existing and working exactly as the AI says. AI-based tools frequently generate inaccurate or fabricated results.” Cautioning that AI-detected bug reports can be too wordy (even before their all-too-common “fabricated details”), the guidelines tell users to first verify that the issue is real, and then “write the report yourself and explain the problem as you have learned it.

“This makes sure the AI-generated inaccuracies and invented issues are filtered out early before they waste more people’s time.”

It’s a sincere attempt to explain how “AI slop” interferes with moving the project forward, since Curl must take security reports seriously and investigate them promptly. “This work is both time and energy consuming and pulls us away from doing other meaningful work.

“Fake and otherwise made-up security problems effectively prevent us from doing real project work and make us waste time and resources.

“We ban users immediately who submit made-up fake reports to the project.”

Stenberg also seems to wish there were a financial penalty, since his LinkedIn post adds that, “If we could, we would charge them for this waste of our time.”

## “Make It Sound Alarming”
Earlier this month, Stenberg [told Ars Technica](https://arstechnica.com/gadgets/2025/05/open-source-project-curl-is-sick-of-users-submitting-ai-slop-vulnerabilities/) he was “super happy” the issue was getting attention “so that possibly we can do something about it…” He sees it as a chance to teach the larger community that “LLMs [large language models] cannot find security problems, at least not like they are being used here.” Stenberg also told the site that in one week, he’d received

*four*obviously AI-generated vulnerability reports — and that they’re easy to spot because they’re friendly and polite, with perfect English and nice bullet points. “An ordinary human never does it like that in their first writing…”
One user actually left their prompt in the bug report, Stenberg remembered — “and he ended it with, ‘and make it sound alarming.'”

And early in May, one [report](https://hackerone.com/reports/3125832) claimed it found evidence of memory corruption, with an analysis showing stack recursion from the function:

*ngtcp2_http3_handle_priority_frame*.
There was just one problem.

“There is no function named like this…” Stenberg [found himself posting](https://hackerone.com/reports/3125832#activity-34392850). He agreed later with embedded systems consultant [Jean-Luc Aufranc](https://www.linkedin.com/in/cnxsoft/), who’d [summarized](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324823934531432448%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325150930834743296%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324823934531432448%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287325150930834743296%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) the situation like this on LinkedIn: “[T]he AI created a random function… that did not exist in the code, and a security bug to go along.”

In a later comment, Stenberg said it’s [a growing phenomenon](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324854476945719296%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324901273827217408%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324854476945719296%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287324901273827217408%2Curn%3Ali%3Aactivity%3A7324820893862363136%29). In his 2024 blog post, Stenberg highlighted a suspected [AI-generated report](https://hackerone.com/reports/2199174) that “mixes and matches facts and details from old security issues, creating and making up something new that has no connection with reality…” However, Stenberg added on LinkedIn this month that “These kinds of reports did not exist at all a few years ago, and the rate seems to be increasing.”

So while the AI-generated comments are “still not drowning us… the trend is not looking good.”

## ‘Something Stronger’
Stenberg also told *Ars Technica* that he’d like to see HackerOne do “something, something stronger, to act on this.” He’s even willing to help them build the necessary infrastructure to create “more tools to strike down this behavior.”

But when a security tester on LinkedIn [suggested](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325880597157928960%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287325880597157928960%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) it was “time to throw out the bug bounty crowd-sourcing model, and hire full-time dedicated staff,” Stenberg disagreed.

“Our bug bounty has paid $86,000 for 78 confirmed vulnerabilities. No professional would come even close to that cost/performance ratio.” And in addition, he notes that Curl has managed to fund exactly one full-time employee. “I would love to hire more people but we struggle to get companies to support us.”

[Tobias Heldt](https://www.linkedin.com/in/tobias-heldt-214561264/), co-founder of cybersecurity company XOR, [wondered](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325545476110409729%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287325545476110409729%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) if the bug-reporting process needed some friction — like “if researchers had to stake a small deposit on their submission,” which was only refunded if their report was rated as clearing a basic threshold for informativeness. Later, Heldt refers to the idea as “Security Report Bonds,” arguing that, “Without it, soon the majority of reports will be from bots brute-forcing bounty programs.”
Stenberg agreed “that could be a workable model,” suggesting maybe companies like HackerOne should be the ones to take the lead.

![](https://cdn.thenewstack.io/media/2025/05/204d3b7f-python-seth_larson-300x225.jpg)
Python Software Foundation’s Seth Larson (Pycon 2025).

[Jim Clover](https://www.linkedin.com/in/jim-clover-obe-996b8724/), director of IT/service company Varadius Ltd, came up with a [novel solution](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324864784556769280%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324864784556769280%2Curn%3Ali%3Aactivity%3A7324820893862363136%29). He’d vetted the “AI slop” by asking ChatGPT o3, which correctly responded it was “technically unsound… cites functions that don’t exist.” Clover’s conclusion? “Could you stick these through AI (oh the irony) as a BS checker to save you guys time?”
But [Python](https://thenewstack.io/what-is-python/)‘s security developer-in-residence [Seth Larson](https://thenewstack.io/pythons-new-security-developer-has-plans-to-secure-the-language/) had already reached the opposite conclusion, [sharing](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136/?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324864784556769280%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325554175856062465%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324864784556769280%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287325554175856062465%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) a blog post he’d written in March titled, “[Don’t bring slop to a slop fight](https://sethmlarson.dev/dont-bring-slop-to-a-slop-fight).”

“[U]sing AI to detect and filter AI content just means that there’ll be even more generative AI in use, not less. This isn’t the signal we want to send to the venture capitalists who are deciding whether to offer these companies more investment money.”

## Responses and Reactions
It’s not clear what happens next. “People who are looking to abuse the system will continue to do so regardless of a checkbox being present,” senior full-stack developer [Damian Mulligan](https://www.linkedin.com/in/damian-mulligan-896b303a/) [posted on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325948820868005891%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287325948820868005891%2Curn%3Ali%3Aactivity%3A7324820893862363136%29).

Databricks software engineer [Hasnain Lakhani](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324870102380617729%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324870102380617729%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) wondered what he’d do when people simply lied about whether they’d used AI. (“Seems like an arms race,” he suggested, with projects needing tools to *screen* for AI.)

There was an ominous warning from Heldt. “AI slop is overwhelming maintainers *today* and it won’t stop at Curl but only starts there.”

But maybe an effective effort to deal with the problem has already begun. When someone on Mastodon asked Stenberg if it’s okay to repurpose Curl’s new guidelines about AI contributions for another project, Stenberg had a ready answer.

“[Absolutely](https://mastodon.social/@bagder/114512085821167451)!”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)