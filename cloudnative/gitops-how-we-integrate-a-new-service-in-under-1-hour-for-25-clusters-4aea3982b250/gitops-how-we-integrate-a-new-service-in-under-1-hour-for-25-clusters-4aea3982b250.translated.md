# GitOps: How to Integrate a New Service into 25 Clusters in Under an Hour!
## Launching Otterize at Scale with GitOps via Argo CD

Fun fact: It took us less than an hour to integrate a new service, but it took us over four months to buy the license. So, your setup can be as fast as you want, but if your other processes are the bottleneck, then speed doesn't matter when introducing new tools! This isn't a finger-pointing exercise; there are many reasons for this, including procurement processes and data protection considerations.

Here you can see the grand goal we were trying to achieve and succeeded (at least we believe so)!

Why can't it be simpler, why does it take a whole hour? Trust me, I ask myself this question every time... !

The biggest challenge when adding a new service to your tech stack is how to integrate it seamlessly and at scale without sacrificing performance or scalability. Why is this so difficult? Well, every tool has its own quirks - especially when you're dealing with SaaS, self-hosted solutions, and needing to manage security credentials and tokens to establish secure connections.

We encountered this exact challenge when using [Otterize](https://otterize.com/). We're not just talking about deploying [Helm charts](https://github.com/otterize/helm-charts). We have to consider the entire setup - connecting to SaaS, deployment controllers, and so on.

**What we had to use:**
Since we're all about efficiency, we wanted to make things as streamlined as possible. Why? Because manually clicking through setup processes (aka [ClickOps](https://blog.equinix.com/blog/2022/12/01/what-is-clickops-and-how-can-you-prevent-it/)) leads to errors and inconsistencies. Plus, let's be honest - we're a little lazy. So, the goal was to automate everything as much as possible.

So, with the introduction out of the way, let's move on to the next step and outline what we actually wanted to set up.

# Setup
Here's what we wanted to achieve:

**Create Organization**: Set up an organization in Otterize. **Invite Users (2.2)**: Add the right people to the organization. **Set up Environment (2.1)**: Create the necessary environments for integration. **Create Integration with Kubernetes**: Connect to the cloud solution using `clientId` and `clientSecret`. **Protect Credentials**: Push `clientId` and `clientSecret` to Azure Key Vault. **Deploy Everything (Establish Connection)**: Deploy the Otterize stack, external Secrets operator, and any related secrets and
A quick note about Client ID: As of August 16, 2024,

`clientId`
cannot be referenced directly from secrets. So, for now, we manually add `clientId` to the cluster's values.
# How we did it: Step-by-step on the CLI
## 1. Create Organization
We started by creating an organization using the Otterize CLI:

`otterize organization create --format json `
The output was:

```json
[
{
"id": "org_h....",
"name": "Cryptocurrency Crusader Otters"
}
]
```
After that, we renamed it to match our cluster and stage:

`otterize org update "org_..." --name "cluster-name-stage"`
ID NAME IMAGE URL
Organization updated
Organization renamed to: cluster-name-stage
## 2.1 Create Environment
Next, we created the environment:

`otterize environment create --org-id "org_fcb967hrqz" --name test3 --labels test=true,env=test,env2=test2 --format json `
The output was:

```json
`[`
{
"appliedIntentsCount": 0,
"id": "env_ubpiqq7odl",
"labels": [
{
"key": "env",
"value": "test"
},
{
"key": "env2",
"value": "test2"
},
{
"key": "test",
"value": "true"
}
],
"name": "test2",
"namespaces": [],
"serviceCount": 0
}
]
```
## 2.2. Invite Users to the Organization
We sent out invites to team members:

`otterize invites --org-id "org_..." create --email "artem.lajko@...."`
The output was:

```
ID EMAIL ORGANIZATION ID INVITER USER ID STATUS CREATED AT ACCEPTED AT
inv_fn3evo2p7p artem.lajko@ org_ usr_u PENDING 2024-08-15
Invitation sent to artem.lajko@
```
## 4. Integrate with Kubernetes
Then, we created the Kubernetes integration:

`otterize integrations create --org-id "org_...." kubernetes --env-id env_6u... --name test-k8s --format json`
The output was:

Note: This CLI was built using a different version/revision of the Otterize Cloud API.
Please run otterize version for more information.
```json
[
{
"cluster": {
"id": "cluster_q..."
},
"components": {
"credentialsOperator": {
"status": {
"type": "NOT_INTEGRATED"
},
"type": "CREDENTIALS_OPERATOR"
},
"intentsOperator": {
"configuration": {
"awsIAMPolicyEnforcementEnabled": false,
"databaseEnforcementEnabled": false,
"egressNetworkPolicyEnforcementEnabled": false,
"globalEnforcementEnabled": false,
"istioPolicyEnforcementEnabled": false,
"kafkaACLEnforcementEnabled": false,
"networkPolicyEnforcementEnabled": false,
"protectedServices": [],
"protectedServicesEnabled": false
},
"status": {
"type": "NOT_INTEGRATED"
},
"type": "INTENTS_OPERATOR"
},

```
```json
"networkMapper": {
"status": {
"type": "NOT_INTEGRATED"
},
"type": "NETWORK_MAPPER"
},
"credentials": {
"clientId": "cli_...",
"clientSecret": "df5..."
},
"defaultEnvironment": {
"id": "env_6u..."
},
"id": "int_...",
"name": "clsuter-name-stage",
"organizationId": "org_...",
"type": "KUBERNETES"
}
]
## 5. 将凭据推送到 Azure Key Vault
我们将凭据安全地存储在 Azure Key Vault 中：

`az keyvault secret set --vault-name kv... --name "otterize-cloud-client-secret" --value ".." >/dev/null`
`az keyvault secret set --vault-name kv... --name "otterize-cloud-client-id" --value ".." >/dev/null`
## 6. 更新 Helm Chart 值
最后，我们使用必要的凭据更新了 Helm 图表：

```yaml
otterizeCloud:
  certificateProvider: otterize-cloud
  credentials:
    # 填写 clientId 和 clientSecret 以连接到 Otterize Cloud
    clientId: "cli_..."
    clientSecretKeyRef:
      secretName: otterize-cloud-credentials-secret-key
      secretKey: otterize-cloud-client-secret
```

我们使用 Python 模板引擎自动将 `clientId`
插入到我们的值中。

查看是否一切按预期工作：

当然，我们没有手动执行此操作 - 我们有一个模板引擎可以自动执行整个过程。运行脚本后，一切都顺利部署，没有出现任何问题。

这里您可以看到脚本（没有模板），但最终输出并执行的内容。

```bash
#!/bin/bash
# 设置环境变量
NAME="<cluster-name-stage>"
STAGE="<stage>"
SUBSCRIPTION="<...>"
KEY_VAULT_NAME="<...>"
LABELS="cluster=<>, env=<>,..."
OTTERIZE_CLOUD_INVITE_USERS="braveone@e-mail.com,lazy@e-mail.com,..."
GROUP_ID="..." #Azure AD 组（平台团队）
# 设置订阅的函数
set_subscription() {
az account set --subscription $SUBSCRIPTION
if [ $? -ne 0 ]; then
echo "无法设置 Azure 订阅。"
exit 1
fi
}
# 步骤 1：创建组织并将 ID 保存到 ORGA_ID 中
ORGA_ID=$(otterize organization create --format json | jq -r '.[0].id')
if [ -z "$ORGA_ID" ]; then
echo "无法创建组织。"
exit 1
fi
echo "组织 ID：$ORGA_ID"
# 步骤 2：使用提供的 NAME 重命名组织
otterize org update "$ORGA_ID" --name "$NAME"
if [ $? -ne 0 ]; then
echo "无法重命名组织。"
exit 1
fi
echo "组织已重命名为：$NAME"
# 步骤 3：遍历 OTTERIZE_CLOUD_INVITE_USERS，检索用户名，将电子邮件格式化为小写，并发送邀请
IFS=',' read -ra ADDR <<<"$OTTERIZE_CLOUD_INVITE_USERS"
for email in "${ADDR[@]}"; do
email=$(echo "$email" | xargs) # 修剪任何前导/尾随空格
# 从 Azure AD 获取用户的姓和名
user_info=$(az ad user show --id "$email" --query '{firstName:givenName,lastName:surname}' --output tsv)
# 提取姓和名
first_name=$(echo "$user_info" | awk '{print $1}')
last_name=$(echo "$user_info" | awk '{print $2}')
# 构建新的电子邮件格式并将其转换为小写
formatted_email=$(echo "${@hpa.hamburg.de">first_name}.${last_name}@hpa.hamburg.de" | tr '[:upper:]' '[:lower:]')
# 使用格式化的电子邮件发送邀请
otterize invites --org-id "$ORGA_ID" create --email "$formatted_email"
if [ $? -ne 0 ]; then
echo "无法向 $formatted_email 发送邀请。"
else
echo "已向 $formatted_email 发送邀请。"
fi
done
# 步骤 3b：通过 ID 从 Azure AD 组邀请用户
group_emails=$(az ad group member list --group "$GROUP_ID" --query "[].mail" -o tsv | tr '[:upper:]' '[:lower:]')
for email in $group_emails; do
if [ -n "$email" ]; then
# 使用直接来自组的电子邮件发送邀请
otterize invites --org-id "$ORGA_ID" create --email "$email"
if [ $? -ne 0 ]; then
echo "无法向 $email 发送邀请。"
else
echo "已向 $email 发送邀请。"
fi
fi
done
# 步骤 4：创建环境并将 ID 保存到 ENV_ID 中
ENV_ID=$(otterize environment create --org-id "$ORGA_ID" --name $STAGE --labels "$LABELS" --format json | jq -r '.[0].id')
if [ -z "$ENV_ID" ]; then
echo "无法创建环境。"
exit 1
fi
echo "环境 ID：$ENV_ID"
# 步骤 5：创建集成并将 CLIENT_ID 和 CLIENT_SECRET 保存起来
CREDENTIALS=$(otterize integrations create --org-id "$ORGA_ID" kubernetes --env-id "$ENV_ID" --name "$NAME" --format json | jq -r '.[0].credentials | "clientID=\(.clientId)\nclientSecret=\(.clientSecret)"')
CLIENT_ID=$(echo "$CREDENTIALS" | grep "clientID=" | cut -d'=' -f2)
CLIENT_SECRET=$(echo "$CREDENTIALS" | grep "clientSecret=" | cut -d'=' -f2)
if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
echo "无法创建集成或检索凭据。"
exit 1
fi
# 步骤 6：将客户端 ID 和客户端密钥推送到 Azure Key Vault
az keyvault secret set --vault-name "$KEY_VAULT_NAME" --name "otterize-cloud-client-id" --value "$CLIENT_ID" >/dev/null
if [ $? -ne 0 ]; then
echo "无法将客户端 ID 存储到 Azure Key Vault 中。"
exit 1
fi
az keyvault secret set --vault-name "$KEY_VAULT_NAME" --name "otterize-cloud-client-secret" --value "$CLIENT_SECRET" >/dev/null
if [ $? -ne 0 ]; then
```
```
echo "Failed to store Client Secret in Azure Key Vault."
exit 1
fi
echo "Client ID and Client Secret successfully stored in Azure Key Vault."
# Output the Client ID for the integration
echo "The Client ID for the integration is: $CLIENT_ID"

这看起来怎么样：

**理想吗？** 不，我们更希望直接从 Secret 中引用 clientId。
**这真的理想吗？** 不，最好的解决方案是使用 [Terraform provider](https://registry.terraform.io/browse/providers) 来简化工作流程，例如：

# 结论
借助 GitOps 与 Argo CD 以及 External Secrets 等工具，我们能够简化设置并保持懒惰（以一种好的、明智的方式）。您现在已经了解了我们如何将 Otterize 大规模集成到我们的工作流程中。

等等…

[meme](https://hicentrik.com/meme-marketing-guide-memevertising-2021/)]
什么是 Otterize 和 Otterize Cloud？如果您好奇，我在之前的博文中详细解释了这一点：

⭐️ [Kubernetes — 使用 Otterize 在 Azure 上自动执行工作负载 IAM](https://medium.com/itnext/kubernetes-automate-workload-iam-on-azure-with-otterize-860faa221eac) ⭐️

您还可以在这里找到大量博客文章：

# 联系方式
有问题、想聊天，还是想保持联系？跳过 Medium 评论，让我们在 [LinkedIn](http://www.linkedin.com/in/lajko) 上联系 🤙。别忘了订阅 [Medium Newsletter](/@artem_lajko/subscribe)，这样您就不会错过任何更新！
```