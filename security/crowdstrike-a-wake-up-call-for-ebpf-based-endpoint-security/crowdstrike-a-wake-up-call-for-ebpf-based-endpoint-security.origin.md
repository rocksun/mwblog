# CrowdStrike: A Wake-Up Call for eBPF-Based Endpoint Security
![Featued image for: CrowdStrike: A Wake-Up Call for eBPF-Based Endpoint Security](https://cdn.thenewstack.io/media/2024/07/a07f281b-screenshot-2024-07-30-at-10.32.56 am-1024x573.png)
The recent IT outage disabled 8.5 million computers, knocking out hundreds of businesses including airlines, hospitals, retail, media, etc.

After dealing with blue screens on their system for hours, and in some cases a day or two, the [question on every industry leader’s mind](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) was: How do you future-proof your computers from Blue Fridays like these?

Let’s look at three underlying causes of adverse impact on organizations and actions they can take to [protect themselves from cybersecurity attacks](https://thenewstack.io/crowdstrike-outage-what-can-cloud-native-teach-us/) and security issues like this.

**Key Highlights: **
- The underlying causes of the outage on July 19 include highly dated architecture, inadequate testing and high market concentration.
- eBPF technology offers a safer and more resilient approach to endpoint security compared to traditional kernel drivers.
- According to experts, the IT outage was a wake-up call for implementing an advanced cybersecurity infrastructure.
**What Happened? **
CrowdStrike, a company whose security software is used in millions of PCs for cyberattack protection, recently rolled out a faulty sensor configuration update.

This led to an error in its platform Falcon’s sensor version 7.11 and above due to a [mistake in a configuration update](https://thenewstack.io/5-agile-techniques-to-help-avoid-a-crowdstrike-like-issue/) called a “channel file.” This specific file, number 291, was meant to enhance security by improving the way Falcon checks certain processes on Windows.

However, a logic flaw in the update caused Falcon to crash, which in turn led to Windows systems crashing with a blue screen of death (BSOD) due to Falcon’s close integration with the Windows kernel.

The update was in file 291 with a timestamp of 2024-07-19 0409 UTC. CrowdStrike quickly fixed the issue and released a new version at 0527 UTC, but many systems had already updated to the flawed version, causing system failures worldwide.

**The Underlying Issue Behind the IT Outage **
On the surface, it seems like a simple mistake from CrowdStrike’s end. However, this incident points at a deeper vulnerability in our digital infrastructure.

To prevent such an outage from occurring, business leaders must understand the three underlying issues that caused the outage:

**1. **** Inherent Challenges in CrowdStrike’s Highly Dated Architecture **
A failure in the deployment of a new kernel driver during the sensor’s update led to the outage. Kernel drivers are the heart of the operating system. They manage vital system resources and interact closely with hardware.

Developing kernel drivers is complex as they must interact with low-level system components and manage hardware. Even minor errors in the code can have cascading effects, leading to systemwide problems. The complexity compounds with the need to ensure compatibility across different hardware configurations and OS versions. This is why it is a big risk for third-party software like CrowdStrike to have complete access to the kernel.

Although the recent incident was due to a faulty update, we cannot say with certainty that any software with direct access to the kernel won’t be compromised. In the future, this software could be exploited by attackers to gain unauthorized access to system resources or data.

Large organizations’ risk is compounded by their need to comply with regulations and maintain control over their data. Many organizations face hefty fines for noncompliance with regulations like GDPR, which can lead to fines of up to 4% of global annual revenue. For a company like Apple, that fine could be as much as $15 billion. Such organizations cannot afford to rely on third-party SaaS deployments for their critical data due to these compliance risks. It is one of the many reasons why some large clients prefer to have an [on-premises security](https://www.accuknox.com/products/on-premise-security) solution.

### What Is the Alternative?
One promising alternative is eBPF (Extended Berkeley Packet Filter), which offers several advantages over traditional kernel drivers.

eBPF programs run in a sandboxed environment within the kernel, significantly reducing the risk of system instability or crashes compared to traditional kernel drivers.

**2. **** Sloppy Testing and Release Processes**
The recent IT outage demonstrates that we are one mistake away from chaos. In this case, the mistake was inadequate testing and release process.

Steve Cobb, chief security officer at Security Scorecard, whose systems were affected, said, “What it looks like is, potentially, the vetting or the sandboxing they do when they look at code. Maybe somehow this file was not included in that or slipped through.”

Experts emphasized the importance of phased rollout for an update. “Ideally, this would have been rolled out to a limited pool first,” John Hammond, principal security researcher at Huntress Labs, told Reuters. “That is a safer approach to avoid a big mess like this.”

If you’re using a third-party service provider, make sure it’s one that employs thorough strong testing and sandboxing practices. Make sure it offers careful code reviews and quick responses to new threats to avoid major disruptions like the recent outage.

**3. Concentration in the Market **
[Raw Reporting](https://x.com/Raw_Reporting) mentioned on X why CrowdStrike had such a global impact, pointing out that it was trusted by 298 Fortune 500 companies and 538 Fortune 100 companies, with a market in 43 of 50 U.S. states.
[Lina Khan](https://x.com/linakhanFTC/status/1814395610788929649), chair of the Federal Trade Commission tweeted on Friday: “All too often these days, a single glitch results in a systemwide outage. The incidents reveal how concentration can create fragile systems.”
Large organizations, due to their need to ensure stringent control over data and comply with global regulations, should consider diversifying their cybersecurity solutions to avoid such widespread impacts. On-premises solutions offer a way to maintain this control, as they align with many organizations’ strict internal authorization and compliance procedures.

**Why Use eBPF?**
To tackle the risks that come with traditional security tools, organizations should consider eBPF. Unlike traditional kernel modules, eBPF operates in a safer, more controlled manner.

Here’s why eBPF is a better alternative for security:

**Minimal kernel access:**eBPF runs in a sandbox within the kernel, so it’s less likely to cause system crashes or instability.**Dynamic tracing:**It offers real-time tracking of system events and performance without the heavy burden of traditional agents.**Efficient monitoring:**eBPF makes it easy to gather and process data from various system events without slowing down your endpoints.**Scalability:**Its lightweight design means you can deploy it across large networks effortlessly, making it perfect for big organizations.
By switching to eBPF-based security, you get better security, smoother system performance and less hassle compared to traditional methods.

**Stopping Attacks in Real Time**
AccuKnox’s eBPF-based [cloud native application protection platform](https://www.accuknox.com/products/cnapp) has clear benefits for organizations that have incorporated security software using traditional kernel access.

The sandboxed nature of eBPF programs ensures that even if a security issue arises, its impact is contained, reducing the risk of widespread system compromise. Unlike tools that act after an attack, AccuKnox powered by the runtime Kubernetes security engine [KubeArmor](https://kubearmor.io) stops attacks in real time.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)