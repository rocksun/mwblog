# Vite’s New Rust-Based JavaScript Bundler Available in Beta
![Featued image for: Vite’s New Rust-Based JavaScript Bundler Available in Beta](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
[Rolldown, a JavaScript bundler written in Rust](https://rolldown.rs/about) created by void(0) — the company also responsible for Vite — is now available in beta. The new bundler provides Rollup-compatible APIs and plugin interface but is more similar to esbuild in scope, the Rolldown team said in introducing the bundler.
The goal is to replace esbuild and Rollup, which are currently used in Vite as dependencies, with one unified build tool for [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/). Because it’s written in Rust, it’s performing on the same level as esbuild and is 10-30 times faster than Rollup.

“Its [WASM](https://thenewstack.io/introduction-to-moonbit-a-new-language-toolchain-for-wasm/) build is also significantly faster than esbuild’s (due to Go’s sub-optimal WASM compilation),” the team added.

Although it’s designed for Vite, Rolldown can be used as a standalone, general-purpose bundler, the team wrote.

It can serve as a drop-in replacement for Rollup in most cases and can also be used as an esbuild alternative when better chunking control is needed, according to the [Rolldown introduction page](https://rolldown.rs/guide/).

JavaScript [YouTuber Theo Browne also did a deep dive on Rolldown](https://www.youtube.com/watch?v=IDe1zVWoX94) if you’d like to learn more.

## React Native vs. Flutter: Usage Is Neck-and-Neck
Despite Flutter’s dominance among a small niche of mobile developers, [React Native edges Flutter](https://thenewstack.io/googles-flutter-beefs-up-web-support-so-how-does-it-compare-to-react-native-now/) among a broader group of developers that use cross-platform mobile frameworks.
Developers whose job focuses on mobile development are twice as likely to use Flutter as React Native (41% vs 20%), according to a TNS analysis of the [latest Stack Overflow survey.](https://survey.stackoverflow.co/2024/technology) Mobile developers represent only 3% of the survey. Among all professional developers, Flutter has a slight lead (9% vs 8%).

Many web-first developers use JavaScript, but only 37% of professional, employed mobile developers regularly use JavaScript. However, among JavaScript users, React Native has a small lead over Flutter (14% vs 13%).

The [latest JetBrains survey](https://www.jetbrains.com/lp/devecosystem-2024/) found that 30% of developers deploy applications to mobile platforms, but only 54% of this group actually utilize cross-platform mobile frameworks. Among this group, 39% use React Native and 38% use Flutter.

According to the JetBrains study, React Native adoption outpaces Flutter in regions like Northern Europe and the United States, where mobile-first development is less common.

## Nue Web Framework Shifts to ‘Standards First’
Frontend/UX developer [Teri Piirainen](https://www.linkedin.com/in/tipiirai/), creator of the web framework [Nue](https://github.com/nuejs/nue), has a lot to say about JavaScript and its hold on modern web development.

“We’ve normalized the idea that simple tasks demand massive amounts of JavaScript,” wrote Piirainen in the [Nue JS documentation](https://nuejs.org/docs/). “That basic styling needs thousands of utility classes. That design changes mean updating countless components. While this approach might seem efficient initially, it produces rigid systems that resist change and grow increasingly difficult to maintain over time.”

As you might imagine, Nue attempts to correct the situation. It’s an extremely small (2.3kb minzipped) JavaScript library for building user interfaces.

While Nue has been in development for some time, this month, Piirainen announced [it would now be a “standards first” web framework](https://nuejs.org/blog/standards-first-web-framework/).

“The focus has always been to strip away artificial layers and help developers take modern HTML, CSS, and JavaScript to their absolute peak,” Piirainen wrote.

He added that the shift will allow him to focus on two problems:

- The frontend engineering problem, which he considers to be the normalization of complexity. “What began as HTML, CSS, and JavaScript has devolved into a complex build orchestration demanding hundreds of dependencies, even for a simple page,” he explained.
- The design engineering problem, which is that web design should refocus on design and off JavaScript. ”First, JavaScript engineers have hijacked the conversation,” he wrote. “When was the last time you saw engineers debating the merits of the Perfect Fifth typographic scale or the principles behind Dieter Rams’s systematic approach?”
But what does he mean when he writes that it’s now standards first?

“Browsers have evolved significantly in the past decade,” he wrote. “By working with the standards rather than against them, we create better products with less code.”

It also means making semantic HTML the foundation for everything and prioritizing content.

“Content lives in clean, accessible files — not in JavaScript,” he added.

He also placed an emphasis on design systems using modern, systematic CSS. The results are faster tooling, cleaner code and faster pages, he contended.

“The fastest page load is one that requires just a single request. No framework initialization, no cumulative layout shifts, no waiting for JavaScript,” he wrote. “When content and styling arrive together, pages simply appear.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)