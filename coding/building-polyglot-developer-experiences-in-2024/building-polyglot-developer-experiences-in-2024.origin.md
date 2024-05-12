# Building Polyglot Developer Experiences in 2024
![Featued image for: Building Polyglot Developer Experiences in 2024](https://cdn.thenewstack.io/media/2024/03/cda19fdc-letters-5570359_1280-1024x576.jpg)
![](https://cdn.thenewstack.io/media/2024/03/1435258b-image001-300x225.png)
dapr logo
As a developer, it’s easy to be overwhelmed by the number of tools you need to learn and use to do your job. While experience has taught us that there is no silver bullet off-the-shelf solution that will serve every need, there are best practices, open interfaces, and standards that can greatly reduce the cognitive load on developers and teams.
With a combination of open-source tools and standards, it’s possible to implement your custom development workflows no matter what tools your company uses.
Let’s look at how to build custom (and polyglot) developer experiences optimized for specialized workflows, based on open source projects such as
[Dapr,](https://thenewstack.io/microsofts-open-source-dapr-could-help-developers-build-agnostic-microservice-applications/) [Knative Serving](https://thenewstack.io/knative-applies-to-join-kubernetes-community-at-cncf/), and [Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/).
The
[Dapr](https://dapr.io) project offers application-level APIs, cloud native patterns, and best practices that enable developers to use different languages to build complex distributed applications. This API-driven approach makes applications portable across environments as application infrastructure such as databases, key/value stores, message brokers, and other cross-cutting application concerns are abstracted away behind APIs.
No matter if you are running the application locally, or on Kubernetes with a cloud provider-managed service, your application code does not change. Dapr integrates with popular frameworks and tools such as: Spring Boot and Quarkus for Java developers; ASP.NET Core and .NET Aspire for C# developers; and Flask for Python developers while providing integration with IDEs such as IntelliJ and VScode.
## Knative Serving
![](https://cdn.thenewstack.io/media/2024/03/4dd5521c-image002.png)
Knative logo
Knative Serving is another
[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) project that focuses on providing a serverless experience on top of Kubernetes, that helps teams not only to scale up their production workloads but also to implement different release strategies (blue/green deployments, canary releases, A/B testing) to optimize their release cycles.
Knative Serving is also a Kubernetes extension and is usually not aimed at developers, but it provides the building blocks for the functionality that developers will be using in their day-to-day activities.
Knative Serving is well known for providing the base layer to build Function as a Service (FaaS) platforms such as the
[Red Hat OpenShift Serverless platform](https://www.openshift.com/try?utm_content=inline+mention), as it greatly simplifies how to configure workload deployments, compared with out-of-the-box Kubernetes resources, such as ingress, services, and deployments.
Projects like Dapr and Knative, by using the Kubernetes resource model, enable teams to create configurations that can be packaged and shared across teams to create environments with the right tools installed and ready to be used. But there is a catch, if you rely on Kubernetes tools and extensions you tie your teams to using a Kubernetes cluster. That is where Dagger comes to save the day.
## Dagger
![](https://cdn.thenewstack.io/media/2024/03/3441a7cd-unnamed.png)
Logo
[Dagger](https://dagger.io) enables teams to codify, using the language of their choice, their custom development and operational processes that can run across on-premises and cloud services. Development teams that utilize multiple languages can combine these different tools to ensure that they focus on their development tasks instead of learning about how multiple tools need to be combined.
By using the Dagger SDKs available in most languages, teams can codify how to build, package, and deploy their applications. While Dagger is mostly compared with tools like Tekton, Jenkins, and GitHub actions, it is becoming quite clear that one of the main advantages of adopting tools like Dagger is to create customized experiences on top of complex tools.
Dagger helps us to codify different but consistent experiences for local and remote development. If we rely on stable and open APIs like the ones provided by Dapr to build complex distributed applications, the
[Dagger Dapr Module](https://www.google.com/url?q=https://daggerverse.dev/mod/github.com/marcosnils/daggerverse/dapr@18ab6cf84f5a783a2c72629eea6ed9e9f728c71e&sa=D&source=docs&ust=1708464005151302&usg=AOvVaw3tZ2W3PFJh184p6L7MYM1c) integration provides a local and polyglot setup for coding applications outside of a cluster.
Once the application is ready to be deployed to a cluster, a developer experience built with Dagger can simplify the deployment to a remote environment hiding, for example, the creation of Kubernetes resources or which release strategies are implemented specifically for these teams. Because Dagger has an ecosystem of integrations that can be combined by using your favorite programming language, your teams can easily package and distribute more complex experiences based on existing and community-maintained integrations.
To sum up, teams building complex distributed applications will need more than one tool to be successful. To avoid pushing every team member to learn how to use and combine complex tools that require for example, to set up Kubernetes clusters, is not a good idea if you are trying to promote fast feedback loops and improve your teams’ software delivery speed.
## Summary
This article covers three open source tools that help teams build applications that run in different environments because they rely on open interfaces such as the Dapr APIs. A project like Knative Serving can make a huge difference in reducing the cognitive load on how teams configure their workloads to run inside a Kubernetes cluster, as it provides a simplified but powerful resource model.
Finally, Dagger can be used to abstract away the inherent complexities of using Kubernetes, to implement polyglot and local development experiences that provide the functionality that applications need outside of a Kubernetes cluster. Once the application is ready to be deployed to a remote environment, a custom remote experience can be codified using your favorite programming language and can hide from users that tools like Knative Serving are used in the target cluster.
The combination of these three technologies provides flexibility and enhances productivity by reducing the cognitive load on the developer and the number of tools they need to learn while building custom (and polyglot) developer experiences that are optimized for specialized workflows. And it’s all based on freely available open source software.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)