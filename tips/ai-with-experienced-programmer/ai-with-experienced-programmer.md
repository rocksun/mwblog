<!--
title: AI武装的老专家怎么写程序？
cover: ./cover.png
-->

有一些调查说明，AI 对于初级和有经验的程序员帮助最大。本文通过一个案例，展示了 AI 加持的经验如何发挥巨大的效益。我最近几年主要是用 Go 和 Python，所以对于 Java 的新动态并不是太确信。

## 需求

先聊聊需求：某系统有一个基于 Spring Boot 微服务 A，需要通过 Restful API 调用其他微服务。不过，在某些客户环境中，微服务 A 对接的是客户已经存在的服务，假定也是 Restful 风格的。我们希望在实施时尽可能避免对微服务 A 代码的修改，通过配置实现与客户现有服务的集成。

## 确认方案

作为一个老程序员，对这个问题的第一反应是质疑，这样点对点的集成是不是合适？客户要不要考虑 Service Mesh？客户有没有 ESB 吗？是不是应该搞一个网关专门干这个？好吧，这些都不考虑。由于还没拿到实际的代码，我决定先写一个原型，展示一下效果。

作为一个老 java 程序员，一定不会忘记当年遍地 XML 的情形，一如现在的 YAML 和 JSON 。当时各大组织，推出了许许多多关于 XML 的标准，其中有一个是 XSLT，可以实现 XML 到 XML 的格式转化。所以我想问问 json 时代有没有类似的？

于是我问 [Claude](https://claude.ai/) ：

![](https://yylives.cc/wp-content/uploads/2024/08/p1.png)

看来 Claude 非常推崇 [JOLT](https://github.com/bazaarvoice/jolt)，甚至直接给出了 Artifacts，效果相当经验。JOLT 这个名字就让我联想起了 XSLT，所以也是加分项。当然 Claude 还推出几个备选：

![](https://yylives.cc/wp-content/uploads/2024/08/p2.png)

简单的调研一下，JSONData 是 Node 的；jq 我了解的是个命令行的工具，可能不合适； JsonLogic 是个标准，支持许多语言；Apache Camel 好像很强，但是放在这里可能太重了；JSON Transform 不太确定是指的什么。

我确实没有要求必须是 Java 的库，其实我是希望有一个类似 XSLT 的标准，然后有一大堆支持的库。可现实是好像并没有。现在的企业级开发生态已经变了，不像以前有个大公司抱团的 JEE 标准，大家会一起商讨一些规范，然后共同推动了。

分析了项目的星星数量以及其他因素，还是觉得 JOLT 可能更好一点，恰好这是一个 Java 的库，而且也有其他语言的兼容版本，所以进入了下个阶段。

## AI 实现

我给了 Claude 一个还算详细的需求：

```
帮我写一个 spring boot 应用，可以使用配置文件中的jolt配置将一个对象对应的json转化成另一种格式，使用指定的 restful 方法，发送到另一个服务上。
```

![](https://yylives.cc/wp-content/uploads/2024/08/p3.png)

结果非常惊人，Claude 给了我完整的 Spring Boot 的代码，并且给了我完成这个测试所需的 application.yml ：

```yaml
// src/main/resources/application.yml
server:
  port: 8080

jolt:
  spec: |
    [
      {
        "operation": "shift",
        "spec": {
          "source": "target"
        }
      }
    ]

target:
  url: "http://example.com/api/endpoint"
  method: "POST"
```

已经很接近我想要的配置文件的样子了，所以我追加了需求：

![](https://yylives.cc/wp-content/uploads/2024/08/p4.png)

这里我打错字了，那个”高内聚“没意义。我的意思是每个 service 要对应不同的 joltSpecs，不过 Claude 没有被我的胡言乱言干扰，给出了新的配置：


```yaml
// src/main/resources/application.yml
server:
  port: 8080

jolt:
  specs:
    service1: |
      [
        {
          "operation": "shift",
          "spec": {
            "source": "target"
          }
        }
      ]
    service2: |
      [
        {
          "operation": "shift",
          "spec": {
            "foo": "bar"
          }
        }
      ]

target:
  urls:
    service1: "http://example1.com/api/endpoint"
    service2: "http://example2.com/api/endpoint"
  methods:
    service1: "POST"
    service2: "PUT"
```

很接近了，但是 target 在另一个配置下，略微显得不太严谨：

![](https://yylives.cc/wp-content/uploads/2024/08/p5.png)

此时得到的配置文件是：

```yaml
// src/main/resources/application.yml
server:
  port: 8080

services:
  service1:
    joltSpec: |
      [
        {
          "operation": "shift",
          "spec": {
            "source": "target"
          }
        }
      ]
    targetUrl: "http://example1.com/api/endpoint"
    targetMethod: "POST"
  service2:
    joltSpec: |
      [
        {
          "operation": "shift",
          "spec": {
            "foo": "bar"
          }
        }
      ]
    targetUrl: "http://example2.com/api/endpoint"
    targetMethod: "PUT"
```

太棒了，这个配置文件正是我想要的。对应的 JoltConfig.java 为：

```java
// src/main/java/com/example/jolttransformer/config/JoltConfig.java
package com.example.jolttransformer.config;

import com.bazaarvoice.jolt.Chainr;
import com.bazaarvoice.jolt.JsonUtils;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Configuration
@ConfigurationProperties(prefix = "services")
public class JoltConfig {

    private Map<String, ServiceConfig> services = new HashMap<>();

    public Map<String, ServiceConfig> getServices() {
        return services;
    }

    @Bean
    public Map<String, Chainr> chainrMap() throws IOException {
        Map<String, Chainr> chainrMap = new HashMap<>();
        for (Map.Entry<String, ServiceConfig> entry : services.entrySet()) {
            List chainrSpecJSON = JsonUtils.jsonToList(entry.getValue().getJoltSpec());
            chainrMap.put(entry.getKey(), Chainr.fromSpec(chainrSpecJSON));
        }
        return chainrMap;
    }
}
```

我在测试时，发现有一点问题，application.yml 中的配置没有读取到 services 中。这里 claude 犯了唯一的一个错误，其实这里不要加前缀了，直接去掉 `prefix = "services"` 即可。

其他文件：

```java
// src/main/java/com/example/jolttransformer/service/TransformerService.java
package com.example.jolttransformer.service;

import com.bazaarvoice.jolt.Chainr;
import com.bazaarvoice.jolt.JsonUtils;
import com.example.jolttransformer.config.JoltConfig;
import com.example.jolttransformer.config.ServiceConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Service
public class TransformerService {

    @Autowired
    private Map<String, Chainr> chainrMap;

    @Autowired
    private JoltConfig joltConfig;

    public void transformAndSend(String serviceName, String inputJson) {
        // Get the appropriate Chainr and ServiceConfig for the service
        Chainr chainr = chainrMap.get(serviceName);
        ServiceConfig serviceConfig = joltConfig.getServices().get(serviceName);
        if (chainr == null || serviceConfig == null) {
            throw new IllegalArgumentException("No configuration found for service: " + serviceName);
        }

        // Transform the input JSON using Jolt
        Object inputObject = JsonUtils.jsonToObject(inputJson);
        Object transformedObject = chainr.transform(inputObject);
        String transformedJson = JsonUtils.toJsonString(transformedObject);

        // Send the transformed JSON to the target service
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "application/json");
        HttpEntity<String> entity = new HttpEntity<>(transformedJson, headers);

        HttpMethod method = HttpMethod.valueOf(serviceConfig.getTargetMethod().toUpperCase());
        restTemplate.exchange(serviceConfig.getTargetUrl(), method, entity, String.class);
    }
}

// src/main/java/com/example/jolttransformer/controller/TransformerController.java
package com.example.jolttransformer.controller;

import com.example.jolttransformer.service.TransformerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TransformerController {

    @Autowired
    private TransformerService transformerService;

    @PostMapping("/transform/{serviceName}")
    public void transformAndSend(@PathVariable String serviceName, @RequestBody String inputJson) {
        transformerService.transformAndSend(serviceName, inputJson);
    }
}
```

所有的文件放到 Spring boot 项目里运行之后，果然实现了我的目标，外发的请求会根据 services 中的 JOLT 配置进行转化。

## 总结

很开心自己的经验发挥了一点点作用。对于新手，掌握好的方法，应该也能实现很好的效果。当然，基本的编程素养还是很重要，比如要对 Spring 框架的原理要有清楚的认识，否则就会陷入到那个小错误里了。

Claude 确实很强大，而我们程序员应该尽快的赶上这个潮流。

