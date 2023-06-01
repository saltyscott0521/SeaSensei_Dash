# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('SeaSensei', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H1('Surf Forecast'),
            html.H5('''
                Welcome to SeaSensei, happy surfing!
            '''),
            html.Div('''
            SeaSensei is an alternative surf forecasting application utilizing different and proprietary techniques for providing the average surfer with information to make the most of their surf adventures.
            ''')
        ])
    ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)