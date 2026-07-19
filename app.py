import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read the processed data
df = pd.read_csv("formatted_output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Group sales by date
sales_by_date = (
    df.groupby("date", as_index=False)["sales"]
    .sum()
    .sort_values("date")
)

fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Total Sales"
    },
    render_mode="svg"
)
# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Visualizer",
        style={
            "textAlign": "center",
            "marginBottom": "30px"
        }
    ),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
