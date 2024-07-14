# Introduction to MoonBit, a New Language Toolchain for Wasm
![Featued image for: Introduction to MoonBit, a New Language Toolchain for Wasm](https://cdn.thenewstack.io/media/2024/07/27dabd2f-john-ruddock-kefjvnqlr94-unsplash-1024x683.jpg)
[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) combines the efficiency inherent in low-level code programming with the ease of component transportability typically found in Linux containers. In some respects, it competes with Docker. However, intensive work within a browser heavily suggests a future in AI.
As it happens, other languages don’t necessarily compile efficiently to Wasm, which somewhat undoes the advantage of having a program that can run in the browser. This is where ** MoonBit** comes in, although it

[can also target other backends](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/), such as JavaScript. By targeting Wasm, MoonBit gets a free ride on many smaller specialist devices.
MoonBit is a Chinese-led project: this accounts for some of the aesthetics, as well as the occasional Chinese language comments in the code. If applicable, you should check your own organization’s governance systems before playing with it.

As MoonBit’s creator Hongbo Zhang [says](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/), “The reason we decided to have a fault-tolerant type system is because we want to have the IDE share the same code base with a compiler.” This allows the MoonBit language you see within [Visual Studio Code](https://try.moonbitlang.com/) to be more of a first-class citizen. This is why the type system is important — the stronger it is, the more valid work the IDE can do before the compiler takes over.

## How to Run Wasm via MoonBit
But what do we mean by “running Wasm”? This is important because your OS doesn’t treat it as a free-running application sitting in your file system quite yet.

Before we look closer at MoonBit, let’s make sure we understand how we run Wasm. In most cases, we need a JavaScript framework to load and hold it. To use WebAssembly in JavaScript, you first need to pull your module into memory before compilation/instantiation:

12345 |
WebAssembly.instantiateStreaming(fetch("simple.wasm"), importObject).then( (results) => { // Do something with the results! }, ); |
Compare with this example within the MoonBit Sudoku gallery [code](https://www.moonbitlang.com/gallery/sudoku/):
12345678910 |
WebAssembly.instantiateStreaming( fetch("target/wasm/release/build/main/main.wasm"), importObject ).then((obj) => { obj.instance.exports._start(); assign = obj.instance.exports["sudoku/main::ij_assign"] initValues = obj.instance.exports["sudoku/main::initValues"] readValues = obj.instance.exports["sudoku/main::ij_read"] solve = obj.instance.exports["sudoku/main::solveValues"] }); |
So we have a few things to get our head around here. The `WebAssemby.instantiateStreaming`
method waits for a Response object (as a promise) for the Wasm file to load. The `obj`
instance member is then accessed, and the contained exported functions are invoked. The exports clearly describe a module/method to call within the Wasm code.
OK, so this gives us a feel for what we need to do via MoonBit; prepare a Wasm file with the necessary exported functions. While we can play with the MoonBit language freely in this [online visual code site](https://try.moonbitlang.com/), in this post I look at constructing the Wasm itself.

## More About MoonBit and its CLI
Here are a few explanations:

**Moon**is the build system for the**MoonBit**language.- You can build third-party packages with
**mooncakes.io**, so it is a putative package management system. - As I’ve mentioned, there is a Visual Studio code plug-in for MoonBit.
- The term
**module**is synonymous with a project. - To create the exports we saw evidence of, we need the
**Foreign Function Interface,**which we’ll check out at the end of this post.
With that, let’s dig in.

We could start with Visual Studio code and install the MoonBit Language Extension. As usual, I’m doing this on my trusty old 2015 Macbook, and it worked just fine.

But we’ll focus on the [CLI tools](https://www.moonbitlang.com/download/) to [manage projects](https://www.moonbitlang.com/docs/build-system-tutorial). That is because I want to cement in my mind the connection between Wasm code and exposing it in the browser.

Opening Warp, I downloaded the CLI tools:

1 |
> curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash |
I then created a nice default ‘hello’ module with the `moon new`
command:

The project’s setup on disk shows the relationship between the library and the main package:

The JSON packaging manifest provides cues for the builder for each package. The mod file describes the module as a whole. The first line declares that this module is called “eastmad/hello”.

The **hello.mbt** file contains our familiar language introduction:

123 |
pub fn hello() -> String { "Hello, world!" } |
This follows in a similar form to the modern language idiom for a method or function — we saw it in [Gleam](https://thenewstack.io/introduction-to-gleam-a-new-functional-programming-language/) for example. This leaves the main.mbt code in the main package with the responsibility of posting the string to the console:
123 |
fn main { println(@lib.hello()) } |
That `@lib.hello()`
is clearly an internal call to the **lib** package that was resolved within the package description.
Running this through the CLI is simple enough:

Wonderful. But I’d like to know what that produced. There is a whole new **target** directory, so let’s take a look at that:

(You can see references to [wasm-gc](https://developer.chrome.com/blog/wasmgc#traditional_methods_of_porting_languages_to_the_wasm_runtime), which is the garbage-collected version of Wasm. All this means, essentially, is who and how responsibility for “cleaning up after itself” works out.)

So we got the promised .**wasm file —** it is 285 bytes long bit of binary, with the greeting words visible, as well as the token “_start”, referenced in the example javascript call at the beginning — as well as other supporting objects. I don’t see evidence of any “exports” like in the JavaScript framework at the top yet; all we did was print to the console internally.

## Interacting With the Hosting Runtime
To interact with the hosting runtime when embedded inside the browser, MoonBit refers to [Foreign Function Interface](https://www.moonbitlang.com/docs/ffi-and-wasm-host) (FFI). Let’s finish off our introduction by having a quick look at this.

To declare a foreign function within MoonBit, you can do this:

1 |
fn cos(d : Double) -> Double = "Math" "cos" |
The actual function itself (the body) has been replaced with the putative module name and function name. You’ll see this reconstructed below when we call it from JavaScript.
You can then describe the relationship in the modules **moon.pkg.json** file:

1234567891011121314151617 |
{ "link": { "wasm-gc": { "exports": [ "add", "fib:test" ] }, "js": { "exports": [ "add", "fib:test" ], "format": "esm" } }} |
In this example the functions `add`
and `fib`
are exported, and the function `fib`
will be exported with the name of `test`
.
Finally, for our maths example, the JavaScript calling framework would look something like this:

12345 |
WebAssembly.instantiateStreaming(fetch("xxx.wasm"), { Math: { cos: (d) => Math.cos(d), }, }); |
And this brings us more or less full circle. Most of these elements are visible in the [Sudoku](https://www.moonbitlang.com/gallery/sudoku/) example.
While MoonBit is nearly production-ready (check the [status here](https://www.moonbitlang.com/docs/syntax)), it already describes a modern language as well as a workflow to create a Wasm project. I’m expecting small LLMs will get packed efficiently into Wasm format in the near future.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)