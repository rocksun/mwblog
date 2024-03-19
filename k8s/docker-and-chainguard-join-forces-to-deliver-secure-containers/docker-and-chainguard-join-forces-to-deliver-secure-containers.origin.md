# Docker and Chainguard Join Forces to Deliver Secure Containers
![Featued image for: Docker and Chainguard Join Forces to Deliver Secure Containers](https://cdn.thenewstack.io/media/2024/03/86c760d9-desk-593327_1280-2-1024x682.jpg)
Chainguard’s secure Developer Images will now be available via Docker Hub as part of the Docker Verified Publisher program.
I like
[Docker](https://www.docker.com/?utm_content=inline-mention) for managing containers, and I like [Chainguard](https://www.chainguard.dev/?utm_content=inline-mention) for its secure container images, so I’m really pleased that the two have joined forces to deliver [Chainguard Developer Images](https://www.chainguard.dev/chainguard-images) to [Docker Hub](https://hub.docker.com/) via the [Docker Verified Publisher (DVP)](https://docs.docker.com/trusted-content/dvp-program/) program.
For those of you who don’t know, Chainguard Developer Images are hardened by design. Each container image includes the minimum number of packages so they have the smallest possible attack surface. In addition, Chainguard images are patched daily without waiting on upstream distributions. The result? Chainguard images, according to the company, has 80% fewer
[Common Vulnerabilities and Exposures (CVE)](https://cve.mitre.org/) than its rivals.
Chainguard Production Images also meet even the most demanding requirements for patching Service Level Agreements (SLAs), FIPs-validated images for FedRAMP, and secure AI images. In other words, they’re darn good.
[Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/), of course, is a well-regarded container registry, which boasts over 10 million accounts and nearly 500 billion pulls from its vast community. I’m sure there must be someone out there who’s never used Docker Hub. I’ve just never met them.
In particular, the DVP program provides trusted content to Docker customers and users. This
[enables development teams to build securely](https://thenewstack.io/how-to-enable-developer-teams-to-improve-container-security/) and minimize access to malicious software.
Together, Chainguard Developer Images offers Docker Hub’s users secure, minimal container images for an expanding roster of cloud native and open source projects, including heavyweights such as Python, Node.JS, and Java.
Justin Cormack, Docker’s CTO, lauded the integration, highlighting the
[Docker Verified Publisher program’s central role in Docker’s mission to deliver](https://thenewstack.io/docker-delivers-docker-extensions-docker-desktop-for-linux/) a wide array of trusted, top-notch content. “By integrating Chainguard Developer Images into Docker Hub, we are providing Docker users with secure, minimal, and performant images.”
Echoing Cormack’s enthusiasm, Dan Lorenc, Chainguard’s CEO and co-founder, emphasized that the partnership allows Docker users to tap into a reliable source for secure, hardened, high-quality images, thus enabling them to meet rigorous security standards confidently. ” Chainguard Images are specifically designed to meet the needs of Docker Business and Trusted Content users, who rely exclusively on Docker to supply quality, secure, and hardened images that they can trust. ”
It’s not just Docker and Chainguard lauding this pairing. Darren Shepherd, AI development company
[Acorn Lab](https://www.acorn.io/)‘s co-founder and Chief Architect, is really pleased to see this combo. “Finally, Chainguard’s hardened container images are accessible on Docker Hub. Starting today, I’d estimate my Docker runs are now 70% more efficient, “Seriously though, this is something I’ve been asking Chainguard about for a while, and I’m glad to see the day has come. I can only hope the next critical innovation that happens is adding [Wolfi](https://github.com/wolfi-dev) [Chainguard’s security-first, container-specific Linux distro] into the library namespace.”
This alliance marks a critical advancement in their shared goal of
[securing the global software supply chain](https://thenewstack.io/linux-foundations-sigstore-aims-to-more-easily-secure-software-supply-chains/). It ensures that developers have the most secure resources and technologies at their disposal, a necessity in today’s fast-evolving digital realm.
For developers eager to explore Chainguard Developer Images, the 384 images currently available are readily available on
[Docker Hub via Chainguard’s DVP page](https://hub.docker.com/u/chainguard).
As usual, the rate limit for authenticated Docker Pro, Teams, and Business users is up to 5,000 daily pulls. Personal or free-tier Docker Hub users can access 200 pulls every six hours, and non-authenticated Docker Hub users can make 100 image pulls every six hours. If you run into rate-limiting issues, you can always pull images directly from
[Chainguard’s Directory](https://images.chainguard.dev/?category=featured?utm_source=blog&utm_medium=website&utm_campaign=FY25-EC-Blog_sourced). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)