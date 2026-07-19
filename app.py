import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read data
df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Visualizer",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        html.Div([
            html.Label(
                "Select Region",
                style={
                    "fontSize": "20px",
                    "fontWeight": "bold"
                }
            ),

            dcc.RadioItems(
                id="region-filter",

                options=[
                    {"label": " All", "value": "all"},
                    {"label": " North", "value": "north"},
                    {"label": " South", "value": "south"},
                    {"label": " East", "value": "east"},
                    {"label": " West", "value": "west"},
                ],

                value="all",

                inline=True,

                style={
                    "marginTop": "10px",
                    "marginBottom": "25px",
                    "fontSize": "18px"
                }
            )
        ]),

        dcc.Graph(id="sales-chart")
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    sales = (
        filtered.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales ({region.title()})",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        },
        render_mode="svg"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)