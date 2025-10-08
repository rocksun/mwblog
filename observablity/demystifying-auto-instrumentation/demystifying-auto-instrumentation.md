
<!--
title: 自动化埋点揭秘：这“魔法”究竟如何运作？
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: 本文揭示了自动插码的五大核心技术：猴子补丁、字节码插码、编译时插码、eBPF和语言运行时API，无需修改源码即可增强可观测性。
-->

本文揭示了自动插码的五大核心技术：猴子补丁、字节码插码、编译时插码、eBPF和语言运行时API，无需修改源码即可增强可观测性。

> 译自：[Demystifying Automatic Instrumentation: How the Magic Actually Works](https://opentelemetry.io/blog/2025/demystifying-auto-instrumentation/)
> 
> 作者： Severin Neumann

尽管OpenTelemetry和[eBPF](https://ebpf.io/)日益兴起，但大多数开发者并不了解自动插码在底层究竟是如何运作的。本文将对其进行分解——并非建议您自行构建，而是帮助您理解当您的工具神奇地“just work”时，背后发生了什么。

我们将探讨支撑自动插码的五种关键技术：猴子补丁、字节码插码、编译时插码、eBPF和语言运行时API。每种技术都利用不同编程语言和运行时环境的独特特性，在不改变代码的情况下增加可观测性。

## 什么是自动插码？

根据[词汇表](/docs/concepts/glossary)的定义，自动插码是指“*无需最终用户修改应用程序源代码的遥测数据收集方法。方法因编程语言而异，示例包括字节码注入或猴子补丁。*”

值得注意的是，“自动插码”常用于描述两个相关但截然不同的概念。在上述定义和本文中，它指的是可用于在不更改代码的情况下实现可观测性的特定技术（如字节码注入或猴子补丁）。然而，当人们在对话中使用“自动插码”时，他们通常指的是完整的零代码解决方案，例如[OpenTelemetry Java agent](/docs/zero-code/java/agent/)。

这种区别很重要：这里实际上存在一个三层架构。最底层是我们在本文中探讨的**自动插码技术**（字节码注入、猴子补丁等）。这些技术被针对特定框架的[插码库](/docs/concepts/glossary/#instrumentation-library)使用，例如，用于对[Spring和Spring Boot](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/spring)、[Express.js](https://www.npmjs.com/package/@opentelemetry/instrumentation-express)、[Laravel](https://packagist.org/packages/open-telemetry/opentelemetry-auto-laravel)或其他流行框架进行插码的库。最后，像OpenTelemetry Java agent这样的完整解决方案将这些插码库捆绑在一起，并为导出器、采样器和其他构建块添加所有样板配置。

可观测性社区中关于正确术语的争论仍在继续，本文不会试图解决这些讨论。

另请注意，对一个人而言“自动”的事物，对另一个人而言可能就是“手动”的：如果一个库开发者将其OpenTelemetry API集成到代码中，当该库的用户将OpenTelemetry SDK添加到其应用程序时，他们将“自动”从该库获取跟踪、日志和指标。

## 想亲自尝试这些技术吗？

本文包含小的代码片段以说明概念。您可以在[实验仓库](https://github.com/causely-oss/automatic-instrumentation-lab)中尝试完整的示例。

在我们探讨这些技术之前，请务必注意，您不应该从零开始构建自己的自动插码，尤其不应将本文用作蓝图。此处的示例为了教育目的进行了简化，并省略了您在实际实现中会遇到的许多复杂细节。目前已有成熟的工具和机制来处理您从头开始构建插码时会面临的大部分复杂性和边缘情况。如果您有兴趣深入研究该领域，最好的方法是[为OpenTelemetry等现有项目做出贡献](/community/#develop-and-contribute)，在那里您可以向经验丰富的维护者学习，并使用生产就绪的代码。

## 自动插码技术

现在让我们深入探讨这些技术的底层运作方式。

### 猴子补丁：运行时函数替换

猴子补丁或许是最直接的自动插码技术，常用于JavaScript、Python和Ruby等动态语言。其概念很简单：在运行时，我们将现有函数替换为已插码的版本，这些版本会在调用原始函数之前和之后注入遥测数据。

以下是其在Node.js中的工作方式：

```
const originalFunction = exports.functionName;

function instrumentedFunction(...args) {
  const startTime = process.hrtime.bigint();
  const result = originalFunction.apply(this, args);
  const duration = process.hrtime.bigint() - startTime;
  console.log(`functionName(${args[0]}) took ${duration} nanoseconds`);
  return result;
}

exports.functionName = instrumentedFunction;

```

require-in-the-middle库允许我们在模块加载时执行此替换，拦截模块加载过程以在应用程序使用导出的函数之前对其进行修改：

```
const hook = require("require-in-the-middle");
hook(["moduleName"], (exports, name, basedir) => {
  const functionName = exports.fibonacci;
  ...
  exports.functionName = instrumentedFunction;
  return exports;
});

```

然而，猴子补丁存在局限性。它无法对已编译为机器码的代码进行插码，并且可能不适用于在插码加载之前就被调用的函数。此外，对于性能关键型应用程序而言，函数包装的开销可能很大。当被插码代码的实现发生显著变化时，猴子补丁也很脆弱，因为插码代码需要更新以匹配新的接口。

要亲自尝试，请查看实验中的[Node.js示例](https://github.com/causely-oss/automatic-instrumentation-lab#monkey-patching-nodejs)。

如果您想查看猴子补丁的实际应用，可以查阅OpenTelemetry为[JavaScript](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages)或[Python](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation)提供的插码库。

### 字节码插码：修改虚拟机

对于运行在虚拟机上的语言，字节码插码提供了一种强大的方法。该技术通过在虚拟机加载编译后的字节码时对其进行修改，从而允许我们在指令级别注入代码。

Java的Instrumentation API为这种方法提供了基础。当通过`-javaagent`标志指定Java agent时，JVM会在主应用程序启动之前调用agent的premain方法。这为我们提供了注册类转换器的机会，该转换器可以在任何类加载时对其进行修改。

```
public static void premain(String args, Instrumentation inst) {
    new AgentBuilder.Default()
        .type(ElementMatchers.nameStartsWith("com.example.TargetApp"))
        .transform((builder, typeDescription, classLoader, module, protectionDomain) ->
            builder.method(ElementMatchers.named("targetMethod"))
                   .intercept(MethodDelegation.to(MethodInterceptor.class))
        ).installOn(inst);
}

```

然后，拦截器用计时逻辑包装原始方法调用：

```
@RuntimeType
public static Object intercept(@Origin String methodName,
                            @AllArguments Object[] args,
                            @SuperCall Callable<?> callable) throws Exception {
    long startTime = System.nanoTime();
    Object result = callable.call();
    long duration = System.nanoTime() - startTime;

    System.out.printf("targetMethod(%s) took %d ns%n", args[0], duration);
    return result;
}

```

字节码插码尤其强大，因为它在JVM级别工作，使其在JVM生态系统内与语言无关。它无需修改即可对Java、Kotlin、Scala和其他JVM语言进行插码。

字节码插码的主要优势是其全面的覆盖范围——它可以对任何在JVM上运行的代码进行插码，包括动态加载或来自外部源的代码。然而，由于字节码转换过程，它会带来一些开销。

在实际实现中，[ByteBuddy](https://bytebuddy.net/#/)是Java中字节码插码的首选库，它为创建Java agent提供了强大而灵活的API。它抽象了字节码操作的大部分复杂性，并提供了一种清晰、类型安全的方式来定义插码规则。

要亲自尝试，请查看实验中的[Java示例](https://github.com/causely-oss/automatic-instrumentation-lab#byte-code-instrumentation-java)。

如果您想查看字节码插码的实际应用，可以查阅OpenTelemetry为[Java](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation)或[.NET](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src)提供的插码库。

### 编译时插码：将可观测性嵌入二进制文件

对于像Go这样的静态编译语言，编译时插码提供了一种不同的方法。我们不是在运行时修改代码，而是在构建过程中使用[抽象语法树](https://en.wikipedia.org/wiki/Abstract_syntax_tree)（AST）操作来转换源代码。

该过程包括将源代码解析为AST，修改树以添加插码代码，然后在编译前生成修改后的源代码。这种方法确保插码被嵌入到最终的二进制文件中，为插码机制本身提供了零运行时开销。

```
func instrumentFunction() {
    fset := token.NewFileSet()
    file, err := parser.ParseFile(fset, "app/target.go", nil, parser.ParseComments)

    // Find the target function and add timing logic
    ast.Inspect(file, func(n ast.Node) bool {
        if fn, ok := n.(*ast.FuncDecl); ok && fn.Name.Name == "targetFunction" {
            // Add defer statement for timing
            deferStmt := &ast.DeferStmt{
                Call: &ast.CallExpr{
                    Fun: &ast.CallExpr{
                        Fun: &ast.Ident{Name: "trace_targetFunction"},
                    },
                },
            }
            fn.Body.List = append([]ast.Stmt{deferStmt}, fn.Body.List...)
        }
        return true
    })

    // Write the modified file back
    printer.Fprint(f, fset, file)
}

```

编译时插码有几个优点。它为插码机制提供了零运行时开销，并且生成的二进制文件包含所需的所有代码。这种方法与编译语言配合良好，并且可以集成到现有的构建流程中。

尽管如此，它也伴随着权衡。它需要访问源代码和构建系统，这使得它不适用于对第三方应用程序或库进行插码。它还需要更复杂的工具来正确且一致地操作抽象语法树（AST），这会增加构建管道的复杂性，并可能需要更改您的CI/CD工作流程。

要亲自尝试，请查看实验中的[Go编译时示例](https://github.com/causely-oss/automatic-instrumentation-lab#compile-time-instrumentation-go)。

如果您想查看编译时插码的实际应用，可以查阅[OpenTelemetry Go编译插码](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation)项目。

### eBPF插码：内核级可观测性

[eBPF](https://ebpf.io/)（扩展伯克利数据包过滤器）代表了一种截然不同的自动插码方法。eBPF不是修改应用程序代码或字节码，而是在内核级别工作，将探针附加到运行中应用程序的函数入口和出口点。

eBPF程序是小型、安全的程序，运行在内核中，可以观察系统调用、函数调用和其他事件。对于自动插码，我们使用uprobe（用户空间探针）来附加到应用程序中的特定函数。

```
#!/usr/bin/env bpftrace

uprobe:/app/fibonacci:main.fibonacci
{
    @start[tid] = nsecs;
}

uretprobe:/app/fibonacci:main.fibonacci /@start[tid]/
{
    $delta = nsecs - @start[tid];
    printf("fibonacci() duration: %d ns\n", $delta);
    delete(@start[tid]);
}

```

这个[bpftrace](https://github.com/bpftrace/bpftrace)脚本将一个探针附加到我们应用程序中的函数。当函数被调用时，它记录开始时间。当函数返回时，它计算持续时间并打印结果。

eBPF插码与语言无关，适用于任何在Linux上运行的语言。它提供深层系统级可观测性，无需对应用程序代码或构建过程进行任何修改。由于插码在内核中运行，开销极小。

然而，eBPF插码也有一些局限性。它需要Linux和root权限才能运行，这使得它不太适合容器化环境或无法以高权限运行的应用程序。

对于实际用例，bpftrace只是众多eBPF工具之一。虽然它非常适合学习和原型开发，但生产环境通常使用更复杂的框架，如[BCC](https://github.com/iovisor/bcc) (BPF编译器集合)或[libbpf](https://github.com/libbpf/libbpf)，它们提供更好的性能、更多功能和更强的安全保障。

要亲自尝试，请查看实验中的[Go eBPF示例](https://github.com/causely-oss/automatic-instrumentation-lab#ebpf-based-instrumentation-go)。

如果您想查看编译时插码的实际应用，可以查阅[OpenTelemetry eBPF插码](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)项目（“OBI”），这是[Grafana Labs捐赠Beyla](https://github.com/open-telemetry/community/issues/2406)的成果。

### 语言运行时API：原生插码支持

一些语言提供了用于插码的内置API，提供了一种更集成的方法。PHP 8.0中引入的[PHP Observer API](https://github.com/php/php-src/blob/PHP-8.0/Zend/zend_observer.h)是这种方法的一个典型例子。

Observer API允许C扩展在Zend引擎级别挂接到PHP引擎的执行流中。这提供了对PHP应用程序行为的深度可见性，而无需修改代码。

```
static void observer_begin(zend_execute_data *execute_data) {
    if (execute_data->func && execute_data->func->common.function_name) {
        const char *function_name = ZSTR_VAL(execute_data->func->common.function_name);
        if (strcmp(function_name, "fib") == 0) {
            start_time = clock();
        }
    }
}

static void observer_end(zend_execute_data *execute_data, zval *retval) {
    if (execute_data->func && execute_data->func->common.function_name) {
        const char *function_name = ZSTR_VAL(execute_data->func->common.function_name);
        if (strcmp(function_name, "fib") == 0) {
            clock_t end_time = clock();
            double duration = (double)(end_time - start_time) / CLOCKS_PER_SEC * 1000;
            php_printf("Function %s() took %.2f ms\n", function_name, duration);
        }
    }
}

```

Observer API提供了一种清晰、受支持的方式来为PHP应用程序添加插码。它在语言运行时级别运行，类似于其他语言如何实现其插码API。这种方法效率高，并与语言生态系统良好集成。

然而，它需要编写C扩展，这增加了复杂性，并使不熟悉C或PHP内部API的开发者难以使用。它也特定于PHP，因此知识无法转移到其他语言。

要亲自尝试，请查看实验中的[PHP Observer API示例](https://github.com/causely-oss/automatic-instrumentation-lab#php-observer-api-php)。

如果您想查看API插码的实际应用，可以查阅OpenTelemetry为[PHP](https://github.com/open-telemetry/opentelemetry-php-contrib/tree/main/src/Instrumentation)提供的插码库。

## 关于上下文传播的说明

虽然我们已经介绍了自动插码的核心技术，但有一个重要方面我们尚未讨论：[上下文传播](/docs/concepts/context-propagation/)。这涉及将跟踪上下文信息（跟踪ID、span ID）注入HTTP头、消息元数据和其他通信通道，以实现跨服务边界的分布式跟踪。

与我们探讨的纯粹观测技术不同，上下文传播通过改变跨服务边界传输的数据来主动修改应用程序的行为。这引入了额外的复杂性，值得专门撰写一篇博客文章。

## 结论

我们探讨了自动插码背后的核心技术，从猴子补丁到字节码插码再到eBPF探针。每种方法都利用不同编程语言和运行时环境的独特特性。

这些技术为OpenTelemetry等生产级可观测性工具提供了支持，使开发者能够快速添加遥测数据而无需修改源代码。最成功的可观测性策略结合了自动和手动插码：自动插码为常见模式提供广泛覆盖，而手动插码则捕获业务特定指标。

如果您想亲自尝试这些技术，可以使用[自动插码实验](https://github.com/causely-oss/automatic-instrumentation-lab)。

如果您有兴趣为这些技术做出贡献，请考虑参与[OpenTelemetry的各种特别兴趣小组](https://github.com/open-telemetry/community/#special-interest-groups)（SIG）。