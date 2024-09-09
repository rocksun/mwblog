# Nhost Carves a Niche Between Managed Backend and Dev Platform
![Featued image for: Nhost Carves a Niche Between Managed Backend and Dev Platform](https://cdn.thenewstack.io/media/2024/09/fb764f49-nhostlogo1-1024x576.png)
In the crowded world of [backends](https://thenewstack.io/why-backend-developers-should-fall-in-love-with-graphql-too/) as a service, Nhost has decided — with apologies to the [Grinch’s take on Christmas in Whoville](https://docs.google.com/document/d/10yulrehQodGE7jqCt6AT0W_gclURWfo4q0HryBjTxVw/preview?hgd=1) — that a BaaS should be “a little bit more.”

“It’s either you are a BaaS or you are a PaaS, a platform as a service like a Heroku, Render or Railway. You have to make lots of decisions there. You have to write the code, you have to run the code, right?” said [Nuno Pato](https://github.com/nunopato), Nhost co-founder and CEO.

By adding its Nhost Run feature, the company is focusing somewhere in the middle. It’s also adding [AI features](https://thenewstack.io/ai/) to make development simpler.

[Nhost Run](https://nhost.io/blog/run) aims to make it easy to extend the Nhost stack to run any custom and third-party open source solutions, in the language of your choice, all in the same place.
“What we’re really trying to do is to offer the convenience of a pre-made or turnkey solution like Firebase — you create the project, you get the fundamentals there, and then with Run, you can actually extend so you don’t need to go outside. [You] have everything under the same umbrella,” Pato said.

You can integrate with services such as Redis, Memcached, Datadog Agents or MongoDB with your Nhost backend.

## Backend Plus the Option to Extend
Pato, who lives in the Azores, began working on Nhost in 2020, through an accelerator program called Antler where he met [Johan Eliasson](https://github.com/elitan), who originally founded the company in Sweden. As with many companies, it grew out of the founders’ frustration with building the same basic backend services over and over.

“Every time I had to start a new project, I had to do the same things over and over: pick a database, configure it, write code for the API, authentication, storage … those fundamental components that are present in most apps or projects,” he said.

Building the company as an open source serverless backend for web and mobile apps, it joined the field offering alternatives to [Google](https://cloud.google.com/?utm_content=inline+mention)’s [ Firebase](https://thenewstack.io/firebase-suite-google-fires-new-mobile-dev-powers/). Under the hood, Nhost offers:

- A Postgres database, in which you can treat the database like a spreadsheet or connect directly to write raw SQL and have full control over it.
- The
[Hasura](https://hasura.io/?utm_content=inline+mention)GraphQL Engine, open source technology that connects various data stores and auto-generates a GraphQL API, is used for full-text search, event triggers and real-time subscriptions. It enables specific row and column permissions to enable collaboration, yet with controls. - Authorization for web and mobile apps with FIDO security keys or device biometrics for passwordless or multifactor authentication.
- Hasura storage connects with any S3-compatible storage service.
- Serverless functions that handle custom code in JavaScript and TypeScript with infinite scale. These functions are built for AWS Lambda and deployed in the same
[AWS](https://aws.amazon.com/?utm_content=inline+mention)region as your backend. - Nhost also offers a managed cloud.
Nhost integrates with major frontend frameworks such as React, Next.js and Vue.

“We had a few customers that were hosting the database and the APIs with us, but they were hosting custom services like Python services for machine learning or artificial intelligence pipelines. They were hosting those in different providers, like Render or Heroku, and at some point, we just said, ‘Why don’t we just allow them to just run everything with us?’ Right?” Pato said of the Run feature.

“So you create the project, you get up and running really quickly with the backend that we provision for you — again, storage, authentication, APIs and databases — but we also allow them to write their own services and then bring those services under the same Nhost umbrella.”

It runs everything on Amazon EKS, the managed Kubernetes service from AWS.

‘The backend has the first part, obviously. We just clean up the containers. We create a namespace per user or per project in each cluster that we have. We have clusters all over the place. And then the Run part. … You create your Docker file, you create the image, you push the image to our own registry, and then we just add the UI in our dashboard where you can set a configuration for that service that you’re bringing, and then we just run it. … We try to make it very, very easy, just with a few configurations,” he said.

## New AI Offerings
More recently, Nhost has added vector embeddings to its Postgres offering using [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/), the open source [Postgres extension](https://github.com/pgvector/pgvector) for similarity search. It also released Auto-Embeddings, using OpenAI to enable queries in natural language plus an easier way to keep embeddings up to date. When there is a change, Auto-Embeddings will regenerate the embeddings and store the new ones in the database so the user does not need to write that code.

Its AI Assistants use ChatGPT, which, along with pre-defined access expressed as GraphQL queries, mutations and/or webhooks can be used for processes involving access to different types of data, with permissions to that data strictly enforced. You can use Assistants to build LLMs using the Nhost knowledge base.

It also has released [Graphite](https://nhost.io/blog/dev-assistant), a developer assistant and coding partner. It understands your project’s database and GraphQL schemas to provide context-aware suggestions to make development easier.

In its $3 million seed founding round, led by Nauta Capital, GitHub founders Scott Chacon and Tom Preston-Werner and Netlify founders Christian Bach and Mathias Biilmann Christensen also participated.

Firebase, though a popular way to get started with a project, is proprietary and has spawned a number of open source [alternatives](https://thenewstack.io/guide-serverless-technologies-functions-backends-service/), including [Supabase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/), [AppWrite](https://thenewstack.io/appwrite-a-cloud-native-backend-as-a-service/), Back4App, Parse, [Kinvey](https://thenewstack.io/introducing-kinvey-flex-industrys-first-unified-node-js-mbaas-platform/), and Kuzzle as well as myriad other proprietary offerings, including [AWS Amplify](https://thenewstack.io/independent-baas-providers-should-be-worried/).

Nhost originally thought of Supabase as its closest competitor, according to Pato, but he now says they are too focused on the database while Nhost is trying to carve out a niche with features like Run, software add-ons like Graphite, and platform features like [Dedicated Compute](https://nhost.io/blog/dedicated-compute), which allows you to allocate CPU and RAM for each service on the Nhost stack, and [Service Replicas](https://nhost.io/blog/service-replicas), multiple concurrent instances of the same service deployed across various machines to eliminate bottlenecks and improve availability and fault tolerance.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)