# Go & Kubernetes: Rapidly Developing Golang Microservices
![](https://cdn.sanity.io/images/rhzn5s2f/production/417d656c328108c96f5a69dc8ae1d9d000f92ac7-2316x3088.jpg?w=40&fit=max&auto=format)
![](https://cdn.sanity.io/images/rhzn5s2f/production/af7c417ea93bd3a822c5f4f4325cb66a204cd7b9-1200x627.jpg?w=1450&fit=max&auto=format)
[Step 1: Deploy a Sample Microservices Application](/blog/go-kubernetes-developing-golang-microservices#body__f50859018ba3) [Step 2: Set up your local Go development environment](/blog/go-kubernetes-developing-golang-microservices#body__a5cd1012faff) [Step 3: Rapid Development with Telepresence](/blog/go-kubernetes-developing-golang-microservices#body__246ca87533aa) [Step 4: Intercept Your Golang Service](/blog/go-kubernetes-developing-golang-microservices#body__73621e2b869e) [Learn More about Telepresence](/blog/go-kubernetes-developing-golang-microservices#body__dbd3049d49ae)
### Build a cloud development environment with Telepresence & Golang
[Kubernetes](/blog/kubernetes-tutorial-beginners-guide) is a container orchestration platform that enables its users to deploy and scale their microservice applications at any scale, from one service to thousands of services. However, unleashing the power of Kubernetes is often more complicated than it may initially seem; the learning curve for application developers is particularly steep. Knowing what to do is just half the battle; then, you have to choose the best tools for the job. So, how do [Go](/docs/telepresence-oss/latest/quick-start/go/) developers create a development workflow on Kubernetes that is fast and effective?
## Build a cloud development environment with Golang & Telepresence
Application developers face two unique challenges when trying to create
[productive development workflows on Kubernetes](/use-case/productive-local-dev-environment):
- Most development workflows are optimized for local development, whereas Kubernetes applications are designed to be cloud-native.
- As Kubernetes applications evolve into complex
[microservice](/kubernetes-glossary/microservices)architectures, the development environments also become more complex. Every microservice adds additional dependencies, and these services quickly start to require more resources than are typically available in a l [ocal development environment](/blog/kubernetes-dev-environments-local-remote).
In this tutorial, weâll set up a development environment for Kubernetes and make a change to a
[Golang](/blog/debug-go-microservices-kubernetes-vscode) microservice. Normally, to develop locally, weâd have to wait for a container build, push it to a registry, and deploy it to see the effect of our code change. Instead, weâll use Telepresence to see the results of our change instantly.
## Step 1: Deploy a Sample Microservices Application
For our example, we'll make code changes to a Go service that operates between a resource-intensive Java service and a large datastore. We'll begin by deploying a sample microservice application consisting of 3 services:
**VeryLargeJavaService:**A memory-intensive service written in Java, responsible for generating the front-end graphics and web pages for our application. **DataProcessingService:**A Golang service that manages requests for information between the VeryLargeJavaService and the VeryLargeDataStore. **VeryLargeDataStore:**A large datastore service that contains the sample data for our Edgey Corp store. **Note: **The 'VeryLarge' descriptor is used to emphasize that your local environment may not have sufficient CPU and RAM to handle these services, or you may prefer not to incur the additional overhead costs for every developer. ![Go & Kubernetes](https://cdn.sanity.io/images/rhzn5s2f/production/47ee441979ac21d300f15159776bab3e411c2179-1400x1040.jpg?w=1920&fit=max&auto=format)
In this architecture diagram, you'll notice that requests from users are routed through an ingress controller to our services. For simplicity's sake, in this tutorial, we'll skip
[deploying an ingress controller](/docs/edge-stack/latest/tutorials/getting-started#kubernetes-yaml/). If you're ready to use Telepresence in your own setup and are looking for a simple way to set up an ingress controller, we recommend checking out the [Edge Stack API Gateway](/products/edge-stack/api-gateway). **Letâs deploy the sample application to your Kubernetes cluster:**
kubectl apply -f
## Step 2: Set up your local Go development environment
Weâll need a local development environment so that we can edit the `DataProcessingService` service. As you can see in the architecture diagram above, the `DataProcessingService` is dependent on both the `VeryLargeJavaService` and the `VeryLargeDataStore`, so in order to make a change to this service, weâll have to interact with these other services as well. Letâs get started!
**1. Clone the repository for this application from GitHub.**
git clone https://github.com/datawire/edgey-corp-go.git
**2. Change directories into the DataProcessingService**
cd edgey-corp-go/DataProcessingService
**3. Start the Go server:**
go build main.go && ./main
**4. See your service running!**
10:23:41 app | Welcome to the DataProcessingGoService!
**5. In another terminal window, curl localhost:3000/color to see that the service is returning blue.**
$ curl localhost:3000/color
âBlueâ
## Step 3: Rapid Development with Telepresence
Instead of waiting for a container image to be built, pushed to a repository, and deployed to our Kubernetes cluster, we are going to use Telepresence.
[Telepresence](/products/telepresence) creates a bidirectional network connection between your local development environment and the Kubernetes cluster to enable [fast, efficient development](/use-case/productive-local-dev-environment).
# Mac OS Xsudo curl -fL https://app.getambassador.io/download/tel2/darwin/amd64/latest/telepresence -o /usr/local/bin/telepresence#Linuxsudo curl -fL https://app.getambassador.io/download/tel2/linux/amd64/latest/telepresence -o /usr/local/bin/telepresence
**2. Make the binary executable**
$ sudo chmod a+x /usr/local/bin/telepresence
**3. Test Telepresence by connecting to the remote cluster**
$ telepresence connect
**4. Send a request to the Kubernetes API server:**
$ curl -ik https://kubernetes.default.svc.cluster.localHTTP/1.1 401 UnauthorizedCache-Control: no-cache, privateContent-Type: application/jsonWww-Authenticate: Basic realm="kubernetes-master"Date: Tue, 09 Feb 2021 23:21:51 GMT
Great! Youâve successfully configured Telepresence. Right now, Telepresence is
[intercepting](/docs/telepresence/latest/reference/intercepts/) the request youâre making to the Kubernetes API server, and routing over its direct connection to the cluster instead of over the Internet.
## Step 4: Intercept Your Golang Service
An
[intercept](/docs/telepresence/latest/concepts/intercepts/) is a routing rule for Telepresence. By creating an intercept, we can route traffic intended for the **DataProcessingService** in the cluster to the *local* version of the **DataProcessingService** running on port 3000 instead. **Create the intercept**
telepresence intercept dataprocessingservice â port 3000
**Access the application directly with Telepresence.**Visit http://verylargejavaservice:8080. Again, Telepresence is intercepting requests from your browser and routing them directly to the Kubernetes cluster. **Now, weâll make a code chang**e. Open edgey-corp-go/DataProcessingService/main.go and change the value of the color variable from blue to orange. Save the file, stop the previous server instance and start it again with go build main.go && ./main. **Reload the page in your browser and see how the color has changed from blue to orange!**
Thatâs it! With Telepresence, we've seen how quickly we can transition from editing a local service to observing how these changes integrate with the larger application. Compared to the original process of building and deploying a container after every change, the time savings become increasingly apparent, especially as we make more complex changes or manage even larger services.
## Learn More about Telepresence
Today, weâve explored using
[Telepresence](/products/telepresence) to rapidly iterate on a Golang microservice running in Kubernetes. Now, instead of being bogged down by slow local development processes, we can iterate swiftly, benefiting from an instant feedback loop and a productive cloud-native development environment.