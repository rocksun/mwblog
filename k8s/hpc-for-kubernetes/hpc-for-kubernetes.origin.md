[treebeardtech](../)
- Posts
- High Performance Computing (HPC) on Kubernetes
# High Performance Computing (HPC) on Kubernetes
## ML Platform Engineering Tips
![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1ddf7a27-490a-4884-bbfc-3036e3f3dbf6/Nanoscience_High-Performance_Computing_Facility.jpg?t=1712250549)
Machine learning (ML) engineering has evolved into a discipline and career path over the last few years. Whilst software engineers build web, mobile, and embedded experiences, ML engineers deliver model versions, inferences, and entire RAG applications.
What does this mean for an engineering organisation as a whole? My main takeaway is that the platform engineering team that is responsible for increasing the ML team’s leverage must provide a different set of primitives that will support an ML engineer as they go through their
*MLOps* processes.
Maximising an ML team’s leverage requires (a) minimising toil—manual workflows, (b) increasing their delivery velocity, and (c) mitigating inherent risks such as security or cost management failures. If you can do these three things, you’ll be able to scale up your operations.
This advice can apply to many different types of ML components:
**“Serverless” Inference applications**used for real-time customer interactions for fraud detection, product recommendations, or chatbots **Asynchronous inference applications**used for image and video generation or understanding, potentially using long-running workers reading from some stream of requests **Batch systems**which can be used for data-prep, training, offline inference, or evaluation
In this post, we’ll explore some of the options available to ML Platform engineers for providing batch processing capabilities to internal customers on their Kubernetes platform.
## From HPC to Kubernetes
Cloud-native computing on top of Kubernetes has become the de-facto standard for new software projects. This is simple for many use cases, but high-performance computing (HPC) is not a simple area.
As big data applications have evolved from low-level distributed computing libraries like MPI to frameworks such as Spark and Ray, the underlying platforms such as Slurm and LSF are also being challenged by Kubernetes which can be adapted to provide an HPC job-queue interface.
Building out an HPC environment on Kubernetes requires understanding the landscape of tools for constructing a more productive, efficient, and secure environment for ML engineering.
### Kuberay
The Ray project is the most successful and universal approach to making the Python programming language scale to large distributed environments.
Its success with ML engineers means that the Kuberay Operator is a promising approach for increasing the agency of team members. This project effectively turns your K8s cluster into a Ray platform which can be used to provide self-service Ray clusters and jobs to any team.
### Kubeflow Spark Operator
Whilst Ray is attractive for how Python-native it is. Spark has been around a lot longer, meaning there is a huge number of Spark applications and practitioners around.
This spark operator is similar to kuberay, except it manages spark clusters. It was originally developed by Google Cloud and recently donated to the Kubeflow project (
[read more here](https://treebeardtech.beehiiv.com/p/treebeard-update)).
### Volcano
Whilst the first two projects provide a Pythonic entry point to distributed systems, it’s important to ensure that jobs are reliably executed with efficient usage of cloud resources.
As previously mentioned, HPC/job-queue workloads have different requirements to many other applications you may want to host on Kubernetes. This is true specifically for pod scheduling logic, which by default is handled by the kube-scheduler.
ML teams may need features for scheduling jobs according to priority or waiting for a whole set of jobs to be ready before running them.
This is what the volcano project lets you achieve, and it does so by replacing the default kube-scheduler.
### Kueue
Whilst Volcano provides advanced scheduling features by replacing the kube-scheduler, Kueue can do so by complementing the scheduler.
Kueue provides job queueing and prioritisation via the admission webhook — i.e. it catches jobs as you create them and suspends them until it’s their turn.
### Armada
Kueue and Volcano both provide relatively lightweight modifications to Kubernetes’ scheduling features but there is a cost to this. Pending jobs are stored in the cluster config store (etcd) which can cause an availability risk depending on the size of the job queue.
Armada fixes this issue by providing this functionality with its own control plane (as opposed to using the Kubernetes control plane).
HPC users can submit jobs directly to the Armada API, which will gradually submit them to the Kubernetes control plane when ready.
Thanks to this design choice Armada can scale to a large number of jobs and is positioned well for multi-cluster environments.
## Conclusion
Just like how the progress of AI has added the concept of a machine learning engineer to product teams, it has added machine learning platform engineering to infrastructure teams.
Serving ML engineers requires dedicated solutions for the type of system they are building, whether it be a serverless inference application, an async inference application, or a batch system.
As Kubernetes plays a central role in cloud infrastructure, we’ve highlighted 5 open source projects that can be used in batch/HPC systems as you progress on your ML platform engineering journey.