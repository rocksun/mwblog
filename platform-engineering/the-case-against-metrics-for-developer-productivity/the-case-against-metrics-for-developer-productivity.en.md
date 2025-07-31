Dashboards, metrics frameworks, acronyms, scorecards, tools — in the rush to quantify and optimize every aspect of software development, our industry forgot that metrics were [never supposed to measure productivity](https://www.aviator.co/blog/the-anti-developer-productivity-metrics/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-6-antimetrics&utm_term=net-new&utm_content=awareness) at all**.**[DORA metrics](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) are not about individual performance or a tool for comparing teams. The website for DORA — Google’s DevOps Research and Assessment team — still reminds us that these four metrics — deployment frequency, lead time for changes, mean time to restore and change failure rate — are not productivity metrics. They are delivery metrics that help engineering organizations “get better at getting better.”

But in a post-COVID world of remote work and asynchronous teams, we saw a rise in manager insecurity about what and how their teams were doing, so the “[developer productivity metrics](https://thenewstack.io/the-anti-metrics-era-of-developer-productivity/) industrial complex” was born. Dozens of additional metrics were added, new tools emerged and dashboards tracking 30 or 40 metrics were created. In a constant effort to build better metrics so that developers can be more productive, [we lost the point](https://thenewstack.io/despite-the-hype-engineers-not-impressed-with-dora-metrics/) of them being a feedback loop.

## **‘Measuring Developer Productivity Is a Fool’s Errand’**

[Martin Fowler](https://martinfowler.com/), the architect of modern software development, was right. We can’t measure developer productivity. The definition of productivity is how much output is generated for a given amount of input. How would we even try to figure out the productivity of an individual?

But we can measure proxies for team effectiveness and process health. What we actually want to find out are answers to two questions:

* Are we as an organization able to ship frequently and effectively so we can support the business?
* Is life for an individual developer in this organization good?

The questions are deceptively simple, but it is very difficult to answer them. And when trust is low in an organization, managers tend to lean on data. They feel like they have to back up their team’s performance, hiring or budget with numbers, and that’s how we end up with DORA metrics interpreted as productivity metrics or, even worse, the productivity of an individual developer being measured by the lines of code written.

Senior engineers often write less code, not more. They spend time mentoring, scoping projects, unblocking teammates and improving architecture. These are high-leverage activities, but they don’t show up on a metrics dashboard. [Bill Gates](https://thenewstack.io/bill-gates-paul-allen-and-the-code-that-started-microsoft/) once said that measuring software by lines of code is like measuring an airplane by weight.

## **Why Measure at All?**

There are two reasons: value or risk. Either we believe a change will help us deliver more value (faster, better, cheaper), or we believe there’s a risk (technical debt, instability, infrastructure cost) that must be addressed.

To address it, we have to identify it, and the best way to do this is not to stare at a dashboard, but to do a value-stream mapping, trace the journey from idea to production to value created. Where are the delays? Where is the waste? Where do things fall over? Then choose metrics, not to measure people, but to improve the system.

Ultimately, everything we do in developer experience or productivity must relate to business outcomes. That’s why metrics are important — as a feedback mechanism. We should connect metrics to value, measure them and always check whether improving a metric yields the expected value.

## **Designing Metrics That Matter**

If we were tasked with designing delivery or productivity metrics from scratch at an engineering organization, here’s how we’d approach it:

### **Step 1: Gather Requirements**

Don’t dive in and measure just to measure. Every engineering work starts with gathering requirements. What is being asked and why? You’ll often hear problems like [slow deployments](https://www.aviator.co/releases?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-6-releases&utm_term=net-new&utm_content=awareness), [long review cycles](https://www.aviator.co/flexreview?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-6-flexreview&utm_term=net-new&utm_content=awareness), [flaky tests](https://docs.aviator.co/mergequeue/concepts/managing-flaky-tests-in-mergequeue?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-6-docs-flakytests&utm_term=net-new&utm_content=awareness) or frequent incidents. Looking at DORA metrics is often a solid first answer, but you should still ask the questions first.

### **Step 2: Talk to Frontline Stakeholders**

Metrics don’t live in a vacuum. Talk to your frontline stakeholders, usually the product team. Ask them: What is the engineering org not doing well enough for you?

### **Step 3: Talk to Management**

Your next conversation is with management. Explain what you plan to do about the issues the product has raised. Management buy-in and support are essential; to achieve your goals, you may need a budget for infrastructure or hiring.

### **Step 4: Talk to Engineering**

This step is often skipped precisely because metrics are not viewed as feedback mechanisms for teams to improve. Talk to engineering and ask them how they would tackle the problem. Don’t walk in with a top-down directive: “Here are your new productivity targets.”

### Step 5: Pair Metrics with Guardrails

We all know [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law): “When a measure becomes a target, it ceases to be a good measure”. If you try and improve only one metric, people will sooner or later figure out how to game that number.

Let’s say you identified that there’s a code quality issue you’d want to improve. Increasing test coverage seems like the first metric that comes to mind, but you also have to be mindful of  
build time and build failures. Now you have the target metric you want to improve and two numbers that act as guardrails. Again, DORA is a set of four metrics, not a single metric, and it’s almost impossible for an individual engineer to move any of them.

### Step 6: Drop or Deprioritize Outdated Metrics

Again, metrics are a feedback mechanism. Once you’ve achieved the desired test coverage improvement, you can shift that metric in the background and just monitor if it falls below a certain level. Don’t fall for the metrics overload. If you actively track 40 metrics, how would you know what’s important?

Keep in mind that metrics will not measure productivity and will not [solve your engineering organization’s problems](https://thenewstack.io/the-anti-metrics-era-of-developer-productivity/); they will just help you identify them.

At [Aviator](https://www.aviator.co/?utm_content=inline+mention), we’re building tools [inspired by Google’s Engineering Productivity](https://www.aviator.co/blog/rebuilding-googles-engineering-productivity-engprod/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-6-rebuilding-google-engprod&utm_term=net-new&utm_content=awareness) initiative on the modern engineering stack to solve collaboration challenges at every stage of the development process, from code reviews to builds, testing, merging and deployment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, an AI-powered, low-config developer portal that automates ownership, code reviews, merges and deploys. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on developer experience,...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)

[![](https://cdn.thenewstack.io/media/2024/11/5060ac45-cropped-2291b1ce-adam-berry-amplitude-profile-photo.jpeg)

Adam Berry has worked on developer tools and infrastructure throughout his career, from Eclipse plugins to service and infrastructure work; he now focuses on developer platforms as products to empower engineers and make teams and organizations drastically more effective.

Read more from Adam Berry](https://thenewstack.io/author/adam-berry/)