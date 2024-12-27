# How Falco Brought Real-Time Observability to Infrastructure
![Featued image for: How Falco Brought Real-Time Observability to Infrastructure](https://cdn.thenewstack.io/media/2024/12/058d04e8-kccnc-na-24_thomas_leo_luca_featured-1024x576.png)
SALT LAKE CITY — Falco was designed to solve a particular problem: How to gain observability of an application at runtime.

[Loris Degioanni](https://www.linkedin.com/in/degio/), founder and now CTO of [Sysdig](https://sysdig.com/?utm_content=inline+mention), spearheaded the creation of [Falco](https://falco.org/docs/), “a tool able to collect events that are happening at inside the kernel, the core of the system,” said [Thomas Labarussia](https://www.linkedin.com/in/thomas-labarussias/?originalSubdomain=fr)s in this On the Road episode of The New Stack Makers.
Labarussias, a senior developer advocate at Sysdig, along with two of his colleagues, joined me to talk about Falco’s evolution as an open source project and what’s ahead for it, in this episode of Makers recorded at [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) in November.

The runtime observability and security project [graduated in February](https://thenewstack.io/falco-is-a-cncf-graduate-now-what/) from the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), six years after it entered the CNCF sandbox. It collects data including pod names, name spaces and other elements of events, and then correlates them with rules.

“It’s really particularly different from the other systems, in that we are not doing analysis, static analysis, of the code base of the images we are in,” Labarussias said. “We are collecting events on the fly, like a stream, We are trying to be, as much as possible, real time.”

The tool uses a kernel module to collect events directly from the kernel, said [Luca Guerra](https://github.com/lucaguerra), senior open source engineer at Sysdig. And it uses [eBPF](https://thenewstack.io/what-is-ebpf/) technology to accomplish its tasks.

“Recently, we had great advancements with eBPF that allows us to essentially have much better safety on our kernel side, which is the closer part to the operating system, where every bug might be a bigger problem than it is in other applications,” Guerra said.

He also credited work by the Linux Foundation that has made it easier to install Falco, “without having to provide separate packages for all different kernel versions that that we might be running.”

The project maintainers want to make Falco “easy to install in every environment, whether the systems are new, whether you are using the latest and greatest technologies or some old and stable versions. We want Falco to cover everything, pretty much.”

## Falco’s Roadmap
Since Falco [moved to the CNCF incubator from the sandbox ](https://thenewstack.io/cncfs-falco-runtime-security-tool-graduates-from-the-sandbox-moves-into-incubation/)in 2020, the project maintainers’s focus has been on achieving technical maturity, said [Leonardo Grasso](https://www.linkedin.com/in/leonardograsso/?originalSubdomain=it), open source tech lead manager at Sysdig.

The only true obstacle the team encountered, he said, was that the process of finally achieving graduation lasted so long; the team wound up giving the CNCF feedback about streamlining the process going forward.

Looking ahead, Grasso said, the team is focused on two things. One is extending Falco’s core functionality. “For example, we are introducing a lot of options to customize the rules or even the format of the alerts,” he said. “But also, most importantly, we are extending the syntax that is used to describe the rules.”

Another destination on the roadmap: [Falco Talon](https://falco.org/blog/falco-talon-v0-2-0/), a “no-code, tailor-made response engine for Falco,” Guerra said.

Open source Talon was introduced in September. “The missing part in our organization or ecosystem was a reaction. So we have a lot of things for the detections, for the notifications, for the visualization, but there was a missing part and people were asking that for a long time,” he said.

“So we introduced something called Talon. And basically, you write tools like you do for Falco, but to correlate Falco alerts with actions, to fire, to remediate, to these alerts, once again, we are trying to do it in real time, in as short a time as possible.”

Check out the full episode for more on Falco’s past, present and future.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)