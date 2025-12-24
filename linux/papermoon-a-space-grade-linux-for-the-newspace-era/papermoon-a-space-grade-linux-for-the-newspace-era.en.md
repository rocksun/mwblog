TOKYO — When I worked for NASA in the 1980s, every satellite and spaceship that went into orbit ran one-off, hand-coded, semi-proprietary programs. This approach was painful, expensive, and sometimes disastrous, as with the loss of the Mars Climate Orbiter in 1999 due to a software blunder.

Things have changed. In his “Space Grade Linux” keynote at the [Open Source Summit Japan](https://events.linuxfoundation.org/open-source-summit-japan/) conference, [Ramón Roche](https://www.linkedin.com/in/ramon-roche), a longtime robotics developer and general manager of the [Dronecode Foundation](https://dronecode.org/), told how [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) and [open source software](https://thenewstack.io/nasas-thirst-for-open-source-software-and-for-open-science/) are becoming the default for every launch — replacing the bespoke, one-off programs of the past.

This change has been coming for a while. By 2013, the International Space Station (ISS) switched out its Windows laptops for Debian Linux machines for mission-critical work. Today, [SpaceX’s](https://thenewstack.io/elon-musk-at-vivatech-spacex-on-mars-in-7-to-8-years/) workhorse rocket, Falcon 9, and its Dragon spacecraft both run Linux. Roche also noted that the first aircraft on another planet, the Ingenuity helicopter on Mars, flew with Linux. Heck, a developer recently managed to run open source Doomon, a European Space Agency (ESA) satellite.

But Roche stressed that one thing has been lacking. A common space Linux platform so that space companies can stop “competing on the plumbing” and start sharing core software infrastructure.

## The NewSpace Challenge: Cheaper Launches, More Complex Software

The economic backdrop is a classic space‑tech storyline: It’s cheaper than ever to access orbit, but software complexity and safety requirements keep rising.

“You can launch a satellite for the cost of a nice car,” Roche said, noting that the cost per kilogram is “quickly approaching less than $100 per kilo to ship payload to space,” which in turn fuels a flywheel of more launches, more applications and even “data centers in space.”

What doesn’t scale, he argued, is the way many missions are still engineered as bespoke, one‑off software stacks. “It’s 2025 right now, and we’re still in a phase like 1969,” where missions are one‑off and expensive. That model “was fine back when launches cost millions of dollars, he noted, “but no longer fits the economics of NewSpace.

## Why Open Source Is the Future for Space Missions

Space’s harsh realities — radiation‑induced “single set events” that reboot systems without warning, communication delays “measured in minutes,” and the impossibility of “SSH there” to fix a broken satellite — are pushing developers toward robust, well-understood, community‑maintained open source instead of proprietary stacks.

The problem, as Roche sees it, is not whether Linux is the right base layer for autonomous systems, but how it is used.

A survey of practitioners identified [Yocto](https://www.yoctoproject.org/) as the “clear winner” among embedded Linux distributions. However, we still have a fragmented landscape of teams “building their own version of Linux from scratch” with “no shared foundational layer,” Roche said.

“Everyone agrees that Linux is the answer,” he said. “But nobody agrees on which Linux.”

## Learning From the Drone Industry’s Open Source Success

That fragmentation looks familiar to Roche, who has spent more than a decade in the drone ecosystem around [PX4](https://px4.io/) and related projects.

“I was there in 2010 when the drone industry looked very similar. Everyone was building on their own stacks, nobody talking to anyone else,” he recalled, describing “years of complicated effort” and “every company reinventing the wheel, incompatible protocols” before the community decided to “stop competing on the plumbing and start competing on innovation.”

In his telling, that shift enabled open source to power “the majority of commercial and professional drones worldwide,” from agriculture and inspection to mapping, search‑and‑rescue, and even defense.

## Introducing Papermoon: A Proposed Space-Grade Linux Stack

The answer is Papermoon, a proposed space‑grade Linux stack. Roche described it as “an open source project and a new foundation” built around Linux as the “autoplay, middle layer architecture,” licensed under MIT, with a Developer Certificate of Origin rather than contribution agreements “friction.”

The goal is a layered stack:

* Mission-specific user‑space frameworks at the top.
* A managed board‑support and chair infrastructure layer in the middle.
* Yocto/OpenEmbedded as the build system underneath, providing reproducible images, long‑term maintenance and cross‑compilation.

On the hardware side, early targets include RISC‑V development boards “like a Raspberry Pi, same price point,” Roche said, alongside space‑designed platforms such as [Microchip’s radiation‑tolerant MPSoC](https://www.microchip.com/en-us/products/fpgas-and-plds/radiation-tolerant-fpgas), with continuous integration already running “on every commit” and images booting on actual boards.

“This is what you’re getting,” Roche told the audience, arguing that teams who adopt Papermoon are “not starting from zero”— the base layer, build system, and “safety‑aware configuration” represent “months that you don’t need to spend reinventing if you collaborate with us.”

## Building a Safety-Critical System With the ELISA Initiative

To tackle safety and certification head-on, the project has been incubating inside the Linux Foundation’s [Enabling Linux in Safety Applications (ELISA) initiative](https://elisa.tech/).  Roche highlighted ELISA vice president [Kate Stewart’](https://www.linkedin.com/in/katestewartaustin/)s work as emblematic of the community Papermoon wants to align with.

“If you’re building safety‑critical systems that run on Linux, there’s no one better to learn from,” he said. “ELISA has been working on this problem since 2019: How do you use Linux in systems where failure means loss of life?”

A year ago, about 30 people met in person at NASA Goddard Space Flight Center (GSFC) — my home base when I worked for NASA — with another 40 joining virtually from more than 20 organizations, agencies, and research groups, to “decide the direction for this project,” which Roche framed as “not a maintenance‑only conversation, that’s actual, real commitment.”

## The Future Roadmap: From Incubation to a New Foundation

The next move, he said, is to “step out of the ELISA incubation and form our own foundation with neutral overheads, member‑driven, the same models that work for automotive grade Linux,” where founding members “help us shape what this becomes: the governance, the roadmap, and standards that we set.”

Roche’s pitch to developers and companies in the room was blunt: Ingenuity “proved Linux belongs in space,” but “the next mission shouldn’t start from scratch.”

“The question is, does every team after this rebuild from zero, or do we give them that foundation?” he asked, positioning Papermoon as that shared base and urging those “building for space” who recognize the pattern from drones and automotive to “come talk to us” and “help us build the foundation for the next era of space.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)