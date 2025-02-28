# Secretly Swapping Clouds While Everybody Is Watching
![Featued image for: Secretly Swapping Clouds While Everybody Is Watching](https://cdn.thenewstack.io/media/2025/02/cf524aff-clouds1-1024x576.jpg)
Earlier this year, our team began secretly working on a new bare metal product called [Colony](https://konstruct.io/colony). At the time our company was called Kubefirst, a brand shared with our popular [Kubefirst platform](https://thenewstack.io/taming-the-cncf-landscape-with-kubefirst/). With the addition of the Colony product line, it was time to rebrand our company to Konstruct.

Since the motivation behind the rebrand was being developed in secret, it gave us a neat opportunity to build out our new company in secret as well. As an open source company, building a new organization in secret was a really fun challenge for our engineering team.

In the end, we were caught by a single member of our community only a few days before [our big announcement](https://blog.konstruct.io/introducing-konstruct/). The execution of our new brand and company was a huge success, and we wanted to share how we did it for your next stealth rebrand.

**Picking a Simpler Cloud to Call Home**
For the last five years, we’ve been running our production environment on Kubefirst in the AWS cloud. [AWS](https://aws.amazon.com/?utm_content=inline+mention) was the first cloud that our Kubefirst platform supported. In fact, Kubefirst supported Kubernetes on AWS before Elastic Kubernetes Service (EKS) even existed. AWS has been incredibly dependable for us, and it was a great home to hang our YAML for a half-decade.

Since we began growing an engineering team two years ago, our platform has expanded to include support for GCP, Azure, Civo, Akamai, DigitalOcean, Vultr and bare metal. This produced a unique opportunity to pick any cloud to host our rebranded Konstruct ecosystem. We had been using the Civo cloud as our development environment for the past two years and have loved the simplicity and speed of its [cloud native approach](https://thenewstack.io/the-rise-of-the-cloud-native-cloud/). We decided to make Civo our new permanent production home at long last, and it was time to set up shop.

## Secret Moving Checklist
- Git organization housing our
[open and closed source codebases](https://thenewstack.io/build-an-open-source-kubernetes-gitops-platform-part-1/) - Publicly hosted CLI binaries
- Public Helm charts
- Public container images
- Public homebrew tap
- DNS (was AWS Route53, migrated to Cloudflare)
- Our internal management (users, teams, permissions and git repositories)
- Our CI and delivery ecosystem (Argo Workflows + GitHub Actions)
- Our cluster control plane (Kubefirst + Crossplane + Atlantis + Argo CD)
- Self-hosted marketing site (React), docs site (Docusaurus) and blog (Ghost)
## Preparing the Bot Accounts
We set up our [konstruct.io](https://konstruct.io/) domain in Cloudflare with a new bot account for our automation. We created an API key for the new platform to have its DNS records automatically managed by `external-dns`
.

Next, we created a new GitHub bot user account to create and manage our new [konstruct.io GitHub organization](https://github.com/konstructio) and a Personal Access Token for the platform’s Infrastructure as Code (IaC) layer. If it weren’t for the stealth operation, we could have merely renamed our GitHub organization to automatically transition the repositories. In a secret operation, however, your private repos should move before your public repos do, so a full organization rename becomes less optimal.

The last bot account we created was a new Civo cloud account, from which we generated an API token to allow the platform to manage our cloud resources.

**Building Day**
There’s something so refreshing about building out your new management account. Never a single human click. Take a deep breath. Can you smell the sterile air in here?

With our new set of keys exported we ran `kubefirst civo create`
to build our kubefirst platform, mint condition, in a very different cloud experience. It used our favorite new DNS provider, with a freshly generated `gitops`
repository built for us and placed in our new GitHub organization.

Next, we needed to create new clusters to represent our preproduction and production environments. For the clusters, we used the Kubefirst Pro user interface to create them. We copied the environments directory from our old `gitops`
repo into our new `gitops`
repo, and Argo CD ensured that all the Helm charts were delivered safely to their new home.

In a scenario where you’re migrating cloud providers, DNS providers and git organizations, you will need to update some old values as you’re transferring repository content into its new home. Be mindful of any references to your old git organization or your old DNS hostnames when copying these settings in.

While making these changes, Argo CD is a great assessment space for the state and health of your cluster. Argo CD will often tell you the problem by surfacing the error through Events in the UI. In our case, these were mostly just some secrets from the old environment that we needed to replicate in the new environment.

![](https://cdn.thenewstack.io/media/2025/02/49d5f9f8-image2.png)
Image 1

One by one we cleared these issues and the platform shifted to that Argo CD heart we learn to love.

## Migrating Charts Across Chartmuseum Instances
We had a tricky nuance to consider with our chart hosting. We hosted our charts in ChartMuseum, so our new instance started out empty. Anything new would publish to it automatically, but we wanted to backfill it with all the existing Kubefirst charts so folks could fully switch to our new chart repository when we were ready.

If you know anything about ChartMuseum, you might think you can just copy the buckets over and update the index.yaml, but it’s more complex than that. There was nothing particularly great online for this migration, so we wrote a new open source utility to help folks do this. If you ever need to back up or migrate a ChartMuseum, take our [charts-mirror](https://github.com/konstructio/charts-mirror) repo for a spin. It’ll let you move charts between ChartMuseuminstances, and let you back up and restore charts between ChartMuseum and GitHub for disaster recovery purposes.

## Migrating IaC
Kubefirst manages our clouds, users, Vault configurations and git configurations using IaC, and for [everything else we use GitOps](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/). All four of these directories are created with default settings when you create a Kubefirst platform, but we wanted to migrate our original Kubefirst content instead.

**Cloud:**The cloud IaC didn’t need any adjustment. We’re in a new cloud, so nothing to move.**Users:**We were able to copy these files right over in a new branch. Our pull request prompted Atlantis to provide a plan that we liked; we added the comment`atlantis apply`
, and boom, our users are in their new home. At this point, invites went out to all of our team about their new git org access, and everyone could use the new platform and log into all of their favorite platform tools in their new cloud. It was all going great.**Vault:**This required no adjustment. The default configurations work great for our team.**GitHub:**This was a tricky one. Let’s talk about it next.
## Migrating GitHub Repos When in Stealth Mode
This was probably the trickiest bit for us to get right. We manage our repos through Atlantis on our old management cluster, and everything was set up on the original `kubefirst`
org where we started.

We wanted to move our repositories to our new `konstructio`
org, but we didn’t want to tip our rebranding cards yet. This meant that for our open source codebase, nothing could change until the last minute.

For all of our closed source repos, we simply copied the files from our old `terraform/github`
folder to our new one. When the pull request was opened, the plan read as if it would create all new repos.

We transferred each of the private repos into the `konstructio`
org, then ran `atlantis import`
for each repo, so its state would be inherited by the new IaC. Then we reran the Atlantis plan to show no changes. Once applied, we were all synced up on the private repos migration.

For our open source repositories, we made new copies of them in the publicly unknown `konstructio`
location, effectively duplicating our existing public repos. This afforded us an opportunity to identify changes as we’d verify our publish and delivery pipelines and ensure everything was ready to build and publish our products from their new home.

This testing introduced our single telling mistake: Homebrew.

## Homebrew Considerations
Homebrew didn’t want to help us keep our secret. By duplicating our public Homebrew repo, we exposed our plans.

Homebrew tap repos are automatically discovered when you create the repo in GitHub. If they’re configured to the new space, they can follow redirects and watch your new public repos as you transfer them.

This was the one detail that showed our hand before the announcement. Some of our new release candidates began showing up before we wanted in the old tap due to GitHub repo forwarding rules. Be extra mindful of your Homebrew configs and repo redirects during a migration if you also maintain a Homebrew tap.

## Migration Day
With our private repos in their new home, we ensured they could build and deliver to the new container registry, chart registry and Kubernetes clusters. We checked Argo CD one final time to verify that all the apps were healthy with no errors. Everything that could be set up before the final batch of repo moves was done, listening on its new domain and healthy.

When it was time for the big shift, we transferred all the remaining git orgs, including all the open source repos, being especially careful with all the clicks surrounding our [1900 GitHub stars](https://github.com/konstructio/kubefirst). If you accidentally make a repo private — or copy instead of transfer the repo — you will unrecoverably lose this important vanity metric.

## Remember to Keep Your SEO Guard Up
One detail that’s easy to get wrong after a domain change is SEO. For as long as your original brand and domain have lived on the internet, Google and others have been deploying SEO robots to read and index relevant content to users. You’ll want to ensure you don’t lose the SEO footprint surrounding your original domain. Here are some ideas that might help if you choose to update.

When changing domains, it’s helpful to change as few words and pages as possible. This is a bad time to introduce new docs or to change blogging technologies if you can avoid it. We did both anyway and lived to tell the tale. Keeping assets and locations the same helps you convince the robots that you’re the same company and still worthy of the SEO reputation that you built on your old domain.

Subscribing to something like Ahrefs for backlinks research can help you find all the links that have broken from your domain shift. It’s important to remedy broken links by updating their original source content if you can, or by adding redirects to your DNShosting configuration when you can’t. Redirects will allow you to send bad links to their new good homes to appease the robots. Our update to Cloudflare DNS made managing redirects very straightforward. Google Search also has some good domain migration tools that may help.

Once you’ve confirmed all traffic has stopped flowing to your original sources and all needed redirects navigate end users to their new home, you can safely tear down the old world and marvel at your cloud native portability.

## Announcing Your Greatness to the World
Congratulations, you made it to your new domain! Now it’s time to invite all of your public users to your new digital home.

Being able to change DNS, git, and cloud providers might be a lot of work for a lot of companies, but it wasn’t hard for Konstruct, because we use Kubefirst.

Kubefirst is agnostic to the cloud, git and DNS providers so you can have the same platform anywhere. How long would it take your organization to change clouds, git orgs or DNS providers? [Check out our overview docs](https://kubefirst-pro.konstruct.io/docs/overview/feature) to learn more about our instant GitOps magic, or [book a demo with me](https://ro.am/johndietz) to get a quick tour today.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)