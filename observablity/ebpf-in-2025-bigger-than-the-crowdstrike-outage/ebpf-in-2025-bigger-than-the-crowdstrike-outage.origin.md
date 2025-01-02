# eBPF in 2025: Bigger Than the CrowdStrike Outage
![Featued image for: eBPF in 2025: Bigger Than the CrowdStrike Outage](https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png)
The [CrowdStrike outage in July](https://thenewstack.io/could-ebpf-save-us-from-crowdstrike-style-disasters/) resulted in disruptions across industries, affecting transportation, IT operations and other sectors in the United States. This incident also brought eBPF — the Extended Berkeley Packet Filter — under intense scrutiny. eBPF was sometimes seen — wrongly — as the culprit. eBPF is also recognized as having the potential, if applied correctly, to mitigate such disasters.

As it turns out, the eBPF element in this equation, specifically the [Falcon Sensor agent for CrowdStrike’s eBPF](https://thenewstack.io/crowdstrike-a-wake-up-call-for-ebpf-based-endpoint-security/) (which bears no relation to [Falco eBPF](https://thenewstack.io/how-falco-brought-real-time-observability-to-infrastructure/)), was part of the problem but not the cause.

The incident highlighted the risks of operating or extending eBPF from the kernel, and some critics argue this approach is dangerous — while I would counter that it was not eBPF itself that failed. The real issue is how IT teams failed to test properly or even do canary updates before deploying such wide-scale updates on a massive scale that disrupted.

I also would argue that the misconfigurations, compatibility issues and general fallibility of Windows played a significant role in this major outage. This event underscores the preponderance of Windows in environments where [Linux](https://thenewstack.io/linux/) has consistently demonstrated greater reliability for servers and even workstations.

Meanwhile, this arguably unwarranted attention for eBPF also pales in comparison to its explosion in adoption and use. Not only does CrowdStrike rely on it, but it is now a matter of finding an observability, security or networking operation, tool provider, or platform provider that does not rely, at least to some extent, on eBPF.

As in, it’s no longer about “we have eBPF,” but rather “here’s what we’re offering,” which, as its adoption matures and the dust begins to settle, will bring another set of challenges — not necessarily growing pains, but new ways in which eBPF will face challenges.

“Every observability vendor is already turning to eBPF for the granular data it can provide,” said [Bill Mulligan,](https://www.linkedin.com/in/bamulligan/) a [Cilium](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) and eBPF community pollinator for Isovalent at [Cisco](http://cisco.com/?utm_content=inline+mention). “In 2025, we will see eBPF become the top technology choice for new security tools, projects and products for the unmatched visibility it provides.”

Here is what to expect in 2025.

## eBPF Becomes a Hacker Target
eBPF runs from within the kernel. But even with access, an attacker or user cannot change the Linux code in the kernel either. It is designed to allow runtimes with eBPF to run in a closed environment. In other words, it removes a potential attack vector. since bad actors cannot write or access it as they might if it were running within a container, a pod or somewhere else with shared privileges. That does not mean, however, that an attacker who has access cannot do a lot of damage from within the kernel to any connected runtime.

To address this eBPF security concern, the eBPF Verifier checks the code and grants eBPF write privileges only after verifying that the program is licensed under the GNU Public License (GPL), to help ensure its security and compatibility. Of course, nothing is entirely foolproof, but up until now, major attacks orchestrated through eBPF at the kernel level have not been reported — yet.

The more eBPF’s use expands, the greater the volume of opportunities to gain access to such an attractive funnel as eBPF connections. Exacerbating the risk, complex eBPF tools and platforms will potentially overwhelm the kernel, said [Ben Hirschberg,](https://il.linkedin.com/in/ben-hirschberg-66141890) CTO and co-founder of [ARMO](https://www.armosec.io/).

“In 2025, we may see a surge in sophisticated eBPF applications for observability, security and networking. However, the kernel’s verifier, which ensures the safety and efficiency of eBPF programs, might struggle to handle these complex scripts,” Hirschberg said. “This could lead to performance bottlenecks and increased latency. To mitigate these challenges, the community will need to enhance the eBPF verifier and develop best practices for writing efficient eBPF programs.”

Indeed, any system that has privileges to automate network and kernel level changes is going to be a huge target for adversaries, according to [Jason Soroko,](https://ca.linkedin.com/in/jason-soroko-19b41920) senior fellow at [Sectigo](https://www.sectigo.com/), a provider of comprehensive certificate life cycle management.

“I predict that in 2025, you will see widespread adoption of Linux eBPF; however, novel forms of attacks against it will continue to be developed,” Soroko said. “We will witness a classic arms race to attack and defend it.”

## Organizations Deal with a ‘Firehose’ of eBPF Data
eBPF has the ability to monitor and scrape data anywhere the kernel is connected to the network, wherever data and applications reside. But as its adoption grows and organizations increasingly rely on it, this means, at least in theory, they could scrape every data point or telemetry data produced. This could turn into a firehose of information, making an analogy to algae look more like opening a Pandora’s box of data that no organization, large or small, can effectively manage.

This issue has become increasingly prominent in the realm of data management. Resources such as [OpenTelemetry](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/) can be used to help contextualize the data before observability solutions are fully implemented. OpenTelemetry plays a key role in organizing and reducing the overwhelming influx of data generated by eBPF.

However, the right tools and platforms must take increasingly nuanced approaches. Their methods will differ based on the specific needs of the organizations using them, ensuring the balance between data collection and manageability.

“The level of data that eBPF can generate is obscene,” Mulligan said. “In 2025, we will begin to see the limitations of applying eBPF blindly and start to realize the benefits of using smarter sensors and filtering data to make sure that eBPF can continue to be laser-focused on finding the needle in the haystack.”

eBPF tools and platforms will need to also be more attuned to specific use cases to properly help solve problems in 2025. Many organizations and individuals today use Linux and the Linux kernel with a “one-size-fits-all” approach as, in general, this process has been good enough — but “like anything in life, good enough isn’t the best,” said [Tomas Hruby,](https://www.linkedin.com/in/tomas-hruby-9552225/?originalSubdomain=ca) software engineer at [Tigera](https://tigera.io/?utm_content=inline+mention).

With eBPF, users can introduce modifications to fit their specific needs, Hruby said: “Enterprise technology and Big Tech companies alike use eBPF, and in 2025, we will see broader adoption as organizations better understand its benefits and unique ability to enable security and performance to co-exist.”

## LLMs Will Need More Monitoring. eBPF Can Help
Many organizations are just starting to wake up to the security, networking and observability issues and challenges associated with AI/machine learning and [large language model (LLM)](https://thenewstack.io/llm/) monitoring through eBPF. As it turns out, eBPF is especially well-configured not only for AI/ML applications and LLMs but also for the GPUs on which they run.

As more organizations take advantage of eBPF’s capabilities for profiling GPUs to optimize AI processing, eBPF is set to “revolutionize” GPU profiling, particularly for AI processing,” said ARMO’s [Amit Schendel,](https://il.linkedin.com/in/amit-schendel) a senior security researcher.

Leveraging eBPF, developers can capture detailed telemetry from GPU operations, such as CUDA calls, kernel launches and memory allocations with minimal overhead, Schendel said. “By providing granular insights into GPU performance, eBPF will help identify bottlenecks and improve the efficiency of AI models, ultimately leading to faster and more cost-effective AI processing.”

## eBPF Use Cases Will Explode
The use of eBPF, as mentioned above, involves observability, security and networking. This means that in 2025, as different tool providers accommodate the users’ needs that eBPF can offer, there will be a convergence between security, observability and networking providers, or networking monitoring providers, or networking management providers.

An observability platform will need eBPF and might even call itself a security company as actionable insights are obtained for both security and operations. Networking, as well, will rely on observability and security with the use of eBPF platforms.

And, of course, security companies themselves will extend their observability and networking capabilities with the eBPF functionalities they offer. CrowdStrike is ostensibly a security provider, but it uses eBPF in its proprietary system with its Falcon agent. That is an example of how the tools it adopts draw from observability and networking with eBPF now more than ever.

“eBPF began its revolution in networking and later expanded into other areas like observability, security and profiling,” said Mulligan. “Because eBPF allows us to rewrite so many things better, in 2025, we will see a Cambrian explosion of use cases from faster databases, new schedulers, improved HID integrations to name a few. eBPF is coming for so many different parts of infrastructure technology.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)