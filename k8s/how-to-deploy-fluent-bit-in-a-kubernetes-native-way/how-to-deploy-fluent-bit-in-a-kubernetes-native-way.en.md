[Fluent Bit](https://fluentbit.io/) is a widely used open source data collection agent, processor and forwarder that enables you to collect logs, metrics and traces from various sources, filter and transform them, and then forward them to multiple destinations.

While there are various ways to deploy [Fluent Bit in Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=TNS&utm_medium=sponsored-content), managing its life cycle and configurations across multiple clusters or teams can become a complex task.

This is where [Fluent Operator](https://github.com/fluent/fluent-operator/tree/master) comes in; it is a Kubernetes-native way to deploy, manage and configure [Fluent Bit and Fluentd](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd) using custom resource definitions (CRDs).

This guide explores how to deploy [Fluent Bit](https://thenewstack.io/whats-driving-fluent-bit-adoption) using the Fluent Operator, why using an Operator can simplify your logging stack and how to make live configuration changes without restarting pods.

### Prerequisites

* **Kubernetes Cluster:** I will deploy [Fluent Bit](https://chronosphere.io/fluent-bit/?utm_source=TNS&utm_medium=sponsored-content) in a Kubernetes cluster. I will be using Docker Desktop, but any cluster will suffice.
* **Elasticsearch:** I will send logs to Elasticsearch. You can use this [guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html) to follow along.
* **Kubectl:** You can refer to the [official documentation](https://kubernetes.io/docs/tasks/tools/#kubectl) to install the Kubernetes command line tool.
* **Helm CLI:** You can refer to the [official documentation](https://helm.sh/docs/intro/install/) when installing Helm.
* **Familiarity with Fluent Bit concepts:**Refer to the [official documentation](https://docs.fluentbit.io/manual/concepts/data-pipeline) if you’re unfamiliar with concepts such as inputs, outputs, parsers and filters.

## What Is a Kubernetes Operator?

A Kubernetes Operator is a software extension that automates the management of complex applications in a Kubernetes-native way. It utilizes CRDs to define how an application should behave and ensures the system continuously aligns with the desired state.

### Why Operators Are Required

[Kubernetes](https://chronosphere.io/learn/what-is-kubernetes-and-how-does-it-benefit-observability/?utm_source=TNS&utm_medium=sponsored-content) provides basic primitives, such as pods and StatefulSets, for deploying and managing containers, but it doesn’t natively understand how to manage the internal logic of complex applications. For example, you can spin up a database pod, but Kubernetes doesn’t know how to safely back it up, perform upgrades or recover from failure.

That’s where Operators come in. They extend Kubernetes with domain-specific intelligence, automating Day 1 and Day 2 tasks like installation, configuration, updates and failure recovery. This turns previously manual, error-prone workflows into repeatable and self-healing processes.

Operators are crucial for managing stateful applications, such as databases, message brokers and telemetry pipelines. Without an Operator, managing these systems requires custom scripts or manual steps that don’t scale well in dynamic environments.

The Fluent Operator allows you to declaratively configure your logging stack and let the Operator handle orchestration and lifecycle management.

## What Is the Fluent Operator

The Fluent Operator simplifies the deployment and configuration of [Fluent Bit and Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=TNS&utm_medium=sponsored-content) in Kubernetes. It exposes configuration via CRDs such as `ClusterInput`, `ClusterFilter` and `ClusterOutput`, which represent different stages of Fluent Bit’s telemetry pipeline.

Once installed, the Fluent Operator provides:

* Automatic deployment of Fluent Bit as a DaemonSet.
* Declarative configuration through Kubernetes-native CRDs.
* Support for dynamic configuration reloads without restarting pods.
* Optional [Fluentd](https://thenewstack.io/a-guide-to-migrating-from-fluentd-to-fluent-bit) deployment for advanced log routing and multitenant log isolation.

This makes it an ideal choice for teams practicing GitOps or managing large, multitenant Kubernetes clusters.

**Note:** Although Fluent Operator manages both Fluent Bit and Fluentd, this post [focuses on Fluent Bit](https://thenewstack.io/fluent-bit-core-concepts/).

### Key Configuration Options

Once Fluent Bit is deployed using the Fluent Operator, you’ll define the logging pipeline using CRDs. Here’s a quick overview of the most important ones:

* **`FluentBit`**: Defines the Fluent Bit DaemonSet and its configs.
* **`ClusterFluentBitConfig`**: Selects cluster-level input/filter/output plugins and generates the final config into a Secret.
* **`ClusterInput`**: Defines where logs come from. For example, you can configure Fluent Bit to tail container logs or collect system logs.
* **`ClusterParser`**: Parses incoming logs using regex, JSON or custom formats.
* **`ClusterFilter`**: Filters and enriches log records.
* **`ClusterOutput`**: Defines where to send logs, such as Elasticsearch, Loki or Kafka.

For more information on the available CRDs for Fluent Bit, refer to this [documentation](https://github.com/fluent/fluent-operator/tree/master?tab=readme-ov-file#fluent-bit).

### How To Configure a Pipeline With CRDs

Each **`ClusterInput`**, **`ClusterParser`**, **`ClusterFilter`**, **`ClusterMultilineParser`** and **`ClusterOutput`** represents a Fluent Bit config section, which is selected by **`ClusterFluentBitConfig`** via label selectors. Fluent Operator watches those objects, constructs the final configuration and then creates a Secret to store the configuration, which will be mounted into the Fluent Bit DaemonSet. The entire workflow looks like this:

[![Fluent Operator watches those objects, constructs the final configuration and then creates a Secret to store the configuration, which will be mounted into the Fluent Bit DaemonSet.](https://cdn.thenewstack.io/media/2025/07/c6b8b673-fluentbit-workflow.png)](https://cdn.thenewstack.io/media/2025/07/c6b8b673-fluentbit-workflow.png)

Source: Chronosphere.

## Deploying Fluent Bit Using the Fluent Operator

I will deploy a Fluent Bit pipeline that collects logs from Kubernetes pods and Systemd and sends them to Elasticsearch, as depicted in the diagram below:

[![Deploy a Fluent Bit pipeline that collects logs from Kubernetes pods and Systemd and sends them to Elasticsearch](https://cdn.thenewstack.io/media/2025/07/69030e66-deploy-pipeline.png)](https://cdn.thenewstack.io/media/2025/07/69030e66-deploy-pipeline.png)

Source: Chronosphere.

### Instructions

1. **Install the Operator using Helm.** Note that the behavior of this chart can be modified by adjusting the [values.yaml](https://github.com/fluent/fluent-operator/blob/master/charts/fluent-operator/values.yaml) file.  

   ```
   export FLUENT_OPERATOR_CONTAINER_RUNTIME="docker" # or "cri-o", "containerd" depending on the container runtime being used (see `values.yaml`)

   helm repo add fluent https://fluent.github.io/helm-charts
   helm upgrade --install fluent-operator fluent/fluent-operator \
     --create-namespace \
     --set containerRuntime=${FLUENT_OPERATOR_CONTAINER_RUNTIME}
   ```
2. **Wait for the pods to run.** Now, execute the following command to check the status of Pods. Wait until the status of the pod changes to `Running`.  

   ```
   kubectl get pods

   ## Expected Output
   NAME                               READY   STATUS    RESTARTS   AGE
   fluent-bit-5k954                   1/1     Running   0          2s
   fluent-operator-5b55477974-7phj7   1/1     Running   0          11s
   ```
3. **View the default configuration.** To list what Kubernetes resources were created, run the following command. This will list the resource type along with its name.  

   ```
   helm get manifest fluent-operator -n default | \
     grep -E '^(kind:|  name:)' | \
     sed 'N;s/\n/ /'

   ## Expected Output
   ...
   kind: ClusterFilter   name: kubernetes
   kind: ClusterFilter   name: systemd
   kind: ClusterFluentBitConfig   name: fluent-bit-config
   kind: ClusterInput   name: "docker"
   kind: ClusterInput   name: tail
   kind: FluentBit   name: fluent-bit
   ```

     
   By default, apart from setting up the Fluent Operator pod, this chart also installs and configures Fluent Bit to collect and send Kubernetes logs to a null destination ([this flag](https://github.com/fluent/fluent-operator/blob/master/charts/fluent-operator/values.yaml#L9) can be used to disable this behavior). The default Fluent Bit pipeline configuration generated by this chart can be viewed using the command below.  

   ```
   kubectl get secret fluent-bit-config -o jsonpath="{.data.fluent-bit\.conf}" | base64 --decode
   ```

     
   Here is a graphical representation of the deployed pipeline:

   [![Deployed pipeline](https://cdn.thenewstack.io/media/2025/07/dd112b0d-deployed-pipeline.png)](https://cdn.thenewstack.io/media/2025/07/dd112b0d-deployed-pipeline.png)

   Source: Chronosphere.
4. **Add Elasticsearch output.** To add an Elasticsearch output, use the `ClusterOutput` CRD.Create an `es-credentials.yaml` file with the content below. This Kubernetes secret holds the username and password to connect to the Elasticsearch cluster.  

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: es-credentials
     namespace: default
   type: Opaque
   data:
     user: <your-base64-encoded-username>
     password: <your-base64-encoded-password>
   ```

     
   Next, create an `elastic-output.yaml` file with the contents below.  

   ```
   apiVersion: fluentbit.fluent.io/v1alpha2
   kind: ClusterOutput
   metadata:
     name: es
     labels:
       fluentbit.fluent.io/enabled: "true"
       fluentbit.fluent.io/component: logging
   spec:
     matchRegex: (?:kube|service)\.(.*)
     es:
       host: <elastic-search-host>
       port: 9200
       suppressTypeName: "On"
       httpUser:
         valueFrom:
           secretKeyRef:
             name: es-credentials
             key: user
       httpPassword: 
         valueFrom:
           secretKeyRef:
             name: es-credentials
             key: password
       logstashPrefix: ks-logstash-log
       timeKey: "@timestamp"
   ```

     
   Now apply the above configuration.  

   ```
   ubectl apply -f es-credentials.yaml
   kubectl apply -f elastic-output.yaml
   ```
5. **Verify that the Fluent Bit config is updated.** You should see the `es` plugin at the end.  

   ```
   kubectl get secret fluent-bit-config -o jsonpath="{.data.fluent-bit\.conf}" | base64 --decode

   ## Expected Output
   [Output]
       Name    es
       Match_Regex    (?:kube|service)\.(.*)
       Host    192.168.0.100
   ...
   ```
6. **Verify logs in Elasticsearch.** Note: I created indices in Elasticsearch with the pattern **`ks-logstash-log-*`**. To view these logs in Kibana, you need to create a [Data View](https://www.elastic.co/docs/explore-analyze/find-and-organize/data-views).

   [![Elasticsearch GUI](https://cdn.thenewstack.io/media/2025/07/48ae4a56-elastic-indices.png)](https://cdn.thenewstack.io/media/2025/07/48ae4a56-elastic-indices.png)

   Source: Chronosphere.

## Live/Hot Reloading Configuration

One important feature of Fluent Operator is the ability to reload configuration without restarting the Fluent Bit pod.

To enable Fluent Bit to pick up and use the latest configuration whenever the Fluent Bit configuration changes, a wrapper called Fluent Bit Watcher is added to restart the Fluent Bit process as soon as Fluent Bit configuration changes are detected.

This way, the Fluent Bit pod does not need to be restarted to reload the new configuration. The Fluent Bit config is reloaded in this manner because Fluent Bit itself does not have a built-in reloading interface.

[![Fluent Bit pod workflow](https://cdn.thenewstack.io/media/2025/07/ef0b141c-hot-reloading-pipeline.png)](https://cdn.thenewstack.io/media/2025/07/ef0b141c-hot-reloading-pipeline.png)

Source: Chronosphere.

### Instructions

1. **Check the Fluent Bit pod age.** To verify that the pod did not restart during configuration changes, check the age of the pod. Execute the command below to check the pod’s current age.  

   ```
   kubectl get pods -l app.kubernetes.io/name=fluent-bit

   ## Expected Output
   NAME               READY   STATUS    RESTARTS   AGE
   fluent-bit-5k954   1/1     Running   0          68m
   ```
2. **Make configuration changes.** To add another `ClusterOutput` CRD, create an `es-hot-reload.yaml` file with the content below. This is similar to the previous CRD, but I changed the `logstashPrefix` in this configuration from `ks-logstash-log` to `new-ks-logstash-log`.  

   ```
   apiVersion: fluentbit.fluent.io/v1alpha2
   kind: ClusterOutput
   metadata:
     name: es-hot-reload
     labels:
       fluentbit.fluent.io/enabled: "true"
       fluentbit.fluent.io/component: logging
   spec:
     matchRegex: (?:kube|service)\.(.*)
     es:
       host: <elastic-search-host>
       port: 9200
       suppressTypeName: "On"
       httpUser:
         valueFrom:
           secretKeyRef:
             name: es-credentials
             key: user
       httpPassword: 
         valueFrom:
           secretKeyRef:
             name: es-credentials
             key: password
       logstashPrefix: new-ks-logstash-log
       timeKey: "@timestamp"
   ```

     
   Now, apply the above configuration.
3. **Verify the pod time.** You should see that the Pod did not restart, and its age remains relatively unchanged.  

   ```
   kubectl get pods -l app.kubernetes.io/name=fluent-bit

   ## Expected Output
   NAME               READY   STATUS    RESTARTS   AGE
   fluent-bit-5k954   1/1     Running   0          68m
   ```
4. ****Verify the Fluent Bit config has been updated with the latest output.****  

   ```
   kubectl get secret fluent-bit-config -o jsonpath="{.data.fluent-bit\.conf}" | base64 --decode
   ```
5. **Verify logs in Elasticsearch.** Note: I have only created indices in Elasticsearch with the pattern **`new-ks-logstash-log-*`**. To view these logs in Kibana, you need to create a [Data View](https://www.elastic.co/docs/explore-analyze/find-and-organize/data-views).

## Conclusion

You can utilize Fluent Operator to manage Fluent Bit deployments in a scalable, Kubernetes-native way.

Fluent Operator streamlines the configuration of complex logging pipelines using CRDs, while enabling dynamic updates without pod restarts. Whether you’re operating in a single cluster or across multiple environments, Fluent Operator simplifies observability and reduces operational overhead.

If you want to learn more or have questions, join the next virtual [Fluent Bit office hours](https://www.meetup.com/fluent-community-meeting/events) or join the [Fluent Bit Slack](https://www.launchpass.com/fluent-all).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/7d96682e-sharadregoti.jpeg)

Sharad Regoti is a CKA & CKS certified software engineer based in Mumbai and who contributes technical articles on behalf of Chronosphere.

Read more from Sharad Regoti](https://thenewstack.io/author/sharad-regoti/)