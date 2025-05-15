# Apache Airflow 3.0: From Data Pipelines to AI Inference
![Featued image for: Apache Airflow 3.0: From Data Pipelines to AI Inference](https://cdn.thenewstack.io/media/2025/04/95ab7678-apache_airflow-1024x768.png)
Approximately 10 years ago, [Apache Airflow](https://github.com/apache/airflow/) launched with a relatively simple, yet timeless premise. It was initially devised as a means to allow developers and data engineers to write data pipelines as code.

With the recent release of the 3.0 version of the solution, the increasingly popular open source workflow management resource now offers a host of new features to support enterprise-scale applications.

There are version controls for data pipelines — termed [Directed Acyclic Graphs](https://www.geeksforgeeks.org/introduction-to-directed-acyclic-graph/) (DAGs) — enhanced security features, and constructs underpinning AI inference execution.

Driven by an ever-active open source community, the platform’s new developments are significantly enlarging the array of use cases it supports.

Although still a mainstay of data integration and data orchestration efforts, it’s now expanding into deployments of data science and machine learning.

According to [Vikram Koka](https://www.linkedin.com/in/vikramkoka), Chief Strategy Officer at [Astronomer](https://www.astronomer.io/) and [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) Committer, “As Airflow adoption has grown, now we see 30% of our users using Airflow for MLOps. We’re seeing 10% of our users using it for generative AI applications.”

The 3.0 release has several capabilities that support each of these developments, while reinforcing its capital value proposition of servicing data-driven workflows via Python-based code.

## DAG Version Controls
One of the most horizontally applicable features of the 3.0 edition of [Airflow](https://airflow.apache.org/) is the versioning it provides for data pipelines or DAGs.

Prior to the release, the system functioned as though users solely cared about the most recent version of the code for these tasks.

The new version of the platform lets developers see previous incarnations of DAGs, as well as a multitude of other relevant concerns, including “all the operation elements,” Koka said. “Logs, diagnostics, metrics… everything about that, you can actually go back now and look at.”

This functionality is pivotal for multiple developer teams working on DAGs, or even on respective parts of the same DAG. It’s also helpful for inheriting data pipelines when their original authors have switched jobs or projects.

The most pervasive use case likely entails debugging attempts and gleaning why parts of data pipelines are broken, or how they can be improved to maximize efficiency.

Airflow’s DAG versioning is fairly detailed, including aspects of the prior history of DAGs, like “What were the logs of that prior history; what was the structure of that prior history,” Koka commented. “How long did it take to run in a historical version? Being able to look at all the DAG runs based on prior incarnations of that pipeline or DAG then becomes more important.”

## Decoupled Security Enhancements
Airflow 3.0 has also boosted its security features to make the platform worthy of enterprise-scale production opportunities. Its chief security upgrade is separating the task execution capabilities from the administration, scheduling, and overall orchestration capabilities the solution provides.

Airflow’s server components now include “an API server which can basically read and write into the Airflow metadata database,” Koka said. “And then, we provide what’s called a task SDK, which is a client component, which is initially in Python. So, all the user-defined code only runs in the context of this task SDK.”

With this paradigm, the task SDK’s code doesn’t directly connect to Airflow’s metadata database, preventing worker processes from directly writing to it. Instead, the jobs specified in the task SDK interface with the API server to report and receive the status of jobs. The result is “a stronger security access control posture,” Koka explained. Koka also mentioned that a task SDK for [Golang](https://go.dev/) will be available imminently, and that community members have been asking for a task SDK with support for Rust.

## Remote Execution
One of the more compelling consequences of the decoupling of Airflow’s task execution capabilities from its other core functions is that it effectively allows for tasks to run wherever users would like them to. In some cases, this latitude can reinforce security and [data governance controls](https://thenewstack.io/make-data-governance-automation-suck-less-with-a-supergraph/) — like running jobs on data complying with financial industry regulations in a private cloud, so it doesn’t leave a particular data center.

For this use case, such data “can be orchestrated centrally but still remain completely local to that particular datacenter for data sovereignty,” Koka said.

The API server provides the centralized orchestration Koka referenced, while its separation from the task SDK enables jobs to run in completely different clusters, in public or private clouds, or wherever else organizations specify. “You might have some ML jobs which would benefit from GPUs,” Koka commented.

“You can run those on a completely separate GPU cluster. You don’t need to add the expense of having those GPUs on your same cluster. You can just go and rent the GPU cluster when the need comes up.”

## Scheduling Options
The 3.0 release still supports, yet substantially expands beyond, the traditional batch paradigm for scheduling data pipeline jobs. Several modes for scheduling tasks are now available, including:

**Event-Driven Scheduling:**With this option, organizations can trigger workflows based on data changes in external systems. There are also low-latency implications, such as relying on this scheduling method to trigger certain pipeline components based on data arriving in[Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/). “It enables Airflow to be reactive to data changes in the rest of the ecosystem,” Koka mentioned. “It’s more near real-time event processing.”**Simultaneous DAG Execution:**This scheduling approach is helpful for machine learning model inferences. “You really want to be able to run many of those at the same time,” Koka said. “We’ve added support for inference execution so you can run multiple of these pipelines of incoming data at the same time.”**Ad-Hoc Scheduling:**Conceptually, there’s some overlap between this scheduling variety and event-driven scheduling. However, “I generally tend to think about it as being something which is triggered based on almost like a human event or human-triggered event,” Koka said. “Something like a mortgage application showing up, or somebody saying I want to run a DAG as the result of an API, which is from some other system, triggered by a human action.”
## Enterprise Maturation
Apache Airflow 3.0’s DAG versioning controls, security upgrades, remote execution capabilities, and job scheduling flexibility make it useful for a broadening number of use cases. The latest edition also allows for backfills, so organizations can asynchronously rerun missed tasks, monitor their progress, and cancel them.

Each of these developments signals a transition of the pipeline authoring and deployment tool from one desired by developers and engineers in backrooms, to those deployed in enterprise applications.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)