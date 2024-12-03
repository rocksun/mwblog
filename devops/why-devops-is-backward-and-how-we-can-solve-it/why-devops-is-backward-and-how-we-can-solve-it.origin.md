# Why DevOps Is Backward and How We Can Solve It
![Featued image for: Why DevOps Is Backward and How We Can Solve It](https://cdn.thenewstack.io/media/2024/11/e030a842-devops-1024x586.png)
Even in the world of technology, written language can play a surprisingly important part of our understanding of how that tech is applied.

The concept of merging development and operations [has been around](https://platformengineering.org/talks-library/devops-is-dead-long-live-platform-engineering) for [about 15 years now](https://blog.mindgrub.com/the-rise-and-fall-of-devops). Shortened to the commonly used term “[DevOps](https://thenewstack.io/devops/),” it’s been used prolifically to describe most established software development, deployment and support. Gaining “sec,” short for security, in more recent times, DevSecOps has now come to represent how software ought to be developed.

But the reality is application development comes first. Only after the code is written does the team [fully define the infrastructure, security requirements and process](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/) to get the application to market and running smoothly. Then well-documented architecture is followed by a well structured [CI/CD pipeline](https://thenewstack.io/ci-cd/), where new features and bug fixes are seamlessly written and deployed. But we don’t live in that ideal world.

## DevOps or OpDev?
Perhaps the term “DevOps” simply rolls off the tongue better than “OpDev,” but the argument could be made that since development comes first, operations will follow. But if we look under the hood, most shops actually do run “OpDev” pipelines, even though they do not recognize how that came about within the organization.

Every time a developer imports a cloud provider’s software development kit (SDK) or accesses resources through a command line (CLI), that dev is being granted the opportunity to [build operations infrastructure in service of accomplishing a task](https://platformengineering.org/talks-library/devops-is-dead-long-live-platform-engineering). Authentication? Database requirements? Serverless functions? Each of these are at least programmatically available to the developer team.

Unless it’s a fast and loose startup (and we can talk about why it’s not a good idea even here) the security and operations teams will need to evaluate the requested resources in the source code and build out a management framework for providing that infrastructure after the code has been written.

In that mythically ideal world discussed above, this might not be a problem if the combined teams had all agreed to a defined set of requirements and project architecture before development began, but even the best plan never survives first contact. And let’s not even start on the headaches that code change pull requests (PRs), feature adds and refactoring have on the architecture.

Without a very strict CI/CD pipeline and (usually) many team members keeping infrastructure safe and cost efficient, operations is a Sisyphean task, and most importantly it’s slow.

## Solving the Problem
So we need a better way to handle infrastructure without turning the ops team into firefighters rather than cooperative team members. Correspondingly we want to enable the devs to build unencumbered by strict rule sets as well as preserve the agile nature and fast pace of development.

[There are a few different solutions to this problem](https://cd.foundation/state-of-cicd-2024/). The most opinionated way is to abstract away the infrastructure as well as the common development methods and replace them with an entirely new language.
A comprehensive solution is a general-purpose [programming language](https://thenewstack.io/programming-languages/), designed to develop entire cloud applications, including their infrastructure and application code. While this solves all the problems, it’s an enormous lift for most teams. The vast majority of developers are comfortable with a set of well-established languages or are working in an existing codebase written in a legacy language.

More realistic and easily workable methods like [Nitric](https://nitric.io?utm_content=inline+mention) abstract away the platform as a service SDKs from the codebase and replace the developers’ infra requirements with a library of tools that can be referenced exactly the same, no matter where the finalized code is deployed. The operations teams can easily maintain the needed infra patterns in a centralized location, reducing the need to solve issues after code PRs.

Maybe we need another term for [this process](https://circleci.com/blog/platform-engineering-devops-at-scale), like [platform engineering](https://platformengineering.org/talks-library/devops-is-dead-long-live-platform-engineering), or perhaps we can keep our existing DevOps terminology. But whatever the language, we need to rethink the tools we give developers to use infrastructure: Bring the ops part of the architecting process to the same development timeframe as the application development.

Using [new backend framework tools](https://nitric.io/blog/nitric-is-terraform) built on the HCL and Pulumi standards, which are already used by the vast majority of developers, is a surprisingly simple way to solve a whole host of problems including clean integration with existing vulnerability scanning tools and processes. And with modern coding AI tools, refactoring a legacy codebase to integrate a standard infra backend is getting easier by the day.

Is DevOps still backwards? More likely it’s still alive and kicking in its original form. It just needs a better way for developers and operations to work together. Long live DevOps.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)