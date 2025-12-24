You’re a company with a developer or a team of developers. Those developers have created several in-house applications and services that integrate into your systems and are rather complicated.

After a while, attrition takes a few of those developers away, and you find those specialty bits and pieces of code were never documented.

What do you do?

How will you train the next round of developers to continue keeping those bits and pieces working seamlessly?

That’s a problem.

Had your developers documented their work and the systems, you could simply point those new team members to said documentation, so they could quickly get up to speed with what’s what.

Maybe those developers did document things, but the documentation was created haphazardly and is found in different locations and in different forms.

Would that you had a documentation management system to make this easier.

Fortunately, there is such a beast, and that beast is [Paperless-Ngx](https://docs.paperless-ngx.com/).

Paperless-Ngx is the official continuation of Paperless and Paperless-Ng. This [document management system](https://thenewstack.io/why-the-document-model-is-more-cost-efficient-than-rdbms/) is open source, self-hosted, and vastly simplifies the process of digitizing, organizing, and searching documents by converting them into an online archive. Paperless-Ngx even includes [Optical Character Recognition (OCR)](https://thenewstack.io/why-upstage-builds-small-language-models/), so you can easily scan documentation and images such that they are searchable, taggable, and indexable.

With Paperless-Ngx, you can eliminate clutter and confusion and ensure you always have documentation at the ready.

Paperless-Ngx includes features such as:

* Organize with tags, correspondents, types, and more.
* All data is stored locally and is never transmitted or shared.
* Built-in OCR support.
* Leverages the open source Tesseract engine to support more than 100 languages.
* Documents are saved in PDF/A format.
* Machine learning automatically adds tags and document types.
* Supports PDFs, images, plain text files, MS Office/LibreOffice documents.
* Customizable dashboard with statistics.
* Filtering
* Bulk editing of tags, correspondents, types, and more.
* Drag and drop uploading of documents.
* Customizable views.
* Custom fields.
* Shareable public links with optional expiration dates.
* Full text search.
* Auto completion to suggest relevant words.
* Email processing.
* Messages can be marked as read, deleted, and more.
* Multi-user permissions system.
* Workflow system for more control.
* Optimized for multi-core systems.
* Integrated sanity checker to ensure the document archive is in good health.

You might think such a system would be a challenge to deploy. Thanks to [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/), it’s not.

Let me walk you through the process of installing this outstanding document management system.

## What You’ll Need

The only things you’ll need for this are an operating system that supports Docker and a working internet connection. I’ll demonstrate this process on Ubuntu Server 24.04. If you’re using a different OS, you’ll need to modify the steps for installing Docker. If you already have Docker installed, you can skip directly to the installing Paperless-Ngx section.

Ready? Let’s go.

## Installing Docker

Before you install Paperless-Ngx, you’ll need to first install Docker. Here’s how to do that in four easy steps.

### Step 1: Add the official Docker GPG key

The first thing you must do is add the official Docker GPG key with the following commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get update |
|  | sudo apt-get install ca-certificates curl |
|  | sudo install -m 0755 -d /etc/apt/keyrings |
|  | sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc |
|  | sudo chmod a+r /etc/apt/keyrings/docker.asc |

### Step 2: Add the Required Docker Repository

With the key added, you can now add the necessary repository with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | <blockquote><i><span style="font-weight: 400;">echo \ |
|  | </span></i><i><span style="font-weight: 400;">  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] |
|  | https://download.docker.com/linux/ubuntu \ |
|  | </span></i><i><span style="font-weight: 400;">  $(. /etc/os-release &amp;&amp; echo "${UBUNTU\_CODENAME:-$VERSION\_CODENAME}") stable" | \ |
|  | </span></i><i><span style="font-weight: 400;">  sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null</span></i></blockquote> |

### Step 3: Update Apts and Install the Required Software

Let’s update apt with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

When that completes, install the required software with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y |

### Step 4: Add Your User to the Docker Group

Finally, to run the Docker command as a standard user, you’ll need to add that user to the Docker group. By doing this, you can avoid running Docker with sudo, which can bring about security issues. Add your user to the Docker group with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo usermod -aG docker $USER |

With that taken care of, log out and log back in so the changes take effect.

## Deploying Paperless-Ngx

It’s finally time to deploy our system. Back at the terminal window, issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)" |

You will have to answer several questions during the text-based installer, most of which are simple. In fact, you will probably want to keep all of the defaults by hitting Enter when prompted.

Pay close attention to the port number when asked. By default, Paperless-Ngx wants to use port 8000. I had several other services on my [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 24.04 server, and the first time I attempted to deploy Paperless-Ngx, I remember that port 8000 was already taken. Instead, I configured it for port 8081 and all was fine.

After the installation is completed, open a web browser on a machine that is connected to your [LAN](https://thenewstack.io/git-set-up-a-local-repository-accessible-by-lan/) and point it to http://SERVER:PORT (Where SERVER is the IP address of the server and PORT is the port you configured).

When the sign-in page opens (**Figure 1**), type an email address and password for your new account.

[![](https://cdn.thenewstack.io/media/2025/12/eec98d4e-screenshot-2025-12-17-at-1.06.59-pm.png)](https://cdn.thenewstack.io/media/2025/12/eec98d4e-screenshot-2025-12-17-at-1.06.59-pm.png)

**Figure 1:** The Paperless-Ngx login screen is also where you create a new account.

After you’ve created your account, you’ll find yourself on the Paperless-Ngx main page (**Figure 2**), where you can begin the process of uploading or creating documentation for your systems.

[![](https://cdn.thenewstack.io/media/2025/12/3c1930e7-screenshot-2025-12-17-at-1.08.10-pm-scaled.png)](https://cdn.thenewstack.io/media/2025/12/3c1930e7-screenshot-2025-12-17-at-1.08.10-pm-scaled.png)

**Figure 2:** Paperless-Ngx is ready to serve.

Never take documentation for granted. If you have proper documentation, you won’t have to deal with new development teams having trouble getting up to speed with what was previously done.

You should also probably put policies in place for how you want your documentation to look and read. Make this as simple as possible, and you’ll have few issues as your company grows and evolves.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)