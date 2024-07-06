# RustLang’s Semantic Versioning Still Breaks Too Many Apps
![Featued image for: RustLang’s Semantic Versioning Still Breaks Too Many Apps](https://cdn.thenewstack.io/media/2024/07/40206855-rust-semverchecksbb-1024x682.png)
Is Semantic Versioning still the best way to mark the new releases of software packages? The [Rust community](https://thenewstack.io/rust-programming-language/) may be finding some challenges around this industrywide approach.

In [a survey](https://predr.ag/blog/semver-violations-are-common-better-tooling-is-the-answer/) of 1,000 most popular Rust utilities, packaged as [Rust crates](https://crates.io/), a group of developers found that 17.2% of the packages had at least one SemVer violation — about 1 in 6 of all Rust packages surveyed.

In other words, someone running a project based on these crates in the survey would experience a breaking change once every 10 days, noted Rust developer [Predrag Gruevski](https://predr.ag/), who appeared in a recent [Changelog podcast](https://changelog.com/podcast/597) to discuss the limits of SemVer, and was also one of the authors of the above-mentioned study.

“When these breaking changes happen, they break the entire ecosystem,” Gruevski said. “Thousands of people have to spend their time figuring out why the build is red all of sudden.”

As the show’s other guest, frontend developer [Chris Krycho](https://v5.chriskrycho.com/index.html), points out, getting SemVer correct is a fundamental communication problem. The maintainers of the language must convey the update information for the end users and end-user tooling, so they can determine if the package needs to be updated in their own apps, and, if doing so, will their programs break as a result.

“As a consumer of SemVer, I don’t care about the numbers. I just want to not sign up to fix things I did not intend to break,” Gruevski said.

## SemVer Made Easy
The[ Semantic Version](https://semver.org/) specification provides a (seemingly) simple format for iterating successive releases of a software package — MAJOR.MINOR.PATCH:

**MAJOR**version when you make incompatible (API changes).**MINOR**version when you add functionality in a backward-compatible manner.**PATCH**version when you make backward-compatible bug fixes.
Additional metadata can be affixed to the end of the numbered string (such as “alpha release.”)

For Rust, the ambiguity creeps in over [what constitutes](https://doc.rust-lang.org/cargo/reference/semver.html) a major release.

Adding a new trait is usually considered worthy of a minor upgrade, though in some cases an addition can lead to a major upgrade if the[ trait](https://doc.rust-lang.org/book/ch10-02-traits.html), or shared functionality, is based on conflicts with other traits.

The docs offer a long list of other breaking or major features, including:

- Whenever a public
[item](https://doc.rust-lang.org/reference/items.html)(such as a module) is changed, moved or removed - Adding a private struct field when all current fields are public, or when there is no previous previous struct field
- Adding new enum variants, or adding new fields to an enum variant
- Tightening generic bounds
- Adding or removing function parameters
Any of these changes to an existing Rust application could cause a compilation error or unexpected behavior for the unsuspecting users.

## The Power of Automating SemVer
The power behind [Semantic Versioning](https://www.joabj.com/Writing/Tech/Dev/1509-Software-Versioning.html), at least in theory, is that the versioning should be uniform so a bundler can recognize a non-breaking change, and automatically include the upgrade in the next build and not have it break anything

“When I maintain a tool, and I have a few hundred dependencies, I don’t necessary want to look very closely at the various different version numbers and think about what they all mean,” Gruevski said. “But what I want to dois run a Cargo update inside my Rust project and know that because everyone adheres to what is abreaking change, I will still have a working project at the end of that command.”

Gruevski has created a tool, [cargo-semver-checks](https://crates.io/crates/cargo-semver-checks) that scans Rust crates and flags for SemVer violations. Think of it as a linter for checking version numbering. It can be used in build pipelines to ensure an upgrade in Rust does not break any dependencies in your code base (It can also be used within a [GitHub Workflow](https://github.com/obi1kenobi/cargo-semver-checks-action)).

Currently, SemverChecks has about 80 “lints,” or rules that identify breaking changes, which can be defined either by the test program producing unexpected behavior or failing to compile altogether.

Gruevski admits there are at at least 150 more behaviors the program should catch but doesn’t. (Users are encouraged to contribute their own lints).

In January, Gruevski posted a [ blog item](https://predr.ag/blog/four-challenges-cargo-semver-checks-has-yet-to-tackle/) listing the many remaining ambiguities within Rust. For one, there are an unbelievable number of edge cases, ones that seem obvious in hindsight, but nearly impossible to anticipate. Unexpected dependencies can crop up across multiple dependencies. And not checking type can also lead to issues.

Krycho pointed out the kind of breaking change that a linter would miss: A refactoring of a data structure so that it uses memory far more judiciously could be a breaking change, even if it does not change the corresponding API. The change in how it scales is alone enough to warrant alerting end users.

[Like YAML,](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) the SemVer spec in its entirety can be deceptively easy, especially with a language [with as many subtleties](https://predr.ag/blog/four-challenges-cargo-semver-checks-has-yet-to-tackle/) as [Rustlang](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/).
“I’ve been doing this years, and there is not a week that goes by where I don’t learn of a new horrifying way to accidently cause a breaking change in a Rust project,” Gruevski said.

There are just too many rules, and it is too easy to break one of them without noticing.

“The most innocuous-seeming changes end up be breaking for some reason that no sane person would ever think of,” Gruevski said.

## Hyrum’s Law
Multiple people working on a project can muddy the waters further, Krycho pointed out.

He has worked with SemVer for another language, [Typescript](https://thenewstack.io/TypeScript/), and has found similar issues.

“Who determines if it is a bug fix or a major break? You don’t always know,” he said. “The semantics sound good, but the definition of what makes for a breaking change gets fuzzy.”

TypeScript ([currently version 5.5](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/)) does not strictly follow Semantic Versioning, but because it is used in the [Node.js](https://thenewstack.io/qa-tracy-hinds-bringing-node-js-people/) ecosystem, it [does follow](https://www.semver-ts.org/1-background.html) the MAJOR.MINOR.PATCH format.

Typescript’s approach has been more along the lines of treating every change as a potential breaking change, even a bug fix.

Kyrcho pointed to a [Hyrum’s Law](https://www.hyrumslaw.com/), named for a Google engineer who noticed that given a sufficient number of users, every observable behavior of the system will be vital to some user. Even bug changes could lead to a breaking change.

“If my bug fix breaks my entire user base, do I call it a bug fix?” Krycho asked.

You still need a human in the loop, he said, to make the judgment call as to what change can really disrupt a user base.

## Versioning in Other Ecosystems
It should be noted that not every software package follows SemVer. Python currently is fixed at the 3.X release, and will increment going forward through minor releases regardless of breaking changes, though the community is considering a move to [year-based versioning](https://thenewstack.io/python-mulls-a-change-in-version-numbering/), so a version of Python released in 2024 would be Python 3.24.

ECMAscript and JavaScript just use the [four-digit year itself](https://thenewstack.io/ecmascript-specs-approved-and-how-google-sheets-used-wasmgc/) as the release number.

Canonical uses a calendar-based versioning (CalVer) for Ubuntu. The latest release version number, [24.04](https://ubuntu.com/download/server), indicates that it was released around April 2024.

So the problem with all these approaches, as Gruevki notes, is the admin is back to reading the release notes to find breaking changes.

Even those software package that seem like they follow SemVer have their own quirks.

[EmberJS](https://thenewstack.io/choose-your-own-adventure-emberjs-co-creator-tom-dale/) follows SemVer sort of, but only revs up to the next major version to alert users of deprecated code.
There are those software projects that bump up their next release to a major release, simply for the marketing benefit that comes with a major release ([free publicity from trade pubs](https://thenewstack.io/six-years-later-mesos-makes-version-1-0-now-real-fun-begins/)).

Maybe we need marketing versions of software as a completely different thing, Kyrcho suggested.

Even [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/), keeper of Linux, [bumped up Linux](https://www.makeuseof.com/how-are-linux-kernel-versions-formed/) to version 5, from 2.6. simply because the number of minor revisions went past what he could count on his fingers and toes.

You can enjoy the full Changelog podcast here:

[Changelog Interviews 597: MAJOR.SEMVER.PATCH](https://changelog.com/podcast/597) – Listen on [Changelog.com](https://changelog.com/)
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)