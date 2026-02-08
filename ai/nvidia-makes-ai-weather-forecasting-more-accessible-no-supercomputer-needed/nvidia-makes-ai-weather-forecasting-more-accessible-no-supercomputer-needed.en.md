With very few [exceptions](https://www.weathercompany.com/), large-scale weather forecasting has been the domain of government agencies with access to massive supercomputers. But that is changing.

Nvidia launched two open source weather forecasting models today: Earth-2 Medium Range and Earth-2 Nowcasting. In addition, it is launching a tool that will significantly speed up the generation of starting conditions for these models.

[Mike Pritchard](https://www.linkedin.com/in/mikepritchard/), Nvidia’s director of climate simulation, tells *The New Stack*, “The stakes can’t be higher in weather.”

“Worsening extreme weather, driven by climate change, is having impacts on all of us and nearly every aspect of modern life. Forecasting affects us all. It can drive improvements to agriculture, energy, aviation, and emergency response, but the science of forecasting is changing,” Pritchard says.

AI has sparked a “scientific revolution in weather forecasting,” Pritchard argues, but researchers have struggled to move this work out of the lab and into practical solutions. “We need to lower the barrier to entry so developers can build tools in the open.”

This isn’t Nvidia’s first foray into the weather forecasting business. As part of Earth-2, its effort to build a digital twin of Earth, it previously launched two other models. The first is [Earth-2 CoreDiff](https://build.nvidia.com/nvidia/corrdiff), a model that takes continental-scale predictions and downscales them to high-res local ones up to 500 times faster than traditional methods. The second is [Earth-2 FourCastNet3](https://developer.nvidia.com/blog/fourcastnet-3-enables-fast-and-accurate-large-ensemble-weather-forecasting-with-scalable-geometric-ml/), a highly efficient global forecasting model that can run on a single Nvidia H100 GPU.

Accurate forecasts aren’t just useful for deciding whether to take an umbrella or not. These models are critical infrastructure for airlines, insurers, energy providers, and agriculture.

## Nvidia’s new weather models

Both of the previous models — and most other existing AI-based forecasting models — use [specialized model architectures](https://arxiv.org/abs/2306.03838) and do not use the transform-based approach that is now the default for modern large language models (LLMs). For the new Medium Range and Nowcasting models, Nvidia adapted exactly this transformer architecture. Transformer-based architectures, after all, are backed by the performance and engineering tooling of virtually every other AI company.

“Philosophically, scientifically, it’s a return to simplicity,” Pritchard says. “We’re moving away from hand-tailored niche AI architectures and leaning into the future of simple, scalable transformer architectures.”

The Medium Range model, as its name implies, is meant to provide high-accuracy forecasts for up to 15 days in the future.

![](https://cdn.thenewstack.io/media/2026/01/1be9e02a-nvidia-weather-model.gif)

The Nvidia Earth-2 Medium Range model in action. (Credit: Nvidia)

Nvidia hasn’t provided *The New Stack* with detailed benchmarks yet, but Pritchard argues that the Medium Range model outperforms DeepMind’s GenCast, the current leader in this space, “across more than 70 weather variables,” including temperature, pressure, and humidity.

The Nowcasting model is maybe even more interesting, though: It generates country-scale forecasts at kilometer resolution — a very high resolution for any modern model. Most of the models that inform weather forecasts in Europe or North America have a resolution of two kilometers or more, while the U.S. National Oceanic and Atmospheric Administration’s (NOAA) [GFS model](https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast), which is available for free and is often the default in free weather apps, has a resolution of 13 kilometers (though NOAA has also started [implementing AI forecasts](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models) recently).

The Israeli Meteorological Service plans to use the Nowcasting model to generate high-resolution forecasts up to eight times daily going forward. The organization already uses Nvidia’s older CoreDiff model. Similarly, The Weather Company (the company behind weather.com) plans to use Nowcasting for localized severe-weather applications.

## No supercomputer needed

For the Medium Range model, which comes in a few variants ranging from 2.4 billion parameters to 3.3 billion, the training was done on 32 80GB A100/H100 GPUs. But to run the model, you would only need 26GB of GPU memory and an A100 GPU can run a single time-step prediction that covers 6 or 12 hours. Depending on the model, it only takes 140 seconds for the GenCast Model, 94 and 88 seconds for the two other Medium Range variants (dubbed Atlas-SI and Atlas EDM) and under four seconds for the Atlas-CRPS model (which has additional noise conditioning and is a bit larger at 3.3 billion parameters.

For the Nowcasting model, each 6km-resolution model requires only 5GB of GPU memory and can run in 33 seconds on a single H100 GPU at maximum precision. “We expect the inference speed to be greatly accelerated by techniques such as distillation and/or reduced precision,” an Nvidia spokesperson tells us.

## Data assimilation: The other 50% of the problem

For weather forecasts, the starting data from which the model begins generating its forecast is crucial. That can be satellite imagery, radar data, sensor data from weather balloons, airplanes, and buoys. All of this data needs to be normalized and transformed so the models can work with it.

Climate scientists call this process “assimilation.” To accelerate this hours-long process, Nvidia also launched the Global Data Assimilation model, which produces these initial snapshots of the global weather within seconds.

“While the AI community and the research community have focused a lot on the prediction models over the past five years, this data assimilation task, this state estimation task, has remained largely unsolved by AI, yet it consumes roughly 50% of the total supercomputing loads of traditional weather [forecasting],” says Pritchard.

The assimilation model is actually quite small, at 330M parameters. Using one H100 GPU, it can run the full inference pipeline in under a second, all while using less than 20GB of GPU memory.

It still seems unlikely — but possible — that even these efficient models will allow hobbyists to start creating their own forecasts anytime soon. Simply acquiring and managing the starting data, after all, is a major data problem. But for an enterprise with the right use case and resources, this may just open the door to creating local forecasts without the need to access a supercomputing cluster.

**Update**: *we updated this post after publication to include the compute requirements for these models.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)