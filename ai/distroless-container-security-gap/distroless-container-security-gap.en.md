Ever tried to shrink your container images to reduce their attack surface? If you have, you’ve likely discovered a frustrating paradox: shrinking a container often blinds your vulnerability scanners to what’s inside.

We’re facing an industry-wide tension between reducing [container attack surfaces](https://thenewstack.io/open-source-and-container-security-are-fundamentally-broken/) and maintaining the security visibility you need. To understand how we got here, and how we can solve it, we have to look at how we historically built containers, and why the current approaches fall short for Day 2 operations.

## The anatomy of container bloat

For a long time, full container images were the industry standard. The workflow was simple: developers pulled a base image that included a complete operating system, bundled their application code on top, and shipped it to production.

---

***KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12.* [*Register Now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)*!***

---

While convenient, this posed a massive security problem. These images included a shell, a package manager, and countless tools and utilities the application never used at runtime. Every piece of unused software in that container represented a potential vulnerability and an unnecessarily large attack surface. If a malicious actor breached the application, they suddenly had a full toolkit to download additional utilities and escalate the attack.

## The distroless security gap

To address these security concerns, the “distroless” movement emerged. The idea made sense: while full container images had a larger attack surface because of countless unnecessary components, the distroless approach sought to strip the container down to the bare-minimum dependencies needed for the application to run. No shell, no package manager, no extra utilities.

This certainly reduced the attack surface, but it came at a steep operational cost. Creating a distroless image is complex, fragile, and error-prone. In the effort to cherry-pick and aggressively trim the image, the package metadata — the manifest of what’s installed — often gets stripped out completely.

The unintended consequence is what we now call the “distroless security gap.”

This isn’t just a theoretical problem; it’s a well-documented industry blind spot. Scanners like Trivy will actively throw warning flags when OS package metadata is missing, and a [2022 Rezilion vulnerability report by Yotam Perkal](https://www.linkedin.com/posts/yotam-perkal_scanning-the-scanners-vulnerability-scanner-activity-7086727226372587521-pd94?utm_source=share&utm_medium=member_desktop) revealed that container scanners suffer from significant false negatives — failing to detect active vulnerabilities simply because they lack the necessary context.

> “You might have built an incredibly small container, but if your security team can’t scan it and mathematically prove it is safe, it becomes a massive compliance liability.”

Organizations like Chainguard have similarly noted that if a scanner can’t collect [complete package metadata](https://thenewstack.io/sbom-sniff-test-hardened-images/), the scan results won’t accurately reflect the image’s true contents. You might have built an incredibly small container, but if your security team can’t scan it and mathematically prove it is safe, it becomes a massive compliance liability.

Between full and distroless container images, we are left with an imperfect choice: bloated containers with a large attack surface, or minimal containers we cannot audit.

## Face-off: Imperative trimming vs bottom-up assembly

Fortunately, there is a third way. Instead of taking a large image and trimming it down, risking the removal of crucial metadata needed for accurate security scans, what if we built containers from the bottom up?

The premise is simple: build your own minimal container image from scratch, including only the exact elements you need. Because you build it from the bottom up rather than stripping it down, you can rest assured that the metadata remains intact. In the open source ecosystem, one example of this new generation of minimal, auditable OCI images is commonly referred to as “rocks.”

A bottom-up container build operates like a conveyor belt with three distinct stations: Slice, Build, and Run.

![Workflow diagram showing the three stations of a bottom-up container build.](https://cdn.thenewstack.io/media/2026/10/55ff8bea-conveyor-lily-rivers-klee.png)

## Station 1: Precision slicing

In a bottom-up build, your container starts as literally an empty image. Using an open-source tool like Chisel, you slice standard, trusted Linux packages (such as those from the Ubuntu archives) into smaller, granular pieces.

Instead of pulling an entire package, you pick only the exact “slices” your application actually needs. Because these slices come straight from curated archives, you maintain a trusted software supply chain with surgical precision. Crucially, the metadata for these slices is preserved, so your security scanners stay fully operational.

![Diagram illustrating the precision slicing capability of a bottom-up build.](https://cdn.thenewstack.io/media/2026/10/39e84d30-chisel-lily-rivers-klee.png)





*Click to enlarge graphic.*

## Station 2: Declarative builds

Traditionally, containers are assembled with imperative Dockerfiles, where the order of every command matters, and layer caching often creates bloat and fragility.

> “It shifts the developer experience from ‘scripting a build’ to ‘declaring a state.'”

Bottom-up builds replace this with [a declarative approach](https://thenewstack.io/buildpacks-container-security-scale/). Using an open-source build tool like Rockcraft, developers write a simple YAML file (e.g., rockcraft.yaml) that describes the app and its needs. The tool takes that definition, fetches the source, pulls in the specific package slices requested, compiles everything, and outputs a standard, OCI-compliant container image. It shifts the developer experience from “scripting a build” to “declaring a state.”

```

name: chiseled-python
base: bare

build-base: ubuntu@26.04-lts
version: "3.14"
summary: Chiseled Python3.14 rock
description: Chiseled Python rock
license: Python-2.0
platforms: { amd64: }

run-user: _daemon_

parts:
    install-python:
        plugin: nil
        stage-packages:
          - base-files_release-info
          - python3_core

```

## Station 3: Taming PID 1 at runtime

The final operational hurdle for minimal containers is what happens when they run. In a standard operating system, the OS handles process management automatically. But inside a container, if your application spawns child processes and those processes die, they leave behind “zombies” — dead processes that still occupy system resources.

Without a proper init system, zombies pile up until your container crashes, causing cascading failures at scale. Traditional base images include process managers, but distroless images often strip them out to save space. To keep minimal containers stable without reintroducing bloat, bottom-up containers use tools like Pebble, a tiny, lightweight service manager that runs as PID 1, serves as the container’s entry point, and safely reaps zombie processes.

## What’s next

For too long, the cloud-native ecosystem has treated security visibility and container minimalism as a zero-sum game. The distroless movement was a necessary step in highlighting the dangers of bloated images, but the resulting blind spots in vulnerability scanning are no longer acceptable for enterprise production environments.

> “For too long, the cloud-native ecosystem has treated security visibility and container minimalism as a zero-sum game.”

By shifting from an imperative, top-down trimming approach to a declarative, bottom-up assembly process, engineering teams can achieve the best of both worlds. We can build security-maintained, minimal containers that are auditable and operationally stable. Container security shouldn’t come at the expense of developer experience or Day 2 visibility.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/5af75322-headshot-lily-rivers-klee.jpg)

Lily Rivers-Klee is a Product Manager at Canonical, focusing on containers, toolchains, and runtimes.

Read more from Lily Rivers-Klee](https://thenewstack.io/author/lily-rivers-klee/)