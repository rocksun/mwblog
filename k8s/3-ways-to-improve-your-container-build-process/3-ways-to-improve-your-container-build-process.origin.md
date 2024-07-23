# 3 Ways To Improve Your Container Build Process
![Featued image for: 3 Ways To Improve Your Container Build Process](https://cdn.thenewstack.io/media/2024/07/5fffaf8c-lego-708087_1280-1024x682.jpg)
As [Kubernetes](https://thenewstack.io/kubernetes/) recently [celebrated its 10-year anniversary](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/), container images are at the heart of modern-day infrastructure. These container images tend to become more complicated and heavy; a report found that responded reporting that build time had [increased by 15.9%](https://www.incredibuild.com/survey-report-2022#item_7490) between 2020 and 2021.

In this article, I will explore the gains that can come from managing containers well, which will allow us to build lighter images, faster. Two of these tips will be specific to [Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/), while the last one uses [Pack](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/), which is a CLI tool that supports the use of [buildpacks](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/).

## Step Ordering
The order of the steps matters when writing a Dockerfile. Docker has a built-in caching mechanism — called layer caching — that caches each step in your file when you build a container image. So, the next time you build an image from the same Dockerfile, it will reuse the cached layers.

However, as soon as a step changes and the cache cannot be used — for example, because the application code has changed — all the following steps will also need to be run again.

Let’s take a look at a section of a Python app Dockerfile. Here, we start with an Ubuntu base image, copy the application code, and then install system packages.

1234567 |
FROM ubuntu:22.04# Copy the current directory contents into the container at /appCOPY . /app# Install Python and pipRUN apt-get update && apt-get install -y python3-pip python3-dev |
The issue with this ordering is that every time the application code changes, Docker cannot use its cache for the package installation part and will need to download and install the packages again. What should take less than a second might end up taking minutes.
Therefore the right ordering here would be to flip the instructions simply:

1234567 |
FROM ubuntu:22.04# Install Python and pipRUN apt-get update && apt-get install -y python3-pip python3-dev# Copy the current directory contents into the container at /appCOPY . /app |
I ran an example on a modest server with 16G of memory and 4 vCores with the following [Python application](https://github.com/sylvainkalache/sample-web-apps/tree/buildpack_pack_rebase_benchmark/python). To mimic the size of enterprise applications, I added numpy, scipy, and pandas as dependencies.
When using the Dockerfile with a [wrong ordering](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/python/wrongDockerfileOrder) — when the application code is copied before Python packages are installed — it took an average of 1.7 minutes to rebuild an image after a code change.

When using the Dockerfile with the [correct ordering](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/python/Dockerfile) — when the application code is copied before Python packages are installed — it took an average of 0.3 seconds to rebuild an image after a code change, which is 99% faster.

So don’t forget the rule of thumb for Dockerfile, place what is unlikely to change at the top of your Dockerfile and what is more likely to change at the bottom.

## Use Multistages
Multistage builds in Dockerfiles optimize the process of building images by allowing multiple FROM statements in the same Dockerfile. This feature helps create smaller, more efficient Docker images. For example, it can be used to separate the build environment from the runtime environment.

Again, I ran an example to see what improvements we could expect. This time, we use a sample Java application with Spring, Spark, and Kafka as dependencies.

Here is the Dockerfile using multistage:

1234567891011121314151617181920 |
# Multi-Stage Dockerfile## Stage 1: Build StageFROM maven:3.8.1-openjdk-16 AS build# Set working directoryWORKDIR /app# Copy the application source code and pom.xmlCOPY pom.xml .COPY src ./src# Build the applicationRUN mvn clean package## Stage 2: Runtime StageFROM openjdk:16-jdk-slim# Set working directoryWORKDIR /app |
As you can see, I have two FROM statements, one that I use to build my jar, and the second one that I use to build my images.
When using the Dockerfile [without multistage](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/java/nonMultiStageDockerfile) — when compilation and container installation are part of the same stage — the image size ended up being 1Gb.

When using the Dockerfile [with multistage](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/java/Dockerfile) — when compilation and container installation are part of the same stage — the image size ended up being 500Mo or 50% lighter. Depending on how many container instances need to load this image, this can provide a massive deployment time gain, and this is especially true if you have a geographically distributed infrastructure.

## Only Rebase a Specific Layer
This last tip is less well-known than the other two tips we discussed. Here we will use an additional tool — [the pack CLI](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) — which is based on the cloud native buildpacks implementation.

Thanks to the way images are generated with Buildpack, the [rebase](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/pack_rebase/) feature allows you to swap out the OS layers (run image) of a container image with a newer version of the run image without re-building the entire container.

To rebase an image, the command is the following:

1 |
pack rebase name-of-container-image |
Here, again, I ran an [experiment](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/python/benchmark.py) using a simple Python application, Dockerfile. When rebuilding a new container image using docker build, I went from Ubuntu 22.04 to the latest, which at the time of writing is 24.04. Rebuilding the image with the latest OS version took, on average, two minutes and 26 seconds.
When using the pack CLI rebase feature, rebuilding the container image with the latest OS version took, on average, 43 seconds, or 70% faster.

This is especially useful when you must urgently apply an OS security patch to your images, which will especially matter for companies with thousands or even hundreds of thousands of images to patch.

## Conclusion
All these may not matter when running things locally as a developer; however, build speeds matter when working with development pipelines. What might seem trivial gains when small will matter at scale. When you work in an engineering organization with many pipelines — especially with the proliferation of microservices — build and rebuild speeds will be essential to maintaining high shipping velocity. It could mean shifting dev cycles to happen in minutes instead of hours.

Smaller images will offer storage, network, and throughput performance gains and reduce cost when operating at scale.

Finally, faster update times matter when organizations are using a large amount of containers in production. The ability to replace an image layer on a central registry and have all the running images update individual layers is a handy protocol, especially when the alternative is to individually build and redeploy images.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)