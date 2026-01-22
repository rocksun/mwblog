Coming off a great holiday break, full of eggnog-induced reflection and an eagerness to get this year rolling, I couldn’t resist a quick (and slightly self-congratulatory) [look back at my 2025 trend predictions.](https://thenewstack.io/5-game-changing-trends-for-2025-kubernetes-leads-the-way/) Let’s see if I deserve a crystal ball or just a cheap plastic one.

Here’s a lightning recap of the 2025 Top Trends, just in case you haven’t memorized them:

## 2025: A Look Back

1. **Generative AI will supercharge software development.** This was the easy one, like predicting the sun would rise. Coding copilots (looking at you, GitHub Copilot, Claude Code and Cursor) didn’t just become “a thing,” [they became the norm](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/). If your dev team isn’t using one, are they even trying?
2. **Agentic AI will transform enterprise operations.** The bots started walking among us! Mid-year, enterprises realized GenAI wasn’t just for writing bad poetry; it could automate actual work. And while the big players (OpenAI, Anthropic and the “big three” hyperscalers) dominated, [Deepseek reminded everyone that training is expensive](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/). We’re all now asking, “How do we get the cost down before our CFO gives us the deep six?” This trend of departmental AI adoption? It’s just getting warmed up.
3. **Enterprise AI will integrate with systems of record.** We’re creating virtual workers! They don’t need coffee, they don’t complain about the air conditioning and they’re taking over the soul-crushingly repetitive tasks. In highly regulated sectors, the data and the AI are becoming besties, sitting right next to each other. Many customers are on this migration path, and trust me, you’ll want to read the 2026 update on where this is going.
4. **Modernization will accelerate under cost pressures.** High TCO from legacy virtual-machine setups and scary cloud bills were already bad, but increased pricing pushed everyone who was “just thinking about” moving their VM workloads into actively looking for alternatives. Kubernetes-based virtualization is now the exit ramp. Modern virtualization has gone from a mere possibility to the way many enterprises are now happily running their VMs at scale. More drama to come in the sequel (2026)!
5. **Kubernetes will become the unified hybrid cloud platform:** This is a fact, especially among our Global 2000 customers (where Pure and Portworx have a strong presence, naturally). They’re merging their VM and [container worlds onto a single control plane](https://thenewstack.io/kubevirts-architecture-crds-controllers-and-daemons/) (hello, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) Openshift and SUSE Virtualization). And the funniest part? Generative AI is driving this convergence. K8s: It’s not just for containers anymore!

## Top 5 Trends for 2026: The New Frontier

While some of my last-year trends went “viral” and others are still emerging, here’s my fresh take after talking (and occasionally commiserating) with Portworx customers across the board.

### Trend 1: It’s All About the Inference, Stupid!

Foundational models? Commoditized. The massive capital expenditure on training? Done. [The new battleground? Inference.](https://thenewstack.io/confronting-ais-next-big-challenge-inference-compute/) This is where the GenAI differentiation will live and die.

Nvidia essentially stamped a giant “True” on this trend with its not-at-all-subtle $20 billion licensing and team acquisition of Groq.

This means you need to take a much closer look at how you build and run your infrastructure. Enterprises will train on the best foundational models, but they will be forced to run inference with smaller, faster models closer to the customer. Why? Because in tech, the last mile is the most challenging, the most lucrative and for GenAI, it requires lightning-fast inference at high accuracy and low cost. If your app and data infrastructure aren’t truly hybrid and portable, you’re basically doomed to be slow.

### Trend 2: Be Open or Die

To survive the inference wars (Trend 1), every enterprise will be forced to adopt open infrastructure. They need to orchestrate apps and data at high velocity, with zero drama and endless elasticity. Closed, legacy systems will become so expensive and cumbersome that they’ll slowly lose their purpose, like a DVD rewinder. This year is the curtain-raiser for a decade-long saga. This is the era of open. Stay closed at your own peril (and with your own very large expense account).

### Trend 3: Large Enterprises Go All-In on Kubernetes for Everything

Global 2000 companies are looking for [VMware](https://tanzu.vmware.com?utm_content=inline+mention) alternatives. In response to the question, “Which of the following statements best represents your company’s overall strategy for using VMware for VM workloads?” Thirty-three percent of the 523 respondents surveyed for Portworx’s “[Voice of Kubernetes Experts Report 2025](https://portworx.com/resources/voice-of-kubernetes-expert-report-2025/)” stated they have stopped or plan to stop using VMware.

![](https://cdn.thenewstack.io/media/2026/01/39f61676-image1.png)

Source: Portworx’s “The Voice of Kubernetes Experts Report 2025.”

These enterprises will finally choose Kubernetes as the single control plane for escaping VMware, modernizing old apps (containers) and acting as the default orchestrator for AI. Again, the real fight is in inferencing, and Kubernetes is perfectly built for that with its elasticity and on-demand agility. It’s the ultimate Swiss Army knife for the modern data center.

### Trend 4: The Edge Gets Its Groove Back

Edge computing is getting a renewed focus, thanks to the proliferation of 5G/6G applications and [GenAI’s revolutionizing of the digital experience](https://thenewstack.io/driving-digital-experiences-via-cloud-native-applications/). More compute, more data and more storage will be required at the edge, simply because the digital workloads of the future will rely on speedy, local inferencing to give customers that “wow, that was fast” experience. The edge is sharp again.

### Trend 5: Specialized Vertical AI Agents Infiltrate Enterprise Infrastructure

While coding agents are making developers faster than ever, we are about to see highly specialized agents take up expert roles, augmenting DevSecOps, SDETs (software development engineers in test), SREs (site reliability engineers) and platform engineers. They will supercharge [DevOps functions beyond just coding](https://thenewstack.io/the-roi-of-speed-how-fast-code-delivery-saves-millions/) and testing, making your infrastructure team suddenly look like the Avengers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/09/b501de70-cropped-d029d219-venkat-ramakrishnan.jpg)

Venkat Ramakrishnan is vice president of Products, Engineering and Customer Experience for the Cloud Native Business Unit/Portworx at Pure Storage. Since joining Portworx in 2016, he has played a pivotal role in pioneering a new category of data management, protection...

Read more from Venkat Ramakrishnan](https://thenewstack.io/author/venkat-ramakrishnan/)