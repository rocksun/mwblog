<!--
title: Kubernetes集群常见操作完整指南
cover: https://teckbootcamps.com/wp-content/uploads/2024/02/dd-3.png
-->

涵盖了 Kubernetes 集群管理的各个方面，可以当作一个速查手册。

> 译自 [Comprehensive Guide to Common Operations in Kubernetes Clusters](https://teckbootcamps.com/comprehensive-guide-to-common-operations-in-kubernetes-clusters/#1-uninstall-steps)，作者 Mohamed BEN HASSINE。


## 1. 删除步骤

```bash
# uninstall:
kubeadm reset

# Cleanup:
kubeadm reset -f
modprobe -r ipip
lsmod
rm -rf ~/.kube/
rm -rf /etc/kubernetes/
rm -rf /etc/systemd/system/kubelet.service.d
rm -rf /etc/systemd/system/kubelet.service
rm -rf /usr/bin/kube*
rm -rf /etc/cni
rm -rf /opt/cni
rm -rf /var/lib/etcd
rm -rf /var/etcd
```

## 2. 进程列表

```bash
[root@teckbootcamps ~] ps -ef|grep kube
root      8395 26979  0 18:03 pts/1    00:00:00 grep --color=auto kube
root     20501     1  2 13:42 ?        00:06:50 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true --network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin --cluster-dns=10.96.0.10 --cluster-domain=cluster.local --authorization-mode=Webhook --client-ca-file=/etc/kubernetes/pki/ca.crt --cadvisor-port=0 --teckbootcamps-driver=systemd --rotate-certificates=true --cert-dir=/var/lib/kubelet/pki

root     20744 20728  0 13:42 ?        00:02:26 etcd --advertise-client-urls=https://127.0.0.1:2379 --cert-file=/etc/kubernetes/pki/etcd/server.crt --client-cert-auth=true --data-dir=/var/lib/etcd --initial-advertise-peer-urls=https://127.0.0.1:2380 --initial-cluster=teckbootcamps=https://127.0.0.1:2380 --key-file=/etc/kubernetes/pki/etcd/server.key --listen-client-urls=https://127.0.0.1:2379 --listen-peer-urls=https://127.0.0.1:2380 --name=teckbootcamps --peer-cert-file=/etc/kubernetes/pki/etcd/peer.crt --peer-client-cert-auth=true --peer-key-file=/etc/kubernetes/pki/etcd/peer.key --peer-trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt --snapshot-count=10000 --trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt

root     20793 20745  1 13:42 ?        00:03:56 kube-controller-manager --address=127.0.0.1 --allocate-node-cidrs=true --cluster-cidr=192.168.0.0/16 --cluster-signing-cert-file=/etc/kubernetes/pki/ca.crt --cluster-signing-key-file=/etc/kubernetes/pki/ca.key --controllers=*,bootstrapsigner,tokencleaner --kubeconfig=/etc/kubernetes/controller-manager.conf --leader-elect=true --node-cidr-mask-size=24 --root-ca-file=/etc/kubernetes/pki/ca.crt --service-account-private-key-file=/etc/kubernetes/pki/sa.key --use-service-account-credentials=true
root     20806 20746  1 13:42 ?        00:04:47 kube-apiserver --authorization-mode=Node,RBAC --advertise-address=172.17.211.142 --allow-privileged=true --client-ca-file=/etc/kubernetes/pki/ca.crt --disable-admission-plugins=PersistentVolumeLabel --enable-admission-plugins=NodeRestriction --enable-bootstrap-token-auth=true --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key --etcd-servers=https://127.0.0.1:2379 --insecure-port=0 --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key --requestheader-allowed-names=front-proxy-client --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt --requestheader-extra-headers-prefix=X-Remote-Extra- --requestheader-group-headers=X-Remote-Group --requestheader-username-headers=X-Remote-User --secure-port=6443 --service-account-key-file=/etc/kubernetes/pki/sa.pub --service-cluster-ip-range=10.96.0.0/12 --tls-cert-file=/etc/kubernetes/pki/apiserver.crt --tls-private-key-file=/etc/kubernetes/pki/apiserver.key

root     20814 20760  0 13:42 ?        00:01:18 kube-scheduler --address=127.0.0.1 --kubeconfig=/etc/kubernetes/scheduler.conf --leader-elect=true

root     21095 21071  0 13:43 ?        00:00:22 /usr/local/bin/kube-proxy --config=/var/lib/kube-proxy/config.conf

root     22065 22047  0 13:43 ?        00:00:03 /usr/bin/kube-controllers
65534    22166 22137  0 13:43 ?        00:00:12 /heapster --source=kubernetes:https://kubernetes.default --sink=influxdb:http://monitoring-influxdb.kube-system.svc:8086
```
## 3. 重启方法

```bash
[root@teckbootcamps ~]# swapoff -a && systemctl stop kubelet
```

## 4. 常用命令

### 1. 查看 cluster-info

```bash
[root@teckbootcamps /]kubectl cluster-info
Kubernetes master is running at https://172.17.211.142:6443
Heapster is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/heapster/proxy
KubeDNS is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
monitoring-grafana is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/monitoring-grafana/proxy
monitoring-influxdb is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/monitoring-influxdb/proxy
 
To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

[root@teckbootcamps /]kubectl cluster-info
Kubernetes master is running at https://172.17.211.142:6443
Heapster is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/heapster/proxy
KubeDNS is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
monitoring-grafana is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/monitoring-grafana/proxy
monitoring-influxdb is running at https://172.17.211.142:6443/api/v1/namespaces/kube-system/services/monitoring-influxdb/proxy
To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

### 2. 通过 cluster-info 查看 dump 信息

```bash
[root@teckbootcamps ~]kubectl cluster-info dump
{
"kind": "NodeList",
"apiVersion": "v1",
"metadata": {
"selfLink": "/api/v1/nodes",
"resourceVersion": "35732"
},
```

### 3. 查看 deployment

```bash
[root@teckbootcamps ~]kubectl -n kube-system get deployments
NAME                          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
calico-kube-controllers       1         1         1            1           98d
coredns                       2         2         2            2           98d
heapster                      1         1         1            1           98d
heapster-teckbootcamps              1         0         0            0           1h
heapster-teckbootcamps2             1         0         0            0           1h
kubernetes-dashboard          1         1         1            1           98d
monitoring-grafana            1         1         1            1           98d
monitoring-grafana-teckbootcamps    1         0         0            0           1h
monitoring-influxdb           1         1         1            1           98d
monitoring-influxdb-teckbootcamps   1         0         0            0           2h
```


### 4. 删除 deployment

```bash
[root@teckbootcamps ~]kubectl -n kube-system delete deployment heapster-teckbootcamps

deployment.extensions "heapster-teckbootcamps" deleted
```

### 5. 查看 services

```bash
[root@teckbootcamps shell]kubectl -n kube-system get svc -o wide
NAME                   TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                  AGE   SELECTOR
heapster               ClusterIP   10.106.70.78     <none>        80/TCP                   23h   k8s-app=heapster
kube-dns               ClusterIP   10.96.0.10       <none>        53/UDP,53/TCP,9153/TCP   23h   k8s-app=kube-dns
kubelet                ClusterIP   None             <none>        10250/TCP                23h   <none>
kubernetes-dashboard   NodePort    10.110.202.105   <none>        443:32000/TCP            23h   k8s-app=kubernetes-dashboard
monitoring-grafana     NodePort    10.98.68.122     <none>        80:32001/TCP             23h   k8s-app=grafana
monitoring-influxdb    ClusterIP   10.104.109.169   <none>        8086/TCP                 23h   k8s-app=influxdb
```

### 6. 查看 nodes

```bash
[root@teckbootcamps ~]kubectl get nodes
NAME             STATUS   ROLES    AGE   VERSION
teckbootcamps    Ready    <none>   90d   v1.26.0
teckbootcamps2   Ready    <none>   90d   v1.26.0
teckbootcamps3   Ready    master   98d   v1.26.0
```

### 7. 查看 Service Account

```bash
[root@teckbootcamps3 ~]kubectl get sa --all-namespaces
NAMESPACE     NAME                                 SECRETS   AGE
default       default                              1         98d
kube-public   default                              1         98d
kube-system   attachdetach-controller              1         98d
... (output truncated for brevity)
kube-system   service-controller                   1         98d
kube-system   statefulset-controller               1         98d
kube-system   token-cleaner                        1         98d
kube-system   ttl-controller                       1         98d
```

### 8. 查看集群 DNS Service 信息

```bash
[root@teckbootcamps /]kubectl get service -l k8s-app=kube-dns --namespace=kube-system
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)         AGE
kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP   12d
```

### 9. 查看 cluster DNS 副本控制器

```bash
[root@teckbootcamps /]# kubectl get pod --selector k8s-app=kube-dns --namespace=kube-system
NAME                       READY     STATUS    RESTARTS   AGE
coredns-78fcdf6894-m7rgl   1/1       Running   0          3d
coredns-78fcdf6894-tpkql   1/1       Running   0          3d
```

### 10. 查看 cluster DNS 服务

```bash
[root@teckbootcamps /]kubectl get service -l k8s-app=kube-dns --namespace=kube-system
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)         AGE
kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP   12d
```

### 11. 查看组件

```bash
[root@teckbootcamps /] kubectl -s https://172.17.211.142:6443 get componentstatus
NAME                 STATUS    MESSAGE              ERROR
controller-manager   Healthy   ok
scheduler            Healthy   ok
etcd-0               Healthy   {"health": "true"}
```

### 12. 查看 endpoint

```bash
[root@teckbootcamps shell] kubectl get endpoints
NAME         ENDPOINTS             AGE
kubernetes   172.17.211.142:6443   23h
```

### 13. 查看 node 列表

```bash
[root@teckbootcamps /]kubectl -s https://172.17.211.142:6443 get nodes

NAME       STATUS    ROLES     AGE       VERSION
teckbootcamps    Ready     <none>    3d        v1.11.0
teckbootcamps2   Ready     <none>    3d        v1.11.0
teckbootcamps3   Ready     master    12d       v1.11.0
```

### 14. 查看 node 详情

```bash
[root@teckbootcamps shell]# kubectl get node
NAME       STATUS   ROLES    AGE   VERSION
teckbootcamps    Ready    <none>   17m   v1.14.4
teckbootcamps2   Ready    <none>   13h   v1.14.4
teckbootcamps3   Ready    master   23h   v1.14.4

[root@teckbootcamps shell] kubectl describe node teckbootcamps

Name:               teckbootcamps
Roles:              <none>
Labels:             beta.kubernetes.io/arch=amd64
beta.kubernetes.io/os=linux
kubernetes.io/arch=amd64
kubernetes.io/hostname=teckbootcamps
kubernetes.io/os=linux
Annotations:        kubeadm.alpha.kubernetes.io/cri-socket: /var/run/dockershim.sock
node.alpha.kubernetes.io/ttl: 0
projectcalico.org/IPv4Address: 172.17.211.143/20
projectcalico.org/IPv4IPIPTunnelAddr: 100.67.134.64
volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Sun, 28 Jul 2019 10:51:34 +0800
Taints:             <none>
Unschedulable:      false
Conditions:
Type                 Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
----                 ------  -----------------                 ------------------                ------                       -------
NetworkUnavailable   False   Sun, 28 Jul 2019 10:51:58 +0800   Sun, 28 Jul 2019 10:51:58 +0800   CalicoIsUp                   Calico is running on this node
MemoryPressure       False   Sun, 28 Jul 2019 11:09:15 +0800   Sun, 28 Jul 2019 10:51:33 +0800   KubeletHasSufficientMemory   kubelet has sufficient memory available
DiskPressure         False   Sun, 28 Jul 2019 11:09:15 +0800   Sun, 28 Jul 2019 10:51:33 +0800   KubeletHasNoDiskPressure     kubelet has no disk pressure
PIDPressure          False   Sun, 28 Jul 2019 11:09:15 +0800   Sun, 28 Jul 2019 10:51:33 +0800   KubeletHasSufficientPID      kubelet has sufficient PID available
Ready                True    Sun, 28 Jul 2019 11:09:15 +0800   Sun, 28 Jul 2019 10:52:04 +0800   KubeletReady                 kubelet is posting ready status
Addresses:
InternalIP:  172.17.211.143
Hostname:    teckbootcamps
Capacity:
cpu:                2
ephemeral-storage:  41152832Ki
hugepages-1Gi:      0
hugepages-2Mi:      0
memory:             3882308Ki
pods:               110
Allocatable:
cpu:                2
ephemeral-storage:  37926449909
hugepages-1Gi:      0
hugepages-2Mi:      0
memory:             3779908Ki
pods:               110
System Info:
Machine ID:                 7d26c16f128042a684ea474c9e2c240f
System UUID:                09D50368-65D8-41BD-A923-FBCF9B8851AB
Boot ID:                    acc62473-6237-49e9-8bf8-222771e267e1
Kernel Version:             3.10.0-327.28.2.el7.x86_64
OS Image:                   CentOS Linux 7 (Core)
Operating System:           linux
Architecture:               amd64
Container Runtime Version:  docker://18.6.1
Kubelet Version:            v1.14.4
Kube-Proxy Version:         v1.14.4
PodCIDR:                     100.64.2.0/24
Non-terminated Pods:         (4 in total)
Namespace                  Name                            CPU Requests  CPU Limits  Memory Requests  Memory Limits  AGE
---------                  ----                            ------------  ----------  ---------------  -------------  ---
kube-system                calico-node-stc89               250m (12%)    0 (0%)      0 (0%)           0 (0%)         18m
kube-system                kube-proxy-qzplb                0 (0%)        0 (0%)      0 (0%)           0 (0%)         18m
kube-system                kube-sealyun-lvscare-teckbootcamps    0 (0%)        0 (0%)      0 (0%)           0 (0%)         18m
monitoring                 node-exporter-tz6ms             112m (5%)     270m (13%)  200Mi (5%)       240Mi (6%)     18m
Allocated resources:
(Total limits may be over 100 percent, i.e., overcommitted.)
Resource           Requests    Limits
--------           --------    ------
cpu                362m (18%)  270m (13%)
memory             200Mi (5%)  240Mi (6%)
ephemeral-storage  0 (0%)      0 (0%)
Events:
Type     Reason                            Age                 From                 Message
----     ------                            ----                ----                 -------
Normal   Starting                          18m                 kubelet, teckbootcamps     Starting kubelet.
Normal   NodeHasSufficientMemory           18m                 kubelet, teckbootcamps     Node teckbootcamps status is now: NodeHasSufficientMemory
Normal   NodeHasNoDiskPressure             18m                 kubelet, teckbootcamps     Node teckbootcamps status is now: NodeHasNoDiskPressure
Normal   NodeHasSufficientPID              18m                 kubelet, teckbootcamps     Node teckbootcamps status is now: NodeHasSufficientPID
Normal   Starting                          18m                 kube-proxy, teckbootcamps  Starting kube-proxy.
Normal   NodeReady                         17m                 kubelet, teckbootcamps     Node teckbootcamps status is now: NodeReady
Warning  ImageGCFailed                     13m                 kubelet, teckbootcamps     wanted to free 1747577241 bytes, but freed 1771511194 bytes space with errors in image deletion: [rpc error: code = Unknown desc = Error response from daemon: conflict: unable to delete abf312888d13 (must be forced) - image is being used by stopped container e5285e77b550, rpc error: code = Unknown desc = Error response from daemon: conflict: unable to remove repository reference "tutum/influxdb:0.13" (must force) - container c986b59b91ed is using its referenced image 39fa42a093e0, rpc error: code = Unknown desc = Error response from daemon: conflict: unable to remove repository reference "teckbootcamps-tomcat8-2:latest" (must force) - container ddc7e49946f1 is using its referenced image c375edce8dfd, rpc error: code = Unknown desc = Error response from daemon: conflict: unable to remove repository reference "teckbootcamps-tomcat8:latest" (must force) - container f627e4cb0dbc is using its referenced image 7e69e1b21246]
Warning  FailedNodeAllocatableEnforcement  27s (x19 over 18m)  kubelet, teckbootcamps     Failed to update Node Allocatable Limits ["kubepods"]: failed to set supported teckbootcamps subsystems for teckbootcamps [kubepods]: Failed to find subsystem mount for required subsystem: pids
```

### 15. 查看系统日志

```bash
[root@teckbootcamps /] journalctl -xeu kubelet
-- Logs begin at Mon 2023-02-27 10:00:20 UTC, end at Wed 2023-02-28 10:16:01 UTC. --
Feb 28 10:16:01 teckbootcamps kubelet[1963]: I0228 10:16:01.517740    1963 kubelet.go:2107] syncLoop (PLEG): "kube-proxy-teckbootcamps/172.17.211.142:6443" did not receive an update for 3m45.215672686s, fallback to rate-limited sync
Feb 28 10:16:01 teckbootcamps kubelet[1963]: I0228 10:16:01.517792    1963 kubelet.go:2107] syncLoop (PLEG): "weave-net-c69dt_kube-system(87511ea3-98d5-4ff6-89a2-74fd50f6d7f2)": waiting for 3m20.702903443s to sync
Feb 28 10:16:01 teckbootcamps kubelet[1963]: I0228 10:16:01.517814    1963 kubelet.go:2107] syncLoop (PLEG): "coredns-78fcdf6894-m7rgl_kube-system(73649fbc-791a-4b99-a575-53a6a77d5a43)": waiting for 3m5.682036808s to sync
```



### 16. 查看 kubelet 配置信息

```bash
[root@teckbootcamps shell] kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://172.17.211.142:6443
  name: kubernetes
contexts:
- context:
    cluster: kubernetes
    user: kubernetes-admin
  name: kubernetes-admin@kubernetes
current-context: kubernetes-admin@kubernetes
kind: Config
preferences: {}
users:
- name: kubernetes-admin
  user:
    client-certificate-data: REDACTED
    client-key-data: REDACTED
```

### 17. 检查 Kubernetes 版本

```bash
[root@teckbootcamps kubernets]kubelet --version

Kubernetes v1.28
```

### 18. 查看配置

```bash
[root@teckbootcamps ~]kubeadm config view

apiServer:
  extraArgs:
    authorization-mode: Node,RBAC
    timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta2
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
dns:
  type: CoreDNS
etcd:
  local:
    dataDir: /var/lib/etcd
  imageRepository: k8s.gcr.io
kind: ClusterConfiguration
kubernetesVersion: v1.14.4
networking:
  dnsDomain: cluster.local
  podSubnet: 100.64.0.0/10
  serviceSubnet: 10.96.0.0/12
```

### 19. 列出需要的镜像

```bash
[root@teckbootcamps ~] kubeadm config images list
W0728 10:09:45.567500   28248 version.go:98] could not fetch a Kubernetes version from the internet: unable to get URL "https://dl.k8s.io/release/stable-1.txt": Get https://dl.k8s.io/release/stable-1.txt: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
W0728 10:09:45.567584   28248 version.go:99] falling back to the local client version: v1.15.0
k8s.gcr.io/kube-apiserver:v1.15.0
k8s.gcr.io/kube-controller-manager:v1.15.0
k8s.gcr.io/kube-scheduler:v1.15.0
k8s.gcr.io/kube-proxy:v1.15.0
k8s.gcr.io/pause:3.1
k8s.gcr.io/etcd:3.3.10
k8s.gcr.io/coredns:1.3.1
```

### 20. 查看默认初始化参数配置

```bash
[root@teckbootcamps ~]kubeadm config print init-defaults

apiVersion: kubeadm.k8s.io/v1beta2
bootstrapTokens:
- groups:
  - system:bootstrappers:kubeadm:default-node-token
  token: abcdef.0123456789abcdef
  ttl: 24h0m0s
  usages:
  - signing
  - authentication
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 1.2.3.4
  bindPort: 6443
nodeRegistration:
  criSocket: /var/run/dockershim.sock
  name: teckbootcamps
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
---
apiServer:
  timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta2
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
dns:
  type: CoreDNS
etcd:
  local:
    dataDir: /var/lib/etcd
  imageRepository: k8s.gcr.io
kind: ClusterConfiguration
kubernetesVersion: v1.14.0
networking:
  dnsDomain: cluster.local
  serviceSubnet: 10.96.0.0/12
```

### 21. 查看 pod 日志

1. 查看特定 pod 的日志

```bash
kubectl logs <pod_name>
kubectl logs -f <pod_name>
#View similar to tail -f (tail -f to view the log file in real time tail -f log file log)
```

2. 查看特定 Pod 特定容器的日志

```bash
kubectl logs <pod_name> -c <container_name>
PS: View Docker container logs
docker logs <container_id>
```


###  22. 查看 pod 的 YAML 文件

```bash
kubectl get pod <pod-name> -n <ns-name> -o yaml
```

例如：

```bash
[root@teckbootcamps shell]kubectl get pod -n kube-system kube-apiserver-teckbootcamps -o yaml

apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubernetes.io/config.hash: 4c09c523e34dd307dbfa1702d7e5f326
    kubernetes.io/config.mirror: 4c09c523e34dd307dbfa1702d7e5f326
    kubernetes.io/config.seen: "2019-07-27T11:32:59.183084282+08:00"
    kubernetes.io/config.source: file
  creationTimestamp: "2019-07-27T03:34:32Z"
  labels:
    component: kube-apiserver
    tier: control-plane
  name: kube-apiserver-teckbootcamps
  namespace: kube-system
  resourceVersion: "41809"
  selfLink: /api/v1/namespaces/kube-system/pods/kube-apiserver-teckbootcamps
  uid: 72b76059-b01f-11e9-9ad8-00163e06971e
spec:
  containers:
  - command:
    - kube-apiserver
    - --advertise-address=172.17.211.142
    - --allow-privileged=true
    ...
```

### 23. 登陆到容器

登录容器时，需要关注容器支持的 shell。

```bash
kubectl exec -it <pod-name> -n <ns-name> bash
kubectl exec -it <pod-name> -n <ns-name> sh
```

```bash
[root@teckbootcamps shell] kubectl exec -it monitoring-grafana-95cbdd789-fzl49 -n kube-system /bin/sh /ls

bin         dashboards  dev         etc         home        proc        root        run.sh      sys         tmp         usr         var
```

登录时报错：

```bash
kubectl  OCI runtime exec failed: exec failed: container_linux.go:345: starting container process ca
```

, 表明shell类型不正确。

### 24. 根据 YAML 创建资源

```bash
# Create resources based on yaml. Apply can be executed repeatedly, but create cannot.
kubectl create -f pod.yaml
kubectl apply -f pod.yaml
```

### 25. 根据 YAML 删除 Pod

```bash
#  Delete a pod based on the name defined in pod.yaml
kubectl delete -f pod.yaml
```

### 26. 根据标签删除pod和服务


```bash
# Delete all pods and services containing a certain label
kubectl delete pod,svc -l name=<label-name>
```

### 27. 删除 Pod

```bash
[root@teckbootcamps ~]kubectl get pods

NAME                 READY   STATUS    RESTARTS   AGE
frontend-2szjk       1/1     Running   0          3d1h
frontend-cv5qw       1/1     Running   0          3d1h
frontend-lp4tc       0/1     Evicted   0          3d2h
frontend-sccqj       1/1     Running   0          2d7h
redis-master-6ssmn   1/1     Running   3          3d1h
redis-slave-6vtrs    1/1     Running   1          3d2h
[root@teckbootcamps ~]kubectl delete pod frontend-lp4tc
pod "frontend-lp4tc" deleted

[root@teckbootcamps ~]kubectl get pods

NAME                 READY   STATUS    RESTARTS   AGE
frontend-2szjk       1/1     Running   0          3d1h
frontend-cv5qw       1/1     Running   0          3d1h
frontend-sccqj       1/1     Running   0          2d7h
redis-master-6ssmn   1/1     Running   3          3d1h
redis-slave-6vtrs    1/1     Running   1          3d2h

```

### 28. 检查节点或 Pod 的资源利用情况

```bash
[root@teckbootcamps ~]kubectl top nodes
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
teckbootcamps    129m         6%     1567Mi          42%
teckbootcamps2   233m         11%    1811Mi          49%
teckbootcamps3   510m         25%    2651Mi          71%


[root@teckbootcamps3 ~]kubectl top pod

NAME                 CPU(cores)   MEMORY(bytes)
frontend-2szjk       0m           16Mi
frontend-cv5qw       0m           16Mi
frontend-sccqj       0m           21Mi
redis-master-6ssmn   0m           1Mi
redis-slave-6vtrs    1m           8Mi
```

### 29. 编辑 Pod 的 yaml 文件

```bash
#Edit pod’s yaml file
kubectl get deployment -n <ns-name>

kubectl edit depolyment <pod-name> -n <ns-name> -o yaml
```

以下示例:

```bash
[root@teckbootcamps shell] kubectl get deployment -n kube-system

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
calico-kube-controllers   1/1     1            1           23h
coredns                   2/2     2            2           23h
heapster                  1/1     1            1           23h
kubernetes-dashboard      1/1     1            1           23h
monitoring-grafana        1/1     1            1           23h
monitoring-influxdb       1/1     1            1           23h
[root@teckbootcamps shell]kubectl edit deployment monitoring-grafana -n kube-system -o yaml
```

### 30. 进入 POD

```bash
[root@teckbootcamps data]kubectl exec -it monitoring-grafana-95cbdd789-fzl49 sh -n kube-system /ls
bin         dashboards  dev         etc         home        proc        root        run.sh      sys         tmp         usr         var
```

## 5. 配置文件目录

```bash
[root@teckbootcamps kubernetes]pwd
/etc/kubernetes

[root@teckbootcamps kubernetes] tree -h
.
├── [5.3K]  admin.conf
├── [5.4K]  controller-manager.conf
├── [5.3K]  kubelet.conf
├── [4.0K]  manifests
│   ├── [1.9K]  etcd.yaml
│   ├── [2.5K]  kube-apiserver.yaml
│   ├── [2.2K]  kube-controller-manager.yaml
│   └── [ 990]  kube-scheduler.yaml
├── [4.0K]  pki
│   ├── [1.2K]  apiserver.crt
│   ├── [1.1K]  apiserver-etcd-client.crt
│   ├── [1.6K]  apiserver-etcd-client.key
│   ├── [1.6K]  apiserver.key
│   ├── [1.1K]  apiserver-kubelet-client.crt
│   ├── [1.6K]  apiserver-kubelet-client.key
│   ├── [1.0K]  ca.crt
│   ├── [1.6K]  ca.key
│   ├── [4.0K]  etcd
│   │   ├── [1021]  ca.crt
│   │   ├── [1.6K]  ca.key
│   │   ├── [1.1K]  healthcheck-client.crt
│   │   ├── [1.6K]  healthcheck-client.key
│   │   ├── [1.1K]  peer.crt
│   │   ├── [1.6K]  peer.key
│   │   ├── [1.1K]  server.crt
│   │   └── [1.6K]  server.key
│   ├── [1.0K]  front-proxy-ca.crt
│   ├── [1.6K]  front-proxy-ca.key
│   ├── [1.0K]  front-proxy-client.crt
│   ├── [1.6K]  front-proxy-client.key
│   ├── [1.6K]  sa.key
│   └── [ 451]  sa.pub
└── [5.3K]  scheduler.conf
3 directories, 30 files
```

## 6. 配置 SSL

### 1. 生成 SSL

#### 1.1. CA 颁发证书的过程如下：

```bash
Zees-Air-2:ssl Zee$ openssl genrsa -des3 -passout pass:x -out dashboard.pass.key 2048
Generating RSA private key, 2048 bit long modulus
.....+++
........................+++
e is 65537 (0x10001)
Zees-Air-2:ssl Zee$ ll
total 32
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
Zees-Air-2:ssl Zee$ openssl rsa -passin pass:x -in dashboard.pass.key -out dashboard.key
writing RSA key
Zees-Air-2:ssl Zee$ ll
total 40
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
Zees-Air-2:ssl Zee$ openssl req -new -key dashboard.key -out dashboard.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CN
State or Province Name (full name) [Some-State]:BeiJing
Locality Name (eg, city) []:BeiJing
Organization Name (eg, company) [Internet Widgits Pty Ltd]:teckbootcamps
Organizational Unit Name (eg, section) []:teckbootcamps
Common Name (e.g. server FQDN or YOUR name) []:teckbootcamps.com
Email Address []:
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
Zees-Air-2:ssl Zee$ ll
total 48
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
-rw-r--r--  1 Zee  staff  1009 Nov 22 09:24 dashboard.csr
Zees-Air-2:ssl Zee$ openssl x509 -req -sha256 -days 365 -in dashboard.csr -signkey dashboard.key -out dashboard.crt
Signature ok
subject=/C=CN/ST=BeiJing/L=BeiJing/O=teckbootcamps/OU=teckbootcamps/CN=teckbootcamps.com
Getting Private key

Zees-Air-2:ssl Zee$ ll
total 56
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
-rw-r--r--  1 Zee  staff  1009 Nov 22 09:24 dashboard.csr
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:25 dashboard.crt
Zees-Air-2:ssl Zee$ openssl x509 -in dashboard.crt -out dashboard.pem

Zees-Air-2:ssl Zee$ ll
total 72
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
-rw-r--r--  1 Zee  staff  1009 Nov 22 09:24 dashboard.csr
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:25 dashboard.crt
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:28 dashboard.out
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:28 dashboard.pem
```

#### 服务器证书的生成方式如下:

```bash
Zees-Air-2:ssl Zee$ openssl genrsa -out server.key 2048

Generating RSA private key, 2048 bit long modulus
..................................................................................................................................................................+++
.............................................+++
e is 65537 (0x10001)
Zees-Air-2:ssl Zee$ ll
total 72
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
-rw-r--r--  1 Zee  staff  1009 Nov 22 09:24 dashboard.csr
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:25 dashboard.crt
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:28 dashboard.pem
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:54 server.key
Zees-Air-2:ssl Zee$ openssl req -new -key server.key -subj "/CN=teckbootcamps" -out server.csr
Zees-Air-2:ssl Zee$ ll
total 80
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
-rw-r--r--  1 Zee  staff  1009 Nov 22 09:24 dashboard.csr
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:25 dashboard.crt
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:28 dashboard.pem
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:54 server.key
-rw-r--r--  1 Zee  staff   891 Nov 22 09:55 server.csr
Zees-Air-2:ssl Zee$ openssl x509 -req -in server.csr -CA dashboard.crt -CAkey dashboard.key -CAcreateserial -out server.crt -days 5000
Signature ok
subject=/CN=teckbootcamps
Getting CA Private Key

Zees-Air-2:ssl Zee$ ll
total 96
-rw-r--r--  1 Zee  staff  1751 Nov 22 09:23 dashboard.pass.key
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:23 dashboard.key
-rw-r--r--  1 Zee  staff  1009 Nov 22 09:24 dashboard.csr
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:25 dashboard.crt
-rw-r--r--  1 Zee  staff  1212 Nov 22 09:28 dashboard.pem
-rw-r--r--  1 Zee  staff  1679 Nov 22 09:54 server.key
-rw-r--r--  1 Zee  staff   891 Nov 22 09:55 server.csr
-rw-r--r--  1 Zee  staff  1094 Nov 22 09:56 server.crt
-rw-r--r--  1 Zee  staff    17 Nov 22 09:56 dashboard.srl
```
