Continuous integration is the process of merging code (updates or existing features) with an existing codebase (software tool or product, for example). CI is a development practice where developers merge code in a central repository several times daily.

In CI, each line of code added to the codebase triggers a sequence in a CI/CD pipeline, generating feedback for developers. This process allows improvements to be made quickly and easily.

CD is an attempt to speed up and automate deployments. An operator can push out multiple deployments in a week across numerous services and know the exact condition of the applications and infrastructure in the course of the deployments.

> “Continuous delivery is the natural extension of continuous integration, an approach in which teams ensure that every change to the system is releasable, and release any version with the push of a button. Continuous delivery aims to make releases boring so that we can deliver frequently and get quick feedback on what users care about.” — Thought Works

With continuous delivery, every change made to the system can be released, and any version can be released at any time. Continuous integration is the natural extension of continuous delivery. Continual delivery provides quick feedback on what users care about and aims to make releases routine — and predictable.

The continuous integration and continuous delivery (CI/CD) process is transforming [DevOps](https://thenewstack.io/devops/). Even if each step of the software development lifecycle can be carried out manually, CI/CD automates the stages in software development and deployment.

## How Platform Engineering Helps Manage Innovation Responsibly

### The Focus of a CI/CD Pipeline

To run a CI/CD pipeline successfully, organizations should outline goals that guide developers’ approaches and processes. While each pipeline is unique, it should reflect some overarching goals.

Here are some results that should be the focus of the pipeline:

### Quick Fixes and Improvements in Subsequent Updates

[CI/CD automation](https://thenewstack.io/3-ways-to-use-automation-in-ci-cd-pipelines/ "CI/CD automation") automatically allows code changes to reflect in end users’ software. CI/CD pipelines should prioritize quick fixes and improvements to existing code to improve software quality and user experience.

### Push Button Deployments

Continuous delivery requires a “state” machine, which is not provided by CI tools. CD tools, such as [Spinnaker](https://thenewstack.io/kick-the-tires-on-spinnaker-with-armorys-minnaker/), can take an environment from one state to the next until it makes it to production. The machine will move the environment, such as [Docker containers](https://thenewstack.io/containers/), through to production in an automated fashion. It will even be able to do rollbacks, canary deployments, and scaling instances.

This process allows for the agile, push-button, automated deployments that an ideal CD mindset drives towards. Such pipelines are at the core of CD capabilities because they orchestrate a repeatable deployment over stages.

### Fast and Frequent Software Releases

One of the higher-level achievements in a DevOps transformation is continuous delivery. Focusing on software releases in a CI/CD pipeline is a cultural shift for companies because it involves organizational change, too. DevOps transformation means building cross-functional teams with common goals, aligning the organization around the architecture, and creating a culture of continuous improvement.

## Three Ways CI/CD Adoption Can Benefit Your DevOps Team

### The Structure of an Effective CI/CD Workflow

The process for achieving CI/CD goals has been broken down into separate stages. The goal is to ensure that new and runnable code is fit for use before it’s sent out to end users.

Most unique and effective pipelines mirror the following structure:

Each new pipeline run is **triggered by a change** in the source code repository. An update or variation to the existing code — such as automated workflows or results from a previous pipeline run — begins the CI/CD process.

In this stage, runnable instances of code that could potentially be deployed to end-users are created. This is done through a combination of source code and its dependencies. Code not passing this stage indicates a problem with the project’s configuration and should receive immediate attention.

**Automated tests are run on the code** to determine its accuracy. These tests, created by software developers, are required to meet certain standards. Multiple tests at this stage would detect bugs or other problems developers do not foresee. The test could take minutes or several hours, depending on its complexity. Code that does not successfully pass this test stage instantly notifies the development team that adjustments must be made. After the code is tested and considered runnable, it’s delivered to the repository.

**Deploy.** Once the code passes all predefined tests, the runnable code in the repository is deployed into different environments, such as a staging environment for the internal team and a production environment for end-users.

Validation and Compliance. Organizational needs determine what takes place in **validation and compliance**. For example, image security scanning tools ensure image quality and match them against known vulnerabilities.

## The Approach to Cloud Native CI/CD Tools Is Changing

An increasing focus on continuous delivery (CD) has brought new tools and practices that allow teams to produce frequent, fast, and boring automated releases. [Cloud native](https://thenewstack.io/cloud-native/) CI/CD requires a deeper understanding of DevOps practices and how they affect the way organizations deploy and manage workloads using containers, microservices, and serverless functions.

A new approach to continuous integration and continuous delivery (CI/CD) is emerging for cloud native architectures. With cloud native architectures, complexity is shifting away from the building and assembly of the code to orchestrating releases. Build tools such as Travis CI and Jenkins are starting to commoditize and become much simpler.

As more organizations get comfortable with building custom code using containers and other immutable constructs, they spend fewer cycles on building that code and shift into solving the problems of orchestrated releases.

## Impact of Kubernetes CI/CD

Kubernetes, the open source container orchestrator, makes CD easier to execute with tools, modularity, and immutable infrastructure. Kubernetes simplifies the deployment and monitoring of microservices. It helps define a container deployment and manage instances but leaves it up to the user to automate those deployments into environments.

Here are some proven practices for improving Kubernetes CI/CD:

Implementing Blue-Green Deployment Strategy. Similar to preparing for emergencies, this strategy involves a pattern that creates an additional set of production instances to existing instances for quick switching in case of failure or downtime. The blue represents the staging environment, while the green represents the production environment.

Leveraging Git-Based Workflows. CI/CD pipelines should be activated through GitOps. This ensures that changes and source code in the pipeline are stored in a unified source repository for easy correction and deployment.

Testing and Scanning New Container Images. Testing and scanning container images every time a new image is created can handle vulnerabilities such as configuration issues introduced with new builds. It also ensures that commands are working properly.

## Challenges With the CI/CD Framework

As much as the CI/CD process is evolving, it is not without challenges. Some difficulties faced include:

Version Control. The CI/CD model requires the creation of versions from the source code repository to ensure continuity. Managing these variations can be difficult because of the number of changes made.

Faulty Tests. As new code is written, developers are expected to write multiple tests to determine the accuracy and behavior of products. If the right tests aren’t administered, developers may receive faulty feedback loops, which could affect the end product entirely.

Security Breaches. Concerns have been raised about the security of the CI/CD process in the development, integration, and deployment phases. Software developers are urged to develop security measures alongside the code-writing process and not at the end of the cycle.

CI/CD practices are constantly getting refined. Learn more about CI/CD trends, new approaches, and the opinions of industry experts through The New Stack articles [in this category](https://thenewstack.io/ci-cd/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.