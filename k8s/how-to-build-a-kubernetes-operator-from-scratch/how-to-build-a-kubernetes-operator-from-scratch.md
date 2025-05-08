
<!--
title: 如何从零开始构建Kubernetes Operator
cover: https://cdn.thenewstack.io/media/2025/05/bc9c55e1-build-kubernetes-operator.jpg
summary: 手把手教你用 Kind 从零构建 Kubernetes Operator！创建 CRD `PodDiagnoser`，实现控制器，监控 Pod 状态，自动添加崩溃信息注释，执行修复。掌握云原生 Operator 模式，简化 Kubernetes 集群管理，提升可观测性，实现基础设施自动化运维。
-->

手把手教你用 Kind 从零构建 Kubernetes Operator！创建 CRD `PodDiagnoser`，实现控制器，监控 Pod 状态，自动添加崩溃信息注释，执行修复。掌握云原生 Operator 模式，简化 Kubernetes 集群管理，提升可观测性，实现基础设施自动化运维。

> 译自：[How To Build a Kubernetes Operator From Scratch](https://thenewstack.io/how-to-build-a-kubernetes-operator-from-scratch/)
> 
> 作者：Joshua Masiko

在 [Kubernetes](https://thenewstack.io/kubernetes/) 中构建强大、可扩展的应用程序通常需要精细的自动化，而这正是 [Kubernetes operators](https://thenewstack.io/kubernetes-operators-the-real-reason-your-boss-is-smiling/) 发挥作用的地方。Operators 通过自动管理自定义资源和有状态应用程序来扩展 Kubernetes 的功能。可以将 operators 视为知道如何操作你的应用程序的软件，即使在复杂的环境中也能确保一切顺利运行。

我将指导你完成从头开始创建 Kubernetes operator 的步骤，这对于在现代云原生生态系统中工作的任何人来说都是至关重要的技能。我们将逐步构建一个“自愈诊断”operator，旨在提高 Kubernetes 集群中的[可观测性](https://thenewstack.io/observability/)。使用此 operator，崩溃信息会自动注释到 Pod，并且可以按需应用修复操作。

## 为什么这对你很重要？

对于任何管理 Kubernetes 集群的人来说，operators 可以简化工作流程，减少手动干预，并实现主动的基础设施管理。

本教程摒弃了理论，为你提供了实践性的真实世界经验，涵盖：

1. **完整的本地工作流程：** 学习如何使用 [Kind](https://kind.sigs.k8s.io/)（一种用于在本地测试 Kubernetes 的工具）和容器管理器 Docker 在本地运行和测试所有内容。
2. **真实世界的 operator 模式：** 你将创建自定义资源定义 (CRD)，实现协调循环，并利用 Kubernetes 客户端 API。
3. **即时反馈：** 然后，你将测试你的 operator，并观察它自动将崩溃信息实时注释到 Pod。

掌握 Kubernetes operators 可以让你精确且可扩展地管理复杂的系统。准备好升级了吗？让我们开始吧！

## 先决条件

首先安装所有必要的工具来构建和运行你的 Kubernetes operator。

**在 macOS 上安装先决条件**

```
# Install Docker Desktop
brew install --cask docker

# Install kubectl
brew install kubectl

# Install Kind (Kubernetes in Docker)
brew install kind

# Install Go
brew install go

# Install Kubebuilder
curl -L -o kubebuilder "https://go.kubebuilder.io/dl/latest/$(go env GOOS)/$(go env GOARCH)"
chmod +x kubebuilder
sudo mv kubebuilder /usr/local/bin/
```

**在 Linux 上安装先决条件**

```
# Install Docker
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker $USER
newgrp docker

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Install Kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.27.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/

# Install Go
wget https://golang.org/dl/go1.24.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.24.1.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.profile
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.profile
source ~/.profile

# Install Kubebuilder
curl -L -o kubebuilder "https://go.kubebuilder.io/dl/latest/$(go env GOOS)/$(go env GOARCH)"
chmod +x kubebuilder
sudo mv kubebuilder /usr/local/bin/
```

**验证你的安装**

```
docker --version
kubectl version --client
kind version
go version
kubebuilder version
```

**使用 Kind 设置集群**

```
# Create a Kubernetes cluster using Kind
kind create cluster --name self-healing-lab

# Verify the cluster is running
kubectl cluster-info
```

如果你需要在任何时候重置你的环境：

```
# Reset your cluster if you need a fresh start
kind delete cluster --name self-healing-lab
kind create cluster --name self-healing-lab
```

## 创建一个测试应用程序

让我们首先在 Golang 中创建一个故意脆弱的应用程序，这将帮助你测试你的 operator。

**创建一个 Go 应用程序**

```bash
mkdir -p fragile-app
cd fragile-app
go mod init local.io/fragile-app
```

创建以下文件：

```
mkdir -p fragile-app
cd fragile-app
go mod init local.io/fragile-app    
 
Create the following files:
main.go:
```

```go
package main

import (
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"sync/atomic"
	"syscall"
)

var requestCount int32

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		count := atomic.AddInt32(&requestCount, 1)
		fmt.Fprintf(w, "Hello from the self-destructing app! %d\n", count)
		if count > 5 {
			fmt.Println("Request limit exceeded. Shutting down...")
			go func() {
				pid := os.Getpid()
				syscall.Kill(pid, syscall.SIGTERM)
			}()
		}
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintln(w, "OK")
	})

	go func() {
		fmt.Println("Server is running on :80")
		if err := http.ListenAndServe(":80", nil); err != nil {
			fmt.Printf("Server error: %v\n", err)
		}
	}()

	// Handle termination signals
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)
	<-stop
	fmt.Println("Server stopped")
}
```

**Dockerfile**

```dockerfile
# Use a small base image
FROM golang:1.24-alpine

# Set working directory
WORKDIR /app

# Copy and build the Go app
COPY . .
RUN go build -o fragile-app

# Expose port 80 and run the app
EXPOSE 80
CMD ["./fragile-app"]
```

**本地构建和测试**

```bash
# Build the Docker image
docker build -t fragile-app:latest .

# Run it locally
docker run -p 8080:80 --rm fragile-app:latest
```

In another terminal, send requests to test the application; it should crash after five requests:

```bash
for i in {1..6}; do curl localhost:8080; echo; done
```

**部署到 Kubernetes**

创建部署清单：

`fragile-app-deployment.yaml:`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fragile-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fragile-app
  template:
    metadata:
      labels:
        app: fragile-app
    spec:
      containers:
        - name: app
          image: fragile-app:latest
          imagePullPolicy: Never
          ports:
            - containerPort: 80
          livenessProbe:
            httpGet:
              path: /health
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 3
          readinessProbe:
            httpGet:
              path: /health
              port: 80
            initialDelaySeconds: 2
            periodSeconds: 3
          resources:
            limits:
              cpu: "100m"
              memory: "128Mi"
```

部署到您的 Kind 集群：

```bash
# Load the local image into Kind
kind load docker-image fragile-app:latest --name self-healing-lab

# Apply the deployment
kubectl apply -f fragile-app-deployment.yaml

# Check that the pod is running
kubectl get pods
```

在集群中测试应用程序：

```bash
# Port forward to the pod
POD_NAME=$(kubectl get pods -l app=fragile-app -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD_NAME 8080:80
```

在另一个终端中，发送请求以使应用程序崩溃：

```bash
for i in {1..10}; do curl localhost:8080; echo; done
```

观察 Kubernetes 重新启动 pod：

```bash
kubectl get pods -w
```

## 理解 Operator 模式

在构建 Operator 之前，最好了解是什么让它如此特别。

**什么是 Kubernetes Operator？**

Operator 是一种扩展 Kubernetes 以处理应用程序特定操作任务的模式。它的工作方式如下：

- 它定义自定义资源（即 CRD），这些资源表示应用程序的所需状态。
- 它实现控制器，这些控制器不断地将实际状态与所需状态进行协调。

可以将 Operator 视为自动化的领域专家，他们可以监控应用程序的运行状况、对更改或问题做出反应，并应用专门的知识来解决问题。

**协调循环**

Operator 的核心是协调循环！可以将其视为 Kubernetes 不断从当前状态移动到所需状态的方式。

```
┌─────────────┐            ┌─────────────┐
│  Observed   │            │   Desired   │
│    State    │─────────►  │    State    │
└─────────────┘            └─────────────┘
       ▲                          │
       │                          │
       │                          ▼
       │                  ┌──────────────┐
       └───────────────── │ Reconcile()  │
                          └──────────────┘
```

每当 pod 发生更改时，都会触发控制器。然后它：

1. 检查 pod 是否与任何 PodDiagnoser 的目标标签匹配。
2. 检查容器重启信息。
3. 如果检测到崩溃，则添加诊断注释。
4. 应用任何配置的修复措施。

此循环会不断重复，确保您的 pod 始终具有最新的诊断信息！

## 构建 Operator

现在，让我们创建一个自动诊断 pod 崩溃的 Operator。

**初始化 Operator 项目**

```bash
# Create a directory for your operator
mkdir -p pod-diagnoser-operator
cd pod-diagnoser-operator

# Initialize a new project with kubebuilder
kubebuilder init --domain=local.io --repo=local.io/pod-diagnoser

# Create the API and controller
kubebuilder create api --group=diagnostics --version=v1 --kind=PodDiagnoser --resource=true --controller=true
```

**定义 CRD**

编辑生成的 `api/v1/poddiagnoser_types.go`
文件：

```go
package v1

import (
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// PodDiagnoserSpec defines the desired state of PodDiagnoser
type PodDiagnoserSpec struct {
	// TargetLabels specifies which pods to monitor based on labels
	// +optional
	TargetLabels map[string]string `json:"targetLabels,omitempty"`
	// EnableAnnotations determines whether to add diagnostic annotations
	// +optional
	EnableAnnotations bool `json:"enableAnnotations,omitempty"`
	// RemediationAction specifies what action to take when crashes are detected
	// +optional
	RemediationAction string `json:"remediationAction,omitempty"`
}

// PodDiagnoserStatus defines the observed state of PodDiagnoser
type PodDiagnoserStatus struct {
	// LastProcessedPod is the last pod that was processed
	// +optional
	LastProcessedPod string `json:"lastProcessedPod,omitempty"`
	// DiagnosedPods contains the count of pods that have been diagnosed
	// +optional
	DiagnosedPods int `json:"diagnosedPods,omitempty"`
}

//+kubebuilder:object:root=true
//+kubebuilder:subresource:status

// PodDiagnoser is the Schema for the poddiagnosers API
type PodDiagnoser struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata,omitempty"`
	Spec              PodDiagnoserSpec   `json:"spec,omitempty"`
	Status            PodDiagnoserStatus `json:"status,omitempty"`
}

//+kubebuilder:object:root=true

// PodDiagnoserList contains a list of PodDiagnoser
type PodDiagnoserList struct {
	metav1.TypeMeta `json:",inline"`
	metav1.ListMeta `json:"metadata,omitempty"`
	Items           []PodDiagnoser `json:"items"`
}

func init() {
	SchemeBuilder.Register(&PodDiagnoser{}, &PodDiagnoserList{})
}
```

运行以下命令来更新生成的代码：

```
make generate
```

**实现控制器**

编辑 `internal/controller/poddiagnoser_controller.go`:

```go
package controller
 
import (
    "context"
    "fmt"
    "time"
 
    corev1 "k8s.io/api/core/v1"
    "k8s.io/apimachinery/pkg/api/errors"
    "k8s.io/apimachinery/pkg/runtime"
    "k8s.io/client-go/tools/record"
    "k8s.io/client-go/util/retry"
    ctrl "sigs.k8s.io/controller-runtime"
    "sigs.k8s.io/controller-runtime/pkg/client"
    "sigs.k8s.io/controller-runtime/pkg/log"
 
    diagnosticsv1 "local.io/pod-diagnoser/api/v1"
)
 
// PodDiagnoserReconciler reconciles a PodDiagnoser object
type PodDiagnoserReconciler struct {
    client.Client
    Scheme *runtime.Scheme
    Recorder record.EventRecorder // Add event recorder
}
 
//+kubebuilder:rbac:groups=diagnostics.local.io,resources=poddiagnosers,verbs=get;list;watch;create;update;patch;delete
//+kubebuilder:rbac:groups=diagnostics.local.io,resources=poddiagnosers/status,verbs=get;update;patch
//+kubebuilder:rbac:groups=diagnostics.local.io,resources=poddiagnosers/finalizers,verbs=update
//+kubebuilder:rbac:groups="",resources=pods,verbs=get;list;watch;update;patch
//+kubebuilder:rbac:groups="",resources=events,verbs=create;patch
 
// Reconcile is part of the main kubernetes reconciliation loop
func (r *PodDiagnoserReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    logger := log.FromContext(ctx)
    
    // Get the pod that triggered reconciliation
    pod := &corev1.Pod{}
    if err := r.Get(ctx, req.NamespacedName, pod); err != nil {
        if errors.IsNotFound(err) {
            // Pod was deleted, nothing to do
            return ctrl.Result{}, nil
        }
        logger.Error(err, "Unable to fetch Pod")
        return ctrl.Result{}, err
    }
 
    // Get all PodDiagnosers
    diagnoserList := &diagnosticsv1.PodDiagnoserList{}
    if err := r.List(ctx, diagnoserList); err != nil {
        logger.Error(err, "Unable to list PodDiagnosers")
        return ctrl.Result{}, err
    }
 
    // Check if this pod should be diagnosed based on PodDiagnoser rules
    var matchingDiagnoser *diagnosticsv1.PodDiagnoser
    for i := range diagnoserList.Items {
        diagnoser := &diagnoserList.Items[i]
        if shouldDiagnosePod(diagnoser, pod) {
            matchingDiagnoser = diagnoser
            break
        }
    }
 
    if matchingDiagnoser == nil {
        // No matching diagnoser for this pod
        return ctrl.Result{}, nil
    }
 
    // Check for container restarts and diagnose
    updated := false
    for _, containerStatus := range pod.Status.ContainerStatuses {
        if containerStatus.RestartCount > 0 && containerStatus.LastTerminationState.Terminated != nil {
            // Container has restarted at least once
            if pod.Annotations == nil {
                pod.Annotations = make(map[string]string)
            }
 
            // Add diagnostic annotations
            restartReason := containerStatus.LastTerminationState.Terminated.Reason
            exitCode := containerStatus.LastTerminationState.Terminated.ExitCode
            restartTime := containerStatus.LastTerminationState.Terminated.FinishedAt.Time
            
            pod.Annotations["diagnostics.local.io/restart-reason"] = 
                fmt.Sprintf("%s (Exit Code: %d)", restartReason, exitCode)
            pod.Annotations["diagnostics.local.io/restart-time"] = 
                restartTime.Format(time.RFC3339)
            
            updated = true
            
            logger.Info("Diagnosed pod restart",
                "pod", pod.Name,
                "container", containerStatus.Name,
                "reason", restartReason,
                "exitCode", exitCode)
        }
    }
 
    if updated {
        // Update the pod with new annotations using retry for robustness
        if err := retry.RetryOnConflict(retry.DefaultRetry, func() error {
            // Get the latest version to avoid conflicts
            latest := &corev1.Pod{}
            if err := r.Get(ctx, req.NamespacedName, latest); err != nil {
                return err
            }
            
            // Update annotations
            if latest.Annotations == nil {
                latest.Annotations = make(map[string]string)
            }
            latest.Annotations["diagnostics.local.io/restart-reason"] = 
                pod.Annotations["diagnostics.local.io/restart-reason"]
            latest.Annotations["diagnostics.local.io/restart-time"] = 
                pod.Annotations["diagnostics.local.io/restart-time"]
                
            return r.Update(ctx, latest)
        }); err != nil {
            logger.Error(err, "Failed to update Pod with diagnostic annotations")
            return ctrl.Result{}, err
        }
        
        // Update the diagnoser status with retry for robustness
        if err := retry.RetryOnConflict(retry.DefaultRetry, func() error {
            // Get the latest version
            latest := &diagnosticsv1.PodDiagnoser{}
            if err := r.Get(ctx, client.ObjectKey{
                Namespace: matchingDiagnoser.Namespace,
                Name:      matchingDiagnoser.Name,
            }, latest); err != nil {
                return err
            }
            
            latest.Status.LastProcessedPod = pod.Name
            latest.Status.DiagnosedPods++
            return r.Status().Update(ctx, latest)
        }); err != nil {
            logger.Error(err, "Unable to update PodDiagnoser status")
            return ctrl.Result{}, err
        }
        
        // Apply remediation if configured
        if matchingDiagnoser.Spec.RemediationAction != "" {
            if err := r.applyRemediation(ctx, matchingDiagnoser, pod); err != nil {
                logger.Error(err, "Failed to apply remediation")
                return ctrl.Result{}, err
            }
        }
    }
 
    return ctrl.Result{}, nil
}
 
// shouldDiagnosePod determines if this pod should be diagnosed by the given diagnoser
func shouldDiagnosePod(diagnoser *diagnosticsv1.PodDiagnoser, pod *corev1.Pod) bool {
    if !diagnoser.Spec.EnableAnnotations {
        return false
    }
    
    // If no target labels specified, match all pods
    if len(diagnoser.Spec.TargetLabels) == 0 {
        return true
    }
    
    // Check if pod matches all target labels
    for key, value := range diagnoser.Spec.TargetLabels {
        if pod.Labels[key] != value {
            return false
        }
    }
    
    return true
}
 
// applyRemediation applies remediation based on the diagnoser configuration
func (r *PodDiagnoserReconciler) applyRemediation(ctx context.Context, 
    diagnoser *diagnosticsv1.PodDiagnoser, pod *corev1.Pod) error {
    
    logger := log.FromContext(ctx)
    
    switch diagnoser.Spec.RemediationAction {
    case "RestartPod":
        logger.Info("Applying remediation: restarting pod", "pod", pod.Name)
        // Just delete the pod, the deployment controller will create a new one
        return r.Delete(ctx, pod)
    
    case "LogEvent":
        // Use the Kubernetes event recorder to log an event
        r.Recorder.Event(pod, 
            corev1.EventTypeWarning, 
            "PodRestarted", 
            fmt.Sprintf("Pod %s restarted due to %s (Exit Code: %d)",
                pod.Name,
                pod.Annotations["diagnostics.local.io/restart-reason"],
                pod.Status.ContainerStatuses[0].LastTerminationState.Terminated.ExitCode))
        return nil
        
    default:
        logger.Info("No remediation action defined or unknown action", 
            "action", diagnoser.Spec.RemediationAction)
        return nil
    }
}
 
// SetupWithManager sets up the controller with the Manager.
func (r *PodDiagnoserReconciler) SetupWithManager(mgr ctrl.Manager) error {
    // Initialize the event recorder
    r.Recorder = mgr.GetEventRecorderFor("pod-diagnoser")
    
    return ctrl.NewControllerManagedBy(mgr).
        For(&corev1.Pod{}).
        Complete(r)
}
```

更新基于角色的访问控制 (RBAC) 清单：

```
make manifests
```

**设置 RBAC 权限**

创建一个名为 `operator-permissions.yaml` 的文件：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pod-diagnoser-operator-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch", "update", "patch"]
- apiGroups: [""]
  resources: ["events"]
  verbs: ["create", "patch"]
- apiGroups: ["apps"]
  resources: ["deployments", "replicasets"]
  verbs: ["get", "list", "watch", "update"]
- apiGroups: ["diagnostics.local.io"]
  resources: ["poddiagnosers", "poddiagnosers/status", "poddiagnosers/finalizers"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pod-diagnoser-operator-rolebinding
subjects:
- kind: ServiceAccount
  name: pod-diagnoser-operator-controller-manager
  namespace: pod-diagnoser-operator-system
roleRef:
  kind: ClusterRole
  name: pod-diagnoser-operator-role
  apiGroup: rbac.authorization.k8s.io
```

**修改配置目录中的 Deployment 清单**

1. 找到你的 Operator 的 Deployment YAML 文件，通常在 `config/manager/manager.yaml` 中
2. 添加 `imagePullPolicy: Never` 到容器规范中：

```yaml
spec:
  template:
    spec:
      containers:
      - name: manager
        image: controller:latest
        imagePullPolicy: Never # Add this line
```

**构建和部署 Operator**

```bash
# Build the operator image
make docker-build IMG=pod-diagnoser:latest

# Load the image into the Kind cluster
kind load docker-image pod-diagnoser:latest --name self-healing-lab

# Install the CRDs
make install

# Deploy the operator
make deploy IMG=pod-diagnoser:latest
```

应用 RBAC 权限：

```bash
kubectl apply -f operator-permissions.yaml
```

检查 Operator 是否正在运行：

```bash
kubectl get pods -n pod-diagnoser-operator-system
```

如果 Pod 在拉取镜像时遇到问题，你可能需要重启它：

```bash
kubectl delete pod -n pod-diagnoser-operator-system \
  $(kubectl get pods -n pod-diagnoser-operator-system -o jsonpath='{.items[0].metadata.name}')
```

**安全警报：** 虽然使用 `cluster-admin` 对于实验来说很方便，但它授予了过多的权限。对于生产环境，始终遵循最小权限原则，创建仅具有必要权限的自定义角色。

如果仍然看到 RBAC 错误，可以暂时授予更广泛的权限以进行开发：

```bash
# For development only - not recommended for production
kubectl create clusterrolebinding pod-diagnoser-admin \
  --clusterrole=cluster-admin \
  --serviceaccount=pod-diagnoser-operator-system:pod-diagnoser-operator-controller-manager
```

**创建 PodDiagnoser 实例**

创建一个名为 `config/samples/diagnostics_v1_poddiagnoser.yaml` 的文件：

```yaml
apiVersion: diagnostics.local.io/v1
kind: PodDiagnoser
metadata:
  name: fragileapp-diagnoser
spec:
  targetLabels:
    app: fragile-app
  enableAnnotations: true
  remediationAction: "LogEvent"
```

将其应用到你的集群：

```bash
kubectl apply -f config/samples/diagnostics_v1_poddiagnoser.yaml
```

**查看 Operator 日志**

```bash
POD_NAME=$(kubectl get pods -n pod-diagnoser-operator-system -o jsonpath='{.items[0].metadata.name}')
kubectl logs -n pod-diagnoser-operator-system $POD_NAME -c manager
```

**测试 Operator**

触发 fragile app 崩溃：

```bash
# Port forward to the pod
POD_NAME=$(kubectl get pods -l app=fragile-app -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward $POD_NAME 8080:80
```

在另一个终端中，发送请求以使应用程序崩溃：

```bash
for i in {1..10}; do curl localhost:8080; echo; done
```

等待 Pod 重新启动，然后检查 Operator 是否添加了诊断注解：

```bash
kubectl get pod -l app=fragile-app -o jsonpath='{.items[0].metadata.annotations}'
```

你应该看到如下注解：

```json
{"diagnostics.local.io/restart-reason":"Completed (Exit Code: 0)","diagnostics.local.io/restart-time":"2025-03-06T16:10:28Z"}%
```

此外，检查 Operator 记录的事件：

```bash
kubectl get events | grep PodRestarted
```

你应该看到如下事件：

```
56s Warning PodRestarted pod/fragile-app-6488586b44-n7qg7 Pod fragile-app-6488586b44-n7qg7 restarted due to Completed (Exit Code: 0) (Exit Code: 0)
```

## 清理

完成本教程后，就可以清理你的资源了：

```bash
# Delete the test application
kubectl delete -f fragile-app-deployment.yaml

# Delete the PodDiagnoser custom resource
kubectl delete -f config/samples/diagnostics_v1_poddiagnoser.yaml

# Uninstall the operator and CRDs
make undeploy
make uninstall

# Delete the cluster when you're done
kind delete cluster --name self-healing-lab
```

## 结论

恭喜！您已成功构建了一个 Kubernetes Operator，它可以诊断 Pod 崩溃，应用修复策略，并与 Kubernetes 事件无缝集成，以增强可观测性。这一成就不仅展示了您对 Operator 模式的理解，还突显了您使用特定于领域的自动化和智能来扩展 Kubernetes 的能力。

通过利用 Operator 的强大功能，您丰富了 Kubernetes 的自我修复能力，创建了一个更智能、更高效的系统，该系统可以通过诊断见解主动解决应用程序故障。

未来成功的关键要点：

*   **CRDs:** 您现在知道如何定义根据您的应用程序需求量身定制的模式！
*   **Controllers and reconciliation:** 您已经掌握了如何构建驱动 Operator 的控制循环。
*   **Robust error handling:** 您现在可以实施重试机制，确保未来运营的弹性。
*   **RBAC and security:** 您已经确定了权限范围，使您的 Operator 可以用于生产环境。

这个项目证明了将 Kubernetes 的强大功能与精确的、专门构建的自动化相结合的可能性。继续构建、迭代并突破 Kubernetes 环境可以实现的界限。未来由这样的创新驱动，所以走出去，继续创造奇迹。

通过 Andela 的指南“[使用 GitHub 和 ArgoCD 为 Kubernetes 构建可扩展的 CI/CD 管道](https://www.andela.com/blog-posts/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=kubernetes-operators&utm_term=writers-room)”，了解如何为 Kubernetes 构建可扩展的 CI/CD 管道。