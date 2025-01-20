# The Rise of Rust and WebAssembly in Web Development
![Featued image for: The Rise of Rust and WebAssembly in Web Development](https://cdn.thenewstack.io/media/2025/01/1f6026cd-getty-images-hqcjql0xgys-unsplashb-1024x576.jpg)
With the emergence of viable WebAssembly-powered [web frameworks for Rust developers](https://thenewstack.io/want-a-web-framework-for-rust-not-javascript-try-leptos/), it’s worth looking at how often Rust is used for web development currently, what tools these developers are using, and suitable use cases for Rust and Wasm going forward.

In the 2024 [JetBrains State of Developer Ecosystem Report](https://www.jetbrains.com/lp/devecosystem-2024/), 35% of Rust developers stated they already do web development work using Rust. That’s second equal with systems programming (also 35%) and behind only CLI tools (44%) — both projects more commonly thought of as being suitable for Rust, since they’re also suitable for C ++ developers (the programming language most under threat from Rust).

Elsewhere in the JetBrains report, 19% of web developers say they deploy to WebAssembly, as compared to 77% to [Linux](https://thenewstack.io/introduction-to-linux-operating-system), 43% to Windows, and 36% to MacOS. So, while Wasm for web development work is fairly well used, there’s still plenty of scope for it to grow. It’s also worth mentioning that Rust has some of the best toolchains for compiling to Wasm, such as:

- Wasm-bindgen: Bridges Rust and JavaScript.
- Wasm-pack: Simplifies packaging Rust for npm.
- Cargo-generate:
[Described as](https://crates.io/crates/cargo-generate)“a developer tool to help you get up and running quickly with a new Rust project by leveraging a pre-existing git repository as a template.”
## Rust IDEs
In the [latest Stack Overflow Survey](https://survey.stackoverflow.co/2024/technology#most-popular-technologies-new-collab-tools-prof), the Integrated Development Environment (IDE) most likely to have been used in the last 12 months by all professional developers was Visual Studio Code, with 74% of respondents having used it. That percentage stays about the same (75%) when looking at professional developers **who used Rust** in the last 12 months. So VS Code is a clear top IDE for Rust devs.

That said, there is an IDE that seems especially popular with Rust developers — because it *isn’t* used as much by other devs. 36% of professional Rust developers said they use [Neovim](https://neovim.io/), compared to just 13% of professional developers who don’t use Rust. That means Neovim is the second most popular IDE for Rust developers, behind only VS Code.

It’s interesting to note that one of the sponsors of Neovim is Warp, a Rust-based terminal that The New Stack’s David Eastman [described as](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) “the kind of IDE on your command line that you often assumed you would have, but you’ve never really had.”

Rust developers have plenty of other choices when it comes to IDEs. JetBrains offers a [dedicated Rust IDE called RustRover](https://thenewstack.io/the-rust-community-matures-with-jetbrains-rustrover-ide/), as well as Rust plugins for IntelliJ IDEA and CLion. Other popular IDEs have support for Rust too; for example Emacs and [the relatively new Zed](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/).

RustRover was only released in September 2023 and JetBrains sees a rosy future for Rust developers. Last February, JetBrains developer advocate [Vitaly Bragilevsky noted](https://mainmatter.com/blog/2024/02/29/launching-rustrover/) that Rust isn’t just being used as a replacement for “memory unsafe” languages like C++ and C.

...there are many folks coming to Rust from other

[programming languages].
- Vitaly Bragilevsky, JetBrains developer advocate
“What we actually see is that there are many folks coming to Rust from other programming languages,” he said, “and they also bring a whole new universe of ideas to implement something in Rust.” Ideas such as for web applications.

In [an earlier interview with The New Stack](https://thenewstack.io/dedicated-ide-for-rust-released-by-jetbrains/), Bragilevsky said that many developers come to Rust from the JavaScript and Python communities. “Those folks may be a bit unhappy about their previous programming languages,” he said. “Maybe they don’t have enough performance, and they can get that performance with Rust. Sometimes they don’t have enough safety. And Rust provides that for sure.”

As for what Rust developers want in their IDEs, according to the JetBrains developer survey, 12% said they want more web framework support. So that’s an opportunity for either existing Rust IDEs or for new dev tool products to tackle.

## What Types of Apps Are Best for Rust and Wasm?
Last November, software engineer [Trevor I. Lasn wrote](https://www.trevorlasn.com/blog/webassembly-when-and-when-not-to-use-it) that “WebAssembly shines in bringing proven C/C++ or Rust libraries to the web.” He used PDF generation as an example. “Instead of reinventing complex font rendering and layout algorithms in JavaScript, we can use battle-tested C++ libraries,” he explained.

Rust is increasingly seen as a language for complex data processing.

The same principle applies to Rust libraries — while these might be less “battle-tested” than C++ libraries, Rust is increasingly seen as a language for complex data processing. And because Rust compiles efficiently to WebAssembly, that means high-performance data processing can be done directly in web browsers or edge environments.

Other use cases for Rust in web development include real-time data visualization, image and video processing, and game engines.

That all said, Rust won’t be replacing JavaScript anytime soon — business logic in a web app is still best handled with JS and there are limited DOM manipulation capabilities in Wasm. Also, Wasm can quickly over-complicate matters if you’re not careful. As Lasn observes, “If you’re not doing heavy computation or using existing libraries from other languages, WebAssembly might just add unnecessary complexity.”

Regardless, web development is increasingly a use case for Rust developers. So we can expect the dev tool ecosystem around Rust to evolve accordingly.

**Note: **Research data and graphs supplied by [Lawrence E Hecht](https://thenewstack.io/author/lawrence-hecht/).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)