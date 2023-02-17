import pandas as pd
from dash import Dash, html
from . import city_dropdown
from . import bar_chart_likes_sum, bar_chart_make_count


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    dashboard_description = """
    Welcome to the Twitter Data Visualization Dashboard! During the month of September, 
    tweets containing the names of the twenty most popular makes from the fifty most populated 
    cities, were collected using twint, an advanced twitter scraping tool. 
    """

    like_vs_make_desc = """
    LIKES COUNT VS. MAKE GRAPH: This graph provides a visual on the number of likes on all the tweets containing a 
    unique make has received in the month of September. It can be read as the following: 
    "all the tweets containing 'mercedes', combined, have received a total of 24,787 likes."
    """

    mention_vs_make_desc = """
    MENTIONS VS. MAKE GRAPH: This graph provides a visual on the number of mentions a unique make has received in the 
    data collected during the month of September. It can be read as the following: 
    "Out of all the tweets collected, there are 1030 mentions of 'tesla'."
    """

    return html.Div(
        className="app-div",
        children=[
            # title div
            html.Div([
                html.H1(app.title,
                        style={'height': '70px', 'align': 'middle'}),
                html.H4(dashboard_description)],
                # style={'backgroundColor': '#1CD760', 'color': 'white'},
            ),
            html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

            # dropdown div
            html.Div(
                className="dropdown-container",
                children=[
                    city_dropdown.render(app, data),
                ],
            ),
            html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

            # likes count vs. make graph div
            html.Div([
                html.H5(like_vs_make_desc),
                bar_chart_likes_sum.render(app, data),
                html.Hr(),
            ],
                # style={'backgroundColor': '#1CD760', 'color': 'white'}
            ),
            html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

            # mentions vs. make graph div
            html.Div([
                html.H5(mention_vs_make_desc),
                bar_chart_make_count.render(app, data),
                html.Hr(),
            ],
                # style={'backgroundColor': '#1CD760', 'color': 'white'}
            ),
        ],
    )
