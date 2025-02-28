Feb 28, 2025

5 Min Read

Every engineering team's success hinges on making the right infrastructure choices early.

When resources are tight and speed matters, choosing the right cloud infrastructure approach can make or break your team's success.

The wrong choice can drain your engineering bandwidth for months; the right one can be the foundation for rapid, sustainable growth.

When it comes to cloud infrastructure, teams typically face three main approaches, each with significant trade-offs:

**Traditional PaaS (Heroku, Supabase, Firebase)**- Quick to start with managed services, but locks you into their ecosystem
- Restricted to platform-specific add-ons, difficult to integrate with other cloud services
- Limited support for multiple environments and local development
- Best for simpler apps that fit within platform constraints
**Infrastructure-as-Code (Terraform, Pulumi)**- Maximum control and cloud provider access
- Requires writing thousands of lines of configuration (a single AWS ECS setup needs 500+ lines)
- Needs dedicated DevOps expertise to maintain
- Manual work needed to wire services together (VPCs, security groups, IAM roles)
- Full access to cloud provider features
**Deployment Platforms (Northflank, Fly, Railway)**- Focused primarily on container deployment and basic databases (Northflank goes beyond this with Kubernetes support)
- Often limited integration with cloud-native services (no direct AWS/GCP service access)
- Simple pricing but less cost-effective at scale (Render charges $7/service/month minimum)
- Basic monitoring and logging capabilities
This trade-off between flexibility and simplicity is the challenge we're trying to solve at Encore.

Our approach is to combine an [open source backend development framework](https://github.com/encoredev/encore), with a SaaS based platform for cloud automation ([Encore Cloud](https://encore.cloud)).
This combination provides PaaS-like deployment simplicity and powerful developer productivity features, while maintaining the flexibility of running everything in your own cloud account (AWS/GCP).

This means Encore sits between these categories, offering a different blend of features:

- Like PaaS, it fully automates infrastructure and cloud deployment.
- Like IaC, it allows you to use your own cloud provider and powerful infrastructure services like Kubernetes, but without the any of the manual overhead and complexity of Terraform.
- Unlike any of the above, it integrates with your dev workflow to provide developer experience and productivity features, like built-in API generation, service discovery, API documentation and service catalog, and observability with distributed tracing.
Unlike traditional PaaS, Encore Cloud doesn't host your applications. Your infrastructure stays in your own AWS or GCP account, so you never lose control.

Encore's open source CLI provides the tools needed to build your application as a Docker container, so you can deploy it anywhere.

If you choose to use [Encore Cloud](https://encore.cloud) to fully automate your infrastructure and deployment, you still use your cloud account with AWS or GCP, so you own your infrastructure and data from day one.

Migrating away from Encore Cloud means you can keep running your application and only need to take over the CI/CD and infrastructure management process.

Encore's declarative infrastructure framework is [open-source](https://github.com/encoredev/encore) with a minimal footprint, 99% of your code is regular TypeScript or Go code.
This means developers don't need to learn very much to start using Encore, and you can still use the tools and libraries you're familiar with.

Migrating away from the framework is also straightforward, since the footprint is limited to the edges of your application.

For example, here's how you can define an API endpoint from a regular TypeScript function, by just wrapping it with the `api`
function:

```
// Normal TypeScript function
export const getBlogPost =
async (req: { id: number }): Promise<BlogPost> => {
// ...
};
// API endpoint
export const getBlogPost = api({ method: "GET", path: "/blog/:id" },
async (req: { id: number }): Promise<BlogPost> => {
// ...
}
);
```
No complex Terraform scripts or Kubernetes manifests are required, you can just write regular TypeScript or Go code and use the framework to wrap your functions to create APIs, or use single lines of code to define your infrastructure like databases and Pub/Sub.

For example, here's how you can define a PostgreSQL database in a single line of code:

```
import { SQLDatabase } from "encore.dev/storage/sqldb";
const db = new SQLDatabase("userdb", {migrations: "./migrations"});
// ... use db.query to query the database.
```
This is all that's needed for Encore to run your application and infrastructure for local development, and automate provisioning and deployment to the cloud.

It works by parsing your code and automatically generating the necessary infrastructure definitions, then using your cloud provider's API to provision and manage the infrastructure.

Encore Cloud handles setting up all the underlying infrastructure complexity, including:

- Security group configurations
- Network routing and VPC setup
- IAM roles and permissions
- Database connection pooling and credentials management
- And more
In local development, Encore's open source CLI will automatically start the infrastructure services using local equivalents and wire them into your application.

Unlike all other tools in this comparison, Encore provides all the developer platform tooling required for productive distributed systems development, including:

- Auto-generated API documentation
- Service Catalog
- Generated architecture diagrams
- Distributed Tracing
- Local development setup
- Preview environments per pull request
This saves you months of setup time and the cost of hiring platform engineering expertise to maintain your own custom developer platform.

The days of choosing between convenience and control are over. With Encore, we aim to provide you with the power of modern cloud automation while keeping full ownership of your infrastructure.

If you're looking for a new tool to make cloud development faster, simpler, and more flexible, we hope you'll give Encore a try.

**Want to see how it works?** Check out the [docs](https://encore.dev/docs), join us on [Discord](https://encore.dev/discord) to ask questions, or [Book a demo](https://encore.dev/book) for a 1:1 introduction.
Our Story

01/15/25 / 3 Min Read

Designing tools for developers means designing for LLMs too

How we used LLMs to produce instructions for LLMs to build Encore applications.

Launch Week

12/13/24 / 3 Min Read

Worker Pooling — 5x performance for CPU-intensive JavaScript workloads

Launch Week Day 5

Launch Week

12/12/24 / 3 Min Read

Advanced Validation in Encore.ts

Launch Week Day 4