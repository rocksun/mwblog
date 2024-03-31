
<!--
title: 使用Gradio和GPT-4构建Kubernetes Pod医生
cover: ./cover.png
-->

Pod Doctor 允许您与 Kubernetes Pod 交互，检索信息并对 Pod 进行故障排除，并从 GPT-4 接收专家见解

> 译自 [Building a Kubernetes Pod Doctor with Gradio and GPT-4](https://www.codereliant.io/pod-doctor/)，作者 Team CodeReliant。

各位开发者，

和你们中的许多人一样，我一直在探索 AI 如何帮助我提高日常任务的生产力。因此，**“Pod Doctor”** 诞生了。这是一个小工具（只有 **180** 行！），它可以帮助我比自己动手更快地解决 Kubernetes Pod 故障。你可以在 [github](https://github.com/codereliant/pod-doctor?ref=codereliant.io) 上找到完整代码，在本入门教程中，我们将逐步了解如何为自己构建类似的工具。

我们将学习如何创建 [Gradio](https://www.gradio.app/?ref=codereliant.io) 聊天机器人 UI，集成 [Kubernetes Python 客户端](https://github.com/kubernetes-client/python?ref=codereliant.io)，并利用 GPT-4 的语言理解和推理能力。 ![](https://www.codereliant.io/content/images/2024/03/Pod-Doctor-1.png)

## 用户界面：

Pod Doctor 应用程序的用户界面使用 [Gradio](https://www.gradio.app/?ref=codereliant.io) 构建，这是一个用于创建可自定义 UI 组件和部署机器学习模型的 Python 库。该界面包含以下元素：

1. **标题：** 显示应用程序名称“Pod Doctor”的标签。
2. **聊天机器人：** 一个聊天机器人风格的界面，用于显示用户和语言模型之间的对话。
3. **命名空间下拉菜单：** 一个下拉菜单，允许用户选择他们想要交互的 Kubernetes 命名空间。
4. **Pod 下拉菜单：** 一个下拉菜单，其中填充了所选命名空间中可用的 Pod 列表。
5. **包含事件复选框：** 一个复选框，允许用户在提供给语言模型的信息中包含 Pod 事件。
6. **包含日志复选框：** 一个复选框，允许用户在提供给语言模型的信息中包含 Pod 日志。
7. **消息输入：** 一个文本输入字段，用户可以在其中输入他们的消息或查询。

```python
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Row():
        title = gr.Label("Pod Doctor")
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(height="600px")
        with gr.Column(scale=1):
            namespace = gr.Dropdown(
                list_namespaces(),
                label="Namespace",
                info="Select the namespace you want to check the pod in.",
                interactive=True,
            )
            pod = gr.Dropdown(
                [],
                label="Pod",
                info="Select the pod you want to interact with.",
                interactive=True,
            )
            include_events = gr.Checkbox(
                label="Include Events",
                info="Include the pod events.",
                interactive=True,
            )
            include_logs = gr.Checkbox(
                label="Include Logs",
                info="Include the pod logs.",
                interactive=True,
            )
    namespace.change(namespace_change, inputs=namespace, outputs=pod)
    with gr.Row():
        msg = gr.Textbox()

    def respond(message, chat_history, namespace, pod, include_events, include_logs):
        if not namespace or not pod or not message:
            chat_history.append((message or "Error", "Please select a namespace and pod."))
            return "", chat_history
        bot_message = call_llm(message, namespace, pod, include_events, include_logs)
        new_message = f"Namespace {namespace}, Pod: {pod}, Include Events: {include_events}, Include Logs: {include_logs} \n {message}"
        chat_history.append((new_message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot, namespace, pod, include_events, include_logs], [msg, chatbot])
```

随着我们继续学习本教程，你可能会遇到尚未定义的函数调用。但是，这些函数将在我们继续前进时进行解释和实现。

让我们定义一个函数，该函数负责在选择命名空间后更新 Pod 的下拉菜单：

```python
def namespace_change(value):
    """
    Returns a Dropdown widget populated with a list of pods based on the given value.

    Args:
        value (str): The namespace to filter the pods.

    Returns:
        gr.Dropdown: A Dropdown widget with choices populated from the list of pods.
    """
    pods = list_pods(value)
    return gr.Dropdown(choices=pods)
```

## Kubernetes 集成

Pod Doctor 应用程序使用 kubernetes Python [库](https://github.com/kubernetes-client/python?ref=codereliant.io) 与 Kubernetes 集群集成。以下函数处理与 Kubernetes API 的交互：

首先，我们需要导入 k8s 库并加载配置：

```python
from kubernetes import client, config

config.load_kube_config()
```

list_namespaces()：从 Kubernetes 集群中检索命名空间列表。

```python
def list_namespaces():
    """
    Retrieves a list of namespaces from the Kubernetes cluster.

    Returns:
        A list of namespace names.
    """
    v1 = client.CoreV1Api()
    namespaces = v1.list_namespace()
    return [namespace.metadata.name for namespace in namespaces.items]
```

list_pods(namespace)：列出指定命名空间中的所有 Pod。

```python
def list_pods(namespace):
    """
    List all pods in the specified namespace.

    Args:
        namespace (str): The namespace to list pods from.

    Returns:
        list: A list of pod names.
    """
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)
    return [pod.metadata.name for pod in pods.items]
```

**get_pod_info(namespace, pod, include_events, include_logs)：** 检索有关特定 Pod 的详细信息，包括事件和日志（如果需要）。

```python
def get_pod_info(namespace, pod, include_events, include_logs):
    """
    Retrieves information about a specific pod in a given namespace.

    Args:
        namespace (str): The namespace of the pod.
        pod (str): The name of the pod.
        include_events (bool): Flag indicating whether to include events associated with the pod.
        include_logs (bool): Flag indicating whether to include logs of the pod.

    Returns:
        dict: A dictionary containing the pod information, events (if include_events is True), and logs (if include_logs is True).
    """
    v1 = client.CoreV1Api()
    pod_info = v1.read_namespaced_pod(pod, namespace)
    pod_info_map = pod_info.to_dict()
    pod_info_map["metadata"]["managed_fields"] = None
    
    info = {
        "PodInfo": pod_info_map,
    }
    if include_events:
        events = v1.list_namespaced_event(namespace)
        info["Events"] = [
            {
                "Name": event.metadata.name,
                "Message": event.message,
                "Reason": event.reason,
            }
            for event in events.items
            if event.involved_object.name == pod
        ]
    if include_logs:
        logs = v1.read_namespaced_pod_log(pod, namespace)
        info["Logs"] = logs
    
    return info
```

## LLM 和 GPT-4

Pod Doctor 应用程序的核心是与 OpenAI 的 GPT-4 语言模型集成。

**call_llm 函数** 负责根据用户的留言、选定的命名空间、Pod 以及包含事件和日志的选项生成响应。

以下是 call_llm 函数的工作原理：

1. 调用 get_pod_info 函数来检索 Pod 信息，包括事件和日志（如果需要）。
2. create_prompt 函数通过将用户的消息与 Pod 信息相结合来生成提示消息。
3. 使用 openAiClient.chat.completions.create 方法调用 OpenAI API，传递提示消息和 GPT-4 模型。
4. 返回语言模型的响应，并在聊天机器人界面中显示。

```python
from openai import OpenAI
import yaml

openAiClient = OpenAI()

def create_prompt(msg, info):
    """
    Creates a prompt message with the given message and pod information.

    Args:
        msg (str): The main message for the prompt.
        info (dict): A dictionary containing pod information.

    Returns:
        str: The generated prompt message.
    """
    prompt = f"{msg}\n"
    prompt += f"Pod Info: \n {yaml.dump(info['PodInfo'])} \n"
    if info.get("Events"):
        prompt += f"Here are the last few events for the pod: \n"
        for event in info["Events"]:
            prompt += f"Event: {event['Name']}, Reason: {event['Reason']}, Message: {event['Message']}\n"
    if info.get("Logs"):
        prompt += f"Here are the last few logs for the pod: \n"
        prompt += info["Logs"]
    return prompt


def call_llm(msg, namespace, pod, include_events, include_logs):
    """
    Calls the Language Model to generate a response based on the given message, namespace, pod, and options.

    Args:
        msg (str): The user's message.
        namespace (str): The namespace of the pod.
        pod (str): The name of the pod.
        include_events (bool): Whether to include events in the pod information.
        include_logs (bool): Whether to include logs in the pod information.

    Returns:
        str: The generated response from the Language Model.
    """
    info = get_pod_info(namespace, pod, include_events, include_logs)
    prompt = create_prompt(msg, info)
    
    completion = openAiClient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a kubernetes expert, and will help the user with request below based on the context and info provided"},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content
```

## 用法

我们需要一段代码将所有内容包装在一起：

```python
if __name__ == "__main__":
demo.launch()
```

```bash
export OPENAI_API_KEY='sk-xxxxxxxxxx'
python app.py
```

要使用 Pod Doctor 应用程序，请按照以下步骤操作：

1. 确保已设置本地 Kubernetes 配置，请尝试 kubectl cluster-info
2. 从“命名空间”下拉列表中选择所需的 Kubernetes 命名空间。
3. 从“Pod”下拉列表中选择要交互的 Pod。
4. 可选：如果要将 Pod 事件和日志包含在提供给语言模型的信息中，请选中“包含事件”和“包含日志”复选框。
5. 在文本输入字段中键入您的消息或查询，然后按 Enter。
6. 该应用程序将在聊天机器人界面中显示 GPT-4 语言模型的响应。

让我们尝试部署一个探测配置中端口错误的 Pod，并要求 Pod Doctor 为我们进行故障排除。

以下是我们将应用的错误 nginx Pod：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80
      livenessProbe:
        httpGet:
          path: /
          port: 81
      readinessProbe:
        httpGet:
          path: /
          port: 81
```

应用此 yaml 后，我们转到我们的应用程序，选择我们应用它的命名空间，选择包含事件和日志，并在文本框中输入 `troubleshoot`，按 Enter 键，然后见证奇迹：

![](https://www.codereliant.io/content/images/2024/03/image-1.png)

正如我们所见，Pod Doctor 能够成功对 Pod 进行故障排除，并提供根本原因解决方案。

## 结论

通过结合[Gradio](https://www.gradio.app/?ref=codereliant.io)的强大功能来构建用户界面，[Kubernetes Python 库](https://github.com/kubernetes-client/python?ref=codereliant.io) 来与 Kubernetes Pod 交互，以及 GPT-4 的高级语言理解能力，**Pod Doctor** 应用程序提供了一种强大且直观的方式来与 Kubernetes Pod 交互并对其进行故障排除。

您可以在[github](https://github.com/codereliant/pod-doctor?ref=codereliant.io)中找到完整代码。

