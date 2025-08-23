If your company is running [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) applications on anything older than version 3.13, you’re likely burning money.

According to the [JetBrains](https://www.jetbrains.com/) [State of Python 2025](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) report, a staggering 83% of [Python developers](https://thenewstack.io/python-developers-hold-the-key-to-blockchain-adoption/) are running on versions that are a year old or older, with nearly half (48%) still on Python 3.11 and 27% on Python 3.10 or earlier.

But this is not just a [technical debt](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/) problem. It is a financial hemorrhage bleeding out organizations’ cloud bills.

## The Hidden Cost of ‘Good Enough’

The top reasons respondents gave for why they’re not using the latest version include: “The version I’m using meets all my needs” (53%) and “I haven’t had the time to update” (25%).

It’s the old “if it ain’t broke, don’t fix it” strategy, but what these developers don’t realize is that their “good enough” [Python versions](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) are costing their organizations massive amounts in unnecessary cloud compute expenses.

## The Performance Gap and Financial Impact

Python’s recent versions have not just added new features — they’ve delivered substantial performance improvements that translate directly to cost savings. Python 3.11 to 3.13 delivers approximately 11% faster execution with 10-15% less memory usage. The jump from Python 3.10 to 3.13 represents a whopping 42% speed increase with 20-30% less memory usage. These improvements represent fundamental efficiency gains.

According to the report, for mid-market companies with a median annual [AWS](https://aws.amazon.com/?utm_content=inline+mention) bill of approximately $2.3 million, where EC2 compute represents 50-70% of costs ($1.15-1.6 million), a Python 3.10 to 3.13 upgrade could deliver potential savings of $420,000 annually.

For large enterprises with annual AWS spending of $24-36 million and EC2 compute costs of $12-25 million, the potential savings from the same upgrade reach $5.6 million annually. These calculations assume a conservative 30% efficiency gain on compute-intensive workloads based on documented performance improvements, the report showed.

## The Containerization Paradox

“The survey also indicates that many of us are using Docker and containers to execute our code, which makes this 83% or higher number even more surprising,” [Michael Kennedy](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/#author), the founder of [Talk Python](https://talkpython.fm/) and a [Python Software Foundation](https://www.python.org/psf-landing/) Fellow, wrote in a [blog post](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) about the report. “With containers, just pick the latest version of Python in the container. Since everything is isolated, you don’t need to worry about its interactions with the rest of the system.”

Yet, the fact that containerization has not accelerated Python upgrades indicates that many dev teams are not aware of the financial implications.

## Beyond Direct Compute Costs

The financial impact extends beyond just compute efficiency. Teams spending time working around performance limitations instead of building features represent opportunity costs that don’t show up directly in cloud bills.

“The 83% of developers running on older versions of Python may be missing out on much more than they realize,” Kennedy wrote. “It’s not just that they are missing some language features. Python 3.11, 3.12, and 3.13 all include major performance benefits, and the upcoming [3.14](https://thenewstack.io/python-3-14-0-alpha-is-now-available-heres-whats-included/) will include even more.”

## The Upgrade Economics

Python version upgrades offer one of the highest ROI improvements available in software development, Kennedy said.

“What’s amazing is you get these benefits without changing your code,” he wrote. “You simply choose a newer runtime, and your code runs faster. CPython has been extremely good at backward compatibility. There’s rarely significant effort involved in upgrading.”

Unlike architectural changes or major refactoring projects, most applications require no code changes, have minimal migration risk, deliver immediate performance benefits upon deployment and provide compound savings that grow with scale, Kennedy noted.

## The Data Science Factor

The survey shows that data science now represents 51% of all Python usage, with [pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/) and [NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) being the most common tools.

Kennedy emphasizes the significance of this shift: “Many of us in the Python pundit space have talked about Python as being divided into thirds: One-third web development, one-third data science and pure science, and one-third as a catch-all bin,” he wrote. “We need to rethink that positioning now that one of those thirds is overwhelmingly the most significant portion of Python.”

This shift toward compute-intensive workloads makes performance improvements even more financially significant. Data science workflows involving large dataset processing, model training and inference, complex statistical computations and extended batch processing jobs all benefit from Python’s recent performance improvements, Kennedy indicated.

## The Bottom Line

In an era where organizations are looking to optimize costs and improve efficiency, Python version upgrades represent low-hanging fruit.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)