# How To Build a Kubernetes Operator From Scratch
![Featued image for: How To Build a Kubernetes Operator From Scratch](https://cdn.thenewstack.io/media/2025/05/bc9c55e1-build-kubernetes-operator-1024x576.jpg)
Building robust, scalable applications in [Kubernetes](https://thenewstack.io/kubernetes/) often requires fine-tuned automation — and that’s where [Kubernetes operators](https://thenewstack.io/kubernetes-operators-the-real-reason-your-boss-is-smiling/) come into play. Operators extend Kubernetes’ capabilities by automating management of custom resources and stateful applications. Think of operators as software that knows how to operate your apps, ensuring everything runs smoothly, even in complex environments.

I will guide you through the steps of creating a Kubernetes operator from scratch, a crucial skill for anyone working in modern cloud native ecosystems. We’ll walk through building a “self-healing diagnostics” operator, designed to boost [observability](https://thenewstack.io/observability/) in Kubernetes clusters. With this operator, crash information is automatically annotated to pods, and remediation actions can be applied on demand.

## Why Is This Important to You?
For anyone managing Kubernetes clusters, operators streamline workflows, reduce manual intervention and allow proactive infrastructure management.

This tutorial cuts through the theory and gives you practical, real-world experience, covering:

**Full local workflow:**Learn how to run and test everything locally using[Kind](https://kind.sigs.k8s.io/), a tool for testing Kubernetes locally, and container manager Docker.**Real-world operator patterns:**You’ll create Custom Resource Definitions (CRDs), implement reconciliation loops and leverage the Kubernetes client API.**Immediate feedback:**You’ll then test your operator and watch it automatically annotate crash information to pods in real time.
Mastering Kubernetes operators sets you up to manage complex systems with precision and scalability. Ready to level up? Let’s get started!

**Prerequisites**
Start by installing all the necessary tools to build and run your Kubernetes operator.

**Installing prerequisites on macOS**
12345678910111213141516 |
# Install Docker Desktopbrew install --cask docker# Install kubectlbrew install kubectl# Install Kind (Kubernetes in Docker)brew install kind# Install Gobrew install go# Install Kubebuildercurl -L -o kubebuilder "https://go.kubebuilder.io/dl/latest/$(go env GOOS)/$(go env GOARCH)"chmod +x kubebuildersudo mv kubebuilder /usr/local/bin/ |
**Installing prerequisites on Linux**
12345678910111213141516171819202122232425262728293031 |
# Install Dockersudo apt-get updatesudo apt-get install -y apt-transport-https ca-certificates curl software-properties-commoncurl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"sudo apt-get updatesudo apt-get install -y docker-ce docker-ce-cli containerd.iosudo usermod -aG docker $USERnewgrp docker# Install kubectlcurl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"chmod +x kubectlsudo mv kubectl /usr/local/bin/# Install Kindcurl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.27.0/kind-linux-amd64chmod +x ./kindsudo mv ./kind /usr/local/bin/# Install Gowget https://golang.org/dl/go1.24.1.linux-amd64.tar.gzsudo tar -C /usr/local -xzf go1.24.1.linux-amd64.tar.gzecho 'export PATH=$PATH:/usr/local/go/bin' >> ~/.profileecho 'export PATH=$PATH:$HOME/go/bin' >> ~/.profilesource ~/.profile# Install Kubebuildercurl -L -o kubebuilder "https://go.kubebuilder.io/dl/latest/$(go env GOOS)/$(go env GOARCH)"chmod +x kubebuildersudo mv kubebuilder /usr/local/bin/ |
**Verify your installations**
12345 |
docker --versionkubectl version --clientkind versiongo versionkubebuilder version |
**Set Up a Cluster With Kind**
12345 |
# Create a Kubernetes cluster using Kindkind create cluster --name self-healing-lab# Verify the cluster is runningkubectl cluster-info |
If you need to reset your environment at any point:
123 |
# Reset your cluster if you need a fresh startkind delete cluster --name self-healing-labkind create cluster --name self-healing-lab |
**Create a Test Application**
Let’s begin by creating a deliberately fragile application in Golang that will help you test your operator.

**Create a Go Application**
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152 |
mkdir -p fragile-appcd fragile-appgo mod init local.io/fragile-app Create the following files:main.go:package mainimport ( "fmt" "net/http" "os" "os/signal" "sync/atomic" "syscall")var requestCount int32func main() { http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) { count := atomic.AddInt32(&requestCount, 1) fmt.Fprintf(w, "Hello from the self-destructing app! %d\n", count) if count > 5 { fmt.Println("Request limit exceeded. Shutting down...") go func() { pid := os.Getpid() syscall.Kill(pid, syscall.SIGTERM) }() } }) http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) { w.WriteHeader(http.StatusOK) fmt.Fprintln(w, "OK") }) go func() { fmt.Println("Server is running on :80") if err := http.ListenAndServe(":80", nil); err != nil { fmt.Printf("Server error: %v\n", err) } }() // Handle termination signals stop := make(chan os.Signal, 1) signal.Notify(stop, os.Interrupt, syscall.SIGTERM) <-stop fmt.Println("Server stopped")} |
**Dockerfile**
12345678910111213 |
# Use a small base imageFROM golang:1.24-alpine# Set working directoryWORKDIR /app# Copy and build the Go appCOPY . .RUN go build -o fragile-app# Expose port 80 and run the appEXPOSE 80CMD ["./fragile-app"] |
**Build and Test Locally**
12345678 |
# Build the Docker imagedocker build -t fragile-app:latest .# Run it locallydocker run -p 8080:80 --rm fragile-app:latestIn another terminal, send requests to test the application; it should crash after five requests:for i in {1..6}; do curl localhost:8080; echo; done |
**Deploy to Kubernetes**
Create a deployment manifest:

`fragile-app-deployment.yaml:`
123456789101112131415161718192021222324252627282930313233343536 |
apiVersion: apps/v1kind: Deploymentmetadata: name: fragile-appspec: replicas: 1 selector: matchLabels: app: fragile-app template: metadata: labels: app: fragile-app spec: containers: - name: app image: fragile-app:latest imagePullPolicy: Never ports: - containerPort: 80 livenessProbe: httpGet: path: /health port: 80 initialDelaySeconds: 5 periodSeconds: 3 readinessProbe: httpGet: path: /health port: 80 initialDelaySeconds: 2 periodSeconds: 3 resources: limits: cpu: "100m" memory: "128Mi" |
Deploy to your Kind cluster:
12345678 |
# Load the local image into Kindkind load docker-image fragile-app:latest --name self-healing-lab# Apply the deploymentkubectl apply -f fragile-app-deployment.yaml# Check that the pod is runningkubectl get pods |
Test the application in the cluster:
123 |
# Port forward to the podPOD_NAME=$(kubectl get pods -l app=fragile-app -o jsonpath="{.items[0].metadata.name}")kubectl port-forward $POD_NAME 8080:80 |
In another terminal, send requests to crash the app:
1 |
for i in {1..10}; do curl localhost:8080; echo; done |
Watch Kubernetes restart the pod:
1 |
kubectl get pods -w |
**Understanding the Operator Pattern**
Before building an operator, it’s good to understand what makes it special.

**What Is a Kubernetes Operator?**
An operator is a pattern that extends Kubernetes to handle application-specific operational tasks. It works by doing the following:

- It defines custom resources (i.e., CRDs) that represent your application’s desired state.
- It implements controllers that continuously reconcile the actual state with the desired state.
Think of operators as automated domain experts that can monitor your application’s health, react to changes or problems, and apply specialized knowledge to fix issues.

**The Reconciliation Loop**
The heart of the operator is the reconciliation loop! Think of it as Kubernetes’ way of constantly moving from the current state to the desired state.

12345678910 |
┌─────────────┐ ┌─────────────┐│ Observed │ │ Desired ││ State │─────────► │ State │└─────────────┘ └─────────────┘ ▲ │ │ │ │ ▼ │ ┌──────────────┐ └───────────────── │ Reconcile() │ └──────────────┘ |
The controller is triggered whenever a pod changes. Then it:
- Checks if the pod matches any PodDiagnoser’s target labels.
- Examines container restart information.
- Adds diagnostic annotations if crashes are detected.
- Applies any configured remediation actions.
This cycle repeats continuously, ensuring your pods always have up-to-date diagnostic information!

**Building an Operator**
Now let’s create an operator that automatically diagnoses pod crashes.

**Initialize the Operator Project**
123456789 |
# Create a directory for your operatormkdir -p pod-diagnoser-operatorcd pod-diagnoser-operator# Initialize a new project with kubebuilderkubebuilder init --domain=local.io --repo=local.io/pod-diagnoser# Create the API and controllerkubebuilder create api --group=diagnostics --version=v1 --kind=PodDiagnoser --resource=true --controller=true |
**Define the CRD**
Edit the generated `api/v1/poddiagnoser_types.go`
file:

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556 |
package v1import ( metav1 "k8s.io/apimachinery/pkg/apis/meta/v1")// PodDiagnoserSpec defines the desired state of PodDiagnosertype PodDiagnoserSpec struct { // TargetLabels specifies which pods to monitor based on labels // +optional TargetLabels map[string]string `json:"targetLabels,omitempty"` // EnableAnnotations determines whether to add diagnostic annotations // +optional EnableAnnotations bool `json:"enableAnnotations,omitempty"` // RemediationAction specifies what action to take when crashes are detected // +optional RemediationAction string `json:"remediationAction,omitempty"`}// PodDiagnoserStatus defines the observed state of PodDiagnosertype PodDiagnoserStatus struct { // LastProcessedPod is the last pod that was processed // +optional LastProcessedPod string `json:"lastProcessedPod,omitempty"` // DiagnosedPods contains the count of pods that have been diagnosed // +optional DiagnosedPods int `json:"diagnosedPods,omitempty"`}//+kubebuilder:object:root=true//+kubebuilder:subresource:status// PodDiagnoser is the Schema for the poddiagnosers APItype PodDiagnoser struct { metav1.TypeMeta `json:",inline"` metav1.ObjectMeta `json:"metadata,omitempty"` Spec PodDiagnoserSpec `json:"spec,omitempty"` Status PodDiagnoserStatus `json:"status,omitempty"`}//+kubebuilder:object:root=true// PodDiagnoserList contains a list of PodDiagnosertype PodDiagnoserList struct { metav1.TypeMeta `json:",inline"` metav1.ListMeta `json:"metadata,omitempty"` Items []PodDiagnoser `json:"items"`}func init() { SchemeBuilder.Register(&PodDiagnoser{}, &PodDiagnoserList{})} |
Run the following command to update the generated code:
1 |
make generate |
**Implement the Controller**
Edit `internal/controller/poddiagnoser_controller.go`
:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167168169170171172173174175176177178179180181182183184185186187188189190191192193194195196197198199200201202203204205206207208209210211212213 |
package controllerimport ( "context" "fmt" "time" corev1 "k8s.io/api/core/v1" "k8s.io/apimachinery/pkg/api/errors" "k8s.io/apimachinery/pkg/runtime" "k8s.io/client-go/tools/record" "k8s.io/client-go/util/retry" ctrl "sigs.k8s.io/controller-runtime" "sigs.k8s.io/controller-runtime/pkg/client" "sigs.k8s.io/controller-runtime/pkg/log" diagnosticsv1 "local.io/pod-diagnoser/api/v1")// PodDiagnoserReconciler reconciles a PodDiagnoser objecttype PodDiagnoserReconciler struct { client.Client Scheme *runtime.Scheme Recorder record.EventRecorder // Add event recorder}//+kubebuilder:rbac:groups=diagnostics.local.io,resources=poddiagnosers,verbs=get;list;watch;create;update;patch;delete//+kubebuilder:rbac:groups=diagnostics.local.io,resources=poddiagnosers/status,verbs=get;update;patch//+kubebuilder:rbac:groups=diagnostics.local.io,resources=poddiagnosers/finalizers,verbs=update//+kubebuilder:rbac:groups="",resources=pods,verbs=get;list;watch;update;patch//+kubebuilder:rbac:groups="",resources=events,verbs=create;patch// Reconcile is part of the main kubernetes reconciliation loopfunc (r *PodDiagnoserReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) { logger := log.FromContext(ctx) // Get the pod that triggered reconciliation pod := &corev1.Pod{} if err := r.Get(ctx, req.NamespacedName, pod); err != nil { if errors.IsNotFound(err) { // Pod was deleted, nothing to do return ctrl.Result{}, nil } logger.Error(err, "Unable to fetch Pod") return ctrl.Result{}, err } // Get all PodDiagnosers diagnoserList := &diagnosticsv1.PodDiagnoserList{} if err := r.List(ctx, diagnoserList); err != nil { logger.Error(err, "Unable to list PodDiagnosers") return ctrl.Result{}, err } // Check if this pod should be diagnosed based on PodDiagnoser rules var matchingDiagnoser *diagnosticsv1.PodDiagnoser for i := range diagnoserList.Items { diagnoser := &diagnoserList.Items[i] if shouldDiagnosePod(diagnoser, pod) { matchingDiagnoser = diagnoser break } } if matchingDiagnoser == nil { // No matching diagnoser for this pod return ctrl.Result{}, nil } // Check for container restarts and diagnose updated := false for _, containerStatus := range pod.Status.ContainerStatuses { if containerStatus.RestartCount > 0 && containerStatus.LastTerminationState.Terminated != nil { // Container has restarted at least once if pod.Annotations == nil { pod.Annotations = make(map[string]string) } // Add diagnostic annotations restartReason := containerStatus.LastTerminationState.Terminated.Reason exitCode := containerStatus.LastTerminationState.Terminated.ExitCode restartTime := containerStatus.LastTerminationState.Terminated.FinishedAt.Time pod.Annotations["diagnostics.local.io/restart-reason"] = fmt.Sprintf("%s (Exit Code: %d)", restartReason, exitCode) pod.Annotations["diagnostics.local.io/restart-time"] = restartTime.Format(time.RFC3339) updated = true logger.Info("Diagnosed pod restart", "pod", pod.Name, "container", containerStatus.Name, "reason", restartReason, "exitCode", exitCode) } } if updated { // Update the pod with new annotations using retry for robustness if err := retry.RetryOnConflict(retry.DefaultRetry, func() error { // Get the latest version to avoid conflicts latest := &corev1.Pod{} if err := r.Get(ctx, req.NamespacedName, latest); err != nil { return err } // Update annotations if latest.Annotations == nil { latest.Annotations = make(map[string]string) } latest.Annotations["diagnostics.local.io/restart-reason"] = pod.Annotations["diagnostics.local.io/restart-reason"] latest.Annotations["diagnostics.local.io/restart-time"] = pod.Annotations["diagnostics.local.io/restart-time"] return r.Update(ctx, latest) }); err != nil { logger.Error(err, "Failed to update Pod with diagnostic annotations") return ctrl.Result{}, err } // Update the diagnoser status with retry for robustness if err := retry.RetryOnConflict(retry.DefaultRetry, func() error { // Get the latest version latest := &diagnosticsv1.PodDiagnoser{} if err := r.Get(ctx, client.ObjectKey{ Namespace: matchingDiagnoser.Namespace, Name: matchingDiagnoser.Name, }, latest); err != nil { return err } latest.Status.LastProcessedPod = pod.Name latest.Status.DiagnosedPods++ return r.Status().Update(ctx, latest) }); err != nil { logger.Error(err, "Unable to update PodDiagnoser status") return ctrl.Result{}, err } // Apply remediation if configured if matchingDiagnoser.Spec.RemediationAction != "" { if err := r.applyRemediation(ctx, matchingDiagnoser, pod); err != nil { logger.Error(err, "Failed to apply remediation") return ctrl.Result{}, err } } } return ctrl.Result{}, nil}// shouldDiagnosePod determines if this pod should be diagnosed by the given diagnoserfunc shouldDiagnosePod(diagnoser *diagnosticsv1.PodDiagnoser, pod *corev1.Pod) bool { if !diagnoser.Spec.EnableAnnotations { return false } // If no target labels specified, match all pods if len(diagnoser.Spec.TargetLabels) == 0 { return true } // Check if pod matches all target labels for key, value := range diagnoser.Spec.TargetLabels { if pod.Labels[key] != value { return false } } return true}// applyRemediation applies remediation based on the diagnoser configurationfunc (r *PodDiagnoserReconciler) applyRemediation(ctx context.Context, diagnoser *diagnosticsv1.PodDiagnoser, pod *corev1.Pod) error { logger := log.FromContext(ctx) switch diagnoser.Spec.RemediationAction { case "RestartPod": logger.Info("Applying remediation: restarting pod", "pod", pod.Name) // Just delete the pod, the deployment controller will create a new one return r.Delete(ctx, pod) case "LogEvent": // Use the Kubernetes event recorder to log an event r.Recorder.Event(pod, corev1.EventTypeWarning, "PodRestarted", fmt.Sprintf("Pod %s restarted due to %s (Exit Code: %d)", pod.Name, pod.Annotations["diagnostics.local.io/restart-reason"], pod.Status.ContainerStatuses[0].LastTerminationState.Terminated.ExitCode)) return nil default: logger.Info("No remediation action defined or unknown action", "action", diagnoser.Spec.RemediationAction) return nil }}// SetupWithManager sets up the controller with the Manager.func (r *PodDiagnoserReconciler) SetupWithManager(mgr ctrl.Manager) error { // Initialize the event recorder r.Recorder = mgr.GetEventRecorderFor("pod-diagnoser") return ctrl.NewControllerManagedBy(mgr). For(&corev1.Pod{}). Complete(r)} |
Update the role-based access control (RBAC) manifests:
1 |
make manifests |
**Set Up RBAC Permissions**
Create a file named `operator-permissions.yaml`
:

123456789101112131415161718192021222324252627282930 |
apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata: name: pod-diagnoser-operator-rolerules:- apiGroups: [""] resources: ["pods"] verbs: ["get", "list", "watch", "update", "patch"]- apiGroups: [""] resources: ["events"] verbs: ["create", "patch"]- apiGroups: ["apps"] resources: ["deployments", "replicasets"] verbs: ["get", "list", "watch", "update"]- apiGroups: ["diagnostics.local.io"] resources: ["poddiagnosers", "poddiagnosers/status", "poddiagnosers/finalizers"] verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]---apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRoleBindingmetadata: name: pod-diagnoser-operator-rolebindingsubjects:- kind: ServiceAccount name: pod-diagnoser-operator-controller-manager namespace: pod-diagnoser-operator-systemroleRef: kind: ClusterRole name: pod-diagnoser-operator-role apiGroup: rbac.authorization.k8s.io |
**Modify the Deployment Manifest in Your Config Directory**
- Locate your operator’s deployment YAML file, typically in
`config/manager/manager.yaml`
- Add
`imagePullPolicy: Never`
to the container spec:
1234567891011yamlCopyspec:template:spec:containers:- name: managerimage: controller:latestimagePullPolicy: Never # Add this line
**Build and Deploy the Operator**
1234567891011 |
# Build the operator imagemake docker-build IMG=pod-diagnoser:latest# Load the image into the Kind clusterkind load docker-image pod-diagnoser:latest --name self-healing-lab# Install the CRDsmake install# Deploy the operatormake deploy IMG=pod-diagnoser:latest |
Apply the RBAC permissions:
1 |
kubectl apply -f operator-permissions.yaml |
Check that the operator is running:
1 |
kubectl get pods -n pod-diagnoser-operator-system |
If the pod is having issues pulling the image, you might need to restart it:
12 |
kubectl delete pod -n pod-diagnoser-operator-system \ $(kubectl get pods -n pod-diagnoser-operator-system -o jsonpath='{.items[0].metadata.name}') |
**Security alert: **While using `cluster-admin`
is convenient for experimentation, it grants excessive privileges. For production, always follow the principle of least privilege by creating custom roles with only the necessary permissions.
If you still see RBAC errors, you can temporarily grant broader permissions for development:

1234 |
# For development only - not recommended for productionkubectl create clusterrolebinding pod-diagnoser-admin \ --clusterrole=cluster-admin \ --serviceaccount=pod-diagnoser-operator-system:pod-diagnoser-operator-controller-manager |
**Create a PodDiagnoser Instance**
Create a file named `config/samples/diagnostics_v1_poddiagnoser.yaml`
:

123456789 |
apiVersion: diagnostics.local.io/v1kind: PodDiagnosermetadata: name: fragileapp-diagnoserspec: targetLabels: app: fragile-app enableAnnotations: true remediationAction: "LogEvent" |
Apply it to your cluster:
1 |
kubectl apply -f config/samples/diagnostics_v1_poddiagnoser.yaml |
**View Operator Logs**
Check the operator logs to see what’s happening:

12 |
POD_NAME=$(kubectl get pods -n pod-diagnoser-operator-system -o jsonpath='{.items[0].metadata.name}')kubectl logs -n pod-diagnoser-operator-system $POD_NAME -c manager |
**Test the Operator**
Trigger the fragile app to crash:

123 |
# Port forward to the podPOD_NAME=$(kubectl get pods -l app=fragile-app -o jsonpath="{.items[0].metadata.name}")kubectl port-forward $POD_NAME 8080:80 |
In another terminal, send requests to crash the app:
1 |
for i in {1..10}; do curl localhost:8080; echo; done |
Wait for the pod to restart, then check if the operator added diagnostic annotations:
1 |
kubectl get pod -l app=fragile-app -o jsonpath='{.items[0].metadata.annotations}' |
You should see annotations like:
1 |
{"diagnostics.local.io/restart-reason":"Completed (Exit Code: 0)","diagnostics.local.io/restart-time":"2025-03-06T16:10:28Z"}% |
Also, check for the event recorded by the operator:
1 |
kubectl get events | grep PodRestarted |
You should see events like:
1 |
56s Warning PodRestarted pod/fragile-app-6488586b44-n7qg7 Pod fragile-app-6488586b44-n7qg7 restarted due to Completed (Exit Code: 0) (Exit Code: 0) |
**Clean Up**
When you’re done with the tutorial, it’s time to clean up your resources:

123456789101112 |
# Delete the test applicationkubectl delete -f fragile-app-deployment.yaml# Delete the PodDiagnoser custom resourcekubectl delete -f config/samples/diagnostics_v1_poddiagnoser.yaml# Uninstall the operator and CRDsmake undeploymake uninstall# Delete the cluster when you're donekind delete cluster --name self-healing-lab |
**Conclusion**
Congratulations! You’ve successfully built a Kubernetes operator that diagnoses pod crashes, applies remediation strategies and integrates seamlessly with Kubernetes events for enhanced visibility. This achievement not only showcases your understanding of the operator pattern but also highlights your ability to extend Kubernetes with domain-specific automation and intelligence.

By leveraging the power of the operator, you’ve enriched Kubernetes’ self-healing capabilities, creating a smarter, more efficient system that proactively addresses application failures with diagnostic insights.

Key takeaways for future success:

**CRDs:**You now know how to define schemas tailored to your application’s needs!**Controllers and reconciliation:**You’ve mastered how to build the control loop that drives your operator.**Robust error handling:**You can now implement retry mechanisms, ensuring resilience in future operations.**RBAC and security:**You’ve scoped permissions, making your operator production-ready.
This project is a testament to what’s possible when you pair Kubernetes’ power with precise, purpose-built automation. Keep building, iterating and pushing the boundaries of what your Kubernetes environment can do. The future is powered by innovation like this, so get out there and keep making things happen.

Learn how to build a scalable CI/CD pipeline for Kubernetes with Andela’s guide “[Make a Scalable CI/CD Pipeline for Kubernetes with GitHub and ArgoCD](https://www.andela.com/blog-posts/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=kubernetes-operators&utm_term=writers-room).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)