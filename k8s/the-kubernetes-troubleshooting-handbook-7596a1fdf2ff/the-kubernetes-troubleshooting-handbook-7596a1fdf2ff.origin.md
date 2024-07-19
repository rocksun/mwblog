# The Kubernetes Troubleshooting Handbook
## Introduction
Debugging Kubernetes applications can feel like navigating a labyrinth. With its distributed nature and myriad of components, identifying and resolving issues in Kubernetes requires a robust set of tools and techniques.

In this blog we will explore various techniques and tools to help with troubleshooting and debugging Kubernetes. Whether you’re an experienced Kubernetes user or just getting started, this guide will provide valuable insights into efficient debugging practices.

Although in this blog I do my best to compile useful advice based on my experience, the authoritative source of truth should always be the

[official Kubernetes documentation].
# Analyzing Pod Lifecycle Events
Understanding the lifecycle of a pod is crucial for debugging and maintaining applications running in Kubernetes. Each pod goes through several phases from creation to termination, and analyzing these events can help you identify and resolve issues.

## Pod Lifecycle Phases
A pod in Kubernetes goes through the following phases:

## Using `kubectl get`
and `kubectl describe`
To analyze the lifecycle events of a pod, you can use the `kubectl get`
and `kubectl describe`
commands.

The `kubectl get`
command provides a high-level overview of the status of pods:

`kubectl get pods`
Output:

`NAME READY STATUS RESTARTS AGE`
web-server-pod 1/1 Running 0 5m
db-server-pod 1/1 Pending 0 2m
cache-server-pod 1/1 Completed 1 10m
This output shows the current status of each pod, which can help you identify pods that need further investigation.

The `kubectl describe`
command provides detailed information about a pod, including its lifecycle events:

`kubectl describe pod <pod-name>`
Output snippet:

`Name: web-server-pod`
Namespace: default
Node: node-1/192.168.1.1
Start Time: Mon, 01 Jan 2024 10:00:00 GMT
Labels: app=web-server
Status: Running
IP: 10.244.0.2
Containers:
web-container:
Container ID: docker://abcdef123456
Image: nginx:latest
State: Running
Started: Mon, 01 Jan 2024 10:01:00 GMT
Ready: True
Restart Count: 0
Events:
Type Reason Age From Message
---- ------ ---- ---- -------
Normal Scheduled 10m default-scheduler Successfully assigned default/web-server-pod to node-1
Normal Pulled 9m kubelet, node-1 Container image "nginx:latest" already present on machine
Normal Created 9m kubelet, node-1 Created container web-container
Normal Started 9m kubelet, node-1 Started container web-container
## Analyzing Pod Events
The `Events`
section in the `kubectl describe`
output provides a chronological log of significant events that have occurred for the pod. These events can help you understand the lifecycle transitions and identify issues such as:

**Scheduling Delays:**Delays in scheduling the pod can indicate resource constraints or issues with the scheduler.**Image Pull Errors:**Failures in pulling container images can indicate network issues or problems with the container registry.**Container Crashes:**Repeated container crashes can be diagnosed by examining the events leading up to the crash.
# Kubernetes Events and Audit Logs
Kubernetes generates cluster wide events resources
which we can use for a quick overview of what’s happening on the cluster.**kind**: Event

Audit logs
on the other hand are useful for ensuring compliance and securtity on the cluster. They can show login attempts, pod priviledges escalation and more.**kind**: Policy

## Kubernetes Events
Kubernetes events provide a timeline of significant occurrences within your cluster, such as pod scheduling, container restarts, and errors. They are useful for understanding the state transitions and identifying the root causes of issues.

Viewing Events

To view events in your cluster, use the `kubectl get events`
command:

`kubectl get events`
Output example:

`LAST SEEN TYPE REASON OBJECT MESSAGE`
12s Normal Scheduled pod/web-server-pod Successfully assigned default/web-server-pod to node-1
10s Normal Pulling pod/web-server-pod Pulling image "nginx:latest"
8s Normal Created pod/web-server-pod Created container web-container
7s Normal Started pod/web-server-pod Started container web-container
5s Warning BackOff pod/db-server-pod Back-off restarting failed container
Filtering Events

You can filter events to focus on specific namespaces, resource types, or time periods. For example, to view events related to a specific pod:

`kubectl get events --field-selector involvedObject.name=web-server-pod`
Describing Resources

The `kubectl describe`
command includes events in its output, providing detailed information about a specific resource along with its event history:

`kubectl describe pod web-server-pod`
Output snippet:

`Events:`
Type Reason Age From Message
---- ------ ---- ---- -------
Normal Scheduled 10m default-scheduler Successfully assigned default/web-server-pod to node-1
Normal Pulled 9m kubelet, node-1 Container image "nginx:latest" already present on machine
Normal Created 9m kubelet, node-1 Created container web-container
Normal Started 9m kubelet, node-1 Started container web-container
## Kubernetes Audit Logs
Audit logs provide a detailed record of all API requests made to the Kubernetes API server, including the user, the action performed, and the outcome. They are essential for security auditing and compliance.

**Enabling Audit Logging**
To enable audit logging, configure the API server with the appropriate flags and audit policy. Here’s an example of an audit policy configuration:

`# audit-policy.yaml`
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
resources:
- group: ""
resources: ["pods"]
- level: RequestResponse
users: ["admin"]
verbs: ["update", "patch"]
resources:
- group: ""
resources: ["configmaps"]
**Configuring the API Server**
Specify the audit policy file and log file location when starting the API server:

`kube-apiserver --audit-policy-file=/etc/kubernetes/audit-policy.yaml --audit-log-path=/var/log/kubernetes/audit.log`
Viewing Audit Logs

Audit logs are typically written to a file. You can use standard log analysis tools to view and filter the logs. Here’s an example of an audit log entry:

`{`
"kind": "Event",
"apiVersion": "audit.k8s.io/v1",
"level": "Metadata",
"auditID": "12345",
"stage": "ResponseComplete",
"requestURI": "/api/v1/namespaces/default/pods",
"verb": "create",
"user": {
"username": "admin",
"groups": ["system:masters"]
},
"sourceIPs": ["192.168.1.1"],
"objectRef": {
"resource": "pods",
"namespace": "default",
"name": "web-server-pod"
},
"responseStatus": {
"metadata": {},
"code": 201
},
"requestReceivedTimestamp": "2024-01-01T12:00:00Z",
"stageTimestamp": "2024-01-01T12:00:01Z"
}
# Kubernetes Dashboard
The Kubernetes Dashboard is a web-based UI that provides an easy way to manage and troubleshoot your Kubernetes cluster. It allows you to visualize cluster resources, deploy applications, and perform various administrative tasks.

## Installing the Kubernetes Dashboard
Please refer to the [kubernetes documentaiton](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/) for details on installing and accessing the dashboard.

## Using the Dashboard
The Dashboard provides various features to help manage and troubleshoot your Kubernetes cluster:

**Cluster Overview**: View the overall status of your cluster, including nodes, namespaces, and resource usage.**Workloads**: Monitor and manage workloads, such as Deployments, ReplicaSets, StatefulSets, and DaemonSets.**Services and Ingress**: Manage services and ingress resources to control network traffic.**Config and Storage**: Manage ConfigMaps, Secrets, PersistentVolumeClaims, and other storage resources.**Logs and Events**: View logs and events for troubleshooting and auditing purposes.
# Monitoring Resource Usage
Monitoring resource usage helps you understand how your applications consume resources and identify opportunities for optimization.

Tools for Monitoring

**kubectl top:**Provides real-time resource usage metrics.**Prometheus:**Collects and stores metrics for detailed analysis.**Grafana:**Visualizes metrics and provides dashboards for monitoring.
Using kubectl top

The `kubectl top`
command shows the current CPU and memory usage of pods and nodes.

`kubectl top pods`
kubectl top nodes
Example output:

`NAME CPU(cores) MEMORY(bytes)`
my-app-pod 100m 120Mi
# Using kubectl logs
When it comes to debugging Kubernetes applications, `kubectl logs`
is one of the most essential tools in our arsenal. This command helps to retrieve logs from a specific container in a pod, allowing you to diagnose and troubleshoot issues effectively.

## Basic Usage
The simplest way to retrieve logs from a pod is by using the `kubectl logs`
command followed by the pod name and namespace. Here’s a basic example for a pod running in a `default`
namespace:

`kubectl logs <pod-name>`
This command fetches the logs from the first container in the specified pod. If your pod has multiple containers, you need to specify the container name as well:

`kubectl logs <pod-name> -c <container-name>`
## Real-time Logs with `-f`
Flag
To stream logs in real-time, similar to `tail -f`
in Linux, use the `-f`
flag:

`kubectl logs -f <pod-name>`
This is particularly useful for monitoring logs as your application runs and observing the output of live processes.

There are projects that enchance the log tailing with additional capabilities, for example

[stern].
## Retrieving Previous Logs
If a pod has restarted, you can view the logs from the previous instance using the `--previous`
flag:

`kubectl logs <pod-name> --previous`
This helps in understanding what caused the pod to restart by examining the logs before the failure.

## Filtering Logs with Labels
You can also filter logs from pods that match certain labels using `kubectl`
along with `jq`
for advanced filtering:

`kubectl get pods -l <label-selector> -o json | jq -r '.items[] | .metadata.name' | xargs -I {} kubectl logs {}`
Replace `<label-selector>`
with your specific labels, such as `app=myapp`
.

## Combining with Other Tools
You can combine `kubectl logs`
with other Linux commands to enhance your debugging process. For example, to search for a specific error message in the logs, you can use `grep`
:

`kubectl logs web-server-pod | grep "Error"`
For a continuous search in real-time logs:

`kubectl logs -f web-server-pod | grep --line-buffered "Error"`
## Practical Tips
**Log Rotation and Retention:** Ensure that your application handles log rotation to prevent the logs from consuming excessive disk space.
**Structured Logging:** Use structured logging (e.g., JSON format) to make it easier to parse and analyze logs using tools like `jq`
.
**Centralized Logging:** Consider setting up a centralized logging system (e.g., Elasticsearch, Fluentd, and Kibana — EFK stack) to aggregate and search logs from all your Kubernetes pods.
# Using kubectl exec for Interactive Troubleshooting
`kubectl exec`
allows us to execute commands directly inside a running container. This is particularly useful for interactive troubleshooting, enabling the inspection of the container’s environment, run diagnostic commands, and perform real-time fixes.
## Basic Usage
The basic syntax for `kubectl exec`
is as follows:

`kubectl exec <pod-name> -- <command>`
To execute a command in a specific container within a pod, use the `-c`
flag. Note that this will execute a command and immediatelly exit the container.

`kubectl exec <pod-name> -c <container-name> -- <command>`
## Running an Interactive Shell
One of the most common uses of `kubectl exec`
is to open an interactive shell session within a container. This allows you to run multiple commands interactively. Here’s how to do it:

`kubectl exec -it <pod-name> -- /bin/bash`
For containers using `sh`
instead of `bash`
:

`kubectl exec -it <pod-name> -- /bin/sh`
## Example: Inspecting Environment Variables
To check the environment variables inside a container, you can use the `env`
command:

`kubectl exec <pod-name> -- env`
If you need to check environment variables in a specific container:

`kubectl exec <pod-name> -c <container-name> -- env`
## Example: Checking Configuration Files
Suppose you need to inspect a configuration file inside the container. You can use `cat`
or any text editor available inside the container:

`kubectl exec <pod-name> -- cat /path/to/config/file`
For a specific container:

`kubectl exec <pod-name> -c <container-name> -- cat /path/to/config/file`
## Copying Files to and from Containers
If you don’t have a binary you need inside a container, it’s easy to files to and from containers using `kubectl cp`
. For example, to copy a file from your local machine to a container:

`kubectl cp /local/path/to/file <pod-name>:/container/path/to/file`
To copy a file from a container to your local machine:

`kubectl cp <pod-name>:/container/path/to/file /local/path/to/file`
## Practical Tips
**Use the ****-i**** and ****-t**** Flags:** The `-i`
flag makes the session interactive, and the `-t`
flag allocates a pseudo-TTY. Together, `-it`
enables a fully interactive session.
**Run as a Specific User:** Use the `--user`
flag to execute commands as a specific user inside the container, if required.
`kubectl exec --user=<username> -it <pod-name> -- /bin/bash`
**Security Considerations:** Be cautious when running `kubectl exec`
with elevated privileges. Ensure you have appropriate RBAC (Role-Based Access Control) policies in place to prevent unauthorized access.
# Node-Level Debugging with `kubectl debug`
Most of the debugging techniquest focus on the application level, however it’s also possible to debug a specific kubernetes node using `kubectl debug node`
command.

Node-level debugging is crucial for diagnosing issues that affect the Kubernetes nodes themselves, such as resource exhaustion, misconfigurations, or hardware failures.

This way **the debugging Pod can access the root filesystem of the Node, mounted at ****/host**** in the Pod.**

**Create a Debugging Session:**
Use the `kubectl debug`
command to start a debugging session on a node. This command creates a pod running a debug container on the specified node.

`kubectl debug node/<node-name> -it --image=busybox`
Replace `<node-name>`
with the name of the node you want to debug. The `-it`
flag opens an interactive terminal, and `--image=busybox`
specifies the image to use for the debug container.

For more details, refer to the

[official Kubernetes documentation on node-level debugging].
# Application-Level Debuging with Debug Containers
For more complex issues, consider using a debug container with pre-installed tools. There are a lot of good docker images with tooling and scripts for debugging, one that stands out to me is [https://github.com/nicolaka/netshoot](https://github.com/nicolaka/netshoot). It can quicky be created using:

`kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot`
Example: Using the debug container as a sidecar

` apiVersion: apps/v1`
kind: Deployment
metadata:
name: nginx-netshoot
labels:
app: nginx-netshoot
spec:
replicas: 1
selector:
matchLabels:
app: nginx-netshoot
template:
metadata:
labels:
app: nginx-netshoot
spec:
containers:
- name: nginx
image: nginx:1.14.2
ports:
- containerPort: 80
- name: netshoot
image: nicolaka/netshoot
command: ["/bin/bash"]
args: ["-c", "while true; do ping localhost; sleep 60;done"]
Apply the configuration:

`kubectl apply -f debug-pod.yaml`
## Practical Tips
**Set Restart Policies:** Ensure that your pod specifications have appropriate restart policies to handle different failure scenarios.
**Automated Monitoring:** Set up automated monitoring and alerting for critical issues such as `CrashLoopBackOff`
using Prometheus and Alertmanager.
# Ephemeral Containers for Debugging
[Ephemeral containers](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container) are temporary and created specifically for debugging purposes. They are useful for running diagnostic tools and commands without affecting the running application. This chapter will explore how to create and use ephemeral pods for interactive troubleshooting in Kubernetes.
## Why Use Ephemeral Pods?
**Isolation:**Debugging in an isolated environment prevents accidental changes to running applications.**Tool Availability:**Allows the use of specialized tools that may not be present in the application container.**Temporary Nature:**These pods can be easily created and destroyed as needed, without leaving residual impact on the cluster.
## Creating Ephemeral Pods
There are several ways to create ephemeral pods in Kubernetes. One common method is to use the `kubectl run`
command.

Example: Creating an Ephemeral Pod

**Using ****kubectl run****:**
`kubectl debug mypod -it --image=nicolaka/netshoot`
This command creates a debug pod using the `netshoot`
image and opens an interactive shell.

## Practical Tips for Using Ephemeral Pods
**Tool Availability:** Ensure the debug container image includes all necessary tools for troubleshooting, such as `curl`
, `netcat`
, `nslookup`
, `df`
, `top`
, and others.
**Security Considerations:** Be mindful of security when creating ephemeral pods. Ensure they have limited access and are used by authorized personnel only.
## Example: Advanced Debugging with Custom Debug Container
Let’s walk through an example of using a custom debug container for advanced debugging tasks.

**Create an Ephemeral Pod with Custom Debug Container:**
`kubectl debug -it redis5 --image=nicolaka/netshoot`
Defaulting debug container name to debugger-v4hfv.
If you don't see a command prompt, try pressing enter.
dP dP dP
88 88 88
88d888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. d8888P
88' `88 88ooood8 88 Y8ooooo. 88' `88 88' `88 88' `88 88
88 88 88. ... 88 88 88 88 88. .88 88. .88 88
dP dP `88888P' dP `88888P' dP dP `88888P' `88888P' dP
Welcome to Netshoot! (github.com/nicolaka/netshoot)
Version: 0.13
redis5 ~
**Run Diagnostic Commands:**
Inside the debug container we can run various commands.

`# Check DNS resolution`
nslookup kubernetes.default.svc.cluster.local
Server: 10.96.0.10
Address: 10.96.0.10#53
Name: kubernetes.default.svc.cluster.local
Address: 10.96.0.1
`# Test network connectivity`
curl http://my-service:8080/healthBy using ephemeral pods, you can effectively debug and troubleshoot Kubernetes applications in an isolated and controlled environment, minimizing the risk of impacting production workloads.
# Handling DNS and Network Issues
Now we will go through 2 common troubleshooting scenarios; DNS issues and stateful pods debugging. Let’s see what we have learned in action.

## Common Network Issues
**DNS Resolution Failures**: Issues resolving service names to IP addresses.**Service Unreachable**: Services are not accessible within the cluster.**Pod Communication Issues**: Pods cannot communicate with each other.**Network Policy Misconfigurations**: Incorrect network policies blocking traffic.
## Tools and Commands for Troubleshooting
**kubectl exec**: Run commands in a container to diagnose network issues. **nslookup**: Check DNS resolution. **ping**: Test connectivity between pods and services. **curl**: Verify HTTP connectivity and responses. **traceroute**: Trace the path packets take to reach a destination.
## Example: Diagnosing a DNS Resolution Issue
Let’s walk through an example of diagnosing a DNS resolution issue for a pod named `my-app-pod`
trying to reach a service `my-db-service`
.

**Check DNS Resolution:**
`kubectl exec -it my-app-pod -- nslookup my-db-service`
Alternatively we can use debug pod or ephemeral containers.

Output indicating a problem:

`Server: 10.96.0.10`
Address:10.96.0.10#53
** server can't find my-db-service: NXDOMAIN
**Check CoreDNS Logs:**
Inspect the logs of CoreDNS pods to identify any DNS resolution issues.

`kubectl logs -l k8s-app=kube-dns -n kube-system`
Look for errors or warnings indicating DNS resolution failures.

**Verify Service and Endpoints:**
Ensure that the service and endpoints exist and are correctly configured.

`kubectl get svc my-db-service`
kubectl get endpoints my-db-service
`NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE`
my-db-serviceClusterIP 10.96.0.11 <none> 5432/TCP 1h
`NAME ENDPOINTS AGE`
my-db-service10.244.0.5:5432 1h
**Restart CoreDNS Pods:**
Restart CoreDNS pods to resolve potential transient issues.

`kubectl rollout restart deployment coredns -n kube-system`
**Verify DNS Resolution Again:**
After resolving the issue, verify DNS resolution again:

`kubectl exec -it my-app-pod -- nslookup my-db-service`
Expected output:

`Server: 10.96.0.10`
Address:10.96.0.10#53
`Name: my-db-service.default.svc.cluster.local`
Address:10.96.0.11
## Practical Tips
**Use Network Debug Containers:** Use network debug containers like `nicolaka/netshoot`
for comprehensive network troubleshooting.
`kubectl run netshoot --rm -it --image nicolaka/netshoot -- /bin/bash`
**Monitor Network Metrics:** Use Prometheus and Grafana to monitor network metrics and set up alerts for network issues.
**Implement Redundancy:** Configure redundant DNS servers and failover mechanisms to enhance network reliability.
# Debugging Stateful Applications
Stateful applications in Kubernetes require special considerations for debugging due to their reliance on persistent storage and consistent state across restarts. This section will explore techniques for handling and debugging issues specific to stateful applications.

## What are Stateful Applications?
Stateful applications maintain state information across sessions and restarts, often using persistent storage. Examples include databases, message queues, and other applications that require data persistence.

## Common Issues in Stateful Applications
**Persistent Storage Issues:**Problems with PVCs or PVs can lead to data loss or unavailability.**Pod Start-up Failures:**Errors during pod initialization due to state dependencies.**Network Partitioning:**Network issues affecting communication between stateful pods.**Data Consistency Problems:**Inconsistent data across replicas or restarts.
## Example: Debugging a MySQL StatefulSet
Let’s walk through an example of debugging a MySQL StatefulSet named `my-mysql`
.

**Inspect the StatefulSet:**
`kubectl describe statefulset my-mysql`
Output snippet:

`Name: my-mysql`
Namespace: default
Selector: app=my-mysql
Replicas: 3 desired | 3 total
...
Events:
Type Reason Age From Message
---- ------ ---- ---- -------
Normal SuccessfulCreate 1m statefulset-controller create Pod my-mysql-0 in StatefulSet my-mysql successful
Normal SuccessfulCreate 1m statefulset-controller create Pod my-mysql-1 in StatefulSet my-mysql successful
Normal SuccessfulCreate 1m statefulset-controller create Pod my-mysql-2 in StatefulSet my-mysql successful
**Check Persistent Volume Claims:**
`kubectl get pvc`
kubectl describe pvc data-my-mysql-0
Output snippet:

`Name: data-my-mysql-0`
Namespace: default
Status: Bound
Volume: pvc-1234abcd-56ef-78gh-90ij-klmnopqrstuv
...
**Check Pod Logs:**
`kubectl logs my-mysql-0`
Output snippet:

`2024-01-01T00:00:00.000000Z 0 [Note] mysqld (mysqld 8.0.23) starting as process 1 ...`
2024-01-01T00:00:00.000000Z 1 [ERROR] InnoDB: Unable to lock ./ibdata1 error: 11
**Execute Commands in Pods:**
`kubectl exec -it my-mysql-0 -- /bin/sh`
Inside the pod:

`# Check mounted volumes`
df -h
# Verify MySQL data directory
ls -l /var/lib/mysql
# Check MySQL status
mysqladmin -u root -p status
**Check Network Connectivity:**
`kubectl exec -it my-mysql-0 -- ping my-mysql-1.my-mysql.default.svc.cluster.local`
Output snippet:

`PING my-mysql-1.my-mysql.default.svc.cluster.local (10.244.0.6): 56 data bytes`
64 bytes from 10.244.0.6: icmp_seq=0 ttl=64 time=0.047 ms
# Advanced Debugging Techniques
Advanced debugging techniques in Kubernetes involve using specialized tools and strategies to diagnose and resolve complex issues. This chapter will cover tracing instrumentation and remote debugging.

## Profiling with Jaeger
[Jaeger](https://www.jaegertracing.io/) is an open-source, end-to-end distributed tracing tool that helps monitor and troubleshoot transactions in complex distributed systems. Profiling with Jaeger can provide insights into the performance of your microservices and help identify latency issues.
You can install Jaeger in your Kubernetes cluster using the Jaeger Operator or Helm.

`helm repo add jaegertracing https://jaegertracing.github.io/helm-charts`
helm repo update
helm install jaeger jaegertracing/jaeger
**Instrument Your Application:**
Ensure your application is instrumented to send tracing data to Jaeger. This typically involves adding Jaeger client libraries to your application code and configuring them to report to the Jaeger backend.

Example in a Go application:

`import (`
"github.com/opentracing/opentracing-go"
"github.com/uber/jaeger-client-go"
"github.com/uber/jaeger-client-go/config"
)
func initJaeger(service string) (opentracing.Tracer, io.Closer) {
cfg := config.Configuration{
ServiceName: service,
Sampler: &config.SamplerConfig{
Type: "const",
Param: 1,
},
Reporter: &config.ReporterConfig{
LogSpans: true,
LocalAgentHostPort: "jaeger-agent.default.svc.cluster.local:6831",
},
}
tracer, closer, _ := cfg.NewTracer()
opentracing.SetGlobalTracer(tracer)
return tracer, closer
}
Access the Jaeger UI to view and analyze traces.

`kubectl port-forward svc/jaeger-query 16686:16686`
Open `http://localhost:16686`
in your browser.

## Remote Debugging with mirrord
Mirrord is an open-source tool that enables remote debugging of Kubernetes services by running local processes in the context of your Kubernetes cluster and remote infrastructure.

## Setting Up mirrord
`curl -fsSL https://raw.githubusercontent.com/metalbear-co/mirrord/main/scripts/install.sh | bash`
**Connect to Your Cluster:**
Start a mirrord session to connect your local environment to your Kubernetes cluster.

`mirrord connect`
**Swap Deployment:**
Use mirrord to swap a deployment in your cluster with your local service.

`mirrord exec --target-namespace devops-team --target deployment/foo-app-deployment nodemon server.js`
This command redirects traffic, environment variables, and file operations from your Kubernetes cluster to your local machine, allowing you to debug the service as if it were running locally.

Once the mirrord session is set up, you can use your favorite debugging tools and IDEs to debug the service running on your local machine.

**Set Breakpoints:**Use your IDE to set breakpoints and step through the code.**Inspect Variables:**Inspect variables and application state to identify issues.**Make Changes:**Make code changes and immediately see the effects without redeploying to the cluster.
For a detailed example and more information on using mirrord for debugging, read

[this blog post].
# Additional Tools
In addition to the core Kubernetes commands and open-source tools, there are several other tools available that can enhance your troubleshooting capabilities across various categories. Here are a few noteworthy tools:

# Closing Thoughts
Debugging Kubernetes applications can be a complex and challenging task, but with the right tools and techniques, it becomes much more manageable.

Remember, effective debugging is not just about resolving issues as they arise but also about proactive monitoring, efficient resource management, and a deep understanding of your application’s architecture and dependencies.

By implementing the strategies and best practices outlined in this guide, you can build a robust debugging framework that empowers you to quickly identify, diagnose, and resolve issues, ensuring the smooth operation of your Kubernetes deployments.

Thanks for taking the time to read this post. I hope you found it interesting and informative.

🔗 **Connect with me on ****LinkedIn**

🌐 **Visit my ****Website**

📺 **Subscribe to my ****YouTube Channel**