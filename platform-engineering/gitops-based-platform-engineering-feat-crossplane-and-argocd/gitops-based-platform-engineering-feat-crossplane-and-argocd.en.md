If you think about it for a minute, once in a lifetime there will be a major invention that profoundly impacts the way we do things. Till late 1990s we all used to shop at physical stores and then internet happened which brought in e-commerce. Now with the AI phenomenon, the way we shop is changing again. Every major innovation brings in little process improvements, give us choice.

We have been provisioning infrastructure since the advent of internet. Firstly, there used to be physical hardware which you procure and set it up manually and run software on it. Then came cloud which brought in IaC tools like Terraform, CF etc. This is an improvement on the existing process. You can quickly setup infrastructure as you need instead of doing clickOps but also have a lot of drawbacks like configuration drift over time, managing statefiles etc. But then Kubernetes happened…

The more and more adoption of Kubernetes led to a plethora of new cloud native tools which offers a little process improvement on the existing tools and applications. Crossplane is one such tool which offers a better way of infra creation and management. It prevents configuration drift and allows us to create abstractions for self service. This helps us shift left so developers can provision the infra they need and manage it as required. Here is a X post contrasting differences between Crossplane and Terraform

> <https://x.com/ianmiell/status/1788973776996028813>

In this article let’s quickly go through the basic terms used in Crossplane. There are 5 main components

[Composite Resource(XR)](https://docs.crossplane.io/latest/composition/composite-resources/) - It can be defined as a bunch of different resources packaged as one resource. If you need IAM Role, Policy and S3 bucket for your application to access that bucket then all three resources can be combined to make one XR.

[Composite Resource Definition(XRD)](https://docs.crossplane.io/latest/composition/composite-resource-definitions/) - Composite resource definitions (`XRDs`) define the schema for a custom API. Users create composite resources (`XRs`) using the API schema defined by an XRD.

[Compositions](https://docs.crossplane.io/latest/composition/compositions/) - Compositions have the actual definition of the things to create that XR is requesting for. It holds all the logic.

[Providers](https://docs.crossplane.io/latest/packages/providers/) - Crossplane providers are extensions that enable Crossplane to manage infrastructure and resources on external services, like cloud providers. Think of them as the bridge that connects your Kubernetes cluster to a third-party API.

[Functions](https://docs.crossplane.io/latest/packages/functions/) - Functions enable you to dynamically populate resources based on the XR. You can use different *composition functions* to configure what Crossplane does when someone creates or updates a [composite resource (XR)](https://docs.crossplane.io/latest/composition/composite-resources/).

Here is an image from Crossplane docs to better understand how these work

[![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757537067976/2133e350-02ca-4e0c-bd8b-98e8c3c766b7.png?auto=compress,format&format=webp)](https://docs.crossplane.io/latest/composition/composite-resources/)

The reason to use Crossplane with ArgoCD in a gitops based approach is that Git manages the commit history so you can quickly refer the changes that are being made to any crossplane resource. ArgoCD can help you visualize the infrastructure you are creating and also allows you to setup sync waves etc. There are lot more benefits than what is stated here but you can catch my drift.

## [Permalink](#heading-crossplane-in-action "Permalink")Crossplane in action

> Here is the [github repo](https://github.com/HighonAces/crossplane-argocd#) used in this blog

Let’s take a scenario where a dev team needs new EKS cluster for some testing. Usually these requests go through a Jira for DevOps team who create a cluster based on their specification and gives it to them. This comes with a lot of friction because dev team do not want to ask ops team to shutdown the cluster for weekend because they have to raise another jira again on monday and have to wait till the cluster is created again. What if we let dev team create the cluster as required but do not want to deal with HCL or low level components like VPC, Subnet etc.

Here are the building blocks of EKS cluster as platform for developers.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757536041748/b80cc3df-4700-4e16-b313-fe2175cd2d9c.png?auto=compress,format&format=webp)

Firstly the dev team have to create the required networking to deploy EKS cluster on top of it. So they will push the eksnetworking XR file in the given Github repository

Using this XR, dev team has ability to configure region, CIDR range, number of subnets etc. Yet it is very guardrailed in terms of what parameters are required and how they have to go in etc. This is controlled by Composite Resource Definition(XRD). You can see the required sections and enum below.

Now The composition is where all the required resources will be configured. It uses one or more functions to fetch the values given in XR to create the resources. KCL is popular language of choice but you can use go-template or Python as well. Here is the [composition](https://gist.github.com/HighonAces/46e348b57481800f854605d6e3cc7a1a) used.

Remember, XRD and Composition must always be owned by ops team who dictates how an XR can be created and what resources will be created as a part of it. Here is a quick snapshot of created resources from ArgoCD

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757537977592/a878a327-edec-4974-91e0-6f6308f7d3d4.png?auto=compress,format&format=webp)

This gives an overall idea about the resources that are being created and the overall health of your XR. Now you have your networking now to create EKS controlplane. It also follows a similar pattern of creating XRD and Composition. Here is the ekscluster XR for reference

```
apiVersion: srujanpakanati.com/v1alpha1
kind: EKSCluster
metadata:
  name: my-eks-cluster
  namespace: default
spec:
  parameters:
    clusterName: my-eks-cluster
    region: us-east-2
    kubernetesVersion: "1.33"
    accessList:
      - name: developer-role
        roleARN: "arn:aws:iam::xxxxxxxxx:role/eks-dev-role-to-test-crossplane" 
        policies:
          - "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
          - "arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
    addons:
      - name: vpc-cni
        version: "v1.20.1-eksbuild.3"
      - name: coredns
        version: "v1.12.3-eksbuild.1"
      - name: kube-proxy
        version: "v1.33.3-eksbuild.6"
    vpcId: "vpc-07ddbab7b7c6a6fef" 
    subnetIds:
      - "subnet-0c7420944a320ddff" 
      - "subnet-095925a4561365bf5"
  crossplane:
    compositionSelector:
      matchLabels:
        provider: aws
        workload: ekscluster

```

Here we can see the components getting created in real time in ArgoCD

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757618940319/7143a6ba-4124-43f3-a4bb-2184ecc6fe48.png?auto=compress,format&format=webp)

Once the controlplane gets created, we can go ahead with NodeGroup creation. Here is my nodegroup XR

```
apiVersion: srujanpakanati.com/v1alpha1
kind: EKSNodeGroup
metadata:
  name: my-nodegroup
  namespace: default
spec:
  parameters:
    clusterName: cluster-my-eks-cluster 
    region: us-east-2
    nodeGroupName: my-managed-nodes
    instanceTypes:
      - "t3.medium"
    scalingConfig:
      minSize: 1
      maxSize: 3
      desiredSize: 2
    subnetIds: 
      - subnet-0c7420944a320ddff
  crossplane:
    compositionSelector:
      matchLabels:
        provider: aws
        workload: eksnodegroup

```

Here is the same XR in ArgoCD.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757621184804/0a215c73-c3d2-4ca6-8e86-acf0f99d2d6b.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757621834599/9a5cfae0-0999-41fd-ab1a-3d433e2fbeb2.png?auto=compress,format&format=webp)

If we take step back here a minute and see what we have created, not only created a cluster and nodegroup. We also created a template in which as many number of clusters can be created as required. 0→1 is done now 1→n is easy. Its not just new controlplanes, you can add nodegroups to the existing EKS clusters. This way we can create self-serving platforms for developer teams so that you prevent the infra related bottlenecks.

Crossplane and ArgoCD are quintessential tools in Cloud Native era. Teams iterate in cycles, these tools offer a significant improvement in that cycle pushing developer experience and cost efficiency further. The returns will be multi-fold and the wildest thing is that these tools are open-source. If your workloads runs on Kubernetes then it is time to adopt appropriate tools for the job.