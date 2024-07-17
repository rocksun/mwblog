# Terminating Elegantly: A Guide to Graceful Shutdowns
**Read the original article on packagemain.tech**
Have you ever yanked the power cord out of your computer in frustration? While this might seem like a quick solution, it can lead to data loss and system instability. In the world of software, a similar concept exists: the hard shutdown. This abrupt termination can cause problems just like its physical counterpart. Thankfully, there’s a better way: the graceful shutdown.

By integrating graceful shutdown, we provide advance notification to the service. This enables it to complete ongoing requests, potentially save state information to disk, and ultimately avoid data corruption during shutdown.

This guide will delve into the world of graceful shutdowns, specifically focusing on their implementation in Go applications running on Kubernetes.

# Signals in Unix Systems
One of the key tools for achieving graceful shutdowns in Unix-based systems is the concept of signals, which are, in simple terms, a simple way to communicate one specific thing to a process, from another process. By understanding how signals work, we can leverage them to implement controlled termination procedures within our applications, ensuring a smooth and data-safe shutdown process.

There are many signals, and you can find them [ here](https://en.wikipedia.org/wiki/Signal_(IPC)), but our concern is only shutdown signals:

**SIGTERM**— sent to a process to request its termination. Most commonly used, and we’ll be focusing on it later.**SIGKILL**— “quit immediately”, can not be interfered with.**SIGINT**— interrupt signal (such as Ctrl+C)**SIGQUIT**— quit signal (such as Ctrl+D)
These signals can be sent from the user (Ctrl+C / Ctrl+D), from another program/process or from the system itself (kernel / OS), for example a **SIGSEGV** aka segmentation fault is sent by the OS.

# Our Guinea Pig Service
To explore the world of graceful shutdowns in a practical setting, let’s create a simple service we can experiment with. This “guinea pig” service will have a single endpoint that simulates some real-world work (we’ll add a slight delay) by calling Redis’s [INCR](https://redis.io/docs/latest/commands/incr/) command. We’ll also provide a basic Kubernetes configuration to test how the platform handles termination signals.

The ultimate goal: ensure our service gracefully handles shutdowns without losing any requests/data. By comparing the number of requests sent in parallel with the final counter value in Redis, we’ll be able to verify if our graceful shutdown implementation is successful.

We won’t go into details of setting up the Kubernetes cluster and Redis, but you can find the [ full setup in our Github repository](https://github.com/plutov/packagemain/tree/master/graceful-shutdown).

The verification process is the following:

- Deploy Redis and Go application to Kubernetes.
- Use
to send 1000 requests (25/s over 40 seconds).**vegeta** - While vegeta is running, initialize a Kubernetes
by updating image tag.**Rolling Update** - Connect to Redis to verify the “counter“, it should be 1000.
Let’s start with our base Go HTTP Server.

hard-shutdown/main.go
`package main`
import (
"net/http"
"os"
"time"
"github.com/go-redis/redis"
)
func main() {
redisdb := redis.NewClient(&redis.Options{
Addr: os.Getenv("REDIS_ADDR"),
})
server := http.Server{
Addr: ":8080",
}
http.HandleFunc("/incr", func(w http.ResponseWriter, r *http.Request) {
go processRequest(redisdb)
w.WriteHeader(http.StatusOK)
})
server.ListenAndServe()
}
func processRequest(redisdb *redis.Client) {
// simulate some business logic here
time.Sleep(time.Second * 5)
redisdb.Incr("counter")
}
When we run our verification procedure using this code we’ll see that some requests fail and the **counter is less than 1000 **(the number may vary each run).

Which clearly means that we lost some data during the rolling update. 😢

# Handling Signals in Go
Go provides a [signal](https://pkg.go.dev/os/signal) package that allows you to handle Unix Signals. It’s important to note that by default, SIGINT and SIGTERM signals cause the Go program to exit. And in order for our Go application not to exit so abruptly, we need to handle incoming signals.

There are two options to do so.

Using channel:
`c := make(chan os.Signal, 1)`
signal.Notify(c, syscall.SIGTERM)
Using context (preferred approach nowadays):
`ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM)`
defer stop()
**NotifyContext** returns a copy of the parent context that is marked done (its Done channel is closed) when one of the listed signals arrives, when the returned **stop()** function is called, or when the parent context’s Done channel is closed, whichever happens first.
There are few problems with our current implementation of HTTP Server:

- We have a slow processRequest goroutine, and since we don’t handle the termination signal, the program exits automatically, meaning all running goroutines are terminated as well.
- The program doesn’t close any connections.
Let’s rewrite it.

graceful-shutdown/main.go
`package main`
// imports
var wg sync.WaitGroup
func main() {
ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM)
defer stop()
// redisdb, server
http.HandleFunc("/incr", func(w http.ResponseWriter, r *http.Request) {
wg.Add(1)
go processRequest(redisdb)
w.WriteHeader(http.StatusOK)
})
// make it a goroutine
go server.ListenAndServe()
// listen for the interrupt signal
<-ctx.Done()
// stop the server
if err := server.Shutdown(context.Background()); err != nil {
log.Fatalf("could not shutdown: %v\n", err)
}
// wait for all goroutines to finish
wg.Wait()
// close redis connection
redisdb.Close()
os.Exit(0)
}
func processRequest(redisdb *redis.Client) {
defer wg.Done()
// simulate some business logic here
time.Sleep(time.Second * 5)
redisdb.Incr("counter")
}
Here’s the summary of updates:

- Added
**signal.NotifyContext**to listen for the SIGTERM termination signal. - Introduced a
**sync.WaitGroup**to track in-flight requests (processRequest goroutines). - Wrapped the server in a goroutine and used
**server.Shutdown**with context to gracefully stop accepting new connections. - Used
**wg.Wait()**to ensure all in-flight requests (processRequest goroutines) finish before proceeding. - Resource Cleanup: Added
**redisdb.Close()**to properly close the Redis connection before exiting. - Clean Exit: Used
**os.Exit(0)**to indicate a successful termination.
Now, if we repeat our verification process we will see that all 1000 requests are processed correctly. 🎉

# Web frameworks / HTTP library
Frameworks like Echo, Gin, Fiber and others will spawn a goroutine for each incoming requests, giving it a context and then call your function / handler depending on the routing you decided. In our case it would be the anonymous function given to HandleFunc for the “/incr” path.

When you intercept a **SIGTERM** signals and ask your framework to gracefully shutdown, 2 important things happen (to oversimplify):

- Your framework stop accepting incoming requests
- It waits for any existing incoming requests to finish (implicitly waiting for the goroutines to end).
*Note: Kubernetes also stop directing incoming traffic from the loadbalancer to your pod once it has labelled it as Terminating.*
# Optional: Shutdown Timeout
Terminating a process can be complex, especially if there are many steps involved like closing connections. To ensure things run smoothly, you can set a timeout. This timeout acts as a safety net, gracefully exiting the process if it takes longer than expected.

`shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)`
defer cancel()
go func() {
if err := server.Shutdown(shutdownCtx); err != nil {
log.Fatalf("could not shutdown: %v\n", err)
}
}()
select {
case <-shutdownCtx.Done():
if shutdownCtx.Err() == context.DeadlineExceeded {
log.Fatalln("timeout exceeded, forcing shutdown")
}
os.Exit(0)
}
# Kubernetes Termination Lifecycle
Since we used Kubernetes to deploy our service, let’s dive deeper into how it terminates the pods. Once Kubernetes decides to terminate the pod, the following events will take place:

- Pod is set to the “Terminating” State and removed from the endpoints list of all Services.
**preStop**Hook is executed if defined.**SIGTERM**signal is sent to the pod. But hey, now our application knows what to do!- Kubernetes waits for a grace period (
**terminationGracePeriodSeconds**), which is 30s by default. **SIGKILL**signal is sent to pod, and the pod is removed.
As you can see, if you have a long-running termination process, it may be necessary to increase the **terminationGracePeriodSeconds **setting**,** allowing your application enough time to shut down gracefully.

# Conclusion
Graceful shutdowns safeguard data integrity, maintain a seamless user experience, and optimize resource management. With its rich standard library and emphasis on concurrency, Go empowers developers to effortlessly integrate graceful shutdown practices — a necessity for applications deployed in containerized or orchestrated environments like Kubernetes.

You can find the Go code and Kubernetes manifests in [our Github repository](https://github.com/plutov/packagemain/tree/master/graceful-shutdown).