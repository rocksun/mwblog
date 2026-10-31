**Ask a platform team what they built last year,** and the list likely includes a Kubernetes controller that creates a few objects in order and copies fields between them. No business logic, just wiring. A Deployment, a Service in front of it, and a ConfigMap whose one interesting value is the hostname the Service reports in its status. [Kubebuilder](https://book.kubebuilder.io/) turns [building the first controller](https://thenewstack.io/kubernetes-controllers-at-scale/) into a pleasant afternoon. The tenth brings its own reconcile bugs, upgrade path, and on-call rotation. It’s the same controller. It’s slightly different each time, and it exists in thousands of organizations.

## Every ingredient, no recipe

Kubernetes has the ingredients: CRDs define new types. [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) give them behavior. [Server-side apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/#field-management) tracks who owns each field. [CEL](https://kubernetes.io/docs/reference/using-api/cel/) evaluates expressions, and [OpenAPI schemas](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation) type every field. What Kubernetes does not provide is the recipe. Nothing says that several resources form one thing, or that a value in one comes from the status of another and must wait for it.

---

***KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12.*** [***Register now***](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)***!***

---

Every tool that manages a set of resources builds that piece itself, and keeps adding to it. Helm does it at render time, and Helm 4 added server-side apply and waiting on resource status. Argo CD has [sync waves, hooks](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/), and [health checks](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/) because manifests cannot say what order they need or when they are done. Crossplane has [compositions and functions](https://docs.crossplane.io/latest/composition/compositions/), and v2 composes native Kubernetes resources directly. Operators do it in Go, by hand. Strip them down and the kernel is the same: a set of objects, dependencies between them, values flowing along the edges, and something that keeps re-checking whether the cluster still matches. Each recent addition reaches for a part the tool lacked: order, readiness, per-field ownership, evaluation inside the cluster.

> “Kubernetes has the ingredients. What Kubernetes does not provide is the recipe. Nothing says that several resources form one thing, or that a value in one comes from the status of another and must wait for it.”

If everyone is building the same piece, the question is whether it should be shared. That is the position of [kro](https://kro.run/), the [Kube Resource Orchestrator](https://thenewstack.io/the-kro-project-giving-kubernetes-users-what-they-want/), and why it moved to [Kubernetes SIG Cloud Provider](https://github.com/kubernetes/community/blob/main/sig-cloud-provider/README.md#kro) in September 2025 as a primitive that other things build on, not another end-to-end platform.

## Taking the controller apart

Kro started by taking the hand-written controller apart. API mechanics and lifecycle are the same in every one; only the wiring differs. Its answer, the [ResourceGraphDefinition](https://kro.run/docs/concepts/rgd/overview/), writes the wiring down as data, and one controller interprets every definition. CRDs, OpenAPI, CEL, and server-side apply were already there, and kro connects them.

![Diagram showing parts of the glue controllers that are shared, vs those that differ.](https://cdn.thenewstack.io/media/2026/10/bbfbaa23-image.png)

A ResourceGraphDefinition holds two separable things:

1. The composition (the template with resources behind each instance and the CEL expressions to reference between them)
2. The API (a schema, the CRD generated from it, and the instances application teams create)

## The composition

kro [derives the dependency graph](https://kro.run/docs/concepts/rgd/dependencies-ordering/) from the references in CEL expressions (so order is never explicitly declared) and [type-checks every expression](https://kro.run/docs/concepts/rgd/static-type-checking/) against OpenAPI before an instance exists. The opening example’s ConfigMap needs the Service’s hostname, so its template names that field. That reference is the entire ordering rule: the ConfigMap reads from the Service, so the Service comes first, and nobody writes the order down. An explicitly declared order is a second description of a relationship the manifests already contain, and the two can disagree after any rename or reorder. An inferred order cannot drift, because it is derived rather than defined separately. The dependency is the reference. Wherever order is declared apart from the reference that needs it, there are two sources of truth, and an opportunity for drift.

## The API

A platform team writes the ResourceGraphDefinition and application teams get a Kubernetes API like any other, with kubectl, RBAC, and [GitOps working as usual](https://thenewstack.io/how-to-scale-gitops-without-hitting-the-argo-ceiling/). Ten glue controllers become ten definitions run by one controller. Wiring as data makes an API cheap to create, and a cheap API is still a promise. Application teams point manifests, RBAC, and pipelines at it, and from then on a removed field breaks something the platform team cannot see. kro [refuses a ResourceGraphDefinition schema change](https://kro.run/docs/concepts/rgd/overview/#breaking-changes) that would break existing instances unless the author explicitly allows it. The cost of an abstraction moved from writing it to owning it: ten codebases gone, ten APIs left. Teams should count APIs, not controllers.

## The primitive on its own

Once composition became cheap, people found more use-cases, and not all of it needed its own dedicated API. A default-deny NetworkPolicy in every labeled Namespace. Labeled Services folded into one Ingress. A DNS stack installed once and kept healthy. Nothing directly requests these; they react to what is already in the cluster. They are one-off definitions that do not need a repeatable API.

kro 0.10 adds a primitive for this case. A Graph is the composition piece alone; namespaced, with no schema, no CRD, and no instances. The Ingress case, abbreviated:

```

apiVersion: kro.run/v1alpha1
kind: Graph
spec:
  nodes:
    - id: services
      ref:                          # read only, never owned
        kind: Service
        metadata:
          selector: {matchLabels: {expose: "true"}}
    - id: ingress
      template:                     # created and owned
        kind: Ingress
        spec:
          rules: >-
            ${services.map(svc, {"host": svc.metadata.name + ".example.com", ...})}

```

Nobody creates an instance. The Services already exist, and the Graph follows them: label one and a rule appears; remove the label, and it goes.

![Architectural diagram comparing kro 0.9 and kro 0.10](https://cdn.thenewstack.io/media/2026/10/3c74120a-image.png)

Of the two halves, only one was ever new. The API half is a CRD, which is a primitive Kubernetes already has. ResourceGraphDefinitions make them cheaper to write, but the primitive was already there. The composition half is the piece Kubernetes lacked and every tool built for itself. Graph is that half on its own, and standing alone it shows what was easy to miss before: the API was never the input, only one kind of input. A composition reconciles against cluster state, and a new instance of a custom resource is just one of the many changes to that state it can react to. Whatever the change, the work is the kernel from earlier: objects, references between them, and a continuous declarative reconciliation loop keeping them in sync. That is the primitive. A ResourceGraphDefinition is the same primitive with a CRD in front of it.

> “Strip the trigger from anything that creates objects, copies values between them, and keeps checking, and what is left is a composition.”

The split travels. Strip the trigger from anything that creates objects, copies values between them, and keeps checking, and what is left is a composition. An operator serving one custom resource is a composition with an API in front. A pipeline stage that applies manifests in order and waits for them is a composition with a commit in front, minus the loop. A runbook that creates a Namespace, its quotas, and its role bindings is a composition with a ticket in front. Seen that way, the question is no longer which tool to adopt but where composition is already happening and what is doing it.

## Graphs in disguise

Kubernetes platforms are already full of resource graphs; they just aren’t written down as such. A naming convention so two manifests agree on a string. Sync waves or hooks that encode a dependency graph as step order. A script that copies a status field into another object. Each exists because the tool underneath cannot express a dependency between two objects, or cannot see what the cluster holds right now, so the dependency lives somewhere else such as a string, a step number, or a script. A composition tool puts it back as a reference between the objects. In kro that reference is a CEL expression continuously watched and evaluated inside a graph.

![Diagram comparing indirect resource dependency methods with direct, continuous object references.](https://cdn.thenewstack.io/media/2026/10/251ae485-image.png)

## A familiar move

Kubernetes has grown this way before. Rolling updates were a [kubectl subcommand](https://github.com/kubernetes/kubernetes/pull/88057) until the Deployment controller took them over, and everything above got simpler. Composition looks due for the same move. kro, a Kubernetes SIG Cloud Provider subproject on [GitHub](https://github.com/kubernetes-sigs/kro), shows what changes when the composition machinery becomes reusable, and the relationships become declarative. The question is bigger than any one project: if composition is what nearly every platform needs, should every platform have to build it for itself? Composition may be the primitive Kubernetes is missing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/cccb1bde-image-9-26-26-at-6.34-am-sabari-s-1.png)

Adam Crowder is a software engineer at AWS working on Amazon Elastic Kubernetes Service (EKS) and a contributor to kro. He helps lead teams focused on platform engineering and making Kubernetes easier to use and adopt. He has been involved...

Read more from Adam Crowder](https://thenewstack.io/author/adam-crowder/)