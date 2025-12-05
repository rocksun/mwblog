Addressing a long-standing perceived roadblock in enabling systems to span [multiple cloud services](https://thenewstack.io/consider-making-shift-toward-multi-cloud/), [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) and [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) have jointly developed a standard for customers to easily bridge their cloud deployments with [Layer 3](https://thenewstack.io/how-to-decide-between-a-layer-2-or-layer-3-network/) connectivity.

The idea, according to both companies, is to make it easy for their customers with cloud operations in both clouds to network them together in a private network, reducing the burden of maintaining multicloud connectivity, and perhaps even dispelling fears of cloud lock-in.

Such easy connectivity may even spur customers to create more multicloud applications, the [two companies pine in the press material](https://cloud.google.com/blog/products/networking/aws-and-google-cloud-collaborate-on-multicloud-networking).

The open source [Connection Coordinator API](https://github.com/aws/Interconnect) specification is built on [OpenAPI 3.0](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) customized for easily provisioning dedicated bandwidth between two cloud providers. The two cloud giants want other cloud providers to use the API as well.

AWS implemented the spec in [AWS Interconnect – multicloud](https://aws.amazon.com/interconnect/) service, currently in preview. Google Cloud did likewise with [Google Cloud’s Cross-Cloud Interconnect](https://cloud.google.com/hybrid-connectivity#multicloud-networking-connectivity). Both companies pledge to “engage in continuous monitoring to proactively detect and resolve issues,” according to the AWS website.

The private lines between Google and AWS will be built on [MACsec encryption](https://www.juniper.net/documentation/us/en/software/junos/security-services/topics/topic-map/understanding-macsec.html).

## The Problem With Multicloud

To date, customers building systems that span multiple clouds, or want them to run on multiple clouds, had a number of options, each somewhat painful in its own way.

They could connect over public internet to connect between clouds, which offers wildly unpredictable performance in terms of meeting actual [service level agreements (SLAs)](https://thenewstack.io/ignoring-slas-doesnt-pay/) of any sort.

Or they could provision private lines joining the clouds, which is not cheap, and often come with long wait times to provision the circuits themselves.

Or they could build out the private lines themselves, which would require considerable network engineering talent.

## The Connectivity Services Promise Ease

AWS bills its service as fully managed, and offers an interface through the AWS Management Console, command line interface, or the API.

To provision a private network, the users must (in AWS’ words):

* *Specify the target cloud service providers,*
* *Select the destination region on the other side,*
* *Pick the required bandwidth.*

[![](https://cdn.thenewstack.io/media/2025/12/f7c36173-2-simplifying_cross-cloud_connectivity.gif)](https://cdn.thenewstack.io/media/2025/12/f7c36173-2-simplifying_cross-cloud_connectivity.gif)

Source: Google

## What Multicloud Could Enable

According to Google, this service’s simplicity is revolutionary, in that its ease of use will encourage more users to think in terms of what could be done across multiple clouds.

In a blog post, two Google engineers [offered a number of ways](https://cloud.google.com/blog/products/networking/extending-cross-cloud-interconnect-to-aws-and-partners) an organization could leverage multicloud connectivity.

One obvious use is disaster recovery. An application can run on both services, with agentic AI applications or database replicas able to quickly synchronize state. So if one [cloud service goes down](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/), the other can quickly step in.

Or, a user could build a service on AWS that calls a service running on Google Cloud, such as a critical data warehouse hosted in BigQuery.

This could work in the other direction as well. Google Cloud analytics app can pull large datasets from an AWS S3 or an RDS instance.

In each of these cases, the multicloud application would benefit from the improved performance, the engineers write. And not routing this traffic over the public Internet would also be a security benefit.

## Other Ways to Connect

Microsoft Azure was not part of this week’s announcement, though it already offers [Azure ExpressRoute](https://azure.microsoft.com/en-us/products/expressroute) and [Azure Virtual WAN](https://azure.microsoft.com/en-us/products/virtual-wan) as ways to connect Azure with other cloud providers or on-prem facilities.

Other third-party cloud exchange services that could get the job done (via their own data centers) include [Equinix Cloud Exchange](https://www.equinix.com/products/digital-infrastructure-services/equinix-fabric), [CoreSite Open Cloud Exchange,](https://www.coresite.com/cloud-networking/open-cloud-exchange) and [Digital Realty’s Interconnection Fabric](https://www.digitalrealty.com/platform-digital/connectivity).

AWS announced its portion of the news for the kickoff of its annual [AWS Re:Invent conference](https://thenewstack.io/amazon-cto-werner-vogels-predictions-for-2026/), which is being held this week in Las Vegas.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)