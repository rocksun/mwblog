Built by the team at Intuit that created [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/), [Numaflow](https://numaflow.numaproj.io/) is a Kubernetes-based open source stream processing engine with a UI that allows engineers to easily compose data processing pipelines. No experience in Kubernetes necessary.

Built for high-throughput workloads, Numaflow connects to [Kafka](https://thenewstack.io/apache-kafka-4-1-the-3-big-things-developers-need-to-know/), [Pulsar](https://thenewstack.io/need-to-scale-apache-kafka-switch-to-apache-pulsar/) and [SQS](https://thenewstack.io/testing-microservices-message-isolation-for-kafka-sqs-more/), and can analyze, filter or process the stream of data before sending it along to its destination. Easily scalable, it will work as fast as you need.

Last week, at the [Kubecrash 2025 virtual conference](https://www.kubecrash.io/), two Intuit team members on the project described how Numaflow could be used for running AI pipelines.

[![screenshot](https://cdn.thenewstack.io/media/2025/10/d83ad6d0-kubecrash-numaflow-01.png)](https://cdn.thenewstack.io/media/2025/10/d83ad6d0-kubecrash-numaflow-01.png)

## The Role of Stream Processing in AI

Think of stream processing as the backbone of AI.

Turns out there is a lot of event processing in AI: **feature engineering,** where features are calculated and added to the model; **inferencing,** where a trained model makes predictions; and, of course, **training,** where the models get the latest data.

A real-time stream processing platform is essential if “you want to understand or process events and then try to respond as they’re happening,” said [Sriharsha Yayi](https://www.linkedin.com/in/sriharshayayi/), Numaflow product manager for Intuit. For instance, user behavior could be tracked in real time to provide recommendations. Fraudulent activity can be thwarted while it is still going on.

Yet building data processing pipelines can be a thorny task, let alone making it scalable and real time.

## Common Challenges in Event Processing on Kubernetes

Numaflow set out to solve a number of challenges with event processing on Kubernetes, Yayi said.

For one, data engineers, who know procedural logic, weren’t super familiar with the Java and Scala platforms they had to design upon. Nor are there many other developers who also wanted to tie into a stream engine.

“We have observed where people wanted to have a stream processing capability or framework that is beyond Java,” Yayi said.

Also, setting up an entire data stream for some sort of processing involved writing a lot of boilerplate code, such as all the duplicated functionality needed across the multiple messaging queues.

“If I’m a developer or maybe an ML [machine learning] guy, why should I really spend a lot of time writing these integrations again and again whenever I write these new pipelines or consumers?” Yayi asked.

Lastly, scaling is a hurdle. In event processing, the need for scalability was measured by an event backlog, but had to be expressed — through the Kubernetes [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — through additional pods needed at that moment. Some users even hand-tuned the number of pods needed when traffic surged in.

[![Screenshot](https://cdn.thenewstack.io/media/2025/10/80598db5-kubecrash-numaflow-02.png)](https://cdn.thenewstack.io/media/2025/10/80598db5-kubecrash-numaflow-02.png)

## How Numaflow Solves Common Stream Processing Challenges

“Numaflow is a serverless platform for stream processing,” explained [Krithika Vijayakumar](https://www.linkedin.com/in/krithikavijayakumar/), Intuit senior software engineer. It was designed to hide (“abstract”) all the infrastructure bits away from the data engineers.

Numaflow allows ML engineers to “focus just on their stream processing or inferencing, and eliminate the need for them understanding the underlying infrastructure,” Vijayakumar said.

It also whisks away the need to learn all the event processing complexities behind such concepts, such as sinks and sources, abstracting them down to a single data object.

“We realize that ML engineers are focused largely on the payload, and they don’t really care about where they are reading the data from. ‘Is it Kafka? Or is it Pulsar? Or is it HTTP?'” Vijayakumar elaborated.

[![screenshot](https://cdn.thenewstack.io/media/2025/10/ab355faf-kubecrash-numaflow-04.png)](https://cdn.thenewstack.io/media/2025/10/ab355faf-kubecrash-numaflow-04.png)

So, details around the sinks and sources are hidden from the engineers, who can get back to worrying about their inferencing and processing logic. Users write their inference logic as *user-defined**functions* (UDFs).

Also, the platform automatically scales based on traffic coming in. No more spinning up pods manually!

## Building an AI Pipeline With Numaflow: A Demo

Vijayakumar ran a demo of a simple task of image recognition. Numaflow comes bundled with a UI, so you can see the pipelines as you build and run them:

[![screenshot](https://cdn.thenewstack.io/media/2025/10/84de75da-kubecrash-numaflow-06.png)](https://cdn.thenewstack.io/media/2025/10/84de75da-kubecrash-numaflow-06.png)

The data is pulled from the source and sent to a prediction vertex. A vertex is a core computational component, which in this case returns a written description of the contents of the image back to the sink, an HTTP endpoint. The vertex itself is run with a local Natural Language Processing model.

The pipelines themselves are defined in [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/), a declarative language.

She also showed a glimpse of a working anomaly-detection pipeline, one in production for a year. Pipelines can have multiple sources, sinks and UDFs. UDFs can be written in a mixture of Python or Java. In the GUI, Vertices can display the number of pods they are running. They work independently, so they can each scale according to their own incoming workload.

## A ‘Pretty Impressive’ Data Stack

“If you are a native Kubernetes shop, this is the way to go,” said data engineer [Dan Young](https://www.linkedin.com/in/dan-young-70b2496/) in his [walkthrough video of Numaflow](https://www.youtube.com/watch?v=zQ170JcbdCo&t=408s). He suggested that Numaflow, along with Argo, could be used to build a “pretty impressive data processing stack.”

If you want to learn more, the Numaflow engineers will also be presenting at upcoming [AllThingsOpen](https://www.eventbrite.com/e/all-things-open-2025-tickets-1092602165489?discount=TNS2025) and [KubeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)