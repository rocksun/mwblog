# Implementing the API Gateway Pattern in a Microservices Based Application with Node.js
## Build your own API Gateway using Node.js in under 5 minutes
Microservices offer enhanced scalability, flexibility, and agility.

As organizations adopt microservices-based applications, managing the diverse and distributed nature of these services becomes a challenge.

Therefore, the API Gateway pattern emerges as a crucial solution, serving as the central entry point for client interaction in a microservices ecosystem.

This pattern acts as a traffic orchestrator, simplifying the client experience and streamlining the complexities of microservices communication. Let’s explore more on this pattern.

# Understanding the API Gateway Pattern
The API Gateway pattern is a crucial component in microservices architecture, serving as a centralized entry point for client interactions. This pattern orchestrates traffic by intelligently routing requests to the appropriate microservices and aggregating responses for a seamless client experience.

Beyond simplifying communication, the API Gateway enforces security measures, including authentication and authorization. It also handles routing, protocol translation, load balancing, and caching, optimizing performance and scalability.

This comprehensive understanding highlights the API Gateway’s pivotal role in streamlining microservices communication and enhancing overall system efficiency.

# How Does The API Gateway Pattern Works?
The microservices API Gateway pattern functions as a central hub for client interactions in a microservices architecture.

Clients communicate exclusively with the API Gateway, which intelligently routes requests to the appropriate microservices based on predefined rules.

The API Gateway orchestrates traffic flow, aggregates responses from multiple microservices, and handles protocol translation for standardized communication. It enforces security measures, including authentication and authorization, and incorporates features like load balancing, caching, and logging.

The API Gateway simplifies client-side implementation, enhances security, and optimizes communication in a microservices-based system.

# What Are The Benefits Of API Gateway Pattern?
Using the API Gateway pattern offers a lot of benefits to an application. Some of its key benefits include:

**Simplified Client Interaction:**Clients interact with a single entry point, the API Gateway, simplifying the client-side implementation.**Intelligent Routing:**The API Gateway performs intelligent routing of requests to the appropriate microservices based on predefined rules, reducing the burden on clients to navigate the intricacies of the microservices network.**Traffic Orchestrator:**Serving as a traffic orchestrator, the API Gateway efficiently directs incoming requests, ensuring seamless communication between clients and microservices.**Response Aggregation:**The API Gateway can aggregate responses from multiple microservices into a cohesive and unified response. This reduces the number of requests made by clients and enhances overall system performance.**Protocol Translation:**It handles protocol translation, allowing clients to use standardized communication protocols while internally translating these requests into microservices-specific protocols.**Security Centralization:**Enforces security measures, including authentication and authorization, at a centralized location. This ensures a consistent and secure approach across the microservices ecosystem.**Load Balancing:**Incorporates load balancing to distribute incoming requests evenly among multiple instances of a microservice. This promotes optimal resource utilization and prevents individual services from becoming performance bottlenecks.**Caching Mechanisms:**Implements caching mechanisms to store and retrieve frequently requested data. Caching reduces the load on microservices, enhances response times, and optimizes resource usage.**Logging and Monitoring:**Centralizes logging and monitoring functionalities, providing insights into the health, performance, and usage patterns of the entire microservices architecture.
**How To Implement the API Gateway Pattern in Node.js?**
Now that we have a basic understanding of what the API Gateway Pattern is and how it works, let’s take a look at how you can implement one in Node.js

It’s important to understand that there is no “one” way to do this. In fact, there are several ways to implement the API Gateway pattern, each suited to different environments and use cases.

So, let’s take a look at two of the most common approaches.

**Approach 01: Container-Based Implementation (Using Kubernetes or Docker)**
Let’s see how we can implement and deploy API Gateway pattern in Docker environment.

First of all I created following folders and files structure for my application.

**Step 1 — Create the service-a Microservice**
`const express = require('express');`
const app = express();
const port = 3001;
app.get('/api/data', (req, res) => {
console.log(Received request to /api/data: ${req.method} ${req.url} );
res.status(200).send('Response from Service A');
});
app.listen(port, () => {
console.log(Service A listening on port ${port} );
});
This simply defines a simple Express API that has one GET method to return some sample data.

**Step 2 — Create the service-a Dockerfile**
`FROM node:14`
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3001
CMD ["node", "service-a.js"]
This creates a Dockerfile that’s responsible for creating a package executable of the microservice defined in step 01. It defines instructions on how to spin up the environment and to launch the server.

**Step 3 — Create the service-b Microservice**
`const express = require('express');`
const app = express();
const port = 3002;
app.get('/api/info', (req, res) => {
console.log(Received request to /api/info: ${req.method} ${req.url} );
res.status(200).send('Response from Service B');
});
app.listen(port, () => {
console.log(Service B listening on port ${port} );
});
This declares the second API that returns some information to the client through a simple GET endpoint.

**Step 4 — Create the service-b Dockerfile**
`FROM node:14`
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3002
CMD ["node", "service-b.js"]
This, again, creates an instruction file on how this microservice can be spun up.

**Step 5 — Create the API Gateway**
`const express = require('express');`
const httpProxy = require('http-proxy');
const app = express();
const proxy = httpProxy.createProxyServer();
const serviceAUrl = 'http://service-A:3001';
const serviceBUrl = 'http://service-B:3002';
app.use('/api/data', (req, res) => {
console.log(Incoming request to /api/data: ${req.method} ${req.url} );
proxy.web(req, res, { target: serviceAUrl }, (err) => {
console.error(Error forwarding request to service A: ${err.message} );
res.status(500).send('Internal Server Error');
});
});
app.use('/api/info', (req, res) => {
console.log(Incoming request to /api/info: ${req.method} ${req.url} );
proxy.web(req, res, { target: serviceBUrl }, (err) => {
console.error(Error forwarding request to service B: ${err.message} );
res.status(500).send('Internal Server Error');
});
});
// Add this middleware to log the request received by the proxy
proxy.on('proxyReq', function (proxyReq, req, res, options) {
console.log(Received request to ${options.target.href}: ${req.method} ${req.url} );
});
const port = 3000;
app.listen(port, () => {
console.log(API Gateway listening on port ${port} );
});
Now, this is the actual API Gateway Implementation. It creates a proxy server using http-proxy. This server is responsible for forwarding requests from the API gateway to the actual microservices (serviceA and serviceB) based on the request path.

Next, the routes are declared in the gateway, and is proxied to the internal microservices when an endpoint is invoked.

**Step 6 — Configure Docker Compose**
`version: '3'`
services:
service-a:
build:
context: ./service-A
dockerfile: Dockerfile
ports:
- 3001:3001
service-b:
build:
context: ./service-B # Correct the path if necessary
dockerfile: Dockerfile
ports:
- 3002:3002
api-gateway:
build:
context: ./api-gateway
dockerfile: Dockerfile
ports:
- 3000:3000
depends_on:
- service-a
- service-b
Next, you’ll have to create a Docker-Compose file that’s responsible for managing all three of these docker containers. This helps spin up, manage and terminate all three containers in a single command and treat it as one single entity.

**Step 7: Build and Run the Application**
Finally, run the`docker-compose up --build`
command to build the images for both services and the api gateway and start them as containers.

The api-gateway will serve on **localhost:3000.**

When you have to access the service-a or service-b, you can instead call api-gateway. Api gateway will route the requests correctly to the relevant service. You can test this by calling HTTP methods using either postman or browser. So that you can see output similar to below in the console.log

You can find the GitHub repository [here](https://github.com/ruvani/api-gateway-pattern) for its full implementation.

## Approach 02: Service Mesh Implementation
You can also use a service mesh with Node.js to implement the API Gateway. To do so, you can use tools like Express.js for building the API Gateway service, and Istio as the service mesh.

In order to do that, it requires below prerequisties.

- Node.js
- Docker installed
- Kubernetes cluster with Istio installed
**Step 1: Create an Express.js API Gateway**
Create a new directory for the API Gateway project and navigate into it

`mkdir api-gateway`
cd api-gateway
Initialize a new Node.js project.

`npm init -y`
Install required dependencies.

`npm install express axios`
Create an index.js file for the API Gateway.

`const express = require('express');`
const axios = require('axios');
const app = express();
const port = 3000;
app.get('/service1', async (req, res) => {
try {
const response = await axios.get('http://service1.default.svc.cluster.local');
res.json(response.data);
} catch (error) {
res.status(500).json({ error: 'Internal Server Error' });
}
});
app.get('/service2', async (req, res) => {
try {
const response = await axios.get('http://service2.default.svc.cluster.local');
res.json(response.data);
} catch (error) {
res.status(500).json({ error: 'Internal Server Error' });
}
});
app.listen(port, () => {
console.log(API Gateway listening at http://localhost:${port} );
});
**Step 2: Deploy Express.js API Gateway**
Dockerize the Node.js application by creating a Dockerfile in the project root.

`FROM node:14`
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
Build and push the Docker image.

`docker build -t your-registry/api-gateway:latest .`
docker push your-registry/api-gateway:latest
Create a Kubernetes deployment for the API Gateway (api-gateway-deployment.yaml).

`apiVersion: apps/v1`
kind: Deployment
metadata:
name: api-gateway
spec:
replicas: 1
selector:
matchLabels:
app: api-gateway
template:
metadata:
labels:
app: api-gateway
spec:
containers:
- name: api-gateway
image: your-registry/api-gateway:latest
ports:
- containerPort: 3000
Apply the deployment.

`kubectl apply -f api-gateway-deployment.yaml`
**Step 3: Configure Istio for API Gateway**
Create an Istio Gateway (gateway.yaml).

`apiVersion: networking.istio.io/v1alpha3`
kind: Gateway
metadata:
name: api-gateway
spec:
selector:
istio: ingressgateway
servers:
- port:
number: 80
name: http
protocol: HTTP
hosts:
- "your-api-gateway-host"
Create an Istio VirtualService (virtualservice.yaml).

`apiVersion: networking.istio.io/v1alpha3`
kind: VirtualService
metadata:
name: api-gateway
spec:
hosts:
- "your-api-gateway-host"
gateways:
- api-gateway
http:
- route:
- destination:
host: api-gateway.default.svc.cluster.local
port:
number: 3000
Apply the Istio Gateway and VirtualService.

`kubectl apply -f gateway.yaml`
kubectl apply -f virtualservice.yaml
**Step 4: Test the API Gateway**
Access your API Gateway using the specified host.

`curl http://your-api-gateway-host/service1`
curl [http://your-api-gateway-host/service2](http://your-api-gateway-host/service2)
This example demonstrates a basic setup for an API Gateway using Express.js and Istio. Adjust the code and configurations based on your specific requirements and service mesh preferences. Additionally, consider enhancing security, adding more features, and implementing service discovery as needed.

You can find the GitHub repository [here](https://github.com/ruvani/api-gateway-pattern-service-mesh).

# Conclusion
In conclusion, the adoption of the API Gateway pattern for microservices emerges as a pivotal strategy in enhancing the scalability, flexibility, and overall efficiency of modern software architectures. By centralizing the management of microservices through a dedicated gateway, organizations can streamline communication, enforce security measures, and simplify the integration of diverse services.

This pattern not only optimizes the development and maintenance processes but also facilitates a more agile and responsive system.

Thank you for reading !

# Learn More
## Implementing Feature Toggling in 2024
### Implementing feature flags with Bit and Bit Platform: A step-by-step guide
blog.bitsrc.io

## A Modern Approach to React Development
### Build composable and modernized React apps with Bit!
blog.bitsrc.io

## Monorepo, Poly-repo, or No Repo at all?
### Using Bit to make “irreversible decisions” easy to make and easy to change.
blog.bitsrc.io

## How to Share Code Between Micro Frontends
### Sharing context, functionality, and styles between micro frontends
blog.bitsrc.io