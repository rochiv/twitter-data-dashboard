# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from twint_search import transform_twint_data as ttd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = ttd.transform_csv('/Users/rohit/PycharmProjects/PersonalProjects/twintProject/search_app/data/september_data.csv')

test_df = df.groupby(['make'])[['likes_count', 'replies_count', 'retweets_count']].sum()

print(test_df)

fig = px.bar(test_df, x="make", y="likes_count")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
