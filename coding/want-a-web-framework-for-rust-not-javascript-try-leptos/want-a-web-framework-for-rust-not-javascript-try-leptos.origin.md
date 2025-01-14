# Want a Web Framework for Rust, Not JavaScript? Try Leptos
![Featued image for: Want a Web Framework for Rust, Not JavaScript? Try Leptos](https://cdn.thenewstack.io/media/2025/01/1d76744b-getty-images-ybl2fiz32qo-unsplashb-1024x576.jpg)
[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) is starting to be used more in web development. In particular, [Rust frameworks](https://thenewstack.io/what-rust-brings-to-frontend-and-web-development/) like Leptos and Sycamore are using Wasm to compile Rust into fast, interactive web apps.
[Leptos](https://leptos.dev/) describes itself as a “cutting-edge Rust framework for the modern web.” The project claims to have a web performance second only to vanilla [JavaScript](https://thenewstack.io/javascript/) — it says it performs better than Vue, Svelte, and React (three times higher than React, according to the quoted benchmark; see below).
In [its documentation](https://book.leptos.dev/), Leptos says that it is “most similar to frameworks like Solid (JavaScript) and Sycamore (Rust).” This is mainly due to its fine-grained reactive system for updates and state management. “This means that only the parts of the UI that changes are re-rendered, leading to a more efficient and performant application (No Virtual DOM!),” [Leptos states](https://github.com/leptos-rs). It’s also component-based and supports both client-side rendering (CSR) and server-side rendering (SSR).

In [a January 2024 YouTube video](https://www.youtube.com/watch?v=xOVx4bM4t9U), Leptos creator [Greg Johnston](https://github.com/gbj) explained the genesis of the project. He was inspired by something Ruby on Rails creator David Heinemeier Hansson (DHH) had once said, to the effect of: the beauty of the web is that you can have anything you want running on a server, as long as it serves HTML to the end user. Johnston said he had “built plenty of JavaScript applications” before creating Leptos, but it was causing him problems. “When I learned Rust,” he continued, “I just felt like […] the language gave me so many ways to avoid those problems that I had caused myself [with JS], and I really wanted to be able to build web apps, which is what I wanted to do with it [Rust].”

He added that it was the emergence of WebAssembly that prompted him to create a Rust web framework. Thanks to Wasm, his goal with Leptos is “to give an experience that’s roughly parallel to the JavaScript frameworks but in Rust.”

## Getting Started With Leptos
There are two paths to starting with Leptos. If you just want a simple, CSR site, you can use [Trunk](https://trunkrs.dev/), an open source Wasm web application bundler for Rust. But if you want a more complex, full-stack SSR site, then Leptos enables this through its build tool [Cargo](https://github.com/leptos-rs/cargo-leptos).

“SSR is a great option for building CRUD-style websites and custom web apps if you want Rust powering both your frontend and backend,” says the project.

“…if you’re willing to contribute a few missing pieces along the way, the framework is most definitely usable.”

– Greg Johnston, Leptos creator
Leptos is currently at version 0.7.3 and, by its own admission, isn’t completely production-ready. But, the maintainers add, “If you’re willing to contribute a few missing pieces along the way, the framework is most definitely usable, especially given the ecosystem of libraries that have sprung up around it.”

So, while the framework is functional, be warned that “production-ready” depends on your willingness to navigate its current limitations.

## Performance and Correctness
The project runs a monthly virtual meetup on YouTube, and [at the end of December](https://www.youtube.com/watch?v=6-luPDoxAHo), Greg Johnston joined host Luke Skinner for an AMA. At one point, Skinner made an observation about “the kinds of people who want to develop in Rust.” In a word, it comes down to a passion for performance.

“For me, it’s like a principle of the matter — like yeah, I want to squeeze performance out, yes I want this to be perfect… or as perfect as I can get it,” said Skinner.

Johnston agreed, adding that the Leptos community is also obsessed with “correctness” — which he clarified means “doing the thing right, rather than in the easiest way.” He gave an interesting example comparing Rust to Go, explaining how both languages would deal with a Windows file name that contains invalid Unicode characters.

“Go just removes them,” he said, regarding the faulty characters, “and Rust will return a result. And it’s, like, sometimes you […] want to be presented with the warts and the complexity, and then asked: how do you want to deal with this?”

## Leptos Stack and Its Future
Later in the chat, Johnston was asked: “if Leptos didn’t exist, what would you be using for personal projects to build a reactive web app?”

In reply, Johnston mentioned Angular, React, Solid, Svelte 5 and Vue (all JavaScript frameworks). He said that Solid is probably the one he’d opt for. He added that he has misgivings about React.

“I don’t love React,” he said. “There are a lot of really nice functional programming languages for the frontend, like [ReScript](https://rescript-lang.org/) […] or [ReasonML](https://reasonml.github.io/) before that, which is like an alternate syntax for [OCaml](https://ocaml.org/). But they all just use React for the backend, and I don’t love [the] React model.”

Skinner provided a nice segue from that, asking Johnston what his preferred stack will be for 2025, other than Leptos and Rust? He said if he was starting a new project, he’d use [axum](https://docs.rs/axum/latest/axum/) — a web application framework for Rust — and “some kind of islands client-side routing.”

“I think we are on a path towards something that I would be happy to call a 1.0 — this feels like it’s the right paradigm.”

– Johnston
Finally, a viewer asked whether Leptos 0.7 is “in its somewhat final form” or whether there will be future major changes.

“I think it’s the final form, I don’t see major changes being made in future releases,” Johnston replied. A little later in his answer, he added, “I think we are on a path towards something that I would be happy to call a 1.0 — this feels like it’s the right paradigm.”

## Conclusion
Neither Leptos nor its competing Rust-based web framework, Sycamore (v0.9.1), have reached version 1.0 yet — so using Rust and Wasm as the basis for building web apps is clearly not fully mature. But if performance and “correctness” are obsessions of yours, then you might be interested in giving one or both of these frameworks a go.

The Wasm aspect is particularly intriguing. As WebAssembly continues to gain traction in web development, frameworks like Leptos offer a glimpse into a possible future of high-performance, Rust-powered web applications. While still evolving, Leptos demonstrates that it’s possible to build reactive web apps without relying on JavaScript-heavy ecosystems.

After all, one of Wasm’s promises is the ability to turn virtually any programming language into a web language.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)