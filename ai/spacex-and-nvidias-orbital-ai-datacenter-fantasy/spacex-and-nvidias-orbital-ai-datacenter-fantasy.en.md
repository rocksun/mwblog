AI data centers in space sound great, but practically speaking, they may be next to impossible.

For tech bros, it sounds great. Two of the buzziest tech giants, [SpaceX](https://www.spacex.com/) and [NVIDIA](https://www.nvidia.com/en-us/), are partnering together to bring AI data centers into space using the just-announced [Starmind AI1 satellite](https://www.spacex.com/spacexai/starmind).

These 30-meter-tall satellites with a 75-meter solar-array wingspan will contain the latest NVIDIA Vera CPUs and Rubin GPUs. These will live in a Low Earth Orbit (LEO) of about 600 kilometers. For networking, it will use Starlink’s laser links. SpaceX says the first AI1 spacecraft will perform localized AI computing in orbit and relay results to Earth via Starlink.

According to SpaceX, AI1 is designed around a compute payload drawing up to 250 kW at peak and 175 kW on average. It will be solar-powered, unlike its Earth-bound competitors, which frequently require the construction of new power plants.

![](https://cdn.thenewstack.io/media/2026/08/ba299be7-starmind-ai1-satellite-1024x425.jpeg)

Credit: SpaceX.

Starmind is not simply a conventional NVIDIA AI cluster launched into orbit. The effort hinges on integrating high-density accelerator hardware with a spacecraft platform capable of generating power, rejecting waste heat, surviving radiation, maintaining laser communications, and being produced in large quantities. None of that is easy.

Once in orbit, which will require SpaceX’s still-not-ready-for-prime-time Starship rockets to launch the estimated 2.3-metric-ton satellites, the satellites will work together.

Eventually, to reach [SpaceX’s goal of a million (that’s not a typo, that’s a million) Starmind satellites](https://www.fcc.gov/document/sb-accepts-filing-spacexs-application-orbital-data-centers), the two companies will need to design a standard model spacecraft. These will be built in SpaceX’s 11-million-square-foot manufacturing campus, [Gigasat Factory](https://www.kvue.com/article/tech/science/aerospace/spacex-plans-gigasat-factory-manufacture-ai-satellite-data-centers-bastrop-county-texas/269-bed7c221-ad0c-4171-9a7f-eeb483d9cad7), which is still under construction in Bastrop County, Texas.

This AI-in-space proposal is the most ambitious yet of SpaceX CEO Elon Musk’s dream of placing energy-intensive AI infrastructure in orbit. There, these satellites won’t need to compete for land, electrical-grid capacity, or water with increasingly contentious terrestrial data center buildouts.

However, SpaceX glosses over the technical issues of turning this vision into reality.

## Cooling space data centers

Let’s start with the biggest headache: Cooling.

Contrary to what you may think from bad science-fiction movies, the vacuum of space is not cold per se. Whether the surface of an object is hot or cold depends entirely on whether it’s facing the sun. Those on the sun side will heat up, while those away from the sun will eventually cool down toward the 3 Kelvin background of deep space.

The keyword is “eventually.” You can’t simply use convection, cooling towers, or evaporative cooling to carry away heat. The heat must radiate away as infrared radiation, and that’s a very slow process.

The physics creates a direct trade-off between computing power, radiator area, spacecraft mass, and operating temperature. A system running hundreds of kilowatts of AI hardware must reject nearly all of that power as waste heat. Liquid cooling can carry heat away from chips, but it does not eliminate the requirement for extensive radiator surfaces.

As NASA has found, “[satellites experience harsh environments in orbit](https://ntrs.nasa.gov/api/citations/20230003714/downloads/Thermal%20Design%20for%20Spaceflight.pptx.pdf),” ranging from about 393 Kelvin in full sun (248 degrees Fahrenheit) all the way down to ~3 Kelvin (-454 degrees Fahrenheit).

To cool down the Starmind satellites, each will have a deployable liquid radiator system measuring 160 square meters. What liquid? We don’t know yet. [Hugh Lewis](https://research.birmingham.ac.uk/en/persons/hugh-lewis/), a professor of astronautics at the University of Birmingham, expects [it to use ammonia](https://www.pcmag.com/news/spacexs-orbiting-data-centers-will-use-liquid-cooling-but-dont-expect-water), which is [already used on the International Space Station (ISS)](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf). Whether this will reliably scale to data-center-class AI deployments with their enormous heat remains to be seen.

## Networking limits in orbit

Another issue is its networking. The architecture depends heavily on Starlink’s optical inter-satellite links. SpaceX says AI1 satellites will use high-speed laser links to communicate with other spacecraft and send AI results to Earth via the Starlink network.

Starlink’s published technology specifications describe mini laser terminals operating at up to 25 Gbps across distances as long as 4,000 kilometers, while SpaceX cites roughly 25-millisecond latency for its customer service.

Those figures suggest a potentially useful network for distributing inference results, transmitting model updates, connecting orbital sensors to compute nodes, and avoiding some reliance on ground-station passes. But they do not establish that a satellite constellation can function like the tightly coupled networking fabric of a terrestrial AI supercomputer.

We won’t be seeing large-scale machine learning and training in space. This requires huge, predictable bandwidth and very low latency for GPU-to-GPU communications. An orbital network would also face physical propagation delays, laser-link acquisition and handoffs, routing across a moving constellation, and limits on available capacity per spacecraft.

## Debris, war and solar storms

Another issue, according to [Doug Mohney](https://www.linkedin.com/in/dougmohney/), a long-time space influencer, is debris. “One bad day, a piece of random junk hits one satellite, which fragments into multiple pieces of shrapnel, which hits another satellite and so on and so on until you get a [Kessler event](https://aerospaceamerica.aiaa.org/features/understanding-the-misunderstood-kessler-syndrome/) that turns the selective orbit into a roaming cloud of debris.”

A Kessler event is when one satellite breaks up, and its fragments hit another, and so on until an area of LEO is filled with wreckage rather than viable satellites.

![](https://cdn.thenewstack.io/media/2026/08/5323dd86-kesler-event-1024x786.jpg)

What a Kessler event could look like. Credit: ESA.

Adding insult to injury, a Kessler event may not happen by accident. Mohney also observes that space warfare is a real threat: “A bad actor such as  Russia, China, Iran, or North Korea could use kinetic (unrandom junk!) means to target one or more satellites, resulting in space debris.” Or, “One good nuclear weapon uses an electromagnetic pulse to get rid of all of them at once. Both Russia and China (and the US) already have anti-satellite weapons (ASAT) programs. North Korea could have ASAT, but a nuke would ensure mass destruction of orbital capability.”

If that sounds crazy, keep in mind that Starlink satellites are already being used by Ukraine, and [Russia has been trying to block their transmissions.](https://www.reuters.com/business/aerospace-defense/russia-tries-jam-musks-starlink-systems-counter-ukrainian-drones-2026-07-08/) There have also been credible reports of [Russia developing ASAT weapons specifically designed to knock Starlink satellites](https://apnews.com/article/russia-starlink-musk-ukraine-space-china-canada-c69c1fda5ffc93828712ab723e606a2c) out of the sky. Larger and more fragile Starmind satellites would be far more vulnerable.

Mohney also worries about the “known unknown” of space weather.

“A Solar flare that hit the Earth along the lines of the 1859 [Carrington Event](https://spacedaily.com/sd-in-1859-a-solar-storm-now-called-the-carrington-event-induced-currents-so-strong-in-north-american-telegraph-lines-that-operators-disconnected-their-batteries-and-kept-sending-messages-on-the-geoma/), the largest recorded solar storm, would take out orbital electronics of all satellites.” This, in turn, as uncontrolled satellites drift from their orbit, might cause a Kessler event.  Lesser events have already pushed LEO satellites out of space. For example, a [February 2022 geomagnetic storm forced thirty-eight newly launched Starlink satellites out of orbit](https://repository.library.noaa.gov/view/noaa/53091).

## The $170 billion question

There are also business concerns. For all the obstacles that new and expanded ground-based AI data centers face, the energy analytics firm [Wood Mackenzie](https://www.woodmac.com/) believes “A hypothetical 1 GW orbital data center would cost an estimated $170 billion, more than three times the equivalent terrestrial facility, with launch and satellite costs accounting for approximately 60% of that total. To bring orbital costs to parity with terrestrial alternatives would require a 70% reduction.”

The company thinks that might be possible, but [Robert Liew](http://linkedin.com/in/robert-liew-sg?originalSubdomain=sg), Wood Mackenzie Research Director, observes, “That gap does not close without sustained and dramatic progress on launch costs. We forecast US$ 9 trillion of terrestrial data center investment between now and 2040. That is where capital goes first. Orbital data centers are a serious long-term proposition, but right now they remain a bet on the cost curve.”

For now, SpaceX has offered a broad technical vision and a hardware partnership with NVIDIA, but few of the operational metrics that would establish commercial viability. The real test will be whether SpaceX Starship becomes a practical launch vehicle and can overcome its cooling and safety issues. Then, the AI1 must also show enough usable compute per kilogram, kilowatt, square meter of radiator, and dollar of launch cost to outperform or complement ground-based AI infrastructure. I don’t see this happening anytime soon.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)