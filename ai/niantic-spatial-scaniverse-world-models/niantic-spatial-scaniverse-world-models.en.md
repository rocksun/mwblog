By now, we’re all generally familiar with [large language models](https://thenewstack.io/introduction-to-llms/) (LLMs) and the core use of text in predictive, generative, and agentic AI services. As automated intelligence services now diversify, our attention turns to large image/vision models, large audio models, and the emerging field of video generation models.

The next frontier in this space may be what the industry is calling spatial intelligence — AI systems that understand and reason over physical environments rather than just text or images. One emerging approach is the ‘large geospatial model’ (LGM), a foundation model built on 3D scans, satellite imagery, LIDAR, and GPS data to create geometrically accurate, machine-readable representations of real-world spaces that developers can build layered services on top of.

## A front door to spatial intelligence

Physical world mapping specialist [Niantic Spatial](https://www.nianticspatial.com/) wants to be seen as a prime mover in the race to create a living model of the world and make it one that people and machines can talk to. On Tuesday this week, the company launched Scaniverse for businesses, a software service designed to act as a front door to spatial intelligence services.

If we accept that building all AI is hard, why is geospatial mapping and model development in this space so tough?

![](https://cdn.thenewstack.io/media/2026/04/e653506c-unnamed-1024x576.png)

*Credit: Niantic Spatial*

## Don’t map the world with text

Niantic Spatial explains that the problem stems from the way world models have been built thus far i.e. most are trained on text and images. The company works to elevate this practice by using technologies that generate models with precise coordinates and geometry to make environments navigable and machine-readable.

But why does any of this really matter, given the already rich set of world mapping and topography datasets that exist? In his role as executive chairman of Niantic Spatial, [John Hanke](https://www.linkedin.com/in/john-hanke-6a896/) has argued that the digital economy only accounts for a fraction of global economic activity and that AI built exclusively on text and images can’t reach the rest.

> Just 20% of the world economy is online but the 80% is not […] the acts of extracting, refining, growing, assembling, combining and shipping the atoms that warm us, shelter us, feed us, and generally make life possible for human beings – John Hanke, Niantic Spatial.

## Undigitized: 80% of the global economy

Writing on his company’s own [blog channel](https://www.nianticspatial.com/blog/ai-real-world), Hanke suggests that as much of 80% of the world economy happens outside of digital screens and is mostly bereft of digital encoding.

“Just 20% of the world economy is online, but the 80% is not,” writes Hanke. “Out in the real world, in industries like energy, agriculture, manufacturing, construction, transportation, and logistics – in other words, the acts of extracting, refining, growing, assembling, combining, and shipping the atoms that warm us, shelter us, feed us, and generally make life possible for human beings. These are our most essential human needs, not chatbots.”

Hanke and team assert that simply capturing a space to digitally encode it, versus and knowing exactly where you are within it, are two different problems; he says that most companies in this space only address one of those two vectors. Niantic Spatial aims to solve both by creating geometrically accurate and spatially grounded models that allow machines to understand and interact with the physical world.

## Photorealism in Gaussian splats

Scaniverse supports versatile capture of physical space, ranging from individual rooms to areas of thousands of square meters. The software works to drive an integrated web and mobile platform that captures 3D spaces (small and large), supporting multiple devices, to generate visual positioning maps and meshes. When needed, the technology also generates [Gaussian splats](https://rd.nytimes.com/projects/gaussian-splatting-guide/), point-based 3D rendering services that draw on overlapping techniques to create fully photorealistic digital scenes.

Scaniverse for businesses is a self-service platform that lets any team capture and reconstruct real-world environments (anything from construction sites to warehouses to industrial facilities and even underwater) using a smartphone or 360° camera. It then generates spatial maps that robots and AI agents need to navigate the physical world.

Niantic Spatial’s VPS 2.0 service is the company’s new visual positioning system, delivering near centimeter-level positioning in mapped environments and reliable positioning across a broad range of locations where GPS fails. It In places mapped with Scaniverse, VPS delivers near 6DoF localization. Everywhere else, it corrects GPS errors and dropouts to provide improved, reliable positioning and heading, especially in GPS-degraded environments.

## Earth Observation & GIS

Working in precisely this space is [Dean Summers](https://www.linkedin.com/in/sunnydean/), founder and director of engineering at Cambridge, UK-based specialized geospatial AI services organization [Lampata](https://lampata.co.uk/). Summers tells *The New Stack* that, to date, the AI industry has focused heavily on language, but the next real leap will come from systems that understand the world as it actually exists: spatially and dynamically.

“Foundational models built on [Earth Observation](https://www.euspa.europa.eu/eu-space-programme/copernicus/what-earth-observation) (EO), GIS and geospatial data are the logical next step, because they allow machines to reason over environments, assets and change over time rather than just words on a page,” Summers says. “This is where AI starts to move beyond conversation and into operational understanding of the physical world.”

He further explains that as we enter the next phase of data mapping for our planet, the real challenge now is integrating and training models across what he specifies as “fundamentally different geospatial data” i.e. from vectors and rasters to point clouds and sensor streams. It will be all about turning that complexity into meaningful, reliable results.

To map the current challenges and technology gaps, Summers and team are working with a larger group within OpenUK to create a tech radar that maps out the landscape for future innovation in the space of space.

## One SDK, every platform

Soon to follow from Niantic Spatial this April 2026 is the Niantic Spatial Development Kit (NSDK) 4.0, a unified SDK for Unity, Swift, Android, and ROS 2, connecting directly to Scaniverse and VPS 2.0. Scaniverse works with regular consumer phones – and now with data from 360o cameras, with no expensive proprietary equipment or training required. Support for new types of data capture and formats is also coming later this year.

On mobile, the newly updated Scaniverse app builds on a platform already used to scan millions of objects and places in the real world. Multiple users can contribute scans to a shared project at different times on different devices. Uploads are stored and managed in the cloud, fused into a single unified model that updates as new scans are added.

Scaniverse is also available on the web via the organization’s browser portal. Users can upload, manage and process data from the Scaniverse mobile app and 360o cameras and visualize outputs directly in the viewer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)