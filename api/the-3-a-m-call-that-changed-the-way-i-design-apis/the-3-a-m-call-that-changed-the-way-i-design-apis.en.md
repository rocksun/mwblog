At 3:17 a.m. on a Tuesday, my phone buzzed with the alert that would reshape the way I think about API design.

Our customer-facing API had stopped responding. Not slowly degrading; it was completely dead. Three downstream services went with it. By the time I got to my laptop, customer support tickets were flooding in.

The root cause? A single database replica had gone down, and our API had no fallback. One failure cascaded into total unavailability. I spent the next four hours manually rerouting traffic while our customers waited.

That night cost us $14,000 in service-level agreement (SLA) credits and a lot of trust. But it taught me something I now apply to [every API I build](https://thenewstack.io/why-api-first-matters-in-an-ai-driven-world/): Every design decision should pass what I call “The 3 a.m. Test.”

## **The 3 a.m. Test**

The test is simple: When this system breaks at 3 a.m., will the [on-call engineer](https://thenewstack.io/holiday-on-call-duty-a-present-or-punishment/) be able to diagnose and fix it quickly?

This single question has eliminated a surprising number of “clever” design choices from my architectures:

* Clever error codes that require documentation lookup? Fail.
* Implicit state that depends on previous requests? Fail.
* Cascading failures that take down unrelated features? Fail.

After that incident, I rebuilt our API infrastructure from the ground up. Over the next three years, handling 50 million daily requests, I developed five principles that transformed our reliability from 99.2% to 99.95% and let me sleep through the night.

## **Principle 1: Design for Partial Failure**

Six months after the initial incident, we had another outage. This time, a downstream payment processor went unresponsive. Our API dutifully waited for responses that never came, and request threads piled up until we crashed.

I realized we’d solved one problem but created another. We needed systems that degraded gracefully instead of failing catastrophically.

Here’s what we built:

```

class ResilientServiceClient:
    def __init__(self, primary_url, fallback_url):
        self.primary = primary_url
        self.fallback = fallback_url
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=5,
            recovery_timeout=30
        )
    
    async def fetch(self, request):
        # Try primary with circuit breaker protection
        if self.circuit_breaker.is_closed():
            try:
                response = await self.call_with_timeout(
                    self.primary, request, timeout_ms=500
                )
                self.circuit_breaker.record_success()
                return response
            except (TimeoutError, ConnectionError):
                self.circuit_breaker.record_failure()
        
        # Fall back to secondary
        try:
            return await self.call_with_timeout(
                self.fallback, request, timeout_ms=1000
            )
        except Exception:
            # Return degraded response rather than error
            return self.degraded_response(request)
```

The key insight: A degraded response is almost always better than an error. Users can work with stale data or reduced functionality. They can’t work with a 500 error.

After [implementing this pattern](https://thenewstack.io/devs-dont-just-read-about-design-patterns-implement-them/) across our services, we stopped having cascading failures. When the payment processor went down again (it did, three more times that year), our API returned cached pricing and queued transactions for later processing. Customers barely noticed.

## **Principle 2: Make Idempotency Non-Negotiable**

This lesson came from a $27,000 mistake.

A mobile client had a bug that caused it to retry failed requests aggressively. One of those requests was a payment. The retry logic didn’t include idempotency keys. You can guess what happened next.

A single customer got charged 23 times for the same order. By the time we noticed, we’d processed duplicate charges across hundreds of accounts. The refunds, the customer service hours, the [engineering time to fix](https://thenewstack.io/fixing-engineerings-biggest-time-suck-finding-information/) it cost $27,000.

Now, every mutating endpoint requires an idempotency key. No exceptions.

```

class IdempotentEndpoint:
    def __init__(self):
        self.idempotency_store = RedisStore(ttl_hours=24)
    
    async def handle_request(self, request, idempotency_key):
        # Check if we've already processed this request
        existing = await self.idempotency_store.get(idempotency_key)
        
        if existing:
            # Return cached response — don't re-execute
            return Response(
                data=existing['response'],
                headers={'X-Idempotent-Replay': 'true'}
            )
        
        # Process the request
        result = await self.execute_operation(request)
        
        # Cache for future retries
        await self.idempotency_store.set(
            idempotency_key,
            {'response': result, 'timestamp': now()}
        )
        
        return Response(data=result)
```

We also started rejecting requests without idempotency keys for any `POST`, `PUT` or `DELETE` operation. Some client developers complained initially. Then they thanked us when their retry bugs didn’t cause data corruption.

## **Principle 3: Version in the URL, Not the Header**

I learned this one by watching a junior engineer debug an issue for six hours.

We’d been versioning our API through a custom header: `X-API-Version: 2`. It seemed clean. Kept the URLs tidy.

But when something went wrong, our logs showed the URL and response code — not the headers. The engineer was looking at logs for `/users/123` and couldn’t figure out why the behavior was different between two clients. Six hours later, he finally thought to check the version header.

We moved versioning to the URL path that week:

```

/v1/users/123
/v2/users/123
```

Now version information shows up in:

* Every log entry
* Every trace
* Every error report
* Every monitoring dashboard

The debugging time savings alone justified the migration. But we also established versioning rules that prevented future pain:

* Breaking changes require a new version
* Additive changes (new optional fields) don’t require a new version
* We support at least two versions simultaneously
* 12-month deprecation notice before sunsetting any version

When we do deprecate a version, clients get a `Deprecation` header warning them for months before we actually turn it off.

## **Principle 4: Rate Limit Before You Need To**

We almost learned this lesson the hard way.

A partner company integrated with our API. Their team’s implementation had a bug: When they got a timeout, they’d retry immediately. Infinitely. With exponential parallelism.

At 2 p.m. on a Thursday, their system started sending 50,000 requests per second. We didn’t have rate limiting. We’d always planned to add it “when we needed it.”

We needed it.

Fortunately, our load balancer had basic protection that kicked in and started dropping requests. But legitimate traffic got dropped too. For 47 minutes, our API was essentially a lottery — maybe your request would get through, maybe it wouldn’t.

The next week, we implemented tiered rate limiting:

```

class TieredRateLimiter:
    def __init__(self):
        self.limiters = {
            'per_client': TokenBucket(rate=100, burst=200),
            'per_endpoint': TokenBucket(rate=1000, burst=2000),
            'global': TokenBucket(rate=10000, burst=15000)
        }
    
    async def check_limit(self, client_id, endpoint):
        # Check all tiers, return first failure
        for tier_name, limiter in self.limiters.items():
            key = client_id if tier_name == 'per_client' else endpoint
            result = await limiter.check(key)
            
            if not result.allowed:
                return RateLimitResponse(
                    allowed=False,
                    retry_after=result.retry_after,
                    limit_type=tier_name
                )
        
        return RateLimitResponse(allowed=True)
```

The key details that made this actually useful:

* Always return `Retry-After` headers so clients know when to try again.
* Include `X-RateLimit-Remaining` so clients can see their budget.
* Use different limits for different client tiers (partners get more than anonymous users).
* Separate limits per endpoint (the search endpoint can handle more than the payment endpoint).

That partner’s bug happened again six months later. This time, their requests got rate-limited, our other clients were unaffected, and I didn’t even find out until I checked the metrics the next morning.

## **Principle 5: If You Can’t See It, You Can’t Fix It**

The scariest outages aren’t the ones where everything breaks. They’re the ones where something is subtly wrong and you don’t notice for days.

We had an issue where 3% of requests were failing with a specific error code. Not enough to trigger our availability alerts (we’d set those at 5%). Not enough for customers to flood support. But enough that hundreds of users per day were having a bad experience.

It took us two weeks to notice. Two weeks of a broken experience for real users.

After that, we built [observability into every endpoint:](https://thenewstack.io/observability-every-engineers-job-not-just-ops-problem/)

```

class ObservableEndpoint:
    async def handle(self, request):
        trace_id = self.tracer.start_trace()
        start_time = time.time()
        
        try:
            response = await self.process(request)
            
            # Record success metrics
            duration_ms = (time.time() - start_time) * 1000
            self.metrics.histogram('request_duration_ms', duration_ms, {
                'endpoint': request.path,
                'status': response.status
            })
            self.metrics.increment('requests_total', {
                'endpoint': request.path,
                'status': response.status
            })
            
            return response
            
        except Exception as e:
            # Record failure with context
            self.metrics.increment('requests_errors', {
                'endpoint': request.path,
                'error_type': type(e).__name__
            })
            self.logger.error('request_failed', {
                'trace_id': trace_id,
                'error': str(e)
            })
            raise
```

Our minimum observability requirements now:

* Request count by endpoint, status code and client
* Latency percentiles (p50, p95, p99) by endpoint
* Error rate by endpoint and error type
* Distributed tracing across service boundaries
* Alerts at 1% error rate, not 5%

The 3% failure issue? With our new observability, we would have caught it in minutes, not weeks.

## **The Results**

After three years of applying these principles across our API infrastructure:

| **Metric** | **Before** | **After** |
| --- | --- | --- |
| Monthly availability | 99.2% | 99.95% |
| Mean time to detection | 45 minutes | 3 minutes |
| Mean time to recovery | 2 hours | 18 minutes |
| Client-reported errors | 340/week | 23/week |
| 3 a.m. pages (per month) | 8 | 0.5 |

That last metric is the one I care about most. I went from being woken up twice a week to once every two months.

## **What I’d Tell My Past Self**

If I could go back to before that first 3 a.m. call, I’d tell myself:

* **Build for failure from day one.** Every external call will eventually fail. Every database will eventually go down. Design for it before it happens, not after.
* **Make the safe thing the easy thing.** Requiring idempotency keys feels like friction until it saves you from a $27,000 mistake. Rate limiting feels unnecessary until a partner’s bug tries to take you down.
* **Invest in observability early.** You can’t fix what you can’t see. The cost of good monitoring is nothing compared to the cost of not knowing your system is broken.
* **Boring is good.** The clever solution that’s hard to debug at 3 a.m. isn’t clever. Version in the URL. Return clear error messages. Make the obvious choice.

APIs don’t survive by accident. They survive by design, specifically, by designing for the moment when everything goes wrong.

Now, when my phone buzzes at 3 a.m., it’s usually just spam. And that’s exactly how I like it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/1507ea85-cropped-e67f5a04-sreenivasa-reddy-hulebeedu-reddy.jpg)

Sreenivasa Reddy Hulebeedu Reddy is a lead software engineer and enterprise systems architect with more than 13 years of experience building APIs that handle tens of millions of daily requests. He serves as a peer reviewer for Wiley-IEEE Press and...

Read more from Sreenivasa Reddy Hulebeedu Reddy](https://thenewstack.io/author/sreenivasa-reddy-hulebeedu-reddy/)