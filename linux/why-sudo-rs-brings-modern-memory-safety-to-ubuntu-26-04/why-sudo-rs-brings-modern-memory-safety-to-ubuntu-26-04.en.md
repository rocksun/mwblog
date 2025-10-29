LONDON — First things, first. Chill out. Yes, Ubuntu 26.04, the next long-term support of [Ubuntu](https://ubuntu.com/), will have [sudo-rs](https://github.com/trifectatechfoundation/sudo-rs), a version of [sudo](https://www.sudo.ws/) written in memory-safe Rust. No, it’s not going to replace good-old C-based sudo. They’ll both be in there. Breathe. Relax.

No, seriously. It’s already in Ubuntu 25.10. It’s been working just fine for me. If you don’t trust it, you can control which version you use with the command:

```
update-alternatives --config sudo
```

As [Marc Schoolderman](https://www.linkedin.com/in/marc-schoolderman/?originalSubdomain=nl), the lead engineer of the sudo-rs project, explained in a presentation at  [Ubuntu Summit 25.10](https://www.reuters.com/business/autos-transportation/us-agency-asking-tesla-about-mad-max-driver-assistance-mode-2025-10-24/), rewriting the essential [sudo command](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) in Rust is not just a “porting for the sake of Rust.” It’s a deliberate redesign to address deep security, maintainability and flexibility concerns at the heart of the Linux privilege boundary.

He came on to the project when someone sent him a message asking, “‘How would you like as part of your day job to work on something that can have huge impacts, in a nice, modern programming language?’ Why not? That’s the honest answer for me.” He is clear that the rewrite serves as “a good point to rethink requirements,” allowing not only greater technical freedom, but also deeper community contribution. Sudo-rs’s reduced code size and expressive Rust semantics make it far easier for outside contributors to propose enhancements.

He and his fellow developers are doing this work hand in glove with [Todd Miller](https://www.linkedin.com/in/millert/). Todd who? You know the guy who is the sole maintainer of sudo and is currently searching for a sponsor to fund continued sudo maintenance. You know the [xkcd cartoon of the world’s modern digital infrastructure depending on a single developer in Nebraska](https://xkcd.com/2347/)? That’s Miller, except he lives in Colorado. We need a modern, more memory-safe version of sudo, that’s sudo-rs, and Miller also needs our support.

## The Motivation for Rewriting Sudo in Rust

That said, Schoolderman explained that sudo-rs got its start in 2023 through the [Internet Security Research Group](https://www.abetterinternet.org/) as part of its [Prossimo](https://www.memorysafety.org/) initiative to rewrite critical open source utilities in safe languages.  In particular, they targeted ubiquitous utilities that live on the security boundary and are not yet implemented in modern memory-safe languages.

While improved memory safety — [Rust’s defining virtue](https://thenewstack.io/rust-programming-language-guide/) — is central, as up to 30% of sudo’s serious vulnerabilities historically stem from memory issues, Schoolderman emphasizes that Rust’s expressive type system and the ease of refactoring it provides are equally transformative for maintainability and auditing.

Instead of blindly copying every legacy feature, sudo-rs’s team uses the opportunity to rethink requirements and streamline features, optimizing for both security and relevance in modern systems.

## Understanding Sudo-rs in Ubuntu

That means sudo-rs’s goal is to be a drop-in replacement for all of sudo’s everyday use cases. For sudo config syntax, this means it supports the default configuration files for common Linux distributions and FreeBSD. “Our implementation should support all commonly used command line options from the original sudo implementation.”

But, and this is important, some parts of the original sudo are explicitly not in scope. Sudo has a large and rich history, and some of the features available in the original sudo implementation are largely unused or only available for legacy platforms.

So, rather than cloning all aspects of the legacy sudo, not every “quirky” feature or infrequently used capability is included. Yes, that means your “essential” sudo feature may not be included. But do you really need it? Check it and see. And, if you really, really do need it, let the developers know, and maybe they’ll include it. Besides, remember, sudo isn’t going anywhere. You can just use it instead.

Besides making sudo-rs safer, another reason for the refactoring was, “There’s a lot of business logic in sudo going on, and if you’re using Rust, you have a modern language that has a very expressive type system, and it’s much easier to express the logic in a way that’s maintainable and readable.”

In addition, Schooderman said, “The biggest benefit of using Rust for sudo-rs from our team has not necessarily been the memory safety issue, although that’s nice, but you get it for free. The biggest benefit is having a smaller codebase that’s easier for external users to look into.”

He continued, “We put sudo on a diet, and we actually brought it down to, I think, three direct dependencies, and they’re all maintained by the Rust project. So I think sudo is a very lean project, and we want to keep it that way.”

## Collaboration with the Original Sudo Maintainer

Schoolderman continued that sudo-rs incorporates lessons from decades of sudo development while actively collaborating with Miller. He has both advised Schoolderman’s team and contributed to bug fixes in sudo-rs. This has led to direct cross-pollination between projects: sudo-rs’s comprehensive tests have even uncovered vulnerabilities in the original sudo, which Miller quickly patched.

Rather than being rivals, sudo-rs and sudo are complementary, and their developers are helping each other make both better.

In 2025, [Canonical decided to make sudo-rs the default sudo implementation for Ubuntu 25.10](https://thenewstack.io/ubuntu-25-10-replaces-sudo-with-a-rust-based-equivalent/). This includes funding milestones for Ubuntu compatibility, such as NOEXEC shell escape prevention and AppArmor controls. By aiming for backward compatibility where it matters (legacy scripts and workflows), Canonical ensures smooth transitions, rigorously testing sudo-rs performance and reliability for the upcoming Ubuntu LTS release in 2026. Canonical’s leadership hopes to inspire other major distributions to join them.

The [Trifecta Tech Foundation](https://trifectatech.org/) now oversees the project’s governance and funding. This ensures a well-maintained and diverse team beyond the “bus factor” of single-maintainer risk.

The hope is that the transition to sudo-rs will deliver fewer security patches, reduced downtime from exploits and a modernized, streamlined codebase that’s easier for newcomers and maintainers alike to audit and extend.

## The ‘Less is More’ Design Philosophy of Sudo-rs

So sudo-rs embodies a “less is more” philosophy, omitting bloat and focusing on robust essentials. System administrators and security engineers should appreciate this change.

Will it work? Stick around and find out, or start experimenting with Ubuntu 25.10 or one of the other many distros that support it as an option today, such as Arch, Fedora, Debian or NixOS.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)