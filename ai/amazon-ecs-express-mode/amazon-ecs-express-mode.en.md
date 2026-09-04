The promise with containers was simple: if it runs on your local machine, it will run in production. And this promise holds – your container runs. But there’s a tax: setting up everything around it. To reach your container, you’ll need a load balancer to route traffic to it, and scaling policies to handle variable traffic. Then come the networking components and the minimally scoped access roles. And somewhere in that checklist, don’t forget the security configuration; unless you’d rather hear about it from your compliance team. At some point, you wonder why you can’t just go back to building.

> “You give it a container image. You get a production service. And when your workload outgrows a single container, you don’t outgrow Amazon ECS Express Mode.”

Sound familiar? You’re not alone. Most teams spend cycles before they feel confident deploying containers in production. That’s time from your roadmap spent on decisions that don’t differentiate your business. Somewhere between the third Terraform module and the second [IAM policy review](https://thenewstack.io/how-iam-missteps-cause-data-breaches/), you’ve lost the speed containers were supposed to give you.

Amazon Elastic Container Service (ECS) is the container orchestration engine behind some of the largest production workloads on AWS. But until now, getting started with it meant understanding load balancers, networking, IAM roles, and scaling policies before you shipped anything.

We tried to change that and make it easier for you to get started and stay focused on building when we [launched Amazon ECS Express Mode](https://aws.amazon.com/about-aws/whats-new/2025/11/announcing-amazon-ecs-express-mode/). Express Mode is a new interface into that same engine. You’re not trading power for simplicity. You’re getting a faster door into infrastructure that’s already battle-tested. The vision was clear: keep it simple but extensible. You give it a container image and two IAM roles; you get an HTTPS service running on Fargate with a load balancer, a TLS certificate, autoscaling, and canary deployments. Oh, and all these resources run in your account, where you have full control.

```

 // Sample Terraform Code
 resource "aws_ecs_express_gateway_service" "frontend_service" {
   execution_role_arn = aws_iam_role.execution.arn
   infrastructure_role_arn = aws_iam_role.infrastructure.arn
 
   primary_container {
     image = "111122223333.dkr.ecr.us-east-1.amazonaws.com/my-service:1.4.2"
   }
 }

```

## What’s in Amazon ECS Express Mode?

Underneath the one-step deploy, this is what you’re getting:

* **No sprawl** – Every service sits behind an Application Load Balancer, but doesn’t get its own. Up to 25 Express Mode services within a VPC share a single ALB. Express Mode adds load balancers only when needed and removes them when services are deleted. No dangling resources for you to worry about.
* **Safer rollouts** – Out of the box, each deployment is a canary release where 5% of your traffic is routed to the new revision and bakes for 3 minutes, following which the remaining traffic is shifted. If your 4xx/5xx error rate exceeds 1%, an alarm we create for you triggers an automatic rollback.
* **Scaling** – Each service ships with an auto-scaling policy that targets 60% CPU utilization, scaling from 1 task to a maximum of 20 by default. If your workloads need to scale on memory or request count, you can configure that too.
* **IaC ready** – Create and manage Express services through CloudFormation, CDK, Terraform or GitHub Actions.
* **Complete ownership** – The cluster, load balancer, target groups, log groups and other resources are all in your AWS account. You can inspect them, audit events, and modify them directly if needed. Nothing is a black box.

### But what about my sidecars? My workloads aren’t that simple.

Sooner or later, as your application evolves, the workload becomes more than just one container. An observability agent needs to run beside the app, publishing traces to your monitoring solution. The base image gets swapped for the hardened one security maintains. The credentials move out of environment variables and into Secrets Manager. This is where extensibility comes into play.

For this, [Express Mode now supports](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-express-mode-custom-task-def/) providing a standard ECS task definition – the spec that describes your containers, their resource limits, and how they connect. Your sidecar, image, and credentials all fit right in. If your team runs ECS today, this is the spec you’re already writing. If not, Express Mode generates a task definition in your account, and when requirements arrive, you take that working spec, add what you need, and hand back the ARN. Once you associate a task definition with an Express Mode service, you can continue managing your application either through task definition updates or directly through Express Mode, whichever you prefer.

```

// Sample CDK snippet
const taskDef = new ecs.FargateTaskDefinition(this, 'TaskDef', {
  cpu: 1024,
  memoryLimitMiB: 2048,
  executionRole,
  taskRole,
});
 
taskDef.addContainer('Main', {
image:
ecs.ContainerImage.fromRegistry('111122223333.dkr.ecr.us-east-1.amaz
onaws.com/my-service:1.4.2'),
  essential: true,
  portMappings: [{ containerPort: 8080, name: 'main' }],
});
 
taskDef.addContainer('otel-collector', {
image:
ecs.ContainerImage.fromRegistry('public. ecr.aws/aws-observability/aw
s-otel-collector:latest'),
  essential: false,
  memoryReservationMiB: 256,
  command: ['--config=/etc/ecs/ecs-default-config.yaml'],
});
 
new ecs.CfnExpressGatewayService(this, 'FrontendService', {
  infrastructureRoleArn: infrastructureRole.roleArn,
  taskDefinitionArn: taskDef.taskDefinitionArn,
});

```

## Wait, am I locked into this?

No. Express Mode is an interface into Amazon ECS, not a walled garden. Every resource it creates is a standard AWS resource in your account, addressable by an ARN. If required, you can modify them directly through their respective AWS APIs in the Console, CLI or SDK.

> “Express Mode is an interface into Amazon ECS, not a walled garden.”

If you change the scaling policy, update a security group rule, or swap the task definition, Express honors those modifications on the next update. It does not overwrite changes you make. This means you can start with Express defaults today and customize individual resources as your requirements evolve, without migrating off Express or recreating your service.

Express also exposes the ARN of everything it manages – the load balancer, target groups, security groups, and alarms – through the Describe APIs and as CloudFormation/CDK outputs. You can reference them in your own stacks or hand them to existing constructs.

## Why did we design it as a single operation?

We deliberately made Express Mode a single API call, not a multi-step workflow. One input (your image or task definition ARN), one operation, one outcome.

That design choice compounds. Your IaC is under ten lines. Your [CI/CD pipeline](https://thenewstack.io/cicd-pipeline-front-line/) doesn’t need custom steps. An AI coding agent can deploy and iterate on your behalf because the entire surface is one well-defined spec it already knows how to read and modify.

But there’s an engineering reason too. Because Express Mode owns the full lifecycle of what it creates, it can clean up what it sets up. Delete a service, and the target groups, [scaling policies](https://thenewstack.io/beyond-magic-scaling-myth/), and alarms go with it. No orphaned infrastructure. And because you didn’t wire these resources together manually, one service’s deploy can’t accidentally touch another’s.

### Wrapping it up

As we continue to build on ECS Express Mode, our priority is simple – taking away the undifferentiated heavy lifting from our customers. Amazon ECS Express Mode is our attempt to make good on that: point it at an image, get a production service: load balancer, TLS, autoscaling, canary deployments, all running in your account, where you can see it and change it.

> “The configuration grows with your requirements; the operational burden doesn’t.”

And when your workload outgrows a single container, you don’t outgrow Express Mode. Bring your own task definition: the sidecars, the hardened images, the secrets, and keep handing the infrastructure to us. The configuration grows with your requirements; the operational burden doesn’t.

Try it from the AWS Console, Terraform, CloudFormation, CDK, or GitHub Actions – or just ask your agent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/9869ac4d-satej_bio-600x600.jpeg)

Satej Sawant is a Software Development Engineer on the Amazon Elastic Container Service team at Amazon Web Services (AWS), where he works on the developer experience for building with ECS — including its APIs, SDKs, CloudFormation, Terraform, and GitHub Actions...

Read more from Satej Sawant](https://thenewstack.io/author/satej-sawant/)