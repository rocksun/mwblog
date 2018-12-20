# 使用perf诊断CPU问题

针对CPU高的问题，尤其是系统态CPU高的问题，Linux下可以使用perf进行分析，AIX下可以采用tprof。这类工具通过对于CPU定时采样，从而推断出占用CPU较高的模块或者方法，详细原理可以参考[这篇文章](https://www.ibm.com/developerworks/cn/linux/l-cn-perf1/index.html),本文会通过一个简单案例介绍perf的常见用法。

客户一个Tuxedo的应用，发现CPU占用率较高，其中系统态约占50%。通过top看发现CPU比较平均。所以我们首先通过perf收集一下整体的信息：

```
perf record -F 99 -ag -- sleep 10
```

