import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART_LIKES_SUM, "children"),
        Input(ids.CITY_DROPDOWN, "value")
    )
    def update_bar_chart(cities: list[str]) -> html.Div:
        filtered_data = data.query("near in @cities")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.LIKES_COUNT,
                index=DataSchema.MAKE,
                aggfunc="sum",
                fill_value=0
            )

            print(DataSchema.LIKES_COUNT)
            for col in pt.columns:
                print(col)

            return pt.reset_index().sort_values(DataSchema.LIKES_COUNT[0], ascending=False)

        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.MAKE,
            y=DataSchema.LIKES_COUNT[0],
            color="make"
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART_LIKES_SUM)

    return html.Div(id=ids.BAR_CHART_LIKES_SUM)


