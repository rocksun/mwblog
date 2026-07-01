[Base44](https://base44.com/), an AI-powered app-building platform, has launched its first proprietary AI model, dubbed Base One. It is a fine-tuned open-source [LLM](https://thenewstack.io/llm/) trained specifically for [vibe coding](https://thenewstack.io/vibe-coding-ceos-executives-ai-agents/) web applications.

The company is claiming it as an industry first: the first app-creation platform to launch its own model. The claim carries an asterisk, though.

Base44 founder and CEO [Maor Shlomo](https://www.linkedin.com/in/maor-shlomo-1088b4144/) confirms in an interview with *The New Stack* that Base One is a fine-tune on an existing open-source base, not a model trained from scratch. (The term “proprietary model” gets used loosely across the industry.)

## Training approach

The training approach is [reinforcement learning](https://thenewstack.io/reinforcement-learning-pioneers-honored-with-acm-turing-prize/)-driven. Base44 runs the model repeatedly against real platform tasks, building and editing applications, scoring outputs as good or bad, and feeding that signal back to update the model’s weights, he says. Shlomo says the training data is a mix, with most of it generated from running the model on Base44’s platform and using reinforcement learning feedback to improve it, along with some synthetic data. The model is already in production and serving users, he adds.

Shlomo says general frontier models like Claude or GPT are trained to be good at everything, from web development to GPU kernel writing to C++ to Chinese poetry. Base44’s bet is that a model optimized exclusively for translating natural-language prompts into working web applications, with design and product decisions baked in, will outperform generalists in its specific use case.

“For many use cases, it might not be the best choice,” Shlomo says of frontier models, “especially if you can control and adapt and align a model to your needs.”

Owning the model stack also saves a buck. Base44 has direct control over compute and inference spend, which Shlomo says is one of the largest cost drivers in AI-native businesses. Thus, it reduces dependence on external vendors for a core part of its product.

## Accelerated development

Things happened faster than Shlomo says he expected. A year ago, he says, he wouldn’t have imagined Base44 would be training its own model this soon. Two factors moved it up: the rapid maturation of open-source model quality, which provided a strong foundation for fine-tuning, and Base44’s own growth trajectory, which generated the data volume and traffic needed for fine-tuning to work effectively.

Wix acquired Base44 for $80 million last year. Shlomo says the company grew revenue from $3 million to $150 million in under a year following the Wix acquisition, a figure Wix has made public.

The model development was a collaboration between Base44 and Wix’s existing machine learning and data science team, which previously built Wix Harmony. The model itself is tuned to Base44’s agentic harness, which includes its tooling, instructions, and the agent’s operation within the platform.

## Competition

Competitors in the vibe coding space include Lovable, Replit, Bold, and Figma, which has moved into the category. Shlomo says he doesn’t expect the new model’s launch to fundamentally shift the competitive landscape, but sees it as a quality and efficiency advantage as Base44 iterates on future versions.

Base One is the first in what Shlomo says will be a series of releases, with larger models and deeper product integration planned.

“We’re just getting started here in this lane of training a model,” he says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)