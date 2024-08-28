# Why CI and CD Need to Go Their Separate Ways
![Featued image for: Why CI and CD Need to Go Their Separate Ways](https://cdn.thenewstack.io/media/2024/08/fa4c83b9-ci-cd-separate-ways-1024x576.jpg)
In the constantly evolving landscape of software development, continuous integration (CI) and continuous delivery (CD) have been foundational methodologies for efficient and reliable application deployment.

Despite their longstanding presence, modern technologies like [Kubernetes](https://thenewstack.io/kubernetes/) and [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) have introduced complexities that traditional [CI/CD processes](https://thenewstack.io/ci-cd/) have not addressed. With Kubernetes providing an asynchronous deployment mechanism and GitOps offering a declarative approach to manage application states, a gap has emerged.

Continuous promotion and related tools aim to bridge these gaps, streamlining the CI/CD pipeline in a GitOps-centric environment.

## Evolution of CI/CD
CI and CD are essential practices in software development, designed to enhance the speed and reliability of deploying applications. Initially, CI/CD was a linear process: code was built, tested and then deployed to a target environment. This approach worked well with traditional virtual machines or physical servers, where deployment environments were relatively static.

However, the introduction of containers and Kubernetes changed the landscape drastically. Kubernetes provided a more dynamic, asynchronous deployment mechanism, creating a mismatch with the synchronous nature of traditional CI/CD processes. As a result, teams began to adopt GitOps to better align with this new paradigm and try to mitigate the disconnect with traditional CI/CD processes.

Despite these advancements, CI/CD processes largely remained unchanged, leading to inefficiencies and complexities in managing deployments across different environments. This ongoing evolution highlights the need for more integrated solutions like continuous promotion to bridge these gaps effectively.

## Challenges with Current Models
Current CI/CD models face several challenges, especially with the [adoption of Kubernetes](https://roadmap.sh/kubernetes) and GitOps.

The crux of the issue lies in the inherent disconnect between the synchronous nature of traditional CI/CD processes and the asynchronous nature of Kubernetes deployments. This mismatch often leads to inefficiencies where deployment pipelines become cluttered with custom scripts and workarounds to manage the gaps between CI and CD.

Additionally, GitOps, while effective in managing the last mile of deployment, can’t handle complex multi-environment orchestration. It focuses solely on the final deployment state, leaving a significant operational gap in orchestrating deployments across various stages or environments.

This has resulted in CI pipelines being overextended and taking on roles they were never designed for, such as managing indefinite deployments and handling complex dependencies. These challenges underscore the need for a more cohesive approach that integrates seamlessly with modern technologies, offering a more flexible and efficient deployment process.

## Complexities in CI/CD
### Linear vs. Complex Reality
The traditional view of CI/CD as a straightforward, linear process belies the intricate realities faced in modern software development. While initially conceptualized as a sequence of steps — build, test and deploy — the actual deployment pipelines are far more complex. Modern applications often involve numerous interconnected services, each with its own dependencies and lifecycle.

The linear model struggles to accommodate these intricacies, leading to a web of interdependencies and asynchronous processes that must be managed. Additionally, the rise of [microservices architecture](https://thenewstack.io/microservices/) further complicates this landscape, as each service may have its own CI/CD pipeline with distinct requirements and triggers.

This complexity can lead to issues such as deployment bottlenecks, increased manual intervention and trouble maintaining consistency across environments. Furthermore, the need for continuous monitoring and the ability to handle rapid changes in dynamic cloud environments necessitate a more flexible and adaptive model than the traditional linear approach can provide. Adapting to this complex reality is essential for effective CI/CD implementation.

### Overusing CI for CD Tasks
In many organizations, CI pipelines are stretched beyond their intended function, taking on tasks that traditionally belong to the CD domain.

CI is designed to automate building and testing code, focusing on creating reliable artifacts. However, as the complexity of deployment environments grows, CI processes are often burdened with tasks like environment provisioning, configuration management and deployment orchestration.

This overextension results in a cumbersome, inefficient CI pipeline that struggles to manage the demands of modern, dynamic deployments. This misuse not only increases the complexity and maintenance overhead of CI pipelines but also leads to longer cycle times and reduced flexibility. Addressing this issue requires a clear delineation of responsibilities between CI and CD, leveraging appropriate tools to keep each process focused on its core objectives without unnecessary overlap.

## Introducing Continuous Promotion
Continuous promotion is a concept designed to bridge the gap between CI and CD, addressing the limitations of traditional CI/CD pipelines when used with modern technologies like Kubernetes and GitOps.

The idea is to insert an intermediary step that focuses on promotion of artifacts based on predefined rules and conditions. This approach allows more granular control over the deployment process, ensuring that artifacts are promoted only when they meet specific criteria, such as passing certain tests or receiving necessary approvals.

By doing so, continuous promotion decouples the CI and CD processes, allowing each to focus on its core responsibilities without overextension. This not only streamlines the deployment pipeline but also enhances the reliability and efficiency of the entire process. The need for continuous promotion arises from the increasing complexity of modern deployments, where traditional CI/CD approaches struggle to manage the asynchronous and dynamic nature of cloud native environments effectively.

### Benefits of Continuous Promotion
Continuous promotion offers several advantages that enhance the efficiency and reliability of deployment pipelines.

Introducing a systematic step between CI and CD ensures that only qualified artifacts progress through the pipeline, reducing the risk of faulty deployments. This approach allows the implementation of detailed rule sets, which can include criteria such as successful test completions, manual approvals or compliance checks. As a result, continuous promotion provides greater control over the deployment process, enabling teams to automate complex decision-making processes that would otherwise require manual intervention.

Additionally, it reduces the burden on CI pipelines, which are often overloaded with deployment tasks they weren’t designed to handle. This separation of concerns allows more focused and efficient CI processes, while CD can concentrate on deployment and management of applications.

Overall, continuous promotion aligns better with the dynamic nature of modern cloud native environments, facilitating smoother and more reliable application rollouts.

## Kargo: A New Approach
[Kargo](https://akuity.io/what-is-kargo/) is an open source tool designed to implement the concept of continuous promotion within CI/CD pipelines. It addresses the complexities associated with deploying applications in a Kubernetes and GitOps environment by providing a structured mechanism for promoting changes.
Kargo operates by monitoring changes to artifacts, such as application images or configuration files, and applying predefined promotion rules to determine if these artifacts should progress to the next stage of deployment. This tool effectively bridges the gap between CI and CD by introducing a declarative framework for managing promotions, ensuring that only vetted changes are deployed.

Kargo does not replace existing CI or CD tools but enhances them by adding an intermediary layer that focuses on orchestrating the promotion of artifacts. By doing so, it helps facilitate more reliable and efficient deployment processes, reducing the manual effort needed to manage complex deployments and aligning better with the asynchronous nature of cloud native ecosystems.

### Continuous Promotion with Kargo
Kargo facilitates continuous promotion by serving as an intermediary that orchestrates the promotion of artifacts within the CI/CD pipeline. It operates by continuously monitoring changes in the repository, such as updates to code, configurations or [Docker](https://www.docker.com/?utm_content=inline+mention) images.

Based on predefined rules and conditions, Kargo evaluates whether these changes meet the criteria for promotion. This evaluation considers factors such as successful test results, compliance checks and necessary manual approvals. Once the conditions are satisfied, Kargo automates the promotion process, updating the GitOps repository to reflect the new state and triggering deployments through GitOps controllers like Argo CD.

This approach minimizes the risk of deploying unverified changes, ensuring a higher level of deployment reliability and efficiency. By utilizing Kargo, teams can reduce manual interventions and streamline their deployment processes, allowing CI tools to focus on building artifacts while CD tools manage the rollout. This integration makes Kargo a vital component in modern, dynamic deployment environments.

### Start Your Continuous Promotion Journey with Kargo
Are you a GitOps practitioner ready to try out Kargo? Head over to the [Kargo GitHub page](https://github.com/akuity/kargo), where you can start your continuous promotion journey. Already a Kargo user and want to take it to the next level? Sign up for our [Kargo Enterprise early access](https://akuity.io/kargo-early-access/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)