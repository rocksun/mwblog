# How To Prepare API Products for Low-Code and No-Code Integrations
![Featued image for: How To Prepare API Products for Low-Code and No-Code Integrations](https://cdn.thenewstack.io/media/2025/01/952a154a-jantine-doornbos-xt9tb6oa42o-unsplash-1024x683.jpg)
[Jantine Doornbos](https://unsplash.com/@jantined?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/black-laptop-computer-turned-on-displaying-source-code-on-table-xt9tb6oa42o?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
It’s 2025, and we’re witnessing the unprecedented rise of the citizen developer. Recent advancements in generative AI fully empower non-developers to create sophisticated workflows and solutions quickly and easily. Low-code and no-code platforms like Zapier, Make, and UIPath are already essential tools for businesses, as they enable broader participation in [software development without requiring deep technical](https://thenewstack.io/a-software-developers-guide-to-technical-writing/) expertise. This represents both a challenge and an opportunity for [API product developers](https://thenewstack.io/bring-purpose-to-api-product-development-with-apiops-cycles/): designing robust APIs for traditional developers yet accessible to this growing audience of non-technical users.

Unfortunately, many APIs fail to meet the needs of low-code and no-code developers. Issues such as complex authentication, cumbersome file handling, and a lack of explicit optimizations on integrations with automation platforms and marketplaces create significant barriers to adoption.

Through a real-world example, this article explores some critical considerations for preparing APIs to thrive in low-code and no-code ecosystems, explicitly focusing on file-handling APIs. By addressing these gaps, developers can position their APIs as user-friendly solutions that appeal to a growing audience.

## We Overlooked Low-Code/No-Code Readiness With Our API Product
We recently integrated our DWS API product with Zapier. Dogfooding our technology is essential at Nutrient, as it keeps the quality of our products high. The integration was a learning journey, as we were quickly reminded that API developers tend to focus on creating resources for developer-centric environments and optimizing their products for direct integration with code. However, low-code/no-code platforms operate differently, and APIs not optimized for these environments can face significant challenges.

These issues can be particularly pronounced for APIs that handle files because many low-code/no-code platforms expect URLs or otherwise can’t handle file streams. Many API products that work with files don’t persist them. The fact that they don’t offer file storage is by design to minimize data breach risks and limit the attack surface, as well as to simplify compliance and provide greater scalability.

In the world of no-code and low-code workflow automation, for example, things like transactional storage matters and not being ready for integration can lead to:

- Frustrated
[citizen developers](https://thenewstack.io/digital-workflows-low-code-and-the-rise-of-citizen-developers/)who struggle to integrate APIs into workflows; - Compatibility issues with popular platforms like Zapier and Make;
- Missed revenue opportunities from potential users unable to adopt the API product;
- Competitive disadvantages against APIs designed for seamless integration.
While integrating our API product with Zapier, we encountered these challenges. Despite being very robust in traditional developer environments, the way our endpoints were designed presented hurdles for low-code workflows, highlighting the need for us to tailor our API design practices to the new reality.

## Why Being Ready For Low-Code/No-Code Integration Matters
The consequences of neglecting low-code/no-code readiness with API products extend beyond user frustration. APIs that fail to align with these platforms risk losing out on significant market opportunities. Low-code/no-code tools are increasingly favored by businesses looking to reduce development overhead and enable non-technical users to automate processes. An API that cannot integrate seamlessly into these ecosystems:

**Limits its user reach**: Many users rely solely on low-code platforms to access APIs;**Misses out on recurring revenue**: Low-code integrations often drive long-term subscriptions;**Falls behind competitors**: APIs designed for low-code readiness gain traction faster and increase marketplace visibility.
API products working with files — an everyday use case across many industries — are especially at risk. Without optimized file-handling mechanisms, such APIs struggle to meet low-code tools’ transactional, secure, and user-friendly requirements.

## What We Learned While Integrating Our API Product With Zapier
To prepare APIs for seamless integration with low-code/no-code platforms, developers should adopt specific design principles and features. Here’s a couple of approaches that we’ve inferred from our experience of integrating DWS API with Zapier:

-
### Authentication Is More Than Passing An API Key With Every Request
API products tend to rely on API keys for authentication. These are primarily transactional APIs that don’t need file storage and complicated permissions, so there’s not much need for OAuth or JWT. When developers sign up for an account, they get an API key, and they can pass this key in the request header or within the payload.

While this looks simple enough for low-code and no-code integrations, we need to think [beyond how authentication is used in code and move](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/) to how our products will be used in a “connector” application on a workflow automation platform. Take [Zapier’s connection label](https://docs.zapier.com/platform/build/connection-label) as an example: A Zapier user could use multiple accounts for a single application. The connection label provides a way to differentiate between accounts beyond simple enumeration. It’s simple: your API product should be able to identify itself based on the API key used for authentication.

For example, to implement authentication for the DWS API with Zapier, where we did not have an endpoint specifically used to validate or identify the connection, we had to first switch from no-code “Form Mode” to low-code “Code Mode” because the only way we could implement it was to do a “dry run” of an API call that would otherwise consume API credits and would fail if the API key was invalid.

We ended up with something like this:

1234567891011121314151617181920212223242526272829 |
const formData = { instructions: JSON.stringify({ parts: [ { html: 'index.html', }, ], }), 'index.html': { content: "<!DOCTYPE html><html><head><title>Hello World</title></head><body><h1>Hello World!</h1><p>This is a PDF now.</p></body></html>", filename: 'index.html', contentType: 'text/html', }, };const options = { url: 'https://api.nutrient.io/analyze_build', method: 'POST', headers: { 'Authorization': `Bearer ${bundle.authData.api_key}` }, body: formData}return z.request(options) .then((response) => { const results = response.json; return results; }); |
We did a dry run of an HTML-to-PDF conversion, and a successful response meant the API key was valid. Unfortunately, we could not identify the connection, which presented a challenge when we wanted to publish our Zapier connector in their marketplace.
To enable your API to self-identify, you could implement an endpoint like **/account/info** that will return information about the account as JSON. Platforms like Zapier can infer the connection identifier from that JSON. There are two design approaches to consider:

**Single API key**: This is the default and likely what your API product started with. If your users get only one key, you can use the user’s email address or other contact information as an identifier and have your endpoint return something like “John Appleseed <john@appleseed.com>. “**Multiple API keys**: You could allow your users to generate, name, and manage multiple API keys. Depending on the complexity of your product, these keys can also have specific scopes. This approach has numerous benefits, as your users can monitor and manage costs per API key and distribute the capabilities within their team. In the context of integrations with low-code/no-code platforms, a user could name their key “Zapier Integration,” this would be what your API endpoint returns as an identifier.
Regardless of your approach, your API product should be ready for low-code or no-code platforms. This means you should have an endpoint designed to validate and identify the API key.

-
### File Handling Should Have Options
If your API product works with files, the integration with no-code/low-code platforms can become extra challenging because their users don’t necessarily think about if and where files persist, nor about how they are exchanged between different apps. But you have to.

When designing an API product that handles files, there’s a finite number of approaches to accepting and outputting files with API endpoints. The most common one for RESTful APIs is using multipart form data. It’s convenient, and developers can send metadata alongside the file. However, multipart form requests won’t necessarily be supported with out-of-the-box no-code tools, and the low-code approach can be challenging.

For example, to use the DWS API’s**/sign** endpoint with Zapier, we again had to switch from “Form Mode” to “Code Mode” because our API streams the resulting file, so we had to [hydrate it](https://docs.zapier.com/platform/build/hydration-cli) for use in Zaps. Then, we had to figure out how to use their limited Platform CLI to implement the multipart form request.

We eventually learned how to include the necessary dependency:

1 |
const MultipartFormData = z.require('form-data'); |
This helped us prepare our form data for requesting to sign a PDF:
12345678910111213141516171819 |
// previously defined: inputPdfBuffer, updatedFileName, bundleconst formData = new MultipartFormData();formData.append("data", JSON.stringify({ signatureType: "cades", cadesLevel: "b-lt",}));formData.append("file", inputPdfBuffer, { filename: updatedFileName, contentType: 'application/pdf',});const formDataHeaders = formData.getHeaders();const headers = { Authorization: `Bearer ${bundle.authData.api_key}`, 'Content-Type': formDataHeaders['content-type'],}; |
This took time because it required understanding their “z” object. The LLMs struggled with this, insisting on using the unsupported **await** and hallucinating which dependencies could be imported and how.
Our API product was not ready for no-code developers, and the low-code approach presented challenges primarily because Zapier’s Platform CLI is sandboxed.

File-handling APIs can work with URL references instead of file streams and multipart form data. Of course, this requires file storage, but many applications that offer connectors on Zapier and other marketplaces expose files from their storage and offer a download permalink for easy integrations.

Looking at our DWS API as an example, the **/build** endpoint can accept a file URL instead of a stream as the **FilePart** parameter. Still, to make it no-code/low-code friendly, we would need to move beyond multipart form requests and have an endpoint that can accept a file URL in the payload without the added complexity. This enables a no-code integration that is not as easy to achieve today.

The situation is very similar when it comes to output. If the API product offers file storage, the API endpoint can return a permalink instead of streaming the file when there’s a file output. This comes with its own business implications, as introducing file storage tends to complicate the offering. At a minimum, businesses serving customers in the EU will have something to say about the geographical region where their users’ files are stored.

-
### API Endpoints Should Be Discrete And Predictable
Low-code/no-code platforms typically operate on a model of discrete tasks or “actions” that users chain together to create workflows. For example, in Zapier, a user might define a trigger (“When a file is uploaded”) and an action (“Convert the file”). It also captures the way no-code and low-code developers think. APIs with clearly defined actions that map directly to this workflow model will make it easier for users to integrate them into such platforms without custom coding or complex configurations.

As an engineer, I love what the team behind DWS API did with the **/build** endpoint. It’s extremely powerful, as you can send multiple documents and bundle different operations, running them sequentially. For example, you can use a single API call to accept a bunch of files of various formats (e.g., several MS Office files, a couple of images, and a PDF), convert them all to PDF, merge them into a single PDF file and then compress the resulting file. It’s amazing, right? However, it tends to be too complex for developers who want to convert a single MS Office file to a PDF. A better approach to making our API product friendlier for no-code and low-code integrations would be to create endpoints around specific actions like**/convert **and **/compress**.

Discrete actions allow for greater API call flexibility, especially relevant for platforms like Zapier that chain “actions.” They are also more intuitive, making potential errors much more straightforward to isolate and debug. Ultimately, APIs designed around predictable, task-based actions promote better usability. We aim to design APIs that are technically robust but also highly accessible and intuitive enough for the growing audience of citizen developers and non-technical users.

-
### Documentation Should Be Low-Code And No-Code Developer Friendly
If you have an API product, you should use it to build integrations with popular workflow automation no-code and low-code platforms. This will be a phenomenal opportunity to learn and improve. Doing this at Nutrient revealed that our API product was not entirely up to the challenge. We had no specific guides for low-code integrations, no manuals for setting up our product with no-code platforms, and no pre-built actions or workflows that users could use directly without learning to code with our API endpoints.

Another suggestion is to continue dogfooding your API product and specifically integrating it with no-code platforms. This will allow you to regularly test API compatibility with these platforms, resolve issues proactively, and continuously improve your documentation.

## Unlocking the Full Potential of Your API Product
API products are no longer just developer tools. They are integral to a growing ecosystem of low-code and no-code solutions. In addition to that, the term “developer” is evolving with every new code-generating productization of an LLM that sees the light of day. By adopting good practices for validating and identifying authentication, providing options for file handling and platform-friendly design, and ensuring documentation is up to speed, you can ensure that your API is ready to meet the demands of this evolving market.

Low-code/no-code readiness for API products isn’t just about avoiding frustration—it’s about unlocking new revenue streams, expanding your user base, and staying competitive in a rapidly changing API landscape. We are already improving [DWS API](https://www.nutrient.io/api/), and you should, too. The time to act is now.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)