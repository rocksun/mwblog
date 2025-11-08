Clickhouse is an open source analytics-oriented database system composed of 1.5 million lines of code, mostly in C++, a notoriously unsafe language in terms of hiding bugs that could be exploited by malicious attackers.

Often it has been written, [even here at The New Stack](https://thenewstack.io/rust-vs-c-a-modern-take-on-performance-and-safety/), that the [Rust programming language](https://thenewstack.io/rust-programming-language-guide/) could replace [C/C++](https://thenewstack.io/introduction-to-c-programming-language/) with its superior handling of memory and thread safety. And there are many large code bases, such as the [Linux kernel](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/) (C) and Windows (C++) written with some decades-old variant language, so many are asking themselves the same questions.

The maintainers of Clickhouse started down that path, with the aim of converting the functionality of Clickhouse written in C++ code. And maybe even rewrite the entire code base itself.

The operational question was, “if we started today, would we write Clickhouse in Rust?” asked [Alexey Milovidov](https://github.com/alexey-milovidov), CTO and cofounder of [Clickhouse](https://clickhouse.com/), who discussed the results in [a talk](https://www.p99conf.io/session/clickhouses-c-rust-journey/) at [ScylaDB](https://www.scylladb.com/?utm_content=inline+mention)‘s [virtual P99 Conf](https://www.p99conf.io/).

In the end, the core developers took a more incremental route to migration, Milovidov explained. They first integrated Rust into the build system, then they built out modules for various functionalities.

Along the way, they encountered numerous challenges, including ensuring reproducible builds and managing dependencies.

“Rust may be perfect, but when you use C+ and Rust together, it could be problematic,” Milovidov advised.

## The Price of C++ Is a Humongous Build System

Writing a mission-critical app in C++ still comes with many advantages, as Milovidov pointed out. “It is well established. It is well recognized. It is quite popular. It is easy to hire people with C++ knowledge. Universities still teach C,” he said.

But using C++ requires “so many efforts,” he lamented. It is “almost inevitable” that you will run into security issues around memory corruptions, segmentation faults, or race conditions, he added.

In fact, Clickhouse ended up building a “gargantuan” [CMake](https://cmake.org/)-based [continuous integration system](https://thenewstack.io/ci-cd/) just to ensure all these types of bugs were caught and fixed.

From an average of 70 pull requests and 145 commits a day, the CI system produces “10s of billions of tests,” which is actually “10s of millions” of individual tests done in varying combinations — all to ensure the new code doesn’t come with any new bugs.

[![Presentation slide](https://cdn.thenewstack.io/media/2025/10/599a26c7-clickhouse-01.jpg)](https://cdn.thenewstack.io/media/2025/10/599a26c7-clickhouse-01.jpg)

Is C++ a pain? Milovidov had a whole slide on the subject…

## The Rust Journey

“So maybe it’s time to rewrite in Rust,” the core dev team wondered. The language offered both memory and thread safety. It also offered more libraries, especially around the emerging data standards such as [Apache Iceberg](https://thenewstack.io/dispelling-myths-of-open-source-complexity-with-apache-iceberg/). And the language seemed to be attracting all the young, ambitious software engineers.

Yet, a full rewrite of [Clickhouse](https://github.com/ClickHouse/ClickHouse) into Rust would take years.

Instead, the team decided on an iterative approach, where various pieces of the Clickhouse system could be redone in Rust. They’d use [Corrosion](https://github.com/corrosion-rs/corrosion) to integrate with CMake.

First, they added a small function to [SQL](https://thenewstack.io/to-sql-or-not-to-sql-that-is-not-the-question/), one for [BLAKE3 hashing](https://github.com/BLAKE3-team/BLAKE3), written in Rust and [wrapped for C++.](https://github.com/ClickHouse/ClickHouse/pull/33435) Then they augmented the command line interface, [`clickhouse-client`](https://clickhouse.com/docs/interfaces/cli), with better history and navigation, thanks to an outside contributor. They also accepted a pull request for an alternative to SQL, a library called the [PRQL](https://prql-lang.org/) (Pipelined Relational Query Language), written in Rust.

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/0ed32157-clickhouse-02.jpg)](https://cdn.thenewstack.io/media/2025/11/0ed32157-clickhouse-02.jpg)

With their confidence in Rust growing, the projects got larger. The next Rust test was to integrate a Rust-based library for the emerging [Delta Lake format](https://thenewstack.io/delta-lake-a-layer-to-ensure-data-quality/), the [Delta-kernel-rs](https://docs.rs/delta_kernel/latest/delta_kernel/) library. Here was a case where a library is available in Rust before one would be available, if ever, in C++.

Clickhouse could have written a library in-house, in C++ , for Delta Lake, but the work would have been “pointless,” Milovidov said. Pity the poor programmer who would spend time writing code for parsing JSON files and redirecting HTTP requests. It was just easier to use the official Databricks Rust-based release.

## Dangers With Rust and C++

Through these experiments, the Clickhouse devs learned about some shortcomings with Rustlang, especially when used in conjunction with C++.

One challenge was reproducible builds, which are necessary to ensure the code is safe, and not accidentally downloaded from the internet somewhere. Clickhouse had gone through the process of ensuring reproducible builds in C++, but with Rust, they had to think through the process of how to ensure hermetic builds again.

Writing C++ wrappers for Rust programs is also a challenge. Sussing out whether to allocate memory in C++ or Rust can be tricky. [Fuzzing tools](https://thenewstack.io/developers-are-buzzing-on-fuzzing/) and Clickhouse’s CI system help find errors a lot here.

There were differences in how each language performed under duress.

Compared to C++, Rust programs and libraries tend to panic too much for Milovidov’s liking. The panics may be due to a bug (indicating that better testing was needed of the library). Or the code’s author used the panic termination in place of [calling an exception](https://learn.microsoft.com/en-us/cpp/cpp/errors-and-exception-handling-modern-cpp?view=msvc-170) (which tends to be [frowned upon by Rustaceans](https://doc.rust-lang.org/book/ch09-00-error-handling.html)).

Panic is cool with batch jobs, but very much less cool with server and interactive applications that are running live in real time.

“Libraries in Rust tend to use Panic too much, even when it is not appropriate, and we have to find and fix all these cases just to avoid abrupt termination of our server application,” Milovidov said.

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/a5e086de-clickhouse-03.jpg)](https://cdn.thenewstack.io/media/2025/11/a5e086de-clickhouse-03.jpg)

Rust code shouldn’t panic so much, Milovidov asserted.

And just as the Clickhouse team has found bugs that needed fixing in C++ libraries, so too have they found plenty of bugs in Rust libraries as well.

Milovidov also delved the into many peculiarities that come about specifically by intermingling C++ and Rust in the same environment, with specific issues around using sanitization, managing cross-dependencies, and cross-compilations, and code composability for the developer. And many of these issues stem from the complexity of the required build system.

One other unexpected side effect of moving to Rust: More dependencies. For the entire codebase, Clickhouse had only 156 dependencies. When the Rust modules were brought in, they found themselves managing an additional 672 transitive Rust dependencies (Still not as much as they would have with [NPM](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/), Milovidov quipped).

## Clickhouse’s Takeaway

For now, anyway, Clickhouse has decided against rewriting the entire database system in Rust. But it is confident enough with the language that it is allowing third-party contributors to submit their own Clickhouse add-ons in the language.

“Rust is a great language,” Milovidov said.

*To hear the [entire presentation](https://www.slideshare.net/slideshow/clickhouse-s-c-rust-journey-by-alexey-milovidov/283656249?from_action=download_slide&slideshow_id=283656249&index=0), sign up for the [P99 Conf](https://www.p99conf.io/).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)