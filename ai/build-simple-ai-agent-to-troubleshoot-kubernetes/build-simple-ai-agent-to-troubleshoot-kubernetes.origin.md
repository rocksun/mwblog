Itâs finally happening! AI assistants are here to help us talk to the machines. And yes - of course they can help us with Kubernetes too.

Hereâs how you can build your own (albeit very basic) Kubernetes troubleshooting assistant using the recently released AutoGen v0.4 AgentChat functionality.

## AutoGen v0.4
**AutoGen** is a leading open source agentic software framework which has just received a major overhaul with the release of version 0.4. One of the changes in the new version is the addition of the **AgentChat** layer which makes building helpful assistants much easier. The following is a diagram of the new AutoGen 0.4 layered architecture:
![autogen v0.4](https://cdn.prod.website-files.com/635e4ccf77408db6bd802ae6/67f61be9a6941ce2cc996f90_AD_4nXfM9r3ycxjRYfWdOXtkGrQNYmaeG1FZ9kf4_9JXkl9ILRZFe7Tshj9nlIyBY49vrCMF7VjFFncV_ezlW1DMXeXB7nDNeHXME7e2hyEGY8lu091UCGkJ1sb52hntI9k3UcBZG7SwSg.png)
## Build a Team of Agents
AgentChat provides us with user-friendly abstractions that help create AI agents and group them into teams so they can all work together towards a common goal.

Creating an agent is as simple as:

`agent = AssistantAgent(name="my_agent",llm_client=llm_client)`
And putting agents into a team can look something like this:

```
team = RoundRobinGroupChat([agent1,agent2],
termination_condition=termination)
stream = team.run_stream(task="Do something useful.")
```
â

## Using LLMs
The way agents basically work is by sending a task to a model and providing the tools that can help with task completion. LLM predicts the correct tool commands to complete the tasks, the agent calls the tools, returns the output to the LLM and the model predicts what the correct resolution for the task is.

â

![LLMs](https://cdn.prod.website-files.com/635e4ccf77408db6bd802ae6/67f61be9b1bafb58f0b09c5c_AD_4nXduCyh0C9xzprdD8MiwxZ-arzHTn9uWKft-bf666tj89I5sPL0jnE1X17kNc5dxWAA3AiHLVDK7Mr134Mr3-hQqQcCf29OisUjuu-hY6fFRNX0n3CgXRgMgN_jIQOVMadt31Rf4qA.png)
â

So we need to connect our agent to a model. We could,could of course use OpenAI, Claude or one of the other big names, but that would typically mean signing up and eventually paying them money. All just to play with open source?! Definitely not! Instead weâre gonna use [Ollama](https://ollama.com/) with an open-weights, free to use model. Luckily nowadays thereâs no shortage of lightweight models that one could run inference on - even without a GPU. For this example, Iâm using the âqwen2â model, but you can use any other model of your choice. And yes, you can also use Gemini for free if you donât mind reaching out to Google for simple Kubernetes troubleshooting. AutoGen supports all of [the major LLM providers](https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/tutorial/models.html):Â

## AgentChat with Ollama
Install Ollama by running `brew install ollama`
if youâre on a Mac or by following [the official installation instructions](https://ollama.com/download) for your OS of choice.Â

Once installed - pull the model: `ollama pull qwen2`
and then serve it by running: `ollama serve`
&.

In order to instantiate a model from our code we will use the [OllamaChatCompletionClient](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.models.ollama.html#autogen_ext.models.ollama.OllamaChatCompletionClient) object with the following parameters:

```
model_client = OllamaChatCompletionClient(model=âqwen2â,
keep_alive="60m", response_format=StructuredOutput)
```
â

## Creating the Agent(s)
Once we have the model available we can create our helpful assistant by using AgentChatâs AssistantAgent - the built-in agent that uses a language model and has the ability to use tools.

```
agent = AssistantAgent(
name="kaia",
model_client=model_client,
tools=[tool],
system_message="""You are a Kubernetes troubleshooting agent.
When asked about a resource but no namespace is specified - you can run kubectl get resource_type -A and then analyze the output to find the resource name.
That's how you find the namespace where a resource is located.
If the resource is a pod - you MUST inspect the pod's logs for issues.
The correct command to do that is: kubectl logs <pod_name> -n <namespace>.
If a resource is not found in any namespace, inform me that it was not found.
""",
reflect_on_tool_use=True,
)
```
â

Here Iâm creating an agent named **kaia** (**K**ubernetes** AI A**gent), which uses the Ollama-based LLM client I created earlier and receives a quite detailed system prompt that explains how one should troubleshoot Kubernetes pods. (Took me about 20 iterations to come up with a prompt that leads to the least hallucinations possible). Iâm also telling it to reflect_on_tool_use which causes it to make another model inference using the tool call and result to generate a response.Â

I suppose modifying additional agent parameters can yield even better results but for this example Iâm sticking to the basics.

## Providing the Tools
As already discussed - an agent needs tools to do its job. In this simple example Iâm just giving it the access to my kubectl. For more advanced use cases - definitely take a look at one of the many Kubernetes [MCP](https://www.anthropic.com/news/model-context-protocol) servers created in the last couple of months. Here is an example of such a server created by Alexey Ledenev : [https://github.com/alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) .

But here Iâm just defining a function that calls `kubectl`
and wrap it in an AutoGen FunctionTool:

```
def call_kubectl(command: str) -> str:
"""Call any kubectl command in the current cluster context"""
if command == '':
return subprocess.check_output(['kubectl', ''])
if command.split()[0] != 'kubectl':
command = 'kubectl ' + command
return (subprocess.check_output(command.split()))
tool = FunctionTool(call_kubectl, description="Kubernetes Command Execution", strict=True)
```
â

## A Team of One
Thereâs a lot of talk on the internet these days about how with the help of GenAI one person can replace a whole team. Not sure how true this is for humans - after all we build teams not for productivity only.

But for AI agents it can definitely work. (even though thereâs also a notion that highly specialized AI agents deliver better results than a generic agent dealing with all of the work). Anyway a single-agent team is good enough for Kaia which has one purpose - troubleshooting Kubernetes. The easiest way to create such a team of one in AgentChat is by using [RoundRobinGroupChat](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.RoundRobinGroupChat)Â - a simple yet effective team configuration where all agents share the same context and take turns responding in a round-robin fashion.

## Adding a Human in the Loop
Of course we all envision a future where machines will not only find issues, but also fix them without asking us. And yet - right now AI is prone to hallucinations, so itâs highly desirable we review whatever it decides to do.The way to add a human reviewer in a team of agents is by creating a [UserProxyAgent](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.UserProxyAgent) :

`user_proxy = UserProxyAgent("user_proxy", input_func=input)`
â

## The Stop Word
Our agents will continue working until the task is completed. But when is that? AgentChat teams allow us to define termination conditions that allow agents to tell one another when itâs time to stop chatting and calling tools. In the case of Kaia Iâve decided itâs always nice to be grateful and polite when team work is involved - so my termination message is âThanks!â. There are also other possible ways to terminate an agent group chat: [TerminationCondition](https://microsoft.github.io/autogen/stable//reference/python/autogen_agentchat.base.html#autogen_agentchat.base.TerminationCondition). Note that we could also define the `max_turns `
argument to limit the total number of agent interactions.Â

So finally - letâs create our team:

```
termination_condition = TextMentionTermination("Thanks!")
team = RoundRobinGroupChat(
[agent, user_proxy],
termination_condition=termination_condition,
# max_turns=10
)
```
â

## Letâs Do The Work!
All we now need to do is get the userâs input - i.e the request for Kubernetes troubleshooting and run the team until the answer is found:

```
async def ainput(string: str) -> str:
await asyncio.to_thread(sys.stdout.write, f'{string}')
return await asyncio.to_thread(sys.stdin.readline)
async def main():
print("What do you want to know?");
prompt = await ainput("Prompt:\n")
# Ignoring warnings to clean up the output.
with warnings.catch_warnings():
warnings.simplefilter("ignore")
async for message in team.run_stream(task=prompt): # type: ignore
if type(message).__name__ == "TextMessage" or type(message).__name__ == "UserInputRequestedEvent":
if message.source not in ["user_proxy", "user"]:
print(message.content)
print("Type 'Thanks!' if you're done.\n")
asyncio.run(main())
```
â

Note how Iâm doing some message cleanup to prevent AgentChat from printing too much stuff to the console.

## Troubleshoot Kubernetes with AI
To run the code I came up with do the following:

```
`git clone https://github.com/otomato-gh/kaia
cd kaia
pip install -r requirements.txt
python3 kaia.py
`
```
â

And then prompt it with something like: âwhatâs the problem with the pod **dummy**?â

[Watch the following video to see kaia in action](https://youtu.be/85RZcMAPAeE?feature=shared). Then click [here](https://github.com/otomato-gh/kaia) to get the full code of this simple basic AI agent. Then run this in your own environment and let me know how it goes. What would you like to add? How much does it hallucinate? What LLM worked best for you?
Whatâs next? Iâll connect Kaia to voice recognition and will finally be able to actually whisper to my clusters. Exciting!

Looking forward to hearing from you.

â

![PerfectScale Lettermark](https://cdn.prod.website-files.com/634ebd5aab79d1fa815c5394/653e2cf7ae6bc5934456d4ab_CTA%20Logo.png)