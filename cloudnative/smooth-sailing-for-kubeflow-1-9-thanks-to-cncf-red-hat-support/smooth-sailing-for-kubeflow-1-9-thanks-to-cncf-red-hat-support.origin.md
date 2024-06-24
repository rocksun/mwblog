# Smooth Sailing for KubeFlow 1.9 Thanks to CNCF, Red Hat Support
![Featued image for: Smooth Sailing for KubeFlow 1.9 Thanks to CNCF, Red Hat Support](https://cdn.thenewstack.io/media/2024/03/50b6aa8b-kubeflow-1024x680.jpg)
Since last year, the open source
[MLOps](https://thenewstack.io/mlops-needs-a-better-way-to-manage-gpus/) platform [KubeFlow](https://thenewstack.io/kubeflow-where-machine-learning-meets-the-modern-infrastructure/) has benefitted from a number of powerful new benefactors, including the [Cloud Native Computing Community](https://cncf.io/?utm_content=inline+mention) for open governance, and Red Hat, which has contributed considerable engineering help.
And next month, users will begin to see the fruits of this support. Scheduled
[for release](https://github.com/kubeflow/community/blob/master/releases/release-1.9/READM) in July 8, the next version of KubeFlow will bring a much-requested model registry, based on [Red Hat’s Quay](https://thenewstack.io/red-hats-quay-3-container-supports-multiple-architectures/). It also brings the capability of creating build flows using the [CNCF Argo project](https://thenewstack.io/argo-cd-and-flux-are-cncf-grads-but-what-now/) and a revised notebook format.
Debuting
[in 2018](https://thenewstack.io/kubeflow-manage-ai-workflows-with-kubernetes/), KubeFlow runs on Kubernetes, so it can be run in the cloud or on in-house servers. KubeFlow uses existing open source projects when available. Components include notebooks for experimentation (based on [Jupyter Notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)), pipelines, a user console, and a training operator.
## Why Is Red Hat Interested in KubeFlow?
Much like
[OpenShift ](https://www.openshift.com/try?utm_content=inline+mention)is based on the [Kubernetes](https://thenewstack.io/Kubernetes/) container orchestrator, so too is Red Hat [Open Data Hub](https://opendatahub.io/) built on KubeFlow, noted [Jeremy Eder](https://research.redhat.com/blog/project_member/jeremy-eder/), distinguished engineer at Red Hat, in an interview with TNS. It is also used for the company’s commercially supported [OpenShift AI](https://www.redhat.com/en/technologies/cloud-computing/openshift/openshift-ai), based on the Open Data Hub.
In keeping with the rest of the company’s software portfolio, Red Hat did not build an MLOps tool in-house but instead adopted software already well-supported in the open source community and then allocated engineering help upstream.
While the open source enterprise software company had been supporting Kubeflow for a while — Red Hat customers were already running AI and ML workloads on OpenShift, thanks in art because of its support for GPUs — Red Hat
[ ramped up its investment](https://www.redhat.com/en/blog/open-source-ai-red-hat-our-journey-kubeflow-community) last year when KubeFlow was moved under the CNCF, Eder noted.
KubeFlow 1.9 will be the first release that has benefitted from Red Hat’s increased investment, he said.
“We’re off and running, man,” Eder said. “The engineers on the ground are represented in almost every workstream.”
## What Is New in KubeFlow 1.9?
Red Had had a lot of customers running AI operation on-premises so, they required a local storage system to build and store models and other build artifacts. That was the first Red Hat-led feature for KubeFlow, a registry to hold models and other build artifacts, such as datasets and metric logs.
If you run a MLops system, you need a registry, and while you could use a stock container registry such as
[Red Hat Quay](https://quay.io/) though “there’s subtly different and important workload ways and we want it to cater very specifically to a data science persona,” Eder said.
This registry implements the
[Open Container Interface 1.1](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/) standard, which is also implemented by Quay. The registry is integrated with KubeFlow pipelines, allowing users to deploy directly from the registry.
The model registry will be available as an alpha, though there are some lingering questions about how a model registry should work. So a newly-formed working group is looking for more input from the user community.
This release will come with Kubeflow Notebooks 2.0, which comes with a pair of Kubernetes-friendly custom resource definitions (Workspace and WorkspaceKind) to provide more control over workspaces.
Once the user is done experimenting in a Notebook, they will be able to move the code over to a pipeline to prepare the software for production use.
The new release also updates KubeFlow pipelines. This feature was originally
[built from](https://thenewstack.io/create-machine-learning-apps-in-your-notebook-with-tecton/) the [ Tecton Pipelines](https://www.reddit.com/r/kubernetes/comments/12x6f2b/is_tekton_still_alive_comparing_tekton_pipelines/), With the 1.9 release, the pipeline will also support the CNCF [Argo](https://thenewstack.io/how-far-can-you-go-with-argo/) project in order to “align with the upstream community,” Eder said.
“Being able to express your operational parameters as a pipeline code is hugely enabling from an automation standpoint,” Eder said.
The pipeline feature stitches together two users of KubeFlow: the data scientist and the machine learning engineer.
One ancillary project that KubeFlow community has been working on is
[KServe](https://www.kubeflow.org/docs/external-add-ons/kserve/), a serverless-based inference front end, which recently graduated KubeFlow incubation as its own project. Out-of-box runtimes have recently been added for HuggingFace and vLLM.
“KServe will allow us to auto-serve inference,” Eder said, adding that this is a difficult problem that hasn’t been fully solved yet.
## What Work Needs To Be Done on KubeFlow?
In a KubeFlow Summit talk earlier this year, “
[The Good, Bad and Missing Parts of Kubeflow](https://www.youtube.com/watch?v=GbqwY-KZtjE),” Red Hat Senior Software Engineer, [Ricardo Martinelli de Oliveira](https://github.com/rimolive), who served as the release manager for Kubeflow 1.9, discussed the work that still needs to be done.
In a recent user survey, KubeFlow users said they enjoyed the use of pipelines and notebooks but wanted for more stability with these features. In that same survey, users grumbled about the weak installation — many installed from the raw manifests. There are distributions (such as Red Hat’s), but there needs to be more conformance testing. The documentation on the distributions available are out of date. Some components are barely documented, or not documented at all.
“There are some parts of the [installation documentation] that don’t look good for users,” Martinelli de Oliveira admitted.
Down the road, the project is also working to achieve the criteria to be a CNCF-graduated project. A Technical Oversite Committee needs to be formed, and the project leaders are looking at porting the software over to the ARM64 architecture.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)