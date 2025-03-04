# Curl’s Daniel Stenberg on Securing 180,000 Lines of C Code
![Featued image for: Curl’s Daniel Stenberg on Securing 180,000 Lines of C Code](https://cdn.thenewstack.io/media/2025/02/c5fdc519-screenshot-from-fosdem-2025-talk-by-curl-maintainer-daniel-stenberg-laughing-1.png)
In [his talk](https://www.youtube.com/watch?v=Yr5fPxZvhOw) for this year’s annual open source conference [FOSDEM,](https://fosdem.org/2025/) Curl creator [Daniel Stenberg](https://daniel.haxx.se) promised to show his audience “Things to do in order to sleep well while having your C code in 20 billion installations.”

Stenberg believes 20 billion is actually a [ low estimate](https://thenewstack.io/youre-addicted-to-curl-you-just-didnt-know-it/) for the

[number of Curl installations](https://thenewstack.io/the-creator-of-curl-remembers-23-wildly-successful-years/)in the world. But the number certainly gives the
[open source data transfer utility](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/)he created “a little bit of a responsibility.”
“But of course, we write this in the safest possible language,” he says, drawing a laugh — because Curl is written in the[ C programming language](https://thenewstack.io/introduction-to-c-programming-language/)…

His talk was entertaining, informative, and ultimately reassuring.

But it also offered an inspiring example of what happens when a project commits to extra levels of high security. And how that commitment turns into execution — when the stakes are unusually high…

## Not a Weekend Project
Toward the end of the talk, Stenberg put up a funny slide parodying an O’Reilly book cover, “Rewriting Curl in Rust. A weekend project.” (The top of the book cover added the tagline “Telling others instead of doing it yourself.”)

“It’s a very popular book,” Stenberg says, while adding pointedly that “No one has really finished it.”

Curl consists of 180,000 lines of C code. That’s 1.14x the length of the novel *War and Peace*, Stenberg tells his audience, describing it as “actually quite a lot of code… for what it is. It transfers data.” So he says emphatically, “We’re [not going to re-write](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/) Curl in Rust. In *any* language — we’re not going to re-write it at *all*. It’s there already.” Stenberg acknowledges Rust is “possibly a great language” and says third-party dependencies can still be written in Rust, which he predicts there’ll be more of in the Curl project going forward.

But Curl’s current codebase is still written in C, and “we’re just patiently iterating and polishing over time. There’s not going to be any re-write.”

So instead, the talk offered examples of everything else they’ve been doing to keep [Curl](https://curl.se/) secure…

For starters, while they’re coding in C, Stenberg says they’ve banned “a bunch of undesired functions” that are easy to use the wrong way. Someone asked for examples at the end of the talk — and Stenberg started with *gets()* (which one commenter on Stack Overflow [calls](https://stackoverflow.com/questions/4344776/student-info-file-handling#comment4725926_4345431) “the devil’s tool for creating buffer overflows”), as well as *scanf()*, *strcopy()*, and *sprintf()*.

“It doesn’t really matter how experienced you are — some functions in the C standard are really not advisable to use in code. And we check for them with tools, we ban them so you can’t really sneak them in by mistake.”

## Testing, Testing…
There’s also a special “torture test” that takes place in a custom debugging build in which every function where a memory allocation could fail (like *malloc* or *calloc*) has a wrapper that lets them call that function — and keep calling it until it fails. “It should just fail nicely — no memory leak, no crash, and just exit with an error code,” Stenberg explained. “That’s an awesome way to test exit paths, really, and make sure that we always free up stuff and clean up stuff when we exit.”

The dev team doesn’t always test them all. He says with a laugh, “It’s not a fast process,” — so they have a system that randomly tests a smaller subset. Stenberg says they’re also using [Continuous Integration](https://thenewstack.io/ci-cd/) — which ends up running more than 400,000 tests for every pull request and commit. “Just, I think a year ago, they could take hours,” he remembers — but they’ve since optimized them, so they now run in 30 minutes. “It’s really convenient to have them finish really fast so that we know the state of the latest changes right now.”

While you may have heard the phrase “CPU second” — a second of full-power use on a server-grade CPU — 86,400 CPU seconds add up to a full CPU day. And on average, Stenberg says “We spend about 10 CPU days per day, right now, in CI only.”

To maintain security throughout the project, there’s also a wide variety of other tests, Stenberg says — even one that tests “that the code style is right, and the indenting and spelling even in the code.” There’s also a CI job to make sure they don’t have any binary blobs. (Although “There should be no way to hide any encrypted payloads in our repository anyway,” Stenberg says since most of their committers are already using digital cryptographic signatures.)

There’s unit tests, library tests, tool tests, “And of course, we have the analyzers checking code all the time” — both static and dynamic analyzers. Curl is also part of Google’s [OSS-Fuzz](https://github.com/google/oss-fuzz) project. (As Stenberg describes it, “They keep fuzzing Curl nonstop on Google hardware…”)

“We want to make sure that all those 20 billion installations run fine.”

## Fixing — and Finding — Vulnerabilities
When it comes to vulnerabilities, “We fix them as soon as we can, we alert distros as we should, and we document everything really really thoroughly,” Stenberg says, including a JSON-formatted list of affected versions of Curl. That information is also made available on Curl’s website. The Curl program is now also an official CVE-numbering authority “so that we can manage our own CVEs a little bit better.”

And they’re serious about finding vulnerabilities, Stenberg says, adding, “We have had multiple audits.”

Stenberg remembers that their first audit in 2016 “resulted in seven CVEs,” and one in 2022 resulted in two more CVEs. But he’s proud that a more narrow audit in 2024 resulted in 0 CVEs — an encouraging trend. Audits are a big and expensive undertaking. “Someone is going to spend a lot of expensive hours looking at code… It’s not something that’s easy to be done right for a small open-source project. You have to have someone who just has a deep pocket who suddenly wants this to happen.”

Yet he also points out that the cost of audits was still “much more than our entire [bug bounty program](https://curl.se/docs/bugbounty.html) for many years” — even though the bug bounty program ultimately found more CVEs.

That bug-bounty program is run in association with [HackerOne](https://www.hackerone.com/) and the [Internet Bug Bounty](https://www.hackerone.com/internet-bug-bounty) program. Stenberg says they’ve paid out more than $85,000 since they started the program nearly six years ago in April of 2019 — and 76% of the 500 reports resulted in a CVE (more than 15% — while another 19% resulted in a non-CVE-level bug fix). “Not everything else is crap,” Stenberg says, “but there’s a fair amount of that too… We always disclose all of them after the fact so that you can follow the discussion…”

Although the last bullet point on the “Bug bounty” slide just says “AI slop is increasing.”

“Actually, right now, we have about the same rate of valid reports as ‘AI slop’ reports,” Stenberg says — about 10 to 15% of submissions!

## Security All the Way Down
The project aspires to top-level security, and that commitment seems to permeate it at every level.

- All commits are carefully reviewed — by humans and by machines. And “We have a really strict code style these days,” Stenberg says, which makes the whole 180,000-line codebase look like it was written by a single author (with that consistency making it easier to read and debug).
- “We have a lot of documentation about the source code and internal APIs and everything.” Later Stenberg explains there’s even documentation-checking tooling, and not just for spelling and grammar. “For example, we try to avoid contractions in the English that we write the documentation in. So ‘isn’t’ isn’t something that’s allowed in the documentation… Stuff like that… “
- The project’s development team all use two-factor authentication for accessing their GitHub-hosted source code…
GitHub has provided them with extra testing resources, which ultimately prompted some [interesting discussion on Mastodon](https://mastodon.social/@bagder/113910838011988132) about whether other open-source projects should launch with the tightest security right from the start.

“Most open source projects I think start small and ‘easy’,” Stenberg replied, adding that “getting them all done right and properly tight from the beginning without even knowing if the project flies might not be the best priority. I think very few projects do that… [I]n the Curl project, pretty much every bolt was loose when we started…”

Later in the discussion, Curl developer [Stefan Eissing](https://eissing.org/) joked that the stakes sometimes feel very high. “We have ‘civilization will end on several planets if you screw this up’ FOSS projects. This is no way to run a civilization.”

And Stenberg seemed grateful for the help they’d received from GitHub — perhaps wishing the same level of support could reach more open-source software repositories that are grapping with their own loose bolts.

“Looking around in the world, lots of projects still have a few that could use a little help…”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)