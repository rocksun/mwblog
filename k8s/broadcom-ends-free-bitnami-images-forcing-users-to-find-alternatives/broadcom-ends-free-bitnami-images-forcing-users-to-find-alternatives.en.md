This week, users of Helm and other cloud native open source projects will have to find other free sources for their pre-compiled production-ready application images and Helm Charts. As of Monday, Broadcom has revamped its image download program, narrowing the [free downloads available](https://github.com/bitnami) in favor of a smaller number of resources mostly available under a commercial license.

Users of many open source applications have been hard hit by the change.

## The Impact on Open Source Application Users

Many administrators, however, have baked the Bitnami into their own automated deployment strategies. For them, work lies ahead to find new images and Helm charts as well as formulate new migration or mirroring strategies to avoid potential disruption.

“For years, Bitnami’s images and Helm charts were the de facto path to running popular apps on [Kubernetes](https://thenewstack.io/kubernetes/). Well-maintained images, sensible defaults, and easy Helm installs. Many teams pinned Bitnami images in deployments, CI pipelines, and internal charts,” [noted a blog post](https://www.prequel.dev/blog-post/bitnami-deprecation) from services provider Prequel.

## The Impact on Open Source Application Users

The biggest risks of the Bitnami deprecation, according to Prequel’s post, are:

* + *Kubernetes ImagePullBackOff on restarts or during  autoscaling,*
  + *stale/unpatched images (CVE drift),*
  + *Time-bomb restarts: Running pods look fine until the next pull (then fail).*
  + *chart drift and subchart dependencies that break upgrades.*

While disruptive to the [Helm community](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/), others are feeling the pinch as well. One Reddit contributor [wondered](https://www.reddit.com/r/kubernetes/comments/1mjx86p/regarding_the_bitnami_situation/) where he could get the latest images for [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), [Postgres](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) and [Redis](https://thenewstack.io/redis-is-open-source-again/).

## CNCF Clarifies Helm Project’s Status

The [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) even issued a [statement](https://www.cncf.io/blog/2025/09/24/cncfs-helm-project-remains-fully-open-source-and-unaffected-by-recent-vendor-deprecations/?ref=dailydev), asserting that the move did not affect Helm itself, in response to user queries.

“Helm is a graduated project that will remain under the CNCF. It continues to be fully open source, Apache 2.0 licensed, and governed by a neutral community,” wrote CNCF CTO [Chris Aniszczyk](https://www.aniszczyk.org/about/) and Helm co-creator [Matt Butcher](https://thenewstack.io/webassembly-and-kubernetes-go-better-together-matt-butcher/), [in a statement](https://www.cncf.io/blog/2025/09/24/cncfs-helm-project-remains-fully-open-source-and-unaffected-by-recent-vendor-deprecations/?ref=dailydev). “Bitnami’s decision to deprecate its public chart and image repositories is entirely separate from the Helm project itself.”

## Broadcom’s New Commercial Model for Bitnami

The [Tanzu Division](https://www.vmware.com/products/app-platform/tanzu) of Broadcom [announced the move in July](https://news.broadcom.com/app-dev/broadcom-introduces-bitnami-secure-images-for-production-ready-containerized-applications), when [unveiling a new service](https://github.com/bitnami/charts/issues/35164) based on the Bitnami repository, called [Bitnami Secure Images](https://www.arrow.com/globalecs/na/vendors/bitnami-secure-images/), which would offer a set of 280 images that have gone through security hardening (SBOM support, CVE patching, enterprise support), and are available commercially (the repository will be managed by [Arrow Electronics](https://www.arrow.com/company)).

As part of the move, the company gradually disables the non-latest [Debian](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/)-based images, shuffling them to the [Bitnami Legacy](https://hub.docker.com/u/bitnamilegacy) archive site.

With a few exceptions, no updates will be made to these older images. The company will still provide a limited subset of free, latest-version images for development use.

Helm charts will still be available on [Docker Hub](http://docker.io/bitnami) as  [OCI artifacts](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/), and will not be updated.

[![Bitnami changes](https://cdn.thenewstack.io/media/2025/09/019753f6-broadcom-bitnami-changes.png)](https://cdn.thenewstack.io/media/2025/09/019753f6-broadcom-bitnami-changes.png)

## How Vendors Are Filling the Void

A number of vendors have quickly jumped in to fill the void: RapidFort [offered its set](https://www.rapidfort.com/blog/bitnami-goes-behind-paywall-rapidforts-curated-near-zero-cve-images-offer-superior-alternative) of “near-zero CVE” curated images. Prequel has published a set of CREs ([Common Reliability Enumerations](https://docs.prequel.dev/cres/commercial)) that detect Bitnami images being pulled into production settings, as part of a paid service.

“The Bitnami disruption represents both a challenge and an opportunity. While the immediate need is to replace Bitnami images to maintain operational continuity, the broader opportunity is to significantly enhance your organization’s security posture through RapidFort’s curated, near-zero CVE container images,” the RapidFort post summarized.

[![screenshot](https://cdn.thenewstack.io/media/2025/09/c561d8bb-68bf3fc32c8101b9b93201e1_bdc994c4.png)](https://cdn.thenewstack.io/media/2025/09/c561d8bb-68bf3fc32c8101b9b93201e1_bdc994c4.png)

Prequel Rules Catalog

## A Brief History of Bitnami

As of earlier this year, Bitnami was serving up as many as [500 million images each month](https://thenewstack.io/the-bitnami-open-source-application-catalog-turns-18/), and [had even ramped up its support for Helm charts](https://github.com/bitnami/charts), scanning for vulnerabilities all the images the Helm chart included.

Bitnami itself was started by in 2007 by Daniel López and Erica Brescia, with the goal of making it easier for developers to deploy open source software across different platforms.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)