# Netflix Open Sources Maestro, a Next-Gen Data Workflow Engine
![Featued image for: Netflix Open Sources Maestro, a Next-Gen Data Workflow Engine](https://cdn.thenewstack.io/media/2023/10/0439525e-netflix-1024x601.png)
Video and gaming streaming service Netflix has released as open source the workflow orchestrator that its army of data scientists and analysts use every day to understand user behaviors and other large-scale data-driven trends.

The [Maestro workflow orchestrator](https://github.com/Netflix/maestro), released under an [Apache 2.0 license](https://thenewstack.io/a-guide-to-leveraging-open-source-licensing/), was designed to support hundreds of thousands of workflows and has completed up to 2 million jobs in a single day for the media company.

## How Maestro Works
According to company engineers, it is highly scalable, extensible and able to meet strict service level objectives ([SLO](https://thenewstack.io/usenix-the-3-measures-of-successful-site-reliability-engineering/)) even during spikes of traffic.

It is built on top of a range of open source technologies, namely [Git](https://thenewstack.io/git-for-managing-small-projects/), [Java (21)](https://thenewstack.io/java-21-is-nigh-whither-javaone/), [Gradle](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/) and [Docker](https://www.docker.com/?utm_content=inline+mention).

Maestro can be evoked from [the cURL command line](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/), which provides the ability to create, run, and delete a workflow and an associated batch of data. The workflow is defined in [JSON](https://thenewstack.io/an-introduction-to-json/), and the user’s business logic can be packaged into Docker images, [Jupyter notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/), bash scripts, [SQL](https://thenewstack.io/using-window-functions-in-sql/), [Python](https://thenewstack.io/what-is-python/), and other formats.

Behind the scenes, Maestro manages the entire lifecycle of a workflow, handling retries, queuing, and task distribution to compute engines. Not only does it support [Directed Acyclic Graphs](https://thenewstack.io/airflow-a-workflow-orchestrator-for-big-data/) (DAGs) — table stakes in the AI-driven world of 2024 — but also cyclic workflows and multiple reusable patterns, through for each loop, sub workflows, and conditional branching.

“It supports a wide range of workflow use cases, including ETL pipelines, ML workflows, AB test pipelines, pipelines to move data between different storages,” a group of Netflix engineers [collectively wrote](https://netflixtechblog.com/orchestrating-data-ml-workflows-at-scale-with-netflix-maestro-aaa2b41b800c) in a recent blog post announcing the release. “Maestro’s horizontal scalability ensures it can manage both a large number of workflows and a large number of jobs within a single workflow.”

## Birth of Maestro
Netflix is no stranger to open source software, [having released](https://netflix.github.io/) many tools it developed internally as open source. System stress-testing tool [Chaos Monkey](https://github.com/Netflix/chaosmonkey) was released in 2011, and inspired a whole generation of [chaos testing tools](https://thenewstack.io/gremlin-applies-chaos-testing-to-serverless/). Other open source projects that Netflix has spun off include the routing gateway [Zuul](https://github.com/Netflix/zuul) and the [microservices](https://thenewstack.io/microservices/) routing engine [Conductor](https://github.com/Netflix/conductor), since deprecated.

Netflix first let the world know about Maestro in 2022 in a [blog post](https://netflixtechblog.com/orchestrating-data-ml-workflows-at-scale-with-netflix-maestro-aaa2b41b800c) that explained its origins. The orchestrator then being used, called Meson, was straining under the workloads of thousands of daily jobs, particularly around peak usage time.

“Meson was based on a single leader architecture with high availability. As the usage increased, we had to vertically scale the system to keep up and were approaching AWS instance type limits,” the engineers wrote in the 2022 post.

Worse, the workloads were expected to increase by at least 100% per year, and the sizes of the workflows were expected to grow as well.

From the start, Maestro was designed to be highly-scale and extensible. It was built on a DAG architecture, where each workflow was comprised of a series of steps. And each step can have dependencies, triggers and other conditionals. The business logic of each workflow is run in isolation, guaranteeing SLOs are met. All the services are designed to be stateless so they can be scaled out as needed.

At [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)‘ 2023 Re:Invent conference, the Netflix engineering team delved further into detailing Maestro:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)