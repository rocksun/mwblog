The Docker Hub is going to drastically decrease the rate limits for free
accounts on April first. Are you ready for those changes? Here’s a high level
overview of
[the rate limit changes we’re about to have](https://docs.docker.com/docker-hub/usage/):

Account type | Old rate limit | New rate limit (April 1st) |
---|---|---|
Free, authenticated | 200 image pulls per hour | 100 image pulls per hour |
Free, unauthenticated | 100 image pulls per hour | 10 image pulls per hour (per IPv4 address or IPv6 /64 subnet) |
What if you could easily cache images so these rate limits don’t impact your workloads? Today I’m going to show you how you can set up your own pull-through cache of the docker hub so that your workloads only have to download images once.

A prone cartoon tiger vibing on a pier with coffee. Image generated using Pony Diffusion v6.

## Pull-through caches and you[](#pull-through-caches-and-you)
When you start an app in a Docker image, the Docker daemon needs to pull the image to your server before it can run. Normally this is done by directly connecting to the registry containing the image (such as the Docker Hub), asking for a list of image blobs, and then downloading all the blobs.

When you configure your Docker daemon to use a pull-through cache for a registry, the process changes a little. Instead of contacting the registry directly, your Docker daemon asks the pull-through cache if it has the image cached. If it does, you pull the image from the cache and avoid using part of your rate limit.

What happens when the image isn’t cached? The pull-through cache will query the upstream registry to see if the image exists. If it doesn’t, the error is propagated back to the Docker daemon.

But if it does, the registry responds with a list of blobs and the pull-through cache starts downloading them. As the blobs get downloaded, they get forwarded to the Docker daemon as well.

![](/blog/assets/images/cache-download-3c40f8efc5af288b0c592ed68e6e1f44.webp)
This lets you continue using the Docker Hub as normal, but you don’t need to authenticate every server with an account. When you store your cached images in Tigris, you also can take advantage of Tigris’ global architecture to make sure that the images are as close to your servers as possible.

## Setting one up[](#setting-one-up)
You can set up your own pull-through cache of the docker hub in minutes with our
[example on GitHub](https://github.com/tigrisdata-community/pull-thru-docker-hub).
All you need is the following:

- A free Tigris account on
[https://storage.new](https://storage.new) - A Tigris bucket
- A Tigris
[authentication keypair](https://console.tigris.dev/createaccesskey) - A user account on the Docker Hub
- A server with
[Docker and Docker Compose installed](https://docs.docker.com/engine/install/ubuntu/)or a Kubernetes cluster with HTTP ingress set up (such as with[k3s](https://k3s.io)and[Traefik](https://docs.k3s.io/networking/networking-services#traefik-ingress-controller))
From there, you prepare the environment configuration, edit some settings, and apply the configs. You can use it in your systems (such as the Docker daemon or k3s) by pointing to the pull-through cache server. Here’s how you do it on a Linux machine running the Docker daemon:

- Open
`/etc/docker/daemon.json`
in a text editor as root - Add the HTTPS url of your pull-through cache server to the
`registry-mirrors`
key like this:
`{`
"registry-mirrors": ["https://dockerhub.yourdomain.example"]
}
After you restart the Docker daemon (`sudo systemctl restart docker`
), any time
you pull an image from the Docker Hub it ’ll automatically be cached and pulled
from Tigris instead.

## Conclusion[](#conclusion)
Once you’ve set up a cache like this, you don’t have to worry about the Docker hub rate limit changes again. If you run into rate limits that start impacting your operations, you only need to update that one account that’s used to do all the pulls for your pull-through cache. This lets you get the best of both worlds: all your machines will be protected from the changes to rate limits and you don’t have to distribute a password to all your systems or developer machines.

Want to give this a try? Create an account on Tigris and follow
[the instructions on GitHub](https://github.com/tigrisdata-community/pull-thru-docker-hub)!

# Want to try Tigris?
Make a bucket and store your Docker images across the globe without egress fees!