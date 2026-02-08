[Whamm](https://thenewstack.io/meet-whamm-the-webassembly-instrumentation-framework/) is designed to allow users to instrument their [WebAssembly](https://thenewstack.io/webassembly/) (or Wasm) applications with a [programming language](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/) or code, or let them program their WebAssembly applications in modules directly. With it, they can debug and monitor their applications within WebAssembly modules.

If you have [Homebrew](https://thenewstack.io/install-homebrew-on-macos-for-more-dev-tool-options/) already installed, updates will be installed automatically as Whamm is installed. This command downloads and installs Homebrew:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Download the latest release for your platform from the Releases page.

Clone the Whamm repo:

```
git clone https://github.com/ejrgilbert/whamm.git
```

[Rust](https://thenewstack.io/rust-programming-language-guide/) is required, and even if you don’t know Rust very well — I certainly don’t — once it’s installed, you can play around with Whamm. I downloaded and installed Rust on my Mac by accessing it at this trusted site with this command (which I highly recommend doing):

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

I then ran these commands to make sure that Rust is available for all terminal sessions. This is necessary because Rust is incredibly complicated to use, is extremely logical, or both:

```
grep -q ".cargo/env" ~/.zshrc 2&gt;/dev/null || echo 'source "$HOME/.cargo/env"' &gt;&gt; ~/.zshrc &amp;&amp; echo "Added to ~/.zshrc - will work in new terminals"
```

Build the source code:

```
cargo build --release
```

When I first prompted Whamm to build the source code, I received an error message:

[![](https://cdn.thenewstack.io/media/2026/01/dd8b42a5-screenshot-2026-01-13-at-8.29.19-pm.png)](https://cdn.thenewstack.io/media/2026/01/dd8b42a5-screenshot-2026-01-13-at-8.29.19-pm.png)

The fact that I had not installed the WebAssembly target was the source of the error. So, I installed the WebAssembly target as a fix:

```
cd ~/whamm &amp;&amp; rustup target add wasm32-wasip1
```

I attempted to build the source code again:

```
cargo build --release
```

And success!

[![](https://cdn.thenewstack.io/media/2026/01/f4ee857a-screenshot-2026-01-13-at-8.37.20-pm.png)](https://cdn.thenewstack.io/media/2026/01/f4ee857a-screenshot-2026-01-13-at-8.37.20-pm.png)

Add the built binary to your PATH. This binary should be located at:

```
target/release/whamm
```

Once you do that, nifty things you can do with Whamm and Wasm are listed neatly. You can use the command line interface (CLI), as indicated, as reference for all of the various commands on offer. These include — as indicated — monitoring or manipulating a program’s execution. I won’t go into what application monitoring means here, but it’s the beginning of adding more observability for Wasm applications. Using Whamm for this is usual for debugging, collecting and analyzing logs and metrics as the application runs, instead of just statically.

Once you find the source of the error, so-called “manipulating execution” allows you to fix errors by changing the “dynamic behavior,” or in other words, fixing what is wrong. You can change the application state by “manipulating an application’s dynamic behavior,” as the documentation states.

## Basic Test

You can run a basic test to make sure that the Whamm binary is on your path and working as expected by running the following command:

```
whamm --help
```

This is what you should see:

[![](https://cdn.thenewstack.io/media/2026/01/d6b227ef-screenshot-2026-01-13-at-9.08.47-pm-1024x157.png)](https://cdn.thenewstack.io/media/2026/01/d6b227ef-screenshot-2026-01-13-at-9.08.47-pm-1024x157.png)

For reasons I don’t yet know, my initial test of Whamm functionality did not work, as shown above. But then I went through all the commands above, including reinstalling the Rust target and rebuilding or reinstalling the WebAssembly target, and reinstalling Cargo for Rust to make sure it was available in all terminals. So it was likely a Rust problem, though I’m not sure. In any case, I went through most of the commands above and eventually succeeded.

Now you’re ready to begin your Whamm journey for instrumenting, rebuilding, correcting, monitoring and debugging code. Hats off to the creator — and now, I assume, main maintainer — [Elizabeth Gilbert](https://www.linkedin.com/in/elizabeth-gilbert-2b01aa338/), a doctoral candidate at Carnegie Mellon University, for this great project.

Although I would argue that this looks simple and is relatively simple to use, it’s an amazing build and represents a lot of hard work and engineering dedication. Definitely another win for the WebAssembly community, as well as for observability, debugging and the ability to update applications dynamically with Wasm.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)