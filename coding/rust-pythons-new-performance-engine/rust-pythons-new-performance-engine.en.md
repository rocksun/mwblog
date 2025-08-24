[Python](https://thenewstack.io/what-is-python/) developers have always faced a trade-off: write elegant, readable code or go for high performance. For a long time, this meant reaching for [C](https://thenewstack.io/code-wars-rust-vs-c-in-the-battle-for-billion-device-safety/) extensions when speed mattered. But [Rust](https://thenewstack.io/rust-programming-language-guide/) has emerged as [Python’s performance](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) co-pilot.

## The Rust Revolution in Python

According to the [JetBrains](https://www.jetbrains.com/) [State of Python 2025](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) report, Rust usage for Python binary extensions jumped from 27% to 33% — a 22% increase in just one year. This represents a key shift in how the Python ecosystem approaches [performance optimization](https://thenewstack.io/how-to-master-javascript-performance-optimization/).

In a [blog post](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) about the study — which was based on a survey of 30,000 developers — [Michael Kennedy](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/#author), the founder of [Talk Python](https://talkpython.fm/) and a [Python Software Foundation](https://www.python.org/psf-landing/) Fellow, wrote that “At the [2025 Python Language Summit](https://us.pycon.org/2025/events/language-summit/), core developers shared an eye-opening statistic: ‘Somewhere between one-quarter and one-third of all native code being uploaded to [PyPI](https://thenewstack.io/the-top-5-python-packages-and-what-they-do/) for new projects uses Rust.’ This means that when developers start new performance-critical Python projects today, they’re increasingly choosing Rust over traditional C extensions.”

## Why Rust Is Winning Over C

Among the key reasons for Rust’s rapid adoption in the Python ecosystem is performance. Rust delivers C-level performance while maintaining Python’s ease of integration. Rust’s [zero-cost abstractions](https://stackoverflow.com/questions/69178380/what-does-zero-cost-abstraction-mean) and efficient memory management make it ideal for performance-critical components.

Rust also provides memory safety. Unlike C, Rust prevents common programming errors like [buffer overflows and memory leaks](https://thenewstack.io/secure-coding-in-c-avoid-buffer-overflows-and-memory-leaks/) at compile time. This makes it dramatically safer for extending Python without introducing security vulnerabilities or crashes.

In addition, Rust offers a high-quality developer experience with its modern toolchain, excellent error messages, and package manager ([Cargo](https://doc.rust-lang.org/cargo/)). It provides a better development experience compared to the often painful process of writing and debugging C extensions.

## Real-World Success Stories

The Python ecosystem already showcases several high-profile Rust success stories:

* **Polars** has revolutionized data science with DataFrame operations that often outperform [Pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/) by orders of magnitude. Built in Rust, it provides a Python API that feels natural while delivering unprecedented speed for data processing tasks.
* **Pydantic V2** rewrote its core validation engine in Rust, resulting in dramatic performance improvements for data validation and serialization across virtually every Python discipline — from web APIs to machine learning pipelines.
* **FastAPI’s ecosystem** increasingly relies on Rust-based components. The survey showed that [FastAPI](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/) usage jumped from 29% to 38% (a 30% increase), partly driven by its async-friendly architecture that pairs well with Rust-based server components.

## The Infrastructure Revolution

Rust’s influence extends beyond individual packages to Python’s core infrastructure. Traditional Web Server Gateway Interface (WSGI) servers are giving way to Asynchronous Server Gateway Interface (ASGI) compatible alternatives, many of which are built with Rust. Kennedy cited [Granian](https://github.com/emmett-framework/granian), a new Rust-based application server, as gaining significant traction. He also singled out [Uvicorn](https://www.uvicorn.org/), which, while Python-based, increasingly integrates with Rust components

## Next-Generation Tooling

Kennedy also noted that two new Python type checkers have emerged, both written in Rust. One is [ty](https://github.com/astral-sh/ty) from [Astral](https://astral.sh/), which is described as “an extremely fast Python type checker and language server.” The other is [Pyrefly](https://pyrefly.org/) from Meta, which is a high-performance alternative to traditional type checkers like [mypy](https://mypy-lang.org/).

“They are both vying to be the next generation tooling for type checking. Moreover, both of these tools provide extremely fast language server protocols (LSPs), Kennedy wrote.

“Notice anything similar? They are both written in Rust, backing up the previous claim that ‘Rust has become Python’s performance co-pilot,’” he added.

## The Business Case

Meanwhile, for enterprises, Rust-enhanced Python delivers tangible benefits. The performance improvements alone can translate into cost savings, including reduced cloud compute costs and lower memory usage. Moreover, faster response times improve customer satisfaction and more efficient code reduces energy consumption, Kennedy said.

## Advice for Python Developers

Kennedy advised Python developers to learn to read Rust.

Python developers should consider learning the basics of Rust, not to replace Python, but to complement it.

“As I discussed in our analysis, Rust is becoming increasingly important in the most significant portions of the Python ecosystem,” Kennedy wrote. “I definitely don’t recommend that you become a Rust developer instead of a Pythonista, but being able to read basic Rust so that you understand what the libraries you’re consuming are doing will be a good skill to have.”

Kennedy also advised Python developers to embrace Rust-enhanced libraries. When choosing between similar packages, consider those with Rust cores — they often provide superior performance without sacrificing Python’s ease of use, he said.

And Python devs also should consider Rust for extensions, Kennedy advises. Python developers building performance-critical Python extensions should evaluate Rust as their implementation language instead of defaulting to C, he indicated.

## The Future Is Hybrid

Overall, Rust is not replacing Python — it’s supercharging it. This hybrid approach gives developers the best of both worlds: Python’s expressiveness and ecosystem for application logic, with Rust’s performance for computationally intensive components, the report expresses.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)