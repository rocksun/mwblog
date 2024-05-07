As a backend developer dealing with Kubernetes daily, I’ve always carried the hope of writing an operator to expand the boundaries of my knowledge. However, obstacles emerged and hindered me from achieving this goal.
This is the story of how I wrote the
[gobackup-operator](https://github.com/gobackup/gobackup-operator) while serving in the military. *tl;dr*: Jump right into “Dive into the project” section
## Sharpening the axe
The intention of writing a Kubernetes(K8s) operator was growing within me. I began reading articles, exploring GitHub repositories, and consulting my colleagues about it. Although I can’t say it was entirely successful, the intention remained alive.
The result of all those efforts was a collection of tutorial projects stored in my
[GitHub account](https://github.com/payamQorbanpour).
The process of practising began approximately a year ago when I was first introduced to kubernetes. I was watching Guru’s tutorial for CKAD and then Nana’s tutorial on youtube.
I should mention that the process of practicing approximately began a year ago when I was first introduced to Kubernetes. I started by watching
[Guru’s tutorial](https://www.pluralsight.com/cloud-guru/courses/certified-kubernetes-application-developer-ckad) for CKAD and then [Nana’s tutorial](https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana) on YouTube.
## Turn into ashes
I was deployed for military service.
There was no internet connection, nor even a single electronic device. Instead, we had only hardcover books, volleyball, and the mesmerizing views of sunrise and sunset to entertain us.
In this situation, the thought of creating an operator was fading away. All I cared about was eating, reading books, and enjoying time to time freedom(vacation). However, sometimes that freedom is short, as the commander once remarked:
The joy of vacation ends the moment you leave the barracks.
The training course ended, and I began working as an employee in the office, but the lack of internet connectivity was felt there too! In the evenings, I left the office and pursued the job I loved. Sometimes, you have better performance in limited time. So, from 4 pm to 9 pm, I had to create something special. And it was indeed special to me!
## The Simorgh has risen
After all, with the help of
[this series](https://www.codereliant.io/build-kubernetes-operator-kubebuilder/) I managed to write another Kubernetes operator from the tutorials :) but this time, it was different.
## Hands-on Kubernetes Operator Development: Kubebuilder
### Learn how to develop a Kubernetes Operator from scratch with this hands-on kubebuilder tutorial.
www.codereliant.io
My colleagues had already developed a backup system, but it appeared to be not working very well. So, they explored for another solution and came across a project named
[gobackup](https://gobackup.github.io/), designed to regularly back up databases and push them to storage. The issue was that the project didn’t include support for the etcd database. Therefore, they decided to [contribute](https://github.com/gobackup/gobackup/pull/225) to the project by adding etcd support to meet the requirements. This ultimately led to a new [release](https://github.com/gobackup/gobackup/releases/tag/v2.10.0).
In my absence, they decided to develop a Kubernetes operator based on it. This was a significant step for me. When they shared it with me, I eagerly examined the project and thought, “Finally, this is it. The operator is about to be created. Yaay!”
While reading the project, I noticed a problem in the project’s README. One of the links led to a 404 page. I took the initiative to fix this and submitted a pull request.
[The owners](https://github.com/huacnlee) accepted it with open arms. :)
Encountering such openness, one of my colleagues suggested that we could place this operator under the
[gobackup organization](https://github.com/gobackup) so that more people could contribute to its development.
I opened an
[issue](https://github.com/gobackup/gobackup/issues/231) and proposed a repository under the [gobackup organization](https://github.com/gobackup), and the openness to collaborate was still present.
During the days, I was serving in the military, and during the nights, I was committing to the gobackup-operator project.
## Dive into the project
I began by setting up my environment.
Fortunately, I already had
Golang,
Docker, and
kubectl installed on my computer. Through previous practices, I had become familiar with local machine Kubernetes clusters like
Kind and tools for creating operators such as
kubebuilder.
So, I initiated the operator code.
$ kubebuilder init --domain gobackup.io --repo github.com/gobackup/gobackup-operator
Then I proceeded to create the APIs for the operator:
$ kubebuilder create api --group gobackup --version v1 --kind Backup
Create Resource [y/n]
y
Create Controller [y/n]
y
And the same for databases and storages:
$ kubebuilder create api --group database.gobackup --version v1 --kind PostgreSQL
Create Resource [y/n]
y
Create Controller [y/n]
y
$ kubebuilder create api --group storage.gobackup --version v1 --kind S3
Create Resource [y/n]
y
Create Controller [y/n]
y
I modified the APIs based on the specific requirements of project:
// Backup is the Schema for the backups API
type Backup struct {
metav1.TypeMeta `json:",inline"`
metav1.ObjectMeta `json:"metadata,omitempty"`
Spec BackupSpec `json:"spec,omitempty"`
Status BackupStatus `json:"status,omitempty"`
BackupModelRef BackupModelRef `json:"backupModelRef,omitempty"`
StorageRefs []StorageRef `json:"storageRefs,omitempty"`
DatabaseRefs []DatabaseRef `json:"databaseRefs,omitempty"`
}
Next I modified
Reconcile method:
//+kubebuilder:rbac:groups=gobackup.io,resources=backups,verbs=get;list;watch;create;update;patch;delete
//+kubebuilder:rbac:groups=gobackup.io,resources=backups/status,verbs=get;update;patch
//+kubebuilder:rbac:groups=gobackup.io,resources=backups/finalizers,verbs=update
func (r *BackupReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
// reconcile implementation
}
## Test it out
Before testing it out, you needed to prepare a test database to back up from. Therefore, Create a PostgreSQL deployment, using the following yaml file available
gobackup-operator-postgres-deployment.yaml file:
apiVersion: apps/v1
kind: Deployment
metadata:
name: postgres-deployment
spec:
selector:
matchLabels:
app: postgres
replicas: 1
template:
metadata:
labels:
app: postgres
spec:
containers:
- name: postgres
image: postgres:14.11
env:
- name: POSTGRES_USER
value: ""
- name: POSTGRES_PASSWORD
value: ""
- name: PGDATA
value: "/var/lib/postgresql/data/pgdata"
volumeMounts:
- mountPath: /var/lib/postgresql/data
name: postgredb
volumes:
- name: postgredb
persistentVolumeClaim:
claimName: postgres-pvc
Remember modifying
*POSTGRES_USER *and *POSTGRES_PASSWORD* in the manifest and the apply it:
kubectl apply -f example/gobackup-opetator-postgres-deployment.yaml,
example/gobackup-opetator-postgres-service.yaml
Additionally, I added some resources to test it inside the Kubernetes cluster, including deployments, roles, clusterroles, serviceaccounts, etc., all of which are available in the
gobackup-operator/example/ directory.
So apply these manifest to add base resources:
kubectl apply -f example/gobackup-opetator-serviceaccount.yaml,
gobackup-opetator-pvc.yaml,
gobackup-opetator-namespace.yaml,
gobackup-opetator-clusterrolebinding.yaml,
gobackup-opetator-clusterrole.yaml
And then storage and database manifests:
kubectl apply -f example/gobackup-opetator-storage/*
kubectl apply -f example/gobackup-opetator-database/*
Using the following manifest, I was able to run the operator on my local machine:
kubectl apply -f example/gobackup-opetator-deployment.yaml
So whenever a Backup or CronBackup object is created or changed, the operator will perform the necessary tasks.
To create a backup model to set backup configuration:
kubectl apply -f example/gobackup-opetator/gobackup-opetator-backupmodel.yaml
Applying one of manifests in
gobackup-operator/example/gobackup-operator directory, backup or cronbackup, will trigger the operator to run the backup:
kubectl apply -f example/gobackup-opetator/gobackup-opetator-cronbackup.yaml
## Conclusion
At first, I felt embarrassed about making such a small change in the README file. It felt like one of those PRs you make just to contribute to Hacktoberfest commits.
But then I thought about its effectiveness. Even those single-line commits were impactful. Who knows, I might not have created this operator if I hadn’t made that change to the README document.
*Small steps count!*
You’re always welcome to take a look and contribute
[here](https://github.com/gobackup/gobackup-operator). If you need to change even the README file, don’t hesitate to do it. ;)
If you found this post charming then
clap, comment and followfor more .