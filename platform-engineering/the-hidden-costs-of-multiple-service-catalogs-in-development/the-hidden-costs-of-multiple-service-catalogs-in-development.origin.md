# The Hidden Costs of Multiple Service Catalogs in Development
![Featued image for: The Hidden Costs of Multiple Service Catalogs in Development](https://cdn.thenewstack.io/media/2025/01/05e3f4b1-aleksi-tappura-cjcqksp2wc4-unsplash-1024x678.jpg)
[Aleksi Tappura](https://unsplash.com/@a?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/assorted-books-cJCQKSP2WC4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Developer [tooling](https://thenewstack.io/platform-engineering-it-is-all-about-the-tooling/) increasingly requires service catalogs to scope the data created within them, especially when that tooling relates to every piece of software an organization develops.

Because of this, you often end up with [multiple service catalogs](https://thenewstack.io/30-of-engineer-leads-use-a-spreadsheet-as-a-service-catalog/) for services you’re brought. Multiple catalogs mean valuable time has been diverted from Platform and Software teams and directed towards populating metadata about the things they should be building.

Building a software catalog takes time and the right tools. I’m a software engineer and product manager who builds developer tools and internal portals. So I’ve seen firsthand how often teams are required to manually input data into catalogs that simply weren’t built for that purpose or keep track of the drift from the catalog to production when the tooling doesn’t support such monitoring, and generally the struggles of organizations to keep their various catalogs in sync.

You can easily sleepwalk into having [multiple service catalogs](https://thenewstack.io/simplify-ci-cd-with-a-general-purpose-software-catalog/) in various places with multiple scope levels. This is inefficient, and the catalogs quickly fall out of sync.

It’s a pain.

**Why Does This Happen?**
Software catalogs are increasingly common as a core concept in tools like:

**Data and observability**, like DataDog and New Relic**Incident management**, like[Incident.io](http://incident.io), PagerDuty, and FireHydrant**Developer Experience**, like DX
While important, being a software catalog is not the number one purpose of any of these services, so the quality of the catalog ingestion, visualization, and manipulation is sub-optimal.

Some form of a catalog describing the types of software built by an organization is required to make them work effectively for your organization, but that doesn’t mean that that piece of software is focused on creating a fantastic ingestion mechanism for catalog creation.

Nowadays, most tooling needs a software catalog, so it allows you to build one inside the application. However, that’s rarely the best approach.

## Why Should You Use an IDP To Build One Catalog?
To avoid multiple catalogs, you need a single source of truth — one catalog to rule them all.

There’s a strong case for an [Internal Developer Portal](https://thenewstack.io/internal-developer-portals-should-be-internal-developer-hubs/) (IDP) to be that catalog.

IDPs like Backstage, Port, and Cortex are, at their core, software catalogs. They have some other essential features (scorecards, an automation runner to help with tasks, etc.), but the bread and butter make the service catalog easy to create, configure, and use.

Information from various systems is surfaced to development teams to create a single pane of glass. In building an IDP, organizations inherently create an integration and enrichment point for data about their software, which can then be used as part of a broader and more complex data flow.

Think in terms of data flows:

- Metadata about software goes in, either auto-ingested or manually added.
- Rich objects are created for each piece of software.
- Structural information is defined and included in the catalog’s data model, allowing a software graph to be constructed that shows how each piece of software relates to the others.
That catalog is a rich information store about the software you have built. It’s just a single step away from being the source of truth for that information to other services that require it.

**Enter: Backstage**
Backstage’s built-in advantages as an IDP help it excel at this use case. As an open system, it is more extensible than proprietary software like Port, Cortex, etc.

As the dominant IDP on the market, Backstage garners a lot of support from the third-party service providers you then need to connect to, as well as providers of catalog information (like AWS, who are particularly active plugin developers):

**Plugin ecosystem**. Third parties are constantly building new options to support this use case. These plugins support either the visualization of information in the catalog or, often, more crucially, the ingestion or extraction of catalog data from Backstage.**Auto-ingestion**. Backstage has. For example, AWS recently released a plugin that supports auto-ingestion of resources like S3 buckets and RDS instances, making completing your software catalog much more straightforward than using another service.**Ease of editing**. Backstage comes with a slew of simple enrichment options, leaning heavily on democratically edited yaml files in a format that**Extraction of data**. The Backstage Catalog API and plugin ecosystem make getting data out of Backstage easy when you’re ready to connect to a third-party system.
**How To Use the Backstage Catalog as a Source of Truth**
Let’s take a look at some examples of how this can be done with examples from incident management, data visualization, and developer experience:

- DataDog
[Incident.io](http://incident.io)- DX
**DataDog**
**Using catalog-info.yaml files**
The core of the Backstage software catalog is a series of yaml files stored alongside code in your source code management (SCM) tool of choice (Backstage supports them all). These are often simply referred to as `catalog-info.yaml`
files. They’re just service metadata and reference keys to other services.

DataDog maintains its ingestion mechanism that uses this catalog-info.yaml files to ingest Catalog information. The integration constantly scans repositories in your SCM for Backstage YAML files named `service.datadog.yaml`
and `catalog-info.yaml`
— which you create when you add your service to the Backstage Software Catalog. The code snippet below shows an example of catalog-info.yaml.

You’ll need to enable the[ GitHub integration](https://docs.datadoghq.com/integrations/github/) for this example

**Using DataDogs API**
You can also POST Backstage YAML files to the Datadog API. This allows you to programmatically send Backstage service definitions that may not exist in your GitHub repositories. The [Backstage Catalog API](https://www.datadoghq.com/blog/service-catalog-backstage-yaml/) can respond with your whole Catalog (or just a subset of it), so syncing the two is possible using this route.

[Incident.io](http://incident.io) maintains various ways to connect its internal software catalog to sources of truth.
**Using catalog-info.yaml files**
[Incident.io](http://incident.io) works similarly via their `catalog-importer`
.
The `catalog-importer`
is a little more involved, so it’s worth looking at.

The importer can pull data from various sources, “catering for all the ways people normally store their catalog data,” as they so delightfully put it.

One option is[ GitHub](https://github.com/incident-io/catalog-importer/blob/master/docs/sources.md#github). This works much the same way as the DataDog ingestion mechanism outlined above.

**Using the Catalog API**
Another option is to read Catalog information directly from Backstage via the Backstage Catalog API. Essentially, This makes a[ GET /entities](https://backstage.io/docs/features/software-catalog/software-catalog-api/#get-entities) call to your Catalog and retrieves information directly. You can filter that as you see fit to ensure you only extract the subset of data that’s relevant for[ Incident.io](http://incident.io).

**DX**
DX takes a different approach. They’ve built a complete Backstage backend plugin to extract data from Backstage.

**Using a Backstage backend plugin**
The DX Backstage backend plugin sets up jobs within Backstage to sync the DX catalog

Those jobs call the DX API to send catalog information.

As this can be a lot of data (I routinely see Backstage Catalogs with 100-200k entities), you should probably use the optional params for filtering. You can set these in your app config.

123 |
# app-config.yamldx: catalogSyncAllowedKinds: [API, Component, User, Group] |
You can also control the sync schedulenot to spam your Catalog. Again, this is just a bit of config configuration-config.
12345 |
# app-config.yamldx: schedule: frequency: minutes: 45 |
**If You Need a Catalog, Get a Catalog. **
We’ve focused largely on Backstage, but the core message here is that a singular catalog is preferable to having a multitude of catalogs, each offering a different source of truth. Suppose you must pick one piece of software to be the definitive catalog. In that case, you should select a piece of software that is intrinsically good at being a software catalog, not a tool that secondarily contains a catalog.

Internal Developer Portals excel in this regard. Be it Backstage, Port, Cortex, Rely, or any other IDP, it is the sane choice in a world of development tooling increasingly based on structured software catalogs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)