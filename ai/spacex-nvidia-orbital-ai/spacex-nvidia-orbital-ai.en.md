**SpaceX and Nvidia say they are adapting** the Vera Rubin NVL72 rack-scale AI platform for orbital use, with SpaceX targeting a first launch in the fourth quarter of 2027.

The dream of an [AI data center in space](https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/) lives on in SpaceX and Nvidia’s August 24 announcements that the platform for Low Earth Orbit (LEO) [Starmind](https://www.spacex.com/spacexai/starmind) AI satellites will be based on the [Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) chip family and architecture.

This proposed system would form [the computing core of SpaceXAI’s first-generation Starmind AI satellite](https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/#spacexai-vera-cpus) and extend Nvidia’s architecture from terrestrial AI data centers into space.

SpaceX CEO Elon Musk posted on X the same day, “SpaceX, in partnership with Nvidia, has designed a space-optimized Vera Rubin NVL72 system for launch to orbit in Q4 next year, with significant scale in 2028.”

Musk’s post came after [he said](https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Q2-2026-Earnings_Transcript-FINAL.pdf) during SpaceX’s Q2 earnings call, “Going forward, we’ve decided to build exclusively on Nvidia because we think the Vera Rubin architecture is the best architecture.” Musk continued, “This is not some sort of far-future, distant thing; we expect to start launching these next year. We think the design of the NVL72 VR computer is a much better design than, say, having a standard rack -style design. So we expect to deploy this on the ground as well as in orbit, because we think it’s going to be a radical simplification of the standard NVL72 rack. It will cost less. It will be more effective. If we’re going to put it in space, why not want to put it on the ground? I think that’s going to be pretty cool.”

On Earth, the [Vera Rubin NVL72](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) is Nvidia’s rack-scale AI design that combines 72 Rubin GPUs and 36 Vera CPUs, alongside high-speed networking components such as ConnectX-9 SuperNICs. Nvidia says SpaceXAI’s planned Starmind satellite will be based on an optimized version of that system.

> A conventional NVL72 rack assumes gravity, technicians, stable grid power, a building-scale liquid loop and frequent replacement of failed parts. Orbit removes each of these assumptions.

The idea is more ambitious than putting a conventional edge-AI accelerator aboard a spacecraft. Nvidia and SpaceXAI are proposing to bring a modified architecture used in AI data centers into orbit, while altering it for orbital operational requirements.

Getting that working in orbit, though, is easier said than done.

As [Curtis Pyke](https://www.linkedin.com/in/curtis-pyke-4b52a420/), founder of [Kingy AI](https://kingy.ai/), writes, “A conventional NVL72 rack assumes gravity, technicians, stable grid power, a building-scale liquid loop and frequent replacement of failed parts. [Orbit removes each of these assumptions.](https://kingy.ai/blog/spacex-nvidia-orbital-ai-supercomputer-2027/)“

> “Cooling is unforgiving. Space is cold, but vacuum does not carry heat away through convection.”

In particular, Pyke continues, “Cooling is unforgiving. Space is cold, but vacuum does not carry heat away through convection. Heat must travel from the chips to the radiator surfaces and then leave as infrared radiation. SpaceX says AI1 can avoid chillers, cooling towers and fans and reduce cooling overhead by an order of magnitude.”

SpaceX explains that AI1 would instead use closed-loop liquid cooling inside the spacecraft and large deployable radiators to send heat directly to space as infrared radiation. While the claimed reduction is physically plausible in principle, there’s no proof yet that these AI satellites’ cooling systems can deliver.

Another major problem that remains unaddressed is how to make the orbital rack radiation-tolerant. Making Vera Rubin NVL72 radiation-tolerant means far more than putting an ordinary NVL72 rack in a shielded satellite enclosure. It would require a system-level redesign of its GPUs, CPUs, memory, networking, power, cooling, firmware, and operations around a specified orbit and mission life.

LEO orbit is not benign. [NASA cites typical trapped-particle dose rates of 100 to 1,000 rad(Si) per year for low-inclination LEO spacecraft](https://llis.nasa.gov/lesson/824) below 500 km. That level of radiation is not an immediate death sentence for electronics, but over a multiyear mission it will cause cumulative degradation. [Radiation-qualified space hardware](https://spacenexus.us/blog/radiation-hardening-space-electronics-strategies-trade-offs) can deal with that. Commercial Off-The-Shelf (COTS) electronics are another matter. A true radiation-hardened Rubin GPU would also require design changes at the transistor and circuit levels.

Even were Nvidia to make such a chip, for a high-density AI system such as the SpaceX design, the concern isn’t simply whether one processor survives a 5- or 10-year dose. The satellite contains numerous radiation-sensitive elements, such as GPU logic, SRAM caches, register files, system memory, and memory controllers. With thousands of cores and billions of memory storage cells, the aggregate fault rate — not the behavior of an individual component — drives the design.

The most realistic near-term answer would be a radiation-tolerant, fault-managed Rubin-derived orbital system, not a fully radiation-hardened NVL72 in the traditional military-space sense. It could use selected commercial Nvidia parts, substantial shielding, ECC and data integrity mechanisms, redundant controllers and power paths, aggressive fault detection, software recovery, and reduced-performance operating modes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)