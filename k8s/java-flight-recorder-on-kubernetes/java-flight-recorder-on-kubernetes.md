<!--
title: Kubernetes上使用Java飞行记录器
cover: ./cover.png
-->

在本文中，您将学习如何使用 Java 飞行记录器和 Cryostat 在 Kubernetes 上持续监控应用程序。

> 译自 [Java Flight Recorder on Kubernetes](https://piotrminkowski.com/2024/02/13/java-flight-recorder-on-kubernetes/)，作者 piotr.minkowski。

在本文中，您将学习如何使用 Java 飞行记录器和 [Cryostat](https://cryostat.io/) 在 Kubernetes 上持续监控应用程序。Java 飞行记录器(JFR)是一种收集 Java 应用程序生成的诊断和性能分析数据的工具。它专为即使在高负载的生产环境中也几乎不造成性能开销的情况而设计。我们可以说 Java 飞行记录器的作用类似于飞机的黑匣子。即使 JVM 崩溃，我们也可以分析就在失败之前收集的诊断数据。这一事实使得 JFR 在像 Kubernetes 这样运行着许多应用程序的环境中特别有用。 

假设我们在 Kubernetes 上运行许多 Java 应用程序，那么我们就应该对自动收集 Java 飞行记录器生成的数据的工具感兴趣。这就是 Cryostat。它允许我们安全地管理容器化 Java 工作负载的 JFR 记录。通过内置的发现机制，它可以检测到所有暴露 JFR 数据的应用程序。根据使用案例，我们可以直接在 Cryostat 控制台上存储和分析录制，也可以导出录制数据以执行更深入的分析。

如果您对 Kubernetes 上的 Java 应用程序相关的更多主题感兴趣，可以看看我博客上的一些其他文章。以下文章描述了在 Kubernetes 上运行 Java 应用程序的一些最佳实践。您也可以阅读例如如何调整 CPU 限制以加速 Kubernetes 上的 Java 启动的文章。

## 源代码

如果您想亲自尝试，可以随时查看我的源代码。为此，您需要克隆我的 GitHub [仓库](https://github.com/piomin/sample-istio-services.git)。然后您需要进入 `callme-service` 目录。之后，您只需要按照我的说明进行操作即可。让我们开始吧。

## 在 Kubernetes 上安装 Cryostat 

在第一步中，我们使用 Cryostat 的 operator 在 Kubernetes 上安装 Cryostat。为了在 Kubernetes 上使用和管理 operator，我们应该在集群上安装 Operator Lifecycle Manager(OLM)。`operator-sdk` 二进制文件提供了一个命令来轻松安装和卸载 OLM:

```bash
$ operator-sdk olm install
```

一旦 OLM 在我们的集群上运行，我们就可以继续 Cryostat 的安装了。我们可以在 Operator Hub 中找到所需的带有 Subscription 声明的 YAML 清单。我们只需要使用以下命令将清单应用到目标:

```bash
$ kubectl create -f https://operatorhub.io/install/cryostat-operator.yaml
```

默认情况下，此 operator 将安装在 operators 命名空间中，并且可以从集群中的所有命名空间使用。安装后，我们可以通过执行以下命令来验证 operator 是否正常工作:

```bash
$ kubectl get csv -n operators
```

为了简化 Cryostat 的安装过程，我们可以使用 OpenShift。使用 OpenShift 我们不需要安装 OLM，因为它已经存在了。我们只需要在 Operator Hub 中找到“Red Hat 构建的 Cryostat”操作器并使用 OpenShift 控制台安装它。默认情况下，该 operator 在 `openshift-operators` 命名空间中可用。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-10.37.25.png?resize=768%2C260&ssl=1)

然后，让我们创建一个专门用于运行 Cryostat 和示例应用程序的命名空间。命名空间的名称是 `demo-jfr`。

```bash
$ kubectl create ns demo-jfr
```

Cryostat 建议使用 [cert-manager](https://cert-manager.io/) 来加密流量。在我们的练习中，为了简化起见，我们禁用了该集成。然而，在生产环境中，除非您不使用另一种加密流量的解决方案，否则应该安装“cert-manager”。为了在所选命名空间中运行 Cryostat，我们需要创建 `Cryostat` 对象。参数 `spec.enableCertManager` 应该设置为 `false`。

```yaml
apiVersion: operator.cryostat.io/v1beta1
kind: Cryostat  
metadata:
  name: cryostat-sample
  namespace: demo-jfr
spec:
  enableCertManager: false
  eventTemplates: []
  minimal: false
  reportOptions:
    replicas: 0
  storageOptions:  
    pvc:
      annotations: {}
      labels: {}
      spec: {}
  trustedCertSecrets: []
```


如果一切正常，您应该会在 `demo-jfr` 命名空间中看到以下 pod:

```bash
$ kubectl get po -n demo-jfr
NAME                     READY   STATUS    RESTARTS   AGE
cryostat-sample-5c57c9b8b8-smzx9   3/3     Running   0          60s
```

下面是一个 Kubernetes 服务列表。Cryostat 控制台通过 cryostat-sample 服务在 8181 端口下公开。

```bash
$ kubectl get svc -n demo-jfr
NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
cryostat-sample          ClusterIP   172.31.56.83     <none>        8181/TCP，9091/TCP            70m  
cryostat-sample-grafana  ClusterIP   172.31.155.26    <none>        3000/TCP                     70m
```

我们可以使用 Kubernetes `Ingress` 或 OpenShift `Route` 来访问 Cryostat 控制台。当前还没有要监控的应用程序。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-12.04.42.png?resize=768%2C454&ssl=1)

## 创建示例 Java 应用程序

我们使用 Spring Boot 框架构建一个示例 Java 应用程序。我们的应用程序公开了一个 REST 端点。如您所见，端点实现非常简单。`pingWithRandomDelay()` 方法在 0 到 3 秒之间添加一个随机延迟，并返回字符串。但是，在该方法中有一件有趣的事情。我们正在创建 `ProcessingEvent` 对象(1)。然后，我们在睡眠线程之前调用它的 `begin` 方法(2)。方法恢复后，我们在 `ProcessingEvent` 对象上调用 commit 方法(3)。通过这种不显眼的方式，我们生成了第一个自定义 JFR 事件。此事件旨在监控我们方法的处理时间。

```java
@RestController
@RequestMapping("/callme")
public class CallmeController {

  private static final Logger LOGGER = LoggerFactory.getLogger(CallmeController.class);

  private Random random = new Random();

  private AtomicInteger index = new AtomicInteger();

  @Value("${VERSION}")
  private String version;

  @GetMapping("/ping-with-random-delay")
  public String pingWithRandomDelay() throws InterruptedException {
    int r = new Random().nextInt(3000);
    int i = index.incrementAndGet();
    
    ProcessingEvent event = new ProcessingEvent(i); // (1)
    event.begin(); // (2)
    
    LOGGER.info("Ping with random delay: id={}， name={}， version={}， delay={}"，
        i， buildProperties.isPresent() ? buildProperties.get().getName() : "callme-service"， version， r);
        
    Thread.sleep(r);
    event.commit(); // (3)

    return "I'm callme-service " + version;
  }

}
```

让我们切换到 `ProcessingEvent` 的实现。我们的自定义事件需要扩展 `jdk.jfr.Event` 抽象类。它包含一个参数 `id`。我们可以使用一些额外的标签来改进 JFR 图形工具中的事件呈现。事件将在 `@Name` 注解中设置的名称和 `@Category` 注解中设置的类别下可见。我们还需要使用 `@Label` 注解参数以将其作为事件的一部分可见。

```java
@Name("ProcessingEvent")
@Category("Custom Events")
@Label("Processing Time")
public class ProcessingEvent extends Event {

  @Label("Event ID")
  private Integer id;

  public ProcessingEvent(Integer id) {
    this.id = id;
  }

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

}
```

当然，我们的应用程序将生成许多用于分析和监控的标准 JFR 事件。但我们也可以监控我们的自定义事件。

## 构建应用镜像并在 Kubernetes 上部署

一旦我们完成实现，就可以构建 Spring Boot 应用程序的容器镜像。Spring Boot 带有一个基于 Cloud Native Buildpacks 构建容器镜像的功能。在 Maven `pom.xml` 中，您将在 `build-image` id 下找到一个专用配置文件。一旦激活此类配置文件，它将使用 Paketo `builder-jammy-base` 镜像构建镜像。

```xml
<profile>
  <id>build-image</id>
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <configuration>
          <image>
            <builder>paketobuildpacks/builder-jammy-base:latest</builder>
            <name>piomin/${project.artifactId}:${project.version}</name>
          </image>
        </configuration>
        <executions>
          <execution>
            <goals>
              <goal>build-image</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</profile>
```

在运行构建之前，我们应该在本地机器上启动 Docker。之后，我们应该执行以下 Maven 命令:

```bash
$ mvn clean package -Pbuild-image -DskipTests
```

通过激活 build-image 配置文件，Spring Boot Maven 插件构建我们应用程序的镜像。您应该获得类似下面显示的结果。在我的例子中，镜像标签是 `piomin/callme-service:1.2.1`。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-15.51.48.png?resize=768%2C277&ssl=1)

默认情况下，Paketo Java 构建包使用 BellSoft Liberica JDK。使用 [Paketo BellSoft Liberica Buildpack](https://github.com/paketo-buildpacks/bellsoft-liberica)，我们可以通过使用 `BPL_JFR_ENABLED` 环境变量轻松地为容器启用 Java 飞行记录器。为了为 Cryostat 暴露数据，我们还需要启用 JMX 端口。理论上，我们可以使用 `BPL_JMX_ENABLED` 和 `BPL_JMX_PORT` 环境变量。然而，该选项包括一些额外的配置到 java 命令参数中，这会破坏 Cryostat 发现。这个问题已经在这里描述过了。因此，我们将使用 `JAVA_TOOL_OPTIONS` 环境变量直接在运行命令上设置所需的 JVM 参数。

> 与其为发现暴露 JMX 端口，不如将 Cryostat 代理包含在应用程序依赖项中。在这种情况下，我们应该在 Kubernetes 部署清单中设置 Cryostat API 的地址。但是，我更倾向于一种不需要应用程序端任何更改的方法。

现在，让我们回到 Cryostat 应用程序发现。Cryostat 能够自动检测暴露 JMX 端口的 Pod。它需要 Kubernetes 服务的具体配置。我们需要将端口的名称设置为 `jfr-jmx`。理论上，我们可以在任何我们想要的端口上公开 JMX，但对我来说，除 `9091` 以外的任何其他端口在 Cryostat 上都会导致发现问题。在 `Deployment` 定义中，我们必须将 `BPL_JFR_ENABLED` 环境变量设置为 `true`，并将 `JAVA_TOOL_OPTIONS` 设置为 `-Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=9091`。

k8s/deployment-jfr.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: callme-service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: callme-service
  template:
    metadata:
      labels:
        app: callme-service
    spec:
      containers:
        - name: callme-service
          image: piomin/callme-service:1.2.1
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
            - containerPort: 9091
          env:
            - name: VERSION
              value: "v1"
            - name: BPL_JFR_ENABLED
              value: "true"
            - name: JAVA_TOOL_OPTIONS
              value: "-Dcom.sun.management.jmxremote.port=9091 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false"
---
apiVersion: v1
kind: Service
metadata:
  name: callme-service
  labels:
    app: callme-service
spec:
  type: ClusterIP
  ports:
  - port: 8080
    name: http
  - port: 9091
    name: jfr-jmx
  selector:
    app: callme-service
```

让我们将部署清单应用到 `demo-jfr` 命名空间:

```bash
$ kubectl apply -f k8s/deployment-jfr.yaml -n demo-jfr 
```

以下是我们的 `callme-service` 应用程序的 Pod 列表:

```bash
$ kubectl get po -n demo-jfr -l app=callme-service -o wide
NAME                     READY   STATUS    RESTARTS   AGE   IP           NODE  
callme-service-6bc5745885-kvqfr   1/1     Running   0        31m   10.134.0.29   worker-cluster-lvsqq-1  
```

## 使用带 JFR 的 Cryostat

### 查看默认控制面板

Cryostat 会自动检测所有与公开 JMX 端口的 Kubernetes 服务相关的 Pod。一旦我们切换到 Cryostat 控制台，我们将在“目标”下拉菜单中看到我们的 Pod 名称。默认控制面板显示说明 CPU 负载、堆内存使用情况和正在运行的 Java 线程数的图表。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-16.33.23.png?resize=768%2C372&ssl=1)

然后，我们可以转到“录制”部分。它显示了为在 Kubernetes 上运行的我们的应用程序生成的活动录制列表。默认情况下，Cryostat 为每个检测到的目标创建并启动一个录制。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-18.03.16.png?resize=768%2C314&ssl=1)

我们可以展开所选的记录以查看详细视图。它提供了一个总结面板，划分为几个不同的类别，如堆、内存泄漏或异常。它使用黄色高亮警告，使用红色高亮问题。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-17.19.22.png?resize=768%2C433&ssl=1)

我们可以显示每个案例的详细描述。我们只需要点击选定的具有问题名称的字段。详细描述将在上下文菜单中出现。

### 创建和使用自定义事件模板

我们可以通过定义新的事件模板来创建自定义录制策略。首先，我们需要转到“事件”部分，然后转到“事件模板”选项卡。有三个内置模板。我们可以将其中每个模板用作自定义模板的基础。在决定选择哪一个后，我们可以将其下载到我们的笔记本电脑上。默认的文件扩展名是 `*.jfc`。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.25.28.png?resize=768%2C283&ssl=1)

为了编辑 `*.jfc` 文件，我们需要一个名为 JDK Mission Control 的特殊工具。每个供应商都为其 JDK 分发提供这样的工具。在我们的例子中，它是 BellSoft Liberica。一旦我们在笔记本电脑上下载并安装了 Liberica Mission Control，我们应该转到窗口 -> 飞行记录模板管理器。  

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.26.09.png?resize=768%2C230&ssl=1)

使用飞行记录模板管理器，我们可以导入和编辑已导出的事件模板。我为“垃圾收集”、“分配分析”、“编译器”和“线程转储”选择了更高的监控。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.28.27.png?resize=768%2C722&ssl=1)

一旦新的模板就绪，我们应该使用所选名称保存它。对我来说，它是“Continuous Detailed”名称。之后，我们需要将模板导出到文件。  

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.29.16.png?resize=768%2C570&ssl=1)

然后，我们需要切换到 Cryostat 控制台。我们必须导入新创建的模板并导出到 `*.jfc` 文件。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.30.26.png?resize=768%2C468&ssl=1)

导入模板后，您应该在“Event Templates”部分中看到新的策略。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.31.06.png?resize=768%2C301&ssl=1)

我们可以根据自定义的“Continuous_Detailed”模板创建录制。过一段时间后，Cryostat 应该收集为在 Kubernetes 上运行的应用程序生成的 Java 飞行记录器的数据。然而，这次我们想使用 Liberica Mission Control 而不是仅仅使用 Cryostat 控制台进行一些高级分析。因此，我们将 recording 导出到 `*.jfr` 文件。这样的文件可以导入到 JDK Mission Control 工具中。 

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-22.59.43.png?resize=768%2C347&ssl=1)

## 使用 JDK Mission Control 工具

让我们使用 Liberica Mission Control 打开导出的 `*.jfr` 文件。一旦我们这样做，我们就可以分析与 Java 应用程序性能相关的所有重要方面。我们可以显示按对象类型分配的内存表。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-23.17.07.png?resize=768%2C339&ssl=1)

我们可以显示正在运行的 Java 线程列表。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-23.17.42.png?resize=768%2C333&ssl=1)

最后，我们转到“事件浏览器”部分。在“自定义事件”类别中，我们应该找到在 `ProcessingEvent` 类上的 `@Label` 注释确定的名称下的自定义事件。我们可以看到所有生成的 JFR 事件的历史记录，以及持续时间、启动时间和处理线程的名称。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/02/Screenshot-2024-02-12-at-23.19.20.png?resize=768%2C335&ssl=1)

## 最后的思考

Cryostat 帮助您在大规模的 Kubernetes 上管理 Java 飞行记录器。它提供了一个图形控制台，允许监控通过 JMX 公开 JFR 数据的所有 Java 工作负载。重要的是，即使应用程序崩溃后，我们也可以导出存档的监控报告并使用像 JDK Mission Control 这样的高级工具对其进行分析。

<!-- 云原生构建包 cryostat Java java 飞行记录器 JFR jmc Kubernetes openshift paketo -->
