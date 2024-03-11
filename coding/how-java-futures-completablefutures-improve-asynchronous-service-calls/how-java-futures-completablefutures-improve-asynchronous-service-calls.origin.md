# How Java Futures, CompletableFutures Improve Asynchronous Service Calls
![Featued image for: How Java Futures, CompletableFutures Improve Asynchronous Service Calls](https://cdn.thenewstack.io/media/2024/03/2f10bcd3-service-calls-2-1024x576.jpg)
Distributed programming at the enterprise level can be a daunting undertaking. Unlike applications that use resources readily available within the scope of a single local computing environment, distributed applications, by definition, use services placed at external locations. Sometimes these external services run on another computer in close proximity; other times the services are running in the cloud, on machines that could be anywhere.
The implication is that calls to these services are unpredictable in terms of response. A call might execute within an expected number of milliseconds. Or in worst-case scenarios, a call could take minutes, maybe hours. Thus, writing blocking code that simply waits around for an external call to complete is bad business, particularly when an application might make hundreds of external calls during its operation.
The better solution is to use a technology that enables writing non-blocking code that makes the external call asynchronously, only to be notified later on when the call completes. Colloquially, this technique can be thought of as “fire and let me know later on.”
Under
[Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/), the technology that enables this sort of asynchronous interaction is called a Future, which is the topic of this article.
I am going to provide a short overview of the Java Future interface and CompletableFuture class that implements the interface. I’ll demonstrate the non-blocking nature of a Future, and then show how to create a chain of non-blocking code using a set of CompletableFutures. Finally, I’ll demonstrate how to run a set of non-blocking CompletableFutures in parallel.
This article is also accompanied by
[a repository on GitHub that has all the demonstration code](https://github.com/reselbob/SimpleFuturesDemo) along with instructions about how to run it.
The use case I will demonstrate in the three examples is a travel scenario that makes airline, hotel and car rental reservations. The first and second examples make the reservations in sequence. The third example makes the reservations simultaneously. But, before I dive into the details, I’ll explain the basics of the Java Future interface and the CompletableFuture class that implements the interface.
In order to get full benefit from reading this article, it’s useful to have some experience
[programming in Java](https://thenewstack.io/java-adapts-to-cloud-native-computing/) and a basic understanding of [Java threads](https://thenewstack.io/why-debugging-doesnt-need-to-be-so-complex-or-outdated/).
## Futures and CompletableFutures 101
A
[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) is a Java interface that defines the following methods:
|
Return type |
Method name |
Description
|boolean
|cancel(boolean mayInterruptIfRunning)
|Attempts to cancel the future, returns true on success.
|V, the type of the result
|get()
|Waits for the asynchronous code to complete then returns a result.
|V, the type of the result
|get(long timeout, TimeUnit unit))
|Waits only for the time period defined by the timeout parameter.
|boolean
|isCancelled()
|Attempts to cancel the execution of the asynchronous code, returns true on success.
|boolean
|isDone()
|Returns true when the asynchronous code completes.
The benefit a
Future provides is that the methods specified by the interface make working with asynchronous code easier. For example, if you want to know if an instance of the Future is still running, you call the
isDone() method. If you want to get the result of an instance of a Future running asynchronous code, you call the
get() method. Things are more apparent. You don’t have to fiddle with the thread underlying the
Future. You just work with the
Future.
A
is a Java class that implements the methods specified in the
[CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)
Future interface but also has many additional methods that add more power and versatility for programming asynchronous code. As the following demonstration examples demonstrate, the
CompletableFuture class enables
Futures to be chained as well as run in parallel.
The details of coding using
Futures and
CompletableFutures are shown in the three examples that follow. As mentioned previously, all three examples emulate a travel scenario that makes airline, hotel and car rental reservations on behalf of a user. The code that defines a reservation is described in a class named
Reservation, as illustrated in Listing 1.
**Listing 1:** The
Reservation class contains waiting logic that is used by all reservations.
Notice that the
Reservation class, which is used by all instances of a reservation, has a method named
makeReservation(String travelService).
makeReservation(String travelService) has a
Thread.sleep() statement (Listing 1, Line 3) that emulates the period of time it takes to make a reservation.
makeReservation(String travelService) is called asynchronously on the airline, hotel and car rental instances of the
Reservation class. The situation in which these calls are made will vary by use case.
Let’s take a look at the first use case that runs
Reservation.makeReservation(String travelService) as a set of
Futures in sequence.
## Running Futures in a Sequence
This section describes running the airline, hotel and car rental reservations in sequence. Each reservation is represented as a
Future.
![](https://cdn.thenewstack.io/media/2024/03/cd63d425-java-graphic-1-573x1024.png)
**Figure 1:** Executing a set of
Futures in sequence.
The logic for programming the sequence of Futures is shown as code, in Listing 2 below. In addition, the code also has logic that checks a running Future to see if it is “done.” Take a moment to review the code in Listing 2. Then I’ll discuss some of the more interesting details.
**Listing 2:** The code to run Futures in sequence.
As mentioned previously, the code in Listing 2 creates airline, hotel and car rental reservations. Each reservation runs in a dedicated Future. A given Future runs within a thread provided by an instance of an ExecutorService created at Line 7 in Listing 2.
The first
Future, which is for the airline reservation, is created at Line 10 by way of the
Executor.submit() method.
Executor.submit() takes as a parameter a lambda expression that encapsulates the creation of a
Reservation object that calls the instance’s
makeReservation() method.
Executor.submit() returns a reference to
Future for the airline reservation.
The airline reservation
Future named
airlineFuture is now running.
The code at Line 13 creates a
while loop that runs until the
airlineFuture.isDone() returns true. The purpose of running the while loop is to demonstrate how
Future.isDone() works,
Notice that the code in the while loop calls
Thread.sleep(300) at Line 15. The call to
Thread.sleep() delays the execution of the
while loop for one-third of a second. Going back to Listing 1 at the beginning of this article, recall that a reservation takes one second to run. Hence, the overall logic in play is that the while loop will run four times before the reservation completes. This demonstrates the power of using
Future.isDone().
Future.isDone() provides an easy way to inspect the state of a running
Future.
Take a look at Listing 3 below, which shows the console output of the code running in Listing 2. The four lines of output from the
while loop running
airlineFuture.isDone() provides evidence of the logic described in the code listing above.
Also, go back to Listing 2 above and notice the call to
airlineFuture.get() at Line 18. The call to
airlineFuture.get() returns the result of the asynchronously running
Future once it completes. The return from the call to
airlineFuture.get() shown in Listing 3 below is
*Result: Airline is confirmed at 2024-02-27 08:20:37*.
Notice the time of the return from
airlineFuture.get() is 2024-02-27 08:20:37, yet the four calls to
airlineFuture.isDone() happen in the second before 08:20:37. This is further evidence that a call to
Future.isDone() will inspect the Future even though it’s running asynchronously to the calling thread.
**Listing 3:** The output from running the Futures in sequence.
The code for making hotel and car rental reservations, shown at Lines 20-44 in Listing 2, is similar to the code for making the airline reservation. Also, the output is similar, as displayed in Listing 3.
The important thing to understand about this demonstration is that the method
Future.isDone() provides a way to inspect the state of a running
Future and that a call to method
Future.get() will return the result of a
Future once it completes, and thus provides a way to run a set of
Futures in sequence.
However, there is another way to run
Futures in sequence. The other way is by using enhancements provided by the class
CompletableFuture to implement a technique called chaining.
## Chained CompletableFutures
Chaining
Futures is a technique in which a series of
Futures run in sequence automatically without needing to call the
.get() method of each
Future. Also, if the originating
Future returns a result, that result is passed to the subsequent
Future automatically.
Figure 2 shows the basic concept behind chaining
Futures using the
CompletableFuture class. One of the benefits of chaining
Futures using the
CompletableFuture class is that a developer can run tasks synchronously or asynchronously within the chain.
![](https://cdn.thenewstack.io/media/2024/03/3ef7df44-java-graphic-2-1024x503.png)
**Figure 2:** Running a sequence of
CompletableFutures in a chain.
In the demonstration example, chaining a set of Futures involves using a few of the many
[methods provided by the CompletableFuture class](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html#method.summary). The methods used in the example are shown in the table below.
|
Method |
Description
|.supplyAsync(lambda)
|Starts the chain by running a method encapsulated by a lambda expression asynchronously.
|.thenAccept(result)
|Synchronously processes the result of the method run previously in the chain.
|.thenApplyAsync(lambda)
|Continues the chain by asynchronously running a method encapsulated by a lambda expression.
Take a moment to review the code in Listing 4 below. Then, I’ll discuss some interesting details about using a
CompletableFuture to run
Futures sequentially within a chain.
**Listing 4:** The Java code for running a set of CompletableFuture<T> in a chained sequence.
The way the chain shown above in Listing 4 works is that a travel reservation, in this case the airline reservation, is executed asynchronously using the static
CompletableFuture.supplyAsync() method.
CompletableFuture.supplyAsync() creates an instance of a
CompletableFuture implicitly.
Also, the method takes two parameters, a lambda expression that contains the method to run asynchronously and an instance of an
ExecutorService that will provide the thread in which the implicit CompletableFuture runs. In Listing 4, Lines 7-15, calling
CompletableFuture.supplyAsync() starts the chain, which continues to run using a series of “then” statements.
The first “then” statement at Line 16 is
.thenAccept().
.thenAccept() runs code synchronously, accepting the result of the previously run
CompletableFuture. The value returned by the previous
CompletableFuture is a confirmation message of type
String.
Since outputting the confirmation message will have a minor impact as blocking code, using
.thenAccept() is appropriate. However, the next behavior in the chain is a hotel reservation, which needs to be run asynchronously. Thus, the next “then” clause is .
thenApplyAsync(), which also accepts a lambda expression and an instance of an
ExecutorService. (See Listing 4, Lines 20-28.)
.thenApplyAsync() creates an implicit
CompletableFuture.
A synchronous
.thenAccept() clause follows to process the confirmation message from the
CompletableFuture handling the hotel reservation. Finally, another
.thenApplyAsync() clause is executed to handle the car rental reservation.
Listing 5 below shows the output from the chain. Notice that the airline, hotel and car rental confirmation output is reported at one-second intervals. This is because it takes a reservation one second to execute (as shown in Listing 1). The output in Listing 5 illustrates that the airline, hotel and car rental are executing and completing in sequence, as is to be expected by a chain of
CompletableFutures.
**Listing 5:** The terminal output from running a set of
CompletableFuture<T> in a chained sequence.
The examples demonstrate the airline, hotel and car rental reservations running in sequence. However, another viable use case is one in which execution of all reservations start at the same time and run in parallel. Coding such a use case could be a difficult undertaking. Fortunately, the
CompletableFuture class makes running asynchronous code in parallel easier.
## Parallel CompletableFutures
Figure 3 is a diagram of a use case in which airline, hotel and car rental reservations run in parallel as
CompletableFutures.
![](https://cdn.thenewstack.io/media/2024/03/81e1ec33-java-graphic-3-1024x453.png)
Figure 3: Running a set of CompletableFutures in parallel.
The code in Listing 6 demonstrates a set of CompletableFutures that run in parallel. Take a moment to look at the code. Then I’ll discuss the key aspects in detail.
**Listing 6:** The Java code for running a set of CompletableFigure<T> in parallel.
The first thing to notice is that the code in Listing 6 uses a new custom class for a reservation named
. The class
[TimedReservation](https://github.com/reselbob/SimpleFuturesDemo/blob/main/src/main/java/futuresdemo/simple/TimedReservation.java)
TimedReservation has a one-second delay and reports the start and end times of the reservation as console output up to the millisecond. (See Lines 11, 22 and 34.)
In terms of executing the code, notice that three
CompletableFutures are created.
airlineFuture is created at Line 11,
hotelFuture is created at Line 18 and
carRentalFuture is created at Line 29.
Then, at Line 20, the static method
CompletableFuture.allOf() is called, providing the
airlineFuture,
hotelFuture and
carRentalFuture as parameters. These futures now run in parallel. The call to
.join() at the end of the
.allOf() statement makes it so the code waits until all the futures have run.
At Lines 43-45, a
.get() call is made on each future. The output of the
.get() call is printed to the console. Listing 7 below shows the console output from the
TimedReservation class as well as from the
main() method in the general demonstration code in Listing 6.
**Listing 7:** The terminal output from running a set of CompletableFuture<T> in parallel.
Notice that the airline, hotel and car rental reservation calls start at the same time. Notice too that they run for one second simultaneously. This output shows that all three
CompletableFutures have run in parallel, each in their own thread. They start at the same time and also end at the same time as expected, This is indicated in lines of output that start with the prefix term,
Result:.
## Putting It All Together
In this article, I provided a brief overview of the
Future interface and
CompletableFuture class. I took an operational point of view showing how to run asynchronous code as a set of standalone Futures in sequence. Also, I showed how to run asynchronous code in sequence using a chain of CompletableFutures. Finally, I demonstrated how to run a set of
CompletableFutures in parallel.
Granted, I presented a lot of code and analysis. Still, this is only the start. There’s a lot more to learn, particularly about the many methods that make up the
CompletableFuture class.
Hopefully, the information I presented here provides the basic understanding you need to move forward taking advantage of the power and simplicity that
Futures and
CompletableFutures provide. They’re compelling technologies that will save you time and make your efforts with asynchronous programming under Java a lot easier.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)