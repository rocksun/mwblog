# eBPF Foundation Releases Security Threat Model and Audit Reports
![Featued image for: eBPF Foundation Releases Security Threat Model and Audit Reports](https://cdn.thenewstack.io/media/2024/11/f8693200-ebpf-foundation-1024x683.png)
SALT LAKE CITY — At [KubeCon+CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) earlier this month, the [eBPF Foundation](https://ebpf.foundation/) announced it was releasing two third-party reports about the in-kernel Linux [eBPF](https://ebpf.io/) programming paradigm security: [Control Plane](https://controlplane.com/)‘s [eBPF Security Threat Model](https://www.linuxfoundation.org/hubfs/eBPF/ControlPlane%20%E2%80%94%20eBPF%20Security%20Threat%20Model.pdf) and [NCC Group](https://www.nccgroup.com/us/)‘s [eBPF Verifier Code Audit](https://www.nccgroup.com/media/4lilthtf/ncc_group_nccgroup_e015561_report_2024-11-11_v10.pdf) Since [eBPF](https://thenewstack.io/what-is-ebpf/) is at the heart of many security programs it only makes sense that we can be sure that eBPF itself is indeed secure.

In particular, these focus on the new [eBPF Security Threat Model](https://www.linuxfoundation.org/hubfs/eBPF/ControlPlane%20%E2%80%94%20eBPF%20Security%20Threat%20Model.pdf) and an accompanying audit. They provide a comprehensive overview of potential eBPF security risks -everything has security worries- and associated mitigation strategies.

After all, by its very nature, eBPF enables tools to leverage low-level Linux kernel access within a sandbox. Its safety comes from the [eBPF verifier](https://docs.kernel.org/bpf/verifier.html), Just-In-Time (JIT) compiler, and some automatic mitigations, and it also enables more granular permission grants via capabilities. This makes eBPF everyone’s first choice for deep Linux programming.

With great power, however, comes great responsibility. In eBPF’s case, this power enables possible evasion of traditional security tooling or attempts to execute attacks in a manner not identified by an eBPF security tool.

That’s not to say that traditional security measures can’t help. For example, many potential denial of service (DoS) attacks can be stopped in their tracks by blocking programs that run as CAP_SYS_ADMIN or as root.

Other familiar security recommendations include:

- Adhere to the Least Privilege Principle when granting permissions to eBPF programs.
- Ensure the integrity of eBPF tools and libraries through robust supply chain security practices.
- Keep kernel and eBPF tools updated with the latest security patches.
- Implement comprehensive monitoring and logging to detect and respond to incidents.
- Conduct regular threat modeling exercises.
- Disable unprivileged eBPF by default to minimize the attack surface.
The eBPF Security Threat Model goes into more detail on such attacks. It also offers insights into potential vulnerabilities and attack vectors that could affect eBPF implementations.

## eBPF Audit Report
Alongside the threat model, the eBPF Foundation has also made an audit report available. This document likely provides an in-depth analysis of eBPF’s current security posture and recommendations for improvement.

Specifically, the NCC Group’s review included:

- Identifying the properties the eBPF Verifier is trying to prove.
- Source code review of the main logic of the eBPF verifier, as (typically) invoked via the do_check() function in kernel/bpf/verifier.c.
- Any issue that could allow eBPF source code to bypass the constraints of the Verifier to compromise the correct operation of the eBPF Verifier, leading to standard confidentiality, integrity, and availability concerns.
While doing this review, the NCC Group A notable flaw was identified that could allow a privileged attacker to read and write arbitrary kernel memory (find_equal_scalars). This security hole has been patched.

The analysts also uncovered several other code weaknesses. There was a lack of defensive code, specifically when it came to checking array bounds and pointer validity. In addition, several overly long and complex functions were identified as candidates for refactoring. As always, the documentation should be clearer, especially regarding the verifier’s checks.

The eBPF Foundation’s proactive approach to addressing security concerns should be commended. It demonstrates a commitment to fostering a secure ecosystem for this powerful technology. Now, if only other vital software programs would follow its lead in finding and fixing security weaknesses before an attacker finds them first.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)