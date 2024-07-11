# Optimize Your ‘Inner Dev Loop’ to Increase Developer Velocity
![Featued image for: Optimize Your ‘Inner Dev Loop’ to Increase Developer Velocity](https://cdn.thenewstack.io/media/2024/07/e2d1b15d-balance-1024x603.png)
Just like there’s a Simpsons joke for every part of pop culture, there is an XKCD cartoon for everything in tech. A great example is *“*[compiling](https://xkcd.com/303/)*,”* from 2007.

![Comic "compiling": two figures sword fighting from office chairs while build compiles](https://cdn.thenewstack.io/media/2024/07/d52d378e-image1a-300x262.png)
Figure 1

Seventeen years later, compiling has fallen a little out of favor. But we all know what this cartoon would say now: “My code’s containerizing.”

Containerization has been instrumental in scaling development. It allows developers to create consistent environments across different stages of development and from local machines to production servers.

This consistency eliminates the age-old “it works on my machine” problem and significantly reduces configuration-related issues.

But it also introduces new problems. Container builds and registry uploads are pure downtime for engineers.

Containerization can be slow, which is a tax on productivity. That tax is often paid to run and test code, and then it’s paid again when changes to code are made. You can see the problem that unfurls from there.

This wasn’t always so. Without containers, traditional development loops were quicker, allowing higher velocity and more iteration.

Can we get back to that speed without sacrificing the benefits of containers? Yes.

## Inner and Outer Dev Loops Explained
The problem here is with the “inner dev loop.” An [inner dev loop](https://www.getambassador.io/docs/telepresence/latest/concepts/devloop) is the cycle of activities a developer performs locally while working on a feature or bug fix. It typically includes:

- Writing or modifying code
- Building the application
- Running and testing the changes
- Debugging, if necessary
- Committing the code
This cycle is repeated throughout the day, and its efficiency greatly affects a developer’s productivity. The faster and smoother this loop, the more iterations a developer can make, leading to quicker problem-solving and feature development.

In contrast, the “outer dev loop” encompasses the broader development life cycle, including:

- Planning and task assignment
- Code review and collaboration
- Continuous integration and deployment
- Staging and production releases
- Monitoring and feedback collection
The benefits of containerization have accrued to the outer dev loop by ensuring consistency across environments and simplifying deployments. But it has introduced friction into the inner dev loop. The time spent building containers and waiting for them to start can reduce the speed of iteration developers need for efficient coding.

Before containerization, the inner dev loop might have looked like this:

So, in the traditional inner dev loop, we have just over five minutes per development iteration, with just 10 seconds of “tax” downtime. Looking back at the containerized version, this is extended to over nine minutes, with almost half of that “tax.”

If a developer codes for six hours per day, we move from 70 to 40 iterations by moving to containers. Throughout a two-week sprint, this is 300 missing cycles.

Thus, optimizing the inner dev loop in a containerized environment is crucial for maintaining high developer velocity.

## Lowering the Downtime Tax of the Inner Dev Loop
The key to reclaiming lost velocity lies in streamlining the inner dev loop within containerized environments. We must find ways to minimize the “tax” imposed by containerization and deployments while retaining the benefits of consistency and portability that containers provide. Here’s where modern tools and practices come into play.

One approach gaining traction is local-to-remote development. This method allows developers to run their code locally while seamlessly connecting to the remote Kubernetes cluster. Tools like Ambassador’s [Telepresence](https://www.getambassador.io/products/telepresence) enable developers to code as if their local machine were part of the remote cluster.

The idea is simple yet powerful: Instead of building and deploying containers for every code change, developers can run a single service under development locally and have it interact with other services in the remote cluster in real time. This approach offers several advantages:

**Faster feedback loops:**Developers can see the impact of their changes immediately, without waiting for their full application to containerize and deploy.**Familiar local development:**Engineers can use their preferred tools and IDEs to maintain their productivity.**Access to remote resources**: Developers can interact with databases, microservices and other resources in the remote cluster as if they were local.**Reduced resource usage:**Fewer remote development environments are needed, potentially leading to cost savings.**Collaborative development:**Thanks to features like personal intercepts, teams can work on the same cluster simultaneously without stepping on each other’s toes.
Adopting such tools and practices can significantly reduce the “tax” on the inner dev loop. Let’s revisit our earlier example with this optimized approach:

In this optimized scenario, we’ve reduced the iteration time to around six minutes, with only about 30 seconds of downtime tax. This translates to approximately 60 iterations in a six-hour coding day — a substantial improvement over the containerized version and much closer to our original pre-container velocity. As you can see above, with local testing the developer loop is marginally longer than the traditional loop, but it’s still much quicker than the regular container loop and it includes the benefits of containerization. Win, win all around!

The goal isn’t to abandon containers — their benefits for scaling and production are too valuable. Instead, a hybrid approach can combine the speed of local development with the consistency and reliability of containerized environments.

By focusing on optimizing the inner dev loop, we can help developers regain their lost velocity, leading to more iterations, faster feature development, and, ultimately, better software more quickly. The key is to find the right balance between local development speed and the benefits of containerization — and with the right tools and practices, that balance is achievable.

Ultimately, your development process can be so smooth that you don’t even have time to check XKCD while containerizing.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)