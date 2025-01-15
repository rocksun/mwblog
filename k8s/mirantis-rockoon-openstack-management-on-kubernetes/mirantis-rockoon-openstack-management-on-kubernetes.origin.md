# Mirantis Rockoon: OpenStack Management on Kubernetes
![Featued image for: Mirantis Rockoon: OpenStack Management on Kubernetes](https://cdn.thenewstack.io/media/2025/01/18b25618-ardian-pranomo-x2vxvweo7w-unsplash-1024x765.jpg)
[Mirantis](https://www.mirantis.com/) has launched [Rockoon](https://github.com/Mirantis/rockoon), an innovative open source project that provides a [Kubernetes](https://thenewstack.io/Kubernetes/) controller for life cycle management for [OpenStack](https://www.openstack.org/) clouds. While new in this open source guise, Mirantis has [been using](https://thenewstack.io/mirantis-unveils-next-generation-kubernetes-platform-with-mke-4-release/) and deploying the program for its customers for years.
Believe it or not, Rockoon is a real word for “rocket + balloon.” Instead of launching rockets into space, Mirantis Rockoon, however, is all about providing a Kubernetes controller for simplified OpenStack management. It does this by providing a high-level abstraction layer using [OpenStack Helm](https://wiki.openstack.org/wiki/Openstack-helm) charts. In addition, it provides a stable, versioned abstraction over OpenStack Helm application programming interfaces (API).

The program also provides a [unified API](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/) for managing OpenStack cluster configurations and lifecycle operations while supporting self-healing processes and facilitating smarter upgrades. With Rocktoon, you can simplify complex operational routines, allowing administrators to manage OpenStack as a unified whole rather than a collection of disparate services.

Together, they provide a unified API for managing OpenStack cluster configurations and lifecycle operations, abstract complex networking tasks, support self-healing processes, and facilitate smarter upgrades and orchestration.

There’s a large audience for Rockoon. [Thierry Carrez](https://www.linkedin.com/in/thierry-carrez-652662a/?originalSubdomain=fr), general manager of the [OpenInfra Foundation](https://openinfra.dev/), explained in an e-mail interview, “More than two-thirds of OpenStack deployments leverage the integration of OpenStack and Kubernetes. Tens of millions of cores are globally implementing that open infrastructure blueprint. Mirantis is opening up Rockoon to the community tracks with the company’s longstanding commitment to both projects. Releasing Rockoon under an open source license makes sense.”

## The Missing Ingredient for OpenStack
Why would you want to do this? [Randy Bias](https://www.linkedin.com/in/randybias/), Mirantis’s vice president of open source strategy and technology, explained, “We are thrilled to provide one of the key missing components in the OpenStack ecosystem: advanced life cycle management of the OpenStack running on Kubernetes, empowered by Rockoon. Rockoon is battle-tested with some of the largest Mirantis customers running it for half a decade or more in production and at scale. Mirantis is reinforcing its role as an innovator in the OpenStack ecosystem by releasing this key piece of code that solves one of OpenStack’s biggest challenges. It’s 100% free forever and available today.”

In another e-mail interview, [Artem Andreev](https://www.linkedin.com/in/arandreev/?originalSubdomain=de), Mirantis staff product manager, added Rockoon is a significant step in our commitment to the open source community. Following our pledge at KubeCon in Paris last year to double down on open source, Rockoon brings the benefits of [Mirantis OpenStack for Kubernetes (MOSK)](https://www.mirantis.com/software/mirantis-openstack-for-kubernetes/) to everyone.”

Andreev added, “In light of[ recent market shifts](https://thenewstack.io/vmware-users-adjust-to-broadcom-subscription-licensing/), there is renewed interest in open-source alternatives to VMware, in particular OpenStack. Mirantis recognizes the growing demand for accessible and efficient tools to manage OpenStack environments, and we believe that MOSK and Rockoon answer that call.”

That said, while Rockoon is optimized for Mirantis’ [K0s](https://k0sproject.io/) distribution, it’s compatible with other Kubernetes environments. Mirantis ensures stability through automated testing for every commit to the repository.

Sounds interesting? Mirantis has made it easy for developers and enterprises to begin using Rockoon. Simply visit the [Rockoon GitHub repository](https://github.com/Mirantis/rockoon). Then, use the provided deployment script for automated setup on something as lightweight as a laptop or virtual machine (VM) to deploy it so you can see if it will work for you.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)