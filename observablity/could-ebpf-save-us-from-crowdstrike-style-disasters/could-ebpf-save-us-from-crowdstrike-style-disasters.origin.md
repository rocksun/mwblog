# Could eBPF Save Us From CrowdStrike-Style Disasters?
![Featued image for: Could eBPF Save Us From CrowdStrike-Style Disasters?](https://cdn.thenewstack.io/media/2024/07/d386ecaf-ebpf-1024x683.png)
Brendan Gregg, [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention) Fellow and system expert, argues that eBPF can prevent future-Crowdstrike-like disasters. Others aren’t so sure.

In the aftermath of the [CrowdStrike Windows security fiasco](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/), security experts and developers alike are looking for a safer way to run low-level security programs. In a recent blog post, [Brendan Gregg](https://au.linkedin.com/in/brendangregg), a well-regarded system performance expert and Intel Fellow, suggests [we can keep computers from crashing due to bad software updates](https://www.brendangregg.com/blog/2024-07-22/no-more-blue-fridays.html), even those updates that involve kernel code,” thanks to [eBPF](https://ebpf.io/).

Now, I like eBPF — the Swiss army knife program, which [enables you to run software in a virtual machine](https://thenewstack.io/swifts-chris-lattner-on-the-possibility-of-machine-learning-enabled-compilers/) (VM) in the Linux kernel — a lot. As Thomas Graf, [Isovalent](https://isovalent.com/)‘s CTO and co-founder, said in a speech at [CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/), “By allowing sandboxed programs to run within the operating system, eBPF enables developers to create programs that add capabilities to the operating system at runtime. The [operating system](https://thenewstack.io/choosing-an-operating-system-and-container-runtime-for-your-cloud-native-stack/) then guarantees safety and execution efficiency as if natively compiled with the aid of a Just-In-Time (JIT) compiler and verification engine.

Diving deeper into security, Gregg wrote, “eBPF programs cannot crash the entire system because they are safety-checked by a software verifier and are effectively run in a sandbox. If the verifier finds any unsafe code, the program is rejected and not executed.”

He continued that [Cisco recently acquired Isovalent](https://isovalent.com/blog/post/cisco-acquires-isovalent/) and has announced a new eBPF security product: [Cisco Hypershield](https://blogs.cisco.com/security/cisco-hypershield-reimagining-security), a fabric for security enforcement and monitoring. Gregg added that “[Google](https://www.youtube.com/watch?v=N4YKcMV8iaY) and [Meta](https://lpc.events/event/17/contributions/1602/) already rely on eBPF to detect and stop bad actors in their fleets.” So, clearly, eBPF isn’t just an attractive deep-tech platform. It’s already being used in [production by major tech](https://thenewstack.io/tech-works-how-can-i-make-myself-more-productive/) players.

But, is eBPF really the answer for anyone needing commercial software that includes kernel drivers or kernel modules? Of course, [eBPF isn’t production-ready for Windows yet](https://microsoft.github.io/ebpf-for-windows/), but Gregg appears certain it won’t be too much longer. Others aren’t so sure that eBPF is the perfect security platform for either operating system.

In an e-mail interview, [Yashin Manraj](https://www.linkedin.com/in/yashinmanraj/), CEO of [Pivotal Technologies](https://pvotal.tech/), a [low-ops](https://cloudogu.com/en/glossary/lowops/) development company, told me, “Gregg’s optimistic view of eBPF’s potential to eliminate kernel crashes, while compelling, requires careful consideration. While eBPF offers a safer sandbox for running code within the kernel, it is not a magic bullet.”

Manraj listed his concerns:

- As BPF programs become more complex, the potential for unforeseen errors increases. Careful testing and thorough code review are essential to mitigate this risk, not leading to
[system crashes but specific services](https://thenewstack.io/linux-skills-manage-system-services/)going down while the rest of the system remains functional. - Since eBPF programs interact directly with the kernel, even minor errors can have cascading effects, potentially
[leading to service](https://thenewstack.io/30-of-engineer-leads-use-a-spreadsheet-as-a-service-catalog/)instability. - Like any software, eBPF programs can be vulnerable to exploits. Developers must prioritize security considerations, including input validation, memory management, and access control.
- Debugging eBPF programs can be challenging. Robust
[logging and tracing](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/)mechanisms are crucial for identifying and resolving issues.
Manraj concluded, “Ultimately, the success of eBPF in preventing kernel crashes and services from becoming unavailable hinges not only on the technology itself but also on the commitment of developers and security professionals to adopt robust coding practices and prioritize security throughout the development lifecycle.”

We’re not there yet.

Delving deeper, [Tomer Filiba](https://il.linkedin.com/in/tomerfiliba), CTO of [Sweet Security](https://www.sweet.security/), a cloud runtime security startup, warned in an e-mail interview that eBPF has its own security concerns. First, eBPF requires high privileges (CAP_SYS_ADMIN or “root”), and a program that has these privileges can also delete important [operating system files or mess up the server’s](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/) configuration.” These foul-ups may be due to bugs and not malicious intent, but they’re still a real concern.

Second, Filiba continued that since eBPF can write to userspace memory, it can mess up “normal programs.” True, this wouldn’t “crash the kernel, as a driver can, but it can cause programs to crash.” Of course, that’s better than manually rebooting [Windows systems into “safe mode” and fixing issues](https://thenewstack.io/rust-1-77-1-a-patch-release-to-fix-an-issue-with-windows/), but it will still mess up your production workloads.

Still, “Bottom line, any high privilege program can cause harm to your environment, but in terms of risk reduction, eBPF is by far superior. For instance, if your eBPF agent goes rogue, the [system will likely still be operational](https://thenewstack.io/shell-less-kubernetes-talos-systems-introduces-the-common-operating-system-interface/) enough to allow you to remove/upgrade the agent.

Is eBPF the answer to your security woes going forward? Well, it may not be the answer, especially in Windows. Still, between optimism and pessimism about eBPF, it’s obvious to me that eBPF-based security systems will be an important part of low-level security defenses and monitoring platforms.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)