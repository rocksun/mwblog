# Backstage Multicluster UI for Cloud Foundry and Kubernetes
The open source and CNCF incubating project [Backstage](https://backstage.io/) has become a central piece of many companies’ platform engineering toolkits. And for good reasons. The framework designed for building developer portals offers an extensive catalog of plugins via its app store and easy creation of your own plugins.

In this article, I will showcase how to integrate [Stratos](https://stratos.app/) — an open source multicluster UI that supports Cloud Foundry, Kubernetes, EKS, AKS, GKE, and more — inside Backstage. While the project has been around for 7 years, it recently received a surge of interest due to the multicloud growth and the [platform engineering need to have every part of an infrastructure](https://thenewstack.io/the-pillars-of-platform-engineering-part-5-orchestration/) under one roof.

## Backstage BYO Plugins
While the Backstage community already features [over 200 plugins](https://backstage.io/plugins), the strength of the tool is also that it offers an easy way to build and integrate any infrastructure or software development tool via your own plugin. While there are a variety of Backstage plugins, they can be grouped into two main categories. The frontend plugins expose a UI on the Backstage app, and the backend plugins [manage server-side operations](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/). You can see all the different plugin templates Backstage offers by typing
yarn new in your Backstage application folder.

## Creating Our Backstage Plugin
First, you need a Backstage app installed (follow the installation instructions [here](https://backstage.io/docs/getting-started/)). Start your app frontend and backend with the
yarn start and
yarn start-backend commands. You will next create the frontend plugin by typing the following at the root of your Backstage project:

The prompt will ask you for a plugin ID. It can be any string. In my case, I will name it
stratos.

12345678910111213 |
? Enter the ID of the plugin [required] stratosCreating frontend plugin @internal/backstage-plugin-stratos Checking Prerequisites: availability plugins/stratos ✔ creating temp dir ✔ Executing Template: templating .eslintrc.js.hbs ✔[...]🎉 Successfully created plugin |
You can check that your plugin is running well by calling it
curl -I http://localhost:3000/stratos/or pasting the URL in a browser.
Each Backstage plugin is treated as a self-contained web app, making it very powerful, but there is also a learning curve. For the sake of simplicity, I will use existing example templates provided by Backstage to build my plugin. If you do this for production purposes, here is the documentation for [building one properly](https://backstage.io/docs/plugins/plugin-development).

We will edit an existing Stratos [component file to integrate our iframe to embed](https://thenewstack.io/how-to-build-embed-components-with-astro-qwik-and-stackblitz/) the Stratos interface. To do so, we will edit the file
plugins/stratos/src/components/ExampleComponent/ExampleComponent.tsx and paste the following content inside it.

12345678910111213141516171819202122 |
import React from 'react';import { Typography, Grid } from '@material-ui/core';import { Header, Page, Content,} from '@backstage/core-components';import { ExampleFetchComponent } from '../ExampleFetchComponent';export const ExampleComponent = () => ( <Page themeId="tool"> <Header title="Backstage + Stratos = ❤️" /> <Content> <iframe src="http://localhost:8080/" width="100%" height="100%" style={{ border: 0 }} /> </Content> </Page>); |
I won’t go into details of the configuration file, but it is important to note that we are serving the iframe with
src="http://localhost:8080/”which will display the Stratos interface into Backstage.
Our work with Backstage is done; now, let’s start with Stratos.

## Deploying Stratos
There are three ways to deploy Stratos: Cloud Foundry, Kubernetes or [Docker](https://stratos.app/docs/deploy/all-in-one). I will use the Docker way, you can start Stratos by running the following command
docker run -p 5443:5443 splatform/stratos:stable .

Depending on how you deploy and configure Stratos, you may be able to serve it directly into the Backstage iframe. In our case, the certificate in the Docker container is expired, and there is no easy [way to fix](https://thenewstack.io/your-authorization-system-is-broken-here-are-5-ways-to-fix-it/) it; we need to put a proxy in front of Stratos. Backstage offers a built-in proxy that can do the job, but depending on how you deploy Stratos, you may not be able to get a working solution. I won’t go into the details in this article, but in [this video,](https://youtu.be/VgbK4rceFSc?si=roojGEYRGkSL6zIB) I demonstrate how to proxy traffic using Backstage and go over the challenges that you may face.

We will instead use Nginx for proxying to create an easy-to-build solution. Here is what we will need for our Nginx configuration.

123456789101112131415161718 |
server { listen 8080 default_server; listen [::]:8080 default_server; # Stratos Proxy location / { proxy_pass https://localhost:5443/; proxy_set_header Host $host; proxy_hide_header X-Frame-Options; } location ~* \.(js|css|png|jpg|jpeg|svg|woff|woff2|ico)$ { proxy_pass https://localhost:5443; proxy_set_header Host $host; proxy_hide_header X-Frame-Options; }} |
This Nginx configuration file is split into two main parts: the first serves the [dynamic content and static](https://thenewstack.io/how-to-secure-web-applications-in-a-static-and-dynamic-world/) assets. As mentioned before, proxying allowed me to make it possible to serve Stratos via an iframe; here are a few essential points:
- listen 8080 default_server; — Stratos is served over HTTPS, and when using the current Docker image, it does not have a valid SSL certificate, which is a problem for the iframe. I am serving the traffic over HTTP with Nginx to solve that issue.
- proxy_hide_header X-Frame-Options; — Stratos includes a same-origin policy in its response header, preventing the browser from displaying the page in an iframe. This Nginx directive removes the header that contains that security policy.
Start Nginx, and you should see this when you refresh the plugin page.

Integrating Stratos into Backstage provides a streamlined, centralized view of multicluster Cloud Foundry and Kubernetes environments, simplifying infrastructure management. Stratos is used by notable end-users like Comcast and TwentyFive. While this setup is intended for demonstration — not production — it highlights how Backstage’s powerful plugin ecosystem can set the stage for scalable and collaborative [platform engineering](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)