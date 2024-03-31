# Evolve Manual and Templated Dockerfiles with Automation
![Featued image for: Evolve Manual and Templated Dockerfiles with Automation](https://cdn.thenewstack.io/media/2024/03/365f0bb7-docker-1024x744.png)
[Docker’s](https://thenewstack.io/containers/how-to-deploy-a-container-with-docker/) portability makes it simpler for organizations to migrate applications to the cloud or adopt hybrid cloud strategies. Applications can be developed locally in containers and then deployed to the cloud without significant changes. This flexibility is crucial for organizations looking to leverage the cloud for its scalability and cost-effectiveness while maintaining some resources on premises.
By standardizing the environment in which applications run, Docker reduces the overhead associated with configuring and maintaining different environments for development, testing and production. This efficiency accelerates the development cycle and simplifies the deployment process, allowing teams to focus more on development and less on infrastructure issues.
The problem is, manually
[crafting and maintaining Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) presents significant challenges for developers. These challenges include the time-consuming nature of writing and maintaining the configuration and also the difficulty in optimizing Dockerfiles for efficient builds across a variety of project types and sizes.
When deciding whether to create Dockerfiles manually or use an abstraction tool to autogenerate them, the right choice depends on several factors, including your project’s complexity, your team’s familiarity with Docker and the specific requirements of your deployment environments.
## The Dockerfile Dilemma
For simple projects, the overhead of learning an abstraction tool might not be justified. For a basic node application, a simple Dockerfile could look like the following snippet.
While this Dockerfile is straightforward for a single application, managing similar files across multiple
[microservices](https://thenewstack.io/microservices/) or updating them to reflect new dependencies becomes increasingly complex and error-prone.
Let’s take a look at an example of an out-of-control Dockerfile for a Node.js application. This is an exaggerated example designed to illustrate common pitfalls that make it challenging to maintain as a project scales.
## Common Docker Pitfalls
While you may not encounter all these pitfalls at once, it’s likely that some of them crop up over time. Let’s look at each issue in this Dockerfile:
**Inefficient layering**– This Dockerfile creates unnecessary layers, as there are multiple
RUNinstructions that could be combined. Moreover, it inefficiently handles file copying and dependency installation.
**Hardcoding**– This Dockerfile uses a specific version of the Node.js image (node:14) without an easy way to update it. It’s more scalable to use build arguments (ARG) to specify versions, allowing for easy updates without modifying the Dockerfile directly. **Global NPM package installation**– Installing global packages (TypeScript, ts-node, nodemon) makes the image larger and ties the build to specific versions of these tools. It’s better to include these as dev dependencies in package.json and use them locally, ensuring consistency across environments. **Unnecessary operations**– The Dockerfile includes steps that add to build time and image size, such as copying all source files twice and installing unnecessary packages after copying source files. Also, the use of
npm prune --productionafter installing all dependencies indicates an inefficient approach to managing production and development dependencies.
## The Case for Autogenerating Docker Images
With the advent of sophisticated tools and frameworks that automate the creation and
[management of Docker containers](https://thenewstack.io/fugue-security-config-checker-now-supports-cis-docker-benchmark-managed-containers/), there’s a strong argument for using these technologies to save time and reduce the potential for human error.
Using template engines like Jinja2, Mustache or EJS can help generate Dockerfiles from templates. These templates can define the structure of your Dockerfile, with placeholders for configurable options like base images, environment variables and dependencies. A simple script can populate these templates with actual values based on your application’s requirements or environment-specific configurations.
### Can We Take It a Step Further?
Frameworks like
[Nitric](https://github.com/nitrictech/nitric) bring intelligent automation to cloud application development, including the generation of Dockerfiles, by abstracting away the complexities of cloud service configurations and deployments.
## How to Automate Dockerfile Generation
Cloud applications generally have multiple entry points into an API, such as
get,
put,
patch and
delete methods. These applications also have handlers that activate triggers, such as listening to an event topic or running a scheduled task. Each entry point within an app can be built into its own container using Docker, then deployed to a cloud container runtime such as AWS Lambda, Google CloudRun or Azure Container Apps.
We can then decide how to build those containers based on the properties of the project — for example, the programming language used in the project or the need for telemetry. At the surface level, it might seem that the convenience of this is in a loss of control, but as long as the framework also includes built-in “escape hatches” to maintain control, you’ll still be able to override the default behavior by implementing custom Dockerfile templates to be used by some or all of the services in your application.
Here’s an example of a Docker template taken from the
[Nitric framework](https://github.com/nitrictech/nitric) that can easily be overridden.
## The Advantages of the Automated Approach
For container-based deployments, automation frameworks can generate Dockerfiles based on the application’s configuration and the services it uses. This includes setting up the appropriate runtime environments, handling dependencies and configuring the build steps necessary for the application to run in a containerized environment.
We also gain two useful power-ups:
**Portability**— Beyond Dockerfile generation, the automation framework can streamline the deployment process to support multiple cloud providers. This means applications can be deployed to [AWS](https://aws.amazon.com/?utm_content=inline-mention), [Microsoft](https://news.microsoft.com/?utm_content=inline-mention)Azure, **Local development**— Automation frameworks can enable development and testing of cloud native applications offline by emulating cloud environments. This means developers can test their applications in a cost-free environment that closely mimics their target deployment environment, reducing the “It works on my machine!” syndrome.
## Try It for Your Project
While templating Dockerfiles can offer a level of automation and standardization for Docker image creation, frameworks like
[Nitric](https://nitric.io) build on this concept, providing a more holistic approach to application deployment and management. They offer a streamlined, high-level interface for common tasks with the ability to override or extend the automatically generated Dockerfiles and deployment configurations.
Developers can specify custom Dockerfile instructions, integrate additional tools or services and even manually adjust the generated configurations before deployment. This ensures that teams can achieve the exact performance optimizations or feature integrations they require, without being constrained by the framework’s automation.
Create a proof of concept with
[Nitric](https://github.com/nitrictech/nitric) to see how you can streamline your application development and autogenerate the boilerplate required to run your application in the cloud. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)