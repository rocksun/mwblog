# Vendoring: Why You Still Have Overlooked Security Holes
![Featued image for: Vendoring: Why You Still Have Overlooked Security Holes](https://cdn.thenewstack.io/media/2024/03/869fcc10-glass-3983411_1280-1024x640.jpg)
It was the
[CVE-2023-4863](https://nvd.nist.gov/vuln/detail/CVE-2023-4863) vulnerability that revealed how truly bad the problem of vendoring had become in the Nix repository, recalled Nix Packages maintainer [Delroth](https://github.com/delroth) (Pierre Bourdon) in his February 5 FOSDEM talk, “ [Remediating 1000s of untracked vulnerabilities in nixpkgs](https://video.fosdem.org/2024/h1302/),” recently posted online.
A heap buffer overflow in the libwebp image decoder (v1.3.2) was found in the Google Chromium browser. Chromium sent out word for users to update immediately because there were exploits in the wild using this vuln.
And so the
[Nix folks](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/) swiftly patched their version of Chromium, and since the vulnerability was actually with [libwebp](https://chromium.googlesource.com/webm/libwebp), the Nix version of that library was patched as well.
But then, the maintainers started wondering, where else was that decoder being used? Nix is a tightly run
[package management system](https://search.nixos.org/packages) for the Nix-OS, a Linux distribution, allowing users to download over 80,000 software packages, utilities.
Certainly, additional packages, such as other web browsers, must have also bundled libwebp in their own open source applications, an inclusion known as “vendoring.”
Turns out there were dozens, or maybe even more. Without any tools to sort through the packages, it took the team about a month to track down only about half of what they estimated was out there. At least 10 contributors spent “hundreds of hours” updating packages.
Initially, they tried to replace every vulnerable instance of that library they found, but soon gave up, recognizing the enormity of the task. And while most the high-risk cases were updated, those packages less likely to be impacted have been delayed, maybe indefinitely.
The lesson is clear: when a vulnerability strikes, package and repository managers can no longer assume the problem is solved once they patch their canonical version of the problematic software.
And if the Nix founders figured this out about their own libraries, it’s pretty likely happening everywhere.
## What Causes Vendoring?
Lazy programmers? Instead of declaring a dependency, and drawing on a system resource, they will just cut and paste the library right into their app’s own source directory. Sneaky-sneaky downstream a copy of an open source library in your own application library.
To be fair, there are some practical reasons for doing this: The chief benefit is that you never have to worry about an external dependency breaking your applications, because it goes missing or is updated in a way that somehow breaks your own app.
Keeping it in-house, after all, will keep things working forever and ever.
Until a vulnerability is found, that is. While system resources are readily patched when they are found unsecured, the copies of these resources buried in the directory of some app’s code will more than likely not be updated and thus remain open to exploitation.
How many of these clever programmers realized that by adding an external library to their own stack they have also taken on the responsibility of
*maintaining* that resource, just as much as they are responsible for their own code?
## The Great Divide
In the Nix community, at least, the situation with vendoring is “not great” Delroth admitted. And it’s a problem that can’t easily be fixed.
In wondering how bad the problem of duplicate libraries had spread, Delroth created a few tools to get a handle on the problem: the self-describing
[grep-nixos-cache](https://github.com/delroth/grep-nixos-cache) and the more [ language-specific vendored vulnerability scanner](https://github.com/delroth/nixpkgs-vendored-vulns-scan).
Turns out there were 116 other copies of libwebp in various nixpkgs across the Nix repository. And it was far from the only image decoder being bundled: He found 237 copies of libpng and 253 copies of libjpeg scattered about. And the all-purpose zlib compression library was found in 761 different places.
And who knows how many of these, if any, are being updated. A few versions of libpng go back to 2004!
![](https://cdn.thenewstack.io/media/2024/03/4fbf31b4-fosdem-vendoring-01-1024x546.png)
Go on! nix build it and get a binary from 2004! Does it still have vulnerabilities? You bet!
The
[Rust programming language](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/) has its own peculiar take on this problem, he noted, through its use of [LockFiles](https://docs.rs/fslock/latest/fslock/struct.LockFile.html). With LockFiles, an application will require a specific version of a resource, which is identified by a numeric hash. So while the program calls an external system resource, it requires a specific version of that may never get patched.
Delroth highlighted Rust
*crates* packages [with LockFile dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html). Of the 1,844 Rust packages identified, 1,149 (62%) had locked-in dependencies, meaning in Rust-speak, that they couldn’t be changed.
“Upstreams don’t understand this, or don’t care,” Delroth said. And 40% of those packages (744) have high or critical security holes.
Of course, not all of these vulnerabilities are exploitable, depending on how they may be used, but some may be.
## What Can Be Done about Vendoring?
Delroth admits the Nix community has not set down any sort of compliance or even guidelines to discourage programming from vendoring.
It is just considered good practice to use the external system libraries, but there is no law saying you have to. It’s
[open source](https://thenewstack.io/open-source/) after all.
Nor is there a even stated preference for building from source. Users can go to
[AppImages](https://appimage.org/) and download an already-compiled binary instead. “People are very creative about how to get binaries,” Delroth said, adding that [Debian](https://www.debian.org/) is the gold standard for keeping binaries fresh.
(And this is assuming someone upstream is still maintaining the packages. Many aren’t, Delroth admitted.)
For Nix, the best approach may be user education, says Delroth. and perhaps a new tag, something like
**knownVulnerable**, that can be used to flag or even programmatically steer users away from out-of-date packages,
## What Does Vendoring Mean for the Rest of Open Source?
Keep in mind, that the Nix folks run a pretty tight packaging system, comparatively speaking. So if vendoring is a problem here, you can bet it is a problem with other open source repositories. What about the other Linux or Docker distribution points, or the
[JavaScript jungle of frameworks](https://thenewstack.io/jamstack-panel-multiple-javascript-frameworks-are-a-good-thing/), or even the [Wild West frontier of C/C++ libraries](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/)?
In a 2022 survey by
[ The Linux Foundation,](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline-mention) only 18% of open source contributors reported that they are confident that the indirect (transitive) dependencies their organization depends on are not malicious or compromised (A transitive dependency is a dependency for a package that you use as a dependency).
Even when there is an existing policy in place for open source security, that figure only goes up to 27%.
“I think that people are concerned that if they report their usage of a dependency, then it will slow down their development and make them look bad,” TNS analyst
[Lawrence Hecht](https://thenewstack.io/author/lawrence-hecht/) noted in a Slack conversation.
They have a bureaucracy to deal with as well. A
[Tidelift survey](https://blog.tidelift.com/finding-4-getting-approval-to-use-new-open-source-components-in-large-organizations-is-often-slow-and-tedious) found that 56% of open source developers at enterprises with more than 10,000 employees say it takes more than a week to get approval to use an open source component.
## Can SBOMs Solve Vendoring?
Is this a problem that could be contained at the user level, through a
[software bills of material](https://thenewstack.io/sboms-sboms-everywhere/) ( [SBOMs)](https://thenewstack.io/a-good-sbom-is-hard-to-find/) that inventory all the one source components that could be used?
“It is highly dependent on how the code or software is vendored, and if the SBOM tool used to generate the SBOM can deal with that,” noted
[Michael Lieberman](https://www.linkedin.com/in/michael-lieberman-65786ba/), co-founder of the security platform company [Kusari](https://www.kusari.dev/about) and one of the creators of the [GUAC SBOM visualization tool](https://thenewstack.io/kubecon-24-guac-reveals-where-the-vulnerabilities-hide/), in an e-mail.
The Go programming language, for instance, “handles vendoring in a fairly straightforward way,” he said. “As long as you don’t modify the vendored code, SBOM tools should be able to handle picking it up.”
Not every case is as straightforward as that, however. “People will sometimes manually vendor code by downloading the source directly into another project. As soon as you modify even a single line of a vendored project, you have now forked and modified that software to turn it into something else.”
In these cases, you run the risk of an SBOM tool being unable to identify the code. You broke it, you bought it.
The term “vendoring” seems to have been borrowed from the world of commercial software, where a commercial vendor would take control of a library for its own purposes. In the open source world, “every open source distribution point” is a vendor, noted
[Tim Mackey](https://www.linkedin.com/in/mackeytim/), the head of software supply chain risk strategy at [Synopsys Software Integrity Group](https://www.synopsys.com/software-integrity.html), in an e-mail.
Take the almost universally-used
[OpenSSL](https://thenewstack.io/update-now-openssl-1-1-1s-shelf-life-has-ended/) library, for instance. The official source is a [ GitHub repository](https://github.com/openssl/openssl), but most users get it from a Linux distribution such as [Red Hat ](https://www.openshift.com/try?utm_content=inline-mention)or Debian. The code may be exactly the same in both distros, but they were compiled for different targets (hence the name “vendoring.”). Realistically, there are probably thousands of different forks, or intermediate source code copies, of OpenSSL in the wild.
“This entire ecosystem makes patch management quite hard,” Mackey wrote. “A patch designed for one branch of OpenSSL might not work the same on a different branch because of changes I made to an independent fork of the code.”
A good SBOM will look at the package’s pUrl (
[persistent uniform resource locator](https://datatracker.ietf.org/doc/html/rfc3986#section-1.2.3)), which identifies the province of a package.
“If that pUrl points to the correct GitHub repository for the version of OpenSSL used by the application, then we’re able to identify who is responsible for any patch. Similarly, if the version of OpenSSL originates from a distribution like Debian, then Debian is the responsible party for any patches,” Mackey noted.
Vendoring could also make things worse for SBOMs, observers note.
An SBOM does not know anything about the code that was shipped in the resulting binary, however. To address this issue,
[VEX](https://www.vexforum.com/t/design-build-workflows/33854) can be used to map the workflow of how an application was assembled.
“The SBOM should document the component and its version, but it’s up to the component vendor to determine if there is a vulnerability in their code and if it’s exploitable or mitigated without a patch,” Mackey wrote. “This is why VEX workflows are an important part of solving the vendoring problem.”
Others are not sure sure vendoring is that big of an issue.
“Vendoring could confuse many SBOM generation tools, leading to incomplete SBOMs. But it’s also possible that clever engineers could simply teach those tools how to recognize vendoring,” wrote
[John Speed Meyers](https://www.linkedin.com/in/john-speed-meyers-66b6a740/), principal research scientist at [Chainguard](https://www.chainguard.dev/?utm_content=inline-mention), in an e-mail.
Meyers notes that there are many other, and potentially more significant, threats to SBOMs, such as “messy, low quality vulnerability data or vulnerabilities that simply don’t actually affect the software in question.”
“Too often, software is like the neighborhood cat: it has no interest in being tracked and does what it wants,” Meyers concluded. “For those that want to know what’s inside their software, it can be hard, really hard.”
Delroth’s entire presentation can be viewed here:
*TNS Analyst Lawrence Hecht contributed to this post. * *Editor’s note, March 8, 2024: This post has been updated with further industry commentary.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)