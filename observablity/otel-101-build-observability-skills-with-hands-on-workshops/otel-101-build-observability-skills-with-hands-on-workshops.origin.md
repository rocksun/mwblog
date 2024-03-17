# OTel 101: Build Observability Skills with Hands-on Workshops
![Featued image for: OTel 101: Build Observability Skills with Hands-on Workshops](https://cdn.thenewstack.io/media/2024/03/054b79f6-hands-on-observability-opentelemetry-1024x576.jpg)
We are in the middle of a tectonic shift toward an open, extensible and observable world. With every pull request, the dream of “instrument once, observe anywhere” is closer than ever. Distributed traces in particular are uniquely positioned to help developers navigate and understand the complexities of the cloud native services they’re building and operating: There is incredible value in being able to trace a transaction across a distributed microservices environment.
Yet, many tracing initiatives have faltered in the decade or so since distributed tracing’s introduction, and it maintains a reputation as a tool for a superset of engineers.
[Tracing ](https://chronosphere.io/learn/now-generally-available-tracing-reimagined-with-chronospheres-observability-platform/)itself is not the problem, in my opinion. The early wave of tools was complex, so tracing’s usefulness has centered on a [small number of power users](https://chronosphere.io/learn/distributed-tracing-is-failing-how-can-we-save-it/).
However, tracing initiatives led and executed by a single site reliability engineering (SRE) team will fail to thrive. For teams to realize the full potential of trace data, every developer must be able to use tracing tools. This means learning everything from how to emit the data in the first place to making use of that data.
## The Value of Hands-on Workshops
I’ve tried many tactics to help developers build up skills with analyzing and leveraging traces to better understand system behavior and inform decisions. The most successful programs are hands-on workshops, like the one on
[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/) (OTel) and tracing I held at [KubeCon North America 2023](https://thenewstack.io/kubecon-2023-managing-pets-cattle-and-starfish/) in Chicago. My course, [OpenTelemetry 101: Let’s Instrument!](https://o11y-workshops.gitlab.io/workshop-opentelemetry/), was designed for developers to take their first steps with tracing.
I’m eager to help as many developers as possible get started on their tracing journey, so this article shares the behind-the-scenes of developing the workshop, including:
- How I designed the learning environment.
- The complexity around establishing a shared understanding of observability concepts.
- How to create and send spans with OpenTelemetry.
- Practicing skills for interpreting and analyzing trace data.
## Creating the Learning Environment
The workshop is designed for tracing novices, and I wanted attendees to leave with the knowledge and skills necessary to bring tracing to their own projects. Enabling this level of independence meant I had a few short hours to cover basic observability concepts; provide an overview of OpenTelemetry and its various subprojects; offer plenty of opportunities for attendees to develop their instrumentation muscles and think through where, when and how to add spans; and help them verify the resulting data until they were satisfied with the level of detail in traces.
Introducing all of that at once would overwhelm even the most seasoned developer, so I broke it down into three main sections:
- Observability concepts
- Sending trace data
- Using trace data
## Observability Concepts: Learning the Jargon
Many people learn observability informally on the job. This can lead to misconceptions such as confusing vendor-specific product names with observability concepts. This is why I start every observability training session with a quick level-set on terminology and concepts. Even a one-sentence definition can clear things up:
After defining key terms, I move to an overview of
[OpenTelemetry (OTel)](https://www.cncf.io/blog/2021/08/06/what-is-opentelemetry-and-why-is-it-the-future-of-instrumentation/), covering the components, the protocol and the community at a high level. It was tempting to include details about its history, development and every component, but I didn’t. Instead, I turned to the learning goal for guidance. Is it really necessary for developers to know all about the [Collector](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/) to be able to confidently instrument traces with OpenTelemetry? No. So I included a slide on the Collector that briefly explains its role in the ecosystem. This gave folks a passing familiarity with the Collector as they continue on their learning journey.
At this point, participants have enough of a foundation to kick off the actual topic that drew them in: instrumenting traces.
## Sending Trace Data
This workshop was designed with a conference audience in mind, so I covered all three approaches to instrumentation: automatic, programmatic and manual.
It is important to give people a quick win early in a learning experience to build confidence and keep them engaged, so I started with auto-instrumentation. To keep things simple, I taught how to configure the console_exporter for traces and explore the textual representation of spans. In my experience, this hands-on approach has proven more effective than throwing up a slide with the same span and lecturing on each part of it. For every skill or piece of knowledge I want to impart, it is important to find a hands-on way for attendees to learn by doing — not by listening to me lecture.
Moving to programmatic and manual approaches provided more chances to practice and strengthen learners’ instrumentation skills. They repeated the same workflow — planning where to instrument, adding instrumentation code, running the program to generate traces and then verifying the trace data was repeated — over and over.
The real value in tracing comes from all the ways you put it to use. It leads to a better understanding of what’s happening in your system and prepares you for the next topic.
## Using Trace Data
Being able to instrument and send traces is the first step, but the pinnacle of the workshop is learning how to query, visualize, interpret and analyze trace data. This opens the door to a final new component,
[Jaeger](https://www.jaegertracing.io/).
Jaeger, like OpenTelemetry, has a long and rich history that is not directly relevant to meeting the learning goal. I therefore focused on how to interact with trace waterfalls, topology diagrams and interpreting the trace scatter plot, rather than the details of operating Jaeger and using it in production.
## Create Your Own OTel Workshop
I hope my sharing the thought process behind my choices in developing this OTel 101 workshop has inspired you to conduct one of your own. My workshop was designed for a broad audience of open source developers (think
[KubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)), so I had certain constraints to work within. Designing a workshop for colleagues at your company will allow everyone to benefit from the shared context about your business and tech stack. Here are my generalized takeaways.
- Set a clear, scoped, measurable learning goal. This serves as a guide to evaluate whether the details you want to include are things your audience needs to know or would be information overload.
- Ground learning in real-world use cases.
- Host an “instrument-a-thon” where developers bring their own service to add tracing.
- Find out what your learners don’t understand.
- Review commonly asked observability questions across your team’s knowledge base and ticketing system.
- Send a survey asking about their prior observability knowledge, what they want to know about tracing, what roadblocks they run into, etc.
- Walk a novice through your workshop and note the places of friction and confusion and then incorporate their feedback.
- Don’t reinvent the wheel. Build upon existing tutorials from open source projects and, if applicable, vendor-provided ones. For maximum efficacy, adapt these resources instead of using them as is. This helps whittle down the material to the features or products in a platform that are relevant to your audience.
- Deliver the information in multiple modalities, especially when working with distributed remote teams. For example, you can offer both live guided sessions and self-guided sessions.
When it comes to cloud native observability, every developer deserves to be able to explore their services with distributed tracing. If you are embarking on a new initiative to introduce tracing or rebooting a stalled tracing effort, consider how a well-crafted training can help.
*To learn more about Kubernetes and the cloud native ecosystem, join us at KubeCon + CloudNativeCon Europe in Paris, from March 19-22.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)