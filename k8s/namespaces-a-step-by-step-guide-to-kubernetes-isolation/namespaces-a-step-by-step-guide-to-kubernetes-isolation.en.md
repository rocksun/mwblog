Managing apps in [Kubernetes](https://thenewstack.io/kubernetes/) can get messy quickly. When everything runs in one big pile, it’s tough to stay organized. Mistakes like deleting the wrong pod or mixing up dev and production environments are all too easy.

That’s where namespaces can help. They act like folders for your cluster, helping you keep different parts of your system neatly separated. Whether you’re managing multiple teams, environments, or apps, namespaces make sure things don’t bump into each other.

Learn how to create a namespace using the kubectl command and explore a few tips to keep your cluster clean and under control.

## **Coming up Next**

* Why Use Namespaces in Kubernetes
* Prerequisites and Context
* Basic Syntax of `kubectl create namespace`
* Verifying and Inspecting New Namespaces
* Attaching Resource Quotas and Limits
* Setting RBAC for the New Namespace
* Integrating Namespaces Into CI/CD Pipelines
* Common Errors and Troubleshooting
* Best Practices for Namespace Organization
* Deleting and Cleaning up Namespaces Safely
* Wrapping Up: Stay Organized, Stay in Control

## **Why Use Namespaces in Kubernetes**

Think of a namespace like a folder on your computer. It keeps things grouped together so you don’t mix up files — or in this case, apps and services.

**Namespaces help:**

* Organize large projects
* Separate environments, such as dev, test and production
* Control who can access what
* Avoid naming conflicts
* Clean up resources more easily

## **Prerequisites and Context**

Before you create a namespace, you need to have a few things in place. These are basics, and you might already have them.

Make sure you have:

* A working [Kubernetes cluster](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/) (even a local one like [Minikube](https://thenewstack.io/how-to-enable-and-use-the-minikube-dashboard/) is fine).
* *kubectl* installed and connected to your cluster.
* Basic knowledge of how to run commands in a terminal.

Namespaces are not required for small setups, but if you’re managing more than one app — or have different teams working on the same cluster — they’re a must-have.

## Basic Syntax of `kubectl create namespace`

Let’s get to the good stuff: how to create a namespace. The most direct way is with a simple command:

```
kubectl create namespace your-namespace-name
```

Just swap in the name you want to use. That’s it! Now let’s look at a few options you can add.

### **Default Flags and Optional Labels**

You can add labels to your namespace when you create it. Labels help you tag your namespace with helpful info, like which team it belongs to.

**Here’s an example with a label:**

```
kubectl create namespace your-namespace-name --dry-run=client -o yaml | kubectl label -f - team=frontend
```

This command adds a label called team=frontend to your namespace.

**Flags you might use:**

* ***–dry-run=client*****:** Shows what the command would do, without making changes.
* ***-o yaml*****:** Outputs the command in [YAML format](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) — great for saving as a file.

### **Creating Namespaces From YAML Manifests**

You can also define a namespace in a [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) file. This is handy if you want to keep track of your setup or share it with your team.

**Here’s a basic YAML example:**

```
apiVersion: v1
kind: Namespace
metadata:
name: your-namespace-name
```

To create the namespace from this file, run: kubectl apply -f namespace.yaml

Using YAML is especially useful in teams, automation or when working with GitOps tools.

## **Verifying and Inspecting New Namespaces**

Once you’ve created a namespace, you’ll want to make sure it actually exists — and maybe peek inside to see what’s going on. Kubernetes gives you a few easy ways to do this using kubectl.

### Listing Namespaces With `kubectl get ns`

To see all the namespaces in your cluster, just run: *kubectl get ns*.

You’ll get a list like this:

```
NAME              STATUS   AGE
default           Active   10d
kube-system       Active   10d
your-namespace    Active   2m
```

This confirms your namespace is up and running.

### **Describing Namespace Details**

If you want more details about a specific namespace, use: *kubectl describe namespace your-namespace-name.*

This shows you info like labels, status and any applied policies. It’s a great way to double-check that everything is set up the way you expected.

## **Attaching Resource Quotas and Limits**

Namespaces aren’t just about organizing things — they can also help you control how much CPU, memory and other resources each team or app can use. This keeps one app from hogging everything and crashing the rest.

### **CPU and Memory Quotas**

You can set limits on how much CPU and memory a namespace can use. First, create a YAML file like this:

```
apiVersion: v1
kind: ResourceQuota
metadata:
   name: basic-quota
   namespace: your-namespace-name
spec:
   hard:
     requests.cpu: "1"
     requests.memory: 500Mi
     limits.cpu: "2"
     limits.memory: 1Gi
```

Then apply it with: *kubectl apply -f quota.yaml.*

This tells Kubernetes, “Hey, this namespace can’t use more than this amount of CPU or memory.”

### **Object Count Restrictions**

You can also limit how many things — pods, services or secrets — a namespace can have. Here’s an example:

```
spec:
   hard:
      pods: "10"
      services: "5"
      secrets: "20"
```

Add this to your quota YAML to make sure a namespace doesn’t get too crowded.

## **Setting RBAC for the New Namespace**

[Role-based access control (RBAC)](https://thenewstack.io/kubernetes-rbac-permissions-you-might-not-know-about-but-should/) helps you manage who can do what inside your namespace. For example, you might want to give the dev team access to one namespace but not another.

### **Role and RoleBinding Basics**

First, create a Role that says what actions are allowed:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
   namespace: your-namespace-name
   name: pod-reader
rules:
 - apiGroups: [""]
   resources: ["pods"]
   verbs: ["get", "watch", "list"]
```

Then, bind that role to a user or group:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
   name: read-pods
   namespace: your-namespace-name
subjects:
-  kind: User
   name: dev-user
   apiGroup: rbac.authorization.k8s.io
roleRef:
   kind: Role
   name: pod-reader
   apiGroup: rbac.authorization.k8s.io
```

This gives dev-user permission to read pod info in that namespace — nothing more.

### **Service Account Scoping**

Instead of assigning roles to users, you can assign them to service accounts used by apps. That way, your app only gets access to the things it actually needs.

**Example:**

```
subjects:
- kind: ServiceAccount
name: my-app
namespace: your-namespace-name
```

This keeps things secure and avoids giving apps unnecessary permissions.

## **Integrating Namespaces Into CI/CD Pipelines**

Namespaces aren’t just useful for organizing apps; they’re also great for automating your workflows. In a [CI/CD pipeline](https://thenewstack.io/why-ci-and-cd-need-to-go-their-separate-ways/), you can use namespaces to keep test runs clean and separate from each other.

### **Dynamic Namespace Creation for Test Environments**

Every time your pipeline runs, you can spin up a brand-new namespace just for that test. This keeps tests isolated, so they don’t mess with your main app or each other.

**Example command:** *kubectl create namespace test-run-123.*

You can use scripts to generate unique names like *test-run-001*, *test-run-002* and so on. This is especially handy when testing pull requests or new builds.

### **Automatic Cleanup Strategies**

Once the test is done, clean up that namespace to save resources.

Here’s how you delete it: *kubectl delete namespace test-run-123.*

Some teams also add a time-based [cleanup](https://thenewstack.io/how-to-detect-and-clean-up-data-contamination-in-llms/), like deleting any test namespace older than an hour. You can script this or use tools like Kubernetes Jobs or TTL controllers.

## **Common Errors and Troubleshooting**

Even simple commands can hit speed bumps. Here are a couple of common namespace-related errors and how to fix them.

### **“AlreadyExists” Conflicts**

If you try to create a namespace that already exists, you’ll see an error like this:

```
Error from server (AlreadyExists): namespaces "your-namespace-name" already exists
```

**Solution(s):**

* Double-check your namespace name.
* You can also list existing namespaces using *kubectl get ns.*
* Or, if you meant to update something, use *apply* instead of *create*.

### **Invalid Metadata or Labels**

If your namespace YAML has bad formatting or unsupported characters in names or labels, Kubernetes will throw an error.

**Common mistakes:**

* Using capital letters or spaces
* Missing required fields like name

Always double-check your YAML file. You can validate it before applying by running:

```
kubectl apply --dry-run=client -f your-file.yaml
```

This shows you if anything’s wrong without actually making changes.

## **Best Practices for Namespace Organization**

Namespaces help you stay organized, but only if you use them the right way. Without a clear system, things can get confusing fast, especially as more people and apps join the party.

Here’s how to keep your namespace setup clean, logical and easy to manage.

### **Naming Conventions**

A good naming system makes it easy to know what a namespace is for, just by looking at it. Stick to names that are short, clear and consistent.

**Tips for naming:**

* Use lowercase letters and hyphens only (Kubernetes is picky!).
* Include the purpose or owner in the name.
* Avoid vague names like *project1* or *testtemp*.

**Examples:**

* *frontend-prod*
* *backend-dev*
* *team-alpha-staging*

If you’re using namespaces in [CI/CD pipelines](https://thenewstack.io/ci-is-not-cd/), use unique but traceable names like:

* *test-pr-204*
* *ci-run-2025-07-17*

This helps you find and clean them up later.

### **Segmenting by Team, Environment or Application**

Namespaces are flexible — you can group things however you want. But here are the most common and effective ways:

**By team:** Each team gets its own namespace. This keeps their resources separate and gives them room to experiment without stepping on each other’s toes.

**Examples:**

* *team-marketing*
* *team-infra*

**By environment:** Separate dev, test, staging and production environments. This avoids accidents, like deploying unfinished code to your live app.

**Examples:**

**By application:** If your cluster runs many small apps, give each one its own namespace. This keeps services from clashing and makes it easier to manage permissions and quotas.

**Examples:**

* *billing-service*
* *user-auth*

You can even combine these approaches. For example:

* *frontend-dev*
* *backend-prod*
* *team-ops-staging*

Just make sure everyone follows the same pattern so your cluster doesn’t turn into a naming mess.

## **Deleting and Cleaning up Namespaces Safely**

Creating namespaces is easy. Forgetting to delete them? Even easier. But leftover namespaces can waste resources, clutter your cluster and even cause security risks if they still have access to sensitive stuff.

Here’s how to clean up like a pro, without accidentally deleting something important.

### **How To Delete a Namespace**

To delete a namespace, run: *kubectl delete namespace your-namespace-name.*

That’s it. Kubernetes will wipe everything inside — pods, services, secrets, configs — the whole thing. But once deleted, it’s gone for good. Always double-check the name before hitting Enter.

### **Check What’s Inside Before Deleting**

If you’re not sure what a namespace contains, list its resources first: *kubectl get all -n your-namespace-name.*

This will show you what’s running — pods, deployments, services, etc. You can also check for secrets and config maps:

```
kubectl get secrets -n your-namespace-name
```

```
kubectl get configmaps -n your-namespace-name
```

It’s like looking in your fridge before tossing it out — you might find something worth saving!

### **Stuck in ‘Terminating’ State?**

Sometimes a namespace gets stuck in the Terminating state. This usually means something inside is hanging and not letting go.

**Steps to troubleshoot:**

1. Run *kubectl get namespace your-namespace-name -o json.* Look for finalizers at the bottom.
2. Remove finalizers manually (advanced — but useful in rare cases).

Use with caution:

```
kubectl patch namespace your-namespace-name -p '{"metadata":{"finalizers":[]}}' --type=merge
```

This force-deletes the namespace, but only if you’re sure it’s safe to do so.

### **Automating Cleanup (Bonus)**

If you use namespaces for short-term things like test runs or CI/CD, set up automation to delete old ones regularly.

**Here are some ideas:**

* Add a TTL (time-to-live) label like *ttl=1h*.
* Write a cleanup script that checks namespace age and deletes old ones.
* Use Kubernetes TTL controllers if your cluster supports them.

This keeps your cluster tidy without constant babysitting.

## **Wrapping Up: Stay Organized, Stay in Control**

Namespaces are one of the simplest but most powerful tools in Kubernetes. They help you organize your apps, protect your environments, control resources and scale without chaos.

From creating a namespace with a one-liner to setting quotas, RBAC and automating cleanup, you now know how to build a clean, safe and team-friendly Kubernetes setup.

Whether you’re managing a single app or a whole fleet, using namespaces the right way gives you the control and clarity you need to grow with confidence.

Check out our step-by-step guide, [How To Remove a Deployment in Kubernetes](https://thenewstack.io/remove-deployment-in-kubernetes/), and keep your cluster clutter-free.

**Primary sources:**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/05/bb2522cc-cropped-e116206d-sunny_photo-600x600.jpg)

Sunny is a seasoned tech writer with an engineering background who digs into developer tools, cloud infrastructure, cybersecurity, and AI, and turns them into stories that even non-engineers don’t mind reading. His work bridges the gap between technical depth and...

Read more from Sunny Yadav](https://thenewstack.io/author/sunny-yadav/)