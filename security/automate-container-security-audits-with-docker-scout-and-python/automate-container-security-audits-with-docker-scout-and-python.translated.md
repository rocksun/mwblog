# 使用 Docker Scout 和 Python 自动化容器安全审计

![使用 Docker Scout 和 Python 自动化容器安全审计的特色图片](https://cdn.thenewstack.io/media/2025/04/2df03d2c-bernd-dittrich-rpm6qvp_tgk-unsplash-1024x618.jpg)

[Bernd 📷 Dittrich](https://unsplash.com/@hdbernd?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/a-stack-of-green-and-red-containers-sitting-on-top-of-each-other-rPM6qVp_tgk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上。

安全审计在容器化应用程序管理中是必要的。然而，手动完成的审计可能需要大量时间，不一致且容易出错。自动化该过程可确保采取先发制人的安全方法，团队可以及时检测和解决漏洞。

Docker Scout [执行自动容器安全](https://thenewstack.io/docker-and-chainguard-join-forces-to-deliver-secure-containers/)分析。它会自动分析镜像中的漏洞并推荐补救措施。当与 Python 结合使用时，安全团队可以自动执行扫描、处理结果并将其发布到 CI/CD 管道和仪表板。

在本文中，您将学习如何：

- 设置 Docker Scout 以进行自动化。
- 使用 Python 启动扫描和结果解析。
- 将自动安全审计集成到 CI/CD 工作流程中。
- 使用 Python 创建安全仪表板。
- 遵循自动安全审计的最佳实践。

## 设置 Docker Scout 以进行自动化

要开始自动化安全审计，请安装和配置 Docker Scout。

### 安装 Docker Scout

Docker Scout 是 Docker Desktop 和 Docker CLI 的内置功能。它有助于分析[容器镜像的安全性](https://thenewstack.io/container-security-a-troubling-tale-but-hope-on-the-horizon/)问题。为了获得最佳性能，请运行以下命令安装最新版本：

```
docker scout update
```

如果您没有安装 Docker，只需下载并将其安装在您的桌面上。然后在您的系统上设置 Docker CLI。

### 运行手动漏洞扫描

了解如何在自动化扫描之前手动运行扫描非常重要。您可以使用以下命令来分析容器镜像：

```
docker scout quickview my-image:latest
```

此命令检查容器镜像 `my-image:latest` 并提供一个安全报告，列出镜像中发现的漏洞。

### 了解输出

扫描完成后将生成报告。它将包括：

- 常见漏洞和暴露 (CVE)
- 严重级别
- 推荐操作：提供旨在纠正或减少问题的建议。
- JSON 输出：可以使用 JSON 标记语言以自动形式提供结果。

要获得结构化的 JSON 输出，请运行：

```
docker scout quickview my-image:latest --format json > scan_results.json
```

示例输出：

```json
{ 
  "findings": [ 
    { 
      "id": "CVE-2023-12345", 
      "severity": "HIGH", 
      "description": "Buer overow vulnerability in XYZ package.", 
      "fixAvailable": true 
    }, 
    { 
      "id": "CVE-2023-67890", 
      "severity": "LOW", 
      "description": "Deprecated function usage in ABC package.", 
      "fixAvailable": false 
    } 
  ] 
}
```

此输出对于自动化至关重要，允许 Python 脚本有效地解析和处理安全数据。

## 使用 Python 自动化 Docker Scout 扫描

您可以使用 Python 以编程方式触发 Docker Scout 扫描和处理结果。

### 从 Python 运行 Docker Scout 扫描

```python
import subprocess
import json

def run_scan(image_name):
    command = ["docker", "scout", "quickview", image_name, "--format", "json"]
    result = subprocess.run(command, capture_output=True, text=True)
    return json.loads(result.stdout)

image = "my-image:latest"
scan_results = run_scan(image)
print(json.dumps(scan_results, indent=4))
```

### 提取安全见解

```python
def extract_vulnerabilities(scan_results):
    vulnerabilities = []
    for finding in scan_results.get("findings", []):
        vulnerabilities.append({
            "id": finding["id"],
            "severity": finding["severity"],
            "description": finding["description"]
        })
    return vulnerabilities

security_issues = extract_vulnerabilities(scan_results)
print(security_issues)
```

### 生成安全报告

```python
with open("security_report.json", "w") as report_file:
    json.dump(security_issues, report_file, indent=4)
```

## 使用 Python 将 Docker Scout 与 CI/CD 管道集成

在 CI/CD 管道中自动化安全扫描可以改进 DevSecOps 实践。

### 在 GitHub Actions 中自动化扫描

```yaml
jobs:
  security_scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Run Docker Scout Scan
        run: |
          docker scout quickview my-image:latest --format json > scan_results.json
```
```markdown
```python
import smtplib
from email.mime.text import MIMEText

def send_email_report(issues):
    msg = MIMEText(json.dumps(issues, indent=4))
    msg["Subject"] = "Docker Scout Security Scan Report"
    msg["From"] = "security@company.com"
    msg["To"] = "devops@company.com"
    with smtplib.SMTP("smtp.example.com") as server:
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())

send_email_report(security_issues)
```

### 发送告警到 Slack

```python
import requests

def send_slack_alert(issues):
    webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    payload = {"text": f"Security Issues Found: {json.dumps(issues, indent=4)}"}
    requests.post(webhook_url, json=payload)

send_slack_alert(security_issues)
```

## 构建基于 Python 的 Docker Scout 安全仪表盘

基于 Web 的安全仪表盘为 DevOps 团队提供了一种交互式方式来监控实时漏洞。

### 使用 Flask/Django 可视化扫描结果

Flask 和 Django 允许我们构建 Web 应用程序。Flask 通常显示安全报告。它很轻量，适合简单的仪表盘，而 Django 功能更丰富，适合复杂的应用程序。

Flask 示例设置：

```python
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/scan_results")
def get_scan_results():
    with open("security_report.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```

## 为 DevOps 团队创建一个交互式仪表盘

- 使用像 Chart.js 或 DataTables.js 这样的 JavaScript 库来增强可视化效果。
- 实施过滤、排序和搜索功能，以实现更好的分析。
- 集成基于角色的访问控制 (RBAC)，以更安全地访问仪表盘。

### 使用 Python 和 Docker Scout 进行实时漏洞监控

- 使用 cron 任务调度定期扫描。或者，您可以采用后台任务队列（例如，Django 的 Celery 或 Flask 的 APScheduler）。
- 将扫描结果存储在[像 PostgreSQL 或 MongoDB 这样的数据库](https://thenewstack.io/how-to-plan-your-mongodb-upgrade/)中。
- 当检测到新问题时触发警报，与 Slack、电子邮件或日志记录平台集成。

## 自动化安全审计的最佳实践

以下是自动化安全审计的最佳方法：

-

### 安排定期安全检查

以定义的频率实施自动化安全扫描。设置 cron 任务、任务计划程序或 CI/CD 管道以每天和每周运行扫描。定期扫描可以更早地识别安全漏洞，并确保镜像是最新的。

示例 ([用于自动化扫描的 Linux Cron 任务](https://thenewstack.io/linux-how-to-use-cron-to-schedule-jobs/)):

```bash
0 2 * * * docker scout quickview my-image:latest --format json > /var/reports/security_scan.json
```

此扫描每天凌晨 2 点运行并保存结果。

-

### 将发现结果集成到漏洞管理工作流程中

安全漏洞不得无人处理。将扫描结果与问题跟踪平台（如 Jira 或 ServiceNow）集成，以便及时分配漏洞、进行监控和管理解决方案。

示例（Python 与 Jira 集成）：

```python
from jira import JIRA

def create_jira_ticket(issue):
    jira = JIRA("https://your-jira-instance.com", auth=("user", "password"))
    new_issue = jira.create_issue(
        project="SEC",
        summary=f"Security Issue: {issue['id']}",
        description=f"Severity: {issue['severity']}\nDetails: {issue['description']}",
        issuetype={"name": "Bug"}
    )
    return new_issue.key

for issue in security_issues:
    create_jira_ticket(issue)
```

上面的命令允许您验证安全漏洞是否在现有工作流程中得到有效管理。

-

### 确保符合安全策略

安全扫描需要满足合规性要求，并经过官员的审查。这些可能包括但不限于 CIS 基准、NIST 或 PCI-DSS 标准。策略规则定义和将镜像标记为不合规应自动化合规性验证。

示例（Docker Scout 策略执行）：

```bash
docker scout policy evaluate my-image:latest --policy my-security-policy.json
```
This enforces predefined security policies and ensures compliance.

-

### 设置实时监控和警报

设置配置以进行实时识别，以检测新兴威胁。使用日志和指标可视化工具（如 Splunk、ELK Stack 或 Prometheus）来监控和可视化安全数据。

示例（使用 Filebeat 将日志发送到 ELK Stack）：

```yaml
filebeat.inputs:
  - type: log
    paths:
      - /var/reports/security_scan.json

output.elasticsearch:
  hosts: ["http://localhost:9200"]
```

此设置确保安全发现结果被持续记录和监控。

## 最后的想法
Docker Scout与Python集成，可以自动执行容器安全审计。它优化了DevSecOps文化，并减轻了手动工作和管理漏洞的过程。[Python允许开发者自动化](https://thenewstack.io/pythons-automation-magic/)扫描和结果评估，并集成安全工作，从而最大限度地提高效率。

未来，由人工智能技术驱动的安全流程自动化可以进一步提高漏洞检测和修复能力。遵循这些最佳实践可确保容器安全，并使公司能够积极主动地应对新威胁。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。