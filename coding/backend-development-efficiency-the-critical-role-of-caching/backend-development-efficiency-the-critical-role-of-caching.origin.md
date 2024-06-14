# Backend Development Efficiency: The Critical Role of Caching
![Featued image for: Backend Development Efficiency: The Critical Role of Caching](https://cdn.thenewstack.io/media/2024/06/8b5e4e0a-caching-1024x576.jpg)
Undoubtedly, many of us have experienced the frustration of completing a project only to find that our application could be better in fetching data from the backend. This not only hampers our application’s efficiency, but also drives users away, forcing them to seek alternatives. Consequently, a brilliant application idea can become unreliable and unusable. But there is a solution to address these challenges.
Caching is the key to
[enhancing application performance](https://thenewstack.io/why-http-caching-matters-for-apis/). When implemented effectively, it can significantly elevate the user experience by streamlining performance. Let’s explore the fundamentals of caching.
In essence, caching involves temporarily storing data retrieved from the database. When subsequent requests for the same data occur, rather than waiting for the API to retrieve it again, the backend application seamlessly delivers the cached data.
I’ll illustrate this concept using a comprehensive stack comprising Nest.js, Redis, Redis-commander, npm, Docker and Postman. Nest.js, a robust backend framework built on Node.js and leveraging
[TypeScript](https://thenewstack.io/typescript-vs-javascript/), will serve as our foundation. Redis, renowned for its high-speed performance, will act as our cache database, while npm facilitates package management. Docker will enable us to containerize the Redis database, enhancing scalability and deployment efficiency. Additionally, Redis-commander will provide a user-friendly interface for monitoring our cache database. Lastly, Postman, a versatile tool for [API testing](https://thenewstack.io/api-management/) and request handling, will play a pivotal role.
First, open the terminal and use the Nest CLI to create a new Nest.js application. Once the application has been successfully scaffolded, navigate to the project folder and open it using VS Code or any other preferred code editor.
Next, install a few packages that will assist us in achieving our objective. It’s important to note that we won’t be using in-memory caching, a technique offered by many backend frameworks. While in-memory caching has its advantages, such as speed, it also has notable downsides. The most significant one is that data is stored in RAM, which may not be ideal, especially if your server or hosting machine has limited resources.
In the code editor, we’ll open a new terminal and install dependencies by running the following commands.
To begin, we’ll navigate to the
src folder and open the
app.module.ts file, then import and register the
CacheModule. Additionally, we’ll configure the module by passing an object of parameters. These parameters will enable our application to connect with the Redis database, which we’ll Dockerize later.
As evident in the
app.module.ts file, the
CacheModule has been successfully imported and registered. Furthermore, we’ve initialized an object of parameters to configure our cache-store. These parameters include:
store: Defines the cache store to be used.
host: Specifies the server where our Redis database will be running.
port: Indicates the port through which Redis will be accessed.
usernameand
password: Left empty for our purposes.
- Other notable properties, such as
ttl(time to live), which determines the duration data is cached in the database, may be added if required. However, for the scope of this article, we won’t include it as it’s not critical to our demonstration.
To interact with the cache database, we need to inject the
CACHE_MANAGER instance into our controller. This instance serves as the intermediary for communication between our application controller and the cache database, hence the need to perform the check at the controller level. If the data already exists in the cache database, the service is not involved in the process.
Following the injection of the cache manager, we’ve defined a function named
getSampleData within the controller. This function is responsible for returning an object containing properties such as
id (string),
items (array of numbers) and
users (array of strings). Internally, this function calls another method,
getSampleData,which resides within the
AppService class defined in the
app.service.ts file.
Additionally, we’ve injected the
AppService into the controller, granting access to its members. The route for our controller has been configured to
/api/test/cache, serving as the endpoint for testing our caching configuration.
Now, let’s dive into the exciting part! The
cache_manager offers a variety of methods, but we’ll focus on four or five of them.
First, we have the
get(key) method, which accepts a key as input, retrieves the corresponding data from the cache database and returns it.
Next up is the
set(key, value) method. Unlike
get, this method takes both a key and a value as parameters and stores them in the cache database.
Moving on, we have the
del(key) method. When invoked, this function deletes the data associated with the specified key from the cache database.
Lastly, let’s explore the
reset() method. This powerful function wipes the entire cache database clean, leaving it empty and ready for new data.
With these methods at our disposal, we’re equipped to effectively manage our cache database and optimize our application’s performance. Armed with the understanding of the aforementioned functions, let’s enhance our
getSampleData function within the controller. When a request is received, the controller will first check the cache database. If cached data exists, the controller will promptly return it to the user, without the need to invoke the service. However, if no cached data is found, the controller will call the service to fetch the data. Once the data is retrieved, it will be cached for future requests before being returned to the user. This approach optimizes performance by minimizing unnecessary calls to the service.
Here’s a refined explanation of the changes made to our controller:
We’ve transformed the
getSampleData function into an asynchronous function, indicating that it returns a
[promise](https://thenewstack.io/what-are-promises-in-javascript/). Consequently, the function’s return type has been updated to a promise that resolves to an object with predefined properties.
Upon receiving a request, the controller first checks if there is cached data corresponding to the key ‘UD’. If such data exists (checked with
if (cachedData)), it is returned to the user as a JSON response.
In the event that no cached data is found, the controller proceeds to call the
getSampleData method of the
AppService. Upon retrieval of the data, it is converted to a string and stored in the cache database with the key ‘UD’ using
this.cacheManager.set('UD', JSON.stringify(fetchedSampleData)). Subsequently, the data is returned to the user.
To ensure seamless execution, the
getSampleData function in the
app.service.ts module has also been modified to be asynchronous. This enables the use of the
await keyword when invoking the function in the controller, preventing any issues with undefined values.
The next step involves creating a
docker-compose.yml file. This file will facilitate the pulling of Redis and Redis-commander images, enabling us to
[run the containers](https://thenewstack.io/containerds-important-role-for-nvidias-gpu-operator-and-ai-accelerated-cloud/) effortlessly. With Docker Compose, we’ll define the services required for our project, including Redis for our cache database and Redis-commander for a user-friendly interface. Once configured, Docker Compose will orchestrate the setup, ensuring the containers are up and running seamlessly.
To provide a concise overview, the
version directive, set to ‘3.8’, denotes the version of the Docker Compose file format in use. Subsequently, we define the services to be executed, namely Redis and Redis-commander. Each service is associated with an image that Docker will retrieve to instantiate the respective containers.
Regarding the
Ports configuration, it specifies the ports on which the containers will operate. These ports are then mapped to enable external access.
To elaborate on specific variables within the
redis-commander service, the
environment variable aids in specifying the location of Redis for the Redis-commander to connect to. Additionally, the
container_name attribute designates the name of the container, while
hostname denotes the hostname assigned to the container. Although container name and hostname are somewhat self-explanatory, they are essential components of container management. Now, we return to the terminal to execute the Docker Compose file, initiating the build and startup processes for our services. Before running the command below, please ensure that you have Docker Desktop installed on your system. If not, you can download it from the
[official Docker website](https://www.docker.com/products/docker-desktop/). Otherwise, attempting to execute the command without Docker Desktop installed will result in an error.
With both containers running smoothly and without errors, we can proceed to open Postman. From there, we’ll commence sending requests to witness caching in action firsthand. Additionally, we’ll navigate to
http://127.0.0.1:8081 to access the Redis-commander interface. This interface will allow us to monitor and manage the contents of our Redis database, providing valuable insights into its operations.
Certainly, achieving a response time of 52 milliseconds for an API is quite satisfactory. Upon verifying our Redis-commander, we can confirm the successful preservation of our data under the “UD” key. Now, let’s explore the prowess of caching by initiating another request. This will enable us to directly witness how caching optimizes response times, thereby enhancing the overall efficiency of our application.
And there you have it! Thanks to the magic of caching, our API response time has plummeted to a mere 9ms. That’s not even half the time it took during the initial request to return a response. This underscores the indispensable role caching plays in backend development.
Caching isn’t just a technique; it’s a game-changer. It dramatically enhances performance, elevates user experience and optimizes resource utilization. By intelligently storing frequently accessed data, caching minimizes redundant computations and database queries, resulting in lightning-fast responses and smoother user interactions.
In the dynamic world of web development, where speed is paramount and user expectations are ever-increasing, caching emerges as a beacon of efficiency. In conclusion, our journey through the realm of caching has illuminated its transformative power in optimizing back end performance. From significantly reducing API response times to enhancing overall user experience, caching emerges as a cornerstone technique in modern web development.
By intelligently storing and retrieving data, caching minimizes computational overhead and database load, resulting in faster and more responsive applications. Through our exploration, we’ve witnessed firsthand how caching can revolutionize application performance, ensuring smoother user interactions and heightened efficiency.
As we navigate the ever-evolving landscape of web development, it’s clear that caching remains a vital tool in our arsenal. Its ability to streamline operations, boost scalability and elevate application reliability underscores its status as a foundational pillar of backend architecture.
In our pursuit of excellence, let’s embrace caching as a fundamental principle, harnessing its capabilities to craft exceptional digital experiences that leave a lasting impression on users. Together, let’s continue to unlock the full potential of caching and propel our applications to new heights of performance and innovation.
Interested in finding out more about how to navigate your data? Data-driven organizations can outperform their competitors by 6% in profitability and 5% in productivity. What does it mean to be data-driven? And how can you navigate data as a leader?
[Check out our guide](https://www.andela.com/resources/navigating-data-driven-leadership?utm_medium=contentmarketing&utm_source=ebook&utm_campaign=client-global-2024-06-13-thenewstack&utm_content=data-driven%20guide&utm_term=ebook). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)