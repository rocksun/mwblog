IPv6 was developed in the late 1990s as a successor to IPv4 to address the internet’s rapid growth and prevent IPv4 address exhaustion. The original vision was that, after a period of dual-stack operation, IPv4 would be phased out. Over 25 years later, full-scale depletion of IPv4 addresses is imminent, yet [IPv6 adoption remains slow](https://thenewstack.io/why-is-ipv6-adoption-slow/) — currently only about 30% worldwide, with the same proportion of Alexa Top 1,000 websites reachable via IPv6. The timeline for a full transition remains uncertain.

## **Understanding IP Addresses: The Internet’s Postal System**

Before diving into the complexities of IPv6 adoption, it’s essential to understand what these protocols actually do. Think of IP addresses as the internet’s equivalent of postal addresses — they tell data packets where to go across the vast network of interconnected computers that make up the internet.

[![IPv4 vs. IPv6 address space: A scale comparison](https://cdn.thenewstack.io/media/2025/07/783108dd-image1-1024x683.png)](https://cdn.thenewstack.io/media/2025/07/783108dd-image1-1024x683.png)

IPv4 vs. IPv6 address space: A scale comparison

The scale difference is staggering. [If IPv4 addresses were grains of sand](https://www.reddit.com/r/theydidthemath/comments/vq7r2v/request_giving_away_1000000_ip_address_to_every/), IPv6 addresses would be like having entire beaches for every grain of sand on Earth. This massive expansion ensures we’ll never run out of internet addresses, no matter how many devices we connect.

[![Key differences between IPv4 and IPv6 protocols](https://cdn.thenewstack.io/media/2025/07/c762e803-image3-1024x366.png)](https://cdn.thenewstack.io/media/2025/07/c762e803-image3-1024x366.png)

Key differences between IPv4 and IPv6 protocols

## **The False Security of Network Address Translation**

Widespread reliance on Network Address Translation (NAT) has delayed IPv6 deployment. [NAT is a technique](https://thenewstack.io/tayga-bridge-an-ipv6-network-back-to-ipv4-using-nat64/) used in IPv4 networks to allow multiple devices on a local network to share a single public IP address when accessing the internet. It modifies the IP address information in packet headers as they pass through a router or firewall, enabling private IP addresses (like 192.168.x.x) to communicate with external networks. While NAT helped delay IPv4 exhaustion, it introduces complexity and breaks the end-to-end connectivity model of the Internet.

NAT also gives organizations a false sense of security, fostering the belief that IPv4 can be extended indefinitely. Many network professionals remain comfortable and confident with IPv4, questioning the [need for a new protocol when their current systems](https://thenewstack.io/devs-need-system-design-tools-not-diagramming-tools/) seem sufficient. Creating private NATs with IPv4 addresses often provides a temporary fix, solving problems for now, but overlooking broader industry and technical shifts.

The challenge is that technology professionals often focus so intensely on their immediate user base that they miss the bigger picture. If you can create a private NAT using IPv4 addresses, your immediate problems appear solved. However, this approach ignores the fundamental shifts happening across the internet infrastructure.

## **What’s Happening Behind the Scenes**

Major content providers, including [Google](https://cloud.google.com/?utm_content=inline+mention) and Facebook, are removing IPv4 from their data centers and relegating it to network edges, forcing translations for non-IPv6 traffic. When operators route traffic through IPv4 and carrier-grade NAT, the system funnels everything through a single translation point, introducing multiple layers of translation and inefficiency.

This creates a particularly inefficient scenario: If you’re an internet service provider routing all your traffic through IPv4 via carrier-grade NAT, you’re essentially connecting through that little translation machine on the network edge to reach content. This approach requires at least double translation and significantly increases costs.

Embracing IPv6 allows direct, “green path” connections from users to content, bypassing expensive translation layers. While some dismiss IPv6 as experimental, in reality, leading companies have deployed it at scale, and adoption is accelerating out of necessity.

## **The Challenge of Deployment**

Organizations face different deployment timelines depending on network complexity. Small, uncomplicated networks can transition to IPv6 within a few months. Large telecom environments may require a year or two, even under the best circumstances. The issue is becoming more urgent as IPv4 address space from regional registries like ARIN (American Registry for Internet Numbers) and RIPE (Réseaux IP Européens) is depleted, adding mounting pressure on operators.

## **Key Deployment Challenges**

* **Legacy system compatibility**: Many older systems and devices don’t support IPv6.
* **Staff training requirements**: Network teams need education on IPv6 management.
* **Dual-stack complexity**: Managing both protocols simultaneously increases operational overhead.
* **Vendor support gaps**: Not all equipment manufacturers fully support IPv6.
* **Cost considerations**: Infrastructure upgrades can be expensive.

## **The Dual Stack Dilemma**

The decision to go dual stack depends on network type and regulatory environment. For fixed networks, dual stack is often practical, although local laws — especially about legal interception — can influence the decision. In mobile networks, dual stack offers little benefit, as solutions like [464XLAT](https://www.lacnic.net/innovaportal/file/5522/1/464xlat-en.pdf) already work well.

## **Understanding Dual Stack Limitations**

Running dual stack doesn’t resolve the problem of limited IPv4 space. It merely makes IPv4 exhaustion more manageable. Deploying dual stack means roughly half of network traffic can move to IPv6, reducing congestion through the carrier-grade NAT, but organizations must still operate and maintain the NAT infrastructure.

However, dual stack does provide an exit strategy. Over time, as more content providers migrate to IPv6, traffic through translation devices will shrink, eventually reducing or eliminating the need for large NAT deployments.

## **Common IPv6 Myths Debunked**

Several persistent myths and misconceptions about IPv6 continue to circulate:

### **Address Structure Concerns**

Some critics argue that the divide between the network and host part of the address “wastes” 64 bits. While this could have been structured differently, IPv6 still represents a vast improvement over 32-bit IPv4 addressing. The design was created nearly three decades ago, and 64 bits for host identification is far superior to IPv4’s limitations.

### **Security Misconceptions**

IPv6 is sometimes misrepresented as more or less secure than IPv4. Security features are fundamentally similar. Although IPv6 supports built-in IPsec in transport mode, deployment is rare owing to a lack of easy key management tools. The real challenge isn’t the technology itself but the absence of simple tools for key distribution and management.

### **Multihoming Complexity**

Practical multihoming with IPv6 remains conceptually identical to IPv4: an Autonomous System (AS) and Border Gateway Protocol (BGP) are required. The minimum advertisable net block is /48, typically assigned per site. Organizations may receive larger allocations such as /29 as Local Internet Registries, depending on their regional registry.

## **Best Practices for IPv6 Addressing**

You shouldn’t worry about counting addresses or subnetting with IPv6. Instead, the prefix length signals use: /64 for individual networks, /48 for entire sites or generous home allocations and /56 for smaller deployments. Assignments below /56 aren’t recommended.

When network engineers ask how many devices can fit in a /64 subnet, the answer is simple: all of them. That’s just the addressing capability for one Layer 3 interface in a typical deployment.

## **Getting IPv6 Adoption Moving**

IPv6 is a mature technology with nearly a quarter-century of real-world deployment experience. Looking ahead, further protocol changes are unlikely in our lifetimes. It’s time to accept IPv6 as the new foundation and get started on deployment.

While some advocate for government intervention to accelerate IPv6 adoption, the approach differs by region. Regulatory frameworks, market forces and local priorities shape the pace and methods of adoption worldwide. There’s no universal solution.

## **Recommendations for Different Stakeholders**

**For Network Operators:**

* Begin with IPv6 training for technical staff
* Audit existing infrastructure for IPv6 compatibility
* Develop a phased implementation plan
* Consider the financial benefits of reduced NAT complexity

**For Business Leaders:**

* Understand that IPv6 adoption is inevitable, not optional
* Budget for infrastructure upgrades and staff training
* Evaluate vendor IPv6 support when making purchasing decisions
* Consider the competitive advantages of early adoption

**For Government Entities:**

* Develop region-appropriate policies that encourage adoption
* Invest in IPv6 education and awareness programs
* Lead by example in government network deployments
* Support international coordination efforts

## **The Path Forward**

You cannot avoid IPv6 much longer. The diminishing utility of NAT, exhaustion of IPv4 addresses and migration by major content providers are converging factors. Delaying the move to IPv6 will only increase complexity and cost as more translation workarounds are required.

The technology and tools for IPv6 are ready, and the business case is clearer than ever. The question isn’t whether to deploy IPv6, but how quickly and efficiently your organization can do so. Those who act now will benefit from direct, efficient connections to an increasingly IPv6-native internet, while those who delay will find themselves managing increasingly complex and expensive translation systems.

The future of the internet is IPv6. The only question remaining is whether you’ll be part of the solution or struggling to catch up from behind.

Hear expert insight on this topic in an [in-depth interview](https://www.catchpoint.com/blog/ipv6-qanda-jan-zorz-slow-ipv6-adoption).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/dd44fd18-cropped-4a12ba2e-alessandro-improta.jpeg)

Alessandro Improta is an engineering manager at Catchpoint. He received his B.Sc. and M.Sc. in computer engineering and his Ph.D. in information engineering from the University of Pisa, Italy. Since 2009 he has held a research position with the Institute...

Read more from Alessandro Improta](https://thenewstack.io/author/alessandro-improta/)

[![](https://cdn.thenewstack.io/media/2025/07/361b4f6e-cropped-223b041a-image2.jpg)

Denton Chikura is an observability advocate focused on helping site reliability engineers and engineering teams discover the tools and capabilities that strengthen internet resilience. With a background at the intersection of monitoring, performance and infrastructure, he works to make complex...

Read more from Denton Chikura](https://thenewstack.io/author/denton-chikura/)