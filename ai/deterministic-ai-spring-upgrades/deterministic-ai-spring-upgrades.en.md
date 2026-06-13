With the rise of AI coding agents, developers have begun experimenting with complex, multi-step upgrade requests. Since Spring is the most popular Java framework, the idea that developers can upgrade applications using natural language commands like “*Please upgrade this application to Spring Boot 4*” is an exciting prospect.

In reality, upgrading this way can be anticlimactic, especially if the application in question is a very large, legacy project. The developer has to wait around for 20 minutes or *even* longer to get the initial results. After that, developers usually need to iterate several more rounds to fix coding and compilation errors, not to mention test cases.

Upgrading a major framework, used across an application, requires a lot of testing and checking: even if the code compiles and looks technically correct, how the framework operates might have changed slightly enough, or there may be new capabilities in the upgrade that work in new and subtle ways that are not exposed until runtime.

This back and forth adds up in two ways:

1. Assuming that the codebase has no dependencies on internal shared libraries or frameworks, this process has consumed between 1 and 2 days. And this is without any guarantee that the changes will be successfully merged (e.g CI checks might fail, developers might reject the PR, etc). Without coding agents, this process could take a few more days, but the results are often more deterministic: the work of human programmers will more often than not work and be mergeable.
2. With code generation, you also need to account for token cost. This includes the initial run and every iteration.

If the reason for a framework upgrade is to resolve CVEs, time is even more critical, especially if you need a major upgrade. You want to deploy the patch as soon as possible to remove any potential security risk.

## Example: upgrading Spring Petclinic

As an example, let’s look at upgrading the Spring Petclinic from Spring Boot 3.5.x to Spring Boot 4. The Spring Petclinic application contains very few entities (vets, owners, appointments) and is relatively simple and well-designed. Using an AI to migrate from Spring Boot 3.5.x to Spring Boot 4 took me 478,380 tokens for planning, plus 908,900 tokens for the code changes… but it ultimately failed.

What went wrong? The coding assistant tried to make several changes I did not request, such as updating or renaming Spring starters and import statements. There were also several compiler warnings about using deprecated methods, as well as a compilation error. This meant I needed more iterations to fix it, and hence consumed more tokens and time.

*The challenges of using AI coding agents for Spring upgrades: errors and deprecated methods often require many iterations to resolve, as seen in the Spring Petclinic example.*

And this was upgrading from a more recent version of Spring. If my goal had been to upgrade from an older version, like 2.7.x, to Spring Boot 4, the situation would have been even worse because there would have been intermediate steps where things could have gone wrong.

Well, in my experience, it *would* have gone wrong. This is worth noting because, in 2025, Broadcom estimated that around 50% of Spring Boot apps were still on Spring Boot 2.7 or earlier.

## When upgrading is not optional

One of the main reasons engineering teams upgrade to new versions of Spring Boot is to address security concerns. This is especially true right now, where Broadcom is seeing [a massive spike in vulnerability discovery](https://blogs.vmware.com/tanzu/how-to-prepare-for-the-world-of-ai-driven-exploits/). Many organizations now recognize that upgrading is part of their security preparedness strategy.

The annoyance/cost of upgrading a demo app like the Petclinic is one thing, but in production, organizations are facing the need to upgrade more than ever to address security concerns across multiple Git repositories that depend on each other. In these cases, practicing [continuous upgrading](https://blogs.vmware.com/tanzu/what-is-a-continuous-upgrade-culture-and-why-is-it-important/) is very helpful. By keeping all dependency versions within supported ranges and using the latest patch releases, a continuous upgrade culture reduces the window during which CVEs affect your code and grants access to Java and Spring’s latest optimizations, leading to infrastructure savings.

In addition, standardization promotes using the same Spring versions across all your applications, enabling you to share internal Spring components across them. While not always possible, a more homogeneous, or at least in-support Spring estate can really help with day 2 maintenance and ongoing upgrades because the processes become more consistent. To promote standardization, you need to think about operations at scale. So, the real critical question to ask yourself is “how can we be more efficient at upgrading Spring at scale?”

As we discovered with something as simple as the Petclinic, even though coding agents allow you to write your upgrade changes faster, coding agents are not perfect, nor free. After all, they’re non-deterministic *by definition*, and hence they are not predictable, consistent, nor do they always give accurate results.

> “Coding agents allow you to write your upgrade changes faster, coding agents are not perfect, nor free. After all, they’re non-deterministic by definition, and hence they are not predictable.”

So, the main question is “How can these upgrades using AI be accelerated at scale and apply more correct code changes?” In my experience, to achieve good results at scale, you need to enrich your coding agents with additional tools that are able to perform type-safe and deterministic refactors.

To understand how human-in-the-loop (HITL) might improve upgrades, let’s first set a foundation on how coding agents work.

## The necessity of type-awareness: addressing agent limitations

[Coding agents](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/) are products designed to produce the best answer using a Large Language Model (LLM) based on a set of configured tools or skills. Coding agents are applications that use Large Language Models (LLMs) and tools to generate code and related artifacts like configurations and docs, and to execute commands, including compiling, running tests, and even deploying code. Some people prefer to use the term “harness” instead of “coding agent”.

“Tools,” in this context, can be any command-line tool (like Maven or Gradle), and skills are natural language descriptions with some scripts that we can configure to force agents to follow in specific situations.

Coding agents have been designed with extensibility in mind; for example, these tools can be expanded with (remote or local) [MCP servers](https://thenewstack.io/why-the-mcp-server-is-now-a-critical-microservice/). Skills are designed to be simple and easy to add; they’re essentially just markdown files stored in a particular directory.

One common source of confusion is that developers assume that coding agents perform semantic analysis of the codebase to enact code changes, just as a human would, leading to higher quality and fidelity. I learned that is not correct.

Coding agents, by default (Claude, Cursor, Copilot), do not understand the type or correctness of every expression that appears in the codebase, and this is why, sometimes, coding assistants introduce compilation errors.

You can reduce errors by connecting a [Language Server Protocol through an MCP server](https://github.com/isaacphi/mcp-language-server), which is a technology that some IDEs, or developer tools, support, but it is not a very common scenario to use it to perform code changes, except in very limited circumstances. On the Java side, the most flexible open-source technology for designing deterministic code changes (recipes) that can resolve the type of every expression in our codebase (yes, like the IDE autocompletion mechanism) is OpenRewrite, which is executed as a Maven or Gradle plugin.

To address these problems, Tanzu Platform and Tanzu Spring have some CLI commands based on OpenRewrite that help coding agents plan and upgrade Spring apps. These Tanzu solutions guide your coding agents on planning and executing incremental Spring upgrades at scale. The CLI will address deprecations, API changes, property changes, and even handle complex cases such as internal frameworks and third-party OSS library upgrades that depend on Spring or its transitive dependencies and must be upgraded first.

If you are using Tanzu Platform, the simplest way to get started is to run “cf repo unpack-skills” in your terminal, then ask your coding agent to upgrade Spring. This will unpack a skill that enables your coding agent to execute “cf repo upgrade-plan” to plan the upgrade and “cf repo apply-upgrade-plan” to perform the first step of the plan, which applies the code changes.

Otherwise, you could use Tanzu Spring Essentials, which includes access to the App Advisor CLI, and you only need to use the [App Advisor local MCP server](https://techdocs.broadcom.com/us/en/vmware-tanzu/spring/application-advisor/1-5/app-advisor/model-context-protocol-server.html), which will teach your coding agent to use the corresponding CLI commands to get and apply an upgrade plan, but every developer needs to maintain the CLI version and the configuration.

Sometimes the engineering team needs to do advanced planning before upgrading to a major version of Spring. This planning may require removing projects that are no longer supported in the new version and migrating to compatible replacements, [such as Spock integration in Spring Boot 4](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide%23features-removed-from-this-release).

There might also be some API-breaking changes that need additional context (e.g., a new type of Exception, or changing a method modifier to make a public method protected) to apply the most appropriate refactor. This is just one example, and each organization will need to decide on a common approach to address these incompatibility issues and centralize the resolution.

## Balancing determinism and non-determinism at scale

When you are deciding how to solve issues during your Spring upgrade, or with any of your internal libraries, the VMware Tanzu Spring team recommends following this principle**:** If the solution for an incompatibility is deterministic, we recommend that organizations create their own recipes and configure common migration patterns (e.g., from Spock to JUnit) with our Tanzu CLI tools.

> “If the solution for an incompatibility is deterministic, we recommend that organizations create their own recipes and configure common migration patterns with our Tanzu CLI tools.”

This solution will be much less expensive at scale than asking developers to follow a naive approach with an AI coding agent, since using the App Advisor CLI does not require tokens, either for testing or for applying changes across hundreds of Git repositories.

Otherwise, if the solution to an incompatibility issue is non-deterministic, we recommend that you create a set of skills centralized in a Git repository that your coding agent can choose before or after the Spring Boot upgrade is applied.

Now, if you think about upgrading Spring at scale, this process should not be triggered by any developer. It should be triggered automatically by your [CI/CD](https://thenewstack.io/ci-for-coding-agents/) pipelines and then configured either directly via the CLI or via an AI coding agent, if you have the additional skills you might need. Using this setup, you prevent the use of a large number of tokens for repetitive tasks that do not necessarily provide good results, and can be consumed instead for your actual business problems, not just upgrading your frameworks

*To learn more, please visit* [*VMware Tanzu Spring*](https://www.vmware.com/products/app-platform/tanzu-spring)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/06/0c4db682-raquel-pau.jpg)

Raquel is a senior product manager at Broadcom. She has extensive experience with Java and CI/CD developer tools, and internal developer platforms (IDPs).

Read more from Raquel Pau](https://thenewstack.io/author/raquel-pau/)