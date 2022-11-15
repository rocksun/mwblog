# Request 和 Limit 到底是啥？

Kubernetes Pod 的容器上设置的 request 和 limit 是什么？有这样一些回答：

1. 资源的请求值和限制值
2. 资源的的软限制(limit)和硬限制(limit)
3. 资源的初始值和最大值

第一个回答真的是没有什么技术含量，是认为面试官不会翻译吗？这个情况不在少数，一些有技巧的同学会配合一系列的车轱辘话，让这个解释显得没那么硬。例如：“CPU 的 Request 值就是 CPU 的请求值，CPU 的 Limit 值就是 CPU 的限制值”，只要说的慢，说的自信，估计也让面试官无言以对。

第二个回答，非常的费解，我[百度](https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=request%20limit%20kubernetes&fenlei=256&rsv_pq=0x85c5d9bd0001da10&rsv_t=63ffLt%2Bdq10lctlJxRx0IVSYlh0CqeSVLa5kuU%2F63KtkV0NxZmRiW6xBrNa%2F&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=2&rsv_sug1=1&rsv_sug7=001&rsv_n=2&rsv_sug2=0&rsv_btype=i&inputT=554&rsv_sug4=944&rsv_sug=9)了一下，至少排名靠前的文章都说的类似且雷同，照着学应该不会有错。但是如果特意去搜“软限制”和“硬限制”也能找到，属实是误认子弟。这个事情吧，我猜啊，可能是某人受 ulimit 设置的 soft limit 和 hard limit 影响，将这个概念强加给了 kubernetes 。在 [kubernetes 官方文档](https://kubernetes.io/zh-cn/docs/concepts/configuration/manage-resources-containers/)中，只有如下描述：

> CPU 限制定义的是容器可使用的 CPU 时间的**硬性**上限。 在每个调度周期（时间片）期间，Linux 内核检查是否已经超出该限制； 内核会在允许该 cgroup 恢复执行之前会等待。

这个“硬性”对应的英文是 hard ，但真的和 soft limit 和 hard limit 毫无关系，而且可以看到这个硬性上限也是针对 CPU 的，对内存来说 limit 有着不同的意义。

第三个回答，没怎么搜到，但作为中间件专家，我也猜到，这个说法可能来自 [Java 虚拟机](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/java.html)的 -Xms 和 -Xmx ，但这个和本文说的 request 和 limit 完全不是一回事。

就这么个简单的概念，好多人说不清楚，我猜测啊，很重要的一个原因，是有一些人喜欢类比。看到过一些奇葩的 kubernetes 课程，脑洞大的没谱，生搬硬套，非要类比。跟外行人科普，这样还可以接受，真的干这行，该是啥就是啥，少作类比，更不要拿着半吊子类比去教别人。

最后，摘录一个传统相声蛤蟆鼓，大家体会一下：

> 一个问：“蛤蟆为什么能叫？”一个答：“因为肚子大。”“肚子大就能叫？纸篓肚子也大，不叫。”“纸篓是竹子编的，竹子做的不叫。”“笛子也是竹子做的，好听着呢。”“笛子有眼儿，有眼的就能响。”“筛子上面全是眼儿，怎么不响？”“筛子是圆的扁的，圆的扁的不响。”“那锣不是圆的扁的？比谁都响。”“锣中间有脐，有脐能响。”“做饭的锅也有脐，不响。”“锅是铁的，铁的不响。”“庙里的钟也是铁的，怎么这么响？”“钟悬则鸣，挂起来响。”“秤砣也是铁的挂起来，你看他响吗？”“秤砣是实心的，实心的不响。”“炸弹也实心的，响得吓人。”“炸弹里有药，有药就响。”“药铺里全是药怎么不响……”
