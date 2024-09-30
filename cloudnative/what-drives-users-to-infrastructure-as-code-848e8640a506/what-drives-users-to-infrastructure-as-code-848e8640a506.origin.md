# What drives users to Infrastructure as Code?
In previous posts in my [Infrastructure as Code and Declarative Configuration series](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836), I wrote about both the [benefits of Infrastructure as Code](https://medium.com/@bgrant0607/reflections-on-declarative-configuration-c2fe1c1e50d5) and [some of the challenges](/why-are-so-many-companies-working-to-improve-infrastructure-as-code-6c29bacdd1e1). Why do cloud and Kubernetes users adopt Infrastructure as Code (IaC) in the first place? What are the pros and cons relative to other common user interface surfaces, such as Graphical User Interfaces (GUIs) and Command-Line Interfaces (CLIs)?

# GUIs
GUIs are ubiquitous interfaces to services. They are quite popular, especially among non-developer users, but even with many application developers.

Here’s an example form:

GUIs can provide a simpler experience, especially for new users who aren’t familiar with all of a product’s features and terminology. A lot of UX design focuses on GUIs.

Features of GUIs that users like include:

- Step-by-step guidance
- Progressive disclosure
- Early validation
- Autocompletion and default values
- Contextual help / documentation
- Error resolution assistance
- Navigational aids
- Organization of complex information
- Dynamic, interactive updates
- Graphical representations of data
Why, then, do users shift from using GUIs to IaC? One reason is a lack of important features and capabilities, such as:

- Reproducibility / repeatability — the ability to create similar variants of a configuration
- Provisioning resources from multiple services
- Review and approval
- Organizational policy enforcement
- Versioning and undo
- Commenting / notes
- Record of who changed what, when, and why
- Sharing / collaboration
Those capabilities are achievable through IaC.

Note that many of those features, such as undo, commenting, sharing, and details of who changed what, are available through GUIs of other products. The [UX of cloud GUIs isn’t nearly as good as it could be](https://medium.com/@bgrant0607/why-does-cloud-ux-lag-behind-other-software-products-3a30555b5a7c).

It’s not uncommon that even relatively common use cases are not explicitly supported by cloud GUIs. Instead, lengthy documentation tutorials and solutions may require users to visit several separate GUI pages in order to accomplish their task.

Here’s a [simple example](https://cloud.google.com/iap/docs/load-balancer-howto) that requires navigating to five distinct pages to complete the task. I’m showing Google Cloud examples just because I’m most familiar with it. Other providers (e.g., [AWS](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html), [Azure](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal)) don’t look simpler.

# CLIs
Ok, what about command-line interfaces? CLIs can be efficient for experienced users who are familiar with a provider’s services, resources, features, terminology, and so on, and who perform similar tasks often, and can execute similar commands using scripts and/or their shell history.

Here’s what the above example looks like using the gcloud CLI. It looks longer mostly because I abbreviated the GUI example above to just show page transitions.

`gcloud compute networks subnets update SUBNET \`
--network=NETWORK \
--stack-type=IPV4_ONLY \
--range=10.1.2.0/24 \
--region=REGION
gcloud compute instance-templates create TEMPLATE_NAME \
--region=REGION \
--network=NETWORK \
--subnet=SUBNET \
--stack-type=IPV4_ONLY \
--tags=allow-health-check \
--image-family=debian-10 \
--image-project=debian-cloud \
--metadata=startup-script='#! /bin/bash
apt-get update
apt-get install apache2 -y
a2ensite default-ssl
a2enmod ssl
vm_hostname="$(curl -H "Metadata-Flavor:Google" \
http://metadata.google.internal/computeMetadata/v1/instance/name)"
echo "Page served from: $vm_hostname" | \
tee /var/www/html/index.html
systemctl restart apache2'
gcloud compute instance-groups managed create lb-backend-example \
--template=TEMPLATE_NAME --size=2 --zone=ZONE_A
gcloud compute instance-groups set-named-ports lb-backend-example \
--named-ports http:80 \
--zone ZONE_A
gcloud compute firewall-rules create fw-allow-health-check \
--network=NETWORK \
--action=allow \
--direction=ingress \
--source-ranges=130.211.0.0/22,35.191.0.0/16 \
--target-tags=allow-health-check \
--rules=tcp:80
gcloud compute addresses create lb-ipv4-1 \
--ip-version=IPV4 \
--network-tier=PREMIUM \
--global
gcloud compute addresses describe lb-ipv4-1 \
--format="get(address)" \
--global
gcloud compute health-checks create http http-basic-check \
--port 80
gcloud compute backend-services create web-backend-service \
--load-balancing-scheme=EXTERNAL \
--protocol=HTTP \
--port-name=http \
--health-checks=http-basic-check \
--global
gcloud beta compute backend-services add-backend web-backend-service \
--instance-group=lb-backend-example \
--instance-group-zone=ZONE_A \
--global
gcloud beta compute url-maps create web-map-https \
--default-service web-backend-service
gcloud compute target-https-proxies create https-lb-proxy \
--url-map=web-map-https \
--ssl-certificates=www-ssl-cert
gcloud compute forwarding-rules create https-content-rule \
--load-balancing-scheme=EXTERNAL \
--network-tier=PREMIUM \
--address=lb-ipv4-1 \
--global \
--target-https-proxy=https-lb-proxy \
--ports=443
gcloud compute ssl-policies create my-ssl-policy \
--profile MODERN \
--min-tls-version 1.0
gcloud compute target-https-proxies update https-lb-proxy \
--ssl-policy my-ssl-policy
gcloud compute backend-services update BACKEND_SERVICE_NAME \
--iap=enabled,oauth2-client-id=ID,oauth2-client-secret=SECRET \
--global
Obviously this “simple” example was pretty involved. Interactive resource creation probably isn’t the best use case for a CLI. Infrastructure resources tend to contain large numbers of attributes, and scenarios like this one require quite a few resources. Also, this probably isn’t something you’d do every day, so the exact sequence of commands would probably be hard to remember and would need to be recorded in a script or notebook.

Properties of CLIs that users like include:

- Repeatable
- Less context switching and navigation
- Incremental and iterative
- Can process and use the output
- Automate tasks using scripts and notebooks
- Shareable
However, it’s my impression that brittleness of long sequences of complex commands drives users towards IaC:

- Different commands are often needed for different initial states. In particular, different commands are usually needed for updates than creation. Also, CLI commands are not necessarily idempotent.
- Error handling is harder than in a general-purpose programming language
- It’s not always possible to validate commands without executing them (e.g., via dry run)
IaC is more robust because it automatically figures out what actions to take based on the initial state, and it’s generally safe to apply again in the case of an ephemeral failure, such as due to API quota exhaustion, or race condition.

# IaC
So there are good reasons why users adopt IaC. It provides some specific capabilities and solves common problems.

However, while there’s some syntax autocompletion in IDEs, there has historically been less assistance with authoring IaC templates/code from scratch than with GUIs and CLIs. A lot of the focus has been on [reusing existing templates](https://medium.com/@bgrant0607/what-is-it-with-template-catalogs-7637c24d5200).

Of course, there have been exceptions. Azure’s portal has the ability to [export an ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal), which seems pretty useful.

This situation seems to be improving with some of the [newer IaC products](/infrastructure-as-code-landscape-overview-2024-a066124e5989). For example, Firefly can [create IaC for existing resources](https://www.firefly.ai/use-cases/iac-adoption).

Composition of templates/modules appears to be an area that multiple categories of products are tackling, such as the diagram-based interfaces, like Brainboard and Massdriver, and the Infrastructure from Code products, like [Nitric](https://thenewstack.io/maximizing-terraform-modules-for-platform-engineering/).

As for assistance with authoring the modules themselves, there’s [Structura](https://www.structura.io/), which kind of reminds me of [Scratch](https://scratch.mit.edu/projects/editor/?tutorial=getStarted), which should at least help get the syntax correct. And, of course, the new bleeding-edge AI products, which currently don’t produce correct IaC consistently.

IaC has a significant learning curve and comes with [complexity and toil](https://medium.com/itnext/complexity-and-toil-in-infrastructure-as-code-6ca9a6d2af37). It seems to me that we had to give up a lot in order to adopt IaC.

We’re also bumping into the limits of the paradigm, which was designed around a [human-driven, artisanal process](/infrastructure-as-code-is-artisanal-automation-2b6b7545c100). But [after 30 years](https://medium.com/@bgrant0607/infrastructure-as-code-reminds-me-of-make-run-all-15eb6628f306), we’re due for a paradigm shift.

What do you think? Would you prefer a GUI or CLI over IaC if it provided equivalent capabilities? Do any of the new GUI-centric IaC-based products appeal to you? What would you want from a new paradigm for infrastructure management? Have you used any interesting alternatives to IaC?

Feel free to reply here, or send me a message on [LinkedIn](https://www.linkedin.com/in/bgrant0607/) or [X/Twitter](https://x.com/bgrant0607), where I plan to crosspost this.

If you found this interesting, you may be interested in other posts in my [Infrastructure as Code and Declarative Configuration series](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836).