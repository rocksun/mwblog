With [Kubernetes 1.35](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/), the [In-Place Pod Resize](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/) feature has graduated to GA, and [Vertical Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) *InPlaceOrRecreate* update mode has graduated to beta. This means VPA can now resize running pods without evicting them, which is a significant improvement for stateful and long-running workloads.

In this tutorial, I will walk you through the hands-on steps to install VPA on Minikube, deploy a sample application, observe resource recommendations, enable in-place resizing, and generate traffic to watch VPA adjust pod resources in real time.

## Prerequisites

Before we begin, ensure the following tools are available on your workstation.

* [**Minikube**](https://minikube.sigs.k8s.io/docs/) is used to provision a local, single-node Kubernetes 1.35 cluster.
* [**kubectl**](https://kubernetes.io/docs/reference/kubectl/) is the Kubernetes command-line tool, configured to communicate with the Minikube cluster.
* [**Git**](https://git-scm.com/) is required to clone the official autoscaler repository for VPA installation.

## Step 1 – Starting and Configuring the Minikube Cluster

If your Minikube cluster is not already running, start it with sufficient resources for VPA and the demo workload. I recommend allocating at least 4 CPUs and 4 GB of memory.

`minikube start --cpus=4 --memory=4096`

Verify that the cluster is running and accessible.  
 `kubectl cluster-info`

The output should confirm that the Kubernetes control plane is running at a local address.

## Step 2 – Enabling the Metrics Server

VPA depends on the [Kubernetes Metrics API](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/) to observe pod resource consumption. Minikube bundles the Metrics Server as a built-in addon. Enable it with the following command.

`minikube addons enable metrics-server`

The Metrics Server needs approximately 60 seconds to start collecting data. After waiting, verify that it is operational.

`kubectl top nodes`

You should see CPU and memory utilization for your Minikube node. If the command returns an error indicating that metrics are not yet available, wait another 30 seconds and try again.

## Step 3 – Installing the VPA Components

While Kubernetes 1.35 ships the in-place resize mechanism natively, the VPA controllers themselves are still installed separately. Clone the official autoscaler [repository](https://github.com/kubernetes/autoscaler) and navigate to the VPA directory.

`git clone https://github.com/kubernetes/autoscaler.git  
cd autoscaler/vertical-pod-autoscaler`

Run the installation script.

`./hack/vpa-up.sh`

This creates the VPA Custom Resource Definition, configures RBAC permissions, deploys the Recommender, Updater, and Admission Controller, and sets up the mutating webhook.

Confirm that all three VPA components are running in the kube-system namespace.

`kubectl get pods -n kube-system | grep vpa`

You should see three pods (vpa-recommender, vpa-updater, and vpa-admission-controller) all in the Running state.

![](https://cdn.thenewstack.io/media/2026/02/ab2df57d-carbon-1024x202.png)

## Step 4 – Deploying the Sample NGINX Application

We will deploy an NGINX web server with two replicas and deliberately lower the resource requests. This gives VPA room to observe usage and recommend adjustments.

Create a dedicated namespace for the demo.

Create the Deployment with a CPU request of just 50 millicores and a memory request of 64 MiB.

Apply both manifests.

`kubectl apply -f vpa-demo-namespace.yaml  
kubectl apply -f vpa-demo-deployment.yaml`

Verify that the two NGINX pods are running.

`kubectl get pods -n vpa-demo`

![](https://cdn.thenewstack.io/media/2026/02/b84f3804-carbon-1-1024x262.png)

## Step 5 – Creating a VPA in Recommendation-Only Mode

Start by setting updateMode to Off so that VPA computes recommendations without modifying any running pods.

The targetRef associates this VPA with our NGINX Deployment. The containerPolicies section sets a floor of 25 millicores and 32 MiB via minAllowed, caps recommendations at 1 CPU and 512 MiB via maxAllowed, and instructs VPA to manage both CPU and memory through controlledResources.

Apply the VPA resource.

`kubectl apply -f vpa-recommendation-only.yaml`

## Step 6 – Inspecting VPA Recommendations

After approximately 2 to 3 minutes, the Recommender will have gathered enough metrics to produce its initial recommendations. Retrieve the VPA status.

`kubectl get vpa nginx-vpa -n vpa-demo -o yaml`

Look for the `status.recommendation` section. You will see an output similar to this.

`status:  
recommendation:  
containerRecommendations:  
- containerName: "nginx"  
target:  
cpu: "25m"  
memory: "262144k"  
lowerBound:  
cpu: "25m"  
memory: "262144k"  
upperBound:  
cpu: "1"  
memory: "262144k"  
uncappedTarget:  
cpu: "12m"  
memory: "262144k"`

The target is what VPA would set as the resource request if automatic updates were enabled. The uncappedTarget is the raw recommendation before minAllowed and maxAllowed constraints are applied. Notice that the uncappedTarget for CPU is 12 millicores, but the target shows 25 millicores because our minAllowed policy enforces that floor.

## Step 7 – Enabling the InPlaceOrRecreate Update Mode

Now let’s enable automatic resource adjustments using the InPlaceOrRecreate mode.

With InPlaceOrRecreate, the Updater first attempts to resize the pod in place by patching its resource specification through the /resize subresource. The pod UID, container ID, and restart count all remain unchanged. If the node lacks sufficient resources, VPA falls back to the traditional evict-and-recreate flow. The controlledValues field set to RequestsAndLimits instructs VPA to adjust both requests and limits while maintaining the original ratio between them.

Apply the updated configuration.

`kubectl apply -f vpa-inplace.yaml`

After a few moments, verify the updated resource requests.

`kubectl describe pod -n vpa-demo -l app=nginx-vpa-demo | grep -A 3 "Requests:"`

The pod age and restart count should confirm that no eviction or restart occurred.  
For clusters running versions prior to Kubernetes 1.35, you can use updateMode set to Auto or Recreate, which achieves the same result through pod eviction and recreation.

## Step 8 – Generating Load and Observing VPA in Action

To see VPA adjust resources dynamically, expose the NGINX Deployment as a Service, and generate sustained HTTP traffic.

Create a ClusterIP Service.

Deploy a load generator pod that sends requests in a tight loop.

Apply both manifests.  
 `kubectl apply -f vpa-demo-service.yaml  
kubectl apply -f vpa-load-generator.yaml`

Poll the VPA target every 30 seconds to observe the recommendations climb.

`kubectl get vpa nginx-vpa -n vpa-demo -o jsonpath='{.status.recommendation.containerRecommendations[0].target}' ; echo`

You should see the CPU target increase as the Recommender incorporates the new usage data. Since we are running in InPlaceOrRecreate mode, the Updater will resize the NGINX pods live. Confirm that the pods have not restarted by checking their age.

`kubectl get pods -n vpa-demo -l app=nginx-vpa-demo`

Inspect the actual resource requests applied to the running pods.

`kubectl describe pod -n vpa-demo -l app=nginx-vpa-demo | grep -A 3 "Requests:"`

The requests should now reflect the VPA’s elevated recommendation rather than the original 50 millicores we specified in the Deployment manifest.

When you are done observing, stop the load generator.

`kubectl delete pod load-generator -n vpa-demo`

## Cleaning Up

Remove all the demo resources by deleting the namespace.

`kubectl delete namespace vpa-demo`

To uninstall VPA entirely from the cluster, run the teardown script.

`cd autoscaler/vertical-pod-autoscaler  
./hack/vpa-down.sh`

## Summary

In this tutorial, we installed VPA on a Minikube cluster running Kubernetes 1.35, deployed a sample NGINX application, observed VPA recommendations in passive mode, enabled the InPlaceOrRecreate update policy, and verified that VPA can resize running pods without disruption under sustained traffic. The in-place resize capability, which graduated to GA in this release, eliminates the need for pod evictions, making VPA a practical choice for stateful and restart-sensitive production workloads.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)