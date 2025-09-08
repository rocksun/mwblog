[Russell Cohen](https://www.linkedin.com/in/russell-cohen-b75b9927/) has watched hundreds of teams try to adopt [Rust](https://thenewstack.io/rust-programming-language-guide/) at Amazon over the past decade. Most of them screw it up.

Cohen, a senior software engineer who leads Rust adoption efforts at [AWS](https://aws.amazon.com/?utm_content=inline+mention), does not sugarcoat it. Speaking at the [RustConf 2025](https://rustconf.com/) event this week, he laid out exactly why most organizations fail at Rust — and what the few successful ones do differently.

Cohen said he gleaned four key insights regarding the success of [Rust projects](https://thenewstack.io/rust-project-reveals-new-constitution-in-wake-of-crisis/). Teams must: have a real reason to use Rust; find, grow and empower Rust pragmatists; learn (or build) new tools; and build operational capabilities early.

## The $100K Rewrite Nobody Asked For

Meanwhile, here’s how it typically goes wrong, Cohen described. In 2024, a Rust enthusiast at Amazon convinced their team to build a new service in Rust instead of [Python](https://thenewstack.io/what-is-python/). The service worked fine. Three months later, the project got reorganized under a different team.

“They took a fully working service and rewrote it from scratch in Java,” Cohen said.

Why would anyone throw away working code? Because the new team looked at the Rust codebase and saw a foreign ecosystem, they would have to learn from scratch. They had deadlines to meet and considerable Python expertise already in-house. The Rust rewrite made zero business sense, he noted.

“When this team inherited the service, they didn’t just see Rust code; they saw an entire stack,” Cohen explained.

## The 10 Times Improvement Win That Actually Mattered

But Cohen also told a different story. [Amazon’s Fire TV](https://www.amazon.com/Amazon-Fire-TV-Family/b?ie=UTF8&node=8521791011) team was dealing with aging hardware — millions of devices that were not getting any younger. Memory was the constraint, and years of [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) optimizations had hit diminishing returns, he said.

However, one engineer tried Rust. “The difference was huge. They were able to cut memory usage, not just a little bit, but by 10x,” Cohen added.

That kind of improvement gets executive attention. But the key difference was “they did not try to rewrite the entire world with Rust,” he added. They found clean API boundaries and replaced components piece by piece.

The reason the effort succeeded was that Fire TV had an actual problem that Rust solved dramatically. The first team just thought Rust was cool, Cohen suggested.

## ‘We Like Rust’ Is Not a Business Case

Cohen’s rule is that you need “at least one order of magnitude improvement over the existing technology.”

“That’s a lot. That is not a 10% speed up,” he said. “If your problem is a theoretical problem that you might hit in the future, I think you’re going to have a very hard time hitting that bar.”

At Amazon, teams mostly choose Rust for [tail latency](https://thenewstack.io/an-introduction-to-new-linux-filesystem-bcachefs/) and memory usage — not generic performance. If you’re coming from Java, rewriting in Rust won’t automatically make things faster. “The [JVM](https://thenewstack.io/introduction-to-java-programming-language/) is an incredible piece of engineering,” Cohen pointed out. Years of Java optimizations don’t just disappear because you switched languages.

Moreover, he explained that he knows a team that spent years trying to rewrite a Java service because GC pauses were killing their [P99 performance](https://thenewstack.io/rust-linux-slos-and-all-things-performance-at-p99-conf/). It seemed like the perfect Rust use case. But “it took them multiple years just to get to parity, because there were decades of optimizations in the service they were trying to rewrite.”

Even worse, “The Java code kept getting faster while they were in this multiyear rewrite effort,” he said.

## The Expert Problem

According to Cohen, teams with a Rust expert are 40% less likely to give up early. Teams without one report that Rust is harder to build with and deploy.

But you can’t just hire your way out of this. “The people you need to make Rust adoption successful; they’re not a Rust expert that gets air dropped into your company,” Cohen said. “It’s the people who know how to be effective in your organization who now become a Rust expert.”

These aren’t the evangelists posting on Reddit about memory safety. They’re pragmatists who will write bash scripts to make Rust work with your build system, he noted. They teach, they build missing tools, and they figure out how to integrate Rust with whatever infrastructure you already have.

## The Three-Month Slog

Cohen described a pattern of learning Rust. Month one involves reading the book, maybe a small pull request. Month two: “Some deep soul searching with the borrow checker, some dark places, and this is where people either push through and learn to think in Rust or they give up,” he said.

Month three: finally productive. “They aren’t experts, but they know enough to unstick themselves.”

But that’s only if they have somewhere to turn for help. Without support, “the timeline either can become much longer or people give up.”

The Fire TV team cracked this with group coding sessions — [Advent of Code](https://adventofcode.com/) problems with everyone in a room, one person driving, everyone watching. “Beginners can learn directly, and the experts can learn by teaching.”

## Tool Roulette

“Rust is just not as mature as a lot of other language ecosystems,” Cohen admitted. That means gaps. Lots of them.

When Fire TV struggled with binary size, they found [cargo-bloat](https://crates.io/crates/cargo-bloat) — a tool that shows exactly what is bloating your artifacts. Obvious in retrospect, but “everyone had to learn that knowledge somewhere.”

Ironically, the tool did not work on their embedded platform. So, they fixed it and contributed back upstream. That’s the pragmatist mindset in action, he said.

Yet sometimes the gap is bigger. For instance, [Amazon’s Aurora database](https://thenewstack.io/amazon-aurora-vs-redshift-what-you-need-to-know/) team needed to test distributed systems under network failures. No good tool existed for async Rust. So, they spent months building “[turmoil](https://tokio.rs/blog/2023-01-03-announcing-turmoil),” which “remains a key component of their capability, and the ability of many teams to test their system,” Cohen said.

## The 2 a.m. Reality Check

The tooling problem gets dangerous in production. Cohen told a story about a team whose service was slow in load tests: “Our service is slow. Have you looked at a [flame graph](https://thenewstack.io/async-rust-in-practice-performance-pitfalls-profiling/)?”

Getting flame graphs from [serverless](https://thenewstack.io/serverless/) environments is not easy. The team had to learn new tools, how to read them and what metrics mattered. But they found the problem. “They were compiling a regular expression for every single request,” he said. They fixed that and gained a 10 times performance improvement.

“Without flame graphs, they’re just making educated guesses,” Cohen said. The alternative — figuring this out at 2 a.m. when your service is melting down — is way worse, he noted.

Another team saw mysterious performance problems for weeks before discovering that their memory allocator was returning memory to the OS during drop operations, stalling the entire async runtime. It took “weeks using esoteric Linux tools” to track down.

## Pay Now or Pay Later

Cohen credits an Amazon engineer who wrote Amazon’s first Rust commit back in 2016, who put it simply: “Rust forces you to pay your technical debt upfront when it’s cheapest. Rearchitecting your application to avoid a race condition is cheaper than debugging in front. Teams that are successful with Rust have to expect some degree of upfront pain knowing that it’s going to be worth it.”

Indeed, the teams that succeed expect upfront pain and plan for it. They budget time for learning. They invest in tooling early. They accept that the existing Java/Python playbook doesn’t apply, he said.

The teams that fail treat Rust like a drop-in replacement and then act surprised when it’s not.

## The Uncomfortable Truth

Cohen indicated that he is not trying to talk anyone out of using Rust. But he said he’s seen too many failed adoptions to pretend it’s easy.

“You can’t underestimate the cost of introducing Rust into an organization,” he said. The language might be great, but organizational change is expensive. Really expensive.

For the right problems — tail latency, memory usage, reliability — Rust can be transformative. But “if you’re introducing Rust or any new technology to an organization, you need to have a real reason,” Cohen said.

The future of Rust is not just better syntax or faster compilation. It’s “building an ecosystem so good that choosing Rust becomes obvious,” he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)