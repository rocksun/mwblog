# Introduction To Plotly Dash, the Most Popular AI Data Tool
![Featued image for: Introduction To Plotly Dash, the Most Popular AI Data Tool](https://cdn.thenewstack.io/media/2024/08/a50a2946-and-machines-dly3c1siybc-unsplash-1024x724.jpg)
The go-to language for data analysis, and to some extent AI development, is Python. [Plotly Dash](https://dash.plotly.com/) is a presentation graphing tool for supporting data apps. Or in their words, “Dash is the original low-code framework for rapidly building data apps in Python.” But as usual, low code still requires a reasonable grasp of programming.

Earlier this month, Plotly Dash was named [the number one most popular tool](https://thenewstack.io/ai-dev-tools-ranked-and-astro-adds-support-for-large-sites/) in Databricks’ [State of Data + AI report](https://www.databricks.com/sites/default/files/2024-06/state-of-data-ai-report.pdf) — even above Langchain! So it’s clearly a trendy tool in the [AI engineering ecosystem](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/). “For more than 2 years, Dash has held its position as No. 1, which speaks to the growing pressure on data scientists to develop production-grade data and AI applications,” wrote Databricks.

In this post, I’ll install and play around with Dash, and maybe in a future post, we can build something with it. I’ve used [Jupyter notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) before, but here we’ll just use a classic web server to host the outcome.

So in my trusty Warp shell, we’ll [install](https://dash.plotly.com/installation) the two requirements. As I’m not a regular Python guy, I didn’t have the recommended Python version in my .zshrc shell configuration file, so I added that:

12 |
#python export PATH="$HOME/Library/Python/3.9/bin:$PATH" |
Then I used pip to install the dependent modules:
12 |
pip install dash pip install panadas |
Dash will effectively match HTML references into its own component base, and has some specially written interactive graphs and tables too.
To test that things are working, we’ll just try the [“minimal”](https://dash.plotly.com/minimal-app) app.py, and run it.

12345678910111213141516171819202122232425 |
from dash import Dash, html, dcc, callback, Output, Input import plotly.express as px import pandas as pd df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv') app = Dash() app.layout = [ html.H1(children='Title of Dash App', style={'textAlign':'center'}), dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'), dcc.Graph(id='graph-content') ] @callback( Output(component_id='graph-content', component_property='figure'), Input(component_id='dropdown-selection', component_property='value') ) def update_graph(value): dff = df[df.country==value] return px.line(dff, x='year', y='pop') if __name__ == '__main__': app.run(debug=True) |
We can see that a layout is established, and a couple of callbacks. So we’ll have to figure out what they are doing later. I’m guessing from the update_graph method that this is a population growth graph, even though the CSV link name gives us no clue.
After making the app.py file and running it, eventually, I get a response:

So looking at the local site at the local address stated, I have:

Note that “Canada” is the set choice in the dropdown, and that the graph changes immediately if I select another nation. So this gives us a bit of a clue as to what the callbacks are doing.
As expected, if I look at the CSV file contents, it has a bunch of data points:

12345678 |
country,continent,year,lifeExp,pop,gdpPercap Afghanistan,Asia,1952,28.801,8425333,779.4453145 Afghanistan,Asia,1957,30.332,9240934,820.8530296 ... Canada,Americas,1950,68.28,14011422,10581.26552 Canada,Americas,1951,68.55,14330675,10932.46678 Canada,Americas,1952,68.75,14785584,11367.16112 ... |
This means we can see what the x and y-axis labels refer to. We can also see the other data we could choose to graph.
Let’s [analyze](https://dash.plotly.com/tutorial) the code until we have figured the rest out. The pandas module read_csv results into a dataframe (hence “df”). This is just the structure for later work. You can read from an Excel data sheet directly too.

The `dcc`
module (Dash Core Components) gives us both the dropdown and the graph. Altogether, the layout is just a list of components: in our case a title, a dropdown and the graph.

At this point, it is interesting to note that neither the Graph nor the Dropdown components are ever referred to directly again. Indeed, the Graph does not even take in the DataFrame. Clearly, there is some studied [decoupling](https://thenewstack.io/devs-dont-just-read-about-design-patterns-implement-them/) going on.

Now, we use the IDs “dropdown-selection” and “graph-content”.

123456 |
... @callback( Output(component_id='graph-content', component_property='figure'), Input(component_id='dropdown-selection', component_property='value') ) ... |
We have an Output callback that refers to the “graph-content” ID first defined for the Graph component and uses the “figure” property of the component. Here, I think “figure” just means the diagram to display. The Input refers to the Dropdown component via the “dropdown-selection” ID, and reads the “value” property.
1234 |
... def update_graph(value): dff = df[df.country==value] return px.line(dff, x='year', y='pop') ... |
As there is only one method mentioned, update_graph, and we don’t use that in the code, it is clearly used by the graph component to, er, update the graph. This just takes the country value from the dropdown. In other words, I could replace `dff = df[df.country==value]`
with `dff = df[df.country==’Canada’]`
to see Canada’s stats from the DataFrame. You can go ahead and change the code with the live page — it hot reloads.
So when we change country, the graph is rebuilt, with each line of the csv feeding into the update_graph method; and in this case, making a line from point to point.

Let’s experiment. If we have understood this correctly, we should be able to add, say, a table using the same data. Now, assuming we get hold of the table constructor, what would we need?

- We will need the import line.
- Add it as a line to the layout.
We won’t need anything else if the table doesn’t interact — the data table is already a fully interactive component.

Next, I’ll add the [table import](https://dash.plotly.com/datatable) to the end of existing imports:

1 |
from dash import Dash, html, dcc, callback, Output, Input, dash_table |
I’ll also add the [table constructor](https://dash.plotly.com/tutorial) to the existing layout. We know it is a big table, so I’ll use a page size:
123456 |
app.layout = [ html.H1(children='Title of Dash App', style={'textAlign':'center'}), dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'), dcc.Graph(id='graph-content'), dash_table.DataTable(data=df.to_dict('records'), page_size=10) ] |
That already works, but we need to limit the columns to Country, Population and Year:
1234567891011121314 |
app.layout = [ html.H1(children='Population by year', style={'textAlign':'center'}), dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'), dcc.Graph(id='graph-content'), dash_table.DataTable(data=df.to_dict('records'), columns=[ {'name': 'Country', 'id': 'country', 'type': 'text'}, {'name': 'Population', 'id': 'pop', 'type': 'numeric'}, {'name': 'Year', 'id': 'year', 'type': 'numeric'} ], page_size=5, style_cell={'textAlign': 'left'} )] |
Notice that I added left alignment, a smaller page size and a nicer title. This gives us:
## The Verdict
Dash was pretty straightforward to work with, even though my Python is very much at a basic level. I was looking at controlling the data into the data_table, and that was a bit trickier.

It doesn’t feel entirely standardized, however, so you will need to read the notes for every component you want to try out. But I recommend you try it out the next time you want to show off some data.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)