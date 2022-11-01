import hashlib
import pandas as pd
import pytest

from position_traps_to_geojson import add_geometry, add_lat_lon, LittleMap,utm_2_lat_lon

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


def test_LittleMap():
    mapita = LittleMap()
    mapita.load_data(dataframe)
    obtained_columns = len(mapita.geopandas.columns)
    assert obtained_columns == dataframe_columns + 3
    mapita.plot("salidita.png")
    expected_hash = "2bc635496791bdbdcb9726d4f6a304b0"
    obtained_hash = _make_hash("salidita.png")
    assert obtained_hash == expected_hash

def _make_hash(png_path):
    file_content = open(png_path, "rb").read()
    obtained_hash = hashlib.md5(file_content).hexdigest()
    return obtained_hash
