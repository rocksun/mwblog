# The Technical History of Kubernetes
I wasn’t able to attend Kubecon in 2024, but the 10th anniversary of Kubernetes was commemorated at KubeconEU and again [in June](https://www.youtube.com/watch?v=jYjEWlnY25M&t=8777s), where I talked about [the Road to 1.0](/kubernetes-the-road-to-1-0-525a9420fdf0). You may also be interested in some of [my other Kubernetes-related posts](https://medium.com/@bgrant0607/list/kubernetes-8b0b8930195b).

We actually started work on Kubernetes back in 2013, and Kubernetes was based fairly directly on R&D that was done over the few years leading up to that. Of course, there were precursors farther back, including Linux Containers, Borg, Workqueue, and Babysitter, but I’m going to focus on efforts I was directly involved with. Five years ago I wrote a series of threads on Twitter for the 5th anniversary. I finally made the time to post a blog based on those threads (still with Twitter-sized paragraphs). I updated some of the links and added some punctuation, but otherwise didn’t edit it much. Hopefully this makes it easier to find than dozens of separate Twitter posts.

[ Kubernetes Borg/Omega history topic 1](https://twitter.com/bgrant0607/status/1102292629465661440): Pods. In Borg, Job Tasks were scheduled into Alloc instances, but almost everyone pinned groups of tasks into each instance. Often these were sidecars, such as for logging or caching.
It was clear that using such groups as the explicit primitive would be simpler. We called these “Scheduling Units”. They were prototyped in Borg, but it was too hard to introduce new concepts. They became “SUnits” in Omega, and then Pods, as in a pod of peas or of whales, in K8s.

We debated whether to embrace the containers-as-lightweight-VMs trend early in Kubernetes and just support one container per pod (initially called Tasks in the code), but I’m glad we didn’t. One app per container unlocks the potential for more intelligent management.

It enables Kubernetes and other systems to observe which apps are running (from their images), when and why they fail, how much CPU and RAM they are using, etc. And, importantly, enables images to be generated as part of the build process rather than during deployment.

And, something that’s often overlooked, a Pod shares a network identity, storage volumes, and other OS and machine resources. This makes it easier to migrate to from VMs.

We started to work on what became the Kubernetes API in October 2013, before we had settled on Open Source or just a hosted/managed cloud project. Exploration intensified in early 2014, a few team members started to work on libcontainer, and the container-agent was released in May 2014.

[ Kubernetes Borg/Omega history topic 2](https://twitter.com/bgrant0607/status/1104435451757125633): Labels. Borg had Machine key/value attributes that could be used in scheduling constraints. Borgmon had target labels to convey application topology, environment, and locale. But Jobs themselves didn’t originally have k/v labels.
So Borg users would embed attribute values in Job names, separated by dots and dashes, up to 180 characters long, and then parse them out in other systems and tools using complex regular expressions.

It was clear that load balancers, monitoring systems, and release, rollout, and configuration tools needed common support for identifying attributes that could flow through the entire lifecycle of an application. However, single-value tags, as in gmail and GCE, were missing types.

Thus, in mid 2013, we proposed key/value labels, for both Borg and Google Cloud, to facilitate higher-level application management. Of course, it was much easier to incorporate them into a greenfield project like Kubernetes, which had labels from the beginning.

Label selector semantics were designed originally for the monitoring system. Monitoring and load-balancing systems wanted to ensure that non-overlapping queries could be constructed. Without disjunction, a common key with different values ensures two selectors don’t overlap.

Selectors are also simple enough they could be reverse-indexed, which could be used by watch to find outstanding queries matching labels of a new/changed resource instance. But we haven’t implemented this yet in K8s ([https://github.com/kubernetes/kubernetes/issues/4817](https://github.com/kubernetes/kubernetes/issues/4817)).

Another thing we haven’t implemented yet that SREs asked for in the original design is a way to default, require, prohibit, and validate label keys and values: [https://github.com/kubernetes/kubernetes/issues/15390](https://github.com/kubernetes/kubernetes/issues/15390).

[ Kubernetes Borg/Omega history topic 3](https://twitter.com/bgrant0607/status/1106651847962443776): Annotations. Borg’s Job type had a single notes field. Like the DNS TXT record, that proved insufficient. For example, layers of client libraries and tools wanted to attach additional information.
Some users found other creative places to carry information, such as scheduling preferences, in which arbitrary key/value strings could be stored. Arbitrary protobuf extensions were eventually supported.

That’s a common theme in many parts of the Kubernetes API: consider when multiple values or key/value pairs may be needed rather than just singleton values. I proposed annotations in [https://github.com/kubernetes/kubernetes/issues/1201](https://github.com/kubernetes/kubernetes/issues/1201).

Annotations provided a place to store the configured state for apply, as discussed in [https://github.com/kubernetes/kubernetes/issues/1178](https://github.com/kubernetes/kubernetes/issues/1178) and [https://github.com/kubernetes/kubernetes/issues/1702](https://github.com/kubernetes/kubernetes/issues/1702), and subsumed Openshift’s description field, in the v1beta3 API overhaul ([http://prs.k8s.io/1225](http://prs.k8s.io/1225)).

Some believed that having 2 kinds of key/value string metadata, labels and annotations, would be confusing, so I put some effort into clarifying the distinction in documentation early on, such as in [https://github.com/kubernetes/kubernetes/pull/1817](https://github.com/kubernetes/kubernetes/pull/1817). I think unifying them would have reduced usability.

[ Kubernetes Borg/Omega history topic 4](https://twitter.com/bgrant0607/status/1109121268534505472): Workload controllers. Before I get into the history, some conceptual background may be useful, since the underpinnings come up in many Cloud Native contexts. The key is to explicitly model state such that it can be externally manipulated.
Around the time Kubernetes was open sourced, there were a number of libraries and tools created to start containers on multiple machines. The original libswarm was one. The problem with such imperative, client-side approaches was that it was hard to add automation.

One could inject a scheduler in between, by emulating a single machine’s remote API, but that would still lack an explicit model of what the user was trying to instantiate, the equivalent of the Pod template in Kubernetes.

That was added by some other tools, but the lack of also modeling the set of instances, with an explicit replica count, was an obstacle to higher-level automation, such as horizontal autoscaling and progressive rolling updates, both of which Kubernetes added in 1.1 and 1.2.

Kubernetes originally just supported one workload controller, the ReplicationController, which was designed for elastic stateless workloads with fungible replicas. Shortly after we open-sourced Kubernetes we started to discuss how to add support for additional kinds of workloads.

In [https://github.com/kubernetes/kubernetes/issues/1518](https://github.com/kubernetes/kubernetes/issues/1518), we started to discuss what became DaemonSet. The key decision was whether to add more functionality to ReplicationController or to create new resource types. Users of other systems were concerned about the complexity of using multiple types.

Borg had supported just one workload “controller”, the Job. (I’ll address the differences between Borg’s synchronous state machine and the Kubernetes async controllers later.) It’s described well by the Borg paper: [https://ai.google/research/pubs/pub43438](https://ai.google/research/pubs/pub43438).

Job, an array of Tasks, is used for elastic services, agents that ran on every node, batch workloads, and stateful workloads. Consequently, it has a large number of settings, and additional, external controllers are needed in order to support these different workloads.

For instance, for the daemon use case, a special controller / autoscaler is needed to ensure that the Job has a sufficient number of Tasks to cover all the machines, and cases where machines are removed from the middle of the array require special handling.

And not only is Job is the first-class primitive rather than Tasks, but each Task has a stable identity, as with StatefulSet in Kubernetes. That overly constraining not just for daemons, but also for autoscaled workloads, CI workloads, graceful termination, debugging, etc.

Job also includes published BNS records for tasks, which is the rough equivalent of Endpoints in Kubernetes. BNS records are stored in Chubby, where they can be watched. (I’ll cover watch in K8s more generally later.)

The decoupling of Pod, workload controllers, and Endpoints, and a precedent for multiple workload controllers in Kubernetes has proven very flexible, for supporting many, many types of workloads. There are now many application-specific workload controllers (aka Operators).

Explicitly representing the PodTemplate as a separate object, as proposed in [http://issues.k8s.io/170](http://issues.k8s.io/170), may also have been useful for these third-party controllers, but in practice the lack of support for that hasn’t been a huge obstacle. (Well, the API exists, but is unused.)

I proposed the idea of modeling workload controllers as loosely coupled sets of instances grouped using a label selector in June 2013, based on an 11-page analysis of Borg Job use cases, around the same timeframe as the original labels proposal.

That partly inspired replicapool.googleapis.com also, though the lack of labels in GCE at the time made implementing the full model infeasible.
Aside on “template”: a “template” is a pattern used to make copies of the same shape. I think the Kubernetes “Pod template” usage is true to that colloquial definition, but typical CS usage implies parameterization and/or macro expansion, so maybe “prototype” would be better.

The idea of explicitly modeling state so that it can be externally controlled and observed is a key principle of Cloud Native. I originally included it in a longer form of the definition I wrote for CNCF: [https://github.com/cncf/toc/blob/master/DEFINITION.md](https://github.com/cncf/toc/blob/master/DEFINITION.md).

The principle can also be applied to workflow systems and configuration management (e.g., see [https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/declarative-application-management.md](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/declarative-application-management.md)). Embodying these as code is powerful, but with great power comes great responsibility, since it obstructs external tooling and automation.

[ Kubernetes Borg/Omega history topic 5](https://twitter.com/bgrant0607/status/1111469578603778048): Asynchronous controllers. Borgmaster had synchronous, transactional, edge-triggered state machines. We had challenges scaling, evolving, and extending them.
High-cardinality resource instances could exceed what could be done in a single transaction. Addition of new states broke clients. Unobserved changes could cause unexpected state transitions. Adding new resource types was hard, and would have had to be added to monolithic files.

As a result, when new teams worked on new functionality, such as batch scheduling and autoscaling, they built it into external components, which were asynchronous. Ingestion of status from nodes (Borglets) was asynchronous, as well. Omega embraced asynchronous controllers.

Omega represented desired state and observed state in separate records in its transactional Paxos store. This made it harder to assemble a picture of what was going on. In Kubernetes, we decided to represent status in the same object as spec, in v1beta3: [http://issues.k8s.io/1225](http://issues.k8s.io/1225).

We also fully embraced the controller model, even for Kubelet, by making Kubelets report back to apiserver ([http://issues.k8s.io/156](http://issues.k8s.io/156)) and patch status ([https://github.com/kubernetes/kubernetes/issues/2726](https://github.com/kubernetes/kubernetes/issues/2726)) so that the API could be used as the source of truth by other controllers.

Rather than rigid fine-grained state enumerations that couldn’t be evolved, we initially adopted simple basic states that could report open-ended reasons for being in each state ([https://github.com/kubernetes/kubernetes/issues/1146](https://github.com/kubernetes/kubernetes/issues/1146)), and later non-orthogonal, extensible conditions ([http://issues.k8s.io/7856](http://issues.k8s.io/7856)).

The entire system can now be described as an unbounded number of independent asynchronous control loops reading and writing from/to a schematized resource store as the source of truth. This model has proven to be very resilient, evolvable, and extensible.

[ Kubernetes Borg/Omega history topic 6](https://twitter.com/bgrant0607/status/1118268924250869760): Watch. This is a deep topic. It’s a follow-up to the controller topic. I realized that I forgot to link to the doc about Kubernetes controllers:
[https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/controllers.md](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/controllers.md).
Borgmaster had 2 models: built-in logic used synchronous edge-triggered state machines, while external components were asynchronous and level-based. More on level vs. edge triggering: [https://hackernoon.com/level-triggering-and-reconciliation-in-kubernetes-1f17fe30333d](https://hackernoon.com/level-triggering-and-reconciliation-in-kubernetes-1f17fe30333d).

One of the first things I did when joining the Borgmaster team back in 2009 was to parallelize the handling of read requests. Something like 99% of requests were reads, primarily from polling external controllers and monitoring systems.

Only BNS (analogous to K8s Endpoints) was written to Chubby, which enabled replicated caching and update notification. That enabled it to scale to much larger numbers of readers (~every container in Borg) and reduced latency, which for polling could be tens of seconds.

Watch-like notification APIs (aka sync and tail) were common for storage systems such as Chubby, Colossus, and Bigtable. In 2013, a generalized Watch API was designed so that each system wouldn’t need to reinvent the wheel. A variant “Observe” added per-entity sequencing.

We built Kubernetes upon Etcd due to its similarities to Chubby and to the Omega store. When we exposed Etcd’s watch ([https://coreos.com/etcd/docs/latest/learning/api.html](https://coreos.com/etcd/docs/latest/learning/api.html)) through the K8s API, we let more Etcd details bleed through than originally intended. We need to clean up some of those details soon.

The Kubernetes model is described here: [https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md#declarative-control](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md#declarative-control).

Some other systems use message buses for notifications. Why didn’t we? Controllers need to start from the initial state, we also don’t want them to fall behind or operate on state that’s too stale, and they need to be able to handle “missed” events — the level-based rationale.

We also wanted Kubernetes to run with a small number of dependencies, and with bounded compute and storage capacity: if we assumed a managed message bus that could store a week of events and an elastic compute platform to process them in parallel, the design would be different.

Watch works well for our typical scenario of mostly active entities with high rates of change per entity, and not a vast number of inactive entities (as opposed to, say, sales catalog entries), since it assumes access to all the relevant state. At some point, we’ll need to shard.

Systems that require a key/value store for leader election and configuration, a database for persistence, an out-of-process cache for performance, a message bus for eventing, and a store for message bus persistence (3–5 stateful components) can be painful to operate.

[ Kubernetes Borg/Omega history topic 7](https://twitter.com/bgrant0607/status/1121054924979064832): The Kubernetes Resource Model: why we (eventually) made it uniform and declarative. A topic even deeper than watch. More details can be found here:
[https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md).
Like most internal Google services, Borgmaster had an imperative, unversioned, monolithic RPC API built using the precursor to grpc.io, Stubby. It exposed an ad hoc collection of operations, like CreateJob, LookupPackage, StartAllocUpdate, and SetMachineAttributes.

Hundreds to thousands of clients interfaced with this API. Many of them were asynchronous controllers or monitoring agents, as discussed in previous threads, and there was a simple command-line tool, and two widely used configuration CLIs.

The APIs were manually mapped into the two Turing-complete configuration languages, and there was also a hand-crafted diff library for comparing the previous and new desired states. The sets of concepts, RPC operations, and configurable resource types were not easily extended.

Some extensions of the core functionality, such as for batch scheduling and vertical autoscaling, used the Borgmaster as a configuration store by manually adding substructures stored with Job objects, which were then retrieved by polling Jobs.

Others, such as for load balancing, built independent services with their own service APIs and configuration mechanisms. This enabled teams to evolve their services independently, but created a heterogeneous, inconsistent management surface.

Omega supported an extensible object model, and [@davidopp](http://twitter.com/davidopp) had proposed putting an API in front of the persistent store, as we later did in Kubernetes, but it wasn’t declarative. Separate work on a common configuration store was discontinued as Google Cloud became the focus.

GCP was comprised of independent services, with some common standards, such as the org hierarchy and authz. They used REST APIs, as the rest of the industry, and gRPC didn’t exist yet. But, GCP’s APIs were not natively declarative, and Terraform didn’t exist, either.

[@jbeda](http://twitter.com/jbeda) proposed layering an aggregated config store/service with consistent, declarative CRUD REST APIs over underlying GCP and third-party service APIs. This sort of later evolved into Deployment Manager.
We folded learnings from these 5+ systems into the Kubernetes Resource Model, which now supports arbitrarily many built-in types, aggregated APIs, and centralized storage (CRDs), and can be used to configure 1st-party and 3rd-party services, including GCP: [https://youtu.be/s_hiFuRDJSE](https://youtu.be/s_hiFuRDJSE).

KRM is consistent and declarative. Metadata and verbs are uniform. Spec and status are distinctly separated. Resource identifiers, modeled closely after Borgmaster’s ([http://issues.k8s.io/148](http://issues.k8s.io/148)), provide declarative names. Label selectors enable declarative sets.

For the most part, controllers know which fields to propagate from one resource instance to another and wait gracefully on declarative object (rather than field) references, without assuming referential integrity, which enables relaxed operation ordering.

There are some gaps in the model (e.g., [http://issues.k8s.io/34363](http://issues.k8s.io/34363), [http://issues.k8s.io/30698](http://issues.k8s.io/30698), [http://issues.k8s.io/1698](http://issues.k8s.io/1698), [http://issues.k8s.io/22675](http://issues.k8s.io/22675)), but for the most part it facilitates generic operations on arbitrary resource types.

In the next thread, I’ll cover more about configuration itself, such as the origin of kubectl apply.

BTW, when I was digging through old docs/decks, I found a diagram from the Dec 2013 API proposal. Sunit->Pod, SunitPrototype->PodTemplate, Replicate->ReplicaSet, Autoscale->HorizontalPodAutoscaler.

[ Kubernetes Borg/Omega history topic 8](https://twitter.com/bgrant0607/status/1123620689930358786): Declarative configuration and Apply. Inside Google, the most used configuration approach for Borg is the Turing-complete Borg Configuration Language (BCL). You can see a snippet of BCL on slide 7 in this deck:
[inf.ed.ac.uk/teaching/cours…](https://www.inf.ed.ac.uk/teaching/courses/exc/slides/Wilkes.pdf)
Millions of lines of BCL have been written. A fair amount of BCL was devoted to configuring application command-line flags, which was the most common way to figure server binaries, which is crazy IMO, but the practice sadly carried over to Kubernetes components.

BCL was evaluated and instantiated using the borgcfg CLI, which supports commands like up, down, and update. Logic to diff and merge, perform rolling updates, and otherwise update the live state was embedded in the tool. Logic for common generation functions was written in BCL.

This created a monolithic configuration and tool ecosystem. Even frameworks like mapreduce and services on top of Borg like BorgCron had to use BCL and borgcfg to interact with Borg. Getting-started tools generated BCL.

A Python-based language was later developed, also. It interfaced with the update logic via a protobuf that wasn’t quite the same as Borgmaster’s. Other languages, such as Ruby, weren’t used in Google. Several new Borg config languages were developed, but none were approved.

Not specifically developed for Borg use, [jsonnet.org/articles/desig…](https://jsonnet.org/articles/design.html) and [https://github.com/cuelang/cue/](https://github.com/cuelang/cue/) were inspired by BCL. [aurora.apache.org/documentation/…](https://aurora.apache.org/documentation/latest/reference/configuration-templating/) and [https://github.com/stripe/skycfg](https://github.com/stripe/skycfg) were inspired by the Python language.

Borgcfg didn’t provide configuration packages. Shared templates were unversioned and directly imported from their homes in the monorepo, which inflicted churn on their consumers. There were also no “stacks” or lifecycle directives, so a number of imperative updates were needed.

In Kubernetes, we wanted to decouple configuration authoring and generation from updates to the desired state via the API, so that users could express configuration using languages and tools familiar to them: Jinja, Python, Ruby, Javascript, Terraform, Ansible, whatever.

I wrote about this in [http://prs.k8s.io/1007](http://prs.k8s.io/1007). I also felt it needed to be possible for automation to write directly to the API and not need to update some arbitrary configuration language. To do that, we needed to be able to merge user intent and automated changes.

My initial proposal, in [http://issues.k8s.io/1178](http://issues.k8s.io/1178), was to maintain and merge 2 separate layers of desired state in the server. Resistance to that idea led to my client-side Apply proposal in [http://issues.k8s.io/1702](http://issues.k8s.io/1702). We’re finally getting server-side apply: [https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/0006-apply.md](https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/0006-apply.md).

A gotcha we ran into early in the Apply implementation was complex schema topology. Merging 2 flat maps is easy, but we unfortunately had associative lists: [https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#lists-of-named-subobjects-preferred-over-maps](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#lists-of-named-subobjects-preferred-over-maps). And also sets and undiscriminated unions (being addressed: [https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/20190325-unions.md](https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/20190325-unions.md)).

Strategic merge patch was developed so that we could diff and merge two objects containing associative lists (non-ordinal lists with index keys in values of fields within list elements): [https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/strategic-merge-patch.md](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/strategic-merge-patch.md).

I wrote an overview of the motivation and principles for the configuration design in [https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/declarative-application-management.md](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/declarative-application-management.md). The original draft of that also contained sketches of what became [https://github.com/kubernetes-sigs/application](https://github.com/kubernetes-sigs/application) and [https://github.com/kubernetes-sigs/kustomize](https://github.com/kubernetes-sigs/kustomize).

Whereas Apply facilitates collaborative config authoring between humans and machines (thanks to [@originalavalamp](http://twitter.com/originalavalamp) for that description), kustomize enables collaboration among humans, by facilitating modification of unchanged base prototype/seed configurations.

The declarative API, Apply, and kustomize facilitate maintaining configuration as YAML or JSON or proto, amenable to manipulation by tools, rather than as YAML marked up with macros, complex configuration languages, or scripts written in general-purpose programming language.

On one hand, the ~100 tools that have been developed show that the decoupling of config format and the API has worked. OTOH, it shows there are still gaps. With work like diff and dry run ([https://github.com/kubernetes/enhancements/pull/893](https://github.com/kubernetes/enhancements/pull/893)) and prune ([https://github.com/kubernetes/enhancements/pull/810](https://github.com/kubernetes/enhancements/pull/810)), we’re working to close them.

A list of tools can be found here: [https://docs.google.com/spreadsheets/d/1FCgqz1Ci7_VCz_wdh8vBitZ3giBtac_H8SBw4uxnrsE/edit#gid=0](https://docs.google.com/spreadsheets/d/1FCgqz1Ci7_VCz_wdh8vBitZ3giBtac_H8SBw4uxnrsE/edit#gid=0). I just added another 20 or so that I’ve seen.
This thread is already the longest yet, so I’ll start another later with configuration terminology: declarative vs intent, macros vs config languages, packages vs stacks, prototypes vs templates, whitebox vs blackbox, overlays, lifecycle directives, etc.

I’ve worked with [@eric_brewer](http://twitter.com/eric_brewer) for several years at Google, including on configuration, between work Omega and Kubernetes. In the second half of this podcast, Eric also briefly discusses declarative configuration: [https://softwareengineeringdaily.com/2019/04/26/cloud-with-eric-brewer/](https://softwareengineeringdaily.com/2019/04/26/cloud-with-eric-brewer/).

BTW, eventually a “production database” called [ProdSpec](https://www.usenix.org/publications/loginonline/prodspec-and-annealing-intent-based-actuation-google-production), did succeed and rolled out. Borg has converged towards a model similar to the Kubernetes Resource Model and “GitOps” (though our internal VCS isn’t git), described here: [https://youtu.be/b4PFHj9s5F8](https://youtu.be/b4PFHj9s5F8).

[ Kubernetes Borg/Omega history topic 9](https://twitter.com/bgrant0607/status/1126153226523267073): Scheduling constraints. I have volumes more to write about configuration, but will move on with history topics for now. Borg’s set of constraints grew organically over time. It started with just required memory, before multicore and NPTL.
Other resources were added: cpu, disks. Hard and soft constraints on key/value machine attributes, and “attribute limits” to limit the number of tasks per failure domain. Automatically injected anti-constraints were used to implement dedicated machines.

In Omega ([https://ai.google/research/pubs/pub41684](https://ai.google/research/pubs/pub41684)), we added the concepts of taints and tolerations in order to subsume a number of ad hoc means to prevent scheduling of most tasks and/or evict them from certain machines, and forgiveness to defer eviction.

These scheduling features made their way pretty directly into Kubernetes: [http://issues.k8s.io/168](http://issues.k8s.io/168), [http://issues.k8s.io/367](http://issues.k8s.io/367), [http://issues.k8s.io/1574](http://issues.k8s.io/1574), [http://issues.k8s.io/17190](http://issues.k8s.io/17190). [@davidopp](http://twitter.com/davidopp), who was the TL of scheduling in Borg and Omega, worked on a number of these features in K8s too.

A scheduling braindump I wrote in early 2015 ([https://github.com/kubernetes/kubernetes/issues/4301#issuecomment-74355529](https://github.com/kubernetes/kubernetes/issues/4301#issuecomment-74355529)) possibly helped to convince some that Google really was fully sharing its experience with the project. The scheduling design docs can be found in [https://github.com/kubernetes/design-proposals-archive/tree/main/scheduling](https://github.com/kubernetes/design-proposals-archive/tree/main/scheduling).

These mechanisms can be used to manage how workloads are binpacked for efficiency, spread for availability, isolated from one another for performance or reliability or security, colocated with required resources, matched with desired configurations, and manage node drains.

These scheduling primitives are pretty flexible, but if there are constraints or other policies or criteria that can’t be represented, users can use their own schedulers. In order to do that in Borg, one would have to add a constraint to a task to pin it to a specific machine.

The Omega paper compared performance of 2-level scheduling with information hiding, but one issue it didn’t mention is that the lower-level scheduler needs to implement all of the same constraints as all the upper-level schedulers, or it may never satisfy their requirements.

Anyway, while resource optimization is an important concern, there are many other considerations in decisions, such as whether container images already resident, which facilitates faster start time.

[ Kubernetes Borg/Omega history topic 10](https://twitter.com/bgrant0607/status/1131202013411176448): In honor of #KubeConEU and the 5th anniversary of open-sourcing Kubernetes, I’ll add more perspective from the Borg and Omega teams to the origin story.
Internally, Google puts a lot of emphasis on both resource efficiency and engineering efficiency. For both reasons, back in June 2013, a few months before GCE was ready to GA ([https://cloudplatform.googleblog.com/2013/12/google-compute-engine-is-now-generally-available.html](https://cloudplatform.googleblog.com/2013/12/google-compute-engine-is-now-generally-available.html)), the Borg and GCE teams started to work more closely to improve both.

The initial focus gravitated towards directly supporting features needed by Cloud in Borg so that Cloud wouldn’t need to work around the the lack of those features (see my previous comment on 2-level scheduling: [https://twitter.com/bgrant0607/status/1126153859041087488](https://twitter.com/bgrant0607/status/1126153859041087488)).

Google also spends a lot of energy constantly mitigating entropy in its internal software and infrastructure. The monorepo is one mechanism for this. It also launches many efforts to “unify” or “converge” multiple systems that co-evolve to do similar things.

In that context, 2 months later, the Unified Compute Working Group was formed by Google Cloud and Google’s internal infrastructure group, “TI”, which included Borg. The goal was to develop a proposal for a “compute platform” that could be used by both Cloud and internal customers.

It was obvious that VMs would be too cumbersome and inefficient and App Engine wasn’t versatile enough to run a wide range of internal services, such as web search and Gmail. We needed a platform that was more like Borg, that was based on containers.

There were discussions regarding how compatible it should be with App Engine and with Borg. Docker, buildpacks, and Omlet (a new node agent under development to replace Borglet) were compared. Early discussions presumed a managed service, like GCE, GAE, and Borg.

In September 2013, viewpoints of 9+ WG participants were collected and composed into a “Unified Compute PRD”, focused on serving workloads (e.g., rather than batch). That was the first time I was aware of the term “Container as a Service” being used.

In October, subgroups of the WG were formed to focus on key problems, including a container management API subgroup. In November, we pulled in more people from Borg and from Cloud to hash out a number of API details. In December, an API proposal was presented to the full WG.

At the same meeting, a proposal was made for what became the App Engine Flexible Environment ([https://cloud.google.com/appengine/docs/flexible/](https://cloud.google.com/appengine/docs/flexible/)), and a proposal to build an open-source container platform, so that we wouldn’t be “Hadooped” by other OSS projects.

That OSS container platform was Project 7. Afterward, there were several proposals from both the Borg side and Cloud side to build products with compatible APIs. Collaboration with the Borg team deepened. Borglet team members started to work on libcontainer for Docker in April 2014.

It soon became clear that other Borg team members (me [@thockin](http://twitter.com/thockin) [@erictune4](http://twitter.com/erictune4) Dawn Chen [@originalavalamp](http://twitter.com/originalavalamp) [@davidopp](http://twitter.com/davidopp) [@vishnukanan](http://twitter.com/vishnukanan)) should work on the open-source project to design and develop the Borg-like functionality. We deeply believed in the potential value to external users
So we created Kubernetes because we needed it to exist, and we believed others needed it to exist also. Looking at the other solutions available at the time (e.g., [https://github.com/tsuru/docker-cluster](https://github.com/tsuru/docker-cluster), [https://github.com/signalfx/maestro-ng](https://github.com/signalfx/maestro-ng)) and since, we made the right call.

[ Kubernetes Borg/Omega history topic 11](https://twitter.com/bgrant0607/status/1134536364823699457): PodDisruptionBudget. Google constantly performs software and hardware maintenance in its datacenters: firmware updates, kernel and image updates, disk repairs, switch updates, battery tests, etc. etc. More and more kinds over time.
Even though Borg tasks are designed to be resilient, this could get pretty disruptive. Rate-limiting maintenance tasks independently isn’t efficient if you have dozens of them, and it’s not always feasible to perform all types of maintenance at the same time.

Even if rate-limiting machine disruptions, it’s also possible for the same task to get disrupted over and over again, like a can being kicked down the road. Hence, the Safe Removal Service (aka SRSly — pronounced seriously) was developed by SRE. SRE builds lots of automation.

SRSly kept track of how often tasks of the same Borg Job were disrupted (aka evicted). Maintenance automation queried SRSly regarding all tasks scheduled on a machine before taking it out of service. This enabled Borg to provide a SLO on task disruption.

Borgmaster, however, did not know about SRSly. Instead, all critical/production workloads were changed to run with the same priority so that they wouldn’t preempt each other. Doing that for every Borg Job in the company was extremely painful — more on priority/preemption later
For Omega, we developed a model that could be applied both during task preemption to run a higher-priority task and eviction for maintenance — disruption counters. There was a time dimension that ended up not being effective due to constant changes, so we dropped it in K8s.

I think I first mentioned this in Kubernetes in my big scheduling braindump comment: [https://github.com/kubernetes/kubernetes/issues/4301#issuecomment-74355529](https://github.com/kubernetes/kubernetes/issues/4301#issuecomment-74355529). It came up again when I proposed maxUnavailable to moderate concurrent disruptions caused by updates during the design of Deployment:[https://github.com/kubernetes/kubernetes/pull/12236#discussion_r36501373](https://github.com/kubernetes/kubernetes/pull/12236#discussion_r36501373).

That discussion was forked into [https://github.com/kubernetes/kubernetes/issues/12611](https://github.com/kubernetes/kubernetes/issues/12611). Around that time, Matt Liggett ([https://github.com/kubernetes/kubernetes/pulls?q=is%3Apr+author%3Amml+is%3Aclosed](https://github.com/kubernetes/kubernetes/pulls?q=is%3Apr+author%3Amml+is%3Aclosed)) joined the GKE team from Borg SRE (woo hoo!). One of the first things Matt worked on was improving node drains: [https://github.com/kubernetes/kubernetes/issues/6080](https://github.com/kubernetes/kubernetes/issues/6080).

Together with [@davidopp](http://twitter.com/davidopp) and [@erictune4](http://twitter.com/erictune4), we folded disruption budgets into the rescheduling design proposal: [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/rescheduling.md#disruption-budget](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/rescheduling.md#disruption-budget). (Rescheduling deserves its own thread — I’ll do that one next.)

Implementation began in [https://github.com/kubernetes/kubernetes/pull/24697](https://github.com/kubernetes/kubernetes/pull/24697) and [https://github.com/kubernetes/kubernetes/pull/25551](https://github.com/kubernetes/kubernetes/pull/25551)
PodDisruptionBudget is now documented: [https://kubernetes.io/docs/concepts/workloads/pods/disruptions/](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) and [https://kubernetes.io/docs/tasks/run-application/configure-pdb/](https://kubernetes.io/docs/tasks/run-application/configure-pdb/). Try it out and give us feedback on how well it works for you. We’re looking to advance it from beta to GA: [https://github.com/kubernetes/enhancements/issues/85](https://github.com/kubernetes/enhancements/issues/85).

You can safely drain a node with kubetctl drain: [https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/). Node upgrades and the cluster autoscaler in Google Kubernetes Engine (GKE) also respect PodDisruptionBudget. The latter is documented here: [https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

Node upgrade behavior is documented here: [https://t.co/eyWfp2TZn3](https://t.co/eyWfp2TZn3)
And more about the Google SRE philosophy behind automation can be found in the SRE book: [https://sre.google/sre-book/automation-at-google/](https://sre.google/sre-book/automation-at-google/).
And the Safe Removal Service was also mentioned in Google’s “VM Live Migration at Scale” paper in VEE 2018: [https://dl.acm.org/doi/10.1145/3296975.3186415](https://dl.acm.org/doi/10.1145/3296975.3186415).

[ Kubernetes Borg/Omega history topic 12](https://twitter.com/bgrant0607/status/1140592824947109888): A follow-on to the PodDisruptionBudget topic: the descheduler (
[https://github.com/kubernetes-incubator/descheduler](https://github.com/kubernetes-incubator/descheduler)). Descheduler is more appropriate than the original term “rescheduler”, because its job is to decide which pods to kill, not to replace or schedule them.
In Kubernetes, when running on a cloud provider such as in GKE, in the case of pending pods with no existing available space to be placed, either cluster autoscaling or even node autoprovisioning ([https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/proposals/node_autoprovisioning.md](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/proposals/node_autoprovisioning.md), [https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)) can create new nodes for them.

In Borg, the rescheduler was created to defragment nodes to make room. It selected tasks to evict so that the new tasks could schedule, while also ensuring the replacements for the evicted tasks could also find new homes so as not to just cause unnecessary churn.

In K8s, the purpose of the descheduler is mainly to reshuffle pods to improve the overall distribution of pods across nodes. After some churn in a cluster due to pod terminations due to pod autoscaling, pod updates, pods for batch/CI tasks, etc., pod layout can become uneven.

A simple example: Say the cluster autoscaler ([https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)) added a new node for new pods. If those pods were due to creation of a new Deployment or ReplicaSet, they could all land on the new node if there weren’t enough space on existing nodes.

From the experience in Borg, we knew the descheduler would be needed from the beginning of the Kubernetes project. I think it was first mentioned when discussing the addition of liveness and readiness probes: [https://github.com/kubernetes/kubernetes/issues/620#issuecomment-50110653](https://github.com/kubernetes/kubernetes/issues/620#issuecomment-50110653).

This enabled us to establish a clear separation of concerns between pod creation and replacement by workload controllers, horizontal scaling by HPA, placement by the scheduler, and rebalancing across nodes and failure domains by the descheduler, which would respect PDB.

That division was discussed when designing eviction for unresponsive nodes ([https://github.com/kubernetes/kubernetes/issues/3885#issuecomment-71984989](https://github.com/kubernetes/kubernetes/issues/3885#issuecomment-71984989)) and then in issues.k8s.io/12140. The design docs can be found at [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/rescheduler.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/rescheduler.md) and [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/rescheduling.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/rescheduling.md).

Note that if churn in the cluster is sufficiently high and eviction is highly constrained due to PodDisruptionBudgets, it may not be possible for the descheduler to keep up. This is one reason why it may not be possible to achieve an “optimal” layout.

[ Kubernetes Borg/Omega history topic 13](https://twitter.com/bgrant0607/status/1145696550959509504): Priority and preemption. Some work is more important and/or urgent than other work. Borg represented this as an integer value: priority. A higher value meant a task was more important than a lower value, and should be able to displace it.
When choosing a machine for a task, the scheduler ignored lower-priority tasks for determining whether/where a task would fit, but considered the number of tasks that would have to be preempted as part of the ranking function for choosing the best machine.

Disruption budgets were never added to the scheduler, which would have been hard, but there were also concerns about performance and priority inversion. Higher-priority tasks could specify how long they would wait for lower-priority ones to gracefully terminate.

Priorities were used to ensure production/critical serving workloads could always get the resources they needed. This was essential to enabling mixed workloads to run together in the same clusters. Batch and experimental workloads ran at lower priorities, infrastructure at higher.

For a while, users tried spreading their workloads across multiple priority bands in order to be nice to other tenants — crude kind of fairness in the case of resource crunches. That resulted in preemption cascades of higher-priority tasks preempting lower-priority ones .

Batch workloads, many of which were continuous automatically submitted, primarily preempted other batch tasks, causing significant amounts of lost work. So, priorities were “collapsed” into bands such that everything in the same band was treated as the same priority.

The collapse reduced preemption, but other mechanisms were needed to ensure timely and efficient scheduling. The rescheduler ensured that pending production-priority tasks could schedule by choosing others to displace. It verified that both tasks would schedule, to avoid cascades.

Groups of batch tasks were queued and admitted to the cluster when enough resources became available to schedule them. Resource quota by priority prevented priority inflation over time. Space was left between the bands in case new bands were needed — like BASIC line numbering.

Eventually the priority values of virtually all tasks were changed to rationalize them with the new scheme, across thousands of jobs, in their configuration files, through a painstaking process. This reiterated the importance of abstracting the operational intent.

Borg’s approach is described in the Borg paper: [https://ai.google/research/pubs/pub43438](https://ai.google/research/pubs/pub43438). K8s design proposals were in [https://github.com/kubernetes/design-proposals-archive/blob/main/scheduling/pod-preemption.md](https://github.com/kubernetes/design-proposals-archive/blob/main/scheduling/pod-preemption.md) and [https://github.com/kubernetes/design-proposals-archive/blob/main/scheduling/pod-priority-api.md](https://github.com/kubernetes/design-proposals-archive/blob/main/scheduling/pod-priority-api.md). Priority in resource quota: [https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/20190409-resource-quota-ga.md](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/20190409-resource-quota-ga.md). Coscheduling: [https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/34-20180703-coscheduling.md](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/34-20180703-coscheduling.md).

Priority in Kubernetes is relatively new, and it’s still evolving. For instance, there’s an open proposal to add a preemption policy, [https://github.com/kubernetes/enhancements/pull/1096](https://github.com/kubernetes/enhancements/pull/1096), primarily to avoid preempting other pods. Borg has a similar mechanism. I’ll discuss why when covering QoS.

Waiting for preempted pods to terminate gracefully before starting newly scheduled pods creates significant complexity in the design. The scheduler then needs to model the future state, and some controller needs to watch for the space to become before starting the new pod.

The complexity of priority and preemption is primarily what drove the change for the DaemonSet controller to rely on the default scheduler to bind pods to nodes, as well as the scheduler framework proposal [https://github.com/kubernetes/enhancements/issues/624](https://github.com/kubernetes/enhancements/issues/624), so the code could be reused in custom schedulers.

I’ll cover Quality of Service (QoS) and oversubscription next. Over time, priority bands in Borg (specific hardcoded integer values) came to be used as part of the determination of QoS level, for reasons I’ll go into in that thread.

[ Kubernetes Borg/Omega history topic 14](https://twitter.com/bgrant0607/status/1153341109692588032): Computational Quality of Service (QoS) and oversubscription. What are they, why would you want them, and how is QoS different than priority? On the last point, it’s distinguishing importance and urgency.
QoS is something that wouldn’t matter if just one process were running per host system or if all the processes steadily used a constant amount of cpu, memory, and other resources. Because they vary, reserving max capacity needed for each would leave systems poorly utilized.

Oversubscription mitigates that by packing more applications onto a system than could all fit at their peak requirements. It’s kind of like a bank: not everyone can withdraw at the same time. The question is then: what happens when apps demand more resources than they can get?

With time-division multiplexing, many CPU threads can be interleaved. They can be blocked and queued by the OS, typically at the cost of context switches and waiting a few time slices. Thus there is no fixed limit to how many can be packed onto a machine. CPU is compressible.

OTOH, swapping memory pages, even to local SSD, is painfully expensive. This is why systems hosting services that need to respond with subsecond latency disable swap. Memory is considered an incompressible resource.

For simplicity, I’ll ignore resources other than CPU and memory
Compressible resources like CPU can be made available quickly by the kernel with low impact to the threads that were interrupted, provided it knows which threads urgently need the resources and which ones don’t. We call this latency sensitive and latency tolerant respectively.

Borg used an explicit attribute to indicate this, called appclass, which is described by the Borg paper: [https://ai.google/research/pubs/pub43438](https://ai.google/research/pubs/pub43438). This was translated to scheduling latency in LMCTFY: [https://github.com/google/lmctfy/blob/master/include/lmctfy.proto#L142](https://github.com/google/lmctfy/blob/master/include/lmctfy.proto#L142).

In Kubernetes, it’s inferred from resource requests and limits
In order to reallocate incompressible resources quickly, threads need to be killed, which is obviously not low impact. (For memory, in Linux this is done by the OOM killer.) This was why Borg used priority (production priority vs not) to make memory oversubscription decisions.

Borg’s resource reclamation approach is described by the paper: reservations based on observed usage were computed and oversubscribed resources (latency-tolerant cpu and non-production memory) were tallied against reservations whereas guaranteed ones used limits. Complicated.
Vertical autoscaling (VA) added even more complexity. VA changed limits, but left its own padding to provide slack for reaction time and observation of demand. Ad hoc mechanisms were added to disable limit enforcement for each resource, creating a notion similar to request in K8s.

In K8s, I wanted something simpler, to directly convey the desire for oversubscription and bursting flexibility. The discussion started way back in issues.k8s.io/147 and issues.k8s.io/168. The model we settled on was determined by looking at limits and requests.

Request==Limit implies guaranteed resources (not oversubscribed). Request<Limit implies burstable (oversubscribed). Zero request implies best effort. Borg scheduled best effort using reservation, but no throughput guarantees could be made in practice.

This is described in the resource model design ([https://github.com/kubernetes/design-proposals-archive/blob/main/scheduling/resources.md](https://github.com/kubernetes/design-proposals-archive/blob/main/scheduling/resources.md)) and the QoS proposal ([https://github.com/kubernetes/design-proposals-archive/blob/main/node/resource-qos.md](https://github.com/kubernetes/design-proposals-archive/blob/main/node/resource-qos.md)), including the mapping to OOM scores. The mapping to cgroup cpu shares is described in the pod resource design ([https://github.com/kubernetes/community/blob/master/contributors/design-proposals/node/pod-resource-management.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/node/pod-resource-management.md)).

Some work on Vertical Pod Autoscaling for Kubernetes has started: [https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/vertical-pod-autoscaler.md](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/vertical-pod-autoscaler.md). There have been proposals to implement oversubscription also ([https://github.com/kubernetes/enhancements/issues/355](https://github.com/kubernetes/enhancements/issues/355)). As for horizontal scaling, resource monitoring infrastructure is a prerequisite.

If managing cluster-level sharing using ResourceQuota and LimitRange, oversubscription can be done at that level also. The original designs were described by [https://github.com/kubernetes/design-proposals-archive/blob/main/resource-management/admission_control_limit_range.md](https://github.com/kubernetes/design-proposals-archive/blob/main/resource-management/admission_control_limit_range.md) and [https://github.com/kubernetes/design-proposals-archive/blob/main/resource-management/admission_control_resource_quota.md](https://github.com/kubernetes/design-proposals-archive/blob/main/resource-management/admission_control_resource_quota.md), with improvements in [https://github.com/kubernetes/design-proposals-archive/blob/main/resource-management/resource-quota-scoping.md](https://github.com/kubernetes/design-proposals-archive/blob/main/resource-management/resource-quota-scoping.md).

Ok, this topic doesn’t fit into a Twitter form factor very well. Maybe some day I’ll get around to writing this up more in long form. For now, that’s about all I have time for, but questions are welcome.