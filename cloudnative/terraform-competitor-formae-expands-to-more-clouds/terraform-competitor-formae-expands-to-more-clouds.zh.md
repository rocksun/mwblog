去年年底，初创公司 Platform Engineering Labs 在[基础设施即代码](https://thenewstack.io/infrastructure-as-code/) (IaC) 领域[引起轰动](https://thenewstack.io/kubecon-a-terraform-killer-built-on-apples-pkl/)，推出了一款名为 [Formae](https://platform.engineering/formae) 的新 IaC 平台，最初在[亚马逊云科技](https://aws.amazon.com/?utm_content=inline+mention)上可用。

本周，[Platform Engineering Labs](https://platform.engineering/) 的平台获得了包括[谷歌云平台](https://cloud.google.com/?utm_content=inline+mention)、[微软 Azure](https://aka.ms/modelmondays?utm_content=inline+mention)、[Oracle 云基础设施](https://www.oracle.com/developer?utm_content=inline+mention)和 [OVHcloud](https://thenewstack.io/how-ovhcloud-made-its-800-databases-more-efficient/) 在内等更多云平台的（测试版）支持。

该公司还发布了一款名为“基础设施构建者平台”的全新 AI 增强型基础设施工具管理软件。

Platform Engineering Labs 联合创始人兼首席执行官 Pavlo Baron 在一份声明中表示：“此次发布是为基础设施构建者而生，也关乎他们。从现在开始，您无需等待我们或任何其他人。为自己的基础设施构建，快速启动，快速迭代，快速扩展。无论是亲自动手，还是借助您的 AI 代理，都能实现。”

该公司正在向那些可能已经通过 IaC 管理部分组件，但希望将业务扩展到以前被认为难以用 IaC 管理的旧有传统资源的企业推广该平台。

## 模式安全变更管理

新平台及其配套的软件开发工具包 (SDK)，将允许用户通过新组件扩展其基础设施，提供模式安全性和易于理解的插件接口。

Platform Engineering Labs 联合创始人兼首席技术官 Zachary Schneider 在一份声明中表示：“工程师现在可以使用 AI 代理快速生成和修改按设计可靠的插件。”

Formae 软件旨在自动发现并将系统资源和系统更改编码成一个单一事实来源。

创始人声称，这种方法比行业领先的 IaC 解决方案 [HashiCorp 的 Terraform](https://thenewstack.io/ibm-hashicorp-sunsets-terraforms-external-language-support/) 提供了更优越的状态管理和更简便的迁移路径。

## 基础设施即代码

[基础设施即代码](https://thenewstack.io/introduction-to-infrastructure-as-code/)是一种将系统配置保存在文件中的实践，通常使用 [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) 或 [JSON](https://thenewstack.io/an-introduction-to-json/)，IaC 编排器随后将其用作指令集来部署基础设施。

IaC 承诺的优势是自动化部署（省时省力）以及防止系统漂移，即系统因手动干预等原因偏离其预期状态。

然而，Baron 在早前接受 *The New Stack* 采访时指出，一旦设置完成，IaC 的日常运维可能会令人头疼。IaC 文件很脆弱，它们很快变得复杂难懂，容易因影子 IT 工作而损坏，也容易出错。它们甚至无法指导所持有的值是否正确。

在 Formae 环境中，单个 IT 资源被[提取](https://docs.formae.io/)到一个版本化的声明性代码工件中，称为“forma”（拉丁语“形式”的单数），然后可以对其进行编程。

与 [Terraform](https://thenewstack.io/how-to-use-terraform-for-automation-at-the-edge/) 或 [Pulumi](https://thenewstack.io/pulumis-new-internal-developer-platform-accelerates-cloud-infrastructure-delivery/) 不同，Formae 中的状态管理不是由客户端本身处理，而是由[代理](https://www.youtube.com/watch?v=QHWCdTAKTgM)处理，以防止系统漂移。更改以部署安全补丁的相同方式进行，从而最大限度地减小每次更新的影响范围。

代码采用一种不寻常的语言编写，即苹果公司[内部开发](https://pkl-lang.org/blog/introducing-pkl.html)用于[管理](https://pkl-lang.org/blog/introducing-pkl.html)自身系统部署的 [Pkl](https://github.com/apple/pkl)。

Pkl 与 JSON 和 YAML 的不同之处在于，它强制用户为每种资源开发一个模式，并附带类型注解。通过类型注解，变量本身的类型值（有时甚至包括允许值的范围）都已经确定。因此，可以减少拼写错误并避免干扰操作。

[Formae 的开源版本现已在 GitHub 上发布](https://github.com/platform-engineering-labs/formae)。