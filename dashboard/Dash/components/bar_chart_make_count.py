import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids

STATE_DATA = px.data.medals_long()


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART_MAKE_COUNT, "children"),
        Input(ids.CITY_DROPDOWN, "value")
    )
    def update_bar_chart(cities: list[str]) -> html.Div:
        filtered_data = data.query("near in @cities")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")

        fig = px.histogram(
            data, x="make",
            category_orders=dict(make=['mercedes', 'bmw', 'lexus', 'ford', 'honda',
                                       'toyota', 'chevrolet', 'audi', 'nissan',
                                       'land rover', 'subaru', 'tesla', 'hyundai',
                                       'GMC', 'jaguar', 'volvo', 'volkswagen',
                                       'rivian', 'dodge', 'jeep']),
            color="make").update_xaxes(categoryorder='total descending')

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART_MAKE_COUNT)

    return html.Div(id=ids.BAR_CHART_MAKE_COUNT)
