import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio',
                  'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Indianapolis',
                  'Charlotte', 'San Francisco', 'Seattle', 'Denver', 'Washington, DC', 'Nashville-Davidson',
                  'Oklahoma City', 'El Paso', 'Boston', 'Portland', 'Las Vegas', 'Detroit', 'Memphis', 'Louisville',
                  'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Mesa',
                  'Atlanta', 'Omaha', 'Colorado Springs', 'Raleigh', 'Long Beach', 'Virginia Beach', 'Miami',
                  'Minneapolis', 'Oakland', 'Tulsa', 'Bakersfield', 'Wichita', 'Arlington']
    unique_cities = sorted(set(all_cities))

    @app.callback(
        Output(ids.CITY_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_CITIES_BUTTON, "n_clicks")
    )
    def select_all_cities(_: int) -> list[str]:
        return unique_cities

    return html.Div(
        children=[
            html.H6("City", style={'margin-right': '2em'}),
            dcc.Dropdown(
                id=ids.CITY_DROPDOWN,
                options=[{"label": city, "value": city} for city in unique_cities],
                value=unique_cities,
                multi=True,
                placeholder="Select Business Area",

            ),
            # style=dict(display='flex'),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_CITIES_BUTTON,
                n_clicks=0,
            ),
        ],
        # style={"width": "25%", "height": "10%"}
    )
