# What’s in the New Node.js, and How Do You Install It?
![Featued image for: What’s in the New Node.js, and How Do You Install It?](https://cdn.thenewstack.io/media/2025/01/3878e196-getty-images-nvlb6gvemlc-unsplash-1-1024x683.jpg)
[Node.js](https://thenewstack.io/dev-news-node-js-23-and-rust-1-82-released-this-week/) is still one of the most popular runtimes for [JavaScript](https://thenewstack.io/5-technical-javascript-trends-you-need-to-know-about-in-2025/). In fact, it’s kind of a juggernaut: It has seemed unstoppable since its introduction in 2009. In fact, Node.js is the industry standard runtime for JavaScript, and is used by companies like [Netflix](https://thenewstack.io/developer-productivity-engineering-at-netflix/), Uber, eBay, PayPal, [LinkedIn](https://thenewstack.io/linkedin-shares-its-developer-productivity-framework/), Trello, [NASA](https://thenewstack.io/nasa-programmer-remembers-debugging-lisp-in-deep-space/), Walmart, Groupon and many more.
This open source, cross-platform runtime environment is an amazing tool for developing scalable network applications, and has become one of the most widely used web frameworks. One reason Node.js is so popular is that it can reduce loading time by as much as 60%. This is immensely important for applications at scale.

But what is there to be excited about in the latest release? Truth be told, you have to go back to version 23.0.0 to find a release that isn’t specifically listed as a security release. And since version 23.0.0 was released on Oct. 16, 2024, it might seem a bit long in the tooth (in tech years), but it is an LTS release, so it’s going to be sticking around for some time.

As far as what’s new in Node.js 23, let’s take a look.

There are four big highlights for this release:

- The require(esm) statement has been enabled by default. This allows you to load ESM modules using the require() function. This is of particular use for projects that still rely on
[CommonJS](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/)but want to take advantage of ESM features. - Removed support for Windows 32-bit systems.
- The
`node --run`
command has been stabilized. - The test runner has been enhanced.
### require(esm)
With require(esm) enabled by default, Node.js will not longer throw the ERR_REQUIRE_ESM error when require() is used to load an ES module. If, however, the ES module being loaded contain top-level await, it can still throw ERR_REQUIRE_ASYNC_MODULE.

### Windows 32-Bit Systems
If you’re still using a 32-bit Windows operating system, Node.js 23.0.0 will no longer function.

### node –run
Node.js provides a built-in task runner that allows you to execute specific commands that are defined in a package.json file. This is done with the `--run`
flag, and with version 23.0.0, the option has been improved and is now more stable.

### Test Runner
The Node.js test runner makes it possible to create JavaScript tests. Here are some of the enhancements to the test runner:

- It now supports glob matching coverage files.
- Includes updates to v8-stats.
- Detects-only test when
`--test`
is not used. - Always makes spec the default reporter.
- Expoes lcov reporter as a newable function.
- Supports custom arguments in run().
- Added test:summary even.
- Added support for coverage via run().
## Miscellaneous changes
Other changes to Node.js in v23 include:

- V8: cherry-pick cd10ad7cdbe5
- Use GCC 12 on AIX for versions of Node.js starting with v23
- Propagate aborted state to dependent signals before firing events
- Change WeakMap and WeakSet comparison handling
- Buffer: throw when writing beyond buffer
- Buffer: Make file cloneable
- Build: reset embedder string to “-node.0”
- Build: Include v8-sandbox.h
- CLI: remove deprecated v8 flag
- CLI: remove –no-experimental-global-customevent flag
- Crypto: runtime deprecate crypto.fips
- Net: validate host name for server listen
- Process: remove process.assert
You can read the entire [Node.js change log here](https://nodejs.org/en).

## How To Install Node.js 23
Let’s first install Node.js 23 on an Ubuntu-based [Linux](https://thenewstack.io/introduction-to-linux-operating-system) distribution. To do that, follow these steps.

Install the necessary dependencies with the command:

*sudo apt-get install ca-certificates curl gnupg -y*
Import the necessary GPG key with the following:

Add the Node.js repository with the following command:


Update apt with:

*sudo apt-get update*
Install Node.js with the command:

*sudo apt-get install nodejs -y*
Next, we’ll install Node.js 23 on macOS. To do this, we’ll use nvm as the installer.

Download and install nvm with the command:

*curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash*
Download and install Node.js with:

*nvm install 23*
Finally, we’ll install Node.js 23 on Windows, using fnm.

Download and install fnm using winget with the following command:

*winget install Schniz.fnm*
Install Node.js 23 with the command:

*fnm install 23*
You can verify the installation with the `node -v`
command.

You should see something like this in the output:

*v23.6.1*
If you find that Linux still reports version 20, you’ll need to remove Node.js (*sudo apt-get remove nodejs -y*) and then install it with the following steps.

Download and install nvm with the command:

*curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash*
Close and reopen your terminal window. Once the terminal is open, install Node.js with:

*nvm install 23*
And that’s all there is to installing the latest version of Node.js. This powerhouse runtime will serve you well for years to come.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)