# Rust Gets Its Missing Piece: Official Spec Finally Arrives
![Featued image for: Rust Gets Its Missing Piece: Official Spec Finally Arrives](https://cdn.thenewstack.io/media/2025/03/7da8b55b-tanja-tepavac-cwmhxnmqvq0-unsplash-1-1024x690.jpg)
The [Rust Foundation](https://rustfoundation.org/) this week announced that Ferrous Systems is donating its [Ferrocene Language Specification (FLS)](https://spec.ferrocene.dev/) to the [Rust Project](https://thenewstack.io/rust-programming-language-guide/).

According to the foundation, this donation addresses a critical gap in Rust’s documentation ecosystem — the lack of an official language specification.

## A Major Step
“This is a major step… A specification allows for lots of additional tools to be written that can rely on predictable behavior from the [language compiler](https://thenewstack.io/programming-languages/),” [Tim McNamara](https://www.linkedin.com/in/timmcnamaranz/?originalSubdomain=nz), founder of Accelerant.dev and author of the “[Rust In Action](https://www.manning.com/books/rust-in-action)” book on Rust programming, told The New Stack.

While the [Rust Project](https://rust-lang.org/) has amassed lots of documentation, [courses, and tutorials](https://doc.rust-lang.org/rust-by-example/), including the official [Rust book](https://doc.rust-lang.org/book/), [Rust Reference,](https://doc.rust-lang.org/stable/reference/) and more in its online library, a key missing piece was an official [language specification](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/).

“Not having a [Rust specification](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/) is a problem that hasn’t been a big problem yet,” [Mitch Ashley](https://www.linkedin.com/in/mitchellashley/), an analyst at The Futurum Group, told The New Stack. “Rust not having a formal spec means there could be potential variances in behaviors, outcomes, and portability between compiler implementations. This hasn’t been a huge issue as ‘[rustc](https://doc.rust-lang.org/rustc/)‘ is the major compiler used in the community. If more implementations come along, or if software created in Rust has to undergo a formal verification process, that’s tough to do when there isn’t a spec.”

## It’s About Time
Initially published in 2015 ([Rust 1.0](https://thenewstack.io/the-rust-c-bridge-a-new-path-forward/)), Rust is nearing its 10th anniversary and it’s about time for a specification.

According to the Rust Foundation, in December 2022, an [RFC](https://rust-lang.github.io/rfcs/3355-rust-spec.html) was submitted to encourage the Rust Project to begin working on a specification. That RFC was approved in July 2023, and work began. Initially, the Rust Project specification team ([t-spec](https://www.rust-lang.org/governance/teams/lang#team-spec)) was interested in creating the document from scratch using the Rust Reference as a guiding marker. However, the team knew there was already an external Rust specification that was being used successfully for compiler qualification purposes — the FLS, the foundation said.

## What Is FLS?
The FLS is a description of the Rust programming language, developed by [Ferrous Systems](https://ferrous-systems.com/) in July 2022 as part of [Ferrocene](https://spec.ferrocene.dev/), a Rust compiler and toolchain designed for safety-critical and regulated industries.

“The FLS provides a structured and detailed reference for Rust’s syntax, semantics, and behavior, serving as a foundation for verification, compliance, and standardization efforts,” the foundation said in a statement.

And since Rust did not have an official language specification back then, nor a plan to write one, the FLS represented a major step toward describing Rust in a way that aligns with industry requirements, particularly in high-assurance domains.

The specification represents “another check box filled for Rust, which will have the cumulative effects of building confidence in the language,” McNamara said. “It’s also an interesting development because the commercial model is different than traditional approaches to creating certified compilers. The company behind the spec has donated it and made their commercial compiler open source.”

## Avoiding Confusion
The Rust Foundation noted that the t-spec team wanted to avoid potential confusion from having two highly visible Rust specifications in the industry and decided to try to integrate the FLS with the Rust Reference to create the official Rust Project specification. They approached Ferrous Systems, which agreed to contribute its FLS to the Rust Project and allow the Rust Project to take over its development and management.

This will also enable the Rust Project to oversee its ongoing evolution, providing confidence to companies and developers already relying on the FLS, and marking a major milestone for the Rust ecosystem.

[Joel Marcey](https://www.linkedin.com/in/joelmarcey/), director of technology at the Rust Foundation and member of the t-spec team, said Ferrous Systems has already done a massive amount of legwork on the effort.
“Having the FLS integrated officially into the Rust Project will allow the t-spec team to supercharge our progress in the delivery of an official Rust specification that can be utilized by developers, safety-critical tool vendors, and others that look to a language specification for their work,” he said in a statement.

There will be a transition period as the FLS is integrated into the Rust Project. The first phase of work will involve incorporating FLS into the project’s tooling and processes in alignment with existing [Rust Project goals](https://rust-lang.github.io/rust-project-goals/2025h1/spec-fls-publish.html). After that integration, Ferrous Systems will discontinue its own specification.

Moving forward, both the FLS and the Rust Reference will form the official Rust Specification.

## Ferrous Systems and Ferrocene
“We originally created the Ferrocene Language Specification to provide a structured and reliable description of Rust for the certification of the Ferrocene compiler,” said [Felix Gilcher](https://www.linkedin.com/in/felix-gilcher-906463283/?originalSubdomain=de), co-founder of Ferrous Systems, in a statement.

Ferrous Systems is a Berlin-based consultancy specializing in Rust software development and training.

“As an open source-first company, contributing the FLS to the Rust Project is a logical step toward fostering the development of a unified, community-driven specification that benefits all Rust users,” Gilcher said. “We are glad to support this effort and look forward to the long-term impact this will have on Rust’s adoption in regulated and high-assurance domains.”

Ferrocene is an open source Rust compiler toolchain for safety- and mission-critical applications, such as automotive, industrial, and medical development. In January, Ferrocene achieved IEC 62304 Class C qualification for medical device software. In fact, Ferrocene is the first open source-qualified Rust compiler toolchain for safety- and mission-critical applications. It is qualified to automotive (ISO 26262, ASIL-D), industrial development (IEC 61508, SIL4), and medical (IEC 62304, Class C) standards, with more to come, said [Florian Gilcher](https://www.linkedin.com/in/floriangilcher/?locale=en_US), managing director and co-founder of Ferrous Systems.

Having Ferrocene qualify for these standards “demonstrates our commitment to advancing safety-critical software development through tools that enhance both security and performance,” he said in a statement.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)