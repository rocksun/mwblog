<!-- 

# CI/CD中SBOM的实用方法第二部分——部署Dependency-Track
 -->

本文介绍如何利用OWASP的Dependency-Track存储和分析软件清单，以识别开源组件中的安全漏洞。它指导如何在生产环境中部署Dependency-Track，并总结这个平台的优缺点。

译自 [A Practical Approach to SBOM in CI/CD Part II — Deploying Dependency-Track](https://itnext.io/a-practical-approach-to-sbom-in-ci-cd-part-ii-deploying-dependency-track-18fbb54d83b9) 。

## 什么是 Dependency-Track？

[Dependency-Track](https://dependencytrack.org/)是一个由OWASP支持的开源持续SBOM分析平台。它的官方描述如下:

> Dependency-Track是一个智能[**组件分析**](https://owasp.org/www-community/Component_Analysis)平台，允许组织识别和降低软件供应链中的风险。Dependency-Track采用了一种独特且非常有益的方法，那就是利用[**软件清单(SBOM)**](https://owasp.org/www-community/Component_Analysis#software-bill-of-materials-sbom)的功能。这种方法可以实现传统的软件组成分析(SCA)解决方案无法实现的功能。

从实际角度来看，Dependency-Track根据上传的SBOM跟踪项目及其关联组件。该平台由以下部分组成:

- **API服务器**
- **托管UI静态文件前端服务器**

此外，该平台利用数据库存储其数据。默认情况下使用内嵌的H2数据库，但在生产环境中，建议使用PostgreSQL或Microsoft SQL Server。

可以通过web应用程序UI或公开的API上传SBOM。就API而言，它可以在CI/CD阶段自动更新项目和上传SBOM。下面是一个根据提供的SBOM识别漏洞的项目表示:

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*eA40Ne5bAfNiZ8VEz8TDGg.png)

*在Dependency-Track UI中审核项目漏洞视图*

此外，Dependency-Track使用[漏洞预测评分系统](https://www.first.org/epss/)(EPSS)，用于估计软件漏洞被利用的可能性(概率)。EPSS可用于优先进行补救工作排定。

Dependency-Track默认配置使用的漏洞源包括：

- 国家漏洞数据库（National Vulnerability Database），
- GitHub Advisories，
- Google OSV Advisories(Beta)

漏洞数据库定期更新，默认每24小时一次。

此外，Dependency-Track支持基于漏洞和许可信息设置安全策略并通知违规情况。例如，可以制定只允许特定许可证的策略，示例如下：

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*s35YKOOM_209c4X95O1kPw.png)

最后，Dependency-Track集成众多功能，从漏洞管理流程实现的角度非常有价值。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/0*WJtc8jbBPEfpdth2.png)

*Dependency-Track 集成*

## 使用Docker Compose在开发/本地环境部署Dependency-Track

了解Dependency-Track基本信息后，在本地测试一下是个好主意!

实际上，可以用文档提供的[Docker Compose](https://docs.dependencytrack.org/getting-started/deploy-docker/#docker-compose-automated--orchestration)轻松部署该平台。但考虑到H2不适合生产，我调整了Compose，改为添加PostgreSQL数据库，也建议开发/本地环境使用PostgreSQL，使环境一致。

我准备了下列Docker Compose内容，可以保存到docker-compose.yaml中:

```yaml
version: '3.7'

#####################################################
# This Docker Compose file contains three services
#    Dependency-Track API Server 4.8.2
#    Dependency-Track FrontEnd 4.8.1
#    PostgreSQL 16.0
#####################################################

services:
  dtrack-apiserver:
    image: dependencytrack/apiserver:4.8.2
    depends_on:
      - postgres-db
    environment:
      - ALPINE_DATABASE_MODE=external
      - ALPINE_DATABASE_URL=jdbc:postgresql://postgres-db:5432/${POSTGRES_DB}
      - ALPINE_DATABASE_DRIVER=org.postgresql.Driver
      - ALPINE_DATABASE_USERNAME=${POSTGRES_USERNAME}
      - ALPINE_DATABASE_PASSWORD=${POSTGRES_PASSWORD}
      - ALPINE_CORS_ENABLED=true
      - ALPINE_CORS_ALLOW_ORIGIN=${CORS_ALLOW_ORIGIN}
      - ALPINE_CORS_ALLOW_METHODS=GET， POST， PUT， DELETE， OPTIONS
      - ALPINE_CORS_ALLOW_HEADERS=Origin， Content-Type， Authorization， X-Requested-With， Content-Length， Accept， Origin， X-Api-Key， X-Total-Count， *
      - ALPINE_CORS_EXPOSE_HEADERS=Origin， Content-Type， Authorization， X-Requested-With， Content-Length， Accept， Origin， X-Api-Key， X-Total-Count
      - ALPINE_CORS_ALLOW_CREDENTIALS=true
      - ALPINE_CORS_MAX_AGE=3600
    deploy:
      resources:
        limits:
          memory: 12288m
        reservations:
          memory: 8192m
      restart_policy:
        condition: on-failure
    ports:
      - '8081:8080'
    volumes:
      - 'dependency-track:/data'
    restart: unless-stopped

  dtrack-frontend:
    image: dependencytrack/frontend:4.8.1
    depends_on:
      - dtrack-apiserver
    environment:
      - API_BASE_URL=http://localhost:8081
    ports:
      - "8080:8080"
    restart: unless-stopped

  postgres-db:
    image: postgres:16.0
    restart: always
    user: postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USERNAME}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL"， "pg_isready -d ${POSTGRES_DB} -U ${POSTGRES_USERNAME}"]
      interval: 1s
      timeout: 5s
      retries: 10
    ports:
      - 5432:5432

volumes:
  pgdata:
    driver: local
  dependency-track:
    driver: local
```

另外需要在.env文件中本地保存以下变量:

```bash
POSTGRES_USERNAME=dtrack
POSTGRES_PASSWORD=dtrack
POSTGRES_DB=dtrack
CORS_ALLOW_ORIGIN=*
```

需要注意的是，无论在开发还是生产环境中，都要调整证书变量并安全地存储。此外，`CORS_ALLOW_ORIGIN`变量应该设定为与托管Dependency-Track的域名相匹配，因为它会用于“Access-Control-Allow-Origin” HTTP头。在生产环境中，不建议为这个HTTP头使用通配符(*)。有关CORS的更多信息，可以参考[PortSwigger的一篇文章](https://portswigger.net/web-security/cors/access-control-allow-origin)。

现在，可以通过在同一目录下执行以下命令启动该平台:

```bash
docker compose --env-file .env up
```

几分钟后，应用程序就可以在 http://localhost:8080/ 上访问了。默认的用户名和密码是 admin:admin。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*Cg7svYjmNRO4QWmju3A4Iw.png)

*Login Panel — Dependency-Track*

## 在Kubernetes中部署Dependency-Track

可以使用[社区管理](https://github.com/DependencyTrack/dependency-track#deploying-on-kubernetes-with-helm)的[Helm](https://helm.sh/) Chart在K8s上部署该平台。 在写这篇文章时，Helm Chart使用了最新版本的Dependency-Track容器镜像，并使用了版本为10.10的PostgreSQL。

为了演示的目的，我决定在本地的Minikube上部署该平台。这对生产环境来说并不推荐，但足以展示如何将Dependency-Track部署到K8s。由于我的私人开发环境基于WSL2，我按照下面的文章在本地配置了Minikube：

[在WSL2上通过Minikube搭建Kubernetes [2023]](https://gaganmanku96.medium.com/kubernetes-setup-with-minikube-on-wsl2-2023-a58aea81e6a3?source=post_page-----18fbb54d83b9--------------------------------)

按照文章中的一系列命令后，我成功地在本地部署了Minikube。 在我的情况下，我需要使用Minikube CLI配置4个CPU来创建集群。 此外，我还需要启用NGINX Ingress插件。 相关命令如下:

```bash
minikube start --cpus=4
minikube addons enable ingress
```

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*8Rs1E4kkQr25TexaIrcsFQ.png)

*在本地启动Minikube*

准备好K8s环境后，需要安装Helm。Helm是Kubernetes的包管理器。各个系统的安装过程在[官方文档](https://helm.sh/docs/intro/install/)中都有描述。

由于我们已经安装了所有先决条件，我们可以通过执行以下命令开始实际部署Dependency-Track:

```bash
# add Helm repository with chart for Dependency-Track
# Helm chart is available at:
# https://github.com/evryfs/helm-charts/tree/master/charts/dependency-track
helm repo add evryfs-oss https://evryfs.github.io/helm-charts/

# deploy Dependency-Track in a namespace named dependency-track
helm install dependency-track evryfs-oss/dependency-track \
--namespace dependency-track \
--create-namespace \
--set ingress.enabled=true \
--set ingress.tls.enabled=true \
--set ingress.host=kubernetes.docker.internal # adjust the host
# I recommend to override below credentials used by PostgreSQL db in prod
# --set postgresql.postgresqlUsername=
# --set postgresql.postgresqlPassword=
```

可以注意到，我通过Helm install命令中的--set参数设置了一些图表变量。这些变量可以在[values.yaml](https://github.com/evryfs/helm-charts/blob/master/charts/dependency-track/values.yaml)中找到。

执行命令后，您应该会看到类似下面的输出:

```
NAME: dependency-track
LAST DEPLOYED: Sat Sep 23 13:54:11 2023
NAMESPACE: dependency-track
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
```

现在，让我们通过运行几条命令来验证资源是否已在K8s中部署:

```bash
$ kubectl get namespaces
NAME               STATUS   AGE
default            Active   19m
dependency-track   Active   2m42s
kube-node-lease    Active   19m
kube-public        Active   19m
kube-system        Active   19m

kubectl get pods --namespace=dependency-track
NAME                                         READY   STATUS    RESTARTS        AGE
dependency-track-apiserver-6b9c86776-djwx8   1/1     Running   2 (2m20s ago)   2m38s
dependency-track-frontend-55c79cdb4c-69rjl   1/1     Running   0               2m38s
dependency-track-frontend-55c79cdb4c-z4t8n   1/1     Running   0               2m38s
dependency-track-postgresql-0                1/1     Running   0               2m38s
```

部署可能需要几分钟时间，所以要耐心等待。 如果**状态**列中显示任何错误，为了调试，我建议使用以下命令获取pod的日志:

```bash
# get logs for the ${POD_NAME}
kubectl logs ${POD_NAME} --namespace=dependency-track

# get pod details with events shown at the bottom of output
# events section is useful when debugging pod start issues
kubectl describe pod ${POD_NAME} --namespace=dependency-track
```

当所有的pod都启动并运行后，您就可以通过指定的主机和Web浏览器访问Dependency-Track了。 在我的情况下，由于我在Minikube上运行它，所以我需要通过`minikube tunnel`命令将流量隧道传输到暴露的Ingress控制器。完成这些步骤后，我在浏览器中打开了该Web应用程序，使用默认凭据登录，并看到了以下 Dashboard:

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*SoI3Fis_qRjjssJjwRL3mQ.png)

*Dashboard — Dependency-Track*

## 总结

在这篇文章中，我介绍了Dependency-Track平台，重点概述了它的功能，以及使用Docker Compose和Kubernetes环境中的Helm Chart进行潜在部署的方法。 在生产环境中部署这些方法时，必须考虑进行额外的调整。 例如，您可能需要为Kubernetes Ingress获取有效的HTTPS证书，或者通过文件或CLI中的机密存储来安全管理敏感信息。 但是，这些调整非常具体，取决于您的环境和选择的方法。 我的主要目的是向您提供执行部署的基本概念。

让我们总结下该平台的优缺点:

**优点:**

- 免费开源，
- 可以通过UI和API上传SBOM，
- API丰富且文档完善，
- EPSS用于优先确定补救措施，
- 社区支持许多集成，
- 与其他类似解决方案相比，UI显得更加现代。

...以及[官方文档](https://docs.dependencytrack.org/#features)中还描述了许多其他功能。

**缺点:**

- 仅支持CycloneDX SBOM格式，
- 需要一定的部署和配置工作。

我希望您觉得这部分信息非常有价值和实用。如果您有使用Dependency-Track的经验，请告诉我它对您的工作效果如何，我对此非常感兴趣。

在下一篇文章中，我将介绍如何将SBOM填充到Dependency-Track中，并探索它的API功能。请继续关注更多精彩内容！