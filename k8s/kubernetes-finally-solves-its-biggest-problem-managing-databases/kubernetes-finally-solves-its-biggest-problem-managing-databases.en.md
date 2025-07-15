Running and managing stateful workloads such as databases on Kubernetes is notoriously difficult. The declarative model maps cleanly to manage things like Pods and Secrets, which can be replaced and swapped, but not so much to things that must evolve without shutting down, like your favorite PostgreSQL instance. Thankfully, there are recent developments in the Kubernetes ecosystem that finally make managing such workloads within reach.

Resource management is all about maintaining a desired state for a system. For modern, cloud native applications, this state can be very complex.

Even small teams can manage thousands of distinct resources, including VPCs, security groups, EC2 instances, Kubernetes objects, load balancers, secrets, databases, CI/CD pipelines, and more. It’s no longer just “running an app” on some server. It orchestrates a sprawling ecosystem of interdependent components, each with its own life cycle, configuration, and constraints.

This explosion in complexity was bad news for many. It amplified the risk of configuration drift, made [observability and troubleshooting](https://thenewstack.io/kubernetes-troubleshooting-primer/) more complex, and created more opportunities for state inconsistencies across environments. Teams struggled to keep all the moving parts in sync, especially as they scaled.

These challenges gave rise to new paradigms that now dominate the cloud native world. And surprisingly, one of the core inspirations behind these modern practices comes from an unlikely place: your air conditioner.

## Why Kubernetes Database Management Was Previously Impossible

It might sound odd at first, but air conditioners offer a surprisingly good mental model for a powerful pattern in modern infrastructure management.

Let’s break it down. An A/C unit doesn’t just blow cold air — it maintains a desired state: a target temperature. To do this, it runs a simple but effective feedback loop:

* A thermostat continuously senses the current temperature.
* A controller compares this to the desired temperature.  
  If there’s a difference, it triggers the system to cool more, less, or not at all.

No one sits there adjusting the knobs manually every few minutes. The system operates autonomously, responding to changes in the environment and continually working to bring it back into line with the goal.

This is the essence of what’s known as a reconciliation loop — and it’s the foundation of one of the most successful models for managing complex infrastructure at scale.

Once you see the A/C metaphor, you start to see reconciliation loops everywhere, especially in cloud infrastructure:

* Auto Scaling Groups: Continuously monitor metrics such as CPU or memory usage and add or remove instances to maintain a target utilization.
* Circuit Breakers: Track error rates in service calls and adjust routing or reject requests when failure thresholds are crossed, then recover when conditions stabilize.
* Kubernetes Controllers: Monitor changes in declared resources (such as Deployments or StatefulSets) and automatically reconcile the system to ensure consistency.

This model — define a desired state, observe the actual state, and reconcile the difference — scales beautifully.

I’ve seen clusters with thousands of nodes and tens of thousands of pods running production workloads, all stitched together by reconciliation loops. No one SSHs into nodes to restart failed services. No one [runs ad-hoc scripts](https://thenewstack.io/want-real-time-run-scripts-inside-the-database/) to rebalance traffic. The system observes, reacts, and heals itself continuously.

That’s the magic of control loops: They aren’t just automation. They’re autonomous.

They provide us with infrastructure that responds to failure, handles change safely, and continues to move forward without requiring constant oversight at every step.

## The Air Conditioner Model: How Reconciliation Loops Changed Everything

But as with all good things in software… there’s a catch.

Reconciliation loops work brilliantly for stateless infrastructure. That’s why Kubernetes excels at managing resources like pods, services, and configurations. Need to update your app? Just change the image tag, and Kubernetes will spin up new pods, wait for them to become healthy, and gracefully replace the old ones. Rollouts, rollbacks, health checks — all baked in. It’s elegant, safe, and hands-off.

However, this model begins to break down when applied to stateful resources.

Industry veterans, such as Kelsey Hightower, have long warned about this. Running a state on Kubernetes, especially a critical state like a production database, opens a very different set of problems.

Let’s take an example: Say you have a pod running a PostgreSQL 16 instance, and now you want to upgrade to version 17.

What do you do?

* Shut down the old pod? That’s downtime.
* Spin up a new pod with the 17 image and point it at the same PVC? Risky — data formats may have changed.

Hope for the best? Probably not a strategy your SRE team will endorse.

If you dive a bit into PostgreSQL upgrade instructions — or have had the joy of doing this in production — you’ll find that a safe, zero-downtime upgrade usually involves a carefully choreographed sequence. A common strategy goes something like this:

1. Provision a new PostgreSQL instance (e.g., v17) alongside the existing one (v16).
2. Pre-create a compatible schema on the new instance. Since logical replication requires schemas to match, this step must be done before replication can begin.
3. Set up logical replication from the old instance to the new one, capturing changes in real time.
4. Monitor replication lag and wait for it to drop to zero.
5. Flip traffic over to the new instance — often by updating a connection string or promoting the new node in a failover setup.

This process is deliberate and highly controlled. Trying to wedge this kind of upgrade into a stateless rollout model — like replacing a pod with a new image — is not just naive. It’s dangerous.

Take another example: schema migrations.

Every time your application evolves, chances are your [data model needs](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) to grow with it. Maybe you’re adding a column, changing a type, or restructuring a table. If the schema isn’t compatible with the new application version, some queries may start to fail, causing runtime errors, broken features, or even outages.

So what happens if we try to apply the same stateless rollout model to a database schema change?

Let’s imagine: You modify your app, and now you want to “roll out” a new schema version. You might think — just like with Deployments — of spinning up a new database pod with the updated schema, waiting for it to become healthy, then switching traffic over and deleting the old one.

But a database isn’t a stateless pod.

A fresh database with the “correct” schema may look healthy until you realize it’s empty because no data was migrated.

Trying to apply that new schema directly to the existing database? That often fails outright — perhaps a table already exists, or a column conflict prevents the change from being made. And even when it does succeed, it can silently break things: maybe a column was dropped or a constraint added, and now your [app is throwing runtime](https://thenewstack.io/kubernetes-for-developers-with-a-distributed-app-runtime/) errors under real traffic.

Unlike stateless workloads, you can’t just retry a failed deployment. Databases hold a persistent, irreversible state. Schema migrations are often non-idempotent, and a poorly designed one can [bring your system](https://thenewstack.io/edgeless-systems-brings-confidential-computing-to-kubernetes/) down — or worse, corrupt data without immediately showing symptoms.

Worse still, traditional Kubernetes patterns — such as running migrations in an init container or bundling them into app startup — introduce race conditions, create fragile deployments, and make it difficult to observe, verify, or roll back what happened.

Even when done well, these approaches rely on a pre-scripted, linear sequence of DDL statements — a fixed plan for a one-way change. That’s fundamentally different from a reconciliation loop. There’s no sensing, no diffing, no reacting to the current state. It’s imperative, not declarative.

Clearly, we need a different model.

## Kubernetes Operators: The Game-Changer for Database Management

If reconciliation loops are so effective for stateless infrastructure, the question is: Can we extend the same idea to stateful resources?

This is precisely what the Kubernetes Operator pattern aims to achieve.

Operators are purpose-built controllers that extend Kubernetes to manage complex, domain-specific, stateful resources, like databases, message brokers, or storage systems. They encode [operational knowledge into software](https://thenewstack.io/how-to-cut-through-a-thicket-of-kubernetes-clusters/), enabling how to install, configure, upgrade, and monitor these systems while maintaining a desired state.

In other words, they bring reconciliation to the stateful world.

## The Core of Every Operator

At the heart of the Operator pattern are two Kubernetes primitives:

* Custom Resource Definitions (CRDs): These extend the Kubernetes API with new resource types. Just like Deployment or Service, you can define a PostgresCluster, KafkaTopic, or in our case, a DatabaseSchema. CRDs let you describe the desired state of something that Kubernetes doesn’t natively understand.
* Controllers: These are the agents that monitor custom resources and take action. They monitor the actual state of the system, compare it to the desired state defined in the CRD, and perform the necessary operations to reconcile the two.

Together, CRDs and controllers form a self-healing loop for tasks that previously required manual intervention or brittle scripts.

Just like how the Deployment controller reconciles pods, an Operator can reconcile the state of a PostgreSQL cluster, a Kafka topic, or even a database schema.

And unlike shell scripts or CI jobs, Operators can make decisions. They don’t just execute — they observe, plan, and react to the environment.

## CloudNativePG and Atlas: Production-Ready Database Solutions

Now that we understand the power of the Operator pattern, let’s look at how to apply it to a real-world use case: managing PostgreSQL schema changes on Kubernetes — declaratively, safely, and with zero scripting.

We’ll use two powerful Kubernetes-native tools:

* [CloudNativePG (CNPG)](https://cloudnative-pg.io/): A production-grade operator for running PostgreSQL clusters on Kubernetes. It handles provisioning, replication, failover, and even backups.
* [Atlas Operator](https://atlasgo.io/): A schema management operator from Ariga that introduces an AtlasSchema CRD, allowing you to declare your desired schema and automatically apply the changes in a safe, policy-aware way.

Together, these tools let you manage both your database infrastructure and your schema lifecycle in a GitOps-native way.

Let’s walk through the setup.

## Step-by-Step: Implementing Declarative Schema Management on Kubernetes

Step 0: Install CloudNativePG and Create a Cluster

First, install the [CloudNativePG operator](https://cloudnative-pg.io/) and spin up a PostgreSQL cluster.

Add the Helm repo and install the operator:

```
bash
CopyEdit
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm repo update
helm install cnpg cnpg/cloudnative-pg
```

Next, define your cluster. Save the following as cluster.yaml:

```
yaml
CopyEdit
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: cluster-example
spec:
  instances: 1
  imageName: ghcr.io/cloudnative-pg/postgresql:15
  storage:
    storageClass: standard
    size: 1Gi
```

Apply it:

```
bash
CopyEdit
kubectl apply -f cluster.yaml
```

This will:

* Create a PostgreSQL database named app.
* Provision a user named app.
* Generate a Kubernetes Secret called cluster-example-app with the credentials.
* Expose a read/write service at cluster-example-rw.default.

Once the pod (e.g. cluster-example-1) is up and running, you’re ready to move on.

**Step 1: Install the Atlas Operator**

Now install the Atlas Operator via Helm:

```
bash
CopyEdit
helm install atlas-operator oci://ghcr.io/ariga/charts/atlas-operator
```

You should now see Atlas CRDs registered in your cluster:

```
kubectl get crd | grep atlas
```

Output:

```
atlasmigrations.db.atlasgo.io
atlasschemas.db.atlasgo.io
```

**Step 2: Apply a Schema**

Use the AtlasSchema resource to declaratively define your database schema. Save the following as atlas-schema.yaml:

```
yaml
CopyEdit
apiVersion: db.atlasgo.io/v1alpha1
kind: AtlasSchema
metadata:
  name: atlasschema-pg
spec:
  credentials:
    scheme: postgres
    host: cluster-example-rw.default
    user: app
    passwordFrom:
      secretKeyRef:
        key: password
        name: cluster-example-app
    database: app
    port: 5432
    parameters:
      sslmode: disable
  schema:
    sql: |
      create table t1 (
        id int
      );
```

Apply it:

```
bash
CopyEdit
kubectl apply -f atlas-schema.yaml
```

Check the reconciliation status:

```
bash
CopyEdit
kubectl get atlasschemas.db.atlasgo.io
```

Expected output:

```
pgsql
CopyEdit
NAME               READY   REASON
atlasschema-pg     True    Applied
```

**Step 3: Verify and Evolve**

You can verify the result directly:

```
kubectl exec -ti cluster-example-1 -- psql app
```

Inside the psql shell:

```
\dt
\d t1
```

To evolve your schema, just edit the sql: field in your manifest — e.g., add a column:

```
create table t1 (
  id int,
  name text
);
```

Then re-apply:

```
kubectl apply -f atlas-schema.yaml
```

The Atlas operator will detect the diff and apply the migration safely.

This gives you full declarative schema management with:

* Built-in access to database credentials via Kubernetes Secrets.
* Schema reconciliation is handled continuously by the operator.
* No imperative migration scripts or manual steps.

A truly GitOps-native approach to schema change management.

## Key Takeaways

* Reconciliation loops are the backbone of cloud-native infrastructure. They work incredibly well for stateless resources — and with the Operator pattern, they can work for stateful ones too.
* Traditional approaches to managing stateful systems like databases break down in Kubernetes. Tools like init containers, CI jobs, and manual scripts don’t align with the declarative, autonomous model we’ve come to expect.
* Operators bring the power of Kubernetes to stateful systems. With CRDs and controllers, you can manage complex resources — like PostgreSQL clusters and schemas — the same way you manage Deployments and Services.
* Atlas and CloudNativePG make end-to-end, GitOps-friendly database management possible. From provisioning to migrations, you can now express and evolve your database infrastructure and schema entirely through Kubernetes-native workflows.

## Why This Matters

As Kubernetes becomes the control plane for everything, state can’t be the exception.

For too long, databases have been treated as untouchable snowflakes — segregated from the rest of our infrastructure automation. However, to achieve truly modern, scalable, and repeatable systems, we must integrate them into the same workflows we use for everything else.

The Operator pattern — and tools like Atlas — help make that vision a reality.

It’s time to make an operator of all the (stateful) things.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/01/27b46b16-rotemtam_profile.png)

Rotem Tamir, co-founder and CTO of Ariga. Co-creator and maintainer of Atlas, an open-source tool that lets you manage your database schema as code. Co-maintainer of Ent, the Linux Foundation-backed entity framework for Go. Ex-infra team lead at ironSource, ex-data...

Read more from Rotem Tamir](https://thenewstack.io/author/rotemtamir/)

[![](https://thenewstack.io/wp-content/uploads/2025/06/c8ac9e06-gb-600x600.jpg)

Navigating the uncharted waters of PostgreSQL within Kubernetes using open-source technologies, I bring a wealth of expertise to the table as a KubeCon speaker, Data on Kubernetes Community Ambassador, maintainer of the CloudNativePG Operator, and author of Postgres books. My...

Read more from Gabriele Bartolini](https://thenewstack.io/author/gabriele-bartolini/)