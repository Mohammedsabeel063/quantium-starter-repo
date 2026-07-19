import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert "Soul Foods Pink Morsel Sales Visualizer" in header.text


def test_graph_exists(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")

    assert radio is not None
