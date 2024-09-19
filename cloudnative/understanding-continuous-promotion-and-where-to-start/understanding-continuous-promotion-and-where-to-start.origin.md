# Understanding Continuous Promotion and Where to Start
![Featued image for: Understanding Continuous Promotion and Where to Start](https://cdn.thenewstack.io/media/2024/09/2a05c31f-mountains-1024x576.jpg)
Continuous integration and continuous deployment (CI/CD) have long been the bedrock of modern software development, seamlessly integrating code changes and ensuring their swift deployment across various environments. However, as the ecosystem evolved with the advent of Kubernetes and GitOps, the traditional CI/CD mechanisms started showing signs of strain.

Continuous promotion offers a transformative approach to [CI/CD](https://thenewstack.io/ci-cd/) tailored for a cloud native environment. Traditional CI/CD processes often struggle to keep pace with the dynamic nature of [Kubernetes](https://thenewstack.io/kubernetes/) and [GitOps](https://thenewstack.io/4-core-principles-of-gitops/). Introducing a continuous promotion mechanism bridges the gap between CI and CD, allowing for a more fluid promotion of artifacts.

## Traditional CI/CD Overview
Traditional CI/CD processes are centered around a linear workflow — building code, running tests, packaging the application and deploying it to target environments. In many cases, these environments were virtual machines (VMs) or bare metal servers with pre-installed dependencies. This approach worked well for monolithic applications but began to show limitations with the rise of [microservices](https://thenewstack.io/microservices/) and [containerization](https://thenewstack.io/containers/).

The introduction of containers provided a standardized packaging mechanism, yet the synchronous nature of traditional CI/CD struggled to align with the asynchronous, declarative characteristics of Kubernetes.

As a result, organizations often found themselves bolting Kubernetes onto existing workflows, leading to inefficiencies and operational friction. Despite the advent of GitOps to streamline last-mile deployments, the core CI/CD processes remained largely unchanged. This dissonance highlighted the need for an evolved approach capable of handling the complexities of modern cloud native environments.

## The Impact of Kubernetes and Containers
[Kubernetes and containerization have drastically altered the landscape ](https://thenewstack.io/what-enterprise-rfps-require-from-kubernetes-and-container-management-software/)of software deployment. Containers provide a consistent and portable environment, simplifying the packaging and distribution of applications. Kubernetes, with its powerful orchestration capabilities, has become the de facto standard for managing containerized applications at scale.
However, this shift introduced a new set of challenges for traditional CI/CD pipelines. The synchronous, linear nature of traditional CI/CD processes struggled to keep up with the declarative, asynchronous operations of Kubernetes. This has often resulted in a mismatch, where Kubernetes’s dynamic environment management clashes with the rigid steps of conventional CI/CD.

Furthermore, the need to manage multiple microservices, each with its own life cycle, introduced additional complexity. As teams adopted Kubernetes, they frequently had to create custom scripts to bridge these gaps, leading to fragmented and error-prone workflows. This highlighted the necessity for a more integrated and adaptive approach to CI/CD in cloud native ecosystems.

Despite advancements, traditional CI/CD processes and Kubernetes operations often find themselves misaligned. At the same time, in the GitOps framework, there’s a tendency to overextend the role of CI beyond its intended scope.

We’ve looked at these issues closely in our previous article, [“Why CI and CD Need to Go Their Separate Ways”](https://thenewstack.io/why-ci-and-cd-need-to-go-their-separate-ways/). So how do we address this and come out victorious?

## Introduction to Continuous Promotion
Continuous promotion is an innovative approach designed to enhance the traditional CI/CD pipeline in a cloud native environment. Unlike conventional methods that treat CI and CD as isolated processes, continuous promotion integrates them through a cohesive framework.

Using the strengths of both CI and CD, it ensures that artifact promotion is automated and aligned with organizational policies. Continuous promotion acts as an intermediary layer that monitors changes in artifacts and orchestrates their progression through various stages, from development to production.

Using rule sets and continuous verification mechanisms, it ensures that only validated updates are promoted, reducing the risk of failures. This approach not only streamlines the deployment process but also enhances visibility and control, making it easier to manage complex microservices architectures. Continuous promotion thus represents a significant evolution in the CI/CD paradigm, aligning it more closely with the demands of modern, cloud native applications

## What Is Necessary to Implement Continuous Promotion?
Sounds good on paper, but where do you start? For your CI/CD process to take full advantage of all that Kubernetes and GitOps have to offer, continuous promotion needs to “speak natively” to both the CI and GitOps/CD processes.

A successful continuous promotion tool or process must include the following:

### Reconciliation Loop for Artifacts
A reconciliation loop process continuously monitors artifact repositories for any changes made to deployment-related artifacts. In the case of Kubernetes and GitOps, this can be a Helm repository, git repository and/or container image repository.

### Policy-Based Retrieval Workflow
Incorporate a policy-based retrieval workflow of the monitored repositories. The continuous promotion tool should take into account that the CI process is constantly happening and not every update to these repositories equals the need to deploy them. With a policy-based retrieval workflow, users can build business logic around deployments and only retrieve artifacts that are meant to be deployed.

### Understanding the Correlation Between Artifacts and Deployments
It understands the relationship between related artifacts and when/how they should be deployed together. Continuous promotion doesn’t need to store artifacts, instead, artifacts are kept at their desired locations, and the continuous promotion process keeps track of the metadata of these artifacts. By using the knowledge of where the artifacts are stored and which versions are of interest, a sort of “meta” artifact is created as a single deployable unit.

### Understanding the Correlation Between Artifacts and Target Stages
It understands the relationship between the artifacts and which stage they need to be in (typically organizations see these stages as “environments”). A continuous promotion process doesn’t get involved directly with GitOps/CD; instead, it interfaces with the source of truth (git) and acts as an orchestrator, knowing when, where and how a promotion process is facilitated.

This keeps a natural separation of CI, which largely produces artifacts, and GitOps/CD, which focuses on the deployment of these artifacts. This shifts the focus away from “environment”-based promotion to purpose-based promotion. Where the purpose of the artifacts is the determining factor.

### Success Verification Mechanism
It verifies the promotion of artifacts after deployment with data collected from existing metrics providers. A successful continuous promotion workflow needs to be able to integrate with existing metrics providers to determine the overall health of the promotion process.

Kubernetes object health checks are only a small part of the bigger picture of your application stack, therefore a continuous promotion workflow must take into account the overall health of your application and how it’s behaving. Working hand in hand with metrics providers and progressive delivery tools, continuous promotion fits perfectly into existing workflows to provide ultimate visibility of the end-to-end process of your cloud native application delivery process.

## Enter Kargo
Our solution to these challenges is called [Kargo](https://akuity.io/what-is-kargo/), an open source tool designed to implement continuous promotion within CI/CD pipelines. It addresses the complexities associated with deploying applications in a Kubernetes and GitOps environment by providing a structured mechanism for promoting changes.

Kargo does not replace existing CI or CD tools but enhances them by adding an intermediary layer that focuses on orchestrating promotion of artifacts. By doing so, it helps facilitate more reliable and efficient deployment processes, reducing the manual effort needed to manage complex deployments and aligning better with the asynchronous nature of cloud native ecosystems.

### Start your Continuous Promotion Journey with Kargo
Are you a GitOps practitioner ready to try out Kargo? Head over to the [Kargo GitHub page](https://github.com/akuity/kargo). Already a Kargo user and want to take it to the next level? Sign up for our [Kargo Enterprise early access](https://akuity.io/what-is-kargo).

Kargo will reach general availability status on Oct. 17. [Join us for a roundtable discussion with its creators and early adopters](https://us06web.zoom.us/webinar/register/7517265595769/WN_q6UIrHAMRk23itv9OUyDMw).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)