# Clean Container Images: A Supply Chain Security Revolution
![Featued image for: Clean Container Images: A Supply Chain Security Revolution](https://cdn.thenewstack.io/media/2025/02/55eba463-cve-visualization-visual-1-1024x684.png)
[Supply chain security](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/) startup [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) has spent the last four-plus years trying to change the way developers and enterprises look at and use [container images](https://thenewstack.io/introduction-to-containers/) and the [open source components](https://thenewstack.io/open-source-in-2025-strap-in-disruption-straight-ahead/) that go inside.
Typically, these images come with any number of [CVEs](https://www.cve.org/) in them, forcing developers to hunt them down and creating a time-consuming process needed to remediate and manage them. Chainguard’s founders felt there was a better way of building a container — essentially, by starting with clean image and building up from there.

The result has been a growing roster of [Chainguard Images](https://thenewstack.io/chainguard-secure-software-supply-chain-images-arrive/), open source components that come without CVEs that organizations can choose from, an app store of sorts. The idea has gotten the attention of the investment crowd, with the Kirkland, Washington-based company raising more than $250 million from four rounds, [including $140 million last summer](https://www.prnewswire.com/news-releases/software-security-leader-chainguard-raises-140-million-in-series-c-funding-to-secure-the-next-frontier-of-ai-workloads-302206133.html) that boosted its valuation to more than $1.12 billion.

Now Chainguard is making it easier for its customers — in 2024, it saw a five-fold year-over-year growth in its customer base — to see the benefits they’re deriving from using vendor’s technology.

## Visualizing the CVEs
The company this week [announced the general availability](https://www.chainguard.dev/unchained/chainguard-cve-visualizations-now-generally-available) of [CVE Visualizations](https://edu.chainguard.dev/chainguard/chainguard-images/features/cve_visualizations/), the latest capability in the [Chainguard Console](https://console.chainguard.dev/auth/login), a single place to get information on everything from security to product updates. With the new feature, organizations can better quantify the engineering, security, and financial benefits that come with using Chainguard’s CVE-free images.

The capability includes seeing the number of CVEs Chainguard remediated in the images over time (and the amount of time engineering teams saved by not having to deal with them) and how Chainguard’s CVE accumulation rate compares with other open source options. In addition, the CVE Visualizations are integrated in the Chainguard Directory, enabling any developer to evaluate and compare container images

![](https://cdn.thenewstack.io/media/2025/02/6da53a25-cve-visualization-python-compare.png)
CVE Visualization Python compare

![](https://cdn.thenewstack.io/media/2025/02/97d26349-cve-visualization-resolved-cves.png)
CVE Visualization Resolved CVEs

Chainguard executives come to potential customers with tables and graphs showing how their CVE-clean images stack up with what the enterprise is using at the time and how it will benefit by going with Chainguard, according to [Julian Dunn](https://www.linkedin.com/in/julian/), senior director of product management at Chainguard. Now, customers have a personalized report showing how those benefits have accumulated in the months and years they have been using the Chainguard images, a good reminder of why they made the change in the first place.

“Six months down the road, they’ve forgotten the plot, or their bosses have forgotten,” Dunn told The New Stack. “They say, ‘What has changed’ or ‘What have you done for me lately? We signed this contract six months ago. How has it actually delivered value?’ Having these sorts of temporal elements of how many [CVEs] we remediated over time helps folks inside those customers who made that purchase — or when they’re considering expanding to other business units — educate themselves have timely, up-to-date information that’s personalized.”

They can see the amount of work they’ve avoided since signing up with Chainguard and how much it would have cost per CVE to remediate, he said. Customers can tie the service they’re getting from the vendor to time and cost savings that come with their engineers not having to do the work themselves.

## Software in the Blood
The four founders of Chainguard came with years of experience in the software world, giving them a first-hand look at how creating container images could be done better. CEO [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) and CTO [Matt Moore](https://www.linkedin.com/in/mattmoor/) made software engineering stops at [Google](https://cloud.google.com/?utm_content=inline+mention) and [Microsoft](https://www.microsoft.com/en-us/) — with Moore also landing for a while at [VMware](https://www.vmware.com/) — and Chief Product Officer [Kim Lewandowski](https://www.linkedin.com/in/kimsterv/details/experience/) also did time with Google. Similarly, Distinguished Engineer [Ville Aikas](https://www.linkedin.com/in/villeaikas/) has Google and VMware on his resume.

Dunn came to Chainguard 10 months ago, after product management stints at places like [GitHub](https://github.com/), [PagerDuty](https://www.pagerduty.com/), and [Chef](https://www.chef.io/). His background was in software, but he was intrigued by what Chainguard was doing, offering organizations container images with no CVEs. That’s not the way the developer world has worked.

## A New Direction
Chainguard saw it another way. There have been so many CVEs in container images not because there were vulnerabilities in the primary package — [Python](https://thenewstack.io/python-crowned-2024s-programming-king-driven-by-ai-ml/), for example — but because they were built atop full operating systems that brought CVEs with them. In addition, the way containers have been built comes from how servers were built and managed: Very expensive machines loaded with all the software for the multiple purposes the system was used for.

In the world of containers, which tend to be purpose-built for one task. A Python container runs one service, so it doesn’t need everything else around it, Dunn said. Taking a full image and then trying to remove unnecessary and low-quality components is tricky and can lead to breaking Python.

Chainguard takes another direction: With Python, what is the minimum level of dependencies it needs to run. There’s the [C library](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) and an associated dependency chain.

“We’ve done all that dependency mapping just once,” he said. “Then what we’re going to do is to build a container with nothing. Instead of starting with something and removing components from it, we’re going to start with an empty container and just say, ‘Starting from Python, what’s the list of all the minimal things you need to get in order for that Python interpreter to run?’”

This is also why Chainguard’s containers are smaller than those from upstream open source projects, Dunn said. Underlying all this is [Wolfi](https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux-un-distro-designed-for-securing-the-software-supply-chain), Chainguard’s custom-built Linux distribution — or what they call (un)distribution — that is built with default security for the [supply chain](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/).

The company’s Directory contains almost 1,200 CVE-clean images of varying open source components, with more coming in the future, according to Dunn. Take the image, deploy the application, and then start building. In addition, Chainguard last summer extended its capabilities to [AI workloads and large language models (LLMs)](https://thenewstack.io/chainguard-launches-cpu-gpu-containers-for-ai-frameworks/), making building those applications more secure.

## Why Live With Vulnerabilities?
Developers just got used to the fact that there were going to be vulnerabilities in their images. Dunn said it didn’t make sense, comparing it with the idea of food shopping in a supermarket without the Department of Agriculture around to ensure the food was safe. If the food buyer in this world had the mindset of developers, they’d look at the risk of buying unsafe food as the cost of doing business, he said.

In addition, the ranking of CVEs — some critical that need immediate attention and others less dangerous that can be dealt with later — while helpful, still creates and leaves flaws in the attack surface. Bad actors may consider lower-priority vulnerabilities safer ways to get into a system.

“Chainguard just changes the game,” he said. “Why is it acceptable that any image — why is it acceptable for any environment in which you’re running and building software — has any vulnerabilities?” Dunn asked. “And why are we saying, ‘We’re going to only eliminate the worst kind of material diseases in our food and all these other ones that don’t cause a horrible effect … we’re not going to worry about that.

“In the physical world, we would not accept that, so why do we accept it in the software world?”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)