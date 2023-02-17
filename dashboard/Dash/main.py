from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout
from data.loader import load_transaction_data

DATA_PATH = "../../../Dash/data/september_data_cleaned.csv"


def main() -> None:
    data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Tweet Dashboard"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
