# OpenMDW Is a New Permissive License for AI Models
![Featued image for: OpenMDW Is a New Permissive License for AI Models](https://cdn.thenewstack.io/media/2025/05/47368cdf-virginia-johnson-qmnnzj_ok-m-unsplash-1024x768.jpg)
The Linux Foundation quietly [released](https://openmdw.ai/) a new license for AI models and their artifacts earlier this month. The new [OpenMDW license](https://openmdw.ai/license/) is a highly permissive license, that combines some aspects of the Apache 2.0 and [MIT licenses](https://opensource.org/license/mit) that are currently a popular choice for licensing AI models. It’s also very short and easily fits on a single page.

OpenMDW was born out of another Linux Foundation effort, the [Model Openness Framework](https://isitopen.ai/) (MOF), which tries to help users evaluate how open a given model actually is. That framework classifies model into three categories, ranging from ‘Open Models’ that include only the model and its parameters, with unrestricted usage rights, up to ‘Open Science Models’ that include research papers, datasets, intermediate model parameters, and more to allow for the full reproduction of a similar model.

That’s a lot of complexity and it doesn’t look like the overall idea caught on. Matt White, who helped chair the efforts to launch the OpenMDW license and who is also the executive director of the PyTorch Foundation, admits as much. “The Model Openness Framework, in its initial version, was not that easy to deploy. It requires multiple licenses for data sets, and a different set of licenses for source code. And so we always thought there’s going to be a need to actually have a license that can cover all of this. And that’s where the OpenMDW was born out of,” he explained.

Initially, White told me, the idea was to create a form of meta-license based on the Creative Commons BY 4.0 license and Apache 2.0 licenses, but that felt unwieldy. The team behind OpenMDW, which includes representatives from the Linux Foundation, as well as Amazon, IBM, Meta and Microsoft, really wanted a short, permissive license in the style of the MIT license.

He noted that part of the motivation also was to ensure that if a developers goes to Hugging Face, for example, and downloads a model covered by the OpenMDW license, it’s clear what the acceptable uses are. Today, he noted, models are often covered by community licenses that have restrictions or are linked to acceptable use policies, among other things.

“Nobody reads MIT and Apache, 2.0, right? We want to build that trust mechanism with this license, so that people recognize the model. It’s openMDW. Okay. I know what I can do with this. It’s safe for commercial usage. I can use it for research. I can use it in production. I can do whatever I want with it,” White said.

At the core of the OpenMDW license is its definition of ‘model materials,’ which includes the models themselves and “all related artifacts (including associated data, documentation, and software).” This would cover the model architecture, which could be in code or configuration, any training and pre-processing code, and everything else. The license does not, however, require that any of the actual training materials themselves have to be made available.

“We want it to be fairly encompassing,” White explained. “Also, we don’t presume that we know what models will look like in the future. The idea is here was to make it broad enough that it could cover not just deep learning models today — and not just machine learning models of yesterday — but what’s next.“

The license also allows developers to make any of these additional materials available under another open-source license. They would simply have to put the appropriate license file into the directory that includes the relevant code.

“One of the other things that was a goal for us, too, was to make this a global license so that it’s compatible with other licenses,” White explained. “So if you have another license, you want to license some of the software code under Apache 2.0 that’s fine. That’s underneath a different directory structure. […] But if you include it, and it’s not explicitly addressed by another license, OpenMDW will cover those components.”

Like the Apache 2.0 license, it includes a patent litigation clause, which essentially means that if if anyone files a patent lawsuit that argues that any of the materials covered under the license infringe on a patent, they themselves will lose all the rights granted by the license.

“If somebody does sue you, they shouldn’t still be able to use the model, right? That’s a no-brainer,” White said.

Since the license does not put any restrictions on model output, it also ensures that models with this license can be used for distillation, for eample.

For the most part, the license has flown under the radar, even though it did have a six-month comment period before the team published the 1.0 draft. Maybe that is because, as of now, it hasn’t been included in the SPDX license list yet, and the team hasn’t submitted it to the OSI yet, either. White noted that the license isn’t a traditional open-source license, even though it embodies open-source principles. But since it doesn’t require any components, while the OSI’s definition of open-source AI models does, it remains to be seen if it will pass muster.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)