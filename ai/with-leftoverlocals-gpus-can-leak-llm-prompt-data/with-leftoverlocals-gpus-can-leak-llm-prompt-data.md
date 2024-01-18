<!--
title: GPU可通过LeftoverLocals泄露LLM提示数据
cover: https://cdn.thenewstack.io/media/2024/01/080320e9-trailtears_leftover-1024x725.jpg
-->

一家纽约安全公司发现了一个漏洞，该漏洞破坏了许多(尽管不是所有)GPU的安全防护。

> 译自 [With LeftoverLocals， GPUs Can Leak LLM Prompt Data](https://thenewstack.io/with-leftoverlocals-gpus-can-leak-llm-prompt-data/)，作者 Joab Jackson。

随着越来越多的组织开始在其服务和产品中结合[大语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)的 [AI](https://thenewstack.io/datastax-gas-data-api-for-genai-application-development/)，他们将不得不关注这些技术暴露的新的攻击载体。

周二，来自纽约安全顾问公司 [Trail of Bits](https://www.trailofbits.com/) 的研究人员发现了一种从同一服务器上托管的 GPU 读取另一 GPU 内存值的方式。研究人员证明，它可以用于窃听——跨容器或进程边界——基于提示的聊天会话。

该漏洞([CVE-2023-4969](https://www.cvedetails.com/cve/CVE-2023-4969/))适用于苹果、高通、AMD 和 [Imagination](https://www.imaginationtech.com/products/gpu/) 的 GPU(尽管到目前为止，还没有在 ARM 或 Nvidia 的 GPU 上演示过，Nvidia 是当前的 GPU [市场领导者](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/))。

例如，在 AMD Radeon RX 7900 XT 上，LeftoverLocals 每次 GPU 调用可以泄露大约 5.5 MB。

对于 [llama.cpp](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/) 上的 70 亿点模型，这将为每个 LLM 查询添加大约 181 MB——这比“以高精度重构 LLM 响应”所需的要多得多，Trail of Bits 的研究人员 [Heidy Khlaaf](https://www.heidyk.com/) 和 [Tyler Sorensen](https://users.soe.ucsc.edu/~tsorensen/) [写道](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)，他们在 9 月发现了该漏洞。

## LeftoverLocals 的工作原理

作为一个“同居型攻击”，LeftoverLocals 需要在与目标相同的机器上通过另一个应用程序或框架(如 OpenCL、Vulkan 或 Metal)运行。不需要提权。

攻击代码基本上会将 GPU 上任何未初始化的本地内存转储到全局内存中，允许攻击者读取该数据。

即使对于专业爱好者来说，编写执行此操作的代码也不难，研究人员指出。他们甚至提供了 [OpenCL](https://www.khronos.org/opencl/) 的示例监听代码:

```c
__kernel void listener(__global volatile int *dump) {
    local volatile int lm[LM_SIZE];
    for (int i = get_local_id(0); i < LM_SIZE; i+= get_local_size(0)) {
    dump[((LM_SIZE * get_group_id(0)) + i)] = lm[i];
    }
}
```

除了监听器，设置还将从写入“标记值”到本地内存中受益，这是检查 GPU 是否易受攻击的一种方式。

该博文提供了更多详细信息和上下文，所以请查看它。有趣的是，此漏洞不适用于浏览器 GPU 框架，例如 Google 的 [WebGPU](https://developer.chrome.com/docs/web-platform/webgpu)，因为它们会向 GPU 内核插入动态内存检查。

## 供应商如何响应 LeftoverLocals？

在确定漏洞后，研究团队通过 [CERT 协调中心](https://www.kb.cert.org/vuls/)启动了一个大型协调披露工作，与所有主要 GPU 供应商接洽。[像硬件提供商一样](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/)，有些响应比其他响应更及时。

苹果直到这个月才确认该漏洞，但 Trail of Bits 的重新测试发现，一些设备已经打了补丁(配备 A12 处理器的第三代 iPad)，而其他设备仍然容易受到攻击(配备 M2 处理器的苹果 MacBook Air)。

AMD [确认了该漏洞](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6010.html)，并正在研究修复方法。高通为其中一些 GPU [发布了补丁](https://lore.kernel.org/linux-firmware/20240111114032.126035-1-quic_akhilpo@quicinc.com/T/#u)，但并非所有 GPU。该公司还赞扬了研究人员的协调披露过程。

Imagination 也[发布了补丁](https://www.imaginationtech.com/gpu-driver-vulnerabilities/)，即使是 Trail of Bits 而不是 Imagination 的硅发现的漏洞，而是来自谷歌的一些研究人员，其 Android 移动软件[支持](https://blog.imaginationtech.com/the-android-invasion-imagination-gpu-ip-buddies-up-with-google-powered-devices/) Imagination GPU。

Trail of Bits 还联系了 Arm 和 Nvidia，尽管到目前为止，它们的 GPU 似乎不容易受到攻击。

## LeftoverLocals 的潜在影响是什么

尽管这种安全漏洞仍然存在于许多流行的消费类设备上，如 iPhone 和 Android 手机，但到目前为止，还没有关于漏洞利用的消息。AMD 本身仅将风险评估为具有中等威胁级别。

尽管如此，LeftoverLocals 指出了保护 LLM 及其支持 [MLops](https://thenewstack.io/mlops-needs-a-better-way-to-manage-gpus/) 的新兴做法。

正如研究人员所指出的: “该漏洞凸显了 ML 开发栈的许多部分存在未知的安全风险，并且没有经过安全专家的严格审查。”
