# Rust Meets Dart With Release of rust_core 1.0.0
![Featued image for: Rust Meets Dart With Release of rust_core 1.0.0](https://cdn.thenewstack.io/media/2024/07/81d81aea-getty-images-i34igy4qrje-unsplash-1024x683.jpg)
[rust_core](https://github.com/mcmah309/rust_core) version 1.0.0 has been released.
According to the [r/dartlang subreddit](https://www.reddit.com/r/dartlang/comments/1dtzhyy/rust_core_v100_released/), rust_core is an implementation of [Rust](https://www.rust-lang.org/)‘s core library in [Dart](https://dart.dev/).

By making adjustments to [Rust’s features](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/) to align with Dart’s principles, the goal of the implementation is to create a seamless and natural integration between the two languages. This enables developers to use advanced tools that were once exclusive to [Rust developers](https://thenewstack.io/aws-gifts-java-rust-developers-with-useful-tools/), allowing for a smooth transition between the languages.

The [project goals](https://mcmah309.github.io/rust_core/) state that “rust_core strives to bring reliability and performance in every feature. Every feature is robustly tested. Over 500 meaningful test suites and counting.”

Moreover “For Rust developers involved in programming with Dart, or Dart developers interested in idiomatic and [safe programming](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/), we have developed ‘rust_core,’ a package designed to implement Rust’s core library in Dart,” wrote [Henry McMahon](https://github.com/mcmah309) in a [blog post](https://mcmah309.github.io/#/blog) last November.

The company behind the rust_core project is called [Voyver](https://voyver.com/), a startup in the AI and educational software space. McMahon is the primary maintainer on the team for rust_core.

“We primarily use Dart and Rust in our stack,” he told The New Stack. “A common API was identified as a missing piece to the primarily Rust developer team and codebase. rust_core solved that for us.”

## Rust Core Book
To support the 1.0.0 release, the project also released the [Rust Core Book](https://mcmah309.github.io/rust_core/).

The Rust Core Book features an FAQ, which includes as the first question: [Why Use Rust Core Even If I Don’t Know Rust?](https://mcmah309.github.io/rust_core/introduction/FAQ.html#why-use-rust-core-even-if-i-dont-know-rust)

In response, the FAQ reads: “From a language perspective we believe Dart is sadly lacking in a few areas, of which this package solves:

- Dart utilizes unchecked try/catch exceptions. Handling errors as values is preferred for maintainability, thus the
`Result`
type. - Dart has nullable types but you cannot do null or non-null-specific operations without a bunch of
`if`
statements.`Option<T>`
fixes this with no runtime cost and you can easily switch back and forth to nullable types since it is just a zero cost extension type of`T?`
. - Dart is missing the functionality of Rust’s
`?`
operator, so we implemented it in Dart. - Dart is missing a built-in
`Cell`
type or equivalent (and`OnceCell`
/`LazyCell`
). - Dart’s
`List`
type is an array/vector union (it’s growable or non-growable). This is not viewable at the type layer, which may lead to runtime exceptions and encourages using growable`List`
s everywhere even when you do not need to, which is less performant. So we added`Arr`
(array). - Dart has no concept of a slice type, so allocating sub-lists is the only method, which is not that efficient. So we added
`Slice<T>`
. - Dart’s between isolate communication is by ports (
`ReceivePort`
/`SendPort`
), which is untyped and horrible, we standardized this with introducing`channel`
for typed bi-directional isolate communication. - Dart’s iteration methods are lacking for
`Iterable`
and`Iterator`
(there are none! just`moveNext()`
and`current`
), while Rust has an abundance of useful methods. So we introduced Rust’s`Iterator`
.”
Meanwhile, [Rust is being adopted more broadly](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/) in use cases where memory-safe programming is recommended.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)