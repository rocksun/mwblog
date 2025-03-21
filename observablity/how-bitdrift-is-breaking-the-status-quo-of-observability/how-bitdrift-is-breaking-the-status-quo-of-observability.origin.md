# How bitdrift Is Breaking the Status Quo of Observability
![Featued image for: How bitdrift Is Breaking the Status Quo of Observability](https://cdn.thenewstack.io/media/2025/03/8a599a43-bitdrift-1024x683.png)
For the past 30 years, the observability industry has attracted [billions in investment](https://www.mordorintelligence.com/industry-reports/observability-market) and made notable advancements in log, traces, and metrics collection and analysis. But the fundamental approach to [observability](https://thenewstack.io/observability/) has remained unchanged.

Best practices continuously preach: *Send as much telemetry as possible—you never know what you’ll need*.

But in reality, more data isn’t always better. For one, while telemetry is indeed crucial for debugging and issue resolution, it comes at a steep price, literally. Beyond paying storage and vendor fees, organizations also lose money on network bandwidth, processing power, and [engineering overhead](https://thenewstack.io/operations/).

Perhaps more alarming is how most observability practices and tools completely overlook mobile. Despite the [millions of dollars being poured into the industry](https://www.itpro.com/cloud/cloud-computing/enterprises-are-ramping-up-it-observability-investment-heres-why), almost all of these funds are directed to server-side observability.

## Why Observability Overlooks Mobile
I sat down with [Peter Morelli](https://www.linkedin.com/in/peterfmorelli), co-founder and CEO, and [Matt Klein](https://www.linkedin.com/in/mattklein123), co-founder and CTO, from bitdrift to discuss developments in observability and why the industry has historically overlooked mobile. They found the whole thing ironic:

“The world has moved to an app-based system. Most people interact with services developed through an app. But as an industry, we haven’t invested enough in understanding — and helping fix — the user experience where it actually matters: on mobile,” says Klein.

What about the 99.99% success rate often touted by service providers as proof of reliability? Klein says this figure isn’t necessarily reflective of reality: “There have probably been a hundred times in my career where a server has a success rate of 100%, but all clients’ requests are crashing. That makes the effective success rate zero.”

When pressed to explain why [mobile observability](https://thenewstack.io/choosing-manual-or-auto-instrumentation-for-mobile-observability/) continues to lag behind the rest of the industry despite its obvious importance, both Morelli and Klein chalk it up to a laundry list of technical challenges.

For one, the sheer scale of mobile devices presents a problem. Compared to hundreds of thousands of servers, teams face tens of millions of mobile devices, including iOS and Android’s horde of different models. Sophisticated user permission structures add another layer of complexity, as does network stability.

“For the most part, server apps have consistent networking that doesn’t fail. Of course, there are failures, but it’s overall a very heterogenous, tame environment,” Klein said. “Mobile networks, on the other hand, are spotty.”

Altogether, these problems make the mobile domain complex, challenging, and expensive, a combination that adds up to long troubleshooting cycles.

On a server, for instance, you can push potentially 20 deployments in a day, depending on the problem. For established applications, however, total turnaround time looks more like two weeks at best, requiring one week for app store approval and another week for users to install updates. Cost considerations aside, this cycle is time- and labor-intensive — but Morelli and Klein say it doesn’t have to stay this way.

## For Observability, bitdrift Says Less Really Is More
“We wanted to take a different approach to observability that allows engineers to get data when they actually need it — and not when they don’t need it,” says Klein. That’s what they’re promising with [bitdrift](https://bitdrift.io/), the startup that spun out from Lyft in 2023. While the bitdrift name is relatively new on the scene, the team themselves have been shaking up observability behind the scenes for years.

Morelli and Klein met working on global performance at Twitter before linking up with bitdrift’s third co-founder, [Martin Conte Mac Donell](https://www.linkedin.com/in/reflejo/), when they moved to [Lyft](https://thenewstack.io/lyfts-tips-for-avoiding-software-crashes/) in 2015. There, the trio spearheaded a solution for the ride-hailing service that, as they describe it, “flip[s] the decades-old mobile observability paradigm on its head, [enabling engineers to] log everything, intelligently choose what to store, and instantly deploy changes to your entire fleet.”

Instead of sending and storing all telemetry by default, the solution logs everything locally using a circular buffer for storage. With a real-time control plane, engineers can enable, retrieve, or adjust telemetry on-demand without having to deploy app updates. This way, they can instantly troubleshoot and quickly solve problems without having to ingest, index, or store unnecessary data — all at a lower cost.

“Fast-forward six years,” says Morelli, and “we realized there still wasn’t anyone else out there doing what our solution does.” That’s when they decided to take their solution independent. After supporting 50+ million devices for Lyft (and reportedly saving the company tens of millions of dollars per year), [the small team of nine launched the previously in-house solution as bitdrift in 2023](https://mattklein123.dev/2023/06/12/the-next-chapter-bitdrift/), with Lyft as its first customer and biggest investor.

## Breaking the Age-Old Observability Mold
bitdrift’s approach is a complete 180 from traditional observability practices — and they acknowledge it’s been a bit of a shock for engineering teams. “It’s been drilled into our heads that more data is better — but that’s not really the case,” Klein says.

Cost is an obvious drawback to this more-is-better approach. The main reason observability is so expensive is that most solutions’ pricing is based on numbers and sessions, where the more you log, the more you pay. Internally, this model often causes tensions between finance and engineering teams; finance teams lobby to send less data to cut costs, while engineering teams lobby to send more data to support troubleshooting.

Finances aren’t the only cost of observability, though; most solutions also drain labor, time, and resources. After all, the more data you generate, the more time and effort it takes to sort through it all, identify root causes, and problem-solve.

“Vendors are always encouraging you to log more information, but you’re not necessarily getting value out of all that information,” Morelli points out. “[But] if you have the power to be more intentional about collecting data only when you need it and turning it off when you no longer need it, then it’s much easier to wrap your head around what you’re looking at,” adds Klein.

This is what the bitdrift solution promises — but it can be hard for people to get on board with the brand’s less-is-more approach, at least at first.

Morelli and Klein admit it’s not unusual for them to face resistance when introducing bitdrift. They say it’s because they’re trying to fundamentally change the industry and do things differently from all the other observability vendors out there.

“We do get a lot of questions, like ‘What if I need that data two years from now?’” Klein shares. But he also says it doesn’t take long for customers to start singing a different tune: “Once they realize they can get a huge amount of data, just when they need it, to solve their problems immediately — it’s frankly eye-opening.”

## Entering a New Era of Observability
Why hasn’t anyone else taken a crack at changing the age-old observability paradigm?

Morelli and Klein’s first point-blank response is that the technology is just very challenging — but there seems to be more to it than that. “Other observability vendors are simply not incentivized to change the cost model,” says Klein. “For most vendors, the more data they send, the more they can charge.” It’s also a matter of inertia. With the industry focused on the more-is-better approach for so many years, it’s not natural to question tradition and seek alternatives.

But perhaps bitdrift is pushing the industry to a turning point.

Morelli and Klein say they’re already getting queries from customers about other use cases, noting that the problems their solution solves extend beyond mobile to diverse industries. Particularly, they see a lot of opportunity for industrial use cases, where real-time control can be highly advantageous, like oil and gas, maritime, space, and industrial machinery.

For now, bitdrift’s focus is purely mobile — but their approach may inspire a whole new era of observability.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)