It’s prediction season. Nowadays that means reading a lot of fanfic about how AI will replace your entire org chart by Q3 and, even more, why you’ll fail because you haven’t completely upended your organization. No AI ROI? That’s [your fault for not changing the soul of your enterprise culture](https://cote.io/2025/11/16/our-tech-is-fine-roi.html).

Annual predictions tell you more about what the author hopes will happen than what actually will. There’s nothing wrong with that. It’s just better to spray off the prediction fiction.

So, here’s what I hope happens in 2026 with enterprise AI: Executives mandate that new AI development starts in their organizations’ dominant programming language, which is likely [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/).

## Go Where Your Developers Are

If you want to start using AI to run your organization better, you don’t need to hire thousands of [Python devs](https://thenewstack.io/my-ai-python-coding-test-surprising-results/). You need to give the thousands of Java devs you already have the tools they need.

There’s a misconception that to “do AI,” you need to hire a legion of Python developers to rewrite your business — maybe some [TypeScript](https://thenewstack.io/typescript-vs-javascript/) developers if you’re that type. While the AI community is held together by Python and TypeScript at the moment, that’s not what’s holding up enterprises. Java is what runs enterprises.

If Java ceased to exist tomorrow, civilization would crawl to a halt. Your banking, your logistics, your health care systems all run on Java. For as long as most can remember — me, at least — Java has been the top or in the top three programming languages. I have no idea how to estimate it, but there are countless enterprise applications written and running in Java. It’s got to be the heart and soul of the enterprise apps universe. That’s what I hear consistently when I talk with large organizations. You can see that in [the RedMonk programming index](https://redmonk.com/rstephens/2025/06/18/top20-jan2025/), and it shows up in [other analyst surveys](https://my.idc.com/getdoc.jsp?containerId=US52257024) as well.

And when it comes to Java, I get the sense that the [Spring Framework](https://thenewstack.io/spring-ai-transforms-java-for-genai-app-delivery/) is the No. 1 Java framework. Just ask around “What’s in our app stack?” and you’ll probably hear the two Javas: Java and JavaScript. After that you’ll likely hear Spring. So, when you look out at all those enterprise applications, what you’re looking at is Java and Spring for as far as the software bill of materials (SBOM) can see.

Why does this matter? Because we already have the understanding, applications and data architectures needed to run enterprises.

“We have invested a lot in domain models, some of which are even very good,” [Rod Johnson](https://www.linkedin.com/in/johnsonroda/), founder of the Spring Framework and now CEO of Embabel, [said in a recent talk on using Java for AI](https://www.youtube.com/watch?v=yMDw0nlWd7s&t=1376s), “and to be able to leverage that as we move to the new world is really, really important.”

We don’t need to rebuild this lattice from scratch in a new language, and we don’t need to reskill or hire new people for that. Throwing away all of that time and effort would be absurd and irresponsible. You’d not only lose all of that domain knowledge and hard-won and well-paid-for code, but you’d lose something else, too.

Starting over again with your code means you also have to start over again with how you manage applications in production, how you diagnose and solve problems, and how you make sure the apps keep running. We’ve had decades of that with Java. People learned how to run Java applications in production, one gut-wrenching production failure at a time, over the years. [We’ve codified these lessons into the platforms that run Java](https://thenewstack.io/how-spring-and-java-shaped-internal-developer-platforms/).

When you change the programming language, you need to change your programmers’ skills. You also need to change your operational skills, your security skills, compliance skills and so on. And just as you’ve finished that 12-month-long modernization process, it’s time to jump back on the gut-wrenching Day 2 ride again. Yippie!

If your organization is running on Java apps, your AI strategy needs to start with Java. You’ll risk too much change and time catching up otherwise.

## How To Get to Where the Developers Are

If working with what and who you have — Java apps written by Java developers — is the goal, how do you get there?

First, think about your AI stack as an integrated platform. It’s not just handing developers a “blinking cursor” from Kubernetes — an empty command line with no services or guardrails — nor is it just a raw endpoint for hosting models. Instead, an AI platform looks like what you see with a [pre-engineered, AI-ready Platform as a Service (PaaS)](https://news.broadcom.com/releases/vmware-explore-2025-tanzu). In the case of Java and Spring, this means tight integration between the Spring Framework and the platform that offers secure, self-service access to developer services like databases, message brokering, large language models (LLMs), Model Context Protocol (MCP) servers and AI inference, to name a few.

As mentioned above, you also need to pay to run those applications, secure them, get compliance approval and set cost controls. A good application platform does more than pay attention to developer experience (DX); it also pays attention to operator experience (OX).

One way of considering this is operator-to-developer ratios. This means the more apps and developers one operations staff person can handle, the more automation and reliability are required by the platform. Let’s hope for more situations where just [a handful of platform engineers support thousands of developers and applications](https://www.youtube.com/watch?v=OHM3EG4IiV0&t=475s).

Second is making sure you can get access to new tools. One of the reasons new programming languages are so attractive is that you’re not trapped in the shackles of success. Organizations often fear updating their Java stacks because they’re leery of what could go wrong. Or, worse, they don’t think they have the time to spend on “non-customer-facing” tasks, like updating the libraries and runtimes used on those apps.

If you haven’t figured out how to keep your app stacks up to date in recent years, you’re probably [stewing in the legacy trap](https://cote.io/legacytrap/). Your executives complain that IT spends too much time on maintenance rather than adding new features, which is exactly what executives are looking for right now. With AI, you want to start putting new features into your apps. Even more so, you want to experiment and try new things, like we all did in the digital transformation years. This means getting access to new frameworks like Spring AI. And not just once, but continuously.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

For example, MCP is now a de facto standard for adding new capabilities and access to AI applications. It came out in November 2024, only a year ago now. For enterprises, this is “just yesterday.” The Spring team quickly integrated MCP into the Spring Framework. In fact, [the Spring team provides the official Java implementation for MCP](https://spring.io/blog/2025/02/14/mcp-java-sdk-released-2), which launched just a few months after MCP. However, you need to run the newer versions of the Spring Framework to get this.

This is the case for any AI programming you do, not just with Java. It just seems easier with languages that are new to your organization because you don’t have those shackles of success. You’re using the new features right now because you just started using the language. And because there are no (to very few) existing applications written in that language, you can’t get stuck in the legacy trap.

## The Easiest Path With the Best Chance of Success

The choice of where and how to start your AI journey is a business decision, not a technology one. By grounding your AI efforts in the operational muscle you’ve already built with Java and Spring, you minimize friction and risk. Everyone just keeps doing what they’re doing, but with a new tool. This established operational and development life is the hard-won experience, paid for in decades of maintenance and gut-wrenching production failures, that gives you the platform to continuously absorb new capabilities like Spring AI and MCP.

Get the developer experience and the operator experience right, and you unlock the organizational velocity needed to turn tentative AI experiments into a mission-critical competitive advantage.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Michael Coté studies how large organizations get better at building software to run better and grow their business. His books "Changing Mindsets," "Monolithic Transformation" and "The Business Bottleneck" cover these topics. He’s been an industry analyst at RedMonk and 451...

Read more from Michael Coté](https://thenewstack.io/author/cote/)