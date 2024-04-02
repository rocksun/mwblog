# Timeline of the xz open source attack
Posted on Monday, April 1, 2024.
Over a period of over two years, an attacker using the name “Jia Tan” worked as a diligent, effective contributor to the xz compression library, eventually being granted commit access and maintainership. Using that access, they installed a very subtle, carefully hidden backdoor into liblzma, a part of xz that also happens to be a dependency of OpenSSH sshd on Debian, Ubuntu, Fedora, and other systemd-based Linux systems. That backdoor watches for the attacker sending hidden commands at the start of an SSH session, giving the attacker the ability to run an arbitrary command on the target system without logging in: unauthenticated, targeted remote code execution.
The attack was
[publicly disclosed on March 29, 2024](https://www.openwall.com/lists/oss-security/2024/03/29/4) and
appears to be the first serious known supply chain attack on widely used open source software.
It marks a watershed moment in open source supply chain security, for better or worse.
This post is a detailed timeline that I have constructed of the social engineering aspect of the attack, which appears to date back to late 2021. Key events have bold times.
Corrections or additions welcome on
[Bluesky](https://bsky.app/profile/swtch.com/post/3kp4my7wdom2q), [Mastodon](https://hachyderm.io/@rsc/112199506755478946), or
## Prologue
**2005–2008**: [Lasse Collin, with help from others](https://github.com/kobolabs/liblzma/blob/87b7682ce4b1c849504e2b3641cebaad62aaef87/doc/history.txt), designs the .xz file format using the LZMA compression algorithm, which compresses files to about 70% of what gzip did [1]. Over time this format becomes widely used for compressing tar files, Linux kernel images, and many other uses.
## Jia Tan arrives on scene, with supporting cast
**2021-10-29**: Jia Tan sends [first, innocuous patch](https://www.mail-archive.com/xz-devel@tukaani.org/msg00512.html) to the xz-devel mailing list, adding “.editorconfig” file.
**2021-11-29**: Jia Tan sends [second innocuous patch](https://www.mail-archive.com/xz-devel@tukaani.org/msg00519.html) to the xz-devel mailing list, fixing an apparent reproducible build problem. More patches that seem (even in retrospect) to be fine follow.
**2022-04-19**: Jia Tan sends [yet another innocuous patch](https://www.mail-archive.com/xz-devel@tukaani.org/msg00553.html) to the xz-devel mailing list.
**2022-04-22**: “Jigar Kumar” sends [first of a few emails](https://www.mail-archive.com/xz-devel@tukaani.org/msg00557.html) complaining about Jia Tan’s patch not landing. (“Patches spend years on this mailing list. There is no reason to think anything is coming soon.”) At this point, Lasse Collin has already landed four of Jia Tan’s patches, marked by “Thanks to Jia Tan” in the commit message.
**2022-05-19**: “Dennis Ens” sends [mail to xz-devel](https://www.mail-archive.com/xz-devel@tukaani.org/msg00562.html) asking if XZ for Java is maintained.
**2022-05-19**: Lasse Collin [replies](https://www.mail-archive.com/xz-devel@tukaani.org/msg00563.html) apologizing for slowness and adds “Jia Tan has helped me off-list with XZ Utils and he might have a bigger role in the future at least with XZ Utils. It's clear that my resources are too limited (thus the many emails waiting for replies) so something has to change in the long term.”
**2022-05-27**: Jigar Kumar sends [pressure email](https://www.mail-archive.com/xz-devel@tukaani.org/msg00565.html) to patch thread. “Over 1 month and no closer to being merged. Not a surprise.”
**2022-06-07**: Jigar Kumar sends [pressure email](https://www.mail-archive.com/xz-devel@tukaani.org/msg00566.html) to Java thread. “Progress will not happen until there is new maintainer. XZ for C has sparse commit log too. Dennis you are better off waiting until new maintainer happens or fork yourself. Submitting patches here has no purpose these days. The current maintainer lost interest or doesn't care to maintain anymore. It is sad to see for a repo like this.”
**2022-06-08**: Lasse Collin [pushes back](https://www.mail-archive.com/xz-devel@tukaani.org/msg00567.html). “I haven't lost interest but my ability to care has been fairly limited mostly due to longterm mental health issues but also due to some other things. Recently I've worked off-list a bit with Jia Tan on XZ Utils and perhaps he will have a bigger role in the future, we'll see. It's also good to keep in mind that this is an unpaid hobby project.”
**2022-06-10**: Lasse Collin merges [first commit with Jia Tan as author in git metadata](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=aa75c5563a760aea3aa23d997d519e702e82726b) (“Tests: Created tests for hardware functions”).
**2022-06-14**: Jugar Kumar sends [pressure email](https://www.mail-archive.com/xz-devel@tukaani.org/msg00568.html). “With your current rate, I very doubt to see 5.4.0 release this year. The only progress since april has been small changes to test code. You ignore the many patches bit rotting away on this mailing list. Right now you choke your repo. Why wait until 5.4.0 to change maintainer? Why delay what your repo needs?”
**2022-06-21**: Dennis Ens sends [pressure email](https://www.mail-archive.com/xz-devel@tukaani.org/msg00569.html). “I am sorry about your mental health issues, but its important to be aware of your own limits. I get that this is a hobby project for all contributors, but the community desires more. Why not pass on maintainership for XZ for C so you can give XZ for Java more attention? Or pass on XZ for Java to someone else to focus on XZ for C? Trying to maintain both means that neither are maintained well.”
**2022-06-21**: Lasse Collin [replies](https://www.mail-archive.com/xz-devel@tukaani.org/msg00571.html): “As I have hinted in earlier emails, Jia Tan may have a bigger role in the project in the future. He has been helping a lot off-list and is practically a co-maintainer already. :-) I know that not much has happened in the git repository yet but things happen in small steps. In any case some change in maintainership is already in progress at least for XZ Utils.”
**2022-06-22**: Jigar Kumar sends [pressure email](https://www.mail-archive.com/xz-devel@tukaani.org/msg00570.html) to C patch thread. “Is there any progress on this? Jia I see you have recent commits. Why can't you commit this yourself?”
## Jia Tan becomes maintainer
At this point Lasse seems to have started working even more closely with Jia Tan. Evan Boehs
[observes](https://boehs.org/node/everything-i-know-about-the-xz-backdoor) that Jigar Kumar and Dennis Ens both had nameNNN@mailhost email addresses that never appeared elsewhere on the internet, nor again in xz-devel. It seems likely that they were fakes created to push Lasse to give Jia more control. It worked. Over the next few months, Jia started replying to threads on xz-devel authoritatively about the upcoming 5.4.0 release.
**2022-09-27**: Jia Tan gives [release summary](https://www.mail-archive.com/xz-devel@tukaani.org/msg00593.html) for 5.4.0. (“The 5.4.0 release that will contain the multi threaded decoder is planned for December. The list of open issues related to 5..4.0 [sic] in general that I am tracking are...”)
**2022-11-30**: Lasse Collin [changes bug report email](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=764955e2d4f2a5e8d6d6fec63af694f799e050e7) from his personal address to an alias that goes to him and Jia Tan, notes in README that “the project maintainers Lasse Collin and Jia Tan can be reached via [xz@tukaani.org](mailto:xz@tukaani.org)”.
**2022-12-30**: Jia Tan merges [first commit directly into the xz repo](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=8ace358d65059152d9a1f43f4770170d29d35754) (“CMake: Update .gitignore for CMake artifacts from in source build”). At this point we know they have commit access.
**2023-01-11**: Lasse Collin [tags and builds his final release](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=18b845e69752c975dfeda418ec00eda22605c2ee), v5.4.1.
**2023-03-18**: Jia Tan [tags and builds their first release](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=6ca8046ecbc7a1c81ee08f544bfd1414819fb2e8), v5.4.2.
**2023-03-20**: Jia Tan [updates Google oss-fuzz configuration](https://github.com/google/oss-fuzz/commit/6403e93344476972e908ce17e8244f5c2b957dfd) to send bugs to them.
**2023-06-22**: Hans Jansen sends a pair of patches, merged by Lasse Collin, that use the “ [GNU indirect function](https://maskray.me/blog/2021-01-18-gnu-indirect-function)” feature to select a fast CRC function at startup time. This change is important because it provides a hook by which the backdoor code can modify the global function tables before they are remapped read-only. While this change could be an innocent performance optimization by itself, Hans Jansen returns in 2024 to promote the backdoored xz and otherwise does not exist on the internet.
**2023-07-07**: Jia Tan [disables ifunc support during oss-fuzz builds](https://github.com/google/oss-fuzz/commit/d2e42b2e489eac6fe6268e381b7db151f4c892c5), claiming ifunc is incompatible with address sanitizer. This may well be innocuous on its own, although it is also more groundwork for using ifunc later.
**2024-01-19**: Jia Tan [moves web site to GitHub pages](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=c26812c5b2c8a2a47f43214afe6b0b840c73e4f5), giving them control over the XZ Utils web page. Lasse Collin presumably created the DNS records for the xz.tukaani.org subdomain that points to GitHub pages. After the attack was discovered, Lasse Collin deleted this DNS record to move back to [tukaani.org](tukaani.org), which he controls.
## Attack begins
**2024-02-23**: Jia Tan [merges hidden backdoor binary code](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=cf44e4b7f5dfdbf8c78aef377c10f71e274f63c0) well hidden inside some binary test input files. The associated README claims “This directory contains bunch of files to test handling of .xz, .lzma (LZMA_Alone), and .lz (lzip) files in decoder implementations. Many of the files have been created by hand with a hex editor, thus there is no better "source code" than the files themselves.”
**2024-02-24**: Jia Tan [tags and builds v5.6.0](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=2d7d862e3ffa8cec4fd3fdffcd84e984a17aa429) and publishes an xz-5.6.0.tar.gz distribution with an extra, malicious build-to-host.m4 that adds the backdoor when building a deb/rpm package. This m4 file is not present in the source repository, but many other legitimate ones are added during package as well, so it’s not suspicious by itself. But the script has been modified from the usual copy to add the backdoor. See my [xz script walkthrough post](xz-script) for more.
**2024-02-24**: Gentoo [starts seeing crashes in 5.6.0](https://bugs.gentoo.org/925415). This seems to be an actual ifunc bug, rather than a bug in the hidden backdoor, since this is the first xz with Hans Jansen’s ifunc changes.
**2024-02-26**: Debian [adds xz-utils 5.6.0-0.1](https://tracker.debian.org/news/1506761/accepted-xz-utils-560-01-source-into-unstable/) to unstable.
**2024-02-28**: Debian [adds xz-utils 5.6.0-0.2](https://tracker.debian.org/news/1507917/accepted-xz-utils-560-02-source-into-unstable/) to unstable.
**2024-02-29**: On GitHub, @teknoraver [sends pull request](https://github.com/systemd/systemd/pull/31550) to stop linking liblzma into libsystemd. It appears that this would have defeated the attack. [Kevin Beaumont speculates](https://doublepulsar.com/inside-the-failed-attempt-to-backdoor-ssh-globally-that-got-caught-by-chance-bbfe628fafdd) that knowing this was on the way may have accelerated the attacker’s schedule. It is unclear whether any earlier discussions exist that would have tipped them off.
**2024-02-28**: Jia Tan [breaks landlock detection](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=a100f9111c8cc7f5b5f0e4a5e8af3de7161c7975) in configure script by adding a subtle typo in the C program used to check for [landlock support](https://docs.kernel.org/userspace-api/landlock.html). The configure script tries to build and run the C program to check for landlock support, but since the C program has a syntax error, it will never build and run, and the script will always decide there is no landlock support. Lasse Collin is listed as the committer; he may have missed the subtle type, or the author may be forged. Probably the former, since Jia Tan did not bother to forge committer on his many other changes. This patch seems to be setting up for something besides the sshd change, since landlock support is part of the xz command and not liblzma. Exactly what is unclear.
**2024-03-04**: RedHat distributions [start seeing Valgrind errors](https://bugzilla.redhat.com/show_bug.cgi?id=2267598) in liblzma’s
_get_cpuid (the entry to the backdoor).
**2024-03-05**: The [libsystemd PR is merged](https://github.com/systemd/systemd/commit/3fc72d54132151c131301fc7954e0b44cdd3c860) to remove liblzma.
**2024-03-05**: Debian [adds xz-utils 5.6.0-0.2](https://tracker.debian.org/news/1509743/xz-utils-560-02-migrated-to-testing/) to testing.
**2024-03-05**: Jia Tan commits [two ifunc](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=ed957d39426695e948b06de0ed952a2fbbe84bd1) [bug fixes](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=4e1c97052b5f14f4d6dda99d12cbbd01e66e3712). These seem to be real fixes for the actual ifunc bug. One commit links to the Gentoo bug and also typos an [upstream GCC bug](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=114115).
**2024-03-08**: Jia Tan [commits purported Valgrind fix](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=82ecc538193b380a21622aea02b0ba078e7ade92). This is a misdirection, but an effective one.
**2024-03-09**: Jia Tan [commits updated backdoor files](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=74b138d2a6529f2c07729d7c77b1725a8e8b16f1). This is the actual Valgrind fix, changing the two test files containing the attack code. “The original files were generated with random local to my machine. To better reproduce these files in the future, a constant seed was used to recreate these files.”
**2024-03-09**: Jia Tan [tags and build v5.6.1](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=fd1b975b7851e081ed6e5cf63df946cd5cbdbb94) and publishes xz 5.6.1 distribution, containing new backdoor. To date I have not seen any analysis of how the old and new backdoors differ.
**2024-03-25**: Hans Jansen is back (!), [filing a Debian bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067708) to get xz-utils updated to 5.6.1. Like in the 2022 pressure campaign, more name###@mailhost addresses that don’t otherwise exist on the internet show up to advocate for it.
**2024-03-28**: Jia Tan [files an Ubuntu bug](https://bugs.launchpad.net/ubuntu/+source/xz-utils/+bug/2059417) to get xz-utils updated to 5.6.1 from Debian.
## Attack detected
**2024-03-28**: Andres Freund discovers bug, privately notifies Debian and distros@openwall. RedHat assigns CVE-2024-3094.
**2024-03-28**: Debian [rolls back 5.6.1](https://tracker.debian.org/news/1515519/accepted-xz-utils-561really545-1-source-into-unstable/), introducing 5.6.1+really5.4.5-1.
**2024-03-29**: Andres Freund [posts backdoor warning](https://www.openwall.com/lists/oss-security/2024/03/29/4) to public oss-security@openwall list, saying he found it “over the last weeks”.
**2024-03-29**: RedHat [announces that the backdoored xz shipped](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users) in Fedora Rawhide and Fedora Linux 40 beta.
**2024-03-30**: Debian [shut down builds](https://fulda.social/@Ganneff/112184975950858403) to rebuild their build machines using Debian stable (in case the malware xz escaped their sandbox?).
## Further Reading
-
Evan Boehs,
[Everything I know about the XZ backdoor](https://boehs.org/node/everything-i-know-about-the-xz-backdoor)(2024-03-29).
-
Filippo Valsorda,
[Bluesky](https://bsky.app/profile/filippo.abyssdomain.expert/post/3kowjkx2njy2b)re backdoor operation (2024-03-30).
-
Michał Zalewski,
[Techies vs spies: the xz backdoor debate](https://lcamtuf.substack.com/p/technologist-vs-spy-the-xz-backdoor)(2024-03-30).
-
Michał Zalewski,
[OSS backdoors: the folly of the easy fix](https://lcamtuf.substack.com/p/oss-backdoors-the-allure-of-the-easy)(2024-03-31).
-
Connor Tumbleson,
[Watching xz unfold from afar](https://connortumbleson.com/2024/03/31/watching-xz-unfold-from-afar/)(2024-03-31).
-
nugxperience,
-
birchb0y,
-
Dan Feidt,
['xz utils' Software Backdoor Uncovered in Years-Long Hacking Plot](https://unicornriot.ninja/2024/xz-utils-software-backdoor-uncovered-in-years-long-hacking-plot/)(2024-03-30)
-
smx-smz,
[[WIP] XZ Backdoor Analysis and symbol mapping](https://gist.github.com/smx-smx/a6112d54777845d389bd7126d6e9f504)
-
Dan Goodin,
[What we know about the xz Utils backdoor that almost infected the world](https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world/)(2024-04-01)
-
Akamai Security Intelligence Group,
[XZ Utils Backdoor — Everything You Need to Know, and What You Can Do](https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know)(2024-04-01)
-
Kevin Beaumont,
[Inside the failed attempt to backdoor SSH globally — that got caught by chance](https://doublepulsar.com/inside-the-failed-attempt-to-backdoor-ssh-globally-that-got-caught-by-chance-bbfe628fafdd)(2024-03-31)
-
amlweems,
[xzbot: notes, honeypot, and exploit demo for the xz backdoor](https://github.com/amlweems/xzbot)(2024-04-01)
-
Rhea's Substack,
[XZ Backdoor: Times, damned times, and scams](https://rheaeve.substack.com/p/xz-backdoor-times-damned-times-and)(2024-03-30)