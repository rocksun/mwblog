# Magma Is Microsoft’s Foundation Multimodal Model for Agentic AI
![Featued image for: Magma Is Microsoft’s Foundation Multimodal Model for Agentic AI](https://cdn.thenewstack.io/media/2025/04/e74db13e-microsoft-magma-4-1024x576.jpeg)
There’s been a lot of excitement around [agentic AI](https://thenewstack.io/the-promises-of-agentic-ai-and-how-to-sidestep-challenges/) as of late, and with [Microsoft’s](https://news.microsoft.com/?utm_content=inline+mention) recently released [Magma](https://microsoft.github.io/Magma/), the company believes its new foundation AI model will empower AI agents to execute multimodal tasks efficiently in both digital and real-world contexts, whether via software or physical robots.

Arising from a collaboration between researchers at Microsoft, [KAIST](https://www.kaist.ac.kr/en/), the University of Maryland, the University of Wisconsin-Madison, and the University of Washington, Magma expands on prior work in [vision language models](https://huggingface.co/blog/vlms) (VLMs), making it a significant step forward for AI-powered automation.

More specifically, Magma is a [multimodal](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) vision-language-action (VLA) model that integrates visual perception, language comprehension and action reasoning, enabling AI systems to process images and text-based instructions in context, and to propose relevant actions.

“Magma is the first foundation model for multimodal AI agents,” [wrote](https://microsoft.github.io/Magma/) the team on Magma’s project page. “As the bedrock for multimodal agentic models, it possesses strong capabilities to perceive the multimodal world groundingly, and to take goal-driven actions precisely.

“By effectively transferring knowledge from freely available visual and language data, Magma bridges verbal, spatial and temporal intelligence to navigate complex tasks and settings across digital and physical world.”

![](https://cdn.thenewstack.io/media/2025/04/042ac26a-magma-1.png)
Via Microsoft Research.

## Vision-Language-Action Are All-In-One AI Models
Until recently, it was difficult for the programming underlying modern robotic control systems to adapt to the dynamic — and often chaotic nature — of the real world. For instance, a robot might be instructed to move to a specified spot in a factory to place something on a shelf, but if an unexpected object were placed in its way, the machine would likely stop and experience problems going around this unplanned obstacle if it was not explicitly programmed to do so.

A traditional robot might “see” the obstruction (vision), but may have trouble reasoning what to do next (language), and how to do it (action), as these tasks are tackled in a more disjointed way.

In contrast, the unified architecture and approach behind VLA models allows robots to handle these unplanned surprises in a human manner, by merging vision, language and action in one integrated process that enables robots to improvise on the fly. VLA models are essentially all-in-one AI models that allow robots to see their environment, understand what to do, and act in an integrated and adaptive way.

## Magma Closes the Gap
Created specifically as a multipurpose solution for robotic systems, Magma integrates real-time perception and action, enabling AI agents to take actions in multiple steps to autonomously control both software and robots, with minimal human intervention.

Magma is pre-trained on large numbers of various vision-language datasets, including images, text, videos and robotics data. Text is tokenized into tokens, while various types of visual data are encoded via a shared vision encoder. The resulting tokens are parsed by a large language model (LLM) that generates the outputs in verbal, spatial and action categories.

However, according to the researchers, Magma’s pre-training pipeline represents a significant improvement over its predecessors.

“Due to the dramatic difference among various digital and physical environments, separate VLA models are trained and used for different environments,” [wrote](https://www.microsoft.com/en-us/research/blog/magma-a-foundation-model-for-multimodal-ai-agents-across-digital-and-physical-worlds/) the Magma team in a post on the Microsoft Research Blog. “As a result, these models struggle to generalize to new tasks and environments outside of their training data. Moreover, most of these models do not leverage pre-trained vision-language (VL) models or diverse VL datasets, which hampers their understanding of VL relations and generalizability.

“Magma, to the best of our knowledge, is one of the first VLA foundation models that can adapt to new tasks in both digital and physical environments, which helps AI-powered assistants or robots understand their surroundings and suggest appropriate actions.”

![Two examples of how Magma converts videos to text.](https://cdn.thenewstack.io/media/2025/04/41957214-video-conversation-1024x480.png)
Two examples from the Magma project site show how the AI model converts video to text that answers user prompts.

Magma’s improved capabilities are due to the team’s novel training approach that focuses on two main annotation methods, developed by Microsoft Research, that are meant to give the model a more structured way to understand tasks in both navigating user interfaces and robotic manipulation:

**Set-of-Mark (SoM):**This is designed for grounding actionable tasks in a space, across all data modalities, by assigning numerical labels to any interactive elements in an environment, like buttons that can be clicked or objects that can be picked up. “By providing SoM, we give Magma a high-level hint of ‘what needs attention’ — the essential elements of the task — without yet specifying the order or method,” the team wrote.**Trace-of-Mark (ToM):**When applied specifically to video and robotics data, this allows the model to learn possible patterns of movements from video data, so that it can “capture how these elements change or move throughout an interaction,” according to the team, and thus anticipate future states while planning out potential actions.
![](https://cdn.thenewstack.io/media/2025/04/0439519f-microsoft_magma-2.jpeg)
Via Microsoft Research.

During testing, the team found that Magma-8B demonstrated strong performance in various benchmarks, particularly in UI navigation and tasks involving robotic manipulation. For the latter, Magma’s performance actually surpasses the open source [OpenVLA](https://openvla.github.io/) in a variety of tasks.

As the Microsoft team noted, Magma is but one component of what the company envisions as the future of agentic AI systems that are capable of executing tasks in both digital and physical worlds. The company has also recently pushed ahead with its latest release of [AutoGen](https://www.microsoft.com/en-us/research/project/autogen/), a popular open source programming framework for [developing multiagent AI systems](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/), and is now in the process of experimenting with new user experience systems powered by foundation agentic AI models.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)