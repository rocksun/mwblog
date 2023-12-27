<!--
title: Kubernetes 的配置文件处理
cover: ./cover.png
-->

本文介绍了 Kubernetes 中应用配置文件管理的最佳实践，并介绍了一些避免开发人员动手的配置文件处理技巧。

> 本文是作者多个 Kubernetes 改造项目经验的总结。希望通过本文可以让开发了解运维中配置文件管理需要考虑的问题，以及 Kubernetes 的实现方法，也能让运维了解 Java 应用的配置文件处理方式。

## 配置文件的方法论

[12 Factor](https://12factor.net/zh_cn/) 指的是部署到 PAAS 的应用应该具备的要素，其中有几条是关于配置文件相关的。

### 配置

将配置保存到“环境”中，而不是代码、属性文件、构建或应用服务器。

笔者确实遇到了以上几种情况。用代码保存配置显然不合适，不能每次配置变化时都去修改代码吧？确实有人将配置存放到 Jenkins 上，这样做的隐含意思就是如果要更改配置，需要重新构建应用，感觉不合适；许多 Spring 应用将不同环境的配置保存在不同的配置文件中，姑且不说添加环境可能也需要重新编译，让开发知道生产的配置也不是一个好的实践；将配置存放在应用服务器确实是以前常见的做法，但我的自动化运维经验告诉我，这样并不直观，也不利于自动化。

12 factor 中的环境特指“环境变量”，这在 PAAS 时代是最简单的方式。而在 Kubernetes 中，推荐使用 [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) 来管理配置，此时”环境“就是指的 Kubernetes ，更具体的就是 ConfigMap 。然后 Kubernetes 能够将 ConfigMap 的内容注入到应用的容器中。如果注入的内容比较简单，可以以环境变量的方式注入，如果注入的参数较多，可以将 ConfigMap 的内容变成文件，在应用运行时由 Kubernetes 注入到容器中文件系统中，应用可以按照读普通文件的方式读取，下面是一个 ConfigMap 的例子，我们首先定义一个 ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
data:
  application.yml: |-
    spring:
      datasource:
        name: test  #数据库名
        url: jdbc:mysql://localhost:3306/test #url
        username: root  #用户名
        password: 123456  #密码
        driver-class-name: com.mysql.jdbc.Driver  #数据库链接驱动
```

可以看到我们定义了一个名为 myconfigmap 的 ConfigMap，其中有一个 key 为 application.yml 的元素，其内容就是一个 Spring Boot 的配置文件。然后，我们可以在 Pod 中引用：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: openjdk:jre-alpine
    volumeMounts:
    - name: app-env-config
      mountPath: /apps/application.yml
      subPath: application.yml
  volumes:
  - name: app-env-config
    configMap:
      name: myconfigmap
```

可以看到上述配置将 ConfigMap 中 application.yml 的内容存放到了容器的 `/apps/application.yml`，应用可以按照普通文件方式读取 。

### 区分构建、发布和运行三个阶段

这是 12 factor 中另一项非常重要的因素，含义是基准代码 转化为一份部署需要以下三个阶段：

- **构建( Build )阶段** 是指将代码仓库转化为可执行包的过程。构建时会使用指定版本的代码，获取和打包 依赖项，编译成二进制文件和资源文件。
- **发布( Release )阶段** 会将构建的结果和当前部署所需配置相结合，并能够立刻在运行环境中投入使用。
- **运行( Run )阶段** （或者说“运行时”）是指针对选定的发布版本，在执行环境中启动一系列应用程序 进程。

许多组织在搞CI/CD时会将这三个步骤揉在一起，美其名曰"更加自动化"，其实这个因素关注的不是说这三个步骤能不能串在一起，而是说能不能拆分分别执行。如果不能拆分，可能会有几个问题：

- 在不同的环境发布应用时还需要重新**构建**，耽误时间。
- 不同环境**构建**的应用可能不同，可能会有未经测试的问题。
- 因为没有对二进制文件与配置进行“**发布**（确定唯一版本号）”，所以回退或切换版本存在困难。
- 缺少**发布**阶段，导致我们无法预先对变更进行更清晰的可视化，需要在**运行**前进行配置修改，一方面增加了版本更新时间，另一方面也会增加出错的可能性。

三个步骤的拆分解决了上述问题，如果使用 Kubernetes 三个步骤可以采用以下方式进行拆分：

- **构建( Build )阶段** – 构建镜像。
- **发布( Release )阶段** – 修订Helm Chart（包含镜像与配置）并打版本。
- **运行( Run )阶段** – 针对 Helm Chart 按照打的版本执行  helm upgrade 。

如果我们采用 ArgoCD 以 GitOps 的方式，那么会变成：

- **发布( Release )阶段** – 修订 ArgoCD 的 Application 定义（包含镜像以及配置）。
- **运行( Run )阶段** – 在 ArgoCD 界面上执行运行。

Helm Chart 和 ArgoCD 的篇幅太长，以后有机会再单独拿出来分享。但无论是哪个工具，一般也是利用 ConfigMap 来实现的配置文件管理。

### 开发环境与线上环境等价

这是一个比较广泛的原则，即希望我们的开发环境与生产环境要尽可能的一致，从而避免环境差异造成的问题。在配置文件层面，如果不同环境的配置参数的条目相近，但是值差别很大，可以考虑将配置文件的这些差异做成 Helm Chart 的变量。

## 单独的配置管理工具的优缺点

就像开发领域出现了许多不同编程语言的微服务框架一样，程序员们也创造了许多配置管理工具。例如 Nacos, ZooKeeper, Consul, Apollo 等。这些软件确实解决了大型组织中开发人员的配置管理问题，但是同微服务框架一样，当这些软件与 Kubernetes 配合使用时，可能需要做一些调整。

相对于 Kubernetes 的 ConfigMap 极其衍生工具的方案，这类配置管理工具的有一些不足：

- **本地开发**：使用这种配置管理工具时，即使是开发一个简单的应用，也需要提前部署好配置管理服务。如果是 ConfigMap 的方案，程序员本地开发时还可以继续使用文件，而在 Kubernetes 环境中，程序可以读到我们用 ConfigMap 配置的文件。
- **应用发布**：通过前面所说的区分“构建、发布和运行三个阶段”，我们可以实现软件版本和配置文件的绑定，从而可以实现更高效的版本切换。如果使用外部的配置管理工具，可能需要设计某个手段实现软件版本更新与配置更新的联动。
- **配置变更生效**：如果配置管理工具的配置发生变更，如果应用设置成自动刷新配置，可以实现不停服务的更新。使用配置文件也能达到类似的效果。应用也可以监听配置文件，如果 ConfigMap 的配置变更，会触发这个 ConfigMap 对应文件的变更，从而引发不停机的服务更新。而且，更好的一点是，如果应用做不到自动更新，我们可以通过一些手段，在 ConfigMap 发生变更时自动触发服务的重启，从而使配置自动生效。

因此，如果应用如果还在使用配置文件，这不是坏事，通过 ConfigMap 我们能够实现类似的能力，而且有可能更好用。

## 配置文件处理案例

又到了开发和运维部门调解时间。前面的探针功能强烈依赖开发，如果开发提供的探针接口不对，会让探测效果大打折扣。不过配置文件相对好一点，即使缺乏开发的配合，运维也能通过一些手段实现许多目标。

在我带过的传统架构转 Kubernetes 的项目中，大多数开发部门的应用还是比较规范的，往往微服务或应用都使用标准的配置文件。而且开发团队的领导也能从整体上分析问题，尝试从框架上做一些统一的调整，所以在 Kubernetes 层面，我们只需要做一些常规的配置即可。

不过，也确实有一些应用团队，可能是缺乏统一的设计，配置文件出现了百花齐放的局面，一个应用有几个、甚至几十个配置文件的情况。然后又可能是因为开发缺乏强有力的技术领导者或动力，所以不能很好的配合配置文件的改造，所以我们便只在 kubernetes 层面进行调整，力争实现前面说的“配置文件的方法论”的需求。以下就是几个案例。

### Spring Boot 标准配置

Spring Boot 本身就包含了对配置文件的支持，包括了如何将[配置文件外化](https://docs.spring.io/spring-boot/docs/2.1.13.RELEASE/reference/html/boot-features-external-config.html)，如果应用很乖巧的只需要一个配置文件，我们可以使用环境变量 `SPRING_CONFIG_LOCATION` 来指定配置文件，也可以添加命令行启动参数 `--spring.config.location=<configfile_path>`,下面是一个实际的例子：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: openjdk:jre-alpine
    env:
      - name: SPRING_CONFIG_LOCATION
        value: file:///apps/application.yml
    volumeMounts:
    - name: app-env-config
      mountPath: /apps/application.yml
      subPath: application.yml
      readOnly: true
  volumes:
  - name: app-env-config
    configMap:
      name: myconfigmap
```

其中 `application.yml` 的内容，已经通过 `myconfigmap` 这个 ConfigMap 部署到了 Kubernetes。

### Spring Cloud 的 bootstrap 配置

Spring Cloud 会根据 bootstrap.yml 的内容加载配置，我们可以通过 `--spring.cloud.bootstarp.location=<configfile_path>` 指定：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: openjdk:jre-alpine
    command: ["/usr/bin/java","-Xms512M","-Xmx512M","-jar","app.jar","--spring.cloud.bootstrap.location=/apps/bootstrap.yml"]
    volumeMounts:
    - name: app-env-config
      mountPath: /apps/application.yml
      subPath: application.yml
      readOnly: true
    - name: app-env-config
      mountPath: /apps/bootstrap.yml
      subPath: bootstrap.yml
      readOnly: true
  volumes:
  - name: app-env-config
    configMap:
      name: myconfigmap
```

### 通过 Tomcat ClassPath 读取配置

我们遇到的一个部署在 Tomcat 中的应用，它需要从 ClassPath 中读取一些配置，所以我们尝试通过 ConfigMap 中包含一份修改后的 Tomcat 的配置文件，使之能在指定的路径加载我们的应用配置文件，这个应用配置文件也是通过 ConfigMap 注入的。首先，我们看看准备一个修改的 `catalina.properties` 配置文件，其中修改的行为：

```properties
···
shared.loader=/usr/local/tomcat/addcp/
···
```

然后，我们使用 ConfigMap 资源包含 `catalina.properties` 文件：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ template "log4j2.fullname" . }}-env-config
data:
  log4j2.xml: |-
{{ tpl (.Files.Get .Values.log4j2.configFile) . | indent 4 }}
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-catalina-properties
data:
  catalina.properties: |-
{{ tpl (.Files.Get .Values.tomcat.catalinaFile) . | indent 4 }}

```

需要注意的是，上面的 ConfigMap 是用 Helm Chart 模板的语法，通过 `.Files.Get` 方法，我们可以加载文件系统里的 `catalina.properties` 文件，使之成为 ConfigMap 的一部分，然后通过 Helm 发布到 Kubernetes 里。

然后，我们在 Pod 模板的定义里，加载这些文件：

```yaml
          volumeMounts:
            - name: env-config
              mountPath: /apps/application.yml
              subPath: application.yml
            - name: log4j2-config
              mountPath: /apps/log4j2.xml
              subPath: log4j2.xml
            - name: storage-pvc
              mountPath: "/attachment"
            - name: catalina-properties
              mountPath: /usr/local/tomcat/conf/catalina.properties
              subPath: catalina.properties
            - name: setting-config
              mountPath: /usr/local/tomcat/addcp/config.setting
              subPath: config.setting
```

可以看到我们定义的 `catalina.properties` 挂载到了 Tomcat 目录 。另外定义了一个名为 setting-config 的 ConfigMap，将 config.setting 挂载到了 `/usr/local/tomcat/addcp/` 目录。这样，Tomcat 启动时就会将 `/usr/local/tomcat/addcp/` 视为 ClassPath，从而应用能够读到这个配置文件。

### 从可执行 Jar 包的 ClassPath 读取配置

可执行 Jar 包不能指定 ClassPath，所以我们想到的一个办法就是将配置文件动态的保存到 Jar 包里。首先，我们需要准备一个 `repackage.sh` 脚本：

```bash
#!/bin/bash
mkdir -p ./BOOT-INF/classes/properties/
cp lib/config.setting  ./BOOT-INF/classes/properties/
jar uf app.jar BOOT-INF/classes/properties/config.setting
```

然后我们通过 ConfigMap 将 `repackage.sh` 和 `config.setting` 挂载到容器中对应的目录，然后我们需要调整容器的启动命令：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  labels:
    apps: jar
spec:
  containers:
  - name: mypod
    image: openjdk:jre-alpine
    command: ["/bin/sh","-c"]
      args: ["sh lib/repackage.sh; /usr/bin/java -Xms512M -Xmx512M -jar app.jar --spring.cloud.bootstrap.location=/apps/lib/bootstrap.properties"]
    volumeMounts:
      - name: setting-config
        mountPath: /apps/lib/config.setting
        subPath: config.setting
      - name: repackage-shell
        mountPath: /apps/lib/repackage.sh
        subPath: repackage.sh
  volumes:
    - name: setting-config
      configMap:
        name: my-pod-setting-config
    - name: repackage-shell
      configMap:
        name: my-pod-repackage-shell
```

可以看到容易启动时会首先设法将配置文件注入到可执行 Jar 包中，然后再执行 Jar 包，实现了我们运行时指定配置文件的目标。