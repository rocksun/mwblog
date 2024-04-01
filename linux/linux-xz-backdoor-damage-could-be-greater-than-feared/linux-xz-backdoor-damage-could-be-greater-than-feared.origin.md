# Linux xz Backdoor Damage Could Be Greater Than Feared
![Featued image for: Linux xz Backdoor Damage Could Be Greater Than Feared](https://cdn.thenewstack.io/media/2024/03/11d74142-ren-wang-pnynuo0dt6s-unsplash-augmented-1024x683.jpg)
When your home has been broken into, you may not initially comprehend all that has been taken, or the damage that has been done. This is the state of apprehension the
[Linux community](https://thenewstack.io/Linux/) now feels with the [recently-unearthed xz backdoor](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/) security vulnerability.
“This upstream supply chain security attack is the kind of nightmare scenario that has gotten people describing it called hysterical for years,” Kubernetes Security Chairperson
[Ian Coldwater](https://www.linkedin.com/in/iancoldwater/) had [written on X](https://twitter.com/IanColdwater/status/1773797427603980393). “It’s real.”
A Microsoft engineer first detected the back door, which he traced back to a recent update to the xz compression library. The library update was a recent one, but it already found homes in the rolling and advanced “rapid” releases of some Linux distributions.
The back door takes a certain combination of conditions and dependencies to trigger. Once triggered however, an attacker could enter your system without any authentication at all.
The errant code has been quickly expunged, but now questions linger as to the potential damage this backdoor has already caused — as well as who planted this subterfuge, and what their intentions were.
Even more concerning is the possibility of other heretofore undiscovered backdoors that have been planted in this library, or have taken root in earlier versions of the library that many more servers are still using.
## If It Weren’t for One Nosey Engineer…
Thank God for engineers geeky enough to debug a slow log-in time on their
[SSH session](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/).
Microsoft Principle Software Engineer
[Andres Freund](https://github.com/anarazel) had [noticed](https://www.openwall.com/lists/oss-security/2024/03/29/4) his [remote ssh log-in](https://thenewstack.io/secure-remote-linux-server-logins-with-ssh-key-authentication/) took 500ms longer than it should have. He traced the latency to a system call that SSH made, for some reason, to the [liblzma](https://tukaani.org/) compression library, which is included with the [xz utility](https://tukaani.org/) embedded in Freund’s [Debian sid](https://wiki.debian.org/DebianUnstable) installation.
He tracked down the backdoor code in the xz utility tarball for that Debian used in the installation process — though they were not in the original GitHub source code for the library.
The extra baggage was an
[obsfucated script](https://gynvael.coldwind.pl/?lang=en&id=782) that would get executed at the end of the configuration setup for the tarballs.
Freund reported the foul tarball to Debian Security and then to the distributer’s channel. Red Hat submitted this issue as
[CVE-2024-3094](https://access.redhat.com/security/cve/CVE-2024-3094), raking it with a severity of 10.
That this injection of seemingly malicious code happened so far upstream in the Linux release cycle for concerned Freund.
“Given the activity over several weeks, the committer is either directly involved or there was some quite severe compromise of their system. Unfortunately the latter looks like the less likely explanation, given they communicated on various lists about the ‘fixes’ mentioned above,” he wrote.
## Who is Jia Tan?
[Red Hat ](https://www.openshift.com/try?utm_content=inline+mention)engineer [Richard WM Jones](https://rwmj.wordpress.com/) had been in contact with the apparent author of the backdoor, he [relayed](https://news.ycombinator.com/item?id=39865810) on Hacker News.
The contributor, who went by the name of Jia Tan, had been “trying to get xz 5.6.x added to Fedora 40 & 41” because of its “‘great new features’.”
![](https://cdn.thenewstack.io/media/2024/03/12d925be-jia_tan-150x150.jpg)
From Jia Tan’s GitHub account.
“He has been part of the xz project for 2 years, adding all sorts of binary test files, and to be honest with this level of sophistication I would be suspicious of even older versions of xz until proven otherwise,” Jones wrote.
It was found that the XZ Utils
[5.6.0](https://github.com/tukaani-project/xz/releases/tag/v5.6.0) and [5.6.1](https://github.com/tukaani-project/xz/releases/tag/v5.6.1) release tarballs that contain the backdoor. Both were created and signed by Jia Tan ( [JiaT75](https://github.com/JiaT75)).
Jia Tan is likely a pseudonym, noted security expert
[Michal Zalewski](https://lcamtuf.coredump.cx/), [explaining that the persona appeared apparently out of nowhere](https://lcamtuf.substack.com/p/technologist-vs-spy-the-xz-backdoor) in 2021.
With no previous activity under this handle, JiaT75 signed up for GitHub in 2021 and went to work immediately on the projects on the
[xz utilities](https://github.com/tukaani-project). The account has no identifying information beyond a gmail address.
The xz chief maintainer has Lasse Collin (
[Larhzu](https://github.com/Larhzu)), who has been with the project since its inception. He has typically signed the xz tarballs (a bundle of multiple files) for distribution. He let Tan handle these last few releases however.
How much Collin knows about Tan is not clear. Just prior to this mess, Collin logged off the Internet, in an online sabbatical, hoping on only once to
[post a short response on the project site](https://tukaani.org/xz-backdoor/).
Zaleski’s sleuthing had found that Collin in the past few years had been beleaguered by trolls
[hounding him](https://www.mail-archive.com/xz-devel@tukaani.org/msg00566.html) to step down from his post as xz administrator. ![Trolling the xz maintainer to step down.](https://cdn.thenewstack.io/media/2024/03/469e4a89-xz-troll.png)
Trolling the xz maintainer to step down.
In one message, Collin admitted the he had little time of late to keep up with the growing backlog of issues. “Something has to change in the long term,” he
[wrote](https://www.mail-archive.com/xz-devel@tukaani.org/msg00563.html), adding that he looked to Tan taking on more duties as time passed.
Zaleski suspects that JiaT75’s work, given its general high quality, is not one of a hobbyist.
“All signs point to this being a professional, for-pay operation,” perhaps even one by a foreign government, Zaleski surmised.
Other security experts seem to concur on the overall sophistication of the injected code:
“This might be the best executed supply chain attack we’ve seen described in the open, and it’s a nightmare scenario: malicious, competent, authorized upstream in a widely used library,”
[wrote](https://bsky.app/profile/filippo.abyssdomain.expert/post/3kouaom62oi2b) open source maintainer [Filippo Valsorda](https://filippo.io/) on BlueSky.
Jia Tan only had access to the xz files hosted on GitHub; Collin retains control of the website. For safety, GitHub has since disabled all the xz utility repositories, and suspended the accounts of both Tan and Collin.
## Is the xz Backdoor Planted on your Linux Server?
If you run Linux or the macOS systems you most likely have some version of the xz and the liblzma dependencies, which are needed to uncompress software packages for installation and updates.
Thus far, it is mostly rolling release and rapid update distributions that have ingested XZ Utils 5.6.0 and 5.6.1, such as Fedora Linux 40 and Fedora Rawhide and the
[Debian advanced distributions](https://lists.debian.org/debian-security-announce/2024/msg00057.html).
Ubuntu 24.04 LTS (Noble Numbat) also contained the infected files,
[which have since been removed](https://discourse.ubuntu.com/t/xz-liblzma-security-update/43714/3). Advisories were also issued by [Arch](https://archlinux.org/news/the-xz-package-has-been-backdoored/) and [openSUSE](https://lwn.net/ml/opensuse-factory/5d7acd45-7021-4c09-8c0b-6f4b8797aecd@suse.com/).
Red Hat has
[reported](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users) no versions of Red Hat Enterprise Linux have been compromised.
The backdoor appears to be triggered only through a select set of conditions: through a “remote unprivileged systems connecting to public SSH ports,” according to a
[za-utils backdoor FAQ](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27) posted by Gentoo Linux developer [Sam James](https://wiki.gentoo.org/wiki/User:Sam).
In addition to having either the 5.6.0 or 5.6.1 tarball installed, the exploit also has to be a Linux distribution running on AMD64 hardware, and uses the
[glibc](https://www.gnu.org/software/libc/) library (such as all those Debian and Red Hat-derived versions).
A combination of
[systemd](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/) and a patched *openssh* also seem to be a requirement for the backdoor.
The payload gets triggered by a running version of the
* sshd* dameon in */usr/sbin/. * The malicious code actually gets embedded into *sshd* itself, thanks to a recent *sshd *patch to support [systemd-notify](https://www.freedesktop.org/software/systemd/man/249/systemd-notify.html) allowing other services —including * liblzma* — to be alerted when *sshd* is running.
Once inside
* ssdh*, the payload then redirects sshd’s decryption function to bypass user authentication.
“Other systems may be vulnerable at this time, but we don’t know,” James wrote.
Red Hat
[warned it its users](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users) of the severity of the compromise:
“Under the right circumstances this interference could potentially enable a malicious actor to break
*sshd* authentication and gain unauthorized access to the entire system remotely.”
## How Many xz Backdoors Could There Be?
Given these conditions listed above, if you are running a server-instance of a publicly-accessible SSH, James advised that you should “
**Update RIGHT NOW NOW NOW.**”
He stressed that is known about the backdoor triggers and versions they infect is extremely limited at this point.
“While not scaremongering, it is important to be clear that at this stage, we got lucky, and there may well be other effects of the infected liblzma,” James wrote.
For one, JiaT75 could have planted other, better-hidden, backdoors into earlier versions of xz during his tenure, which goes back to at least to v5.3.1?
This would mean, of course, a
[ of Linux distros much larger pool](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/) [could be affected](https://thenewstack.io/chainguard-outdated-containers-accumulate-vulnerabilities/).
The U.S Cybersecurity and Infrastructure Security Agency (
[CISA](https://www.cisa.gov/)) is currently investigating the backdoor further, according to Red Hat.
The good news is that it could have been worse: Vanilla upstream OpenSSH isn’t affected — unless
*liblzma* is added as a dependency.
Nonetheless, OpenSUSE recommend its Tumbleweed users reinstall SSH for public-facing servers, as there can be no telling if those servers have already been compromised.
At any rate, how the backdoor got so close to so many production systems may be a cautionary tale over the state of the Internet infrastructure.
“I do however think that this should mean an end to the practice of preferring manually built upstream tarballs over pulling in git sources directly that distributions such as debian have espoused,” one commentor
[noted on LXN.net](https://lwn.net/Articles/967180/).
“It’s the one weak link where few eyes exist in an otherwise pretty reproducible pipeline and it was really only a question of time until someone took advantage of it.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)