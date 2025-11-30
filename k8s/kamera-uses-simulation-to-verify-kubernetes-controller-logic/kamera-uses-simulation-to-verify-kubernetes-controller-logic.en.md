[Tim Goodwin](https://discrete.events/), a graduate student at the University of California Santa Cruz has been thinking a lot about the future of Kubernetes. And he sees a world beyond clusters, where Kubernetes can be a universal control plane for just about anything.

Making this possible is the magic of controllers, which are built on the [Kubernetes controller runtime](https://github.com/kubernetes-sigs/controller-runtime). The ability to compose controllers — and to yoke them together — is what gives Kubernetes a lot of its power,

Controllers, however, are really difficult to manage and debug. So Goodwin created a controller simulation software, called [Kamera](https://github.com/tgoodwin/kamera), which provides targeted instrumentation to capture the behaviors of individual controllers and the interactions between them, using simulation and model checking.

Kamera works with real controller code, and you don’t need a cluster to run it — in fact, it’ll work just fine on a developer’s laptop.

Goodwin introduced the technology at [KubeCon + CloudNativeCon NA 2025](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) earlier this month.

## Kubernetes as a Universal Control Plane

Kubernetes [was created](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/) as a way to run containerized apps on clusters, and it has since been extended to manage other resources as well.

Databases, CI/CD systems like [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/), external infrastructure platforms such as [Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/), and, most recently, [machine learning (ML) systems](https://thenewstack.io/jumpstart-ai-workflows-with-kubernetes-ai-toolchain-operator/) are all controlled by Kubernetes these days.

Kubernetes has the potential for being a “universal control plane for anything we want,” Goodwin said. “Pretty much anything that can be described declaratively and reconciled continuously, we can manage with Kubernetes.”

With Kubernetes, the user describes in a [declarative language](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/) the desired state of their system, in terms of resources. It is the controllers that will continuously reconcile the actual state to the desired state through a control loop. They monitor a series of change events that are sent from the API server, and respond with the necessary changes back to the server.

[![](https://cdn.thenewstack.io/media/2025/11/2742a54d-kubecon25-goodwin-controllers-01.png)](https://cdn.thenewstack.io/media/2025/11/2742a54d-kubecon25-goodwin-controllers-01.png)

You can also write controllers to run non-Kubernetes resources as well, with the help of a [custom resource definition](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) (CRD) to define the resource.

Controllers can also be aggregated and controlled collectively, paving the way for as-yet-unseen platforms.

“It’s this composition technique that allows us to raise the level of abstraction,” Goodwin said.

## The Challenges of Managing and Debugging Controllers

Controllers, however, are difficult to manage, especially in large numbers. They get into race conditions. They operate from stale data and can produce nondeterministic results if badly written.

With control loops, “the business logic is pretty simple, but there’s a lot of things that you need to watch out for to ensure that this business logic runs soundly within a reconcile loop,” Goodwin said.

[![code comparison](https://cdn.thenewstack.io/media/2025/11/20f5f5a1-kubecon25-goodwin-controllers-02.png)](https://cdn.thenewstack.io/media/2025/11/20f5f5a1-kubecon25-goodwin-controllers-02.png)

Writing a control loop can be difficult. The first condition may be met (i.e., create a StatefulSet), but then the controller will crash before follow-up states may be initialized (booting the headless server), leaving the controller with the false signal that the app is running. So the creation operations must be separate. (Goodwin)

In addition to single controllers, assembling them in an aggregate will also bring challenges, as the devs also need to reason about the composite logic of multiple controllers, Goodwin said.

Ensuring that each individual controller works as planned doesn’t ensure that they, when run collectively, won’t do some sort of damage. Two controllers managing a single resource may vie for control, causing a race condition.

“When something goes wrong in these interactions, it can be a huge headache to debug,” he said.

These sorts of bugs can come up in code changes, or changes in configuration, or changes in resources. And these race conditions may happen all the time, or only rarely, if you are really unlucky.

Today, there are few tools to help. In many cases, the best a developer can do is pull up the log files of a controller and guess the cluster state at the time when everything went wrong.

“Because these types of issues can reproduce in very specific and maybe fleeting conditions, that makes our overall debugging process even harder when there’s a reproducibility challenge,” he said.

Welcome to distributed program debugging hell.

## Exploring the Execution Space With Kamera

Goodwin wrote Kamera to help the developer better understand a cluster state.

“For a given reconciliation process, Kamera is going to show all of the controller actions that went into that process,” he said. “So if there’s some issue, we can understand exactly what’s going on to create it.”

In order to save time, Kamera simulates a cluster. Usually, controllers interact with the system through the [Kubernetes API server](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/); Kamera simulates the server with a mocked API client interface.

“If you have controller runtime implementations, you can wire them up to this tool without any additional code changes,” Goodwin said.

The software, written in [Golang](https://thenewstack.io/introduction-to-go-programming-language/), runs on a single CPU thread and can be run on a laptop. No cluster needed.

To work, the software represents the cluster (or, more generally, the system) and walks through the creation of [ReplicaStates](https://www.youtube.com/watch?v=fCMPpVLWnpA) — following any other controllers that are called — and proceeds until all the controller states are converged and there are no pending reconciliations.

“So what this means is that we’re in some state where every controller that has a stake in the contents of that state has observed those contents and decided that nothing needs to change about it,” he explained.

If it works, that means your control plane logic is sound.

## Distributed Program Debugging Blues

If the simulation gets caught in a loop, that means something is wrong. There may be a race issue, or a [nonidempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent) operation producing a different result each time it’s executed. Or maybe there is some other nondeterministic operation that keeps shifting the state into some other (presumably) converged state.

If you’re running these operations on a real cluster, you’d be in serious danger of toppling it over with the series of actions described across all the controllers. Good thing it’s a simulation.

[![modeling execution space](https://cdn.thenewstack.io/media/2025/11/de1722b6-kubecon25-goodwin-controllers-03.png)](https://cdn.thenewstack.io/media/2025/11/de1722b6-kubecon25-goodwin-controllers-03.png)

“It’s really great we can create these types of scenarios in simulation,” Goodwin said.

## Modeling the Execution Space

Kamera can not only simulate the actions of components, but it will also model the entire execution space in order to verify that none of the bugs mentioned above will ever happen.

“We can use our execution model to comprehensively search every possible execution path and check for properties of interest like stable convergence,” Goodwin said.

This process, called model checking, “exhaustively explores the space of all possible states that our system can enter into to verify that certain properties that we care about always hold.”

Every single execution path of each controller is exhaustively tested, in effect [creating a graph](https://thenewstack.io/gql-a-new-iso-standard-for-querying-graph-databases/) of all possible system states (to whatever depth you specify). Each resulting converged space is tracked and compared. Each converged state can be explored, via an action-by-action stepper, to see what execution paths were taken.

“So what this lets us do is step through each reconcile, and inspect in a granular way how cluster state is evolving,” he said.

To test the Kamera on real cloud native software, Goodwin used the software to look at how various services within the [Knative](https://thenewstack.io/knative-has-finally-graduated-from-the-cncf/) serverless software reconcile with each other. Not surprisingly, he found the program to be sound.

Kamera takes a different approach than [SimKube](https://github.com/acrlabs/simkube), which acts as more of a [replay mechanism](https://thenewstack.io/simulate-kubernetes-cluster-behavior-with-simkube/) of actions that have already happened on a cluster.

Kamera is open source, but Goodwin warned that the software is only “research-ready” and is looking for more feedback from the Kubernetes community.

Despite any rough edges, this software could be a very handy tool for debugging stubbornly elusive misbehaviors within Kubernetes clusters.

Or planning for systems for Kubernetes to control that haven’t ever been thought of before.

View the entire talk here:

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)