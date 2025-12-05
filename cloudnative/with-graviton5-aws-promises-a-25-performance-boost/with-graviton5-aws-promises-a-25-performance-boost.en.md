LAS VEGAS — At its annual re:Invent conference, [AWS](https://aws.amazon.com/?utm_content=inline+mention) today [launched](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2) the latest version of its Arm-based Graviton chips. The company promises that these new chips, which will feature 192 cores per chip (up from 96 in the last generation), will deliver up to 25% higher performance than the Graviton4 chips, which launched two years ago.

In addition to higher speeds, the team also added a new layer to its Nitro hypervisor cards, the Nitro Isolation Engine, which now mathematically guarantees that different workloads are isolated from each other.

## Graviton5

[Ali Saidi](https://www.linkedin.com/in/a-saidi/), a VP and Distinguished Engineer at AWS whose group develops these chips, told me that over 90,000 AWS customers now use the Graviton chips and 98% of the top 1,000 users of AWS’ EC2 compute service use them. As AWS CEO [Matt Garman](https://www.linkedin.com/in/mattgarman) announced earlier this week, over 50% of the CPU capacity AWS added over the last few years was Graviton-based.

“That’s a story that spans across our EC2 compute, where customers are getting their own compute and running their own workload, and also our managed services — Redshift serverless, is 90% Graviton, Elasticache, Amazon, Aurora, DocumentDB, all these things are greater than 50% Graviton today,” Saidi said.

[![The AWS Graviton logo](https://cdn.thenewstack.io/media/2025/12/de5009a0-aa-graviton-5-hero-2000x1125-1.jpg)](https://cdn.thenewstack.io/media/2025/12/de5009a0-aa-graviton-5-hero-2000x1125-1.jpg)

The Graviton logo. Credit: AWS.

With Graviton5, the team focused on not just improving raw benchmark performance but also ensuring that those performance gains would also apply to real-world use cases. More cores help there, of course, but as Saidi noted, having those cores closer together also provides advantages in scalability and latency. For some workloads, that can mean between 30% and 40% improvements in performance, for example.

He also noted that these workloads benefit from larger caches, with every core having access to 2.6x more L3 cache than the previous generation (which means the core ideally needs to spend far less time waiting for data to arrive to start its computations).

The team also improved the network and storage bandwidth.

## Nitro Isolation Engine

From a computer science perspective, the more interesting update today may actually not be the chip itself but the Nitro Isolation Engine. AWS has long promised that its Nitro system — its custom hardware virtualization system for EC2 — would sandbox different workloads and ensure that no information could leak between them.

This is the sixth generation of Nitro cards and for the first time, the team decided to compartmentalize the functions of the hypervisor even more. “We said: could we take the code that manipulates things like the page tables and handles guest state and put it in its own really thin layer?” Saidi explained.

That new layer was built in Rust, which itself promises enhanced memory and concurrency safety. But more importantly, since the team started from zero, it worked with AWS’s automated reasoning group to, from day one, make formal verification an integral part of the development process.

“It’s not providing anything more than that hypervisor does in terms of guest confidentiality,” Saidi explained. “But we’re able to say: look, this is how we’ve raised the bar in doing this. This is how we’re trying to improve transparency, of showing you how we’ve used formal verification to actually saying that, yes, we are keeping guest content isolated from each other and isolated from us.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)