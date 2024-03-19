<!-- 
title: 使用JSON Resume写简历
cover: ./cover.png
-->

先通知大家一个消息，我又开始修改简历了，不过我觉得这次会有些不一样。有兴趣的朋友可以加我的微信 **rocksun21** ，一起探讨各种合作方式。

> 先做个广告，最近想组织一个 DevOps 培训，通过这个课程你可以学习到 Kubernetes, Harbor, Jenkins, Helm, ArgoCD 的安装和最佳实践，另外也能帮你理解开发和运维不同的的工作方式。最重要的是，是可以学习到一些适合中小企业的实践过的、**符合理论和最佳实践的流程**。具体时间和形式还没定，大家可以先加我的微信（备注 devops）进群讨论。

言归正传，最近就业市场好像非常严峻，不少人都在准备简历。市面上也有不少不错的工具，例如 LapisCV[^1]，这是一个 obsidian/Typora 的插件，可以直接用 Markdown 写简历；也可以考虑简单简历[^2]这样的收费产品，已经有了许多付费用户；如果愿意折腾，也可以考虑 Reactive Resume[^3] 这样的开源工具。

## 介绍

不过，今天介绍了的是 JSON Resume[^4]。这个工具其实我很久之前尝试过一次，当时生成的简历很多不满意的地方，所以也没实际用起来。不过这次觉得，有个 JSON 简历还是方便，所以决定再尝试一次，结果还不错，所以通过本文跟大家分享一下。

## 安装

JSON Resume 是一个 Node 项目，所以主要是首先要安装 Node，安装 18.* 版本的即可，这里就不详细讲了。不过强烈建议大家使用 nvm[^5] 管理 Node 版本，我作为一个半吊子前端开发，手上也有几个项目使用了不同的 Node 版本，偶尔还是需要用 nvm 切换下版本。

然后安装 resume-cli：

```bash
npm install -g resume-cli
```

## 安装主题

然后我们要安装主题。我第一次试用时觉得不爽，一个很重要的原因是没有看到舒服的主题，而且许多主题包含的元素并不一致，导致结果总是与预期不一致，所以这一次，我从一开始就先确定好了主题 actual[^6]。这个主题比较简约紧凑，正是我心目中的样子。只是，其中的章节标题都是英文，作为中文简历，还是需要调整一下。

我 fork 了 actual 项目，做了一个 actualzh[^7] 的主题，修改了其中的标题和日期样式。如果想要试用这个主题，可以按照以下步骤操作。

首先是下载编译这个项目：

```bash
git clone https://github.com/rocksun/jsonresume-theme-actual
cd jsonresume-theme-actual

npm install
npm install -g gulp
gulp
```

此时应该可以访问 `http://localhost:3000/` ，能看到简历说明一切正常。

## 开始写简历

准备一个目录，例如 resume ，其中写一个 resume.json ，内容为：

```json
{
    "basics": {
      "name": "岱军",
      "label": "云原生专家",
      "image": "",
      "email": "daijun@example.com",
      "phone": "(86)88866669999",
      "url": "https://yylives.cc",
      "summary": "近些年来主要带领云原生转型和相关的研发效能提升工作（见公众号“[云云众生s](https://mp.weixin.qq.com/s/pOOg9IC78zJ70uMQzkQUDA)”）。精通 Kubernetes 等云原生技术，熟练运用 DevOps、Scrum 和 Design Thinking 等方法论。技术功底全面，善于学习和处理问题，对于 ChatGPT 等生成式 AI 技术有比较深入的研究和应用。具备丰富的 Golang、Java、Python 以及前端项目经验。多年的 WebSphere 中间件产品专家工作经验，也曾经担任 BEA（后被 Oracle 收购） Dev2dev 社区 WebLogic 管理版块版主，精通各类 Java 中间件以及 Tuxedo 。精通研发过程的各个方面。早年也从事过自动化测试、软件配置管理和自动化运维等工作。",
      "location": {
        "address": "",
        "postalCode": "",
        "city": "青岛",
        "countryCode": "",
        "region": ""
      },
      "profiles": [
        {
          "url": "https://github.com/rocksun"
        }
      ]
    },
    "work": [
      {
        "name": "云云众生",
        "position": "云原生解决方案部总监",
        "location": "北京",
        "startDate": "2021/07",
        "endDate": "",
        "summary": "组建云原生团队，构建 DevOps 和平台工程平台，带领研发部门进行云原生转型，并形成解决方案推向给客户，负责重要客户的云原生服务售前工作。还开发了 Go 核心代码，组建了公司战略运维产品 Edith 的开发团队。",
        "highlights": ["完整的云原生 DevOps 方案","完整的平台工程方案","云原生的实战 DevOps 课程", "开源云原生数据库方案", "新一代可观测性方案", "基于 Go 的自动化运维产品", "引入大数据、全文检索、OCR和GenAI等技术"]
      }
    ],
    "volunteer": [
      {
        "organization": "Subversion 社区",
        "position": "Subversion 中文站站长",
        "url": "https://subversion.apache.org/",
        "startDate": "2004-01-01",
        "endDate": "2012-01-01",
        "summary": "Subversion(SVN)项目代码贡献者。建设 Subversion 中文站，组织维护官方文档的翻译，编写原创 SVN 教程。",
        "highlights": ["组织完成 Subversion 官方文档翻译工作", "为 Subversion 贡献代码", "参与 TortoiseSVN 项目", "独立完成 Subersion 中文站建设"]
      }
    ],
    "education": [
      {
        "institution": "中国海洋大学",
        "area": "数学与应用数学 和 计算机科学",
        "studyType": "本科"
      }
    ],
    "awards": [
      {
        "title": "软件企业经营技能人才",
        "date": "2023-09",
        "awarder": "北京软件和信息服务业协会"
      }
    ],
    "certificates": [
      {
        "name": "WLS-D11-8 J2EE Programming with servlets and JSPs Web Using BEA Weblogic Server",
        "date": "2004-11-26",
        "issuer": "BEA"
      }
    ],
    "skills": [
      {
        "name": "后端开发",
        "level": "专家",
        "keywords": ["Java", "Go", "Python"]
      },
      {
        "name": "中间件",
        "level": "专家",
        "keywords": ["WebLogic", "WebSphere", "JBoss"]
      },
      {
        "name": "方法论",
        "level": "专家",
        "keywords": ["Scrum", "DevOps", "Design Thinking"]
      },
      {
        "name": "云原生",
        "level": "熟练",
        "keywords": ["Kubernetes", "Jenkins", "ArgoCD", "Helm"]
      },
      {
        "name": "前端开发",
        "level": "熟练",
        "keywords": ["Angular", "VUE", "React", "NEXT.js"]
      },
      {
        "name": "云计算",
        "level": "熟练",
        "keywords": ["AWS", "阿里云", "华为云", "Azure"]
      }
    ],
  
    "projects": [
      {
        "name": "EasyDevOps 课程",
        "startDate": "2023/11",
        "endDate": "2024/3",
        "description": "EasyDevOps 是一套完整的云原生开源 DevOps 课程。这个课程为大家提供了一套 DevOps 平台参考架构，包含 Kubernetes, Jenkins, ArgoCD, Harbor, GitLab 等产品，融合各类云原生运维和开发的方法论，可以帮助开发和运维团队快速转向云原生 DevOps 环境。",
        "highlights": [],
        "roles":["项目经理"]
      },
      {
        "name": "Etude - 云原生数据库和中间件管理平台",
        "startDate": "2022/11",
        "endDate": "2023/3",
        "description": "根据 Kubernetes 下管理数据库的经验和最佳实践，使用 ArgoCD 和 Helm 构建了一套 Etude 云原生数据库和中间件管理平台。通过 Etude 可以一个 YAML 文件部署具备自动备份、可观测面板的高可用数据库和中间件，大大减轻数据库和中间件工程师的运维工作。\n\n 目前 Etude 已经支持了 MySQL、 PostgreSQL、MongoDB、ElasticSearch、Redis，达梦，openGauss 等数据库和中间件。另外，方案也参考了 KubeBlock 和 Percona 等云原生数据库平台。",
        "highlights": [],
        "roles":["项目经理"]
      },
      {
        "name": "Concerto - 统一可观测平台",
        "startDate": "2023/4",
        "endDate": "2023/11",
        "description": "许多传统的可观测系统可能只关注 Log, Metric 和 Trace 的某一方面。但是对于解决问题来说，有一个统一的可观测平台会更有价值。Concerto 是新一代的可观测解决方案，融合了 OpenTelemetry, eBPF 和 ClickHouse 等工具，能够更轻松地实现复杂的可观测能力。",
        "highlights": [],
        "roles":["项目经理"]
      }
    ],
    "interests": [
      {
        "name": "开源"
      },
      {
        "name": "宗教"
      },
      {
        "name": "电影"
      }
    ]
  }
  
```

然后在 resume 目录执行：

```
npm link E:\projects\rocksun\jsonresume-theme-actual
resume export resume.pdf --format pdf --theme actualzh
resume export resume.html --format html --theme actualzh
```

可以看到已经了有了 `resume.json` 和 `resume.pdf` 。

如果希望一边编辑一边看效果，可以执行 `resume serve --theme actualzh` ，这样可以弹出一个浏览器，每次保存 json 时都会刷新。不过，这个有点 bug ，经常需要重启一下才刷新。

## AI写简历

显然，编写 JSON 并没有 Markdown 那么舒服，将原来的简历搬运到 JSON 的框框里也不是那么轻松。可是我们现在是 AI 时代了，这个事情 AI 完成的相当出色。例如可以让 Claude 根据示例 JSON 格式，将你其他格式的简历，转化为 JSON 格式。我的第一份 JSON 简历就是这么得到的，效果相当令人满意。

[^1]: https://github.com/BingyanStudio/LapisCV "LapisCV"
[^2]: https://easycv.cn/ "简单简历"
[^3]: https://github.com/AmruthPillai/Reactive-Resume "Reactive Resume"
[^4]: https://jsonresume.org/ "JSON Resume"
[^5]: https://github.com/nvm-sh/nvm "nvm"
[^6]: https://github.com/davcd/jsonresume-theme-actual "Actual theme"
[^7]: https://github.com/rocksun/jsonresume-theme-actual "Actual Chinese theme"
