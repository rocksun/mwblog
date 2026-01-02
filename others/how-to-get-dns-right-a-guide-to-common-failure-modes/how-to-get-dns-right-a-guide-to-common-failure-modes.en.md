*This is the first in a two-part series.*

If you’ve spent any time diagnosing outages or performance issues, you know that when nothing seems to work, “It’s probably DNS.” The Domain Name System (DNS) remains the backbone of digital connectivity, quietly enabling every web transaction, application call and end user experience.

Every click, app and transaction depends on [DNS](https://thenewstack.io/why-you-need-distributed-dns-implementation/). It translates names to addresses so users can reach your services.

But while the basics of DNS are well-known, monitoring and troubleshooting this critical layer demands ongoing vigilance and advanced tooling. This two-part series walks through why DNS problems are so hard to see, then shows how to monitor, test and validate DNS performance from the user’s point of view.

## **The DNS Risk Landscape**

DNS plays a vital role in directing users to their intended destinations. Since most organizations depend on external DNS providers, they often have limited visibility into the service’s overall reachability, performance and the security of records in real time. Understanding the main failure modes will help you decide what to monitor.

### **1. Micro‑Outages**

Micro‑outages briefly prevent users from resolving a domain. They may last for minutes up to an hour and affect only certain regions or networks. [Anycast](https://www.catchpoint.com/blog/troubleshoot-anycast-dns-issues), a routing method that directs queries to multiple geographically distributed servers, can mask underlying problems because a node may continue advertising its [Border Gateway Protocol (BGP)](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/) route even when some paths or sites are unhealthy. Common causes include:

* Data center or pop outages.
* Routing or connectivity incidents between networks.
* Server performance saturation.
* Capacity limits that trigger timeouts during bursts.
* ISP-specific routing or packet loss issues affecting only certain user segments.

To users, this looks like a random failure to load your site, then a normal experience on retry. To operations teams, it can be hard to reproduce without continuous, distributed testing.

### **2. Misconfigurations**

[Configuration mistakes](https://thenewstack.io/tech-veterans-new-approach-to-eliminate-configuration-hell/) are a frequent root cause of resolution failures. A few high‑impact examples:

* **CNAME at the apex**CNAME (Canonical Name) records create aliases that let you use different domain name variations to point users to the same location on your website. For example, `help.mystore.com` and `support.mystore.com` can both direct visitors to the same destination. While CNAME records are commonly used to create aliases for existing A (address) records, referred to as the CNAME’s owner record, they should never be configured as the apex domain. This restriction exists because of the way CNAME records interact with their owner and target records. A CNAME replaces all DNS records associated with its owner by directing queries to those of the target record. When both an A record and a CNAME exist at the apex, a conflict occurs: The apex A record cannot be both the CNAME owner and its target. This conflict leads to resolution failures.

For instance, www.ggle.com can point to google.com using a CNAME, but google.com itself should not be a CNAME since it represents the apex domain.

* **Missing glued records**A records link a website’s domain or subdomain to an IPv4 address, allowing users to reach the correct server. Most websites use a single A record, although larger sites that implement round-robin load balancing may configure multiple A records for the same name.​

Glue records are A records that are paired with corresponding nameserver (NS) records, so the nameserver has an IP address. This lets the server resolve its own fully qualified domain name. Without glue records, operations like delegation, dynamic DNS updates and normal query resolution can run into issues or fail outright.

Glue issues typically occur only when the nameserver is inside the zone being delegated (ns1.example.com for example.com); adding glue for external nameservers is unnecessary and can itself become a misconfiguration.

* **Incorrect TTL values**DNS time to live (TTL) values define how long a response stays in cache. Setting them improperly can be the difference between a near-instant cached lookup and a much slower query that has to traverse the internet to get a fresh answer. How long to cache responses should be guided by the characteristics of your environment. Highly dynamic systems will run into problems with a 24-hour TTL because records change too frequently, while more static environments may not need a 5-minute TTL and can even gain performance benefits by increasing it. Overly long TTLs can also slow down failovers or cutovers because resolvers may continue serving stale IP addresses.
* **Lame delegation**Domain names are typically required to use at least two nameservers. When a query is made, each nameserver that responds can be either properly authoritative or “lame,” meaning it is listed as authoritative but does not actually hold authoritative zone data for that domain. To avoid lame delegation and ensure reliable resolution, configure every nameserver so it is correctly authoritative for the appropriate zone associated with the domain. Lame delegations often occur when the NS records at the parent zone list servers that no longer host the zone, causing those servers to return nonauthoritative responses.

### **3. DNS Poisoning**

DNS poisoning, also called cache poisoning or spoofing, occurs when an attacker injects forged DNS data so that resolvers cache and serve malicious answers. Misconfigurations and lack of validation increase exposure. Poisoning can spread downstream when an affected resolver feeds internet service providers, home routers and device caches. The result is traffic redirected to malicious hosts, phishing sites or person‑in‑the‑middle infrastructure.

* **Attackers alter a DNS record as part of a DNS poisoning attack**  
  Domain Name System Security Extensions (DNSSEC) is the strongest defense against cache poisoning because it allows resolvers to verify that DNS records are digitally signed and have not been tampered with.

### **4. Denial of Service (DoS) Attacks**

Attackers can try to make your web resources unavailable by overwhelming a specific URL with excessive requests, in what is known as a denial of service (DoS) attack. This floods the service with bogus traffic, crowding out legitimate users and causing severe slowdowns or complete outages.

A distributed denial of service (DDoS) attack uses the same idea but relies on thousands of compromised machines, or botnets, across the internet to take the service offline at scale. A more recent variation uses [memcaching](https://www.cloudflare.com/learning/ddos/memcached-ddos-attack/)-based techniques to amplify DDoS traffic even further.

* **Amplification DDoS attacks**In an amplification attack, attackers exploit small queries that trigger much larger responses. By repeatedly sending these lightweight requests, they force DNS or other services to return disproportionately heavy replies, quickly exhausting the target’s bandwidth and resources.
* **Reflection DDoS attacks**In reflection attacks, attackers send large, spoofed queries that appear to originate from the victim’s IP address. The victim then receives the oversized responses and is flooded with traffic, while the recursive nameserver and authoritative server can also be strained by the amplified load.

## **The Business Impact**

DNS issues reduce availability and degrade performance. They also undermine security controls that depend on name resolution. Symptoms include elevated error rates, checkout abandonment, login failures, stuck API clients and misrouted email. Because DNS sits before everything else, problems multiply across services.

## **What Comes Next**

Now that you have the context for why DNS fails, the next step is learning how to detect these conditions before users do. Part 2 in this series explains how to monitor DNS for performance, integrity and resilience with tests that reflect real user experience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/1cf49f99-cropped-d4e400fe-sheldon-pereira.jpg)

Sheldon Pereira is a solutions engineer at Catchpoint, a LogicMonitor company. He specializes in synthetic monitoring, network performance and observability. He works closely with global enterprises to improve digital experience across web, application, API and network layers.

Read more from Sheldon Pereira](https://thenewstack.io/author/sheldon-pereira/)