PhiloLabs wanted to see how far a group of AI coding agents could get building something where working code wasn’t enough. In a recently published experiment, the company set [Claude Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/) agents loose on a 3D reconstruction of San Francisco’s Union Square, built from real-world geographic data and reference images.

Two hours later, the agents had built a working [Three.js](https://threejs.org/) version of Union Square in the browser. The [experiment](https://github.com/PhiloLabs/fable-5-1-worlds) included 453 building footprints, 75 custom façades and 129 named storefronts, along with 220 pedestrians and 109 vehicles moving through the scene, including Powell Street’s cable cars.

But getting the application to run was only one part of the experiment. PhiloLabs also wanted the agents to catch visual problems that [conventional tests would miss](https://thenewstack.io/go-language-ai-agents/), so it put Playwright into the development loop.

The entire run used roughly 8 million tokens and cost about $33 in API calls.

> The entire run used roughly 8 million tokens and cost about $33 in API calls.

## Playwright as agent vision

PhiloLabs divided the reconstruction among subagents that handled geographic research, building geometry, textures, storefronts, and other parts of the scene. Once their work was running in the browser, Playwright moved through 34 predetermined camera positions and captured screenshots that could be checked against photographs of the real Union Square.

In all, the agents produced 147 comparison sheets, making it easier to spot things that were technically correct but still looked wrong. For instance, a building might be in the right place but have the wrong proportions, or a storefront might end up on the wrong side of the street. Using the same camera positions each time also made it easier to see what changed from one pass to the next.

> In all, the agents produced 147 comparison sheets, making it easier to spot things that were technically correct but still looked wrong.

## Agents reviewing agents

PhiloLabs then had specialist agents examine the material, with some focused on architecture and geography and others on technical art and interactions. Together, they produced nine reports on the Union Square build.

Those reports became a punch list for the next pass. The development agents could address the reviewers’ findings and rerun the scene.

That division is useful because not every mistake translates neatly into a test. You can check whether a building was placed at the right coordinates. It’s much harder to write a test that tells you whether the street actually looks like Union Square.

## Filling gaps in source data

The agents weren’t starting with a finished 3D model they could simply recreate. They had to pull together open geographic data (primarily [OpenStreetMap](https://www.openstreetmap.org/copyright) and USGS elevation data) along with information about the real location, then turn all of it into geometry, façades, and objects that would run in a browser.

There were still plenty of gaps to fill because geographic data could tell the agents where a building belonged without showing what its façade looked like, while photographs only captured the parts of the building visible from a particular angle, leaving the agents to make their own calls when neither source provided an answer.

Another agent checking the work doesn’t guarantee that those decisions are right, especially when the source material is incomplete to begin with, because the reviewer can miss the same thing the first agent did.

## What $33 buys

Eight million tokens is a lot of model activity for a single application. Yet the reported API cost for the Union Square run was about $33.

PhiloLabs split the job among subagents, ran tasks in parallel, and reused cached context rather than having a single agent repeatedly work through the entire project from scratch.

Still, Union Square was a fairly contained experiment. Screenshots are not as useful once agents move into complicated applications. [Spline recently rebuilt its 3D editor using Claude Code agents](https://thenewstack.io/spline-v2-mcp-agents/), but the finished interface only shows part of what those agents built. Problems buried in the code or triggered by the way people actually use the editor may never show up in a screenshot.

> Eight million tokens is a lot of model activity for a single application. Yet the reported API cost for the Union Square run was about $33.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)