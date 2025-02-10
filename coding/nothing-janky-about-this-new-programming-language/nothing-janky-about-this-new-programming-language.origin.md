# Nothing Janky About This New Programming Language
![Featued image for: Nothing Janky About This New Programming Language](https://cdn.thenewstack.io/media/2025/01/1d056ff7-fredrick-tendong-hvyepjyehdq-unsplash-1-1024x683.jpg)
With [programming languages](https://thenewstack.io/programming-languages/) among the top interests of TNS readers, we are constantly on the lookout for new languages that could have a potential impact on developers. [Jeaye Wilkerson](https://www.linkedin.com/in/jeaye/)’s [jank](https://jank-lang.org/) is a dialect of [Clojure](https://thenewstack.io/stack-overflow-rust-remains-most-favored-but-clojure-pays-the-most/) that he says can be used anywhere C++ and Lua are used. It is a general-purpose language aimed at gaming and other use cases.

jank includes Clojure’s code-as-data philosophy and strong macro system. It is a functional-first language that builds upon Clojure’s rich set of persistent, immutable data structures, Wilkerson said.

TNS News Editor Darryl K. Taft interviewed Wilkerson, who recently quit his job at Electronic Arts (EA) to focus full-time on jank, about his creation.

**What was the tipping point that made you decide to work on jank full-time?**
**Wilkerson: **jank has been ramping up over the past two years, since I switched to part-time at EA. At this point, it’s an incredibly popular project, for something which is unreleased, and I still didn’t feel like I had enough time to work on it. I had been considering working on jank full-time for months. I suppose the tipping point was when my wife said something along the lines of “Well, are you going to do it or not?”
**What were the key technical challenges in developing jank?**
**Wilkerson:** jank is marrying Clojure and the native world. The two could not be more dissimilar. To get Clojure running in a native environment, we first needed to be able to JIT compile native code. The tooling around this is still young and I’ve had to work closely with multiple [LLVM](https://llvm.org/) devs to get issues fixed.
Beyond that, Clojure is built on the [JVM](https://www.ibm.com/docs/en/b2b-integrator/6.1.1?topic=management-java-virtual-machine), which has decades of development put into it. To replicate that on native, I need to effectively build a mini VM myself. This includes the object model, the module loader, the JIT compiler, and the garbage collector, to name a few. I use off-the-shelf solutions where possible, but everything needs to be put together manually.

Lastly, jank aims to provide seamless interop with C++ from an entirely dynamic language. This requires JIT compiling C++ at runtime so that we can know the types of values, look up which functions exist, do overload resolution, instantiate templates, and carry on C++’s RAII guarantees. There is no mainstream dynamic language which has this level of interop with C++, from what I’ve seen. The primary reason is that it’s incredibly difficult.

**What’s your vision for jank’s development over the next year?**
**Wilkerson:** In 2025, I will release an alpha version of jank for people to start using. I’ll collect feedback, improve stability, and start changing the Clojure ecosystem to be one which has first-class support for native.
**How are you approaching sustainability/funding for jank’s development?**
**Wilkerson:** This year, I’m just focused on getting jank out the door. I’m prepared to not receive any funding, if none comes in. However, in the past, jank has received open source grants from [Clojurists Together](https://www.clojuriststogether.org/) and I will continue to apply for those. It’s my dream that I can be paid to work on jank full-time, but in order to do that I need jank to start providing value and become and indispensable part of Clojure’s ecosystem. If that doesn’t happen, it’s no problem. I’ll get another job when I need to, but I’ll keep working on jank either way.
**Are you working completely solo, or do you have any collaborators/contributors?**
**Wilkerson:** I’m the only one working on jank full-time, but I do have some regular contributors. I also have three mentees, as part of the [SciCloj](https://scicloj.github.io/) mentorship program, with whom I meet weekly and give them tasks which further develop jank and their compiler hacking skills.
Building a healthy community is important to me. Encouraging people to help out, and making it easy for them to do so, is part of that.

**Are you looking to build a community around jank? If so, what kind of contributions would be most valuable?**
**Wilkerson:** Absolutely. In the coming weeks, jank will get easier and easier to install. As of today, it can now be installed via homebrew, which wasn’t possible last month, for example. As jank becomes more accessible, having people try it, provide feedback, and, more importantly, report bugs will be crucial to jank having a stable launch later this year.
**How does jank handle performance optimization, particularly for resource-intensive applications?**
**Wilkerson:** jank is written in C++ and has seamless C++ interop, but it’s not C++. It’s not a systems programming language. It’s a Clojure dialect and it has the same performance characteristics of Clojure. jank will do well anywhere Clojure does well, and perhaps in other places, too, since it’s lighter in memory usage and starts up much faster.
With that said, after I reach parity with[ Clojure](https://thenewstack.io/from-c-to-clojure-new-language-promises-best-of-both) and I continue to develop jank’s feature set beyond that, I will be adding more control on the spectrum of dynamism so that some parts of jank can be locked down, with little to no dynamic allocations, using static typing and monomorphized functions.

Clojure, historically, has not had a strong focus on optimizing its compiler. It relies on the JVM for all of the heavy lifting. jank will not follow that path; I think that a smarter compiler can make all the difference and every low hanging fruit will be plucked.

**Are there any specific technical decisions or trade-offs you made that you think would be interesting for other developers to understand?**
**Wilkerson:** The JVM is a heavily optimized machine. Competing with it, from the ground up, is tough, even starting on native. In the micro-benchmarking I’ve done, jank is quite competitive with Clojure, but I’ve done this by taking advantage of the fact that I’m building a system specifically for jank while the JVM is a much more generic system. An example of that is jank’s object model, which doesn’t use virtual dispatch to avoid the cost of vtables. [This is documented here: [https://jank-lang.org/blog/2023-07-08-object-model/](https://jank-lang.org/blog/2023-07-08-object-model/)]
**What advice would you give to other developers considering a similar move with their projects?**
**Wilkerson:** You only live once.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)