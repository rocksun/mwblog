If 2025 was “the year of type checking and language server protocols” for Python, will 2026 be the year of the type server protocol? “Transformative” developments like free threading were said to be coming to Python in 2026, along with performance-improving “lazy” imports for [Python](https://thenewstack.io/what-is-python/) modules. We’ll (hopefully) also be seeing improved Python agent frameworks.

But 2026 could even see a change in change itself — in the ways that Python changes are proposed.

Last month, there was an illuminating seven-person conversation — including three of Python’s core developers, two of whom are also members of [Python’s Steering Council](https://discuss.python.org/t/steering-council-election-results-2026-term/105296). As 2025 came to a close, these prominent guests came together for a [special year-in-review episode of the “Talk Python to Me” podcast](https://www.youtube.com/live/PfRCbeOrUd8?si=x5MVtWW6nu7kzGgY), discussing what trends they’d seen in 2025 — but also what they see coming in the year ahead for Python and its developer community.

## Tools That Run Python

From the beginning, the podcast showed that Python is still a broad-based global community. From Vancouver came [Brett Cannon](https://www.linkedin.com/in/drbrettcannon/), a Python core developer [since 2003](https://opensource.snarky.ca/About+Me/Frequently+Asked+Questions%20), and a Microsoft principal software engineer for over 10 years. And what Cannon saw in 2025 was advances in people running Python code using tools.

Where before you’d install the Python interpreter — and then also any needed dependencies — to then launch everything in a virtual environment, “Now we’ve got tools that will compress all that into a run command!” A growing set of tools like [Hatch](https://hatch.pypa.io/latest/), [BDM](https://www.scalefree.com/portfolio/development-of-the-business-data-modeler-using-python/) [and](https://python-poetry.org/) [uv](https://github.com/astral-sh/uv) [“build on each other and … just slowly build up this repertoire of tool approaches.”](https://python-poetry.org/)

This caught the attention of Python’s core developers. “These tools treat Python as an implementation detail, almost,” Cannon said. The Python interpreter just fades into the background as “a thing that they pull in to make your code run.”

Also on the call was [Barry Warsaw](https://www.linkedin.com/in/barry-warsaw/), who has been a Python core developer for more than 30 years. He told Cannon, “I think you’re really onto something.” Warsaw is also on the 2026 Python Steering Council (while currently working on Python at Nvidia), and sees this as an even larger trend — “a renewed focus on the user experience.”

Just installing the binary with the Python interpreter can be complicated for new users, but [2024](https://discuss.python.org/t/how-would-you-like-to-declare-runtime-dependencies-and-python-requirements-for-pep-723/40418/82) saw Python [adding a format for metadata to embed in Python scripts](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata) to help IDEs, launchers and other external tools. So in the world of 2025, it’s now that much easier to write code that will be run by Python. “You can put uv in the shebang line of your script — and now you don’t have to think about anything. And Hatch can work the same way for developers.”

This drew some enthusiastic agreement from Associate CS Professor [Gregory Kapfhammer](https://allegheny.edu/about/campus-department-resources/faculty-and-staff-directory/gregory-kapfhammer/). Dialing in from Pittsburgh (where he’s already using uv in his classes at Allegheny College), Kapfhammer said he’s amazed how much uv had simplified lessons for his students. “I don’t have to teach them about Docker containers, and I don’t have to tell them how to install Python with some package manager.”

And from Berlin came more agreement from [Jodie Burchell](https://www.linkedin.com/in/jodieburchell/), a 10-year data scientist (now a developer advocate at JetBrains, working on PyCharm). Burchell said they’re even discussing whether to use uv at the data science mentoring community [Humble Data](https://humbledata.org/) (where she’s one of the organizers). “It does abstract away all these details. The debate I have is, is it too magic?” And as a developer advocate at JetBrains, “It’s also a debate we have in PyCharm. How much do you magic away the fundamentals versus making people think a little bit?”

This led to a discussion about possible future developments in Python. Core developer Cannon said that for the troubleshooters — and even just for the curious — “I want the magic to decompose. You should be able to explain the ‘magic’ path via more decomposed steps using the tool all the way down to what the tools actually do behind the scenes.” And it’s not just a hypothetical for him. “I’ve been thinking about this a lot,” Cannon said, because “I’m thinking of trying to get the Python launcher to do a bit more.”

After all, uv is still made by a company (named [Astral](https://astral.sh/about)), and “There’s always the risk they might disappear.” And a lot of work has now been put in place to create standards for this kind of packaging, including that [metadata addition](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata).

## Lazy Imports and Free-Threaded Python

2026 will also bring performance-improving “lazy imports,” which will speed start-up times by deferring until first use the importing of modules. “It’s been accepted, and it’s going to be awesome,” said Core Developer [Thomas Wouters](https://github.com/yhg1s). Dialing in from Amsterdam, Wouters has also deployed Python internally at [Google](https://cloud.google.com/?utm_content=inline+mention), where he worked for 17 years before moving to Meta. He’s been a board member of the Python Software Foundation — even receiving their [Distinguished Service Award](https://pyfound.blogspot.com/2025/03/dsa-thomas-wouters.html) in 2025 — and is a [current member of 2026’s Python steering council](https://discuss.python.org/t/steering-council-election-results-2026-term/105296).

Wouters is even more excited about Python’s progress toward adding parallel processing capabilities. Thinking of how Python’s Global Interpreter Lock notoriously slowed down performance by enforcing single-thread processing, Wouters phrased this development indelicately as “the global interpreter lock is going away! I am stating it as a fact — it’s not actually a fact yet, but that’s because the Steering Council hasn’t realized the fact yet.”

Wouters said this because he was on the Steering Council that accepted an alternative — free-threading — as an experimental feature, and now for Python 3.14, “It is officially supported. The performance is great … It’s basically the same speed on MacOS … That’s a combination of the ARM hardware and *clang* specializing things … And then on recent GCCs on Linux, it’s like a couple percent slower.”

2026 will see a focus on community adoption, said Wouters, “getting third-party packages to update their extension modules for the new APIs” and “supporting free-threading in a good way.” But for Python code, “it turns out there’s very few changes that need to be made for things to work well under free-threading.”

And more to the point, “We’ve seen a lot of examples of really promising, very parallel problems that now speed up by 10x or more. And it’s going to be really exciting in the future.”

## Enhancing the Enhancement Proposals?

The biggest change may have been suggested by Barry Warsaw. As the creator of Python Enhancement Proposals — the procedure for changing the language — Warsaw brings real credibility when he said, “We have to rethink how we evolve Python — and how we propose changes to Python, and how we discuss those changes in the community.”

The current process is over a quarter of a century old, and while the developer community is “somewhat larger,” Warsaw said there’s been a more exponential growth in “the number of people who are using Python and who have an interest in it.” But more to the point, “One of the things that I’ve heard over and over and over again is that authoring Python Enhancement Proposals is incredibly difficult, and emotionally draining. It’s a time sink, and leading those discussions on discuss.Python.org … can be toxic at times, and very difficult.”

The end result? “It has become really difficult to evolve the language and the standard library and the interpreter … We need to think about how we can make this easier for people and not lose the voice of the user.”

When it comes to the Python community, comments left at discuss.python.org are “the tip of the iceberg,” Warsaw said. “We’ve got millions and millions of users out there in the world who, for example, lazy imports will *affect* — free threading will *affect*. And yet they don’t even know that they *have* a voice.” Warsaw hopes to represent them “in a much more collaborative and positive way.”

So in 2026, Warsaw said, “I think this is something I’m going to spend some time on, trying to think about — you know, and talk to people about — ways we can make this easier for everyone.”

Warsaw shared an interesting observation on where we are now. “There have been changes that have been made to Python that really should have been a PEP. And they aren’t because … core developers don’t want to go through this gauntlet!

“But that’s also not good because then, you know, we don’t have the right level of consideration.”

## When Types Meet Tools

Kapfhammer shared an important tip, pointing out that “If you can teach your AI agent to use the type checkers and use the LSPs, it will also generate better code for you.” It’s giving the large language model (LLM) one more useful piece of information and context — and the industry is starting to take notice. Kapfhammer said the team behind Meta’s type checker is working directly with [Pydantic AI](https://ai.pydantic.dev/) to create interoperability, “So that when you’re building an AI agent using Pydantic AI, you can also then have better guarantees when you’re using Pyrefly as your type checker.”

In fact, for Kapfhammer, 2025 was “the year of type checking and language server protocols.” He uses the static type checker [Mypy](https://mypy-lang.org/) and language server protocols like [Pyright](https://github.com/microsoft/pyright) or PyLance. But 2025 also brought Meta’s [Pyrefly](https://pyrefly.org/) type checker/LSP, Astral’s [ty](https://docs.astral.sh/ty/) and a new type checker/LSP called [Zuban](https://zubanls.com/blog/open-source/). He notes these 2025 tools were all implemented in Rust — and are “significantly faster,” which changes how he uses the tools, and how often. “It’s helped me to take things that might take tens of seconds or hundreds of seconds, and cut them down often to less than a second.”

Cannon noted that “It takes more work to write Rust code than it does to write Python code,” and applauded the tool makers for being willing to shoulder that extra effort to deliver “an overall win for the community.”

But Cannon also seemed to have some high hopes for what we’ll see in 2026. “Pylance is actually working with the Pyrefly team to [define a type server protocol](https://github.com/microsoft/pylance-release/discussions/7180) [TSP] so that a lot of these type servers can just kind of feed the type information to a higher-level LSP, and let that LSP handle the stuff like symbol renaming and all that stuff.”

The podcast was hosted by [Michael Kennedy](https://www.linkedin.com/in/mkennedy/), a Portland-based Python enthusiast and educator, who gave the 84-minute conversation — and the year ahead — a perfect summation.

“I still think it’s an incredibly exciting time to be a developer or a data scientist. There’s so much opportunity out there … Every day is slightly more amazing than the previous day … I love it.”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)