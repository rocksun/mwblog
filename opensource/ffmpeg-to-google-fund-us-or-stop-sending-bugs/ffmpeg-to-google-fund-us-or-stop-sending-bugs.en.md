You may never have heard of [FFmpeg](https://www.ffmpeg.org/), but you’ve used it. This [open source](https://thenewstack.io/the-reality-of-open-source-more-puppies-less-beer/) program’s robust multimedia framework is used to process video and audio media files and streams across numerous platforms and devices. It provides tools and libraries for format conversion, aka transcoding, playback, editing, streaming, and post-production effects for both audio and video media.

FFmpeg’s libraries, such as [libavcodec](https://ffmpeg.org/libavcodec.html) and [libavformat](https://ffmpeg.org/doxygen/trunk/group__libavf.html), are essential for media players and software, including VLC, Kodi, Plex, Google Chrome, Firefox, and even YouTube’s video processing backend. It is also, like many other vital [open source programs, terribly underfunded](https://thenewstack.io/can-open-source-sustain-itself-without-losing-its-soul/).

## Corporate Responsibility vs. Volunteer Labor

A lively debate on Twitter began between [Dan Lorenc](https://www.linkedin.com/in/danlorenc), CEO and co-founder of [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention), the software supply chain security company, the FFmpeg project, [Google](https://cloud.google.com/?utm_content=inline+mention), and security researchers over security disclosures and the responsibilities of large tech companies in open-source software.

The core of the discussion revolves around how vulnerabilities should be reported, who is responsible for fixing them, and the challenges that arise when AI is used to uncover a flood of potentially meaningless security issues. But at heart, it’s about money.

## An Obscure Bug Ignites the Controversy

This discussion has been heating up for some time. In mid-October, FFmpeg tweeted that “[security issues are taken extremely seriously in FFmpeg](https://x.com/FFmpeg/status/1979066506030793116), but fixes are written by volunteers.” This point cannot be emphasised enough. As FFmpeg tweeted later, “[FFmpeg is written almost exclusively by volunteers.](https://x.com/FFmpeg/status/1982592087494398164)”

Thus, as [Mark Atwood](https://www.linkedin.com/in/-mark-atwood/), an open source policy expert, pointed out on Twitter, he had to keep telling [Amazon](https://aws.amazon.com/?utm_content=inline+mention) to not do things that would mess up FFmpeg because, he had to keep explaining to his bosses that “[They are not a vendor, there is no NDA, we have no leverage,](https://x.com/_Mark_Atwood/status/1978888607298691279) your VP has refused to help fund them, and they could kill three major product lines tomorrow with an email. So, stop, and listen to me … ”

## The Growing Burden on Open Source Maintainers

The latest episode was sparked after a Google AI agent found an especially obscure bug in FFmpeg. How obscure? This “[medium impact issue in ffmpeg](https://issuetracker.google.com/issues/440183164),” which the FFmpeg developers did patch, is “an issue with [decoding LucasArts Smush codec](https://x.com/FFmpeg/status/1983949866725437791), specifically the first 10-20 frames of Rebel Assault 2, a game from 1995.”

Wow.

FFmpeg added, “FFmpeg aims to play every video file ever made.” That’s all well and good, but is that a valuable use of an assembly programmer’s time? Oh, right, you may not know. FFmpeg’s heart is assembly language. As a former assembly language programmer, it is not, in any way, shape, or form, easy to work with.

As FFmpeg put it, this is “[CVE slop.](https://x.com/ffmpeg/status/1984207514389586050)”

Many in the FFmpeg community argue, with reason, that it is unreasonable for a trillion-dollar corporation like Google, which heavily relies on FFmpeg in its products, to shift the workload of fixing vulnerabilities to unpaid volunteers. They believe Google should either provide patches with vulnerability reports or directly support the project’s maintenance.

Earlier, FFmpeg pointed out that it’s far from the only open source project to face such issues.

Specifically, the project team mentions [Nick Wellnhofer](https://www.linkedin.com/in/nwellnhof/), the former maintainer of [libxml2](https://gitlab.gnome.org/GNOME/libxml2), a widely used open source software library for parsing Extensible Markup Language (XML). [Wellnhofer recently resigned from maintaining libxml2](https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398) because he had to “spend several hours each week dealing with security issues reported by third parties. Most of these issues aren’t critical, but it’s still a lot of work.

“In the long term, this is [unsustainable for an unpaid volunteer like me.](https://gitlab.gnome.org/GNOME/libxml2/-/issues/913) … In the long run, putting such demands on OSS maintainers without compensating them is detrimental. …  It’s even more unlikely with Google Project Zero, the best white-hat security researchers money can buy, breathing down the necks of volunteers.”

## Google’s Controversial Security Disclosure Policy

What made this a hot issue was that back in July, [Google Project Zero (GPZ)](https://googleprojectzero.blogspot.com/) announced a trial of its new [Reporting Transparency](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html) policy. With this policy change, GPZ announces that it has reported an issue on a specific project within a week of discovery, and the security standard 90-day disclosure clock then starts, regardless of whether a patch is available or not.

Many volunteer open source program maintainers and developers feel this is massively unfair to put them under such pressure when Google has billions to address the problem.

FFmpeg tweeted, “[We take security very seriously](https://x.com/FFmpeg/status/1984178359354483058), but at the same time, is it really fair that trillion-dollar corporations run AI to find security issues in people’s hobby code? Then expect volunteers to fix.”

True, Google does offer a [Patch Rewards Program](https://bughunters.google.com/about/rules/open-source/4928084514701312/patch-rewards-program-rules), but as a Twitter user using the handle Ignix The Salamander observed, “[FFmpeg already mentioned the program is too limited for them](https://x.com/ignixsalamander/status/1986111396095074689), and they point out the three patches per month limit. Please don’t assume people complain just for the sake of complaining, there is a genuine conflict between corporate security & usage vs open source support IMHO.”

Lorenc argues back, in an e-mail to me, that “Creating and publishing software under an open source license is an act of contribution to the digital commons. Finding and publishing information about security issues in that software is also an act of contribution to the same commons.

“The position of the FFmpeg X account is that somehow disclosing vulnerabilities is a bad thing. Google provides more assistance to open source software projects than almost any other organization, and these debates are more likely to drive away potential sponsors than to attract them.”

## Differing Perspectives on Vulnerability Disclosures

The fundamental problem remains that the FFmpeg team lacks the financial and developer resources to address a flood of AI-created CVEs.

On the other hand, security experts are certainly right in thinking that FFmpeg is a critical part of the Internet’s technology framework and that security issues do need to be made public responsibly and addressed. After all, hackers can use AI to find vulnerabilities in the same way Google does with its AI bug finder, [Big Sleep](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html), and Google wants to identify potential security holes ahead of them.

The reality is, however, that without more support from the trillion-dollar companies that profit from open source, many woefully underfunded, volunteer-driven critical open-source projects will no longer be maintained at all.

For example, [Wellnhofer has said he will no longer maintain libxml2 in December](https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398). Libxml2 is a critical library in all web browsers, web servers, LibreOffice and numerous Linux packages. We don’t need any more arguments; we need real support for critical [open source programs](https://thenewstack.io/open-source/ "open source programs") before we have another major security breach.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)