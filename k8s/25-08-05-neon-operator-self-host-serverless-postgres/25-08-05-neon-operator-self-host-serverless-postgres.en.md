## Here we go!

We're happy to announce an early version of <https://github.com/molnett/neon-operator>, a Kubernetes operator that allows you to self-host Neon on your own infrastructure. This is the culmination of our efforts to understand the internal details of Neon, and we're excited to share our findings with the community.

We're slowly growing a community of people and companies who are interested in building this, with some major players already joining the effort. The hope is that publishing this operator will bring forth a wave of platform builders that are as interested in disaggregated architectures as we are.

If you feel the same, please reach out to me on [X](https://X.com/jonathangrahl) or Discord @bittermandel, I would love to chat!

### Recognition well deserved

None of this would be possible without the relentless effort of the team at Neon. They have done amazing work making an OSS product that is feasible to self-host at scale. The architecture that they have designed allows us to confidently build a control plane ourselves without competing with Neon Cloud (which would require a substantial VC-funded effort). A win-win situation in my eyes!

The reason why it's worth noting is that it's extremely uncommon that OSS databases have features that allow you to reasonably self-host a larger cluster. Clickhouse is a counter-example of that, as they deliberately keep features like SharedMergeTree closed-source, which is what allows them to run ClickHouse in a multi-tenant environment with shared storage and separated compute, similarly to Neon.

### The elephant in the room

There are plenty of relentless posts on X about how bad Neon is from a small group of larger accounts with a substantial audience. My personal opinion is that it's quite tiring to even observe the negativity, which seemingly is just for clout at this point. I understand much of it is for marketing reasons, and it's definitely working. But at what cost?

In terms of what actual reliability problems Neon might have, we are confident this is related to Neon Cloud's unique load patterns rather than a fundamental achitectural or code quality issue.

At Molnett, we're still just as eager to run Neon as we've always been. There is no other option that is built with the same type of architecture, so we've got to make it work either way! Skin in the game, as they call it.

### How it works

The operator utilizes three separate CRDs (Cluster, Project, Branch) to deploy the necessary components to run a full cluster. The Cluster resource must be configured with a S3-compatible object storage, a pre-existing Postgres instance and locally-attached disks (NVMe recommended). What you end up with is a cluster of Safekeepers, Pageservers, and auxiliary components.

The Project and Branch (internally called Tenant and Timeline) resources are equivalent to the Neon Cloud Project and Branch. Creating these resources results in a fully functional Postgres instance being spawned, ready to be used as needed!

Attached to the operator is an API which communicates directly with the Storage Controller (the orchestrator in Neon) to assign new timelines (branches) to specific pageservers and safekeepers.

In case of node failures, compute nodes are automatically configured to communicate with a potentially new set of pageservers and safekeepers. This allows the operator to manage sharding and failovers without requiring human intervention.

You can read more about the architecture here: <https://github.com/molnett/neon-operator/>

### Why Rust and kube-rs

The intention is for the operator to directly depend on the `neondatabase/neon` repository for API clients, protobufs and other types. This is not possible today as Neon does not publish their crates, and utilizing a git dependency in Cargo is not possible as they have multiple versions of postgres as submodules.

We're intending to contribute a solution to this upstream, likely through publishing some of the crates. The benefit of not having to copy or vendor code to ensure compatibility shouldn't be understated for a system like this, so we will do our best to make it work.

It is true though that Rust might not be the best alternative. kube-rs is significantly less feature-rich than kubebuilder, not having `envtest` is a problem for integration testing, **and** Rust is famously hard to learn.

We will see in a few months how Rust and kube-rs work out for us. We're still in the early stages of development, so we're open to feedback and suggestions.

### What's next

I am currently working full-time on finishing a production-ready release, which would allow us to deploy Neon to production at Molnett and start validating the correctness and day two operations in a realistic setting.

To reach that milestone, these are some of the improvements we will have to implement:

* A management layer for configuring databases and users through the control plane
* Drain and fill operations for Pageservers
* Deploying PGBouncer together with Compute to allow access to the databases
* Basic observability support for monitoring and alerting purposes

### Looking for collaborators

Are you looking to deploy Neon locally? Or to collaborate milestone described above? Reach out to me on [X](https://X.com/jonathangrahl) or Discord @bittermandel, or create issues on [GitHub](https://github.com/molnett/neon-operator).

And if you'd like to try out Molnett, you can sign up on <https://console.molnett.com> and we'll be in touch!