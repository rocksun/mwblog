# Building a Metrics System with Thanos and Kubernetes
Metrics are the backbone of observability in any distributed system, and in Kubernetes environments, Prometheus is often the tool of choice.

However, scaling Prometheus and retaining long-term metrics data can be challenging. Thanos is a project that extends Prometheus with additional capabilities, such as scalable storage, global querying across multiple Prometheus instances, and highly available metrics. This article explores how to build a robust, scalable, and resilient metrics system using Thanos on Kubernetes, covering everything from setup to best practices.

# What the H#ck is a Metrics System with Thanos and Kubernetes?
A metrics system built with **Thanos and Kubernetes** is like taking your Prometheus monitoring to the next level. Prometheus is fantastic for scraping and storing metrics from your Kubernetes clusters, but it hits limits when you need to scale, store metrics long-term, or query across multiple clusters. Enter **Thanos**, a tool that layers on top of Prometheus to solve these problems by offering **scalable storage**, **global querying** across clusters, and **high availability** for failover and redundancy.

With Thanos, you’re not just collecting metrics; you’re building a resilient system that allows you to store and access metrics across distributed environments without the typical headaches of managing multiple Prometheus instances independently. This makes Thanos a go-to solution for organizations with large-scale Kubernetes deployments or those looking to retain metrics for long-term analysis.

# Why Do I Need One?
If you’re just running a small Kubernetes cluster, Prometheus alone might be enough for you. But once your cluster scales, or you have multiple clusters across different regions or environments, **Prometheus on its own starts to show limitations**:

**Metrics Retention**: Prometheus wasn’t designed for long-term storage. You might want to store metrics for months or years, but Prometheus will only retain data for a limited period.**High Availability**: Prometheus doesn’t offer built-in redundancy. If your Prometheus instance goes down, you lose metrics data until it’s back online.**Global Queries**: Prometheus is a single-node system, so querying across multiple clusters isn’t supported natively.
Thanos solves these problems by extending Prometheus with **cloud-native features** that allow you to store metrics in object storage (e.g., Amazon S3), query across multiple clusters in real-time, and ensure metrics availability even when components fail.

# Components of a Metrics System with Thanos and Kubernetes
Thanos isn’t just one tool — it’s a suite of components that work together to create a full-featured metrics system:

**Thanos Sidecar**: This runs alongside each Prometheus instance, shipping metrics data to object storage and allowing Prometheus to be part of a larger Thanos architecture.**Querier**: This component aggregates data from multiple Prometheus instances and other Thanos components, providing a unified view of your metrics.**Store Gateway**: It retrieves older metrics from object storage, making it possible to query data beyond what Prometheus retains locally.**Compactor**: Reduces the footprint of stored metrics by compacting and downsampling them, improving both query performance and storage efficiency.**Ruler**: Evaluates Prometheus-style recording and alerting rules but on historical data, enabling alerts on long-term trends.
Each of these components plays a role in ensuring that your metrics system scales as your infrastructure grows, and that you can access long-term data without managing huge Prometheus instances on their own.

# Before We Start, a Couple of Recommendations…
**Plan your storage strategy**: When setting up Thanos, keep in mind that storing large volumes of metrics data in the cloud can get expensive. Choose your storage provider and lifecycle management policies wisely (e.g., move old metrics to cheaper storage tiers).**Automate deployments**: Use Kubernetes tools like Helm to manage your Thanos and Prometheus deployments. This will make scaling and updating the system much easier as your infrastructure grows.**Monitor Thanos components**: Don’t just monitor your applications — set up alerts for the health of your Thanos components too. If your Querier or Sidecar goes down, you’ll want to know immediately.
Now that you know why a metrics system with Thanos and Kubernetes is powerful and what components make it work, let’s dive into the setup and get everything running.

# Deploying Thanos with Kubernetes: A Real-World Tutorial
In this step-by-step guide, we’re going to walk through deploying Thanos with Kubernetes in a real-world scenario. The goal is to set up a scalable, long-term metrics system for Kubernetes clusters using Prometheus as the core metrics collector and Thanos as the layer that extends Prometheus’ capabilities. By the end of this tutorial, you’ll have a robust, distributed system that can handle long-term storage, querying across multiple Prometheus instances, and high availability.

# Step 1: Install Prometheus on Kubernetes
The first step in setting up your metrics system is to get Prometheus up and running in your Kubernetes cluster. If Prometheus isn’t installed yet, you can use **Helm** to deploy it quickly.

Begin by adding the Helm repository for Prometheus charts:

`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
helm repo update
Once the repository is updated, you can install Prometheus by running:

`helm install prometheus prometheus-community/prometheus`
After running this command, Helm will install the Prometheus server, and you can check its status by listing the running pods:

`kubectl get pods -l "app=prometheus"`
If Prometheus is up and running, you’ll see one or more pods with names starting with **prometheus**. If the pods are not running or stuck in an error state, you may need to check the logs with:

`kubectl logs <prometheus-pod-name>`
# Step 2: Set Up Thanos Sidecar
The Thanos Sidecar is crucial for integrating Prometheus with Thanos. It will run alongside Prometheus, forwarding its data to long-term storage (e.g., Amazon S3).

Before configuring the sidecar, if you’re using Amazon S3, create a new S3 bucket to store the metrics:

`aws s3api create-bucket --bucket my-thanos-bucket --region us-east-1`
Now, you need to update the Prometheus deployment to include the Thanos Sidecar. You’ll do this by adding the Thanos container to the existing Prometheus deployment. Here’s an example deployment configuration for **Prometheus with Thanos Sidecar**:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: prometheus
spec:
replicas: 1
template:
spec:
containers:
- name: prometheus
image: prom/prometheus:v2.43.0
args:
- "--config.file=/etc/prometheus/prometheus.yml"
- "--storage.tsdb.path=/prometheus"
ports:
- containerPort: 9090
- name: thanos-sidecar
image: quay.io/thanos/thanos:v0.32.1
args:
- sidecar
- --tsdb.path=/prometheus
- --objstore.config-file=/etc/thanos/s3.yaml
ports:
- containerPort: 10902
volumeMounts:
- name: prometheus-data
mountPath: /prometheus
- name: s3-config
mountPath: /etc/thanos/s3.yaml
subPath: s3.yaml
volumes:
- name: s3-config
configMap:
name: s3-config
Make sure you create the **s3.yaml** file containing the necessary S3 credentials for your bucket:

`type: S3`
config:
bucket: my-thanos-bucket
endpoint: s3.amazonaws.com
region: us-east-1
access_key: YOUR_ACCESS_KEY
secret_key: YOUR_SECRET_KEY
Once you’ve configured the sidecar, apply the changes to your Kubernetes cluster:

`kubectl apply -f prometheus-thanos-deployment.yaml`
This will deploy both Prometheus and the Thanos sidecar, and the sidecar will start sending Prometheus data to the S3 bucket.

# Step 3: Deploy the Thanos Querier
The **Thanos Querier** allows you to query data across multiple Prometheus instances, providing a global view of your metrics. This is especially useful when you have multiple Kubernetes clusters or regions and want a unified metrics system.

Here’s an example deployment for the Thanos Querier:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: thanos-querier
spec:
replicas: 1
template:
spec:
containers:
- name: thanos-querier
image: quay.io/thanos/thanos:v0.32.1
args:
- query
- --http-address=0.0.0.0:9090
- --store=dnssrv+_grpc._tcp.thanos-sidecar.default.svc.cluster.local:10901
- --store=dnssrv+_grpc._tcp.thanos-store.default.svc.cluster.local:10901
ports:
- containerPort: 9090
In this configuration, the Querier is set up to pull data from the Thanos Sidecar and Store Gateway via DNS service discovery. The Querier will act as a centralized point for querying metrics.

Deploy the Thanos Querier to your cluster by applying the YAML:

`kubectl apply -f thanos-querier-deployment.yaml`
To test the Querier, forward the service port to your local machine:

`kubectl port-forward svc/thanos-querier 9090:9090`
Now, open your browser and go to [ http://localhost:9090](http://localhost:9090) to interact with the Thanos Querier UI and start querying data across Prometheus instances.

# Step 4: Deploy Thanos Store Gateway
The Thanos **Store Gateway** retrieves historical metrics stored in the S3 bucket. This allows you to query data beyond the retention limits of Prometheus itself.

Here’s an example configuration for the Thanos Store Gateway deployment:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: thanos-store
spec:
replicas: 1
template:
spec:
containers:
- name: thanos-store
image: quay.io/thanos/thanos:v0.32.1
args:
- store
- --data-dir=/data
- --objstore.config-file=/etc/thanos/s3.yaml
ports:
- containerPort: 10901
volumeMounts:
- name: data
mountPath: /data
- name: s3-config
mountPath: /etc/thanos/s3.yaml
subPath: s3.yaml
volumes:
- name: data
emptyDir: {}
- name: s3-config
configMap:
name: s3-config
Apply this configuration to deploy the Thanos Store Gateway:

`kubectl apply -f thanos-store-deployment.yaml`
The Store Gateway will start retrieving older metrics from your S3 bucket, making them available for queries through the Thanos Querier.

# Step 5: Verify and Test Your Setup
Once all the Thanos components are running, you should test the entire setup to ensure that metrics are being stored and queried correctly.

Start by checking that all your Prometheus and Thanos pods are running:

`kubectl get pods`
If everything is running as expected, use the Thanos Querier UI to execute queries. Verify that you can retrieve both recent and historical data from the S3 bucket.

You can also check the logs of the Thanos components to ensure they are communicating correctly:

`kubectl logs <thanos-querier-pod-name>`
kubectl logs <thanos-store-pod-name>
kubectl logs <thanos-sidecar-pod-name>
If any component isn’t working as expected, these logs will provide clues on what’s going wrong.

# Best Practices
# Best Practices for a Metrics System with Thanos and Kubernetes
Deploying Thanos on Kubernetes is a powerful way to manage metrics at scale, but to ensure that your setup performs efficiently and remains cost-effective, there are several best practices to follow. These will not only improve performance but also reduce overhead and make long-term metric retention more manageable.

# Use Downsampling to Reduce Query Load
As the volume of metrics grows, querying the data can become slow and resource-intensive. This is where **downsampling** comes into play. Downsampling aggregates older metrics, reducing their granularity while preserving essential trends over time. By configuring **Thanos Compactor** to downsample your metrics, you can significantly improve query performance, reduce storage costs, and lighten the load on your object storage.

In a typical Thanos setup, the **Compactor** handles two tasks: compacting time series into smaller blocks and downsampling older data. Here’s an example of how to configure the Compactor:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: thanos-compactor
spec:
replicas: 1
template:
spec:
containers:
- name: thanos-compactor
image: quay.io/thanos/thanos:v0.32.1
args:
- compact
- --data-dir=/data
- --objstore.config-file=/etc/thanos/s3.yaml
- --retention.resolution-raw=30d
- --retention.resolution-5m=180d
- --retention.resolution-1h=1y
volumeMounts:
- name: data
mountPath: /data
- name: s3-config
mountPath: /etc/thanos/s3.yaml
subPath: s3.yaml
volumes:
- name: data
emptyDir: {}
- name: s3-config
configMap:
name: s3-config
In this configuration, the **Compactor** is set to retain raw, high-resolution data for 30 days, 5-minute downsampled data for 180 days, and 1-hour downsampled data for a year. The Compactor automatically creates these downsampled blocks, making it easier to query historical data without burdening the system.

Make sure to tune the retention periods based on your data needs and storage capacity. Downsampling is ideal when you don’t need fine-grained detail for older metrics but still want to preserve long-term trends for analysis or compliance.

# Leverage Kubernetes Service Discovery
Thanos Querier can automatically discover Prometheus instances using **Kubernetes service discovery**. This simplifies the process of scaling up or down without having to manually configure new Prometheus instances. Kubernetes’ native DNS-based service discovery allows Thanos to dynamically discover services within the cluster, making the system more flexible and easier to manage.

To enable service discovery in Thanos Querier, you can modify the deployment configuration as follows:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: thanos-querier
spec:
replicas: 1
template:
spec:
containers:
- name: thanos-querier
image: quay.io/thanos/thanos:v0.32.1
args:
- query
- --http-address=0.0.0.0:9090
- --store=dnssrv+_grpc._tcp.prometheus.default.svc.cluster.local:10901
- --store=dnssrv+_grpc._tcp.thanos-store.default.svc.cluster.local:10901
In this setup, the `dnssrv`
address is used to auto-discover any Prometheus instances and Thanos Store Gateways running within the Kubernetes cluster. By leveraging Kubernetes DNS-based service discovery, Thanos can dynamically scale without any manual configuration when new Prometheus instances are added.

# Secure Object Storage Access
When using cloud object storage like **Amazon S3** or **Google Cloud Storage** for storing your metrics, securing the access credentials is critical. Instead of hardcoding the credentials in your YAML files, you should use **Kubernetes Secrets** to manage sensitive information like your object storage access keys.

Here’s how to securely store your S3 credentials in a Kubernetes Secret:

`kubectl create secret generic s3-credentials \`
--from-literal=access_key=YOUR_ACCESS_KEY \
--from-literal=secret_key=YOUR_SECRET_KEY
Once the secret is created, reference it in your Thanos sidecar or store configurations:

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: thanos-sidecar
spec:
replicas: 1
template:
spec:
containers:
- name: thanos-sidecar
image: quay.io/thanos/thanos:v0.32.1
args:
- sidecar
- --tsdb.path=/prometheus
- --objstore.config-file=/etc/thanos/s3.yaml
env:
- name: S3_ACCESS_KEY
valueFrom:
secretKeyRef:
name: s3-credentials
key: access_key
- name: S3_SECRET_KEY
valueFrom:
secretKeyRef:
name: s3-credentials
key: secret_key
volumeMounts:
- name: s3-config
mountPath: /etc/thanos/s3.yaml
subPath: s3.yaml
By using **Kubernetes Secrets**, you ensure that your access keys are encrypted and safely stored, reducing the risk of accidental exposure.

# Monitor Thanos Components
Monitoring the health of your Thanos components is just as important as monitoring the health of your applications. If any Thanos component like the Querier, Sidecar, or Store Gateway fails, it could impact your metrics system, leading to missing data or failed queries.

The first step is to set up **Prometheus alerting rules** to track the status of Thanos components. For example, you can monitor the **up** status of Thanos instances with Prometheus using the following alerting rule:

`groups:`
- name: thanos-alerts
rules:
- alert: ThanosDown
expr: up{job="thanos"} == 0
for: 5m
labels:
severity: critical
annotations:
summary: "Thanos instance down"
description: "The Thanos {{ $labels.instance }} instance is down for more than 5 minutes."
This alert will fire if any Thanos instance is down for more than 5 minutes, allowing you to quickly detect and respond to failures in the system.

You should also consider using **Grafana** for visualizing the performance of your Thanos components and creating dashboards that track the health and performance of each service in real-time.

# Optimize Storage Costs
Storing large volumes of metrics can become costly, especially if you’re retaining high-resolution data for long periods. To optimize costs, use **lifecycle policies** in your object storage to automatically move older data to cheaper storage tiers like Amazon S3’s **Glacier** or **Google Cloud Nearline Storage**.

For example, in Amazon S3, you can configure a lifecycle policy that transitions older data to Glacier after 90 days:

`{`
"Rules": [
{
"ID": "MoveOlderDataToGlacier",
"Filter": {
"Prefix": ""
},
"Status": "Enabled",
"Transitions": [
{
"Days": 90,
"StorageClass": "GLACIER"
}
],
"NoncurrentVersionTransitions": [],
"Expiration": {
"Days": 365
}
}
]
}
Applying this policy ensures that you’re only paying for high-performance storage for recent data, while older data is moved to a cheaper, slower storage class.

In Google Cloud Storage, you can configure a similar lifecycle rule to transition objects to **Nearline** or **Coldline** storage after a set number of days. This strategy helps in optimizing your storage costs, especially when retaining large amounts of historical metrics data.

# Conclusion
Setting up a metrics system with **Thanos** and **Kubernetes** can feel like a big task, especially when you start thinking about long-term storage, high availability, and global querying across multiple clusters. But the good news is that it doesn’t have to be a daunting process. By integrating Thanos with Prometheus, you tackle some of the biggest challenges in observability for Kubernetes environments — scalability, redundancy, and cost management.

Throughout this guide, I’ve walked you through deploying Prometheus and Thanos step by step, configuring downsampling, securing object storage access, and using Kubernetes service discovery. Each of these steps helps create a more robust, efficient metrics system that scales with your infrastructure. The important thing here is to keep your setup flexible, monitor the health of your components, and optimize for both performance and cost as your data grows.

Now, I’d love to hear your thoughts! If you’ve got additional tips or encountered any interesting challenges while deploying Thanos, drop your suggestions in the comments below. Let’s make this a collaborative resource where everyone can benefit.

# Learn More
## 15 Best Kubernetes Cost Optimization Tools for 2024
### Financial times are tough, that’s no secret. Most organizations need to scale their offering to their market and…
overcast.blog

## 11 Ways to Optimize Kubernetes Load Balancing
### Optimizing load balancing in Kubernetes is crucial for maintaining the high availability, scalability, and performance…
overcast.blog

## 15 Cloud-Native DevOps Tools You Should Know
### Managing dynamic and scalable environments efficiently requires cloud-native DevOps tools. These tools automate…
overcast.blog