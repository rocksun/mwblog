The [Rust](https://thenewstack.io/rust-programming-language-guide/) programming language is moving into new areas, including enterprise data pipelines.

While most of the industry relies on [Python](https://thenewstack.io/python/) and [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) for data processing, a growing number of companies are discovering that Rust’s combination of performance, safety and modern design makes it a game-changer for data-intensive workloads.

The latest proof point comes from [Singular](https://www.singular.net/), whose new [Extract](https://www.extract.to/) platform is delivering 17x performance improvements and up to 70% cost reductions compared to established [Extract, Load, Transform (ELT)](https://thenewstack.io/the-future-of-data-integration/) tools — all powered by Rust.

## Why Rust Matters for Data Engineering

Rust solves fundamental problems that have plagued [data engineering](https://thenewstack.io/demystifying-data-engineering/) for years. Most ELT platforms run on languages designed for different purposes — Python for simplicity, Java for enterprise adoption. Both carry significant overhead: [Garbage collectors](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/) that pause execution unpredictably, runtime environments that consume memory, and abstractions that distance developers from the underlying hardware, [Gadi Eliashiv](https://www.linkedin.com/in/gadie/), CEO of Singular, told The New Stack.

However, Rust eliminates these trade-offs, he said. It delivers C-level performance with memory safety guarantees that prevent entire categories of bugs, all wrapped in a modern language design that doesn’t feel like a step backward.

“I just fell in love with it, because I certainly felt the power in my fingertips,” Eliashiv said. “I’m like, I’m writing stuff that could be kernel code. It’s so efficient and this language is so modern at the same time.”

## The Memory Efficiency Revolution

The numbers tell the story**.** Singular’s team compared equivalent connector code between their legacy Python implementation and their new Rust version They achieved 20 times less memory consumption with Rust. For a multi-tenant SaaS platform this is transformative, he said.

“We can basically cram 20 times more customers on a given server, and so that is a dramatic cost saving we can offer our customers,” Eliashiv explained. The company reports that customers are seeing more than 50% cost savings, with some operations running 100 times more efficiently than legacy tools.

This efficiency gain is not theoretical. Extract is already serving enterprise customers including Warner Bros. and Electronic Arts, processing data at scales that would strain traditional Python or Java-based platforms, he noted.

## Memory Safety: The Hidden Advantage

Eliashiv’s team has deep experience in cybersecurity and vulnerability research, giving them a unique perspective on why memory safety matters for production systems.

“Every time somebody was misusing an array or a struct in C, C++ they were freeing some memory area twice. That was a source of a vulnerability,” he said. “The fact that we don’t have to think about it in Rust is incredible, because we can write code that’s effectively C/C++ level efficiency without having to worry about all those things.”

For data pipelines handling sensitive enterprise information, this isn’t just about preventing crashes — it’s about preventing the kind of memory corruption bugs that can lead to data breaches or silent data corruption, Eliashiv said.

## The Rust Development Reality

But Rust adoption isn’t without challenges. Unlike Python’s rich ecosystem of pre-built data connectors, Rust required building infrastructure from scratch.

“The initial infrastructure took a while, because… you don’t have a lot of people writing connectors using Rust,” Eliashiv acknowledged. The team spent significant time building foundations that could handle the variety of REST APIs and data formats they needed to support.

However, once that infrastructure was in place, development velocity increased. The Rust compiler’s strict checks catch errors at compile time rather than runtime, reducing debugging cycles and increasing confidence in code quality, he said.

## Scaling Rust Teams

Yet, the talent issue looms large for Rust adoption. Eliashiv’s approach was methodical — start with the company’s best engineers to establish patterns and infrastructure, then expand the circle.

“We took the best engineers in the company, and we put like this sort of special team for this product, and they were the first ones to learn Rust,” he explained. Many had backgrounds in C and C++, easing the transition.

As a bonus, Rust’s strict compiler became a training advantage. “Unlike Python, the chances of [new developers] breaking the code is really small because there’s a compiler, and it really makes sure you don’t mess things up,” Eliashiv said. “We are a lot more confident onboarding people and giving them defined tasks.”

AI coding tools like Cursor helped to accelerate this process, helping developers understand Rust concepts and even enabling cross-functional contributions, he added

## Beyond Data Pipelines: Rust’s Expanding Reach

The implications extend beyond ELT platforms**.**

“I think there is a real-time variant of Rust where you don’t have the full standard library, but you can write super-efficient code,” Eliashiv said. “I think it’s wonderful for all these different types of use cases.”

The language continues evolving rapidly, with improvements in [async programming](https://thenewstack.io/3-types-of-asynchronous-programming/) and ecosystem maturity making it increasingly viable for demanding, real-time applications, he noted.

## The Inflection Point

Rust’s adoption in data engineering signals a broader shift. As cloud costs continue climbing and data volumes explode, the efficiency gains Rust provides translate directly to business value. The performance improvements provide a competitive advantage.

“Extract gave us the performance we needed, with the simplicity our team wanted — and all without hiring another engineer,” said [Gal Karniel](https://www.linkedin.com/in/gal-karniel-774288134/), product director at SciPlay, in a statement.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)