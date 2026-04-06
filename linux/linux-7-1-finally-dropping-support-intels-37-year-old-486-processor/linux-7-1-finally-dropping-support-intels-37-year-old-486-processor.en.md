### Summary

* Linux 7.1 begins sunsetting built-in support for i486 CPUs.
* Linus says it's time to leave i486 behind as compatibility glue wastes dev time and causes issues.
* Keep using an LTS kernel or older distro if you run an i486; modern kernels may drop support.

Linux is well-known for supporting old hardware. If you have an aging PC and want to install an operating system on it that's still supported by its creators, there's a very good chance you can squeeze a modern-day Linux distro on it, and it'll run just fine. However, it seems that there is a limit to what the Linux community deems appropriate to continue supporting.

There's a proposed change for Linux version 7.1 that, if merged, will begin the process of dismantling the support for Intel's 486 processors. And if you're not sure what that is, you may be surprised to learn that the processor could be older than you.

![A laptop shwoing the KDE Plasma desktop with apps including Affinity and Vivaldi open](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/linux-laptop-with-kde-plasma.jpg?q=49&fit=crop&w=220&h=182&dpr=2)
Related

I know it's not perfect, but I love it

## Linux 7.1 begins sunsetting support for a 37-year-old processor

### The i486 was legendary, but all legends need to move on eventually

![Running Tmux and a couple of apps on the Linux terminal](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/01/linux-tmux.jpg?q=49&fit=crop&w=825&dpr=2)

As spotted by [Phoronix](https://www.phoronix.com/news/Linux-7.1-Phasing-Out-i486), there's a new change that's queued up to merge into Linux 7.1. Authored by Ingo Molnar, the change, titled "[x86/cpu: Remove M486/M486SX/ELAN support](https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/platform&id=8b793a92d862c89055daa97ffa61a6929cf732f9)," begins dismantling Linux's built-in support for the i486, which was first released back in 1989. As the changelog notes, even Linus is keen to cut ties with the architecture:

> In the x86 architecture we have various complicated hardware emulation facilities on x86-32 to support ancient 32-bit CPUs that very very few people are using with modern kernels. This compatibility glue is sometimes even causing problems that people spend time to resolve, which time could be spent on other things. As Linus recently remarked:
>
> "I really get the feeling that it's time to leave i486 support behind. There's zero real reason for anybody to waste one second of development effort on this kind of issue."

To achieve this, the proposed change gets rid of M486/M486SX/ELAN support by erasing CONFIG\_M486SX, CONFIG\_M486, and CONFIG\_MELAN. The changes haven't been merged into Linux 7.1 just yet, but given how Linus himself has expressed interest in removing support, there's a good chance it'll make it in.

There's a good chance that nobody is using an i486 in this day and age, but if someone *were*, there's a good chance they'd be using Linux to get the job done. If you're one of the rare few who still keep the decades-old CPU alive, your best bet will be to grab an LTS Linux distro that keeps the older version of Linux for a few more years.

![A Steam Deck on a colorful background held in one hand.](https://static0.xdaimages.com/wordpress/wp-content/uploads/2024/09/reasons-to-pick-a-gaming-handheld-over-a-pc.jpg?q=49&fit=crop&w=220&h=182&dpr=2)
Related

Linux is a completely different beast than it was a decade ago.