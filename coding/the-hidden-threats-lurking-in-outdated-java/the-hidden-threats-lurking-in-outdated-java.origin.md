# The Hidden Threats Lurking in Outdated Java
![Featued image for: The Hidden Threats Lurking in Outdated Java](https://cdn.thenewstack.io/media/2024/07/2606d764-java-1024x576.jpg)
Keeping your enterprise systems as secure as possible should be obvious, shouldn’t it? Unfortunately, with so many security aspects to consider, this is often neglected in some of the most important places.

The [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) runtime, for example.

Until 2019, keeping your JDK updated with the latest security patches was straightforward and did not come with a direct cost. When Sun Microsystems released Java, you could download the Java Development Kit for free, unless you were using it for some kind of embedded or [single-use application](https://www.oracle.com/java/technologies/javase-embedded/embedded-faq.html) (like a ticket kiosk that uses an embedded PC). Even when a new version of Java was released — which happened only every two, three or even four years — there was a considerable overlap with continued free updates to allow a smooth transition.

Having acquired Sun in 2010, Oracle continued to deliver its JDK in the same way until 2019. Its first change was to move to a time-based, rather than a feature-based, release schedule. Now, like clockwork, we have two new versions of Java each year: one in March and one in September.

This faster release cadence led to the introduction of long-term support (LTS) releases of the Oracle JDK, since providing extended maintenance and support for all releases was not practical. Initially, there was a new LTS release every three years, but that has now been shortened to two.

The current LTS releases are JDK 8, 11, 17 and 21. Older open source versions of Java, JDK 6 and 7, are no longer supported (even commercially) by Oracle.

How important are [security updates](https://thenewstack.io/the-great-security-debate-is-patching-useless/)? After all, Java is now nearly 30 years old; haven’t we eliminated all the vulnerabilities by now? Sadly not, and realistically, that will never happen. OpenJDK contains 7.5 million lines of code and relies on many external libraries, all of which can be subject to undiscovered vulnerabilities.

Let’s put this into context with some hard data.

Suppose you are running your application on JDK 6 and haven’t updated it since the end of free public updates from Oracle (April 2013). In this case, your application is exposed to a total of 425 vulnerabilities, 89 of which are critical.

The ability to [update your systems](https://thenewstack.io/security-of-software-update-systems-in-2023/) promptly is of critical importance.

Oracle provides two versions of each update, referred to as the Critical Patch Update (CPU) and Patch Set Update (PSU). The CPU contains only security-related changes; the PSU contains security-related changes, bug fixes, performance improvements and any other code changes. The difference in size is significant. A large CPU will contain maybe 15 changes but typically less than 10. A PSU, on the other hand, can contain anywhere from 200 to 400 changes.

The more changes included in an update, the more the chance that one of those changes may affect an application’s functionality. With just three months between updates, only so much testing of applications can be done. This leads to situations where a PSU has a significant impact. For example, the July 2022 PSU included a fix that prevented Hadoop Cluster-, Solr- and Lucene-based applications from working correctly.

Since Oracle changed its distributions and licensing, there have been 22 updates. Of these, six PSUs required a modification and new release to address a regression that had been introduced. The time to create the new update has varied from just under two weeks to over five weeks. At no time have any of the CPUs been affected like this. Access to a CPU is essential to maintain the maximum level of security for your applications.

Since all free binary distributions of OpenJDK only provide the PSU version, some users may consider a couple of weeks before being able to deploy as an acceptable risk.

This is very dangerous.

When an update to the JDK is released, all vulnerabilities addressed are disclosed in the release notes. Bad actors now have information enabling them to try and find ways to exploit unpatched applications.

Let’s use the example of a commonly used Java library, Apache Struts, to show how much of a danger this could be.

On Dec. 7, 2023, details of a vulnerability in Struts were published. The Common Vulnerability Scoring System (CVSS) for this was 9.8, making it a critical vulnerability. In addition, it had the potential to allow [remote code execution](https://thenewstack.io/github-actions-design-flaw-leaves-security-hole-for-remote-code-execution/) (RCE), a much worse kind of vulnerability than one that could be used for denial of service (DOS).

Only four days later, proof-of-concept code was published showing how this exploit could be used. And within 24 hours of this code release, attacks were observed on unpatched systems. Waiting two weeks, or much longer, before a usable Java update is available will leave your applications exposed. Is that a risk you’re prepared to take?

Azul’s Platform Core, which provides TCK (Technology Compatibility Kit)-tested Zulu builds of OpenJDK includes both the CPU and PSU each quarter. It also still supports JDK 6 and 7. This provides you with the maximum security and stability for your mission-critical enterprise Java applications without forcing you to upgrade legacy applications to a newer release.

[Learn more about Java and OpenJDK](https://www.azul.com/products/core/).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)