Python is ubiquitous. Millions of professionals, from scientists to software developers, rely on it. Organizations like [Google](https://cloud.google.com/?utm_content=inline+mention) and Meta have built critical infrastructure using it. Python even helped NASA explore [Mars](https://thenewstack.io/python-in-unexpected-places/), thanks to its image processing abilities.

And its growth isn’t slowing anytime soon.

In 2024, Python [surpassed](https://github.blog/news-insights/octoverse/octoverse-2024/) JavaScript as the most popular language on GitHub, and today, it has become the backbone of modern AI systems. Python’s versatility and passionate community have made it what it is today. However, as more enterprises rely on Python for everything from web services to AI models, there are unique needs that enterprises must address around visibility, performance, governance and security to ensure business continuity, fast time to market and true differentiation.

## **How Python Became the Universal AI Language**

Most popular languages have benefited from corporate sponsorship. [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) supports Java. Microsoft backs C#. And Apple champions Swift. But Python has almost always been a [community project](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/), supported by several companies, and has been developed and improved over decades by a committed group of mainly volunteers, directed by [Guido van Rossum](https://www.linkedin.com/in/guido-van-rossum-4a0756/) as Benevolent Dictator for Life until 2018.

In the 1980s, van Rossum sought to create a language that was both simple and beautiful. Since the early ’90s, as an open source project, Python was available for anyone to inspect, modify or improve.

[![](https://cdn.thenewstack.io/media/2025/11/a3cbfa5c-picture1.png)](https://cdn.thenewstack.io/media/2025/11/a3cbfa5c-picture1.png)

The Zen of Python, by Tim Peters, image originally posted by Pycon India on X.

Python quickly differentiated itself from its peers. It was easy to learn, write and understand. Developers could easily tell what was happening in their and others’ code just by looking at it, an anomaly in the days of Perl, C++ and complex shell scripts. This low barrier to entry made it highly approachable to [new users](https://thenewstack.io/why-beginning-developers-love-python/).

Then there was Python’s extensibility, meaning it could easily integrate with other languages and systems. With the rise of the internet in the early 2000s, this extensibility took Python from a scripting solution to a production language for web servers, services and applications.

In the 2010s, Python became the de facto language for numerical computing and data science. Today, the world’s leading AI and machine learning (ML) packages, such as PyTorch, TensorFlow, scikit-learn, SciPy, Pandas and more, are Python-based. Still, the high-performance data and AI algorithms they use rely on highly optimized code written in compiled languages like C or C++. It is Python’s ability to easily integrate with these and other languages that has been critical in its ability to provide the best of both worlds: an easy interface to these packages for the millions of users who want to use them, but flexible interfaces for the experts that can optimize them in the language of their choice. These factors have made Python indispensable for both data science and AI workflows.

Today, if you’re working with any kind of AI or ML application, you’re likely using Python. However, as Python has become both the glue and the engine powering modern AI systems, enterprises need to be aware of critical needs specific to corporations around compliance, security and performance, and the community must strive to address them.

## **Helping Python Meet Enterprise Needs**

Longtime Python core contributor [Brett Cannon](https://www.linkedin.com/in/drbrettcannon/) famously said, “I came for the language, but I stayed for the community.”

The community has made Python the incredible language it is today, serving users above all else. However, the community’s mission has always been to build a language that works for everyone, from programmers to scientists to data engineers. This has proven to be the right approach. This also means Python wasn’t engineered for the specific needs of enterprises running their business with Python.

And that’s OK, as long as those needs are addressed.

[Anaconda’s “2025 State of Data Science and AI Report”](https://www.anaconda.com/resources/report/8th-annual-state-of-data-science?utm_source=InsightMedia&utm_medium=organicsearch&utm_campaign=sods-2025-insight-media-tns) found that enterprises face many of the same recurring challenges as they move data and AI applications to production. Over 57% reported that it takes more than a month to move AI projects from development to production. To demonstrate ROI, respondents were mostly interested in business concerns, such as:

* Productivity Improvements (58%)
* Cost Savings (48%)
* Revenue Impact (46%)
* Customer Experience / Loyalty (45%)

Think about it like cloud computing fifteen years ago. Organizations could immediately see the massive cost and operational advantages of moving workloads to the cloud. However, they realized that the security, compliance and cost model had changed entirely. They needed to continuously monitor, govern and optimize this new tool in altogether new ways. Python has reached that same point for enterprises.

I’ve spoken with dozens of leaders at organizations using Python, and here are the common challenges and themes I see.

### **Security**

While 82% of organizations [validate](https://www.anaconda.com/resources/report/bridging-the-ai-model-governance-gap) open source Python packages for security, nearly 40% of respondents still frequently encounter security vulnerabilities in their projects. These security issues create deployment delays for over two-thirds of organizations.

One of the strengths of Python, and all open source software, is that they’re free to download and use. You get the latest and greatest technology, and you can experiment, develop and push applications to production without paying a dime on the software.

However, history has shown that this openness and collaborative community can be abused by bad actors or even allow simple mistakes to proliferate, leading to the spread of vulnerable and malicious software. A piece of software or a package that looks fine could actually be dangerous. That problem is now compounding, with AI systems now generating and executing Python code without a human in the loop. Enterprises must protect their people, systems and data, and in turn, ensure safe AI deployment without missing deadlines.

### **Performance Optimization**

Though Python is straightforward to use, it can also *be* prolonged, which is fine for many use cases. But as we saw in the “State of Data Science and AI Report,” the modern enterprise’s primary concern is to do more with less — continually improve and increase efficiency, productivity improvements, cost savings, increase revenue, etc. The economics of producing AI applications is only exacerbating performance and efficiency concerns.

With limited time, expertise or tools, most enterprises struggle to fine-tune the Python runtime, leading to far more compute than needed and higher costs, or to running AI systems that aren’t performant enough to provide a usable experience.

### **Auditability**

Every CIO and CISO I know is staring down a wave of regulations, from the EU AI Act to internal SOC 2 and ISO 27001 compliance audits. Enterprises must be able to prove what code is running, where it’s running and how it’s interacting with sensitive data and systems.

Free and open source software makes that challenging because when anyone can download and run software freely, everyone will. New Python applications are popping up outside of IT control, packages are constantly updating, unknown or new dependencies are pulled in and there’s limited runtime visibility. Especially for organizations in highly regulated industries, this lack of runtime visibility creates present and future risk.

### **Managing Deployments**

According to a recent [survey](https://www.anaconda.com/resources/report/bridging-the-ai-model-governance-gap) of Anaconda’s users, over 80% of practitioners spend more than 10% of their AI development time troubleshooting dependency conflicts or security issues. Over 40% spend greater than a quarter of their time on these tasks, and time is money.

Once applications are in production, continuous maintenance, upgrades and security hardening can compound those issues. For an individual running and maintaining a small number of scripts and applications, this is not so hard. Still, for a large enterprise managing thousands of production applications, this becomes a considerable challenge.

Enterprises need a way to easily adopt new versions of Python and new technologies, while also minimizing [version sprawl](https://thenewstack.io/outdated-python-versions-cost-companies-millions/), security exposure and management overhead.

## **How To Help Enterprise AI Meet the Needs of Modern Enterprises**

The good news is you can start addressing many of these challenges today. It all comes down to being intentional about your governance strategy.

[More than half of organizations today](https://www.anaconda.com/resources/report/8th-annual-state-of-data-science?utm_source=InsightMedia&utm_medium=organicsearch&utm_campaign=sods-2025-insight-media-tns) have no or very limited open source and AI governance policies or frameworks in place. Creating an official policy around governance and investing in visibility and auditability already puts you ahead of most enterprises.

When building your governance strategy, start by building internal processes that track Python usage across teams and systems. Ensure you know what packages are running, where, and under what configurations.

Next, you’ll want to ensure you’re managing Shadow IT/AI and reviewing any and all AI-generated code. Agentic tools can’t replace a solid software development life cycle (SDLC) process. Ensure you have the right visibility, standards and processes in place to prevent unverified scripts from entering production.

It’s also critical to invest in workforce upskilling, increasing AI literacy among your employees so they better understand the risks of open source and AI solutions and why governance is so important. Some of the best education is in using these tools directly and gaining experience.

Finally, give your teams safe, reliable solutions across AI and data science workflows so that doing the right thing becomes the path of least resistance.

## **Make Python Your Competitive Edge**

Python’s openness is its greatest strength and its most significant challenge. While it’s democratized AI development, it’s also created new risk vectors and blind spots that enterprises must address. IT teams need the same visibility and governance for open source solutions as they would for any other part of their tech stack. Time has shown that this is a primary source of innovation in the enterprise, so the investment in securing that innovation is worth it. And while specific upgrades to the language itself can help, intentional governance can make a difference today.

At Anaconda, we’ve seen enterprises tackle these challenges by building strong SDLC, governance, and observability layers around their Python environments. It adds a little more work upfront, but it’s a critical shift that will protect your organization in the long run and ensure the success and longevity of your AI initiatives.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/08/2beda629-cropped-151f2f81-screenshot-2025-08-21-at-8.19.33%E2%80%AFam.png)

Steve Croce is the Field Chief Technology Officer at Anaconda, where he bridges technical innovation with customer success for the world's leading Python platform for AI and data science. With over 20 years in the tech industry, he combines deep...

Read more from Steve Croce](https://thenewstack.io/author/steve-croce/)