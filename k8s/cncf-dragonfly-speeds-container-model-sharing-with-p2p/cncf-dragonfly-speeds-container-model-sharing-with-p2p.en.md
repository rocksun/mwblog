The Dragonfly project, an open source peer-to-peer image and file distribution system, [has graduated](https://www.cncf.io/announcements/2026/01/14/cloud-native-computing-foundation-announces-dragonflys-graduation/) from the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)‘s program for incubating new cloud native technologies.

The [open source technology](https://github.com/dragonflyoss/dragonfly), under CNCF’s wing [since 2018](https://www.cncf.io/projects/dragonfly/), has shown that it can work in production settings, with its ability to copy containers and large AI models across a network at scale, according to the organization. Built to run on [Kubernetes](https://thenewstack.io/kubernetes/), it has found use by organizations managing large-scale AI workloads, and has found a home in other environs as well, including [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) and [edge computing](https://thenewstack.io/edge-computing/).

CNCF [Dragonfly](https://d7y.io/), originally developed for internal use by [Alibaba Cloud](https://www.alibabacloud.com/), provides [a way for organizations](https://thenewstack.io/dragonfly-brings-peer-to-peer-image-sharing-to-kubernetes/) to distribute images across a network. It can copy container images to thousands of nodes nearly simultaneously.

It also works well with files, caches and logs.

Overall, 271 individuals across 130 companies have contributed 26,000 commits to building out the project.

“Looking back on this journey over the past eight years, every step has embodied the open source spirit and the tireless efforts of the many contributors,” said Zuozheng Hu, founder of Dragonfly and emeritus maintainer, in a statement.

## The Power of P2P

A peer-to-peer file sharing mechanism could help cloud native deployments in distributing new and updated container images across a cluster more quickly and with less stress to the upstream network.

P2P, first popularized by music sharing programs such as Napster over two decades ago, can make full use of the cluster’s bandwidth while eliminating the possible bottleneck of having a single server respond to all the requests for a new image.

In a P2P network, each node, or “peer,” can share files with each other, rather than all the nodes saturating the bandwidth to the image server by downloading identical copies of a single image.

Dragonfly is not a pure P2P technology; It still requires a supernode, to schedule and control distribution within the peer network. An agent on each node, dfget, downloads the file pieces. Another component, the dfdaemon proxy, intercepts image downloading requests from a container engine to dfget.

## Dragonfly’s Robust Support Stack

As a CNCF project, the development team has built a robust support stack in the past decade. The Dragonfly can be installed via [Helm](https://artifacthub.io/packages/helm/dragonfly/dragonfly), and monitored with [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) and [OpenTelemetry](https://thenewstack.io/can-opentelemetry-save-observability-in-2026/).

To speed transfers, it can run on the [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) protocol. Images can be “[preheated](https://goharbor.io/docs/2.12.0/working-with-projects/working-with-images/preheat-images/)” for faster sharing via the [Harbor open source registry](https://goharbor.io/docs/2.12.0/working-with-projects/working-with-images/preheat-images/).

Dragonfly also supports CNCF’s [ModelPack specification](https://github.com/modelpack/model-spec) for tidier AI model distribution.

One Dragonfly subproject, called [Nydus](https://nydus.dev/), has brought considerable value to the software by further accelerating model distribution.

“The combination of Dragonfly and Nydus substantially shortens launch times for container images and AI models, enhancing system resilience and efficiency,” said [Jiang Liu](https://github.com/jiangliu), Nydus maintainer, in a statement.

## Use Cases for Dragonfly

Dragonfly has found a home across some of the most innovative [cloud native services](https://thenewstack.io/cloud-native/), many located in Asia. CNCF provided a few key examples.

It has become a core component of the container image and data distribution system for Alibaba, providing support for the annual Double 11 (Singles’ Day) shopping festival, as well as an ongoing role in model data distribution and cache acceleration.

It has saved considerable transmission bandwidth across the 10,000 Kubernetes nodes of the Asian financial company [Ant Group](https://www.antgroup.com/en/home). Nydus, in particular, helped the organization reduce image pull time to near zero, and the technology is used for large language model movement as well.

For the [Datadog](https://thenewstack.io/is-datadog-becoming-a-platform-engineering-company/) observability firm, Dragonfly with Nydus cut the time it takes node daemonsets to start up within seconds, whereas the image pulls would previously drag that time out to five minutes.

Chinese mobile technology company [DiDi](https://web.didiglobal.com/) uses Dragonfly for large-scale file synchronization and image distribution for enterprises.

And container registry service [Kuaishou](https://www.cncf.io/case-studies/kuaishou-technology/) is about to use Dragonfly to support image distribution capabilities for tens of thousands of services and hundreds of thousands of servers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)