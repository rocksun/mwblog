PARIS —When I worked for NASA in the 1980s, I helped build a Near Space Network tracking program using [xBase](https://en.wikipedia.org/wiki/XBase) for the front-end and [Datatrieve](https://products.vmssoftware.com/datatrieve) on VAX/VMS for the backend. When completed, it manually tracked just over a thousand static network links.

That’s nothing — nothing — compared to what [Deutsche Telekom](https://www.telekom.com/) is attempting to do is create a high-performance emulation platform for simulating satellite and ground stations: vast, dynamic communication networks such as SpaceX’s [Starlink](https://www.starlink.com/fr?srsltid=AfmBOor4cOvUEpw_mRdkjxuTxCKKtsB1k094-kTKDDN5DoWfdv0OfsrG).

This is not easy, as [Andreas Florath](https://be.linkedin.com/in/andreas-florath-1252a8140) a Deutsche Telekom cloud architect and Matthias Britsch, a Deutsche Telekom senior technical expert, explained in a presentation at [OpenInfra Summit Europe 2025](https://summit2025.openinfra.org/).

The problem they face is that while the mega-constellations of Low Earth Orbit (LEO) and Medium Earth Orbit (MEO) are revolutionizing telecom, traditional network routing protocols such as Open Shortest Path First (OSPF) and Border Gateway Protocol (BGP) struggle with their dynamic topologies — not to mention the next-generation Internet protocol, [IPv6](https://thenewstack.io/why-is-ipv6-adoption-slow/).

## The Challenge of Emulating Dynamic Satellite Networks

So, the goal is to emulate large-scale, satellite mesh networks where the nodes are constantly moving and falling in and out of contact as they orbit the Earth and the world revolves underneath them. Deutsche Telekom’s answer, which is still a work in progress, is to build a scalable, container-based testbed capable of reproducing these network dynamics accurately.

The best result to date is a record-breaking Kubernetes cluster. The cluster is successfully running 2,000 pods, each with five network interfaces, for a total of 10,000 interfaces on a single worker node using [Multus](https://www.redhat.com/en/blog/demystifying-multus), the multi-network plugin from [Red Hat](https://www.openshift.com/try?utm_content=inline+mention).

As Florath told the OpenInfra audience, “We’re not aware of any other project scaling Kubernetes to this level.” This accomplishment sets a new standard for high-density container networking. It also offers vital lessons for both enterprise operators and satellite network researchers aiming to emulate large-scale, dynamic topologies.

Getting to this point was hard work. Accurate network emulation requires not just massive numbers of [containers](https://thenewstack.io/introduction-to-containers/), but complex, changing topologies reflecting real-world node movements. As Florath told the audience, “These networks have the property that the nodes are moving, they are changing their positions, and today’s routing algorithms are not designed for that.” You can say that again.

## Building a Record-Breaking Kubernetes Cluster

Indeed, in building their simulation, they found that many network building blocks were not up to the challenge. For example, the team used IPv6 for network addresses. You’d think that since [IPv6 adoption](https://thenewstack.io/mythbusting-ipv6-why-adoption-lags-and-what-will-change-it/) exceeded 25% network use globally in 2020 and all major platforms, ISPs and mobile networks have deployed it in production, we’d have worked out all the bugs. You’d be wrong.

Britsch reported that the Medicube installer, based on [OpenStack’s Ironic](https://docs.openstack.org/ironic/latest/), “created completely wrong configurations for IPv6.” Even after configuring everything correctly, the automated setup consistently produced invalid IPv6 settings, indicating deep-seated bugs in the tool’s network provisioning process.

## Unexpected Failures in IPv6 Implementation

The team also struggled to use netboot installation [over IPv6](https://thenewstack.io/kubernetes-warms-up-to-ipv6/). Certain Dell BIOS implementations lacked complete IPv6 boot support, and when present, were buggy. This caused boot stalls or failures. The toolchains required manual fixes or kernel-level workarounds to enable reliable PXE/HTTP booting with IPv6. Dell did eventually patch the BIOS, mitigating the problems.

Still, when all was said and done, they had to build custom provisioning tooling to make IPv6 work correctly for their large-scale Kubernetes deployment. Others looking to deploy high-density networking should take note.

The engineers also faced and overcame severe bottlenecks that manifested only at these unprecedented scales. Limitations included network interface and MAC address table overflows, vanishing IPs, CPU cycle misconfigurations for packet processing, and system crashes tied to BIOS update challenges. A succession of tools was tried and abandoned—commercial installations such as Canonical’s offerings faltered in documentation and reliability, while network automation and custom disk image creation offered a pathway to a stable platform.

## Overcoming Unprecedented Scaling Bottlenecks

Crucially, socket buffer sizes, kernel configuration parameters and network device address tables all needed major adjustments. The Multus plugin enabled each pod to handle multiple interfaces, but major IP address management issues appeared once scaling crossed into the thousands. This prompted the team to redesign addressing by making it local to each pod, optimizing kernel limits and switching off some hardware limitations to force MAC address handling.

As Britsch noted, the saw network interface cards limitations “that were new to me; even up-to-date cards could not handle that many MAC addresses.”

Following months of troubleshooting and incremental improvements, the setup reached a robust stability point: 2,000 pods enduring 10,000 interfaces per node for over three months. Finally, as Britsch proudly stated, “We completely automated everything: installation from scratch, fully configured stack.”

## Achieving Stability and Full Automation

However, further scale attempts revealed new, unresolved bottlenecks, indicating that while the current level is sufficient for simulation tasks, future enhancements will require solutions to additional network fidelity and packet processing lag. In short, the work’s not done yet.

Still, the team has finally managed to automate their stack deployment and is exploring integration with satellite positioning data to simulate dynamic line-of-sight networking conditions. This is a critical step toward validating next-generation routing protocols such as [IS-IS](https://networklessons.com/is-is/introduction-to-is-is) at an orbital scale.

With the rise of satellite networking and voice services such as [T-Mobile’s T-Satellite, satellite phone service](https://www.t-mobile.com/coverage/satellite-phone-service), we need these services to understand our Internet in the sky.  The engineers are talking to their bosses about open  sourcing their deployment scripts and modular boot solutions, so everyone can benefit from their work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)