# Python Meets JavaScript, Wasm With the Magic of PythonMonkey
![Featued image for: Python Meets JavaScript, Wasm With the Magic of PythonMonkey](https://cdn.thenewstack.io/media/2024/07/eacad406-pythonmonkey2-1024x512.png)
[PythonMonkey](https://github.com/Distributive-Network/PythonMonkey), an innovative [JavaScript](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/) runtime embedded within [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/), is bridging the gap between two of the world’s most [popular programming languages](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/).
PythonMonkey is a JavaScript runtime living inside of Python, built on top of [Mozilla](https://thenewstack.io/mozilla-llamafile-builders-projects-shine-at-ai-engineers-worlds-fair/)‘s [SpiderMonkey](https://spidermonkey.dev/) engine. Developers can use it as a Python library for running JavaScript code in Python.

[Distributive](https://distributive.network/), a Kingston, Ontario Canada-based cloud computing startup, built PythonMonkey so they could port their JavaScript [NodeJS](https://thenewstack.io/node-js-22-release-improves-developer-experience/) SDK directly to Python without having to maintain both projects, essentially cutting their code maintenance costs in half.
“We’re hoping PythonMonkey will help bridge the gap between the millions of npm packages and Python developers as well as potentially one day standing on its own as a JavaScript runtime competing with [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/), [Bun](https://thenewstack.io/meet-bun-a-javascript-runtime-for-the-whole-dev-lifecycle/) and [Deno](https://thenewstack.io/with-additional-funding-deno-sets-out-to-challenge-node-js/) but with the ability to use ‘any’ Python package from JS,” said [Will Pringle](https://www.linkedin.com/in/will-pringle/), a software developer at Distributive.

Indeed, PythonMonkey enables developers to use Python code in JavaScript and vice versa with ease and virtually no performance loss, Pringle wrote in a [blog post introducing the technology](https://medium.com/@willkantorpringle/pythonmonkey-javascript-wasm-interop-in-python-using-spidermonkey-bindings-4a8efce2e598) last year — meanwhile, Distributive plans to release PythonMonkey 1.0 next month.

## WebAssembly API and Engine
“For instance, it’ll be possible to call Python packages like [NumPy](https://numpy.org/) from within a JavaScript library, or use NPM packages like [crypto-js](https://www.npmjs.com/package/crypto-js) directly from Python,” Pringle wrote “Also, executing [WebAssembly](https://thenewstack.io/webassembly-adoption-is-slow-and-steady-winning-the-race/) (Wasm) modules in Python becomes trivial using the WebAssembly API and engine from SpiderMonkey.”

Yes, the library leverages SpiderMonkey’s features, including its WebAssembly engine, allowing Python to run untrusted Wasm code in a sandbox from a variety of languages such as C, C++, [Rust](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/), and others.

In addition, developers could use PythonMonkey to refactor a slow “hot loop” written in Python to execute in JavaScript instead, taking advantage of SpiderMonkey’s just-in-time compiler for near-native speed, Pringle wrote.

Moreover, PythonMonkey also ships with PMJS, a JavaScript runtime environment like Node.js that supports calling Python libraries from JavaScript.

## Simple Code Examples
In his post, Pringle included some coding guidance, including the “hello world” example below that demonstrates a string generated from JavaScript being returned to a Python context:

>>> import pythonmonkey as pm
>>> hello = pm.eval(” ‘Hello World’.toUpperCase(); “)
>>> print(hello)
‘HELLO WORLD’

This more involved example below demonstrates passing the Python print function as an argument to a JavaScript function and then calling that JavaScript function from Python:

>>> import pythonmonkey as pm
>>> hello = pm.eval(“(func) => { func(‘Hello World!’)}”)
>>> hello(print)
Hello World!

This example uses pmjs to execute a JavaScript file that uses Python’s print function (This can be executed with pmjs main.js):
*main.js*

const pyPrint = python.eval(“print”);
pyPrint(“Hello, World!”); // this outputs “Hello, World!”

## Project Goals
The project’s goals include:

- Fast and memory-efficient.
- Make writing code in either JS or Python a developer preference.
- Use JavaScript libraries from Python.
- Use Python libraries from JavaScript.
- The same process runs both JavaScript and Python VirtualMachines — no serialization, pipes, etc.
- Python Lists and Dicts behave as JavaScript Arrays and Objects, and vice-versa, fully adapting to the given context.
## PythonMonkey Origins
Distributive’s CTO [Wes Garland](https://www.linkedin.com/in/wesley-garland-2203a23/) created PythonMonkey to make life easier for the company’s developers. Garland created a precursor to Node.js called[ gpsee](https://github.com/wesgarland/gpsee) around 2007 — built on Mozilla’s SpiderMonkey engine like PythonMonkey.

“We have a large, complicated client-side SDK at Distributive called dcp-client written in JavaScript,” Pringle told The New Stack. “There’s a lot of logic in there so we didn’t want to rewrite it in Python and maintain both projects — essentially doubling our development costs on the SDK. PythonMonkey is enabling us to port all the underlying logic from our JavaScript library to Python while only maintaining one codebase.”
Primarily a JavaScript Shop

Distributive mainly develops in JavaScript since the company needs to operate in the web stack.

“For context, we’re building [DCP (Distributive Compute Protocol)](https://distributive.network/platform), a marketplace for compute where people can rent CPU/GPU cycles from other people’s home computers,” Pringle said. “The idea is that if you have a computer lying around not doing anything (sitting idle), you can hook it up to our cloud computing network and earn money computing other people’s workloads. The program that turns your computer into a worker node is a JavaScript engine that can execute JS programs, WebAssembly, or any programming language that can compile to (or has an interpreter compiled to) WebAssembly.

“You can also run it directly in the browser. Anyway, as a result, we have a lot of JavaScript code in our implementation, but everyone wants to write this kind of stuff in Python, so PythonMonkey enables Python developers to use our product (DCP) — without us having to re-write our SDK.”

Pringle is now working on Distributive’s Python SDK and the company expects to release it in the coming weeks.

## Evolution of the Project
Since launching PythonMonkey last July, Distributive has made a vast number of enhancements to the technology, including:

### Web Stack APIs
- Implemented
`XMLHttpRequest`
APIs from the ground up**—**enabling popular JavaScript libraries like socketio to run in PythonMonkey using the standard JavaScript networking APIs. - Implemented several timer global functions:
[setInterval](https://developer.mozilla.org/en-US/docs/Web/API/setInterval)/[clearInterval](https://developer.mozilla.org/en-US/docs/Web/API/clearInterval), setImmediate/clearImmediate, and setTimeout/clearTimeout, returning Node.js-style`Timeout`
class with`.ref()`
and`.unref()`
methods. - Implemented all missing methods from the
`console`
API, now the`console`
behaves the same as the web spec[https://console.spec.whatwg.org/](https://console.spec.whatwg.org/). `atob`
,`btoa`
functions.
### Cross-language Coercion
- Users can now wrap/proxy any arbitrary Python objects in JavaScript.
- Better cross-language iterator support.
### Exceptions Handling
- Implemented complete cross-language stack traces.
- Improved cross-language nested exceptions handling and promise rejection handling.
- uncaughtExceptionHandler
### JavaScript Engine Update
- Updated SpiderMonkey to the latest version, so users can enjoy the same new JS + WASM language features as the latest Firefox, and performs better.
- Contributed a
[patch](https://bugzilla.mozilla.org/show_bug.cgi?id=1904747)to SpiderMonkey fixing a[bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1904747).
### Developer Experience Improvement
- Better developer experience with an embedded debugger tool called
`pmdb`
(inspired by`gdb`
), and WTFPythonMonkey (inspired by[wtfnode](https://www.npmjs.com/package/wtfnode).) - Better Python-type hints and documentation for developers.
## Module System
PythonMonkey’s module system allows easy porting of JavaScript libraries to Python and vice versa. The runtime enables developers “to easily port their JavaScript libraries to Python, without suffering the costly burden of rewriting their libraries in Python and maintaining the ports,” Pringle wrote.

Additionally, “JavaScript is also ideal for highly asynchronous workloads, whereas Python is not,” Pringle explained in his post. “At Distributive, we intend to use this library to execute our complex [dcp-client](https://docs.dcp.dev/api/dcp-client/index.html) library, which is written in JS, and enables distributed computing on the web stack.”

Meanwhile, PythonMonkey aims to minimize memory consumption and copy overhead by sharing immutable backing stores when possible, Pringle noted.

## PythonMonkey Roadmap
“PythonMonkey’s roadmap includes a number of features and improvements to expand its usability, such as importing Python modules in JavaScript using esm syntax, XMLHttpRequest, implementing a standalone event loop without relying on Python’s, and support for Node.js APIs such as fs, path, process, which would allow Python to use NPM packages like [express.js](https://expressjs.com/) and [socket.io](https://socket.io/),” Pringle wrote at launch last year. The company has achieved much of this.

Another proposed goal further down the roadmap is to expand PMJS into a fully integrated Node.js environment which could act as a drop-in replacement for Node.js which also has the ability to use Python packages from JavaScript.

With these planned enhancements, PythonMonkey and PMJS aim to offer a fully integrated Python-JS environment for developers.

## Superior to Related Projects?
Meanwhile, Pringle compared PythonMonkey to related projects like [JS2PY](https://github.com/PiotrDabkowski/Js2Py), [PyV8](https://github.com/okoye/PyV8), and [Metacall](https://github.com/metacall/core), highlighting PythonMonkey’s advantages in terms of performance and features.

You can try PythonMonkey out on a [Google Colab](https://colab.research.google.com/drive/1INshyn0gNMgULQVtXlQWK1QuDGwdgSGZ?usp=sharing).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)