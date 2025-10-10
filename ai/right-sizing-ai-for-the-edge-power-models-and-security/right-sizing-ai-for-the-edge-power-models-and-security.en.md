MOUNTAIN VIEW, Calif. — At [Edge Impulse’s](https://edgeimpulse.com/) recent panel discussion on [Edge AI](https://thenewstack.io/ai-is-coming-to-the-edge-but-it-will-look-different/), three industry leaders shared their views on the opportunities and challenges of deploying AI closer to where data is created. Moderated by The New Stack’s founder and publisher [Alex Williams](https://thenewstack.io/author/alex/), the panel featured [Margherita Ferragatta](https://www.linkedin.com/in/margherita-ferragatta-7b5818243/?originalSubdomain=it), CEO of [IDT Solution](https://idtsolution.com/); [Sean Varley](https://www.linkedin.com/in/sean-lentz-varley/), chief evangelist for [Ampere Computing](https://amperecomputing.com/); and [Aniket Ponkshe](https://www.linkedin.com/in/aniketponkshe/), head of Software Partnerships at [Canonical](https://canonical.com/).

Together, they described an ecosystem in rapid transition — one in which standardized platforms, specialized chips and [developer-first](https://thenewstack.io/comcast-cut-app-vulnerabilities-with-developer-first-approach/) approaches are redefining how enterprises move AI workloads from the cloud to the edge.

Edge AI refers to the deployment of AI models directly on devices or infrastructure located near where data is generated — such as sensors, cameras, vehicles or industrial machines — rather than in centralized cloud data centers. By processing data locally, Edge AI reduces latency, lowers bandwidth costs, enhances privacy and enables real-time decision-making, even when connectivity is limited. It combines advances in machine learning (ML), specialized chips and lightweight software frameworks to deliver intelligent functionality at the network’s edge — powering applications in areas such as autonomous vehicles, industrial automation, retail analytics and smart energy systems.

From the store floor to the factory line, Edge AI enables low-latency decision-making where it’s needed most. As use cases later in this story indicate, the edge isn’t only a frontier for experimentation — it’s rapidly becoming a production-ready environment.

[![](https://cdn.thenewstack.io/media/2025/10/1809fecd-edge-it-2-1.png)](https://cdn.thenewstack.io/media/2025/10/1809fecd-edge-it-2-1.png)

L-R: Alex Williams, Margherita Ferragatta, Aniket Ponkshe and Sean Varley.

## Lowering Barriers To Edge AI

Not long ago, running AI at the edge was technically prohibitive. Models were constrained by limited compute, and frameworks designed for the cloud did not fit embedded environments. No longer.

Since 2017, innovations in chip architectures and open source frameworks have drastically lowered the barrier to entry. “You can now do things like [YOLO](https://en.wikipedia.org/wiki/You_Only_Look_Once) (a real-time object detection system in computer vision) on a very small device, or run large language models [LLMs] with trillions of parameters on CPUs, GPUs, and accelerators,” Varley said. “The ecosystem has evolved across the entire stack — hardware, operating systems, frameworks and applications.”

This evolution has unlocked new possibilities: computer vision at the device level, real-time analytics on factory floors and even edge-enabled recommendation engines for retailers.

## Ubuntu at the Edge

For Canonical, the maker of Ubuntu, the rise of Edge AI has validated years of investment in lightweight, secure operating systems. Ponkshe recalled how Ubuntu Core, launched in the mid-2010s, anticipated the need for developer-friendly, cloud-like environments at the edge.

“Edge AI has a distinct set of challenges,” Ponkshe said. “Embedded developers and cloud native developers often speak different languages. The stacks are different, and enterprises increasingly expect cloud-grade security even on small devices. Ubuntu’s role has been to bring those worlds together, so you can train in the cloud and deploy the same stack at the edge — in weeks, not quarters.”

Canonical has also pushed hard on platform standardization, partnering with silicon vendors to ensure optimized performance across hardware. The result: Developers can focus on building applications instead of wrangling device-specific integrations.

## Open Source Meets Industrial Automation

Ferragata described IDT’s mission as bringing open source hardware and software to industrial automation, a sector historically dominated by proprietary systems and vendor lock-in. Early on, IDT turned to [Arduino](https://www.arduino.cc/), even before industrial-ready boards existed. Arduino is an open source hardware and software platform designed to make it easy to build and prototype electronic projects.

“It was difficult at first,” Ferragata said. “In 2016 and 2017, Arduino wasn’t industrial grade. We had to do a lot of partnerships and development ourselves. But eventually, Arduino Pro emerged, and we delivered projects like a battery cell handling system for a luxury automotive manufacturer — running entirely on Arduino hardware.”

For Ferragata, the lesson is clear: Open hardware and software can succeed in environments once thought too demanding. And in an era where factories and vehicles demand deterministic, offline reaction times, edge-enabled open systems can reduce dependencies on fragile connectivity and shorten time to market.

## The Hardware Gold Rush

If open source is reshaping software, specialized silicon is redefining the hardware layer. Varley called it a “gold rush” in AI computing, from hyperscale data centers down to small edge devices.

“Every layer comes with a power cost,” he said. “Whether you’re running AI in a rack of GPUs or on a battery-powered sensor, power consumption is now the defining constraint. Optimizations at every level — from model size to container footprint — matter.”

Ampere’s strategy centers on building sustainable processors with high performance per watt, scaling from server-class CPUs with nearly 200 cores to edge-ready configurations. Varley predicted that soon, all computing will be measured by power consumption, not just abstract performance benchmarks. Industry superstars such as former Intel CEO [Pat Gelsinger](https://www.linkedin.com/in/patgelsinger/) and NVIDIA CEO [Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/) are also on record for subscribing to that theory.

## Emerging Use Cases

With faster chips and optimized frameworks, enterprises are moving from proofs of concept to production. Ponkshe cited real-world deployments:

* **Retail:** Using Canonical’s ML stack, a major U.S. retailer implemented a real-time recommendation system at the point of sale, boosting conversion rates by 10%.
* **Energy:** Duke Energy is applying Edge AI for real-time load balancing in renewable energy grids, dynamically adjusting supply when wind or solar output fluctuates.
* **Automotive manufacturing and operations:** Factories and vehicles are becoming edge platforms. IDT’s work with Arduino-based automation systems shows how open hardware and AI can manage processes like battery cell handling for luxury automakers. In-vehicle AI, meanwhile, promises deterministic reaction times — milliseconds matter when it comes to driver assistance or autonomous features.
* **Intelligent video and security systems:** From cameras with built-in neural networks to distributed analysis across telco infrastructure, Edge AI is transforming how video is captured and processed. Instead of sending raw feeds to the cloud, systems can analyze video at the source, flag anomalies and send only relevant data upstream — reducing bandwidth and enabling faster response.
* **Industrial automation and robotics:** Edge AI is making factories smarter, not only faster. Robots can now collaborate in real time, with low-latency coordination handled at the edge. This reduces reliance on fragile connectivity, ensures continuity even when networks fail, and allows operators to focus on higher-value tasks — advancing the shift from Industry 4.0 to Industry 5.0, where human-centric design and flexibility will be keys.

“These are use cases that were impossible five years ago,” Ponkshe said. “Now they’re economically viable because we can process data close to the source, reduce latency, and still keep security front and center.”

## Right-Sizing Models

A recurring theme was the need to “right-size” AI models to the available hardware. Massive LLMs may require rack-scale compute, but smaller, task-specific models can run efficiently at the edge.

“The size of the model dictates where it can run,” Varley said. “Frameworks must be optimized not just for the workload, but for the specific chip architecture. That’s how you make sure the edge device is doing what it can, and the cloud only handles what it must.”

This balance is increasingly critical as sensors and devices proliferate. Millions of endpoints generating data cannot all rely on centralized cloud processing. Edge deployments offer a way to reduce cost and latency while improving resilience.

## Automotive: Slow but Steady

Because cars are edge devices, the automotive industry is now an edge battleground — but one where cultural and technical inertia still slows adoption. Ferragata observed that while automakers see the benefits of faster time to market and deterministic offline functionality, many remain tied to legacy proprietary systems.

“In manufacturing, you can’t always rely on connectivity,” she said. “Reaction times need to be deterministic — sometimes down to milliseconds. That’s where Edge AI really proves its value, but adoption is still gradual.”

Still, as vehicles themselves become rolling edge platforms, the pressure to integrate AI at scale is growing.

## What Developers Want

For developers, Edge AI success depends on platform simplicity and consistency. Ponkshe said that standardized stacks — with familiar frameworks such as [TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/), [MLflow](https://thenewstack.io/address-common-machine-learning-challenges-with-managed-mlflow/) or [Kubeflow](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support/) — let developers spend time on applications, not on debugging OS boots or hardware quirks.

“Developers want a cloud-like environment optimized for edge hardware,” he said. “That’s what accelerates innovation. You get the same tools you use in the cloud but tuned for the device you’re deploying on.”

Canonical’s long-term support guarantees and ecosystem partnerships are designed to reinforce that trust, helping developers experiment without fear that today’s work will be obsolete tomorrow.

## Looking Ahead: Power, Security and Control

As the session closed, each panelist shared a “wish list” for the future of Edge AI:

* **Ferragata (IDT):** Easier adoption of open technologies in industrial settings, greater flexibility and more recognition that open source systems are reliable enough for mission-critical production.
* **Varley (Ampere):** Hardware that delivers maximum horsepower with minimum power draw, achieved through heterogeneous designs combining AI acceleration, general-purpose processing, sensors and storage into ever-smaller SOCs.
* **Ponkshe (Canonical):** Platforms that give data creators more control — keeping processing closer to the edge for sovereignty and monetization, while embedding security by design.

Security especially looms large. From factories to vehicles, breaches can cripple operations for months. Regulatory pressure is rising, and enterprises will demand that edge deployments meet the same security standards as the cloud.

## Edge AI at a Turning Point

The panelists agreed: Edge AI is no longer experimental. It’s becoming a core architectural pattern for enterprises that need low-latency, resilient and secure AI outside the data center. The pieces are coming together — standardized OS platforms, sustainable processors, optimized frameworks and industrial-ready open hardware.

“We’re simplifying the complexity of AI by right-sizing models and infrastructure for the edge,” Varley said in summary. “In the end, power consumption will be the universal benchmark. That’s how we’ll scale AI sustainably, from hyperscale to the smallest device.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)