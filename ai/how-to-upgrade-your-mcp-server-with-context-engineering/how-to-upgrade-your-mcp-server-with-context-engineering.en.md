I never liked the phrase *prompt engineering*, which always sounded to me like a fancy way to talk about casting magic spells. Now, that phrase is tired and *context engineering* is wired. We’re all realizing it’s critical to manage what AI agents hold in their context windows.

Engineering that context can mean different things. I’ll focus here on how an upgrade to the [MCP server](https://github.com/xmlui-org/xmlui-mcp) for [XMLUI](https://docs.xmlui.org) improved its ability to manage context for agents (disclosure: I am a consultant on the XMLUI project; see also [The New Stack’s writeup](https://thenewstack.io/make-react-components-with-xmlui-a-visual-basic-for-the-ai-era/)).

## Using xmlui-mcp

*xmlui-mcp* works with documentation, source code, and examples. Here is a typical configuration for agents like Claude or Cursor.

```
"xmlui": {
    "command": "/Users/jonudell/xmlui-mcp/xmlui-mcp",
    "args": [
    "/Users/jonudell/xmlui",
    "/Users/jonudell",
    "xmlui-invoice,xmlui-mastodon"
    ]
},
```

This code means:

* Launch the xmlui-mcp binary
* Use /Users/jonudell/xmlui as the location of a clone of the XMLUI repo
* Use /Users/jonudell as the root for examples
* Look for examples in the xmlui-invoice and xmlui-mastodon subfolders

This had worked pretty well. I’ve heard from XMLUI devs about successful one-shot results and was delighted by this feedback:

“I left the MCP server running, refreshed the page, and suddenly had working UI for what I asked. I am living in the future.”

Nice!

## Raising Expectations

Despite the encouragement, I wasn’t satisfied. When you are working with the combination of agents and *xmlui-mcp,* you should always be led to a correct solution that’s supported with citations to source code, docs, how-to articles, or working examples. If no solution emerges? That’s a bug in the documentation (that we can fix) or a missing feature (that we can add). You should *never* be led to an incorrect solution that isn’t anchored to ground truth. And that was happening a lot.

I added a prompt called `xmlui_rules` with guidance like “do not invent any xmlui syntax, only use constructs for which you can find examples in the docs and sample apps, and always cite your sources.” Now, instead of pasting the rules into a chat I could just say “remember the rules,” but I kept having to repeat that. How could *xmlui-mcp* play a more active role in managing context and reiterating the rules?

For starters, the xmlui-mcp search tools needed to get smarter about fuzzy search. Working with my [team of assistants](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) (in this case ChatGPT, Claude and Cursor) we came up with a phased approach: first look for the exact search string, then take a relaxed approach that omits common stopwords, then take a partial-matching approach that only requires a subset of query words to match (for example, finding documents with only two of four query terms, instead of requiring all four). The first version used an algorithm that favored precision over recall. That seemed too strict, but when I boosted recall the results were swamped with irrelevant hits. A conservative approach to precision in this layer wasn’t a dealbreaker, it turned out, if the system could help agents orchestrate a mix of tools and search strategies.

To make this concrete, consider this test query: “How do I create a row of equal width components?”

This is the URL I want the agent to find and report: [Make a set of equal-width cards](https://docs.xmlui.org/howto/make-a-set-of-equal-width-cards). The query was imperfect for that outcome, but Cursor got where I wanted it to go.

[![](https://jonudell.info/newstack/equal-width-components.png)](https://jonudell.info/newstack/equal-width-components.png)

How did it get there? I asked it to explain.

1. Initial Search Strategy  
I started by searching for “row equal width components layout” but got no matches. Then I tried more specific terms:  
mcp\_xmlui\_xmlui\_search with “HStack row layout components” – found general HStack info  
2. The Key Discovery  
In the “width 100% equal” search results, I found this specific match:  
mcp\_xmlui\_xmlui\_search with “width 100% equal” – this was the key search that found the how-to  
The filename itself contained “equal-width-cards” which was exactly what I needed!  
3. How I Connected Equal Width Components to Equal Width Cards  
The connection wasn’t a leap – it was a direct match in the search results. When I searched for “width 100% equal”, the search engine found:  
– The filename: make-a-set-of-equal-width-cards.md  
– The title: “Make a set of equal-width cards”  
– The howto listing: Make a set of equal-width cards, in the howto index  
– The Search Process  
4. Here’s the exact sequence:  
– First search: “row equal width components layout” → No results  
– Second search: “HStack row layout components” → Found general HStack info  
– Third search: “width 100% equal” → Found the how-to guide!  
The third search was the breakthrough because it found the specific how-to guide that addresses exactly what you asked for.5. Why This Worked  
The search was successful because:  
– The how-to guide filename contains “equal-width-cards”  
– The search term “equal” matched “equal-width” in the filename  
– The search term “width” matched the content about width sizing  
– The how-to guide specifically addresses creating equal-width components in a row

To see how this works, look at one of the responses Cursor received from *xmlui-mcp*:

```
Query: "width 100% equal"  (stages=3, hits=50, confidence=high)
Facets: components=12 files (36 matches)  examples=0 files (0 matches)
  howtos=2  source=6 files (12 matches)

docs/public/pages/layout.md:395: When you use a `HStack` child with percentage width, the effective width is calculated from the stack's viewport width.
docs/content/components/IFrame.md:45:       width="100%"
...
xmlui/src/components/AppHeader/AppHeader.module.scss:127:       width: 100%;
xmlui/src/components/AutoComplete/AutoComplete.module.scss:42:     width: 100%;

---
JSON:
{
  "query_plan": [
    {
      "stage": "exact",
      "query": "width 100% equal",
      "hits": 1
    },
    {
      "stage": "relaxed",
      "query": "width 100% equal",
      "hits": 1
    },
    {
      "stage": "partial",
      "query": "width 100% equal",
      "hits": 109
    }
  ],
  "sections": {
    "components": [
      {
        "type": "components",
        "path": "docs/content/components/IFrame.md",
        "line": 45,
        "snippet": "      width=\"100%\" "
      },
      ...
      {
        "type": "components",
        "path": "docs/public/pages/tutorial-09.md",
        "line": 146,
        "snippet": "    \u003cTable width=\"100%\" data=\"{[$props.details]}\"\u003e"
      }
    ],
    "examples": [],
    "howtos": [
      {
        "type": "howtos",
        "path": "docs/public/pages/howto/make-a-set-of-equal-width-cards.md",
        "line": 0,
        "snippet": "[filename match]"
      },
      {
        "type": "howtos",
        "path": "docs/public/pages/howto/make-a-set-of-equal-width-cards.md",
        "line": 1,
        "snippet": "# Make a set of equal-width cards"
      }
    ],
    "source": [
      {
        "type": "source",
        "path": "xmlui/src/components/Accordion/Accordion.module.scss",
        "line": 19,
        "snippet": "    width: 100%;"
      },
      ...
      {
        "type": "source",
        "path": "xmlui/src/components/App/App.module.scss",
        "line": 165,
        "snippet": "          width: calc(100% + (2 * var(--scrollbar-width)));"
      },
  },
  "facets": {
    "components": {
      "files": 12,
      "matches": 36
    },
    "examples": {
      "files": 0,
      "matches": 0
    },
    "howtos": {
      "files": 1,
      "matches": 2
    },
    "source": {
      "files": 6,
      "matches": 12
    }
  },
  "confidence": "high",
  "agent_guidance": {
    "rule_reminders": [
      "🚨 BEFORE RESPONDING: Ask yourself 'Am I about to provide code without a documented working example?' If yes, STOP and acknowledge the limitation instead",
      "🚨 PRIORITY ORDER: 1) Check for documented working examples 2) IF NONE FOUND: Explicitly state this and provide no code 3) ONLY THEN: Provide general documentation URLs (if any exist)",
      "🚨 MANDATORY ACKNOWLEDGMENT: When no documented examples are found, you MUST start your response with: 'I am following the guidance by not providing code examples because no documented working examples were found.'",
      "🔍 SEARCH STRATEGY: Use xmlui_examples and xmlui_search_howto first, then fall back to xmlui_search",
      "📚 PREFER: Examples and howtos over general component documentation",
      "🔄 FALLBACK: If no examples/howtos found, then search general documentation",
      "🔗 MANDATORY: Always include documentation or example URLs in your response",
      "🔗 MANDATORY: Always include documentation URLs in your response - see documentation_urls",
      "📍 REQUIRED: Cite specific sources with clickable links from the search results",
      "✅ VERIFY: You must include at least one URL from documentation_urls in your response",
      "❌ Do not invent syntax - only use documented constructs",
      "📝 Always cite your sources when providing code examples",
      "🔗 Provide specific URLs to documentation sources (see documentation_urls)",
      "📍 Reference file paths and line numbers when available",
      "⚠️ Preview and discuss limitations before providing code"
    ],
    "suggested_approach": "Limited examples found. Cross-reference component documentation with any available examples. Always provide URLs to documentation sources.",
    "url_base": "https://docs.xmlui.org",
    "documentation_urls": [
      {
        "title": "Layout",
        "url": "https://docs.xmlui.org/layout",
        "type": "components"
      },
      ...
      {
        "title": "Make A Set Of Equal Width Cards",
        "url": "https://docs.xmlui.org/howto/make-a-set-of-equal-width-cards",
        "type": "howtos"
      },
      ...
      {
        "title": "Accordion.module",
        "url": "https://docs.xmlui.org#xmlui/src/components/Accordion/Accordion.module.scss:19",
        "type": "source"
      },
    ]
  }
}
```

The responses had formerly been undifferentiated lists of filenames and snippets. Now they describe how the results land in buckets that suggest which tool to choose for followup searches. Also, they pound the agent with guidance about anchoring answers to documentation they can cite.

For belt-and-suspenders coverage, I also added this to the base user prompts for Claude and Cursor:

Obey the guidance you receive from the xmlui-mcp server.

I will disbelieve any answer for which you cannot cite an URL to documentation or a working example.

If you don’t find an URL, say so.

If you do find one, cite it.

## Acknowledging Failure Honestly

We shouldn’t only test the happy path. Here is a query that should fail: “How do I right-align a cell in a table?” There isn’t yet a way to do that! Agents working with the original *xmlui-mcp* gave all kinds of nonsense answers. Here’s how Cursor responded using the new version.

[![](https://jonudell.info/newstack/right-align-cell-in-table.png)](https://jonudell.info/newstack/right-align-cell-in-table.png)

That’s more like it. Show me what your research found, but don’t pretend there’s a definitive answer if there isn’t. When you can’t cite evidence, say so.

## Context Engineering With Testable Documentation

In the [last installment](https://thenewstack.io/mcp-is-rss-for-ai-more-use-cases-for-model-context-protocol/) (and also in [an earlier post](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)), I suggested that documentation is now amenable to testing. If there’s a right way to do something, an XMLUI developer working with an AI agent should find it. Failure to find a correct solution should point to a hole in the documentation that we can plug by adding a working example that illustrates the recommended pattern. We can then test to verify that a formerly failing search now succeeds in the way we expect.

> Nothing about how we write our docs privileges the LLM. The accessibility mantra “curb cuts benefit everyone” applies here too.

Something you hear nowadays is: “We are no longer writing for people, we are writing for machines so they can help people.” I don’t see it that way. Nothing about how we write our docs privileges the LLM. The accessibility mantra “curb cuts benefit everyone” applies here too. Thoughtful naming and careful selection layering — these are editorial best practices that benefit all readers. What does privilege the LLM, though, is an MCP server that makes documentation available to agents in ways they are best equipped to process.

It’s becoming a partnership in which agent-friendly docs helps us work with agents to create more and better agent-friendly docs, while a docs-aware MCP server helps us work with agents to produce software in a docs-informed way. Agents can even help us tune the MCP server’s usefulness to agents. That was the most delightful part of this exercise: working with agents to iterate on the MCP server, use it, introspect on their tool selection and search strategy, and feed learnings back in to a next iteration of the MCP server.

Although autonomous LLMs are inherently unreliable, there’s a long software tradition of building reliable layers on top of unreliable layers. That applies here too. We can’t guarantee that you’ll never be led astray when building an XMLUI app with the help of agents that use the XMLUI MCP server to extract patterns from docs, sources, how-tos, and samples. But it’s a lot more likely now that you and your AI team will stay anchored to ground truth. At this point, I would define context engineering as whatever it takes to make that happen.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/02/9d121cd7-cropped-f95c0bac-jonudell-2025.png)

Jon Udell is an author and software developer who explores software tools and technologies and explains them in writing, audio, and video. He is the author of the cult classic Practical Internet Groupware. Past gigs include Lotus, BYTE magazine, Safari...](https://thenewstack.io/author/jon-udell/)