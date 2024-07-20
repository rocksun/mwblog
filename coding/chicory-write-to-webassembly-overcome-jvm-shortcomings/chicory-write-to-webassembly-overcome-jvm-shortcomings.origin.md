# Chicory: Write to WebAssembly, Overcome JVM Shortcomings
![Featued image for: Chicory: Write to WebAssembly, Overcome JVM Shortcomings](https://cdn.thenewstack.io/media/2024/07/2d1fbb61-wyxina-tresse-h9lxuk5eamy-unsplash-1024x683.jpg)
The [Java Virtual Machine (JVM)](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) and [WebAssembly](https://thenewstack.io/webassembly/) have their inherent capabilities. The JVM has been tried and trusted for decades to run [Java code](https://thenewstack.io/trash-pandas-love-enterprise-java-code/) and applications. As an inherent part of running Java applications on cloud, mobile especially, on-premises or anywhere Java is run, the JVM has been in wide-scale use across most sectors, including finance, manufacturing, banks and finance. Security and monitoring are provided and through [just-in-time (JIT)](https://thenewstack.io/how-to-reduce-cloud-waste/) compilers the JVM has been developed over the years to execute Java code on a range of devices and endpoints, including edge devices, servers, mobile environments and PCs.

WebAssembly (also known as Wasm), on the other hand, has emerged more recently as a way to bundle applications of your choice, written in the language of your choice, and deploy simultaneously across any host environment from edge to cloud wherever there is a [CPU instruction set](https://thenewstack.io/webassembly-isnt-software-its-a-computer/) that is compatible with Wasm. Like the JVM, Wasm is — rightly or wrongly — associated with “write once, run anywhere,” although language compatibility struggles to finalize a standard component model to standardize endpoint distribution and other challenges remain. Again, the JVM also is write once, run anywhere only where there are JVM endpoints, unlike a WebAssembly module, which in theory should be able to run anywhere there is a device capable of running a CPU instruction set.

Meanwhile, [Chicory](https://github.com/dylibso/chicory) was created to bring some of the benefits of Wasm to native JVM. It’s like a virtual machine within a virtual machine, given the security, the tunnel, the sandbox aspects of WebAssembly. With an additional closed module that the JVM offers, the user benefits from a double sandbox, so to speak.

As described on [Chicory’s readme.md file on GitHub,](https://github.com/dylibso/chicory/blob/main/README.md) Chicory is a JVM-native WebAssembly runtime. It was created so WebAssembly programs can run with zero native dependencies or [Java Native Interface (JNI)](https://docs.oracle.com/javase/8/docs/technotes/guides/jni/). “Chicory can run Wasm anywhere that the JVM can go. It is designed with simplicity and safety in mind,” its creators write.

## Wasm Help
On its own, Wasm can’t do anything but compute, explained [Benjamin Eckel,](https://www.linkedin.com/in/benjamin-eckel-b025831a3/) co-creator of Chicory and CTO and co-founder of [Dylibso](https://dylibso.com/) — which makes [Extism](https://thenewstack.io/extism-v1-run-webassembly-in-your-app/), a framework designed to enable software end users to enhance existing applications with Wasm. Since, in theory, it cannot affect the outside world, WebAssembly might seem like a weakness, but this is actually Wasm’s greatest strength, Eckel said.

By default, programs are sandboxed and have no capabilities. If a program needs capabilities, capabilities must be provided. This puts the developer in the position of the operating system. A module can ask for a capability by listing an “import” function in the bytecode format. This import can be fulfilled with a host function written in Java. Regardless of the language of the module, the module can call this Java function when needed. Host functions can be thought of as syscalls or a language’s standard library, but host functions are determined and implemented in Java, Eckel said.

If linking to a native object in the JVM, the object must be shipped with the application or library, Eckel noted. One of the main reasons for using the JVM is that it compiles to a platform-independent bytecode, which is the primary benefit of writing your application for the JVM. However, this creates the problem of compiling for every OS, architecture, and libc that needs to be shipped, he said.

On the runtime side, to communicate with some shared object, most systems require using a foreign function interface. In Java, there are a few different names for this, but it is roughly the same concept. There is significant complexity and many problems when execution leaves the safety and observability of the JVM, Eckel said.

If staying within the JVM boundaries, guaranteed memory safety is provided, which has been a reliable feature for a long time, according to Eckel. Fault isolation is also provided, meaning that if a Wasm program is like JVM bytecode, it cannot crash the JVM, which is a major advantage for many applications. Additionally, a super-advanced JIT is available. When using a foreign function interface (FFI), the JIT from the JVM sees the program as a series of holes, going in and out. However, if everything was just one continuous stream of JVM bytecode, the benefits would be much greater, he said.

Memory vulnerabilities are increasingly a concern, and the U.S. government has signaled they will start [enforcing use of memory-safe languages](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/), Eckel said in an email response. Meanwhile, by default, Java code is memory-safe and the implementation of the JVM just needs to be checked. “But, if you call native code, you leave the safety of the JVM,” Eckel said. “It’s more opportunity for attackers and more opportunities for mistakes.”

## Inspiration
![](https://cdn.thenewstack.io/media/2024/07/86c0bad4-capture-decran-2024-07-18-170609-1024x450.png)
Andrea Peruffo, principal software engineer, for Red Hat, explains how to get started with Chicory.

The open source project [Wazero](https://wazero.io/) has served as an inspiration for Chicory. With it, runtimes execute WebAssembly modules, which are usually binaries with a .wasm extension, according to Wazero’s documentation. Wazero, for now, is also a zero-dependency WebAssembly runtime written in Go. So, like Chicory, Wazero was created to help make writing a runtime in different languages — C++, Go, Java, Rust and others — easier.

One of the more interesting use cases for Chicory is for identity management software, [Andrea Peruffo,](https://www.linkedin.com/in/andrea-peruffo-32269178/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=pt) principal software engineer, for [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), discussed during a talk “Chicory: Creating a Language-Native Wasm Runtime,” during the Linux Foundation [Wasm I/0 conference](https://www.youtube.com/watch?v=00LYdZS0YlI&ab_channel=WASMI%2FO) in 2023. He described how [Keycloak](https://thenewstack.io/how-to-integrate-openshift-with-keycloak/) is a very popular identity management software that enables single sign-on and other related operations. However, what might not be known is that it contains complex, spaghetti code designed to integrate with any kind of legacy system. Active Directory can be on one side, [LDAP](https://thenewstack.io/deploy-the-ldap-directory-system-to-an-ubuntu-server/), and then Kerberos, and so on. While rewriting these integrations in Rust might seem appealing, it’s not practical. This is where the power of Java comes in. Enterprise applications like these are not easy to replace, so the goal is to empower them and make their usage more flexible, Peruffo noted.

In Keycloak, if custom operations are needed, such as checking a user’s identity against different providers or inserting custom business rules, typically a Java plugin has to be written, Peruffo continued. But why limit development to Java? By importing a JVM library, plugins can be written in any language that compiles to WebAssembly, such as Rust, C, Go, JavaScript and more. An initial proof of concept was created in just two hours by importing a JVM library. This approach makes enterprise applications, which are often heavy and complex, easily extensible with a lightweight system. It simply involves importing a library and enabling the application to load and run Wasm code. This capability is incredibly useful, Peruffo said.

## Up and Running
Chicory is not able to overcome Java’s inherent slowness, compared to other languages, yet it remains potentially practical for the reason described above. Still, Chicory is a new project and work remains to be done. Thus far, it can (according to the documentation):

Bootstrap a bytecode interpreter and test suite and features:

- Wasm
[binary parser.](https://github.com/dylibso/chicory/blob/main/wasm) - Simple bytecode interpreter
- Establish basic coding and testing patterns
- Generate JUnit tests from a
[wasm test suite.](https://github.com/dylibso/chicory/tree/main/test-gen-plugin)
#### By the end of summer, it should be able to:
- Make all tests green with the interpreter (important for correctness).
- Implement validation logic (important for safety).
- Draft of the v1.0 API (important for stability and dx).
Other new roadmap updates from the project’s readme.md include:

- Completion of about 30,000 tests to ensure Wasm specifications are met.
- Bytecode validation is 95% complete.
- The ahead-of-time compilation is in production and has proven to be much faster than the interpreter mode, the project’s creators say.
## Set-Up
While I was not yet able to get Chicory to load and run on my Windows laptop, stay tuned for a review about how to set it up and run. Chicory’s readme.md provides solid setup instructions to get started, in the meantime:

Add the `com.dylibso.chicory:runtime`
dependency to the dependency management system to use the runtime:

12345 |
<dependency><groupId>com.dylibso.chicory</groupId><artifactId>runtime</artifactId><version>0.0.10</version></dependency> |
Implementation:
1 |
'com.dylibso.chicory:runtime:0.0.10' |
The Java generator CLI is available for download on Maven at the link:
1 |
https://repo1.maven.org/maven2/com/dylibso/chicory/cli/<version>/cli-<version>.sh |
For more information about the project and how to contribute, a [dedicated Zulip channel](https://chicory.zulipchat.com/join/g4gqsxoys6orfxlrk6hn4cyp/) is available.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)