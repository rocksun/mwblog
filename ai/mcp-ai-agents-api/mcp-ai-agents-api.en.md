**Suppose someone on your operations team wants to ask their AI assistant**: “Which orders are going to miss today’s shipping cutoff? Check inventory at the other warehouses and create transfer requests where we can cover the shortages.”

That sort of agentic workflow requires calling APIs. The agent needs current orders and available inventory; yesterday’s report won’t tell it what stock is still available this afternoon. And it needs to write transfer requests back into the fulfillment system.

To make the company’s internal order management API available to an agent, an engineer might build an MCP server. It’s the fastest way to make a system like this reachable, but reach is the easy part now. The harder question, which existed long before MCP, is what the agent should see once it gets there. MCP just makes that question urgent.

An API for a service like order management might return a wide array of information, including personally identifiable information, sensitive financial and fraud details, and operational information never meant to leave the confines of the trusted network. We already know how to handle access control for a traditional application: the backend checks the user’s permissions, processes the upstream API call, and returns only the appropriate view.

So engineers enabling flexible agents like these are caught between a rock and a hard place. An MCP tool that passes along everything from its upstream is a security risk. That’s the rock. The obvious fix is to filter the tool’s response. But then finance needs a different view of orders, support needs some of the internal notes, another team connects the inventory system, and now you have to maintain dozens of similar, overlapping tools. That’s the hard place.

The way out is a deterministic, field-level contract that specifies exactly what each agent can see and do, independent of both the upstream APIs and downstream agents. MCP defines how agents discover and call tools. A field-level contract defines what those tools are allowed to access. They’re different layers, and you need both.

GraphQL, a popular, widely deployed technology, gives us a practical way to do that.

GraphQL was designed around the idea that API calls should specify the exact fields they need. An order-status lookup can be as small as this:

```
query {
  order(id: "order-1842") {
    status
    shipBy
  }
}
```

The response contains only those fields, no matter what else the upstream systems provide. Originally designed to narrow large API payloads on mobile networks and avoid writing BFFs, that idea now gives engineers a place to enforce agentic permissions.

So, for example, if an agent asks for a field like `internalFraudScore` or `customerSSN`a GraphQL server can block the request or even make those fields unreachable. The rule belongs to the field and applies across the operations that request it. Each tool author doesn’t have to remember to remove the same property from another response.

Writes work the same way. Our operations employee needs permission to request inventory transfers. A read-only connection would prevent the work; unrestricted access could also let the agent change stock counts, cancel orders, or issue refunds. A mutation (what we call writes in GraphQL) such as `requestInventoryTransfer` exposes the particular business action. The runtime authorizes it, and the underlying service checks current availability and any required approvals before accepting the request.

None of this requires replacing the APIs that run the business. A GraphQL layer can sit over existing services that expose REST, gRPC, SOAP, and any other protocol. The order API can continue returning a broad record to the integration layer while the agent receives only the fields it is permitted to see.

The precision that helped developers build efficient applications quickly is even more useful when the caller is an agent composing operations at runtime. GraphQL has supplied this field-level contract to applications for more than a decade, powering billions of daily transactions at Shopify, Netflix, Airbnb, Expedia Group, and Walmart. These companies and countless others have built up a decade of experience and production infrastructure running exactly this model.

MCP makes business systems reachable by agents. A field-level contract makes that access something the organization can control. GraphQL is a perfect answer sitting right in front of us.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/53e94460-1761254142216-600x600.jpeg)

Matt DeBergalis is CEO and co-founder of Apollo GraphQL.

Read more from Matt DeBergalis](https://thenewstack.io/author/matt-debergalis1/)