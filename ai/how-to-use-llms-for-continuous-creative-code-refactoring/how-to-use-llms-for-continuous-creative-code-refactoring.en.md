Refactoring used to be limited to a fixed set of transforms hardwired into IDEs. If the one you needed wasn’t included, you were out of luck and had to do it the hard way. AI-assisted IDEs with Model Context Protocol (MCP) tool support have changed that game. Show them before and after examples of a wide variety of patterns, and they can figure out all kinds of transforms without explicit support for them.

For example, here is a prompt I’m using to clean up [XMLUI](https://thenewstack.io/make-react-components-with-xmlui-a-visual-basic-for-the-ai-era/) apps that make unnecessary use of the [Fragment](https://docs.xmlui.org/components/Fragment) component:

[![](https://jonudell.info/newstack/refactor-01.png)](https://jonudell.info/newstack/refactor-01.png)

I pointed Claude, Cursor and Codex at a directory with an XMLUI app that included uses of `Fragment` that should and should not be refactored according to these rules. All produced the same correct diff. A conventional approach would entail the use of an XMLUI parser that could distinguish `when` attributes from others (like `gap`) and act accordingly. Large language models (LLMs) don’t work that way; they are general-purpose pattern recognizers, and one of my [seven rules](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) for working with them is: *Exploit pattern recognition*.

## Extracting Components To Reduce Repetition

It’s easy to create a [user-defined component](https://docs.xmlui.org/components-intro) in XMLUI to encapsulate repetition. When you do something once, there’s no need. When you do it again, with variation, you may start to think about extracting what’s common into a component. But it often takes more repetition, with more variation, to clarify what the common core is that a component should embody. There’s always been tension between letting variation happen to discover what’s truly common and consolidating into more readable and maintainable code. LLMs can ease that tension.

Suppose you find yourself doing something like this:

```
<!-- before -->
<HStack>
  <VStack>
    <Text variant="secondary" fontSize="$fontSize-sm">Cloud Cover</Text>
    <Text fontWeight="semibold" fontSize="$fontSize-lg">
      {condition.cloudcover}%
    </Text>
  </VStack>


  <VStack>
    <Text variant="secondary" fontSize="$fontSize-sm">Humidity</Text>
    <Text fontWeight="semibold" fontSize="$fontSize-lg">
      {condition.humidity}%
    </Text>
  </VStack>


  <VStack>
    <Text variant="secondary" fontSize="$fontSize-sm">Wind Speed</Text>
    <Text fontWeight="semibold" fontSize="$fontSize-lg">
      {condition.windspeedMiles} mph
    </Text>
  </VStack>
</HStack>
```

You may realize this would be better:

```
<!-- after -->
<HStack>
  <WeatherStat
 label="Cloud Cover"
 value="{condition.cloudcover}%"
  />
  <WeatherStat
 label="Humidity"
 value="{condition.humidity}%"
  />
  <WeatherStat
 label="Wind Speed"
 value="{condition.windspeedMiles} mph"
  />
</HStack>


<!-- a new component -->
<Component name="WeatherStat">
  <VStack
 gap="$space-1"
 minWidth="8rem"
  >
    <Text
 variant="secondary"
 fontSize="$fontSize-sm"
    >
      {$props.label}
    </Text>
    <Text fontWeight="semibold">
      {$props.value}
    </Text>
  </VStack>
</Component>
```

We’re often lazy about applying that kind of transform, but laziness can be a virtue. If you haven’t seen a sufficient number and variety of *before* cases, you may not yet know what *after* should be. AI assistants can make experimentation cheap and fluid.

## Planning Code Changes With AI Collaboration

[AWS Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/) invites you to operate in Spec mode, where you collaborate on writing requirements, design documents and task checklists. In my experience, its reach often exceeds its grasp, and I’ve abandoned several checklists. But the idea took hold in a less formal way and is now woven into conversational use of Claude Code and Codex.

When I asked Claude to [implement an authentication gate](https://docs.xmlui.org/howto/implement-an-authentication-gate) for an app built by a novice XMLUI developer, it identified all the user-defined components that needed to change, enumerated the changes it proposed to make and noted one component requiring special treatment.

*Customers.xmlui has a pattern close to the standard but with some differences:*  
*– Uses contact\_id for routes, but id for API URLs*  
*– Only has “Mark as inactive” (no status toggle)*  
*– Delete APICall is outside the DropdownMenuI need to update the component to support different ID fields for routes vs API calls.*  
*Let me do that first.*

The app also made unnecessary use of the [Queue](https://docs.xmlui.org/components/Queue) component, which handles batches of API calls. In this case, there was no need for `Queue` because the backend provides a batch API. The change entailed the removal of extraneous stuff and the addition of calls to the batch API. Here was the plan:

*1. Remove the Queue (lines 106-143)*  
*2. Remove unnecessary variables (lines 4-7): var.action, var.processedCount, var.errorCount, var.completed*  
*3. Replace the bulk action buttons (lines 84-104) to call APICall components instead of Queue*  
*4. Add APICall components following the pattern you described:*  
*– POST /contacts/active with body: {contact\_ids: […], organization\_id: 906441453}*  
*– POST /contacts/inactive with body: {contact\_ids: […], organization\_id: 906441453}*  
*– DELETE /contacts/{ids} for bulk delete*

In this case, things went exactly as planned. Often they don’t, but the [conversational style](https://thenewstack.io/lets-talk-conversational-software-development/) of AI-assisted coding helps me adjust the plan as work proceeds.

## Limiting Software Liability With Cleaner Code

As [Cory Doctorow](https://doctorow.medium.com/) recently observed, [code is a liability (not an asset)](https://doctorow.medium.com/https-pluralistic-net-2026-01-06-1000x-liability-graceful-failure-modes-d69f384af9e4). Tech bosses, he says, don’t know this.

“They think they’ve found a machine that produces assets at 10,000 times the rate of a human programmer. They haven’t. They’ve found a machine that produces liability at 10,000 times the rate of any human programmer.”

For Bruce Schneier, such liability entails [legal and financial](https://www.schneier.com/essays/archives/2003/11/liability_changes_ev.html) risks that software makers will need to mitigate with insurance policies that make it costly to ship insecure or otherwise flawed products. Will AI-assisted coding increase software liability? Of course, when used improperly. But two things can be true at the same time. Thoughtful use of AI can also help us reduce liability by making it easier and safer to do the continuous refactoring that keeps codebases lean and clean.

## Applying Creative Insight With AI Assistance

With the extraneous uses of `Queue` removed, there was still repetitive use of [APICall](https://docs.xmlui.org/components/APICall) to implement a similar pattern across a suite of user-defined components. How to consolidate, given that `APICall` can’t be packaged in a declarative user-defined component? I realized that `APICall`‘s imperative, cousin [Actions.callAPI](https://docs.xmlui.org/globals#actionscallapi), can be used in `onClick` handlers, obviating the need to declare separate `APICall` components. That wasn’t an immediate win; it just shifted declarative properties to imperative arguments. But in the imperative domain, it became easier to define families of arguments for different cases. When handling a batch of items, for example, an action’s name might be *Mark as active* or *Delete*, its in-progress message might be *Marking as active* or *Deleting*, and its completion message might be *Marked as inactive* or *Deleted*.

Encapsulating that variation in a function made the code cleaner, but led to a new refactoring challenge. Each component needed a variant of the function. How could they share a common one? [AppState](https://docs.xmlui.org/components/AppState) provides a global key/value store that’s visible to all user-defined components in an app. It’s typically used to store simple values, but I realized it might be possible to store arrow functions there, too. LLMs won’t discover that kind of [creative insight](https://thenewstack.io/human-insight-llm-grunt-work-creative-publishing-solution/), but when you do, they can help you validate and apply it. In this case, Claude wrote a quick test to prove it would work, then merged a family of similar functions into a common global function.

## The ‘Less Is More’ Approach To Coding

The most memorable thing [Bill Gates](https://en.wikipedia.org/wiki/Bill_Gates) said to me, in a long-ago interview, was: “It’s all about writing less code.” LLMs love to write code, and when used indiscriminately, will create more than we want or need. Code *is* a liability. It’s on us to rein in the generative instinct of LLMs and focus them on the refactoring needed to limit that liability. We decide when and how to refactor, they do the mechanical transformations — it’s a continuous conversation. Tools built to generate vast amounts of code can, paradoxically, help us write less of it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/02/9d121cd7-cropped-f95c0bac-jonudell-2025.png)

Jon Udell is an author and software developer who explores software tools and technologies and explains them in writing, audio, and video. He is the author of the cult classic Practical Internet Groupware. Past gigs include Lotus, BYTE magazine, Safari...](https://thenewstack.io/author/jon-udell/)