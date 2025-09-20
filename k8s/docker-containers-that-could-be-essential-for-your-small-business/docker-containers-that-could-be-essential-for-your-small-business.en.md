Generally speaking, [containers](https://thenewstack.io/introduction-to-containers/) make things easy. From deployment, management, backups and so much more, this technology has become invaluable for many user types. If you run a small business and are tired of having to pay the high cost of third-party services, you might want to consider opting to go with containers for essential services that don’t require proprietary, vendor-locked-in tools.

If you head over to [Docker Hub](https://hub.docker.com/), you’ll find what seems like a never-ending supply of [container images](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) that you can pull, configure and deploy. But if you were to ask me which containers you should use for your business, I could easily shorten that list down to a select few.

Do understand, however, that every business is different, and yours might have special requirements that those on this list don’t meet. That’s fine, because you can head back to Docker Hub and find exactly what you’re looking for.

Let me tell you the containers I think are all perfectly suited for [small businesses](https://thenewstack.io/linux-zentyal-is-the-small-business-server-you-may-need/).

## 1. Nextcloud

There’s a reason why Nextcloud is listed at the top; it’s fantastic. This cloud solution makes it possible for you and/or your business to be weaned from the likes of [Google](https://cloud.google.com/?utm_content=inline+mention) Workspace, [Microsoft 365](https://thenewstack.io/saas-rootkit-attack-to-create-hidden-rules-in-office-365/) and Apple iCloud. Nextcloud includes plenty of built-in features, like storage, calendars, documents, talk, emails, Kanban boards and so much more. If you find Nextcloud doesn’t include a feature you need, there are tons of apps you can sift through and install. Nextcloud is simply the de facto standard for a self-hosted cloud service. I’ve used Nextcloud for years and have always found it not only incredibly useful, but also reliable and secure. For Docker purposes, I suggest using the [Nextcloud AIO solution](https://hub.docker.com/r/nextcloud/all-in-one), as it includes all the pieces you’ll need in one handy container image.

You can deploy Nextcloud with a command like so:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo docker run \ |
|  | --sig-proxy=false \ |
|  | --name nextcloud-aio-mastercontainer \ |
|  | --restart always \ |
|  | --publish 80:80 \ |
|  | --publish 8080:8080 \ |
|  | --publish 8443:8443 \ |
|  | --volume nextcloud\_aio\_mastercontainer:/mnt/docker-aio-config \ |
|  | --volume /var/run/docker.sock:/var/run/docker.sock:ro \ |
|  | nextcloud/all-in-one:latest |

## 2. Invoice Ninja

I’ve been using Invoice Ninja for nearly five years, and it never lets me down. Invoice Ninja is a great alternative because it makes creating and sending invoices to clients easy and professional-looking. I’ve tried other invoice apps, and they all pale in comparison to this. Invoice Ninja includes features like customizable invoice creation, recurring billing, automated payment reminders and support for multiple currencies and languages. I’ve yet to find a better self-hosted invoicing solution than Invoice Ninja.

You can deploy an instance of Invoice Ninja with a command like:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d \ |
|  | -v /var/invoiceninja/public:/var/app/public \ |
|  | -v /var/invoiceninja/storage:/var/app/storage \ |
|  | -e APP\_ENV='production' \ |
|  | -e APP\_DEBUG=0 \ |
|  | -e APP\_URL='http://ninja.dev' \ |
|  | -e APP\_KEY='<INSERT THE GENERATED APPLICATION KEY HERE>' \ |
|  | -e DB\_TYPE='mysql' \ |
|  | -e DB\_STRICT='false' \ |
|  | -e DB\_HOST='localhost' \ |
|  | -e DB\_DATABASE='ninja' \ |
|  | -e DB\_USERNAME='ninja' \ |
|  | -e DB\_PASSWORD='ninja' \ |
|  | -p '9000:9000' \ |
|  | invoiceninja/invoiceninja-debian |

Do note that you need to have an application key, which can be generated with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show |

## 3. Bitwarden

Don’t get me wrong, I’m all about using the official [Bitwarden](https://thenewstack.io/walkthrough-bitwardens-new-secrets-manager/) servers for my vaults, but there are certain reasons why you might want to use this [password manager](https://thenewstack.io/linux-pass-a-text-based-password-manager/) from within your LAN. For example, you might have information that absolutely must not fall into the wrong hands. For such information, you can deploy a Bitwarden server on your LAN via Docker. I’ve used Bitwarden for years and have always been happy with the product and the security it offers. If you do decide to deploy a Bitwarden server on your LAN, know that it’s a bit more complicated than some other options, but the company has plenty of [documentation](https://bitwarden.com/help/install-and-deploy-unified-beta) to help you get through the process.

## 4. Homebox

Homebox is actually geared towards home, but that doesn’t mean it’s not a viable option for your small business. What Homebox does is help you keep track of just about anything you need. You can also create rooms that house those items, or locations for collecting items (such as Office, Kitchen, etc.). One thing to understand is that when you first create an item, you’re very limited in the information you can save. Once the item is created, however, go back to the edit page for that item and you’ll find tons more fields that can be used. Homebox also includes an asset ID label generator, a Bill of Materials feature, import/export and inventory actions. There’s also a powerful search feature and labels feature, for when your item list gets out of hand. One thing to keep in mind is that Homebox is in early development.

Homebox can be deployed and used for free with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d \ |
|  | --name homebox \ |
|  | --restart unless-stopped \ |
|  | --publish 3100:7745 \ |
|  | --env TZ=Your/Locale\ |
|  | --volume /path/to/data/folder/:/data \ |
|  | ghcr.io/hay-kot/homebox:latest |

Make sure to change

*Your/Locale*

to match your location.

## 5. Outline

Outline is a knowledge base tool that can help you collect your company’s information in a single place. Outline is a collaborative note-taking app on steroids that includes markdown support, slash commands, interactive embeds and much more. With this app, you can collaborate with teammates in real time, add comments and threads, use a powerful search tool, integrate it with Slack (and over 20 other tools) and share documents with the public.

Deploying Outline is a bit more complicated than a single command, but you can read the [installation documentation](https://docs.getoutline.com/s/hosting/doc/docker-7pfeLP5a8t) and find out exactly how it’s done. The self-hosted instance of Outline is free to deploy and use.

And there you have it: With just these five simple tools, deployed as Docker containers, you’ll find running your business to be a bit easier. There are certainly a ton more apps you could deploy via Docker, but these will get you started.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)