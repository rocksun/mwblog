# When Do Retry, Backoff, and Jitter Work?
![Featued image for: When Do Retry, Backoff, and Jitter Work?](https://cdn.thenewstack.io/media/2025/03/c74e4825-mohammad-rahmani-_fx34keqiew-unsplash-1024x683.jpg)
[Mohammad Rahmani](https://unsplash.com/@afgprogrammer?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash.](https://unsplash.com/photos/man-in-black-long-sleeve-shirt-using-computer-_Fx34KeqIEw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
In a recent discussion with engineers, I came across a common misconception about how retries, exponential backoff, jitter, and others would help maintain the availability of services while experiencing increased service load. I was excited to learn about the deep theoretical knowledge of engineers around different types of backoffs, jitters, and retries.

But what surprised me was that many folks felt that these retries, backoffs, and jitters are perfect antidotes for reliably handling increased load on servers. While retries, backoffs, and jitters are amazing and [cheap solutions to handle situations of bursty load](https://thenewstack.io/handling-bursty-traffic-in-real-time-analytics-applications/), there is an important distinction to understand before assuming this is a universal cure.

It would be better to understand how and why these [work and then use that knowledge](https://thenewstack.io/productivity-paradox-productivity-in-the-age-of-knowledge-work/) to apply and validate if they work in different situations.

**Introduction of a Hypothetical Service**
Let us assume that we have a Deals Service that calculates the discount applicable to a given product. For the sake of simplicity, we will assume that the Deals Service can handle two concurrent requests every second. Below is a simple diagram for the Deals Service.

![](https://cdn.thenewstack.io/media/2025/03/06239017-image1-1024x524.png)
Diagram 1.

Let us assume that we are having a flash sale and have five users interested in deals. So when the sale starts, they all make concurrent requests to our Deals Service. Bear with me here; some may say this is not how it works in the real world. Given that five requests are way higher than what the Deals Service can handle, it starts getting overloaded. This happens as there are limited resources on the server like CPU, memory, network I/O, etc., and with increased requests, there is increased contention for these resources. With increased latency, this often manifests on the server side, and client requests start timing out.

Diagram 2 shows the relation between the increase in TPS (X-axis) and latency (Y-axis) seen by customers. For simplicity, we will assume a one-second client-side timeout.

![](https://cdn.thenewstack.io/media/2025/03/8b054d14-image3.png)
Diagram 2.

Note that as concurrent TPS grows beyond 2 (the safe limit we established for Deals Service in Diagram 1), the latency grows beyond the client timeout of 1 second, leading to request timeouts. Note that service performance degrades rapidly beyond the safe limit of two requests, and this is also how real-world services behave in almost all cases, so it is a useful diagram to remember if you are interviewing.

*Note: To identify these safe limits (e.g., TPS of 2 in our case of Deals Service), we will need to consistently load test the service at some cadence and ensure each server resource and service metrics are within safe limits. For example, CPU does not go beyond 60% usage for 2 TPS but increases to 90% CPU for 3 TPS, etc.*
**How Do We Solve This Problem?**
When clients see timeouts, we usually rely on retries. Retry is a powerful solution to handle transient failures (i.e., network issues like packet loss, etc.) that all distributed systems encounter. Retries have side effects that most folks don’t think about (e.g., if retries are idempotent, will we create retry storms, etc.). We won’t be delving into that here for the sake of simplicity, and I will cover that in a separate article. For now, let us implement a retry without any delay.

In the case of the Deals Service, assuming all five of our requests time out after the first attempt, we will send the same surge of five requests to the Deals Service immediately, leading to the same outcome. So, adding retries does not help.

**How About the Antidote of Retry With Exponential Backoff?**
Exponential backoff (or a different type of backoff) increases the wait period exponentially after every failed retry attempt. The waiting period is usually proportional to the retry attempt count (many exponential backoffs will cap the overall wait period). Given all five requests, Deals Service will timeout simultaneously, so exponential retry will lead to the same outcome as retrying with no wait. So, backing off didn’t help much compared to retrying without waiting.

**How About Retry With Exponential Backoff and Jitter?**
Let us assume a hypothetical jitter formula — rand (1,3) — where we choose a random value between 1 and 3 seconds. We add this random jitter value to the exponential backoff value and get a new wait time before making subsequent requests to the Deals Service. Diagram 3 shows the situation after all five requests failed after making the first request.

![](https://cdn.thenewstack.io/media/2025/03/9042e653-image2-1024x723.png)
Diagram 3.

For instance, Customer 1 calculates the random jitter value of 1s and adds this to the exponential calculated value of 1s to get the wait time of 2s before making the subsequent request. Similarly, Customer 2 calculates the jitter value of 2s and adds this to the exponential backoff of 1s to wait for 3s before making the following request to Deals Service.

As we can see, adding jitter to exponential backoff helps spread the burst of requests, leading to a situation where all requests succeed in the next attempt.

*Note: We have conveniently chosen a jitter value that helps spread out requests to the Deals Service and keeps concurrent requests under 2 TPS. However, in real-world scenarios, a few new customers may send new requests very easily, tipping the Deals Service beyond the 2 TPS breaking point and rendering our efforts to smoothen the burst out useless. Let us look at the details below.*
**When Do Jitter and Exponential Backoff Not Work?**
In our example of the Deals Service, we assumed that the overall number of customers stayed constant at five (i.e., the fixed number of customers in our system). In contrast, if we consistently add a new customer every second (beyond these five customers), making a new first request to the Deals Service, our solution for backoff and jitter does not work. This raises an essential point about the effectiveness of jitter and exponential backoff. If we have new customers constantly added to the system, they are not aware of other customers backing off in an attempt to reduce the concurrent workload on our service. As a result, the overall concurrent load on the system continues to increase even as backoff/jitter attempts to spread out the prior load on service by delaying them to the future.

**Closing Thoughts**
Backoff with jitter is an effective mechanism to smoothen out a short burst of requests when using retries. However, their overall effectiveness diminishes if we see new customer requests that increase the concurrent load on our service. In cases where the concurrent load goes beyond the tipping point (e.g., TPS of 2 in our case of the Deals Service), backoffs and jitters don’t help at all. I hope this allows developers to understand how exponential backoffs and jitters work in real situations and what assumptions need to exist for them to be helpful in a distributed system.


[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)