# FOSDEM 2025: Rust Runs Riot in Linux Despite Backlash
![Featued image for: FOSDEM 2025: Rust Runs Riot in Linux Despite Backlash](https://cdn.thenewstack.io/media/2025/02/1d3d9a33-img_9596-1-1-1024x683.png)
[Rust](https://thenewstack.io/big-moments-in-rust-2024/) should eventually replace [C code](https://thenewstack.io/the-obfuscated-c-code-competition-returns/) in the [Linux kernel](https://thenewstack.io/rust-in-the-linux-kernel/). The rub is that you’ll have to wait decades for it to happen. But in the near term, expect to see a surge in Rust code that powers Linux in anything from edge devices to Microsoft’s Xbox — while many, including some maintainers of the Linux kernel, are not happy about it.
Rust owes its rising popularity in the kernel and has long proven its superiority over C in a wide variety of use cases for the Linux kernel and elsewhere, particularly for memory security. And yet, Rust is not without its own risks versus C in the kernel, its very steep learning curve to use not withstanding. More developers and kernel maintainers love Rust, but contention exists within the kernel development community between those pro-Rust and –C camps, which has continued this week through heated exchanges.


[@fosdem]25: let’s just say there are many strong opinions about[@rustlang]´s place in the[@Linux]kernel, as Rust for Linux ´s Miguel Ojeda described, nuances and caveats included.[pic.twitter.com/qYOUzB2fBG]— BC Gain (@bcamerongain)

[February 1, 2025]
Rust-related dynamics were a major subject of discussion at [FOSDEM (Free and Open Source Developers’ European Meeting),](https://fosdem.org/) a leading open source conference organized by volunteers held at Université Libre de Bruxelles (ULB) in Brussels. Among dozens of Rust-related talks, the eponymously called [Rust for Linux](https://rust-for-linux.com/) talk stood out, given by [Miguel Ojeda,](https://www.linkedin.com/in/ojedamiguel/?originalSubdomain=es) who maintains the project and is a member of the Linux Foundation technical advisory board. In addition to discussing the Rust for Linux project, he covered the status of the distribution toolchain, Rust stability and importantly, how you can contribute to the kernel’s development. The Rust for Linux program is also collaborating with GCC and other organizations in ways to promote the addition of Direct Memory Access (DMA) Rust abstractions in the Linux kernel.

Google has been a staunch supporter of [adding Rust to the kernel](https://thenewstack.io/rust-in-the-linux-kernel/) for Linux running in its Android phones. The use of Rust in the kernel is seen as a way to avoid memory vulnerabilities associated with [C and C++ code](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) and to add more stability to the Android OS. “Google’s wanting to replace C code with Rust represents a small piece of the kernel but it would have a huge impact since we are talking about billions of phones,” Ojeda told me after his talk.

In addition to Google, Rust adoption and enthusiasm for it is increasing as Rust gets more architectural support and as “maintainers become more comfortable with it,” Ojeda told me. “Maintainers have already told me that if they could, then they would start writing Rust now,” Ojeda said. “If they could drop C, they would do it.”

Kernel developers:

[@Linus__Torvalds]at[#OSSummit]: « For some reason the whole[@rustlang]versus C discussion is taking almost religious overtones. »[@thenewstack][pic.twitter.com/6TL7CaViRK]— BC Gain (@bcamerongain)

[September 16, 2024]
What Ojeda did not cover during his talk was the most recent backlash against those maintainers reluctant to mix C and Rust code in the container. In September, [Linus Torvalds](https://www.linkedin.com/in/linustorvalds/), Linux’s creator, described the controversy as having “almost religious war undertones” during his [Open Source Summit](https://events.linuxfoundation.org/open-source-summit-europe/) keynote. Torvalds then said that while the controversy involves healthy arguments, some are becoming very negative.

At issue is a cultural clash between the C language and the Rust language when it comes to submitting changes across language boundaries. Modifying something that’s a C interface on behalf of Rust people might make sense from the Rust point of view (and vice versa), while the C people seek Rust contributions to plug into C.

The controversy traces back to over three years ago when the idea was introduced that Rust, offering certain security benefits that C did not, could become part of the kernel and potentially replace it. Despite this, the project didn’t come to a standstill.

For example, the famous buffer overflow hacks or vulnerabilities that could be generated with C and a CPU have now become almost outdated. While Rust offers certain security features and drawbacks, it’s also much harder to learn compared to C, which is easier to grasp.

In a recent exchange between the pro-Rust and -C camps, software engineer and Linux kernel maintainer [Christoph Hellwig](https://ostconf.com/en/materials/2307) [wrote in an email](https://lore.kernel.org/rust-for-linux/2b9b75d1-eb8e-494a-b05f-59f75c92e6ae@marcan.st/T/) in early January: “No rust code in kernel/dma, please.” His message was in response to a request to add a [patch](https://lore.kernel.org/rust-for-linux/20250108122825.136021-3-abdiel.janulgue@gmail.com/#r) for Rust for the DMA API in the Linux kernel. In January during a more recent back-and-forth, the discussion heated up further on the eve of the FOSDEM fringe meetings on Wednesday.

(In 2016, Hellwig lost as the plaintiff in a lawsuit in a German court against then VMware, claiming vSphere infringed on an open source license. The German court in Hamburg dismissed the lawsuit.)

Last week, Hellwig rejected communications by Red Hat engineer and kernel contributor [Danilo Krummrich’s](https://de.linkedin.com/in/danilo-krummrich-796885153) support for adding Rust abstractions for C APIs.

Krummrich had offered that the Rust abstraction layer be maintained for the DMA coherent allocator to serve as a “separate component.” Hellwig then replied to Krummrich’s proposal last week:

“Which doesn’t help me a bit. Every additional bit that the another language creeps in drastically reduces the maintainability of the kernel as an integrated project. The only reason Linux managed to survive so long is by not having internal boundaries, and adding another language completely breaks this. You might not like my answer, but I will do everything I can do to stop this. This is NOT because I hate Rust.

While not my favourite language it’s definitively one of the best new ones and I encourage people to use it for new projects where it fits. I do not want it anywhere near a huge C code base that I need to maintain.”
## The Rust Rush
Amid the controversy, there has been a steady stream of vocal support for Ojeda. Much of his discussion also covered statements given by advocates for Rust in the kernel, ranging from lead developers of the kernel and including Linux creator Linus Torvalds himself to technology leads from [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), Samsung, [Google](https://cloud.google.com/?utm_content=inline+mention), Microsoft and others.

During his talk, Ojeda reiterated a statement he previously wrote in an [email message](https://lore.kernel.org/lkml/20210414184604.23473-1-ojeda@kernel.org/) to Torvalds in 2021 that he says still holds true today:

“By using Rust in the Linux kernel, our hope is that:

‒ New code written in Rust has a reduced risk of memory safety bugs, data races and logic bugs overall, thanks to the language properties mentioned below.

‒ Maintainers are more confident in refactoring and accepting patches for modules thanks to the safe subset of Rust.

‒ New drivers and modules become easier to write, thanks to abstractions that are easier to reason about, based on modern language features, as well as backed by detailed documentation.

‒ More people get involved overall in developing the kernel thanks to the usage of a modern language.

‒ By taking advantage of Rust tooling, we keep enforcing the documentation guidelines we have established so far in the project. For instance, we require having all public APIs, safety preconditions,

`unsafe`
blocks and type invariants [sic] documented.”
Meanwhile, the choice between the use of Rust and C is not necessarily an either/or issue. Again, C will be in use in a number of the kernel layers and specifications indefinitely, I would argue. After all, the old adage applies that “if it ain’t broke, then don’t fix it.”

“Some maintainers don’t want to drop C,” Ojeda told me. “But when C is no longer used depends on the maturity. It depends on the substrate and the maturity of the architecture, which varies.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)