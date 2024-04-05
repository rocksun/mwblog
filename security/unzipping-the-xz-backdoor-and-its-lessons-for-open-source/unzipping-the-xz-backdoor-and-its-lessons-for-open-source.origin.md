# Unzipping the XZ Backdoor and Its Lessons for Open Source
![Featued image for: Unzipping the XZ Backdoor and Its Lessons for Open Source](https://cdn.thenewstack.io/media/2024/04/176ff530-intruder123-1024x576.jpg)
By now, you have probably heard about the recently discovered backdoor into versions 5.6.0 and 5.6.1 of the tarballs of the
[xz utilities](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/), a popular compression/decompression library for xz files, which provides unauthorized remote access under certain conditions. This vulnerability was reported under [CVE-2024-3094](https://access.redhat.com/security/cve/CVE-2024-3094). Andres Freund, of Microsoft, who discovered the vulnerability, [summarized it well](https://www.openwall.com/lists/oss-security/2024/03/29/4).
This initial announcement quickly sent shockwaves through the entire open source ecosystem due to the manner in which it was introduced and the extent of risk introduced by this backdoor. This opened a lot of questions (again) around the thankless work of open source maintenance, particularly when individual contributors have the task of doing this with little incentive to continue doing so.
This is my perspective on the what, how and why of this type of exploit and what the industry can do to try to change this worrying trend.
**What Happened and How Was It Discovered **
While this is
[ still a developing story](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/), a lot of details have been uncovered about how this library was compromised. It started in 2021 when some GitHub account under the name of Jia Tan opened a suspicious PR in libarchive. Then in 2022, he was added as the maintainer of the xz project, while Lasse Collin, the official maintainer of the project, was dealing with personal issues. Gradually, parts of the backdoor were committed and merged into xz by Jia Tan in 2023.
On March 29, Freund, who says he’s not a security researcher, started to experience some slowness in sshd, which depends on the xz library in some Linux distributions, as well as high CPU. After investigating the source of the issue, he discovered the backdoor into the xz package, which was introduced as part of seemingly innocent commits aiming to add more tests to the repository and which ultimately modified the build process to introduce the malware.
![](https://cdn.thenewstack.io/media/2024/04/4347ee46-image1a.png)
Source:
[https://xkcd.com/2347/](https://xkcd.com/2347/)
**Who Is Affected?**
These Linux distributions have issued statements about being affected by the backdoor:
Please follow the instructions for each distribution as soon as possible to either upgrade or revert to the previous version of the package.
[Debian](https://lists.debian.org/debian-security-announce/2024/msg00057.html)maintainers acknowledged that compromised packages were part of the distribution testing, but the stable versions should not be affected. [Ubuntu](https://ubuntu.com/security/CVE-2024-3094)distributions as well as Amazon Linux are not affected.
**Protecting against Supply Chain Attacks**
Although the backdoor was introduced into a package found in Linux distributions and MacOS systems, it again raises the concern of supply-chain attacks. Ensuring the integrity of your build pipeline and all the dependencies you use in your projects is crucial. Jit orchestrates several tools to help you automate these daunting tasks, both in terms of GitHub misconfigurations and dependency checks (SCA).
**The Future of Open Source**
This fluke discovery outlines the underlying risks in open source libraries that have a single maintainer who’s overwhelmed and under constant pressure. It is also a cry for help for the whole community. While some big corporations may derive commercial benefits from the
[open source world](https://thenewstack.io/making-europes-romantic-open-source-world-more-practical/), they usually contribute by donating instead of allowing their employees to actively help fix these projects during their work hours. On the other hand, there is also a need to sponsor underpaid maintainers — platforms like GitHub Sponsors and Open Collective can help here.
Initiatives from nonprofits such as the Linux Foundation and Apache Foundation are a good way to provide governance support, legal assistance and financial support to help
[secure the longevity of important projects](https://thenewstack.io/tracy-ragan-my-favorite-open-source-security-projects/). Being backed by a whole community will certainly relieve the stress of single maintainers. What happened here should be a warning sign that it is time to act and dive into the daily struggles of [open source maintainers](https://thenewstack.io/bots-emojis-and-open-source-maintainers-how-people-and-tools-make-the-difference/). It is not too late to act. Now is the time to rise as a community.
## TL;DR and How to Get Informed and Protected
Due to the explosive nature of this backdoor, many folks in the community are tracking it closely and reporting on it in real time. A good place to get started that provides lots of details and nearly up-to-the-minute updates is
[this post](https://boehs.org/node/everything-i-know-about-the-xz-backdoor?utm_source=tldrwebdev), which dives into the timeline and a little OSINT (open source intelligence) on tracking the malicious entity that introduced this backdoor.
Another good reference about the risks and available information on the xz-utils backdoor is this
[FAQ post](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27), which share details, suggestions for recommended security measures to implement and discussions the community can participate in for different OSS projects that were affected. This was another wake-up call to the entire open source industry, reminding us of the human toil under the hood that enables our excellent OSS ecosystem to thrive, and we certainly need to revisit how we incentivize maintainers and create greater shared ownership of mission-critical and widely adopted projects. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)