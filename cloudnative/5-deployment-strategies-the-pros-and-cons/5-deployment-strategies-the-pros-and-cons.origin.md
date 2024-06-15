# 5 Deployment Strategies: The Pros and Cons
![Featued image for: 5 Deployment Strategies: The Pros and Cons](https://cdn.thenewstack.io/media/2024/06/1f537c66-shutterstock_1537549334-1024x576.jpg)
When you deploy applications and services to production, you want to minimize downtime and provide a seamless user experience. The days of switching off an application to perform an upgrade are long gone, and zero-downtime deployments are now table stakes for many industries.
You don’t get seamless deployments entirely without cost. Each strategy requires you to
[handle compatibility](https://thenewstack.io/ci-is-not-cd/) between versions. However, some techniques bring lots of benefits with [little additional complexity](https://thenewstack.io/kubernetes-predictions-were-wrong/).
To manage updates without maintenance windows, there are a number of
[deployment strategies](https://thenewstack.io/gatekeepers-limit-continuous-deliverys-benefits/) available. Let’s look at the most common strategies to see what the trade-offs are:
- Recreate
- Blue/green
- Canary
- Rolling
- Shadow
## Recreate
The recreate strategy shuts down the running application, deploys the new version, then makes the new version available to users. This means users can’t use the application during the deployment.
Because this strategy is the simplest to implement, it’s often the application’s default deployment strategy. The only mechanism to reduce downtime on a recreate deployment is to make the deployment operation as fast as possible.
**Before deployment:**Version 1 is running and accepting all traffic. **During deployment:**Version 1 has been stopped and doesn’t accept traffic while the new version is deployed. **After deployment:**Version 2 is running and accepting all traffic. ![](https://cdn.thenewstack.io/media/2024/06/77b326df-recreate.gif)
### Benefits of the Recreate Strategy
The recreate strategy for deployments is very simple. You don’t need to manage multiple versions of the application running simultaneously, and after the deployment, you can expect all users to be running the same application version.
When you use the recreate strategy, there are fewer cases where a user will interact across a version boundary. All running instances have the same application version.
There are still some cases where a user may interact across the version boundary. If they open a form in version 1 and submit it after the deployment, the request may fail if the application can’t accept the submission from the previous version. Where you have a frontend application that runs background requests, it’s possible for a user to make requests from version 1 in the frontend to your newly deployed version 2 backend.
### Drawbacks of the Recreate Strategy
The main downside of the recreate strategy is the downtime. Requests made during the deployment will result in an error, as the application isn’t available. Your service-level objectives (SLOs) may account for deployment windows, in this case, a more complex strategy isn’t required as long as you can achieve the objectives without artificially limiting your deployment frequency.
The recreate strategy also means all users are exposed to problems introduced in a new application version. If a problem is detected, the previous application version must be redeployed, causing further downtime.
A progressive deployment strategy can minimize deployment-related downtime. Progressive delivery allows you to deploy an application gradually, minimizing downtime and providing simple rollbacks where needed. Let’s look at the most common options for progressive delivery.
## Blue/Green Deployments
With blue/green deployments, the new version is deployed without receiving traffic. The load balancer is updated to send traffic to the new application version when the deployment is complete.
**Before deployment:**The blue environment is running version 1 and accepting all traffic while the green environment has no version installed. **During deployment (phase 1):**Version 2 is deployed to the green environment while the blue environment continues to handle traffic with version 1. **During deployment (phase 2):**Traffic is switched from the blue environment to the green environment. The blue environment has no traffic but is running and available if a rollback to version 1 is needed. **After deployment:**The green environment is running version 2 and accepting all traffic, and the blue environment is phased out.
### Benefits of the Blue/Green Strategy
Traffic continues to flow to the application during the deployment of the new version of the application. This means the deployment has no downtime. If you detect a problem with the new application version, you can switch traffic back to the previous version just as easily.
### Drawbacks of the Blue/Green Strategy
Requests between the two application versions will likely overlap more, so your application needs to be designed to handle this gracefully. If you want seamless rollbacks, compatibility in both directions must be considered.
Because two application versions run simultaneously, you need sufficient resources to run both workloads. The out-of-balance workload will not consume as much resource as the production workload, but it will still consume some. Once you’re satisfied the new version is running successfully, you can decommission the out-of-balance resources. Alternatively, you can leave them available for fast rollbacks.
## Rolling Deployments
With a rolling deployment, each application instance is replaced with the new version until all instances are running the new version of the application. This allows zero-downtime deployments without the same resource requirements as blue/green deployments.
**Before deployment:**All instances have version 1 of the application. **During deployment:**One at a time, each instance is stopped and replaced with an instance of the new application version. **After deployment:**All instances have version 2 of the application.
### Benefits of Rolling Deployments
Rolling deployments require fewer resources than a blue/green deployment yet still provide zero-downtime deployments.
### Drawbacks of Rolling Deployments
If you discover a problem with a new version, you must redeploy the previous version to resolve it. This will take longer than a blue/green deployment, where you can just update the load balancer to send traffic to the previous version.
You also need sufficient capacity to serve requests with one instance removed, which may limit your ability to deploy during peak times. To avoid this problem, you can use a surge upgrade, which adds a new instance before each old one is removed.
With rolling deployments, both versions of the application will be run throughout the deployment process. That means you must design the application to handle both versions running simultaneously, including concerns such as both versions communicating with the same database.
## Canary and A/B Test Patterns
Rather than expose all users to the new application at once, the canary strategy exposes a small number of users to the new version. You can validate the application’s stability before sending more users to the new version. You can use this approach as both a deployment and test strategy.
**Before deployment:**All users are routed to version 1 of the application. **During deployment:**A small group of users are routed to the new application version. If this is successful, you can increase the proportion of users using the new version. **After deployment:**All users are routed to the new application version.
### Benefits of Canary Deployments
Canary deployments reduce deployment risk as only a sample of users is routed to the new application version. You can test application performance and functional stability based on the canary sample.
### Drawbacks of Canary Deployments
Canary deployments are more complex than other strategies. You’ll need to use more advanced routing on your load balancer to ensure users don’t switch between application versions with each request. However, this also enables you to A/B test changes, as you can set up routing rules based on request headers or user properties (like location).
Though the load balancer pins each user to a version, you’ll need to ensure that components such as data stores are compatible with both versions of the application.
You may need extra capacity as the traffic volumes may not reflect the proportion of users assigned to each application version. For example, you might route a group of users to the new version only to find they are the most intensive system users. This can lead to insufficient resources to handle the canary group.
While canary deployments help you reduce the impact of any issues introduced by the new application version, this only works if you detect the issue early. If you discover the problem too late, you might have already routed all users to the new version.
## Shadow Deployments
In cases where you can’t test a new application version using a sample of real traffic, you can use the shadow deployment strategy. This approach replays real requests in an isolated environment.
### Benefits of Shadow Deployments
Done correctly, shadow deployments have no impact on production systems. Any problems found in the new version have zero impact on real users.
You can compare the response times of the production requests with those in the shadow environment, which means the most accurate comparison for performance, errors and outcomes between the production and shadow environments.
### Drawbacks of Shadow Deployments
You must be certain that repeating requests in an isolated environment will not have side effects. For example, if your application sends emails or other notifications to users, you must ensure these are switched off in the shadow environment. You also need to ensure that the shadow environment doesn’t issue calls to external services that might result in side effects.
Because requests are replayed from the production environment, which runs the previous application version, shadow environments will fail if they feature breaking changes to these requests.
By introducing shadow deployments, you double the amount of work you have to do in production. Both the real production environment and the shadow environment need to handle the real workload.
For your existing application, the risk of introducing shadow deployments may outweigh that of running a small sample of users against the new version with canary deployments.
When it comes to promoting the new software version to production, you’ll still need to use one of the other deployment strategies, as shadow deployments are a test-only strategy.
## Choosing a Deployment Strategy
There are a few things to consider when selecting your deployment strategy.
- Can you achieve your desired deployment frequency with your current approach?
- Is downtime acceptable?
- How much can you spend on infrastructure to reduce downtime?
- What patterns does your system support and can you re-architect it?
- How quickly do you need to redeploy a version?
|
Strategy |
Zero- downtime |
Easy rollbacks |
Pre-flight tests |
Cost
|Recreate
|No
|No
|No
|No additional resources
|Blue/green
|
Yes |
Yes |No
|Two environments must run at the same time during deployments, but not full-time
|Rolling
|
Yes |No
|No
|Some additional resources required
|Canary
|
Yes |
Yes |
Yes |No additional resources
|Shadow
|n/a
|n/a
|
Yes |Parallel environments needed throughout the test
The recreate strategy for deployments is rarely sufficient for modern applications, but it’s worth double-checking whether you need anything more complex. If your software isn’t used outside of local business hours, you can schedule an out-of-hours deployment and avoid any complexity.
In most cases, though, you need to eliminate the downtime. Continuous delivery and DevOps mean we’re moving toward more frequent deployments, which multiplies the impact of downtime to levels that make it hard to achieve your SLOs.
If the resource cost is acceptable, blue/green deployments provide the most benefits with the least complexity. Where cost containment is necessary, rolling deployments eliminate downtime at low cost, though you don’t get the rollback benefit of blue/green deployments.
Canary deployments and A/B deployments, which are canary deployments with more specific routing rules, allow you to test new software versions with real traffic, which can be a good way to spot problems your automated tests might miss. Ideally, you’d use what you learn from canary testing to increase the likelihood of detecting similar issues in your deployment pipeline in the future.
Shadow deployments require a robust architecture that guarantees the shadow environment has no side effects. This makes it hard to retrofit to existing applications, though some components may not be too far from this requirement. This is an advanced strategy with many trip hazards, so if you’re not going to get lots of valuable insights from this approach, it’s better to avoid it.
Modern infrastructure and CD tools can help you implement these deployment strategies without inventing them from scratch.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)