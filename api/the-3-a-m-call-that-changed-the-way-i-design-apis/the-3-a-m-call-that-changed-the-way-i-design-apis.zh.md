某个周二凌晨3点17分，我的手机响起了警报，这个警报彻底改变了我对API设计的看法。

我们的面向客户的API停止响应了。不是缓慢退化，而是完全宕机。三个下游服务也随之宕机。等我赶到笔记本电脑前时，客户支持工单已经如潮水般涌入。

根本原因？单个数据库副本宕机了，而我们的API没有备用方案。单点故障最终导致了全面不可用。我花了接下来的四个小时手动重新路由流量，而我们的客户则在等待。

那晚我们损失了14,000美元的服务水平协议（SLA）赔款，并失去了大量客户信任。但它教会了我一个我现在应用于[我构建的每一个API](https://thenewstack.io/why-api-first-matters-in-an-ai-driven-world/)的道理：每一个设计决策都应该通过我所谓的“凌晨3点测试”。

## **凌晨3点测试**

这个测试很简单：当这个系统在凌晨3点宕机时，[值班工程师](https://thenewstack.io/holiday-on-call-duty-a-present-or-punishment/)能否快速诊断并修复它？

这个简单的问题从我的架构中剔除了许多看似“巧妙”的设计选择：

*   需要查阅文档的“巧妙”错误码？不及格。
*   依赖于先前请求的隐式状态？不及格。
*   导致不相关功能宕机的级联故障？不及格。

那次事故之后，我从头重建了我们的API基础设施。在接下来的三年里，处理每天5000万次请求的过程中，我总结出了五个原则，它们将我们的可靠性从99.2%提升到99.95%，让我能够安睡到天明。

## **原则1：为部分故障而设计**

初次事故六个月后，我们又发生了一次宕机。这次，一个下游支付处理器停止响应。我们的API尽职地等待着永远不会到来的响应，请求线程堆积如山，直到我们崩溃。

我意识到我们解决了一个问题，但又制造了另一个问题。我们需要能够优雅降级而非灾难性失败的系统。

这是我们构建的：

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

关键洞察：降级响应几乎总是优于错误。用户可以处理陈旧数据或受限功能。他们无法处理500错误。

在我们的服务中[实现这一模式](https://thenewstack.io/devs-dont-just-read-about-design-patterns-implement-them/)后，我们不再发生级联故障。当支付处理器再次宕机时（当年确实又发生了三次），我们的API返回了缓存的价格，并将交易排队等待稍后处理。客户几乎没有察觉。

## **原则2：将幂等性设为非协商条件**

这个教训来自一个27,000美元的错误。

一个移动客户端有一个bug，导致它激进地重试失败的请求。其中一个请求是支付。重试逻辑没有包含幂等键。你可以猜到接下来发生了什么。

一个客户被同一订单收费了23次。等我们注意到时，我们已经处理了数百个账户的重复收费。退款、客服工时以及[修复所需的工程时间](https://thenewstack.io/fixing-engineerings-biggest-time-suck-finding-information/)总共花费了27,000美元。

现在，每个修改数据的端点都必须要求幂等键。无一例外。

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

对于任何`POST`、`PUT`或`DELETE`操作，我们还开始拒绝没有幂等键的请求。一开始，一些客户端开发者抱怨。然后，当他们的重试bug不再导致数据损坏时，他们感谢了我们。

## **原则3：在URL中进行版本控制，而不是在Header中**

我通过观察一名初级工程师调试一个问题长达六个小时学到了这一点。

我们之前通过自定义头部对API进行版本控制：`X-API-Version: 2`。看起来很简洁，保持了URL的整洁。

但当出现问题时，我们的日志只显示URL和响应码——而不是头部信息。这名工程师查看了`/users/123`的日志，却搞不清楚为什么两个客户端之间的行为会不同。六个小时后，他才终于想到检查版本头部。

那周我们将版本控制移到了URL路径中：

```

/v1/users/123
/v2/users/123
```

现在版本信息会出现在：

*   每个日志条目
*   每个跟踪记录
*   每个错误报告
*   每个监控仪表盘

仅仅是调试时间的节省就证明了这次迁移是值得的。但我们也建立了版本控制规则，以避免未来的麻烦：

*   破坏性变更需要新版本
*   增量变更（新增可选字段）不需要新版本
*   我们同时支持至少两个版本
*   任何版本在停用前有12个月的弃用通知

当我们弃用一个版本时，客户端会在我们实际关闭它之前几个月收到一个`Deprecation`头部警告。

## **原则4：在需要之前进行限速**

我们差点以艰难的方式学到这个教训。

一家合作公司与我们的API进行了集成。他们的团队实现中有一个bug：当他们遇到超时时，他们会立即重试。无限次。并且以指数级并行方式。

某个周四下午2点，他们的系统开始每秒发送50,000个请求。我们没有限速。我们总是计划“需要时”再添加它。

我们需要它了。

幸运的是，我们的负载均衡器具有基本保护，它启动并开始丢弃请求。但合法的流量也被丢弃了。在47分钟内，我们的API基本上成了一个抽奖：你的请求可能通过，也可能不通过。

下一周，我们实施了分层限速：

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

使其真正有用的关键细节：

*   始终返回`Retry-After`头部，以便客户端知道何时重试。
*   包含`X-RateLimit-Remaining`，以便客户端可以看到他们的配额。
*   对不同的客户端层级使用不同的限制（合作伙伴比匿名用户获得更多）。
*   每个端点单独限制（搜索端点可以处理比支付端点更多的请求）。

那个合作伙伴的bug六个月后又发生了。这次，他们的请求被限速了，我们的其他客户端未受影响，我甚至直到第二天早上检查指标时才发现。

## **原则5：如果你看不到它，就无法修复它**

最可怕的宕机并不是所有东西都坏掉的情况。而是那些有细微问题且你几天都没有察觉的情况。

我们曾遇到一个问题，有3%的请求因特定错误码而失败。不足以触发我们的可用性警报（我们将其设置为5%）。不足以让客户大量涌入支持。但足以让每天数百名用户体验不佳。

我们花了两个星期才注意到。真实用户长达两周的糟糕体验。

在那之后，我们[为每个端点构建了可观测性：](https://thenewstack.io/observability-every-engineers-job-not-just-ops-problem/)

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

我们现在的最低可观测性要求：

*   按端点、状态码和客户端统计的请求计数
*   按端点统计的延迟百分位数（p50、p95、p99）
*   按端点和错误类型统计的错误率
*   跨服务边界的分布式跟踪
*   1%错误率时报警，而不是5%

那个3%的失败问题？有了我们新的可观测性，我们会在几分钟内发现它，而不是几周。

## **成果**

在我们的API基础设施中应用这些原则三年后：

| **指标** | **之前** | **之后** |
| --- | --- | --- |
| 月度可用性 | 99.2% | 99.95% |
| 平均检测时间 | 45分钟 | 3分钟 |
| 平均恢复时间 | 2小时 | 18分钟 |
| 客户端报告错误 | 340/周 | 23/周 |
| 凌晨3点呼叫（每月） | 8 | 0.5 |

最后一个指标是我最关心的。我从每周被叫醒两次变成了每两个月一次。

## **我会对过去的自己说什么**

如果我能回到第一次凌晨3点电话响起之前，我会告诉自己：

*   **从第一天起就为故障而构建。** 每一个外部调用最终都会失败。每一个数据库最终都会宕机。在它们发生之前就做好设计，而不是之后。
*   **让安全成为容易的事。** 要求幂等键在它帮你避免27,000美元的错误之前，可能感觉像是一种摩擦。限速在合作伙伴的bug试图拖垮你之前，可能感觉没必要。
*   **及早投资可观测性。** 你看不到的东西就无法修复。良好的监控成本与不知道系统出问题的成本相比，微不足道。
*   **平淡是福。** 凌晨3点难以调试的“巧妙”解决方案并不巧妙。在URL中进行版本控制。返回清晰的错误信息。做出显而易见的选择。

API并非偶然幸存。它们是通过设计幸存下来的，特别是通过为一切都出问题的那一刻而设计。

现在，当我的手机在凌晨3点震动时，通常只是垃圾信息。这正是我喜欢它的方式。