We’ve all experienced a frozen web page followed by endless refreshing, frustrated sighs, and the occasional foot stomp, only to keep seeing the spinning wheel. In many cases, this is caused by a bottleneck in [JavaScript](https://thenewstack.io/introduction-to-javascript/)’s main thread.

The main thread is a single-lane highway where the browser processes everything in a strict sequence. It handles clicks, manages scrolling, renders animations, and executes your logic. Because it can only do one thing at a time, adding heavy computations to the mix creates a massive traffic jam. When the main thread is overloaded, the entire UI dies.

[We’ve talked a lot about WebAssembly (Wasm) lately](https://thenewstack.io/when-should-javascript-devs-use-the-power-of-webassembly/), so it should come as no surprise that Wasm is a good solution here. By combining the raw power of Wasm with [Web Workers](https://thenewstack.io/leveraging-web-workers-to-safely-store-access-tokens/), we can move those heavy calculations into a background lane. This takes the pressure off the main thread, allowing your users to continue scrolling and clicking without interruption.

To show you the benefit of using C with Wasm for calculations over JavaScript, this tutorial will help you build a high-performance [Fibonacci calculator](https://elementor.com/tools/fibonacci-calculator/). We’ll then run the Fibonacci sequence recursively using Wasm powered by a Web Worker and calculate using JavaScript so you can see how the timing stacks up.

By offloading intensive math to a background thread, we will demonstrate how to keep the user interface functional and fluid even when the processor is under heavy load. Though the recursive Fibonacci algorithm isn’t suited for a working application, this project serves as a blueprint for keeping web applications responsive.

Let’s get started.

First, make sure you have everything you need.

Create your project structure.

Open a terminal in your project and navigate to`wasm-worker-demo`. Once you’re in that folder, type`ls`and make sure you see your files,`index.html`, `main.js`, `worker.js`, `compute.c`. Once you’re sure you’re in the right place, we need to download the [Emscripten SDK](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/).

The Emscripten SDK compiles C/C++ to Wasm. We can’t move forward without it. In your terminal, type the following command:

This will add a folder called`emsdk`to your current directory.

Go into the`emsdk`folder with the command`cd emsdk`.

Install the latest verson of Emscripten:`./emsdk install latest`

Activate the SDK so your terminal can use it: `./emsdk activate latest`

The last step here is to set up your environment variables for this terminal session:`source ./emsdk_env.sh`

Confirm accurate set up with the command:`emcc -v`

Head back to your main project folder in the terminal.

We’re ready to start building out the files.

## Build Wasm calculation logic in C

Let’s start in the`compute.c`file. The algorithm we’re going to use for this demo is the recursive Fibonacci sequence. Cue the nightmares for anyone who’s gone to coding school. This algorithm, though inefficient for a production level application, is perfect for this demo. It creates billions of function calls and pushes the CPU to its limits.

## Emscripten: C to Wasm

Emscripten compiles our C code to a .wasm binary and a .js “glue” file. The .wasm binary is the compiled version of your C code. It contains the low-level instructions that the browser can execute at near-native speed. The .js “glue” file acts as the bridge between languages, providing the necessary code to load the binary and allowing JavaScript to call functions inside the WebAssembly module.

Type this command into your terminal to build the .wasm and .js files. In less than a minute you should see them appear in your project.

We use these file flags because:

* `-O3`: High-level optimization. It tells the compiler to make the code as fast as humanly possible.
* `-s MODULARIZE=1`: Wraps the output into a Promise-based module, making it easier to load safely.
* `-s EXPORTED_FUNCTIONS`: Tells Emscripten not to remove our`calculate_fib`function during optimization.

## Web Workers

Workers allow the calculation to happen outside of the main threads. We don’t want to run this Wasm on the main thread because a high-speed calculation of this magnitude will hijack the browser’s attention and cause the UI to freeze until the task is finished. To avoid this, we use a Web Worker. A Web Worker is a dedicated background script that runs in its own isolated thread, completely independent of the user interface.

The code below initializes the background environment by loading the Emscripten “glue” script and waiting for the WebAssembly module to be fully ready. Once loaded, it maps the C-based`calculate_fib`function into a usable JavaScript variable via`cwrap`. Then it sets up an event listener to receive numbers from the main thread, performs the calculation in isolation, and sends the result back without interrupting the user’s experience.

Running the server

You can run the server with the command `http-serve`. Navigate to `http://localhost:8080/` and you’ll see the webpage. Enter your number in the input box (start with numbers under 49) and watch the calculation timers.

## Putting it all together

While the worker handles the math, the`main.js` script acts as the command center. It is responsible for spawning the worker, sending it data, and updating the screen once the result is ready. This keeps the user interface alive and responsive, even while a massive calculation is happening just a few pixels away in the background.

The code below creates the worker instance and sets up a listener to catch the finished result. When you click the button, it records the start time and posts the input value to the worker, then waits for the response to calculate the total execution time.

## Bringing it to the browser

Now we have our `index.html`code. This is the basic HTML that facilitates the calculations in the browser.

## Results

For small numbers below 25, JavaScript is actually faster because the small startup cost of starting the WASM engine isn’t worth it for such a quick task. However, once we hit 25 and the calculations get heavier, the real value of WebAssembly starts to shine.

By the time you reach 50, the calculation is so massive it might never finish. But here is the most important part: because we are running this on a Web Worker, your browser remains alive. You can still click buttons, scroll, or even attempt to run the JavaScript version before the application eventually hits its limit. This proves that WASM isn’t just about raw speed. It is about keeping your UI responsive.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)