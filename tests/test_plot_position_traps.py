import pandas as pd
import pytest

from position_traps_to_geojson import add_geometry, add_lat_lon, utm_2_lat_lon

dataframe = pd.read_csv("tests/data/position_traps_example.csv")
dataframe_columns = len(dataframe.columns)


def test_utm_2_lat_lon():
    x_coordinate = 374682
    y_coordinate = 3200783
    obtained_lat_lon = utm_2_lat_lon(x_coordinate, y_coordinate)
    expected_latitude = 28.92
    expected_longitude = -118.28
    assert pytest.approx(obtained_lat_lon[0], 0.01) == expected_latitude
    assert pytest.approx(obtained_lat_lon[1], 0.01) == expected_longitude


def test_add_lat_lon():
    obtained_lat_lon = add_lat_lon(dataframe)
    obtained_columns = len(obtained_lat_lon.columns)
    assert obtained_columns == dataframe_columns + 2
    expected_latitude = 28.92
    expected_longitude = -118.28
    assert pytest.approx(obtained_lat_lon.Lat[0], 0.01) == expected_latitude
    assert pytest.approx(obtained_lat_lon.Lon[0], 0.01) == expected_longitude


def test_add_geometry():
    obtained_geometry = add_geometry(dataframe)
    obtained_columns = len(obtained_geometry.columns)
    assert obtained_columns == dataframe_columns + 3
