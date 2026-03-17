Every backend project of any real size ends up with two codebases that describe the same system. You've got your application code in TypeScript or Go, and then somewhere else, usually a `terraform/` directory or a whole separate repo, you've got the HCL that provisions the database, the message queue, the IAM roles. They're written in different languages, reviewed in separate PRs, deployed through different pipelines. Nobody has a great answer for keeping them in sync.

Infrastructure from Code (IFC) gets rid of the second codebase. You declare your infrastructure (databases, Pub/Sub topics, cron jobs) right in the application code, and a framework reads those declarations to provision the actual cloud resources. Everything ships in a single PR, the infrastructure can't drift from the application because it's derived from it, and you stop maintaining Terraform modules that mirror what your code already knows.

Beyond cleaning up the day-to-day workflow, IFC changes how AI agents interact with your codebase, which is where things get interesting. More on that after covering the basics.

1import { api, SQLDatabase }

2import { Topic }

3

4const db = new SQLDatabase("orders")

5const topic = new Topic("order-created")

6

7export const create = api({

8method: "POST", path: "/orders"

9}, async (req) => {

10await db.insert(req)

11await topic.publish(req)

12})

Infrastructure from Code pipeline

Code → compile → provision. The IFC pipeline in three steps.

A service that needs a PostgreSQL database and a [Pub/Sub topic](/blog/event-driven-architecture) declares both right where they're used:

```


import { api } from "encore.dev/api";
import { SQLDatabase } from "encore.dev/storage/sqldb";
import { Topic } from "encore.dev/pubsub";


const db = new SQLDatabase("orders", { migrations: "./migrations" });


const orderCreated = new Topic<OrderEvent>("order-created", {
  deliveryGuarantee: "at-least-once",
});


export const createOrder = api(
  { expose: true, auth: true, method: "POST", path: "/orders" },
  async (req: CreateOrderRequest): Promise<Order> => {
    const order = await db.queryRow`
      INSERT INTO orders (customer_id, total)
      VALUES (${req.customerId}, ${req.total})
      RETURNING *`;
    await orderCreated.publish({ orderId: order!.id, total: order!.total });
    return order!;
  }
);


```

Locally, the framework provisions a real PostgreSQL instance through Docker and runs Pub/Sub with equivalent semantics in memory. In production, a platform like [Encore Cloud](https://encore.cloud) reads the same declarations and provisions RDS + SNS/SQS on AWS, or Cloud SQL + GCP Pub/Sub on GCP, in your own cloud account. Encryption, backups, least-privilege IAM are handled by [environment-level configuration](/docs/platform/infrastructure/configuration) that the infrastructure team sets once.

The same pattern applies to cron jobs, object storage, caching, and secrets. Each maps to different cloud resources depending on where you deploy:

SQL Database

Pub/Sub

Cron Jobs

Object Storage

Caching

Secrets

SQL Database

declaration

new SQLDatabase("orders", {
migrations: "./migrations"
})

localPostgreSQL via Docker

awsRDS

gcpCloud SQL

same code → different infrastructure per environment

Click a primitive to see how it maps across environments.

IFC as a concept isn't new. [Encore](https://encore.dev) shipped this approach before the current wave of AI coding tools, and the idea of deriving infrastructure from application code predates even that. The reason it's picking up momentum is that AI agents changed the volume.

When an agent generates ten new endpoints in an afternoon, nobody writes the ten Terraform modules to match. The application code is ready in minutes, but the infrastructure work to actually run it takes the rest of the day. [DORA's research](https://dora.dev/research/) found that writing code faster with AI doesn't speed up delivery unless the surrounding workflows change too, and infrastructure provisioning is the workflow that hasn't changed for most teams.

per month

22 features waiting for infrastructure

AI accelerates code generation. Infrastructure provisioning stays the same speed.

There's a context problem too. When infrastructure is declared inline, an AI agent can read a single service file and understand that it uses a PostgreSQL database, publishes to a topic with at-least-once delivery, and exposes an authenticated POST endpoint. That's enough to generate a new endpoint that queries the same database, or a subscriber that processes events from the same topic. With Terraform, the infrastructure context lives in a different repo (or a different directory with a different language), and the agent has no way to connect the application logic to the resources it depends on.

With an IFC framework, the agent writes application code that declares its infrastructure needs, and the output is deployable on `git push`. No separate infrastructure PR, no plan/apply cycle, and what the agent wrote matches what actually runs. Encore's [MCP server](/blog/mcp-server) takes this further by giving the agent visibility into existing services, APIs, and schemas across the whole application, so generated code follows the project's existing patterns.

Terraform made infrastructure reproducible and version-controlled, which was a real improvement over clicking through cloud consoles. It also created a permanent separation between application code and infrastructure code that teams have been living with for a decade. (We covered this shift in more detail in [Moving on from Terraform CDK](/blog/terraform-cdk-alternative).)

Here's what the two deploy workflows look like end to end:

Width = elapsed time. Solid = active work. Dim = waiting for review or verification.

Traditional IaC vs Infrastructure from Code deploy workflows.

The most obvious difference is drift. When infrastructure is derived from application code, the two can't diverge. There's no scenario where the app expects a Pub/Sub topic that Terraform forgot to create, or where a database migration references a table that hasn't been provisioned yet. The infrastructure is always a function of the code.

Terraform state goes away too. Locking conflicts, corrupted state, sensitive data in state files, the remote backend that every team configures slightly differently. IFC platforms manage state internally, so you don't deal with any of that.

The plan/apply cycle was designed for a world where infrastructure changed a few times a week. When you're deploying multiple times a day, or when an AI agent is generating services continuously, it becomes the bottleneck. With IFC, deploying infrastructure changes is the same action as deploying application code.

There's also no language switch. The infrastructure is declared in TypeScript or Go, the same language the application is written in. You're not context-switching between HCL and your application language, or maintaining YAML configs alongside your business logic.

Local development is where the difference is most tangible. With Terraform, you typically set up Docker Compose or mock services to approximate your cloud environment. With IFC, `encore run` gives you real PostgreSQL, real Pub/Sub semantics, and a [local dashboard](/docs/ts/observability/dev-dash) with distributed traces, API explorer, and database browser. No configuration needed.

The file structure reflects all of this:

Agent output with Terraform

Agent output with Encore

security-groups.tf28 lines

docker-compose.yml32 lines

1\_create\_tables.up.sql8 lines

Same system, different project structures.

We wrote about this transition in more detail in [The Last Year of Terraform](/blog/last-year-of-terraform).

IFC isn't free of constraints. Adopting it means:

**You use the framework's patterns.** Infrastructure declarations follow the framework's conventions: `new SQLDatabase()`, `new Topic()`, etc. Your business logic is standard TypeScript or Go (roughly 99% of the code), but the infrastructure surface uses the framework's APIs. You can [generate Docker images](/docs/ts/self-host/build) with `encore build docker` and deploy anywhere, so you're not locked into a specific hosting platform.

**Language constraints.** [Encore](https://encore.dev) supports TypeScript and Go, which is where most backend development is happening, but if your team uses Python, Ruby, or Java, the IFC options are more limited today.

**Less granular control over individual resources.** Terraform lets you configure every parameter of every resource. IFC abstracts the resource-level details, with the platform handling configuration based on environment settings. For most teams this is a feature (fewer things to get wrong). Some teams need fine-grained control over specific resources and will find the abstraction too opaque.

What you get in return: no state files to manage, no drift between application and infrastructure, no plan/apply cycles, no Docker Compose files that approximate production, and less coordination overhead between application developers and platform engineers.

The separation between application code and infrastructure code made sense when both were written by humans at a similar pace, but a growing share of application code is now generated by AI, and the infrastructure layer is what determines whether that code actually runs or sits waiting for someone to write the Terraform.

We published a whitepaper, [Backend Development 3.0](https://encore.cloud/library/backend-development-3-0), that goes deeper into the data behind this shift: DORA findings on AI adoption, infrastructure maturity models, and what the transition path looks like for teams moving off Terraform.

For teams already using AI to write application code, the infrastructure workflow is usually the thing that hasn't caught up yet. IFC is one way to close that gap.

**Want to see it in action?**
We'd love to show you how Encore works with your AI tools of choice. [Book a 1:1 intro](https://encore.cloud/book), no pressure, just a conversation.