# Rust Integration in Linux Kernel Faces Challenges but Shows Progress
![Featued image for: Rust Integration in Linux Kernel Faces Challenges but Shows Progress](https://cdn.thenewstack.io/media/2025/02/9fc50f48-getty-images-1lk8lc-xq44-unsplash-1024x683.jpg)
The conflict between Rust and C supporters in the Linux kernel has been growing for some time. A [Linus Torvalds](https://www.linkedin.com/in/linustorvalds/), [Linux](https://thenewstack.io/rust-in-the-linux-kernel/)’s creator, said in [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) in August 2024, the [disagreements have risen to “almost religious war undertones.](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/)” Since then, things have grown even more hostile.

Why? [Dan Williams](https://www.linkedin.com/in/djbw/), senior principal engineer on Intel’s Linux core kernel architecture team, explained at the [Linux Plumbers 2024](https://lpc.events/event/18/timetable/) meeting, “[Kernel maintainers tend to be very conservative.](https://www.zdnet.com/article/rust-in-linux-now-progress-pitfalls-and-why-devs-and-maintainers-need-each-other/) They know C backward and forward, but they don’t know Rust. So, they “don’t know how to review this or debug that because they don’t understand the code.”

The same is true, however, for Rust developers trying to work with the Linux kernel’s C foundations. The latest flare-up resulted from a request to add a [patch for Rust for the Linux kernel’s Direct Memory Access (DMA) Application Programming Interface (API)](https://lore.kernel.org/rust-for-linux/20250108122825.136021-3-abdiel.janulgue@gmail.com/#r) transfers in January. This functionality is necessary for Rust device drivers to have usable data input/output (I/O).

## Rust Code and C APIs
Prominent software engineer and Linux kernel maintainer Christoph Hellwig wanted nothing to do with this. He replied, “[No rust code in kernel/dma, please.](https://lwn.net/ml/all/20250108135951.GA18074@lst.de/)” That’s an odd position since the [patch did not put any code in that directory](https://lwn.net/SubscriberLink/1006805/f75d238e25728afe/).

When Miguel Ojeda, overseer of the [Rust for Linux](https://rust-for-linux.com/) project, asked Hellwig to suggest an alternative, he replied that Rust developers should “[Keep the wrappers in your code](https://lwn.net/ml/all/20250108151858.GB24499@lst.de/) instead of making life painful for others.” Getting to the heart of the matter, in another Linux Kernel Mailing List (LKML) note, Hellwig wrote, “[Maintaining multi-language projects is a pain](https://lwn.net/ml/all/20250110083955.GA5395@lst.de/) I have no interest in dealing with. If you want to use something that’s not C, be that assembly or Rust, you write to C interfaces and deal with the impedance mismatch yourself.”

## Is Rust Harder for Maintainers?
As an alternative,[ Red Hat](https://www.openshift.com/try?utm_content=inline+mention) engineer and kernel developer [Danilo Krummrich](https://de.linkedin.com/in/danilo-krummrich-796885153) “offered to [maintain the Rust abstraction layer for the DMA](https://lwn.net/ml/all/Z5qeoqRZKjiR1YAD@pollux/) coherent allocator as a separate component.” Krummrich added that the [Rust for Linux](https://thenewstack.io/fosdem-2025-rust-runs-riot-in-linux-despite-backlash/) developers are writing Rust code that would abstract the C APIs for all Rust drivers and be maintained by Rust developers.

That doesn’t work for Hellwig, either. He replied, “I also do not want another maintainer. If you want to make Linux impossible to maintain due to a cross-language codebase, do that in your driver so that you have to do it instead of spreading this cancer to core subsystems.”

[“Cancer](https://www.theregister.com/2001/06/02/ballmer_linux_is_a_cancer/),” thanks to Steve Ballmer’s criticism of Linux, has always been a red-letter term in [Linux circles](https://thenewstack.io/learning-linux-start-here/). A lot of heated words followed. I think senior Linux kernel developer Ted T’so, though, hit the nail on the head when he said that, Ultimately, [Cristoph’s concern is that Rust is going to make life harder for maintainers ](https://lore.kernel.org/lkml/20250208204416.GL1130956@mit.edu/)because of particular build breaks getting in the way of the very limited bandwidth that Maintainers have. In short, it’s not so much that kernel maintainers think Rust is awful; they don’t have enough hours in the day to maintain their projects.
## ‘Rust Device Driver Mess’
Be that as it may, one maintainer, [Asahi Linux](https://asahilinux.org/) lead developer Hector Martin, called on Torvalds to “pipe up with an authoritative answer” to resolve the Rust device driver mess. “If he doesn’t, Miguel and the other Rust folks should just merge this series once it is reviewed and ready, ignoring Christoph’s overt attempt at sabotaging the project.” When that didn’t work, Martin took to “shaming on social media” to carry his point. Torvalds was not amused.

Torvalds replied, “How about you accept the fact that maybe the problem is you? You think you know better. But the current process works. It has problems, but problems are a fact of life. There is no perfect.” That said, Torvalds continued, “If we have issues in the kernel development model, then [social media sure as hell isn’t the solution](https://lkml.org/lkml/2025/2/6/1292). The same way, it sure as hell wasn’t the solution to politics.”

Martin responded by dropping out of the Linux Apple/ARM platform development, saying, “[I no longer have any faith left in the kernel](https://lore.kernel.org/lkml/20250207-rm-maint-v1-1-10f069a24f3d@marcan.st/#r) development process or community management approach.”

## Lessons From Real-Time Linux
So, what can be done moving forward with Rust and Linux? Senior real-time Linux developer Steven Rostedt suggested the Rust developers might follow in the footsteps of [real-time Linux, which took twenty years to join the mainline Linux kernel](https://www.zdnet.com/article/20-years-later-real-time-linux-makes-it-to-the-kernel-really/); that was to “[keep [Rust as] an out of tree patch](https://lkml.org/lkml/2025/2/7/1955). … Yes, being out of tree is very difficult because you have to constantly rebase … But it also gives you full flexibility to try new approaches. Just because something is out of tree doesn’t mean it can’t be published and used. Red Hat and SUSE, as well as many others, shipped PREEMPT_RT while it was out of tree.”

Since then, Ojeda published a “[Rust kernel policy](https://rust-for-linux.com/rust-kernel-policy)” document to clarify the status of Rust integration efforts. This move came in response to growing confusion and debate within the Linux community regarding the role of Rust in kernel development.

This document addresses several crucial points, including kernel maintainers’ expected level of support. Ojeda noted that it continues to be up to each maintainer to decide how to deal with Rust. “Some subsystems may decide they do not want to have Rust code for the time being, typically for bandwidth reasons. This is fine and expected.” So, while some developers want Rust to move much more quickly into the kernel, Hellwig’s position is perfectly defendable.

Indeed, Ojeda continued, “For Rust, a subsystem may allow to temporarily break Rust code. The intention is to facilitate the friendly adoption of Rust in a subsystem without introducing a burden to existing maintainers who may be working on urgent fixes for the C side. The breakage should nevertheless be fixed as soon as possible, ideally before the breakage reaches Linus.”

## Rust Integration With Linux
When it comes to Rust’s integration with Linux, unlike the tech mantra of “move fast and break things,” the rule is to “move slow and stabilize things.” After all, despite all the harsh words, Rust’s integration into Linux continued to move forward.

For example, the Linux 6.13 kernel, released in January 2025, brought significant expansions to Rust support. This [kernel introduced in-place modules](https://www.phoronix.com/news/Linux-6.13-char-misc-More-Rust), bindings, and trace events for Rust developers. What that means, explained [Greg Kroah-Hartman](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/), the Linux stable release maintainer, is that [Rust support is at “the tipping point;](https://lore.kernel.org/lkml/Z0lG-CIjqvSvKWK4@kroah.com/) expect to see way more rust drivers going forward now that these bindings are present.

Next merge window, hopefully, we will have PCI and platform drivers working, which will fully enable almost all driver subsystems to start accepting (or at least getting) rust drivers. This is the end result of a lot of work from a lot of people, congrats to all of them for getting this far, you’ve proved many of us wrong in the best way possible, working code.”

In short, for all the war of words, Rust’s movement into Linux continues to be slow, steady, and productive, as we can see in 6.13. Rust will find its place in Linux.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)