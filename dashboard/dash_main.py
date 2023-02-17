from dash import Dash, html, dcc
from dash import Input, Output

import plotly.express as px

import pandas as pd

from dashboard.dash_loader import load_transaction_data
from dashboard.dash_layout import create_layout


def main(csv_path: str) -> None:
    app = Dash()
    data = load_transaction_data(csv_path)

    app.title = 'Twitter Data Dashboard'
    app.layout = create_layout(app, data)


if __name__ == '__main__':
    main()
