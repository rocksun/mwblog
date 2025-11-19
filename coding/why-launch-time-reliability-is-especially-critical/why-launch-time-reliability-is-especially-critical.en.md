Ensuring the reliability of a new product or feature at launch is crucial. Wherever it sits in an organization’s offering, a shiny, new tool or capability might look good on the surface, but customers will notice if it runs poorly or affects performance. Developers must bake launch-time [reliability](https://thenewstack.io/a-new-definition-of-reliability/) into their workflows so they can help the broader operations team prepare for a successful launch.

However, product reliability of any new launch is not a “one-and-done” process. Instead, both developers and operations teams play key roles in ensuring that product launches go smoothly.

For developers, preparatory steps include continuous testing, building greenfield projects in dedicated environments while keeping legacy applications running as usual and treating complex deployments with the care they deserve.

On the other hand, operations teams must have their monitoring in place, be on the lookout for performance changes after a release and have on-call rotations planned before new services are presented to users. Together, these two teams can help prevent customers from being adversely affected by a new launch.

Reliability is about more than just protecting customers. There are three key reasons for organizations to prioritize launch time reliability:

## **1. Complex, Distributed Systems**

Modern enterprises are built on incredibly complex ecosystems. While monolithic architectures do still exist, they often include a number of add-on tooling that’s been added over time as the business has expanded or needed them to offer new capabilities to their customers. These complex systems mean launching a new product or capability requires [engineers to work across cloud services and third-party platforms](https://thenewstack.io/platform-engineering-what-does-good-look-like/). Moreover, large enterprise systems and teams are often globally distributed, further increasing their complexity and, at times, introducing service delays. Altogether, the complexity of these systems means that any new launch can potentially upset a delicate balance and cause a service outage.

Launch-time reliability must always be front of mind to mitigate risk. This involves always building with a mindset that promotes DevOps best practices, including the adoption of a “shift left” approach where [stability and security](https://thenewstack.io/shifting-it-strategy-to-balance-security-and-resilience/) are prioritized right from the start of each development cycle, as well as secure coding and CI/CD practices that promote regular testing and code reviews. Without reinforcing these behaviors across teams, product launches may risk making organizations more vulnerable to service disruptions, data breaches and system failures.

## **2. Compliance With Regulations**

Launch-time reliability isn’t just about managing internal systems. Keeping services online and providing timely reporting around any incidents are key to staying fully compliant with regulations. Compliance is becoming ever more crucial as regulatory bodies mandate increasingly stringent incident reporting requirements.

For example, in the UK, regulations such as the [Financial Conduct Authority’s CP24/28](https://www.fca.org.uk/publications/consultation-papers/cp24-28-operational-incident-third-party-reporting) and the [Prudential Regulation Authority’s CP17/24](https://www.bankofengland.co.uk/prudential-regulation/publication/2024/december/operational-incident-and-outsourcing-and-third-party-reporting-consultation-paper) require financial services firms to have detailed incident management policies, clear escalation procedures and rapid reporting mechanisms. Similarly, in the United States, several industries are required to report downtime, including finance and broadcasting, which have reporting requirements to the Securities and Exchange Commission (SEC) and the Federal Communications Commission (FCC), respectively.

Failure to comply with regulations will result in penalties and reputational damage, a heavy price to pay for a failure that can be avoided as early as the development stage.

## **3. Delivering Good Customer Experience**

New product launches must actively improve the services provided to customers while also being seamless without interrupting existing provisions. With service level agreements (SLAs) determining minimum performance requirements, providing a good customer experience goes beyond being a “nice to have.” It is an essential part of the service a business provides.

In many cases, SLAs also offer customers a “get-out-of-jail-free card” in the event of frequent or prolonged service disruptions. Outages can erode trust in an existing customer base, but they will also lead to customer attrition, hurting an organization’s revenue.

To minimize the potential damage to an organization’s bottom line, engineering teams must adopt DevOps best practices, such as implementing a CI/CD pipeline to enable regular releases throughout each day with zero downtime or promoting cross-functional collaboration throughout the software delivery cycle to encourage rapid troubleshooting. On the flipside, operations teams can provide support by implementing an incident management framework that promotes timely communication and resolution of issues when these do arise. This requires broader data observability so that information can flow between [teams in the event of an incident](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/). Together, these teams can help their organization meet all the requirements of its SLAs to protect revenue and continually deliver a top-class service to their customers.

## **Hitting the Moving Target of ‘Good’ Development**

Over time, as enterprises and development practices have evolved, what may be considered as “good” hasn’t stood still. Over the past 20 years, there has been a Cambrian explosion of software, as well as improvements to best practices, changes in metrics and new monitoring capabilities. These have been combined with enterprise systems becoming more complex over the same timeframe, meaning that maintaining launch-time reliability is highly challenging for engineering and operations teams. It is only by close collaboration that these teams can ensure that the launch of new products and features can deliver a great customer experience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/11/06cb1037-cropped-9d413136-mandiwalls-735x800-1-600x600.jpg)

Mandi Walls is a DevOps advocate at PagerDuty. She is a regular speaker at technical conferences and is the author of the O'Reilly Media white paper "Building a DevOps Culture." She is interested in the emergence of new tools and...

Read more from Mandi Walls](https://thenewstack.io/author/mandi-walls/)