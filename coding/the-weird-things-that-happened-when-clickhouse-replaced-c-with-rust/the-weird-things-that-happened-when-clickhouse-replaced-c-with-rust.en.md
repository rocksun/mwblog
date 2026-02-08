ClickHouse’s decision to shift parts of its codebase to [Rust](https://thenewstack.io/rust-programming-language-guide/) is a perfect storm: the convergence of a wildly popular database and a language riding a massive wave of momentum. While ClickHouse has earned its adoption for good reason, Rust’s momentum as a beautiful, modern programming language arguably deserves its explosive growth and its emergence as a language of choice — not just for ClickHouse in this case, but across many projects, including parts of the [Linux kernel,](https://thenewstack.io/rust-in-the-linux-kernel/) replacing [C code,](https://thenewstack.io/the-obfuscated-c-code-competition-returns/)

That said, on Sunday at [FOSDEM 2026](https://fosdem.org/2026/) here in Brussels, [Alexey Milovidov](https://www.linkedin.com/in/alexey-milovidov-clickhouse/?originalSubdomain=nl), co-founder and CTO of ClickHouse was very precise about what interested him: not hype, but what Rust can concretely do for ClickHouse during this [talk](https://fosdem.org/2026/schedule/event/NBLNRY-rust-clickhouse/) “Clickhouse’s C++ and Rust Journey.” In fact, he explicitly pushed back on the hype, even calling it one of Rust’s negative aspects amid the Rust-heavy interest — that I would argue was merited — at FOSDEM this week.

There was huge interest in the how and why behind ClickHouse’s move toward Rust, and it’s worth noting that the transition hasn’t been without hiccups and not representing a big shift as many might think. In fact, about 98% of Clickhouse’s runtimes remain in C++, Milovidov told *The New Stack.*

Before getting into those details, though: After his talk on Sunday, I asked Milovidov what surprised him most over the past couple of weeks. His answer wasn’t about Rust itself, but about something unexpected that had happened very recently, which he said caught him off guard.

During our discussion, Milovidov said the “weirdest” challenges his team faced during the ongoing shift to Rust had to do with the  build system and build infrastructure. A specific example involved the Delta kernel library, which he found to be disabled under the memory sanitizer. The issue stemmed from how the library did not provide certain symbols required for the memory sanitizer to function correctly, an issue he identified only a “day or two” before his talk and our conversation. This underscored the difficulty of maintaining a rigorous testing environment when mixing different language ecosystems.

“The Delta kernel library is disabled under the memory sanitizer…some some symbols required for members are not provided,” Milovidov said. “The was weird.”

Much of our discussion involved the clarified ClickHouse’s use of Corrosion, an open source tool for integrating C++ and Rust. There was a point of clarification regarding the direction of the migration: it was not a move from Corrosion to C++, but rather building on the C++ while the Rust code remained. Milovidov confirmed that the Rust code did not change and the libraries stayed the same. Instead of translating the code, they were going to continue building in Rust.

During his talk, Milovidov recalled that initially when making the switch to Rust, there were issues with a library that did not provide some symbols, as mentioned above. Milovidov stated that cross inflation was much better, though the team faced a huge amount of effort that was not easy. He observed that for some reason, the system ended up with two different versions of open SSL. Finally, he mentioned that they could make it run in their rooms and glue it in the same way to avoid surprises with symbols.

“This and the entire project required a huge amount of effort,” Milovidov said. “It was not easy.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)