# Spin + StarlingMonkey Equals JavaScript for WebAssembly
![Featued image for: Spin + StarlingMonkey Equals JavaScript for WebAssembly](https://cdn.thenewstack.io/media/2024/09/8d5aab92-christophe-hautier-902vnyeows4-unsplash-1024x683.jpg)
VIENNA — It took a while, but JavaScript deployment with [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) has seen a nice development, highlighted here with how [Fermyon](https://thenewstack.io/fermyon-says-webassembly-on-kubernetes-is-now-doable/)’s [Spin](https://www.fermyon.com/spin) offers a more direct route for deploying [JavaScript](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/) in a [Wasm](https://thenewstack.io/what-makes-wasm-different/) module. With the Spin JavaScript SDK, this approach addresses previous limitations and is considered more elegant.

Additionally, the [Bytecode Alliance](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) has contributed to a new JavaScript runtime called [StarlingMonkey](https://github.com/bytecodealliance/StarlingMonkey), which enhances Fetch API support and compatibility with Node.js APIs. A new JavaScript SDK built on Starling Monkey is introduced, aiming to expand the capabilities of JavaScript for backend services, aligning with the goals of the Bytecode Alliance.

A key feature is how Spin development is helpful for providing a more direct way to deploy JavaScript code with WebAssembly. This method of deployment is more elegant than before and solves a lot of problems and limitations that came with JavaScript. This approach with the Spin JavaScript SDK offers a direct route for JavaScript implemented in a Wasm module for deployment.

“The main thing is that we did two things: First, we contributed to a new JavaScript runtime called StarlingMonkey, which is now part of the Bytecode Alliance. Second, we implemented a new SDK for Spin,” [Mikkel Mørk Hegnhøj](https://www.linkedin.com/in/mikkelhegn/?originalSubdomain=dk), Fermyon’s head of product and developer relations, told me during Open Source Summit EU here in Vienna. “The new JavaScript SDK, built on top of Starling Monkey essentially helps us provide proper Fetch support for the Fetch API, but it also offers a much wider range of compatibility with Node.js APIs. A lot of the stuff you used to solve with Node.js for backend services can now be handled by JavaScript in this new environment.”

Spin JavaScript SDK is under the Fermyon’s Spin umbrella. Spin is a developer tool you can use to build serverless WebAssembly workloads or apps. Spin supports a wide range of programming languages such as [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/), C++ and others in addition to JavaScript. With the Spin JavaScript SDK, language-specific commands needed to compile JavaScript code into WebAssembly are processed. Spin was also designed to simplify the development process through access to templates for creating apps, compiling them to WebAssembly and testing them locally with the bundled runtime in the Spin CLI before deploying to different environments, according to Spin documentation.

## Let’s Run It
In order to add your JavaScript code to the Spin JavaScript SDK, you need to first install [Spin.](https://github.com/fermyon/spin)

The templates are installed with:

Create and build a new app:

Create a new app from the template installed in the previous step:

Change directory into the app:

Install the dependencies and build the app:

Test your app using e.g. curl in another terminal:

You should see something like this:

Being able to run JavaScript apps on backends is the result of decades of work on JavaScript and, not so recently, WebAssembly. For background, toward the beginning of what is popularly known as the World Wide Web, there was JavaScript. JavaScript has been around since 1995, when [Brendan Eich](https://thenewstack.io/brendan-eich-on-how-javascript-survived-the-browser-wars/) created the language to support Netscape, the now sadly defunct yet aesthetically pleasing web browser that was revolutionary for its time. Since then, the [ECMAScript](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) standard has served to underpin web development, representing the vast majority of applications that run in the web browser.

More recently, WebAssembly — which actually has been around for a while — has emerged. After the World Wide Web Consortium (W3C) named it as a web standard in 2019, it has become the fourth web standard with HTML, CSS and JavaScript. But while web browser applications have represented Wasm’s central and historical use case, again, the point is that it is designed to run anywhere on a properly configured CPU — this is where Wasm and JavaScript both bifurcate and become more integrated for some use cases.

Wasm and JavaScript remain closely linked, yet Wasm is very much about other things in addition to JavaScript. In a nutshell, Wasm’s original purpose to help JavaScript run more efficiently in the web browser remains a key component of their integration. That integration now extends beyond the web browser and into edge and server applications for which JavaScript alone has not been the best fit.

This is due to how Wasm runs in a binary format on a CPU level. And lest we forget, unlike JavaScript, Wasm is not a programming language. One of the main beauties of Wasm is that its functionality enables it to accommodate a number of different languages in addition to JavaScript, including [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/), [Rust, of course,](https://thenewstack.io/rust-and-c-work-better-for-webassembly/) as well as Go, .NET, C++, Java and PHP.

So, WebAssembly can integrate JavaScript when needed, but it is not limited to integrating JavaScript. This integration and use with JavaScript have been a cornerstone of the symbiosis between WebAssembly and JavaScript, especially in the sphere of web applications.

The JavaScript SDK was built on a project called [Javy](https://github.com/bytecodealliance/javy), which is part of the Bytecode Alliance, a group of people and organizations focused on WebAssembly system interfaces. The Javy project initially used QuickJS, a minimal but complete implementation of the JavaScript runtime according to the spec. This original JavaScript SDK was based on QuickJS but offered limited flexibility for creating new components.

Flash forward to a few months ago, to the development of the Bytecode Alliance project called [ComponentizeJS](https://github.com/bytecodealliance/ComponentizeJS). According to Hegnhøj and Fermyon’s documentation, this project allows the generation of arbitrary bindings and uses StarlingMonkey as the engine, which is based on Mozilla’s SpiderMonkey engine. The shift brought the SDK more in line with service-worker specifications, offering a larger API surface for developers to create more varied apps and improving compatibility with many Node.js packages that previously didn’t work with the older SDK.

One of the biggest improvements in the new SDK is the Fetch implementation. Previously, Fetch was a basic implementation that only supported simple outbound requests. Now, Fetch is compliant with the service-worker specification, allowing packages that depend on a fully implemented Fetch, such as the [AWS](https://aws.amazon.com/?utm_content=inline+mention) SDK for SQS and S3, to work. This enhancement enables the development of more varied applications, such as those that store and retrieve data from S3.

The goal of the new JavaScript SDK for Spin was to make it more idiomatic for experienced JavaScript developers, Hegnhøj said. The new API mimics [Express.js](https://thenewstack.io/a-showdown-between-express-js-and-fastify-web-app-frameworks/) to a degree, a popular framework for building web applications. The signature of the SDK was altered to be more Express-like, and the SDK now allows streaming responses, Hegnhøj said.

The new SDK introduces component IDs internally, and StarlingMonkey targets the service-worker specification, meaning it does not have access to all Node.js APIs. Some packages that rely on Node.js APIs like the filesystem or process won’t work natively, but the wasi-exd library provides a polyfill, allowing the use of features such as process.env with some modifications.

StarlingMonkey is compatible with all WebAssembly runtimes, meaning applications that don’t rely on Spin-specific features like key-value storage, SQLite or [Postgres](https://thenewstack.io/postgres-is-now-a-vector-database-too/) should run on any WebAssembly runtime that supports OAC3. Even applications without Spin-specific features should run in any supported runtime without issues, Hegnhøj said.

## Work Ahead
Improvements to the new Spin JavaScript SDK are in order. In a [blog post, ](https://www.fermyon.com/blog/introducing-the-new-js-sdk)[Till Schneidereit](https://de.linkedin.com/in/tillschneidereit), a principal engineer at Fermyon and a co-founder of the Bytecode Alliance noted that:

- The edge cloud platform provider Fastly, which is a significant contributor to the WebAssembly project and the Bytecode Alliance, continues to contribute to JavaScript execution in WebAssembly. The first iteration of this work has been integrated into StarlingMonkey, resulting in execution speeds several times faster, depending on the workload. This integration was completed recently but has not yet been incorporated into the JavaScript SDK, but it will be added in the near future, Schneidereit wrote.
- A key improvement to StarlingMonkey is nearing completion, allowing parts of the runtime and the web APIs it provides to be implemented in Rust instead of C++, Schneidereit wrote. This change will make it easier to stay updated with the latest developments in the web ecosystem and provide a more complete and compatible implementation of web APIs that are essential for existing JavaScript applications. Since not all JavaScript code relies on web standards-based APIs, with some using Node.js APIs, a compatibility layer is being developed for these APIs to enable their use in Spin applications, Schneidereit wrote.
- Support for more trigger types: The new JavaScript SDK currently supports only HTTP triggers. Work is underway to add support for additional trigger types, such as Cron and Redis triggers, Schneidereit wrote.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)