[](https://github.com/developer-friendly/blog/blob/main/docs/posts/2024/0016-victoria-metrics.md) [](https://github.com/developer-friendly/blog/raw/main/docs/posts/2024/0016-victoria-metrics.md)
# Unlocking the Power of VictoriaMetrics: A Prometheus Alternative
[¶](#unlocking-the-power-of-victoriametrics-a-prometheus-alternative)
One of the main tasks of an operations team in any organization is to provide a solid and robust monitoring solution for the platform, the application, and the entire infrastructure.
Monitoring enables business owners to understand how their applications behave in a production setup, how to optimize it, and how to proactively fine-tune & forecast the future growth of the platform.
In this blog post, we will explore what Victoria Metrics has to offer, how to set it up and configure it to work as a drop-in replacement for Prometheus and a datastore for Grafana.
## Why Monitoring is Crucial?
[¶](#why-monitoring-is-crucial)
Monitoring is crucial because it gives you real-time & historic insights into the health and performance of your systems, helping you catch issues before they escalate into bigger problems.
Consider monitoring as a constant health check-up for the systems and infrastructure, ensuring everything runs smoothly and efficiently.
With successful monitoring, one can optimize resource usage, prevent downtime, quickly troubleshoot unexpected behaviors, and do capacity planning, ultimately saving time and reducing costs.
Additionally, it provides valuable data for improving future performance and planning capacity, making it an indispensable part of managing any tech environment.
## Introduction to Victoria Metrics
[¶](#introduction-to-victoria-metrics)
Victoria Metrics
is a high-performance 1 , cost-effective time series database designed for monitoring and observability. It's known for its speed, efficiency, and scalability, making it an excellent choice for handling large volumes of data effortlessly. [2](#fn:last9-prometheus-comparison)
Furthermore, it’s fully compatible with Prometheus
, offering an effortless transition for those looking to migrate their current monitoring setup. 3
## Why Victoria Metrics?
[¶](#why-victoria-metrics)
Victoria Metrics stands out because of multiple factors.
For one, it is scalable, which is a perfect choice for handling vast amounts of time series data
. 4
Also, it’s designed to be a drop-in replacement for Prometheus, offering
**faster queries**, better compression , and multi-tenant support. 5
For me personally, I came across Victoria Metrics looking for a long-term storage solution for Prometheus. Looking through the available tools, the most compelling ones were Victoria Metrics and Thanos.
I chose Victoria Metrics because it was far more resource efficient and a lot easier to set up and configure. With Thanos, there's a huge learning curve and the overhead and maintainability cost outweighed the benefits.
## Key Features of Victoria Metrics
[¶](#key-features-of-victoria-metrics)
- Delivers high performance with fast query capabilities
. [6](#fn:vm-vs-prom-perf)
- Offers efficient data compression to save storage space, e.g., it provides a decent performance on HDD storage.
- Ensures smooth handling of multiple data sources with multi-tenant support.
- Provides effortless compatibility with Prometheus for easy integration.
- Scales easily to manage large datasets.
## Victoria Metrics vs. Prometheus
[¶](#victoria-metrics-vs-prometheus) **Resource Utilization**: Victoria Metrics is more memory and CPU efficient than Prometheus, making it a cost-effective solution. I have personally seen as much as a 50% reduction in memory footprint when switching to Victoria Metrics. **Long-term Storage**: Victoria Metrics has native support for long-term storage, whereas with Prometheus, you need to set up a separate solution like Thanos . [7](#fn:prometheus-long-term-storage) **Scalability**: Victoria Metrics is designed to be scalable both vertically and horizontally. Prometheus, on the other hand, falls short in that regard and requires additional tools like Thanos to scale . [8](#fn:last9-vm-vs-thanos)
## Deploy Victoria Metrics
[¶](#deploy-victoria-metrics)
For this guide, we wil use
[Kubernetes](/category/kubernetes/) to deploy Victoria Metrics. Feel free to pick an easy way to create your cluster, like Minikube, Kind, or K3s.
We have other guides in our archive to set up a Kubernetes cluster if you are interested:
[Kubernetes The Hard Way](../../../03/03/kubernetes-the-hard-way/) [How to Install Lightweight Kubernetes on Ubuntu 22.04](../../../03/22/how-to-install-lightweight-kubernetes-on-ubuntu-2204/) [Create an Azure AKS Cluster with OpenTofu](../../../04/29/external-secrets-operator-fetching-aws-ssm-parameters-into-azure-aks/#step-0-setting-up-azure-managed-kubernetes-cluster)
Diagram below shows the installation architecture for this blog post.
flowchart TD
kubeStateMetrics([kube-state-metrics])
nodeExporter([node-exporter])
vmagent([VMAgent])
externalSources["External Sources"]
subgraph "VictoriaMetrics Cluster"
vminsert([VMInsert])
vmstorage([VMStorage])
vmselect([VMSelect])
vminsert -- "Store Metrics" --> vmstorage
vmstorage -- "Query Metrics" --> vmselect
end
grafana([Grafana])
kubeStateMetrics -- "ServiceMonitor" --> vmagent
nodeExporter -- "ServiceMonitor" --> vmagent
externalSources -- "/metrics endpoint" --> vmagent
vmagent -- "Remote Write URL" --> vminsert
vmselect -- "Datasource for Dashboards" --> grafana
### Victoria Metrics Operator
[¶](#victoria-metrics-operator)
The official provided operator
for Victoria Metrics has a lot of benefits compared to alternative one-shot installation methods. 9
With the Victoria Metrics operator you get to decide the architecture of your Victoria Metrics using one or multiple CRD resources. It is more flexible in the long run.
We are using
[FluxCD](/category/fluxcd/) as our [GitOps](/category/gitops/) tool of choice, but feel free to use any other tool you are comfortable with. apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: HelmRepository
metadata:
name: victoria-metrics
spec:
interval: 60m
url: https://victoriametrics.github.io/helm-charts/
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
name: victoria-metrics-operator
spec:
chart:
spec:
chart: victoria-metrics-operator
sourceRef:
kind: HelmRepository
name: victoria-metrics
version: 0.x
interval: 30m
maxHistory: 10
releaseName: victoria-metrics-operator
timeout: 5m
resources:
- namespace.yml
- repository.yml
- release.yml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
name: victoria-metrics-operator
namespace: flux-system
spec:
force: false
interval: 5m
path: ./victoria-metrics-operator
prune: true
sourceRef:
kind: GitRepository
name: flux-system
targetNamespace: monitoring
wait: true
Finally, to deploy this stack:
### Victoria Metrics CRDs
[¶](#victoria-metrics-crds)
Having the Victoria Metrics Operator installed, we can query and see that we have the corresponding CRDs available in our Kubernetes cluster.
And the output:
![Click to zoom in Victoria Metrics Operator CRDs](/static/img/2024/0016/vm-api-resources.webp)
![Click to zoom in Victoria Metrics Operator CRDs](/static/img/2024/0016/vm-api-resources.webp)
Just by looking at the CRDs here, you can quickly realize how powerful this mode of installation is and how much flexibility it provides. Because, at any point in time, you can scale your VictoriaMetrics instance components, resize or completely replace them with a different architecture.
For example, one of the quickest ways to provide authentication on top of any of the Victoria Metrics component instances is to create a
VMAuth as a proxy and one or more
VMUser CRD
. 10
See an example below.
---
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAuth
metadata:
name: auth-proxy
spec:
selectAllByDefault: true
---
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMUser
metadata:
name: john-doe
spec:
generatePassword: true
targetRefs:
- static:
urls:
- http://victoria-metrics.monitoring:8428
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
name: vmproxy
spec:
hostnames:
- vmproxy.developer-friendly.blog
parentRefs:
- group: gateway.networking.k8s.io
kind: Gateway
name: developer-friendly-blog
namespace: cert-manager
sectionName: https
rules:
- backendRefs:
- kind: Service
name: vmauth-auth-proxy
port: 8427
filters:
- responseHeaderModifier:
set:
- name: Strict-Transport-Security
value: max-age=31536000; includeSubDomains; preload
type: ResponseHeaderModifier
matches:
- path:
type: PathPrefix
value: /
A few seconds after applying these resources, a new Kubernetes Service and a Secret in the target namespace will be created.
We can get the corresponding password for the user by running:
kubectl get \
-n monitoring \
secret/vmuser-john-doe \
-o jsonpath='{.data.password}' | \
base64 -d -
Having the password we grabbed from the Secret, and the address from the
HTTPRoute resource, we will be prompted for basic HTTP authentication upon the first visit to the address.
![Click to zoom in VMAuth Authentication Proxy](/static/img/2024/0016/vmauth-basic-auth.webp)
![Click to zoom in VMAuth Authentication Proxy](/static/img/2024/0016/vmauth-basic-auth.webp)
The best thing about this architecture is that any piece of it is replaceable by your preferred tooling. If you choose to use a different authentication proxy server such as
[Ory Oathkeeper](/category/oathkeeper/) to take advantage of your current Identity Provider, you definitely can . 11
## Migration From Kube Prometheus Stack
[¶](#migration-from-kube-prometheus-stack)
At this point, we will assume that you have the Kube Prometheus Stack
installed in your cluster. Due to the massive adoption of the Kube Prometheus Stack, this assumption is not far-fetched. 12
That stack comes with a number of CRDs that make it easier for discovering new targets for your Prometheus server.
Upon the
[installation of Victoria Metrics Operator](#victoria-metrics-operator), you are, by default and unless explicitly disabled, opting in for automatic conversion of every one of the Prometheus Stack's CRDs into that of Victoria Metrics Operator . 13
That, in essence, means that the following conversion table applies to you:
|Kube Prometheus Stack CRD
|Victoria Metrics Operator CRD
|
ServiceMonitor
|
VMServiceScrape
|
PodMonitor
|
VMPodScrape
|
Probe
|
VMProbe
|
PrometheusRule
|
VMRule
|
AlertmanagerConfig
|
VMAlertmanagerConfig
|
ScrapeConfig
|
VMScrapeConfig
With this table in mind, moving away from Prometheus to Victoria Metrics has the least overhead
. All your current scrape targets (e.g., 14
ServiceMonitor &
PodMonitor) will continue to work when replacing a Prometheus server with a
VMAgent instance; the Victoria Metrics Operator takes care of the CRD conversion and the
VMAgent will scrape those targets.
Your Grafana dashboard will also continue to work as expected just by a change of datasource address from Prometheus URL to that of Victoria Metrics.
## Scrape Targets with Victoria Metrics
[¶](#scrape-targets-with-victoria-metrics)
At this point, we should visit our last objective for this blog post. We aim to scrape targets with Victoria Metrics components and ship them to a storage to later be queried.
As such, we aim to provide the following variations:
- Shipping metrics from
kube-state-metricsand
node-exporterto Victoria Metrics, as you saw earlier in
[the diagram above](#deploy-victoria-metrics).
- Shipping metrics from the same sources to Grafana Cloud.
- Shipping metrics from another Prometheus instance elsewhere or a
VMAgentto the Victoria Metrics standalone deployment.
### Deploy Victoria Metrics to Kubernetes Cluster
[¶](#deploy-victoria-metrics-to-kubernetes-cluster)
For the deployment of the Victoria Metrics storage, you have the option to deploy them one by one or all in a single instance. The former gives you more scalability, whereas the latter gives you more simplicity
. 15
We will deploy the
VMCluster in this section and leave
VMSingle for
[the last section](#monitor-standalone-hosts-with-victoria-metrics).
We first deploy the
storage component , the query component (
select) and the ingestion component (
insert)
. These components are the core of Victoria Metrics. 16 apiVersion: operator.victoriametrics.com/v1beta1
kind: VMCluster
metadata:
name: vmserver
spec:
retentionPeriod: 1d
vmstorage:
replicaCount: 1
storage:
volumeClaimTemplate:
spec:
resources:
requests:
storage: "1Gi"
vmselect:
replicaCount: 1
storage:
volumeClaimTemplate:
spec:
resources:
requests:
storage: "1Gi"
vminsert:
replicaCount: 1
We then deploy a
VMAgent, scraping metrics from any of the discovered targets and ship them to the cluster created with
VMCluster.
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAgent
metadata:
name: vmscrape
spec:
extraArgs:
promscrape.maxScrapeSize: 32MiB
selectAllByDefault: true
remoteWrite:
- url: http://vminsert-vmserver.monitoring:8480/insert/0/prometheus
Notice that in the
VMAgent, the URL we are passing to the remote-write is coming from our
VMCluster instance, one that can be verified with the
kubectl get service command, as well as looking through the documentation for Victoria Metrics endpoints
. 17 remoteWrite:
- url: http://vminsert-vmserver.monitoring:8480/insert/0/prometheus
Lastly, we need to be able to access the UI from our browser. That's where the rest of the components come as you see below
. 18 apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAuth
metadata:
name: auth-proxy
spec:
selectAllByDefault: true
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMUser
metadata:
name: vmadmin
spec:
generatePassword: true
targetRefs:
# vmui + vmselect
- crd:
kind: VMCluster/vmselect
name: vmserver
namespace: monitoring
target_path_suffix: "/select/0"
paths:
- "/vmui"
- "/vmui/.*"
- "/prometheus/api/v1/query"
- "/prometheus/api/v1/query_range"
- "/prometheus/api/v1/series"
- "/prometheus/api/v1/status/.*"
- "/prometheus/api/v1/label/"
- "/prometheus/api/v1/label/[^/]+/values"
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
name: victoria-metrics
spec:
hostnames:
- victoria-metrics.developer-friendly.blog
parentRefs:
- group: gateway.networking.k8s.io
kind: Gateway
name: developer-friendly-blog
namespace: cert-manager
sectionName: https
rules:
- backendRefs:
- kind: Service
name: vmauth-auth-proxy
port: 8427
filters:
- responseHeaderModifier:
set:
- name: Strict-Transport-Security
value: max-age=31536000; includeSubDomains; preload
type: ResponseHeaderModifier
matches:
- path:
type: PathPrefix
value: /
resources:
- vmcluster.yml
- vmagent.yml
- vmuser.yml
- vmauth.yml
- httproute.yml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
name: victoria-metrics-cluster
namespace: flux-system
spec:
force: false
interval: 5m
path: ./victoria-metrics-cluster
prune: true
sourceRef:
kind: GitRepository
name: flux-system
targetNamespace: monitoring
wait: true
Finally, to deploy this stack:
Opening the target address at
/vmui endpoint, we will see the Victoria Metrics query dashboard as you see below.
![Click to zoom in Victoria Metrics UI](/static/img/2024/0016/vm-cluster-ui.webp)
![Click to zoom in Victoria Metrics UI](/static/img/2024/0016/vm-cluster-ui.webp)
This concludes
[our first objective](#scrape-targets-with-victoria-metrics), to scrape and ship metrics from the same cluster.
### Remote Write Victoria Metrics to Grafana Cloud
[¶](#remote-write-victoria-metrics-to-grafana-cloud)
Grafana Cloud makes it very easy for you to ship your metrics with the least overhead. You will be responsible for only scraping your targets. The rest is the taken care of by their infrastructure, including storage, query, scaling, availabilty, etc.
Let's create a single
VMAgent to scrape all the metrics and ship them to the Grafana Cloud.
Grafana Cloud Account
If don't already have one, they provide a generous free tier for you to try out their services
. 19
For the Prometheus server, you will have a remote write URL similar to what you see below.
remote_write:
- url: https://prometheus-prod-24-prod-eu-west-2.grafana.net/api/prom/push
basic_auth:
username: 123456
password: <Your Grafana.com API Token>
Let's use this configuration to create such a
VMAgent instance.
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAgent
metadata:
name: vmscrape
spec:
extraArgs:
promscrape.maxScrapeSize: 32MiB
selectAllByDefault: true
remoteWrite:
- url: https://prometheus-prod-24-prod-eu-west-2.grafana.net/api/prom/push
basicAuth:
password:
key: password
name: grafana-cloud-secret
optional: false
username:
key: username
name: grafana-cloud-secret
optional: false
This agent will also, just like the last one, scrape all the
VMServiceScrape &
VMPodScrape resources.
The difference is, however, that this agent will ship the metrics to the remote write URL of the Grafana Cloud and we won't have to manage any storage or
[Grafana](/category/grafana/) instance of our own anymore.
### Monitor Standalone Hosts with Victoria Metrics
[¶](#monitor-standalone-hosts-with-victoria-metrics)
For addressing
[the last objective](#scrape-targets-with-victoria-metrics), we aim to make things a bit more different in that we will scrape the target host from a single standalone machine (outside [Kubernetes](/category/kubernetes/)) and ship those to the in-cluster Victoria Metrics we will create with the
VMSingle CRD resource.
Since this is assumed to be a standalone machine, we will use our beloved tool
[Ansible](/category/ansible/)
. This helps reproducibility as well as documenting the steps for future reference.
---
vmutils_url: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.101.0/vmutils-linux-arm64-v1.101.0.tar.gz
---
vmutils_url: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.101.0/vmutils-linux-amd64-v1.101.0.tar.gz
[Unit]
Description=Victoria Metrics - VMAgent
Documentation=https://github.com/VictoriaMetrics/VictoriaMetrics
[Service]
ExecStart=/usr/local/bin/vmagent-prod \
-promscrape.config=/etc/victoria-metrics/vmagent.yml \
-remoteWrite.url={{ remote_write_url }} \
-influxListenAddr='' \
-httpListenAddr='' \
-remoteWrite.tmpDataPath=/var/lib/victoria-metrics/remote-write-data
Restart=always
RestartSec=5
[Install]
WantedBy=multi-user.target
global:
scrape_interval: 30s
scrape_configs:
- job_name: node-exporter
static_configs:
- targets:
- localhost:9100
labels:
instance: {{ ansible_hostname }}
- name: Include host specific variables
ansible.builtin.include_vars:
file: vars-{{ ansible_architecture }}.yml
- name: Download vmutils
ansible.builtin.get_url:
url: "{{ vmutils_url }}"
dest: "/tmp/{{ vmutils_url | basename }}"
mode: "0444"
owner: root
group: root
register: vmutils_download
- name: Extract binaries
ansible.builtin.unarchive:
src: "{{ vmutils_download.dest }}"
dest: /usr/local/bin/
remote_src: true
mode: "0755"
owner: root
group: root
extra_opts:
- vmagent-prod
- vmalert-prod
- vmalert-tool-prod
- vmauth-prod
- vmbackup-prod
- vmrestore-prod
- vmctl-prod
- name: Ensure victoria-metrics relevant dir exists
ansible.builtin.file:
path: "{{ item }}"
state: directory
owner: root
group: root
mode: "0755"
loop:
- /var/lib/victoria-metrics
- /etc/victoria-metrics
- name: Copy service file
ansible.builtin.template:
src: vmagent.service.j2
dest: /etc/systemd/system/vmagent.service
owner: root
group: root
mode: "0644"
notify: Restart vmagent service
- name: Copy config file
ansible.builtin.template:
src: vmagent.yml.j2
dest: /etc/victoria-metrics/vmagent.yml
owner: root
group: root
mode: "0444"
notify: Restart vmagent service
- name: Start vmagent service
ansible.builtin.systemd:
name: vmagent
state: started
enabled: true
daemon_reload: true
---
- name: Restart vmagent service
ansible.builtin.systemd:
name: vmagent
state: restarted
daemon_reload: true
Having this Ansible role, we can now use it to monitor our target host.
But, before doing that, let's deploy a
VMSingle instance to our Kubernetes cluster as promised earlier.
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMSingle
metadata:
name: standalone
spec:
retentionPeriod: "1"
removePvcAfterDelete: true
extraArgs:
dedup.minScrapeInterval: 10s
storage:
accessModes:
- ReadWriteOnce
resources:
requests:
storage: 1Gi
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
name: victoria-metrics
spec:
hostnames:
- vmsingle.developer-friendly.blog
parentRefs:
- group: gateway.networking.k8s.io
kind: Gateway
name: developer-friendly-blog
namespace: cert-manager
sectionName: https
rules:
- backendRefs:
- kind: Service
name: vmsingle-standalone
port: 8429
filters:
- responseHeaderModifier:
set:
- name: Strict-Transport-Security
value: max-age=31536000; includeSubDomains; preload
type: ResponseHeaderModifier
matches:
- path:
type: PathPrefix
value: /
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
name: victoria-metrics-standalone
namespace: flux-system
spec:
force: false
interval: 5m
path: ./victoria-metrics-standalone
prune: true
sourceRef:
kind: GitRepository
name: flux-system
targetNamespace: monitoring
wait: true
Finally, to deploy this stack:
And now we are ready to run the following Ansible playbook.
- name: Monitor targets with Victoria Metrics
hosts: monitoring
roles:
- victoria-metrics
vars:
remote_write_url: https://vminsert.developer-friendly.blog/api/v1/write
All of these approaches are just a few of the many ways you can monitor your infrastructure with
[Victoria Metrics](/category/victoriametrics/). We covered some of the most typical ways you would normally monitor a production setup. This should give you a good idea on how to get started with Victoria Metrics.
## Conclusion
[¶](#conclusion)
Victoria Metrics is a powerful, high-performance and resource efficient monitoring solution that can easily replace Prometheus in your monitoring stack. It offers a wide range of features and capabilities that make it an ideal choice for handling large-scale data and optimizing monitoring performance. Although we didn't cover it in this blog post, VictoriaMetrics come with a product for logging as well which is just as powerful as their metrics product
. 20
By following the steps outlined in this guide, you can migrate or integrate your current monitoring setup with Victoria Metrics effortlessly and take advantage of its advanced features and benefits.
We have covered some of the most common patterns for monitoring the target hosts and scraping the metrics using Victoria Metrics. You can use these examples to build up your own monitoring solution in a way that fits your environment.
If you are looking for a high-performance, scalable, and cost-effective monitoring solution, Victoria Metrics is definitely worth considering.
Give it a try today and see how it can transform your monitoring experience!
Happy hacking and until next time
,
*ciao*. **If you enjoyed this blog post, consider sharing it with these buttons . Please leave a comment for us at the end, we read & love 'em all.. ** [Share on ](https://news.ycombinator.com/submitlink?u=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/&t=Unlocking%20the%20Power%20of%20VictoriaMetrics%3A%20A%20Prometheus%20Alternative%0A) [Share on ](https://www.linkedin.com/sharing/share-offsite/?url=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/) [Share on ](https://www.reddit.com/submit?url=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/&title=Unlocking%20the%20Power%20of%20VictoriaMetrics%3A%20A%20Prometheus%20Alternative%0A) [Share on ](https://twitter.com/intent/tweet?text=%40devfriendly_%0AUnlocking%20the%20Power%20of%20VictoriaMetrics%3A%20A%20Prometheus%20Alternative%0A&url=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/)
-
-
-
[https://medium.com/@seifeddinerajhi/victoriametrics-a-comprehensive-guide-comparing-it-to-prometheus-and-implementing-kubernetes-03eb8feb0cc2](https://medium.com/@seifeddinerajhi/victoriametrics-a-comprehensive-guide-comparing-it-to-prometheus-and-implementing-kubernetes-03eb8feb0cc2) [↩](#fnref:seifeddinerajhi-medium)
-
[https://docs.victoriametrics.com/single-server-victoriametrics/#prominent-features](https://docs.victoriametrics.com/single-server-victoriametrics/#prominent-features) [↩](#fnref:vm-prominent-features)
-
[https://victoriametrics.com/blog/comparing-agents-for-scraping/](https://victoriametrics.com/blog/comparing-agents-for-scraping/) [↩](#fnref:vm-blog-comparing-agents)
-
[https://zetablogs.medium.com/prometheus-vs-victoria-metrics-load-testing-3fa0cc782912](https://zetablogs.medium.com/prometheus-vs-victoria-metrics-load-testing-3fa0cc782912) [↩](#fnref:vm-vs-prom-perf)
-
[https://prometheus.io/docs/prometheus/latest/storage/#operational-aspects](https://prometheus.io/docs/prometheus/latest/storage/#operational-aspects) [↩](#fnref:prometheus-long-term-storage)
-
-
[https://artifacthub.io/packages/helm/victoriametrics/victoria-metrics-operator/0.32.2](https://artifacthub.io/packages/helm/victoriametrics/victoria-metrics-operator/0.32.2) [↩](#fnref:vm-operator)
-
-
-
[https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack/60.1.0](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack/60.1.0) [↩](#fnref:k8s-prom-stack)
-
[https://docs.victoriametrics.com/operator/migration/#objects-conversion](https://docs.victoriametrics.com/operator/migration/#objects-conversion) [↩](#fnref:vm-object-conversion)
-
-
[https://docs.victoriametrics.com/cluster-victoriametrics/#architecture-overview](https://docs.victoriametrics.com/cluster-victoriametrics/#architecture-overview) [↩](#fnref:vm-cluster-arch)
-
[https://docs.victoriametrics.com/operator/quick-start/#vmcluster-vmselect-vminsert-vmstorage](https://docs.victoriametrics.com/operator/quick-start/#vmcluster-vmselect-vminsert-vmstorage) [↩](#fnref:vm-cluster)
-
[https://docs.victoriametrics.com/cluster-victoriametrics/#url-format](https://docs.victoriametrics.com/cluster-victoriametrics/#url-format) [↩](#fnref:vm-url-formats)
-
[https://docs.victoriametrics.com/operator/quick-start/#vmauth](https://docs.victoriametrics.com/operator/quick-start/#vmauth) [↩](#fnref:vm-operator-vmauth)
-
-