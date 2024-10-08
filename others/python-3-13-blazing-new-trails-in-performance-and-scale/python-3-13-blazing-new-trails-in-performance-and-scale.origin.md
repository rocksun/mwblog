# Python 3.13: Blazing New Trails in Performance and Scale
![Featued image for: Python 3.13: Blazing New Trails in Performance and Scale](https://cdn.thenewstack.io/media/2024/10/48878a39-kyle-glenn-hn2xf1sk_y4-unsplash-1-1024x683.jpg)
[Python 3.13](https://docs.python.org/3.13/whatsnew/3.13.html), [expected to be released today](https://peps.python.org/pep-0719/), represents a significant step forward for the [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) programming language, particularly in terms of performance and developer experience, with the experimental free-threaded mode and [just-in-time (JIT) compiler](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) laying groundwork for future improvements.
[Initially scheduled for release on Oct. 1](https://www.phoronix.com/news/Python-3.13-rc3-Released), the new release was delayed because of a performance regression and the publication date for the latest stable release of Python was moved to Oct. 7.
As noted, some of the major changes to Python include a new [interactive interpreter](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter), as well as experimental support for running in a [free-threaded mode](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-free-threaded-cpython) and a [JIT compiler](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-jit-compiler).

## Free Threading
The experimental free-threaded [CPython](https://thenewstack.io/how-python-is-evolving/) feature allows running with the [Global Interpreter Lock (GIL)](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) disabled. It requires a separate executable and can be installed via official Windows and macOS installers or built from source. It enables full utilization of multicore processors. And it currently takes a performance hit for single-threaded operations.

“Free threading is an attempt to remove the [Global Interpreter Lock](https://realpython.com/python-gil/) from CPython, which has traditionally been the biggest obstacle to achieving [thread-based](https://realpython.com/intro-to-python-threading/) parallelism when performing [CPU-bound](https://en.wikipedia.org/wiki/CPU-bound) tasks,” wrote [Bartosz Zaczyński](https://www.linkedin.com/in/bzaczynski/?originalSubdomain=pl), a content creator at Real Python, [in an article](https://realpython.com/python313-free-threading-jit/). “In short, the GIL allows only one thread of execution to run at any given time, regardless of how many cores your CPU is equipped with. This prevents Python from leveraging the available computing power effectively.”

Historically, Python’s GIL prevented true concurrent execution of threads, [Stanley Seibert](https://www.linkedin.com/in/stanleyseibert/), senior director of Community Innovation at [Anaconda](https://thenewstack.io/faster-python-easier-access-to-llms-anacondas-ai-roadmap/), told The New Stack. However, the new experimental feature in Python 3.13 allows for concurrent execution of pure Python code. The feature aims to better utilize multicore processors without sacrificing single-thread performance. It will be turned off by default in this release due to its experimental nature. The feature was developed by Meta engineers and approved by Python’s steering committee. Anaconda is working on test packages for the community to try out this feature, Seibert said.

## JIT Compiler
Meanwhile, “Up to now, you could take advantage of various JIT compilers for Python through external tools and libraries only,” wrote Zaczyński. “Some of them, like [PyPy](https://pypy.org/) and [Pyjion](https://pypi.org/project/pyjion/), offered more or less general-purpose JIT compilers, while others, such as [Numba](https://numba.pydata.org/), focused on specific use cases like numerical computation.”

The new experimental JIT compiler in Python 3.13 uses a fairly recent algorithm named [copy-and-patch](https://en.wikipedia.org/wiki/Copy-and-patch), he wrote.

“The basic idea behind this compilation technique boils down to finding a suitable template with pre-compiled machine code for the target CPU and filling it with the missing information, such as memory addresses of variables,” he noted in his article.

Zaczyński added that the long-term plan is to enhance Python’s JIT to the point where it actually makes a noticeable difference in code execution performance without taking much additional memory.

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin), an analyst at Omdia, called the JIT compiler “a huge deal,” as it puts Python on a more even footing opposite storied and enterprise-focused JIT-based languages like Java.
“More than that, this JIT implementation introduces a performance improvement over traditional JIT architectures,” he told The New Stack. “Rather than walking code through an intermediate language before creating machine code can be pretty slow, Python 13.3’s implementation uses a copy-and-patch approach that doesn’t require the full JIT to run inside the Python runtime.”

[Andrew Cornwall](https://www.linkedin.com/in/acornwall/), an analyst at Forrester Research, agrees that the two most significant runtime changes in Python 3.13 are experimental, “so everyday CPython users won’t see much difference yet,” he told The New Stack. However, Python is laying the groundwork for faster code running on multiple processors.
“A JIT compiler should make CPython run faster for everyone once enabled, but Python is being conservative and leaving it off by default for now,” Cornwall said. Yet, “The ability to disable the global interpreter lock could be more disruptive, by allowing Python libraries to take advantage of more cores if the libraries can support multithreading. Those developing C libraries will need to investigate the effects of disabling the GIL. However, for everyday users those changes are further away — they’re in a separate python3.13t binary for now.”

Free threading is about trying to use more cores. Yet, “the JIT compilation is about trying to get more out of the single core just by making the interpreter more efficient,” Seibert told The New Stack. “This release will include the first version of that JIT compiler, and that will just the goal is for that to just invisibly make everything faster.”

Indeed, there’s been a multiyear focus on speed for Python, Seibert said. “I know historically Python’s been slower but easier to program [than some other languages]. This [JIT compiler] kind of brings it into the realm of like C or C++,” he said.

## Interactive Interpreter Improvements
Meanwhile, the improved interactive interpreter features multiline editing with history preservation, direct support for read–eval–print loop (REPL)-specific commands including help, exit, and quit, color-enabled prompts and tracebacks by default, interactive help browsing (F1 key), history browsing (F2 key), and “paste mode” for easier code pasting (F3 key).

“There’s a new interactive interpreter that adds some quality of life things, like coloring and being able to edit multiple lines of Python code at the same time — stuff that you could have done with [IPython](https://ipython.org/), but now it’s built into the interpreter,” Seibert said.

Python’s new [interactive](https://docs.python.org/3.13/glossary.html#term-interactive) shell, available by default, is based on code from the [PyPy project](https://pypy.org/).

## Other Key Changes
Moreover, Python 3.13 has an incremental [garbage collector](https://thenewstack.io/time-to-get-the-garbage-out-of-webassembly/) implementation that reduces long pauses when cleaning up allocated memory, Cornwall said.

In addition, “Platform support now includes mobile devices (iOS and Android are both at tier 3, meaning there’s at least one core developer involved). And [Wasm](https://thenewstack.io/what-makes-wasm-different/) support has moved from [emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) to [WASI](https://thenewstack.io/wasi-0-2-unlocking-webassemblys-promise-outside-the-browser/),” he said.

## More Improvements Under the Hood
Also, “There are a few deprecated libraries — if you’re using [cgi](https://docs.python.org/3/library/cgi.html) or [crypt](https://docs.python.org/3/library/crypt.html), for instance, you’ll need to find alternatives,” Cornwall told The New Stack. “Language changes are not likely to bite most users. Previously undefined semantics around locals() have now been defined, but that’s in the weeds for most developers. With this release, most developers will notice the new paint job but not the significant changes under the hood.”

One such developer who has noticed changes under the hood is [Tom Tang](https://github.com/xmader), an engineer at [Distributive](https://distributive.network/), the creator of the [PythonMonkey](https://pythonmonkey.io/) project. Tang is a core developer for the [PythonMonkey project](https://thenewstack.io/python-meets-javascript-wasm-with-the-magic-of-pythonmonkey/) and is currently working on bringing Python 3.13 support to PythonMonkey.

## API Stability: PythonMonkey Example
Tang said he has a different perspective as a systems developer who works deeply with the lower-level parts of Python, so the change of C API stability in Python 3.13 is one thing worth noticing.

Prior to version 3.13, Python’s C API changed frequently in every minor version, and there were plenty of undocumented internal APIs that were either broken or removed in every next Python release, Tang told The New Stack.

“This causes some troubles for us developing PythonMonkey, as PythonMonkey is promised to support multiple Python versions, and it’s very complicated. In Python 3.13, the CPython core maintainers made a [move to address the API instability](https://github.com/python/cpython/issues/106320) issue by making only stable public APIs available for use. Most of the undocumented ‘private’ APIs are removed in Python 3.13, and the remaining few are now documented and promoted to stable APIs.”

This move is important for Python extension developers as it lets you stay with the well-documented APIs, and forces you to really think about back and forward compatibility when dealing with the lower parts of Python, Tang said.

“On the other hand in the case of PythonMonkey, since we are dealing with very niche implementation details in the CPython interpreter to make PythonMonkey as fast and efficient as possible, hiding away the ‘internal APIs’ or the implementation details may have closed doors for us to further optimize PythonMonkey towards a faster cross-language runtime,” he said.

Besides, “It would be helpful to deeply integrated products like PythonMonkey if there were a more formalized API for accessing internals, even if these became part of an ‘unstable’ API,” Tang said.

## Do It All and Do It Well
Overall, the changes in Python 3.13 “are nice additions that in themselves will further solidify Python as a ‘go-to’ language within existing use cases, particularly for data, AI, and IT engineers,” Shimmin said. “However, to me, the most defining aspect of this release revolves around speed and scale.”

The attention the Python community is paying to performance and efficiency will, of course, solve some of Python’s current growing pains around performance. The updates in Python 3.13 “will also better secure Python’s reputation as a ‘do it all and do it well’ language across a broader range of use cases,” Shimmin said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)