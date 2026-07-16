**Editor’s Note:** This article contains an exclusive excerpt from [*Latency*](https://www.manning.com/books/latency) by Pekka Engberg, which helps readers diagnose latency problems and master the low-latency techniques that have been predominantly “tribal knowledge” until now. You can [download three chapters for free](https://lp.scylladb.com/latency-book-offer) from ScyllaDB. And if you really want to geek out on latency, join the community at [P99 CONF (free and virtual)](https://www.p99conf.io/).

Asynchronous processing is a powerful technique for improving system concurrency and hiding latency in systems where further latency reduction is impractical or impossible. By performing I/O operations asynchronously and deferring noncritical work, you can significantly improve perceived responsiveness because end users don’t perceive the latency. Whereas techniques like partitioning, caching, and other latency optimizations can reduce absolute latency, asynchronous processing offers a complementary strategy—it hides latency by allowing the system to remain responsive even when [some operations take time](https://thenewstack.io/hpe-agentic-ai-ops-burnout/).

> “Asynchronous processing offers a complementary strategy—it hides latency by allowing the system to remain responsive even when some operations take time.”

In this article, we’ll explore the fundamental differences between synchronous and asynchronous processing, examine how the event loop enables efficient async execution, and investigate the key challenges and tradeoffs that async systems must address.

## Asynchronous vs. synchronous processing

*Asynchronous processing* enables tasks to execute independently and in overlapping periods, unlike synchronous processing, where tasks run in sequence. In other words, in a synchronous system, a task is executed to completion before the next one can begin. For example, suppose a single-threaded synchronous server is reading and processing messages. It first reads a message from a socket, which may require the thread to block until the message fully arrives. The server then processes the message, and it finally sends a response before starting to process the next message. If request processing takes a long time or blocks, the system waits synchronously.

Asynchronous processing removes this constraint, allowing multiple tasks to pro­gress simultaneously. For example, a server using asynchronous processing can process multiple independent requests concurrently by using I/O multiplexing, an operating system (OS) interface, to poll for the status of various connections. The server can then react to events, such as the socket becoming readable or writeable, to process a request. Similarly, the asynchronous server can initiate sending a response over the network and then work on other tasks without waiting for the response.

Asynchronous processing is similar to [concurrent programming](https://thenewstack.io/python-threadpool-vs-multiprocessing/). However, asynchronous processing differs from concurrent programming because it has explicit interfaces. For example, concurrent programming using threads allows a server to synchronously process a request while retaining concurrency by context-switching between threads. The server executes the `send()` and `recv()` system calls, which block if there’s nothing to read from a socket or the socket is not writeable. When the server blocks, the OS switches to another thread for concurrent execution. In contrast, with asynchronous processing, the server uses an I/O multiplexing interface to poll for socket state. The I/O multiplexing interface tells the server what sockets are readable, and the server can read from them without blocking the thread. Similarly, when the server sends a response, it uses an asynchronous interface to send the response, but it can then immediately continue work without blocking, letting the OS send the response in the background.

Figure 1 illustrates the difference between synchronous and asynchronous processing (which are also summarized in the sidebar titled “Differences between asynchronous, concurrent, and parallel processing”). In this example, we have two tasks, A and B, that must run to finish our work in full. Suppose a backend system needs to communicate with external systems A and B to complete a request it has received. In synchronous processing, each task must finish before the next one starts. We run task A until it is complete, including the I/O it submits, and then run task B. The total time needed is the time of all tasks added together. If a backend service needs to do all these tasks, users must wait for this total time to get their response.

![A timeline diagram comparing synchronous and asynchronous processing.](https://cdn.thenewstack.io/media/2026/07/88dc0a53-image1.png)

**Figure 1** Synchronous versus asynchronous processing. Synchronous processing (at the top) processes sequentially from one task to the next. In this example, we have tasks A and B, where A submits I/O. The I/O is executed synchronously before task B can execute. In contrast, asynchronous processing (at the bottom) can perform I/O in parallel with task B. That is, task A runs, submits the I/O, and immediately starts executing task B. When the I/O for task A and task B finishes, we’re done, completing the work faster than with synchronous processing.

However, in asynchronous processing, we can perform the I/O for task A simultaneously with task B, and we are finished when both of them are done. If the I/O runs simultaneously, the wait time is much shorter for users, even though each task still takes the same time. This works well in backend services when making database calls or calling other services because these tasks can run independently without blocking each other. But there’s a catch: if your I/O can’t run in parallel, using asynchronous processing won’t help but could instead make things run slower because managing async tasks adds extra work for the system.

|  |
| --- |
| **Differences between asynchronous, concurrent, and parallel processing**  *Concurrent processing* means executing tasks at the same time through multiplexing on the same compute unit, and *parallel processing* means executing tasks simultaneously on different compute units. While this distinction may seem subtle, the takeaway is that concurrent processing is about structuring applications in a way conducive to executing multiple things despite them potentially running sequentially on the same compute unit. *Parallel processing*, on the other hand, is about performing various things on different compute units, reducing execution time.  Although asynchronous processing is related to concurrent and parallel processing, it is fundamentally about structuring your code to handle tasks that might take time to complete. In other words, asynchronous processing can enable both concurrency and parallelism, but it doesn’t guarantee either. For example, you might write asynchronous code that runs concurrently on a single CPU core by switching between tasks, or you might have asynchronous code that runs in parallel across multiple cores. |

Asynchronous processing is also a critical technique for *hiding* latency. Some operations take a long time to complete, despite your best efforts to reduce latency, so it is essential to perform operations without everyone having to wait for them to complete. For example, backend systems typically interact with external systems like third-party services, database servers, and message queues, where each interaction adds some latency. With synchronous processing, you often build systems that don’t exploit the inherent parallelism available and that cause idle time where you’re waiting for systems to complete their work. In contrast, async processing allows you to minimize wait time by starting operations asynchronously and reacting when they are complete.

In synchronous processing, you structure your code as a sequence of operations that depend on each other. For example, a request processing function for a synchronous server might look something like the following.

### Listing 1 A simple example of a synchronous system

```

fn process_requests(socket: &amp;Socket) {
  loop {
    process_request(socket);
  }
}

fn process_request(socket: &amp;Socket) {
  let msg = socket.recv();
  let request = parse_message(msg);
  let resp = match request {
    Request::GetUserInfo(id) => get_user_info(id);    
  };
  let resp = format_response(resp);
  socket.send(resp);
}

```

At a high-level, we have the `process_requests` function, which processes any incoming requests from a socket. In the `process_request` function, each step is run to completion before we start another step. We read a message from the socket, we parse the message to determine what the request is, we process the request, and we finally send a response over the socket. More importantly, we don’t start another `process_request` until we’ve sent out a response, and we don’t allow requests to be processed from multiple sockets either.

While concurrency primitives like coroutines and futures enable parallel execution they’re insufficient for efficient asynchronous processing, particularly for I/O. You must structure the application differently if a server processes thousands of concurrent connections. The event loop is the foundation for efficiently multiplexing I/O operations across many connections.

## The event loop

The event loop is the central coordinator for all input and output operations—it’s at the heart of an asynchronous system. While traditional synchronous programs handle one connection at a time—like a single worker processing tasks in sequence—an event loop operates as a dispatcher, simultaneously managing thousands of I/O operations. This architectural pattern, sometimes called an I/O loop or I/O dispatcher, is how asynchronous processing handles concurrent operations efficiently. Instead of dedicating separate resources to each connection, the event loop multiplexes various I/O sources—network connections, file operations, timers, and more—by tracking their states and processing them when they’re ready.

> “The event loop is the central coordinator for all input and output operations—it’s at the heart of an asynchronous system.”

The event loop follows a simple yet powerful pattern:

1. Poll for events.
2. Process events.
3. Run scheduled tasks.
4. Repeat.

The event loop polls for events such as incoming data from a socket, an expired timer, or I/O completion by using OS-specific I/O multiplexing interfaces such as `io_uring` and `epoll` on Linux, `kqueue` on macOS, and IOCP on Windows. These interfaces let you register interest in an event source and get a notification when an event happens. For example, instead of reading data from a socket, the application expresses interest in a socket becoming readable. When data arrives from the network to the socket, the OS notifies the application, via the I/O multiplexing interface, that the socket is now readable. The event loop discovers this via polling and calls into the application’s event handling logic to process the newly arrived data from the socket.

Let’s implement a basic event loop in Rust to understand its structure better:

```

struct EventLoop {
    // Holds registered event sources like sockets, files, timers
    sources: Vec&lt;EventSource>,    
}

impl EventLoop {
    fn run(&amp;mut self) {
        loop {
            // Create a new collection to store events
            let mut events = Events::new();

            // Poll for new events with a timeout
            self.poll(&amp;mut events, Duration::from_millis(100));

            // Process each event that was found
            for event in events.iter() {
                self.process_event(&amp;event);
            }

            // Run any scheduled tasks
            self.run_scheduled_tasks();
        }
    }
}

```

The `EventLoop::run()` method demonstrates the core functionality of event-driven programming: continuously polling for and processing events. The `poll()` method uses an OS-specific I/O multiplexing interface, such as `io_uring`, for events on event sources. As you can see in the example code, we also specify a timeout for event polling. A timeout is needed because I/O polling in the event loop is often the only synchronous code that blocks the thread until an event happens. Polling can block if the system is idle and no events occur, and this blocking can reduce the wasted CPU cycles when there’s nothing to do. However, to ensure that the event loop does not block forever, the timeout ensures that we return from `poll()`. This allows the event loop to also perform work that is not conditional to an event, such as executing background work. However, in some cases, you might use busy-polling to avoid the sleep/wakeup cycle latency for some latency-sensitive event loops.

The `process_event` function is responsible for processing any events discovered during polling. For example, if the application registered interest in data arriving from the network (such as a socket becoming readable), the `process_event` function reads from the socket and forwards the data for the application to process. A simple `process_event` function might look something like this:

```

struct EventLoop {
    // Holds registered event sources like sockets, files, timers
    sources: Vec&lt;EventSource>,    
}

impl EventLoop {
    fn run(&amp;mut self) {
        loop {
            // Create a new collection to store events
            let mut events = Events::new();

            // Poll for new events with a timeout
            self.poll(&amp;mut events, Duration::from_millis(100));

            // Process each event that was found
            for event in events.iter() {
                self.process_event(&amp;event);
            }

            // Run any scheduled tasks
            self.run_scheduled_tasks();
        }
    }
}

```

As you can see, each event is represented by an `Event` enumeration with variants for different events. The event-processing logic is specific to how the event loop is structured. For example, if the event loop uses callbacks for event handling, it calls them, delegating work to the application. The application may then perform the work in the callback or submit the work to another thread for processing.

Figure 10.2 visualizes how the event loop performs work. In this example, work is split into three separate tasks:

1. Accept connection
2. Process request
3. Send response

![Diagram of the event loop broken down into three separate tasks.](https://cdn.thenewstack.io/media/2026/07/f917c16c-image2.png)

**Figure 2** The event loop breaks down work into individual tasks that execute when an event happens. In this example, the event loop processes three different tasks—accept connection, process request, and send response—as part of processing a request arriving from the network. Each task runs when an event, such as a socket becoming readable, happens.

The first task runs when the I/O multiplexer notifies the event loop that there is an incoming connection. The application reacts to the event by accepting the connection and then registering interest about when the accepted socket becomes readable. When data arrives from the network, the OS notifies the event loop that the socket is readable. The application reacts to this by reading from the socket and processing the incoming request. Finally, the application registers interest in the socket becoming writable. When the OS has enough buffer memory for an outgoing response, it notifies the application, which writes the response to the socket.

> “While the event loop is the low-level infrastructure for asynchronous processing, you’ll also need some concurrency primitives to specify dependencies between individual tasks.”

If you contrast the event loop to a synchronous server, which you saw in listing 1, you’ll see two key differences between these approaches:

* *Non-blocking operations*—The event loop does not block the thread, but instead registers interest in events such as a socket becoming readable, and it defers reading from the socket until that condition is true, handling other events meanwhile.
* *Resource efficiency*—A single thread running an event loop can handle thousands of concurrent connections because it does not need to wait for I/O operations to complete. Instead, the I/O multiplexing OS interface allows the event loop to poll for the status of multiple event sources, such as sockets, at the same time, performing event-based processing.

While the event loop is the low-level infrastructure for asynchronous processing, you’ll also need some concurrency primitives, like callbacks or futures to specify dependencies between individual tasks.

## Challenges

While asynchronous processing can significantly improve application performance, it comes with several important pitfalls to consider:

* *Complexity*—Asynchronous code is generally more complex than synchronous code. You need to carefully [manage task dependencies](https://thenewstack.io/unlocking-the-power-of-automatic-dependency-management/), handle errors across multiple operations, and deal with race conditions.
* *Resource management*—Running many tasks simultaneously can consume significant memory and system resources. You need to implement proper throttling and resource management.
* *Debuggability*—When something goes wrong in asynchronous code, it can be harder to track down the issue because the execution order isn’t always obvious, and stack traces might not tell the whole story.
* *Error handling*—With multiple operations running independently, error handling becomes more complex. You need to decide how failures in one task should affect other running tasks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/08/df1fe7ce-cropped-fe90b14b-pekka-enberg-.png)

Pekka Enberg is a software professional with a background and experience in operating systems, databases and distributed systems and a research interest in low-latency networked systems. In the past, Pekka has worked on the Linux kernel as a maintainer of...

Read more from Pekka Enberg](https://thenewstack.io/author/pekka-enberg/)