# Kubernetes Powers Mastercard’s AI-Workbench for Secure Innovation
![Featued image for: Kubernetes Powers Mastercard’s AI-Workbench for Secure Innovation](https://cdn.thenewstack.io/media/2025/04/9633e0a9-kubernetes-mastercard-ai-workbench-1024x576.jpg)
AI isn’t a foreign idea for many businesses today. With the right tools, platforms and team, useful business implementations of AI and machine learning can grow as an extension of a company’s current infrastructure. For Mastercard, a [deep understanding of data science](https://roadmap.sh/ai-data-scientist) was already built into the globe-spanning payments company.

[Alexander Hughes](https://www.linkedin.com/in/alexanderwilliamhughes), director of software engineering at Mastercard, said that the company’s mission is to “connect and power an inclusive digital economy that benefits everyone everywhere by making transactions safe, simple, smart and accessible. We leverage secure data and networks, partnerships and passion to deliver solutions and innovations that help individuals, financial institutions, governments and businesses to realize their greatest potential.”
## Creating Space for Experimentation
He was presenting with Ravishankar Rao, principal Kubernetes architect of record at Mastercard, at [OpenShift Commons Gathering](https://commons.openshift.org/), a KubeCon Salt Lake City[ co-located event](https://commons.openshift.org/gatherings/kubecon-24-nov-12/), late last year. In their presentation, they detailed the transformation they’ve enabled at Mastercard for their data scientists. They first envisioned a new platform, built around the idea of having space for experimentation that can seamlessly and safely move to production.

“We wanted to make sure that this platform empowered the data engineers and the data scientists with a rapid experimentation space, and we do that using [Jupyter Notebooks](https://jupyter.org/). This is coupled with fine-tuned CPU and GPU profiles for efficient resource utilization, allowing for quick iterations and innovative solutions,” said Hughes.

“Next, we started to address the workflow orchestration for training. So we enabled efficient and scalable machine learning model training through dynamic GPU allocation and specialized GPU cluster environments,” said Hughes.

“We have centralized collaboration features that further enhance the training workflow, making it seamless and productive,” he continued “The platform offers the capability to seamlessly register, manage and share features. This fosters collaborative feature engineering, ensuring that these teams can work together effectively and leverage shared resources.”

## Building the AI-Workbench on Kubernetes
![AI-Workbench capabilities: elastic compute, workload segregation, dedicated AI/ML ecosystem, workflow instantiation, model serving](https://cdn.thenewstack.io/media/2025/04/01259fd9-mastercard-ai-workbench-kubernetes-capabilities.png)
Key capabilities of Mastercard’s AI-Workbench on Kubernetes. Source: Mastercard

Already dubbed the AI-Workbench, this new platform also had dramatic [security requirements](https://thenewstack.io/security/), because there’s no greater source of credit-card information than a credit-card provider. It’s the very essence of private data, and it forms the core of Mastercard’s data set.

Naturally, being able to run this type of AI-Workbench in an offline mode, without even the whiff of open internet access for workloads and clusters, is the best-case scenario for this type of work, and that’s why Mastercard [built with Red Hat OpenShift](https://thenewstack.io/choosing-the-right-red-hat-ai-solution-rhel-ai-vs-openshift-ai/): Clusters can be run in disconnected environments.

“Everything that we do in this workbench is based on [Kubernetes](https://thenewstack.io/kubernetes/), but we wanted to make sure the resources of the Kubernetes cluster that we’re talking about were protected and isolated from general-purpose workloads, and we do that with purpose-built pure AI/ML clusters. This ensures a dedicated ecosystem tailored for those advanced purposes,” Hughes said.

“In the realm of AI product development, we noticed that our engineers are frequently performing repetitive tasks, and so we’ve implemented an automated workflow instantiation assisting with activities such as hyperparameter optimization, model selection and feature selection,” Hughes explained.

![Architecture includes UX (Spark workloads, Jupyter CLI, Kubeflow dashboard and profiles) and Workbench platform to deploy AI/ML and Spark workloads.](https://cdn.thenewstack.io/media/2025/04/8d82b18b-ai-workbench-technical-diagram.png)
Technical diagram of the components of the AI-Workbench at Mastercard. Source: Mastercard

Rao described the final steps and process of building out AI-Workbench. “We integrated all the components of the Kubeflow and the Spark Operator so that the data scientists can run their AI/ML workloads. Towards the end of this, what we actually achieved was we were able to, in an automated way, deploy quite a few AI-Workbenches in development, staging and production environments, and we were able to onboard a large set of data scientists on this platform and able to deliver some value-added solutions. The most important aspect was we were also able to bring in the GPU compute, which accelerated the training and moved it from weeks to days,” said Rao.

Mastercard performed an internal survey to see what users thought of the AI-Workbench. Their internal data scientists and developers noted that it was a “great platform to experiment.” The internal team was happy with how easy it was to consume data from the OpenShift-based AI-Workbench because the platform already supported the necessary libraries and tools.

To learn more about OpenShift as a platform for your AI workloads, check out the [guide to advancing your business with AI/ML](https://www.redhat.com/en/resources/advance-business-with-ai-ml-ebook).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)