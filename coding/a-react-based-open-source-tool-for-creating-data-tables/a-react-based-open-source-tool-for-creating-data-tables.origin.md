# A React-Based Open Source Tool for Creating Data Tables
![Featued image for: A React-Based Open Source Tool for Creating Data Tables](https://cdn.thenewstack.io/media/2024/11/d98417a9-aggridusethis2-1024x576.jpg)
[AG Grid](https://github.com/ag-grid/ag-grid)‘s developer relations lead, [James Swinton-Bland](https://www.linkedin.com/in/james-swinton-bland?originalSubdomain=uk), doesn’t see TanStack Table as a competitor. TanStack Table is an open source library for creating tables in the React framework, formerly known as React Table. On the contrary, the data grid [company sponsors TanStack Table](https://www.ag-grid.com/react-table/) and considers TanStack a partner.
“Our founder, [Niall [Crosby](https://blog.ag-grid.com/in-memory-of-niall-crosby/)], who sadly passed away recently, was a big fan of supporting open source communities and open source projects, and a big fan of supporting [Tanner [Linsley](https://github.com/tannerlinsley)] specifically,” Stinton-Bland said. “Tanner’s React Table solution is headless. Essentially that means that you have to build out the UI yourself, and you have to style everything, and you have to do a lot of legwork to get things working.”

AG Grid, an open source solution, is a feature-rich JavaScript data grid library used to build interactive and sophisticated data tables or grids in web applications. A JavaScript grid is a UI component used to display and manage tabular data in a web application. It provides a structured way to present information in rows and columns, making it easy for users to understand and interact with the data.

AG Grid provides a way to put these grids into your web applications, he added. It’s essentially like React Table but with “batteries included,” he added.

“The simplest way I can describe that is it’s built to be basically Excel for web developers,” he said. “Essentially, it lets you put a very powerful table into your web applications.”

Last year, the company launched AG Charts, a charting library created as a way to power the integrated charting features of AG Grid, where it’s possible to highlight data and build charts from it.

“In order to power that functionality, we essentially had to build a whole charting library to do that, and we took the decision last year to turn it into its own product, essentially,” he said. “Now AG Charts is a completely standalone JavaScript charting library with support from React, Angular and Vue, much the same as AG Grid.”

The two products are built to work seamlessly together, but they can also be used as standalone applications, he added.

## Support for Frameworks
For both products, the core business logic is written in JavaScript, which allows the solutions to be very fast, Stinton-Bland said. AG Grid and AG Charts support [React](https://thenewstack.io/frontend-schism-will-react-server-components-destroy-react/), [Angular](https://thenewstack.io/angulars-approach-to-partial-hydration/), [Vue](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/) and JavaScript with full TypeScript support. Solid was supported, but that has been deprioritized due to less interest than anticipated, he said. However, [Solid](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) does offer its [own wrapper for AG Grid](https://github.com/solidjs-community/solid-ag-grid), he added.

“We’re not restricted by any of the restrictions of the individual frameworks, but then we actually provide full support for those frameworks on top of that, and it’s not a thin wrapper layer or anything like that,” he said. “All of the rendering is done in pure React, for example. In that way, you can get all of the benefits of performing your logic in pure JavaScript, but you also get all the benefits of it working just like you would expect any other React library to.”

## Features of AG Grid
AG Grid can handle large amounts of data without seeing any sort of lag or performance drops from the UI perspective, Swinton-Bland said. They make sure to optimize every release.

“Because of all of that core business logic being in pure JavaScript, we don’t have any of the overhead that you might get with some pure React libraries, for example,” he said.

![A chart from AG Grid showing performance of of a grid with adjustable rows and columns.](https://cdn.thenewstack.io/media/2024/11/3cc1515d-aggrid.jpg)
Screenshot from AG-Grid’s example page.

AG Grid has what it calls client-side role models and server-side role models. Developers can either hand all of the data off to AG Grid and it will manage it on the client side, or developers can implement the server-side row model, which would require the developer to figure out how they want to send the data from the server to AG Grid. The product offers features that allow you to easily make that connection, Swinton-Bland said. It also supports features such as tree data views, master-detail views, and things like that.

“If you have more nested data or different levels of data, there [are] features in there to fit those use cases as well,” Swinton-Bland said. “It really is quite versatile. I don’t think we would find a use case where we wouldn’t be able to handle the data.”

Ag Grid also does virtualization out of the box, which means that rather than loading all of your data in one go into the data grid and the browser, AG Grid loads what you see or what you want the user to see and then some data before and after it.

“A lot of other data grids will do the same sort of thing,” he added. “They’ll implement virtualization, but the way that we’ve done it is just in a much more performant way, essentially.”

Most recently, the company has put together a new community section of their website. Under [tools and extensions](https://www.ag-grid.com/community/tools-extensions/), there’s a list of the ecosystem built for AG Grid, including extensions and open source tools.

“Companies have built design systems and custom themes,” he said. “They’ve built wrappers and integrations for no code, [low code platforms](https://thenewstack.io/what-a-low-code-platform-offers-frontend-developers/) for other frameworks like .Net and Rust, and it really was quite surprising to me how much of an ecosystem there was built around and on top of AG-Grid.

The company has received fewer feature requests recently because there are “very few features that we get requests for from users that there isn’t a way to do it already.” That said, AG Grid is open to feature requests from developers.

“[Web development](https://roadmap.sh/roadmaps?g=Web+Development) is a constantly evolving and changing space, and so we put a lot of work into maintaining everything that we’ve built so far,” Swinton-Bland said. “AG Charts is a big focus of ours now as well. That being a whole new product, we’re constantly releasing new features, new series types and really trying to grow that product as well.”

**Competitors**
AG Grid lists its customers as Amazon, Facebook, Microsoft, PayPal and FedEx, among others. While it is a popular option open source solution for creating data grids and tables, it isn’t the only open source solution. Open source competitors include:

[Material UI](https://github.com/mui/material-ui)is an open source React component library that implements Google’s Material Design. Its clients include Netflix, Amazon, NASA and Shutterfly.[SlickGrid](https://github.com/6pac/SlickGrid)is another open source solution that’s designed for large datasets and real-time updates.
There are also proprietary competitors such as:

[DevExpress Data Grid](https://docs.devexpress.com/WindowsForms/3455/controls-and-libraries/data-grid)is a commercial offering known for its feature set of advanced filtering, grouping, and pivot tables.[Handsontable](https://handsontable.com/), which used to be open source but is no longer. Currently, it offers a free non-commercial license, which allows developers to use it for personal and non-profit projects. However, for commercial use, a commercial license is required.[Syncfusion Essential JS 2 DataGrid](https://ej2.syncfusion.com/demos/#/fluent2/grid/grid-overview.html), which includes data editing, filtering, grouping, and exporting. It offers a free community license for personal and small-scale commercial use, but the full version with[all features requires a commercial license](https://ej2.syncfusion.com/documentation/licensing/overview).
AG Charts’ open source competitors include [Chart.js](https://github.com/chartjs/Chart.js), [D3.js](https://github.com/d3/d3) and [Plotly.js](https://github.com/plotly/plotly.js).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)