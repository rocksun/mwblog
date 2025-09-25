Anyone who uses Kubernetes, has probably executed `kubectl apply` command to create resources or update them on the cluster, or in more advanced cases, tried to create/update resources programatically when building an operator. The “apply” operation is flexible and abstracts quite a lot in the background. For instance, `kubectl apply` command has two modes: a client-side mode, which has been the default mode in `kubectl` for years, and a (relatively) more recent mode: server-side apply, or SSA, which was made [generally available](https://kubernetes.io/blog/2021/08/04/kubernetes-1-22-release-announcement/) amidst summer of 2021 with the release of Kubernetes v1.22.

I find SSA to be a beautiful and well-thought feature in Kubernetes, which we will discuss in-depth in this article. We will talk about what it is, how it works and how it solves some important headaches for both DevOps folks and K8s operator developers, highlighting some interesting ideas such optimistic concurrent control. But let’s start from the roots, with a brief discussion on the default mode of `kubectl apply`: client-side apply (CSA).

When you run `kubectl apply` on an existing resource, here’s what happens on your machine by default (e.g. running `kubectl apply -f …`):

1. Fetch the current live version of the resource from the API server.
2. Compare three different configurations:

   * The local file you're providing, this is commonly referred to as the *desired state* because we are asking the cluster to move to a new state.
   * The live version running in the cluster, referred to as the *current state*.
   * The `last-applied-configuration` annotation stored on the live resource, which is a snapshot of the YAML from the last time `apply` was run, stored as a JSON string.
3. Compute a diff patch using a **three-way merge** strategy based on the comparison of those three sources.
4. Send the calculated patch to the Kubernetes API server, which then updates the resource or creates if it doesn’t exist.

The following figure summarize this 3-way merge process:

[![](https://substackcdn.com/image/fetch/$s_!PY0G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9afa0205-f325-403c-afeb-c72ef5c3bf79_1427x542.png)](https://substackcdn.com/image/fetch/$s_!PY0G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9afa0205-f325-403c-afeb-c72ef5c3bf79_1427x542.png)

This is the approach that `kubectl` uses by default for years now. In environments where a resource can be updated by different actors such as different users or controllers, several problems might arise. We will discuss these problems shortly and how server-side apply helps avoiding those issues, however, let’s start by introducing the second mode of the apply command: Server-Side Apply, or SSA for short.

Server-side apply, generally available since v1.22, works differently: instead of having `kubectl` pull three versions for the resource and comparing them, we now have one central actor that does all of this for us: the Kubernetes API server in the control-plane will compare the new desired version of the resource that we specify and the current version running in the cluster, if it exists. It also calculates a *diff* and patches the resource if needed.

The comparison and diffing has now moved from the local kubectl program running on our machine to the control plane of the cluster itself, that’s why we call it server-side apply. Below is a visual representation of this approach:

[![](https://substackcdn.com/image/fetch/$s_!7yrz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd813a52-32dd-4cf2-a252-6a709af8c39d_1003x480.png)](https://substackcdn.com/image/fetch/$s_!7yrz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd813a52-32dd-4cf2-a252-6a709af8c39d_1003x480.png)

As you can see, `kubectl` now acts as a straightforward messenger. It sends your YAML to the API server, and the control plane handles the rest for us. To use this mode, you just need to add the `--server-side` flag to your `apply` command:

`kubectl apply --server-side -f my-deployment.yaml`

Resources can be updated with SSA through different ways, not just using `kubectl apply —serverside` command. In case you build an operator and need to update a resource programatically (e.g. using the client SDK of Kubernetes, Kubebuilder or the Operator Framework), SSA is supported be default at the k8s API level for the `client.Apply` method, which you can send through a PATCH request. This requires providing a `fieldManager` string key to specify which actor is responsible for the provided fields. We will discover soon what are managed fields and how SSA uses that for handling conflicts.

Great! Now that we know how SSA works and how to use it, let’s discuss some of the headaches it solves.

---

I believe that server-side apply shines in certain aspects compared to client-side apply, namely regarding the following topics:

In the default client-based workflow of Kubernetes Apply, updating a resource could result in a conflict if the same resource was modified before by another actor, such as a controller, an administrator or a CI/CD pipeline. These conflicts arise because the `resourceVersion` that the resource has at the time you run `kubectl apply -f …` is different from the `resourceVersion` which just got updated from a different actor.

SSA simplify the conflict management by providing a “field versioning” mechanism during updates: we can specify the name of the field manager, that is the ID of the actor responsible for manipulating this field, Kubernetes will then check if that specified ID corresponds to the proper `managedFields.manager` property in the resource. The [SSA docs](https://kubernetes.io/docs/reference/using-api/server-side-apply/#field-management) do a good job of explaining this:

> A Server-Side Apply **patch** request requires the client to provide its identity as a [field manager](https://kubernetes.io/docs/reference/using-api/server-side-apply/#managers). When using Server-Side Apply, trying to change a field that is controlled by a different manager results in a rejected request unless the client forces an override. For details of overrides, see [Conflicts](https://kubernetes.io/docs/reference/using-api/server-side-apply/#conflicts).
>
> When two or more appliers set a field to the same value, they share ownership of that field. Any subsequent attempt to change the value of the shared field, by any of the appliers, results in a conflict. Shared field owners may give up ownership of a field by making a Server-Side Apply **patch** request that doesn't include that field.

As mentioned in the docs, you can also force overrides of certain fields by other actors.

This behaviour has a nice consequence: *optimistic concurrency control* which we will discuss next.

Adopting SSA helps avoid certain issues that come with the concurrent, distributed nature of Kubernetes. We usually have different controllers that run concurrently and in parallel in the cluster. They might act on the same resource, leading to conflicts as previously discussed.

To better understand the problem, imagine building a controller for a new type of resource (a CRD). To update the resource, your controller executes the following standard "*Get-Modify-Update*" approach:

1. Fetch the resource from the cluster.
2. Update some fields.
3. Push the update, usually through a `client.Update()` call or a PATCH request.

However, in an environment where a resource can be modified by other actors, this approach is not safe. While we fetch the resource locally and run some logic to update the needed fields, another controller or an administrator might also update it before us. This leaves us with a stale version of the resource locally. When we send our update request, it will result in an error, as the version of the live resource is newer than the version we have.

If you've ever dealt with concurrent programming, this is very similar to a data race, where one thread changes some data while another thread is reading it.

Data races are usually solved through synchronization techniques such as using locks to coordinate different threads. Locking, however, is usually a very expensive operation. In the context of Kubernetes, we can’t really lock an entire resource until the update is executed. This approach of locking and unlocking resources is often referred to as *Pessimistic Concurrency Control* in distributed systems.

Server-Side Apply in Kubernetes provides a better approach to this issue, commonly known as *Optimistic Concurrency Control*. Since the server is now the single source of truth and all of the computation moves to the API server, it achieves optimistic concurrency control by avoiding locks and using managedFields along with the provided fieldManager in the request to control concurrent updates.

Optimistic concurrency works best in distributed systems with low resource contention—that is, systems where competitive access to shared resources is not very frequent, and therefore the probability of conflicts arising is low (but not zero). In environments where resource contention is high (i.e., access to shared resources by different actors is frequent), using the pessimistic concurrency we discussed earlier is better, but it comes with performance and complexity trade-offs.

The last part we will dicuss in this section about SSA benefits are CI/CD pipelines that often interact with resources deployed on the cluster. Imagine a setup where an automated pipeline is responsible for deploying new versions of an application. Its only job is to update the container `image` field in a Deployment manifest to roll out the latest tag. For sake of simplicity, imagine having an horizontal pod autoscaler running in the cluster as well to scale your deployment to multiple replicas in case of a traffic spike.

With the old client-side `apply`, this process is surprisingly fragile. The pipeline's static YAML file would specify a default `replicas` count of 2 pods ( `replicas: 2)`. Now if the HPA scales your application up to 10 replicas to handle a traffic spike, the next time your CI/CD pipeline runs to deploy a new image, it will use its local file as the desired state. It will see the `replicas` count in the cluster is 10, but its `last-applied-configuration` and local file both say 2. It will try to scale your application back down to 2 replicas, in good intentions, right in the middle of peak traffic, potentially causing an outage due to a race condition between two concurrent yet independent systems: the CI/CD pipeline and the HPA.

Server-Side Apply solves this nicely by introducing the same field ownership concept we previously discussed. When the CI/CD pipeline applies its change using `--server-side`, it claims ownership of *only* the `spec.template.spec.containers[0].image` field. At the same time, the Horizontal Pod Autoscaler is registered as the owner of the `spec.replicas` field. Now, the two systems can operate on the same resource **concurrently without conflict**. The pipeline can update the image tag as many times as it wants, and the HPA can freely scale the replica count up or down. The Kubernetes API server understands that these changes are managed by different actors and merges them safely.

If another administrator or a different pipeline *does* try to change the image tag, SSA will immediately flag a **conflict**. Instead of silently overwriting the change, the apply command will fail. By propagating these conflicts back to your CI/CD logs, you create a clear and immediate signal for a DevOps engineer to investigate and resolve the issue, preventing unexpected production bugs.

So far, we’ve discussed several important benefits of using Server-Side Apply (SSA) in Kubernetes. I find this feature to be a great addition that elegantly solves several problems, particularly for large clusters.

In my humble opinion, if you are an operator or controller developer, you should definitely aim to use SSA in your logic for resource updates. The robust conflict management it provides is well worth it, making your declarative updates safer and more reliable. Your operator might be used in large clusters with several other controllers and its best to offer a high-quality, reliable operator if that’s your job.

Second, if you are a cluster administrator or an application developer, I would also advise using SSA with the `kubectl apply` command. This is particularly true if your cluster has different controllers that might update the same resource, as SSA helps manage conflicts and avoid the race conditions we’ve discussed. However, for a small cluster without many controllers competing for the same resources, the default client-side apply might still be sufficient.

If you want another view of why you should use SSA from **one of the contributors of this feature**, I would highly recommend reading: [Server-side apply is great and you should use it](https://kubernetes.io/blog/2022/10/20/advanced-server-side-apply/) by Daniel Smith from Google.

---