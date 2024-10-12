# Configure Microservices in NestJS: A Beginner’s Guide
![Featued image for: Configure Microservices in NestJS: A Beginner’s Guide](https://cdn.thenewstack.io/media/2024/10/38d0b844-microservices-nestjs-configure-1024x576.jpg)
Monolithic architecture was the predominant approach to backend development before 2011. In this model, the entire application is structured as a single, unified codebase, where all components and services are tightly coupled and deployed together as one module. The monolithic approach encapsulates all business logic, data access, the user interface (UI) and other functionalities within a single executable or application.

While the [monolithic approach](https://thenewstack.io/monolith-vs-microservice-architecture-for-software-delivery/) offers simplicity in development and deployment, it introduces significant challenges as applications scale. With a single codebase, even minor changes necessitate rebuilding and redeploying the entire application, resulting in longer development cycles and higher risk of introducing errors. Moreover, scaling a monolithic application is often inefficient, as it typically requires scaling the entire system, even if demand increases in only one component. The tight coupling of components also leads to interdependencies, making the system more fragile and harder to maintain as teams and codebases grow.

The most critical drawback of monolithic architecture, however, is its extensive failure impact, often described as the “burst radius.” A failure in one component can cause the entire system to go down, leading to significant downtime. This interconnection heightens the risk of widespread outages and complicates troubleshooting and recovery. A single issue can cascade through the entire system, making it difficult to isolate and resolve without affecting other parts. Consequently, organizations often face prolonged downtimes, which can have a severe impact on business operations and the overall user experience.

Despite these drawbacks, the monolithic method was the standard for many years due to its simplicity and the lack of alternatives. However, [microservices](https://thenewstack.io/microservices/) and other new architectural paradigms have provided more flexible and scalable solutions.

## What Are Microservices?
In a microservices architecture, an application is composed of small, independent services that communicate with each other through well-defined APIs. Microservices divide an application into distinct, loosely coupled services. Each service is responsible for a specific piece of functionality; for example, in an e-commerce backend application, user authentication, payment processing, inventory management and other services, can be developed, deployed and scaled independently. This provides numerous advantages, including:

**Scalability**: Microservices enable the independent scaling of individual services. When one service experiences high demand, it can be scaled without impacting the entire application. This optimizes resource utilization and enhances overall performance.**Technology flexibility**: In a microservices architecture, each service can be developed using the most suitable technologies, languages or frameworks for its specific needs. This flexibility allows development teams to select the best tools for each task.**Fault isolation**: Due to the independent nature of microservices, a failure in one service is less likely to affect the entire system. This minimizes the impact of failures, enhances system resilience and reduces downtime.**Development and deployment speed**: Microservices allow teams to work on different services concurrently, accelerating development processes. Continuous integration and deployment practices are easier to implement, enabling faster updates and more frequent improvements.**Simplified maintenance and updates**: The modular structure of microservices makes maintaining and updating applications more straightforward. Changes can be made to individual services without affecting others, reducing the risk of errors and simplifying the testing process.**Organizational alignment**: Microservices facilitate organizing teams around specific business capabilities. Each team can take full ownership of a service, from development through deployment and support, leading to increased autonomy, accountability and efficiency.**Enhanced agility**: The modular design of microservices supports iterative development, allowing for more responsive adaptation to changing business needs and fostering rapid innovation.
## Monoliths vs. Microservices: Structural Differences
In a monolithic application, all client requests are handled by a single, general controller. This controller is responsible for processing the requests, executing the necessary commands or operations and returning the responses to the client. Essentially, all business logic and request handling is centralized, which simplifies the development process.

[In contrast](https://thenewstack.io/microservices/microservices-vs-monoliths-an-operational-comparison/), a microservices architecture introduces additional complexity with the inclusion of an application gateway. The application gateway serves as a crucial intermediary layer in a microservices setup. Here’s how it works:
**Request handling**: The gateway receives all incoming requests from clients.**Routing**: It then determines the appropriate microservice or controller that should handle each request based on its routing rules.**Service interaction**: The selected controller interacts with the corresponding microservice to process the request.**Response aggregation**: Once the microservice has completed its task, it sends the result back to the controller, which then forwards it to the gateway.**Client response**: Finally, the gateway returns the processed response to the client.
This layered approach separates the concerns of request routing and business logic, allowing each microservice to focus on its specific functionality while the gateway manages request distribution and response aggregation. If this sounds complex, don’t worry — I will walk through each component in detail and explain how it all works together.

## Implementing Microservices With NestJS
[NestJS is a progressive Node.js framework](https://thenewstack.io/implementing-iam-in-nestjs-the-essential-guide/) that leverages [TypeScript](https://roadmap.sh/typescript), offering a powerful combination of modern [JavaScript](https://roadmap.sh/javascript) features, object-oriented programming and functional programming paradigms. It is designed to provide a native application architecture that helps developers build highly testable, scalable and maintainable applications.
In this tutorial, I will show you how to implement microservices using NestJS as the primary technology, [NATS](https://nats.io/) as the communication medium, Prisma as the object-relational mapping (ORM) technology, MySQL as the database and finally Postman to test endpoints.

This approach will demonstrate how to effectively manage microservices, ensuring they communicate seamlessly, are easily scalable and can be deployed reliably in a production environment. Along the way, I’ll cover best practices for setting up a microservices architecture, managing dependencies and securing a deployment, creating a solid foundation for building robust and efficient distributed systems.

### Set Up the Base NestJS Application
Before you begin, ensure Node.js is Installed. Node.js is essential for running JavaScript code server-side and managing packages. If you haven’t installed Node.js yet, you can download it from the [official Node.js website](https://nodejs.org/). Next, use npm (which comes bundled with Node.js) to install the Nest command-line interface (CLI), a tool that simplifies the creation and management of NestJS applications.

With the Nest CLI installed, set up your base NestJS application to serve as your gateway and name it `api-gateway`
:

Launch your preferred text editor (e.g., VS Code, Sublime Text) and open the parent directory of the NestJS application (the directory that contains the parent folder of your base application). Navigate into the base application folder (i.e., `api-gateway`
) and open a new terminal instance. Most modern text editors have built-in terminal capabilities. For VS Code, you can open the terminal by selecting `Terminal`
from the top menu and then `New Terminal`
. For Sublime Text, you might need to use a plug-in like Terminus to open a terminal within the editor.

### Build the Backend Application
With your base application successfully up and running, the next step is to build a foundational backend application for a blog site. You’ll implement two separate services in this tutorial: one for managing readers, and another for handling create, read, update and delete (CRUD) operations for your blog articles. If you’ve worked with NestJS before, the project structure will be familiar and straightforward. However, I’ll provide a brief overview of the structure in case you’re not sure how it’s organized.

When you scaffold a new NestJS project, the default structure typically includes:

1. **src**: This is the main directory where most of your application code resides.

**app.module.ts**: The root module that ties together the different parts of the application.**app.controller.ts**: The controller responsible for handling incoming requests and returning responses.**app.service.ts**: The service that contains the business logic; can be injected into controllers.**main.ts**: The entry point of the application, where the NestJS app is bootstrapped.
2.** test**: This directory contains the test files for your application.

**app.e2e-spec.ts**: The end-to-end test file.**jest-e2e.json**: The configuration file for end-to-end testing with Jest.
3.** node_modules**: This directory holds all the installed dependencies for the project.

4.** package.json**: This file lists the dependencies and scripts for your project.

5.** tsconfig.json**: The TypeScript configuration file.

6.** nest-cli.json**: The configuration file for the NestJS CLI.

### Create the Microservices and Gateway
The next step is to create two additional applications that will serve as microservices and name them `reader-mgt`
and `article-mgt`
. These applications will function as independent microservices within the architecture. After that, install the `@nestjs/microservices`
and `nats`
libraries to enable communication between services. Then configure these two applications to listen for requests via NATS, ensuring they can handle the incoming messages accordingly.

So, in the same folder, run the following commands:

With the two services now scaffolded, configure your gateway to handle client requests and route them to the appropriate services. First, install the `@nestjs/microservices`
and `nats`
dependencies. Then create a NATS module, which will be registered in the [API gateway](https://thenewstack.io/api-gateway-checklist-how-strong-is-your-apis-front-door/)‘s app module to enable proper communication between the gateway and the microservices:

If you’re not already in the `gateway`
folder, use the `cd`
command to navigate into it. Once there, go to the `src`
folder and create a new directory named `nats-client`
, which will serve as the location for your NATS client configuration. After that, create a file named `nats.module.ts`
within the `nats-client`
folder, and add the following code:

This code creates a `NatsClientModule`
, which you’ll later register in the API gateway’s app module. First, it imports the `Module`
decorator along with the `ClientsModule`
and `Transport`
declarations from the `@nestjs/microservices`
library that you installed earlier. Next, it registers the `NATS_SERVICE`
and specifies the transport as `Transport.NATS`
. NestJS supports various transport clients by default, but for this example, stick with NATS.

Then it defines an `options`
object, which specifies the `servers`
property and sets the NATS server address to `nats://localhost:4222`
. Finally, it exports the registered NATS clients to make them accessible to other modules, which is useful if you have multiple modules within the gateway. For instance, you might have a users module, articles module, readers module and more. However, this tutorial uses a single controller and module for readers and articles.

With this complete, you can now proceed to the `app.module.ts`
file and register the `NatsClientModule`
:

At this point, you’re about 80% done with configuring the API gateway. The last step is to define the API routes in the `app.controller.ts`
file. Navigate to that file and add the following code:

This defines the API routes that will handle incoming HTTP requests and forward them to the NATS service for processing. The `AppController`
class uses the `@Controller`
decorator to specify the base route for all endpoints, which is `'api/'`
. Within this controller, inject the NATS client using the `@Inject`
decorator, associating it with the `'NATS_SERVICE'`
token. The controller includes several endpoints: `POST /save-reader`
and `GET /get-all-readers`
for managing readers, and `POST /save-article`
, `GET /get-all-articles`
and `POST /delete-article`
for managing articles. Each endpoint method uses the `natsClient.send`
method to send commands to the NATS service, passing the request body as the payload. This setup allows the API gateway to relay client requests to the appropriate microservices via NATS.

Finally, execute the `npm run start:dev`
command to start the API gateway application. This will verify that the application runs smoothly and without any errors.

![Screenshot of the api-gateway application](https://cdn.thenewstack.io/media/2024/10/11eb0f52-api-gateway_1-1024x640.png)
Figure 1: The api-gateway application

### Configure Communication Services
Next, configure your services to handle requests from the running API gateway, process them and send responses back. However, before proceeding, there’s an important step: setting up the NATS server locally. Since you specified the NATS server address as `nats://localhost:4222`
, both the gateway and services will expect a NATS server running on your local machine.

For development purposes, install the NATS server locally. Although you can run this in a [Docker](https://www.docker.com/?utm_content=inline+mention) container, work with a local setup for simplicity. For Linux and macOS users, install the NATS server using `brew install nats-server `
and run `nats-server`
to start the service. For Windows users, use `choco install nats-server`
. If `choco`
is not recognized, ensure Chocolatey is installed by running:

Then verify the installation by running `choco --version`
. If you need further guidance, consult the [NATS documentation](https://docs.nats.io/running-a-nats-service/introduction/installation).

![Figure 2: Screenshot showing the NATS server running locally](https://cdn.thenewstack.io/media/2024/10/e589f8d3-nats-server_2-1024x192.png)
Figure 2: NATS server running locally

### Configure Your First Service
Now you can configure your first service, `article-mgt`
. Go to the `main.ts`
file, which is the entry point of this service, and replace the default code with:

This code transforms `article-mgt`
from a standalone application into a NestJS microservice instance and configures it to use NATS as the transport mechanism, specifying the server address (`nats://localhost:4222`
) to connect to the NATS server.

Next, create a new directory named `dto`
within the `src`
folder, and then create a file named `dto.ts`
, which will house the expected payload structure. DTO stands for data transfer objects, which are simple objects used to transfer data between different layers of an application, especially during network requests. In this context, DTOs help define the structure and type of the payload that the backend application expects from client requests. You can implement further validation using the `class-validator`
dependency, if needed. However, to keep this article focused, we won’t use it here. You can learn more about `class-validator`
in the NestJS official [documentation](https://docs.nestjs.com/techniques/validation), if you’re interested.

This code defines two DTOs for handling data in the `article-mgt`
service. The `saveArticleDto`
class specifies the structure for saving an article, requiring a `title`
and `content`
. And the `deleteArticleDto`
class defines the structure for deleting an article, which requires an `id`
to identify the article to be removed. These DTOs help ensure that the data passed between different parts of the application is well-defined, consistent and matches the expected type. There are three routes for articles but only two DTO classes are defined. This is because the third route, which retrieves all articles, does not require any payload.

Now go to the `app.controller.ts`
file and modify the code.

![Figure 3: Screenshot of the code in the app.controller.ts](https://cdn.thenewstack.io/media/2024/10/27686622-app.controller-ts_3-1024x640.png)
Figure 3: Code in `app.controller.ts`

You might notice the red squiggly lines under the function names in the controller methods; this is because you haven’t yet defined these functions in `app.service.ts`
. Before addressing that, let me explain the code: It imports the DTOs to enforce type checking on payloads, ensuring the data passed to the functions meets the expected structure. The `@MessagePattern`
decorator specifies how messages should be handled. It takes an object where the `cmd`
property defines a command string. This string must match the command specified earlier in the API gateway. The API gateway uses this command to determine which function to call for a given API request, attaching the command to the request before forwarding it.

### Use Prisma To Interact With Your Database
To interact with your database using Prisma, create a Prisma module and service that you can use in the `app.service.ts`
file. Start by creating a folder named `prisma`
inside the `src`
directory. Then, within this folder, create two files: `prisma.module.ts`
and `prisma.service.ts`
. The `PrismaService`
in `prisma.service.ts`
extends the `PrismaClient`
class from Prisma and customizes the Prisma client by configuring the database connection URL using the `DATABASE_URL`
environment variable. The `PrismaModule`
in `prisma.module.ts`
defines a module that provides the `PrismaService`
, allowing it to be injected and used in other parts of the microservice for database operations.

Now, move to the `app.service.ts`
and add the code below to define the necessary functions. To explain briefly: The `saveArticle `
function takes `data`
as a parameter, which must be of the `saveArticleDto`
type, as defined earlier. The function uses a try-catch block to handle the process. First, it attempts to insert the data into the database. After that, it calls the `getAllArticles`
function to retrieve the updated list of articles. Since `getAllArticles`
is an asynchronous function, it uses the `await`
keyword. Once this is done, the function returns an object as a response, containing the `HttpCode`
, which includes the `statusCode`
, a message and a string. Additionally, the `getAllArticles`
function returns all articles from the database, and the `deleteArticle`
function handles the deletion of an article based on the provided ID.

### Start Your First Service
With that accomplished, you can now start your `articles-mgt`
service and check if it runs smoothly without any errors. To do this, simply execute the command `'npm run start:dev'`
.

![Figure 4: Screenshot of the article-mgt service running](https://cdn.thenewstack.io/media/2024/10/65f501f0-article-mgt_4-1024x640.png)
Figure 4: `article-mgt`
service

### Configure Your Second Service
Now that you’ve completed the `article-mgt`
microservice configuration, move on to configuring the `reader-mgt`
service. This service will handle two primary operations: registering readers and retrieving all registered readers. Since the setup process is quite similar to what I’ve already covered, I’ll skip the detailed explanations to save time. The implementation is essentially the same, just within a different service context.

To set up the `reader-mgt`
service, start by navigating to the `reader-mgt`
directory. Since the `main.ts`
file in this service will have the same code as the `article-mgt`
service, you can simply copy the content from the `article-mgt main.ts`
file and paste it into the corresponding file in `reader-mgt`
. Next, copy the entire `prisma`
directory from the `article-mgt`
service into the `reader-mgt`
service. However, this won’t work immediately; you’ll need to install and initialize Prisma in the `reader-mgt`
service. Run `npm install Prisma @prisma/client`
to install Prisma, and then execute `npx prisma generate`
to initialize it. Additionally, define the schema for the readers and perform a migration. Don’t forget to copy the database connection string from the `.env`
file in `article-mgt`
because without it, the `reader-mgt`
microservice won’t be able to connect to the database.

![Figure 5: Screenshot of the reader and article models](https://cdn.thenewstack.io/media/2024/10/ce5c42cf-reader-article-modules_5-1024x640.png)
Figure 5: Reader and article models

After defining the reader schema, run `npx prisma migrate dev`
to apply the migration to the database, which will add the `reader`
table to the MySQL database.

The final step involves configuring the `app.controller.ts`
and `app.service.ts`
files in the `reader-mgt`
service. This process is similar to what you did in the `article-mgt`
service. In the controller, define the routes, and then map these routes to corresponding functions in the service. You can use the `article-mgt`
microservice configuration as a reference to guide you through this process.

### Run Your Microservice
After configuring the `app.service.ts`
, `app.module.ts`
and `app.controller.ts`
files for the `reader-mgt`
service, the final step is to run the microservice to ensure that everything is functioning correctly and that there are no errors. This involves verifying that the routes in the controller correctly map to the functions in the service and that the microservice can handle requests as expected.

Once you’ve confirmed that all configurations are in place, you can start the `reader-mgt`
service using the `npm run start:dev`
command. This will launch the service in development mode, allowing you to check for any issues and ensure that the service is working seamlessly.

![Figure 6: Screenshot of the reader-mgt microservice in operation](https://cdn.thenewstack.io/media/2024/10/f428f8f6-reader-mgt_6-1024x640.png)
Figure 6: reader-mgt microservice

### Test Your Application
If you’ve made it this far, congratulations! The coding portion of your project is complete, and your `api-gateway`
, `reader-mgt`
and `article-mgt`
services are up and running without any errors. The next step is to use Postman to test the application and ensure that it performs as expected. Use Postman to send requests to the API gateway and verify that the operations are being correctly handled by the microservices. This will help confirm that all parts of the application are working together seamlessly.

![Figure 7: Screenshot showing the /save-reader endpoint working](https://cdn.thenewstack.io/media/2024/10/393ac4e1-save-reader_7-1024x640.png)
Figure 7: `/save-reader`
endpoint

![Figure 8: Screenshot showing /get-all-readers returning all registered readers](https://cdn.thenewstack.io/media/2024/10/acdfdbfd-get-all-readers_8-1024x640.png)
Figure 8: `/get-all-readers`

The image illustrates the flow of the `save-reader`
and `get-all-readers`
endpoints as they pass through the API gateway and reach the `reader-mgt`
microservice. The API gateway first receives the requests, identifies the correct commands and forwards them to the `reader-mgt`
service via NATS. The `reader-mgt`
service then processes the requests by creating a new reader or retrieving all readers. Once the requests are successful, the service returns the appropriate response.

Next, test the `article-mgt`
endpoints by sending requests to create, delete and retrieve articles. First, send three create requests to the `/save-article`
endpoint to add three articles to the database, as shown in Figure 9. Then send a request to the `/delete-article`
endpoint to delete the article with an ID of 2. Finally, make a GET request to the `/get-all-articles`
endpoint to retrieve the updated list of articles, confirming that the deletion was successful and the remaining articles are correctly listed in the database.

![Figure 9: Screenshot of successful /save-article requests](https://cdn.thenewstack.io/media/2024/10/49bb1ed6-save-article_9-1024x640.png)
Figure 9: `/save-article`
requests

![Figure 10: Screenshot of a successful /delete-article request](https://cdn.thenewstack.io/media/2024/10/d1593eca-delete-article_10-1024x640.png)
Figure 10: `/delete-article`
request

![Figure 11: Screenshot of a successful /get-all-articles request](https://cdn.thenewstack.io/media/2024/10/012dd0aa-get-all-articles_11-1024x640.png)
Figure 11: `/get-all-articles`
request

## Conclusion
Congratulations on reaching the end of this comprehensive setup guide! You’ve navigated through the intricacies of configuring a robust microservices architecture using NestJS, Prisma, MySQL and NATS. While you’ve successfully set up a functional microservices architecture, there’s always room for further enhancements.

As you continue to develop your application, consider implementing additional features such as robust error handling, security measures and comprehensive logging. Exploring Docker for containerization and [Kubernetes](https://thenewstack.io/kubernetes/) for orchestration could further streamline your development and deployment processes.

Thank you for following along with this guide. Your dedication to mastering these technologies will undoubtedly pave the way for creating sophisticated and resilient applications. If you need the code for this blog, find it in my [GitHub repository](https://github.com/RaymondZziwa/microservices). Happy coding, and best of luck with your continued development!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)