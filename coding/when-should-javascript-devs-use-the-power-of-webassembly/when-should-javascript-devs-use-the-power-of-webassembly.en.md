JavaScript was created [thirty years ago](https://cybercultural.com/p/1995-the-birth-of-javascript/) for simple web interactions. While it still basically runs the web, applications are far more complex today than they were back then. This means there’s a lot of functionality needed in the browser that JavaScript can handle, but often at a performance cost. As someone who refreshes every few seconds while waiting for a slow app to load (yes, I know it doesn’t help, but I do it anyway), speed matters.

As a solution to this, [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) was introduced in 2017.

## Understanding Wasm and How it Works with JavaScript

Among other things, WebAssembly helps developers move computationally expensive or complex logic out of JavaScript without giving up the JavaScript ecosystem. By using WebAssembly, you can write performance-heavy code in languages like Rust, C++, or AssemblyScript that still runs efficiently in the browser or on the server. Since WebAssembly compiles closer to machine code, it makes applications faster and more efficient.

Of course, Wasm wasn’t built as a replacement for JavaScript. It can’t manipulate the DOM, handle events, or work with existing frameworks. Instead, it was designed to work *alongside* JavaScript. Think of Wasm as a way to handle the heavy lifting, while JavaScript provides an ecosystem and convenience.

In the early days of WebAssembly, building and integrating Wasm components was tricky — especially for developers with a JavaScript background. It often required complex setup and unclear debugging workflows, making it far from beginner-friendly.

> AssemblyScript lowers the barrier to entry by letting JavaScript developers write Wasm using familiar, TypeScript-like syntax.

After years of updates, WebAssembly is now more accessible to developers of all levels, which has led to increased adoption.

Today, WebAssembly tooling is mature. Modern workflows make it easier to compile Wasm modules, organize projects and load WebAssembly in both Node.js and the browser. AssemblyScript lowers the barrier to entry by letting JavaScript developers write Wasm using familiar, TypeScript-like syntax; while tools like `asinit`, `asc` and official loaders handle much of the boilerplate.

## Ideal Use Cases for WebAssembly in JS Applications

Here are some examples of applications that benefit from pairing WebAssembly with JavaScript.

### CPU-Intensive Computations

Heavy calculations — such as data processing, simulations, image manipulation, or complex math — often run acceptably at small scales in JavaScript, but can become bottlenecks as workloads grow. In these cases, using WebAssembly alongside JavaScript can significantly outperform equivalent JavaScript implementations by executing closer to native speed.

### Using Existing Non-JavaScript Code

With WebAssembly, you can bring libraries written in languages like C++, Rust, or AssemblyScript into the browser. This lets you integrate battle-tested, high-performance code without rewriting it in JavaScript, which is especially helpful when solutions already exist outside the JavaScript ecosystem.

### Performance-Critical Features

This category includes workloads that require high-speed execution with low overhead, such as real-time data transformations, image processing, or video processing.

WebAssembly is not a good fit for tasks like DOM manipulation, simple application logic, or I/O-heavy workflows. Save WebAssembly for the heavy work.

## A Step-by-Step WebAssembly Tutorial With AssemblyScript

The following tutorial shows how to bring Wasm-based math functionality written in AssemblyScript into the browser. While the example is simple, mathematically intensive computations are a great use case for WebAssembly.

Let’s build.

### Prerequisites

* Basic understanding of JavaScript
* npm
* Homebrew (macOS only)
* An IDE (VS Code is used in this tutorial)
* [Node.js](https://nodejs.org) version 22 or higher

The first step is to install `wash`. It’s a command-line tool, and while it doesn’t need to be installed system-wide, doing so can make things easier. Below is an example of installing it system-wide on macOS.

```
brew install wasmcloud/wasmcloud/wash@0.42.0
```

Open a new project in your IDE and make sure all prerequisites are installed.

```
node -v
npm -v
wash --help
```

Now, create the project folder:

```
mkdir wasm-adder
cd wasm-adder
```

### Initialize AssemblyScript

Run `npm install --save-dev assemblyscript` to install AssemblyScript locally. Then run `npx asinit .` to initialize the project with the recommended structure, including `assembly/`, `build/`, `asconfig.json`, and example files.

```
npm install --save-dev assemblyscript
npx asinit .
```

This creates the recommended AssemblyScript project structure:

```
wasm-adder/
├─ assembly/       # AssemblyScript sources
├─ build/          # Compiled WASM artifacts
├─ package.json
├─ asconfig.json
├─ tsconfig.json
├─ index.js
└─ tests/
```

### Write the AssemblyScript function

The `add` function contains the application logic that will run in WebAssembly. When compiled, this AssemblyScript code becomes a `.wasm` module.

```
export function add(a: i32, b: i32): i32 {
  return a + b;
}
```

`i32` is a numeric type provided by AssemblyScript.

### Compile to WebAssembly

The code is compiled to the `build/` folder, producing `release.wasm` and `release.wat`. The `.wasm` file is the binary executed by Node.js or the browser, while the `.wat` file is a human-readable format useful for debugging.

```
npx asc assembly/adder.ts -b build/release.wasm -t build/release.wat --optimize
```

## Conclusion

And there you have it: a working WebAssembly example. With this foundation, you can offload complex or performance-critical computations to WebAssembly while keeping JavaScript focused on orchestration and user experience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)