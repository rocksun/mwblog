# Mastering Kubernetes Pods Troubleshooting: Advanced Strategies and Solutions
![](https://cdn.sanity.io/images/rhzn5s2f/production/e43ddff88e75e373ce94de0bf9436333ed554f5e-1200x627.jpg?w=1450&fit=max&auto=format)
[Prerequisites](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__3522f0680c90) [Kubernetes pods error - ImagePullBackoff](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__617bec3157e1) [Kubernetes Pods Error - Image pulled but the pod is pending.](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__739dc6a05bde) [Liveness & Readiness Probe Failure](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__bb3376ad6f37) [Get to Troubleshooting!](/blog/kubernetes-pods-troubleshooting-advanced-strategies#body__88ceac778110) [Kubernetes](/kubernetes-glossary/kubernetes) (K8s) deployments often pose challenges from various angles, including pods, services, ingress, non-responsive clusters, control planes, and high-availability setups. Kubernetes [pods](/kubernetes-glossary/pod) are the smallest deployable units in the Kubernetes ecosystem, encapsulating one or more containers that share resources and a network. Pods are designed to run a single instance of an app or process and are created and disposed of as needed. Pods are crucial for scaling, updating, and maintaining apps in a K8s environment.
This article explores the challenges faced with Kubernetes pods and the troubleshooting steps to take. Some of the error messages encountered when running Kubernetes pods include the following:
- ImagePullBackoff
- ErrImagePull
- InvalidImageName
- CrashLoopBackOff
Sometimes, you do not even encounter the listed errors but still observe that your pods fail. First, it is essential to note that you should understand the
[ API reference](https://kubernetes.io/docs/reference/) when debugging any Kubernetes resources. It explains how the various Kubernetes APIs are defined and how the multiple objects in your pods/ deployments work. The documentation is well-defined under API reference on the [ Kubernetes website](https://kubernetes.io/docs/reference/). In this case, when debugging pods, select the pods object from the API reference to get a detailed explanation of how pods work. It defines the fields that go into pods, i.e., version, kind, metadata, spec, and status. Kubernetes also provides a [ cheat sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) that contains a guide to the commands needed.
## Prerequisites
This article assumes the reader has the following:
[Kind](https://github.com/kubernetes-sigs/kind)installed for scenario demonstrations
- Intermediate understanding of Kubernetes architecture
[Kubectl](https://kubernetes.io/docs/reference/kubectl/)command line tool
## Kubernetes pods error - ImagePullBackoff
The error is shown for three different reasons:
- Invalid Image
- Invalid Tag
- Invalid Permissions
These scenarios arise when you don't have the correct information about your image. You might also not have permission to pull the image from its repository (private repositories). To demonstrate this in the example below, we create an nginx deployment:
â ~ kubectl create deploy nginx --image=nginxdeployment.apps/nginx created
Once the pod is running, get the pod name:
â ~ kubectl get podsNAME READY STATUS RESTARTS AGEnginx-8f458dc5b-hcrsh 1/1 Running 0 100s
Copy the name of the running pod and get further information about it:
â ~ kubectl describe pod nginx-8f458dc5b-hcrshName: nginx-8f458dc5b-hcrshhable:NoExecute op=Exists for 300sEvents:Type Reason Age From Message---- ------ ---- ---- -------Normal Scheduled 2m43s default-scheduler Successfully assigned default/nginx-8f458dc5b-hcrsh to k8s-troubleshooting-control-planeNormal Pulling 2m43s kubelet Pulling image "nginx"Normal Pulled 100s kubelet Successfully pulled image "nginx" in 1m2.220189835sNormal Created 100s kubelet Created container nginxNormal Started 100s kubelet Started container nginx
The image was pulled successfully. Your Kubernetes pod is running without errors.
To demonstrate ImagePullBackoff, edit the deployment YAML file and specify an image that does not exist:
â kubectl edit deploy nginxcontainers:-image: nginxdoestexistimagePullPolicy: Alwaysname: nginx
The new pod is not successfully deployed
â ~ kubectl get podsNAME READY STATUS RESTARTS AGEnginx-5b847fdb95-mx4pq 0/1 ErrImagePull 0 3m40snginx-8f458dc5b-hcrsh 1/1 Running 0 38m
ImagePullBackoff error is shown
â ~ kubectl describe pod nginx-6f46cbfbcb-c92blEvents:Type Reason Age From Message---- ------ ---- ---- -------Normal Scheduled 88s default-scheduler Successfully assigned default/nginx-6f46cbfbcb-c92bl to k8s-troubleshooting-control-planeNormal Pulling 40s (x3 over 88s) kubelet Pulling image "nginxdoesntexist"Warning Failed 37s (x3 over 85s) kubelet Failed to pull image "nginxdoesntexist": rpc error: code = Unknown desc = failed to pull and unpack image "docker.io/library/nginxdoesntexist:latest": failed to resolve reference "docker.io/library/nginxdoesntexist:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failedWarning Failed 37s (x3 over 85s) kubelet Error: ErrImagePullNormal BackOff 11s (x4 over 85s) kubelet Back-off pulling image "nginxdoesntexist"Warning Failed 11s (x4 over 85s) kubelet Error: ImagePullBackOff
## Kubernetes Pods Error - Image pulled but the pod is pending.
Whenever you run K8s in a
[production environment](https://blog.getambassador.io/kubernetes-development-environments-from-local-to-remote-4e33131147c6), the K8s administrators allocate ResourceQuotas for each namespace according to the requirements of the namespaces running within a cluster. Namespaces are used for logical separation within the cluster.
When the specifications in the ResourceQuota do not meet the minimal requirement of the application in a pod, the 'Image pulled, but the pod is still pending' error is thrown. In the example below, create a namespace called payments:
â ~ kubectl create ns payments
namespace/payments created
Create a ResourceQuota with relevant specifications
â ~ cat resourcequota.yamlapiVersion: v1kind: ResourceQuotametadata:name: compute-resourcesspec:hard:requests.cpu: "1"requests.memory: 1Gilimits.cpu: "2"limits.memory: 4Gi
Assign a resource quota to the namespace payments
â ~ kubectl apply -f resourcequota.yaml -n paymentsresourcequota/compute-resources created
Create a new deployment within the namespace with the resource quota restrictions:
â ~ kubectl create deploy nginx --image=nginx -n paymentsdeployment.apps/nginx created
Despite the deployment being successfully created, no pods exist:
â ~ kubectl get pods -n payments
No resources found in payments namespace.
The deployment is created, but there is no pod in the ready status, none up-to-date, and none available:
â ~ kubectl get deploy -n paymentsNAME READY UP-TO-DATE AVAILABLE AGEnginx 0/1 0 0 7m4s
To further debug, describe the nginx deployment. The pods failed to create:
â ~ kubectl describe deploy nginx -n paymentsName: nginxNamespace: paymentsCreationTimestamp: Wed, 24 May 2023 21:37:55 +0300Labels: app=nginxAnnotations: deployment.kubernetes.io/revision: 1Selector: app=nginxReplicas: 1 desired | 0 updated | 0 total | 0 available | 1 unavailableStrategyType: RollingUpdateMinReadySeconds: 0RollingUpdateStrategy: 25% max unavailable, 25% max surgePod Template:Labels: app=nginxContainers:nginx:Image: nginxPort: <none>Host Port: <none>Environment: <none>Mounts: <none>Volumes: <none>Conditions:Type Status Reason---- ------ ------Available False MinimumReplicasUnavailableReplicaFailure True FailedCreateProgressing False ProgressDeadlineExceededOldReplicaSets: <none>NewReplicaSet: nginx-8f458dc5b (0/1 replicas created)Events:Type Reason Age From Message---- ------ ---- ---- -------Normal ScalingReplicaSet 10m deployment-controller Scaled up replica set nginx-8f458dc5b to 1
Further analysis from Kubernetes events reveals insufficient memory for the pod to create.
â ~ kubectl get events --sort-by=/metadata.creationTimestamp
Kubernetes Pods Error - CrashLoopBackOff
This error occurs when your image is pulled successfully, and your container is created, but your runtime configuration fails. For example, if you have a working Python application that is trying to write to a folder that does not exist or does not have permission to write to that folder. Initially, the application gets executed, then runs into an error. The container is stopped if there is a
[ panic](https://medium.com/analytics-vidhya/defer-panic-and-recover-control-flow-concepts-in-go-c84265a05993#:~:text=panic%20is%20a%20built%2Din,that%20it%20cannot%20recover%20from) in your application logic. The container will go into a CrashLoopBackOff. Eventually, you observe that the deployment has zero pods, i.e., one pod exists, but it is not running and throws a CrashLoopBackoff error.
## Liveness & Readiness Probe Failure
A liveness probe detects if your pod has entered a broken state and can no longer serve traffic. Kubernetes will restart the pod for you. A readiness probe checks if your application is ready to handle the traffic. The readiness probe ensures that your application pulls all the necessary configurations from the configuration map and starts its threads. Only after this process is your application ready to receive traffic. If your application runs into an error during this process, it also goes into CrashLoopBackoff.
## Get to Troubleshooting!
This article provides an overview of troubleshooting techniques for Kubernetes pods. It addresses common errors encountered while deploying pods and practical solutions to resolve them. It also provides insight into the reference pages and cheat sheets vital in understanding how Kubernetes works and techniques to identify and resolve issues effectively. By following the guidance presented in this article, readers can enhance their troubleshooting skills and streamline the deployment and management of their Kubernetes pods.