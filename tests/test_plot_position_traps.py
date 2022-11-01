import hashlib
import os
import pandas as pd
import pytest

from position_traps_to_geojson import add_geometry, LittleMap

dataframe = pd.read_csv("tests/data/position_traps_example.csv")
dataframe_columns = len(dataframe.columns)


def test_LittleMap():
    mapita = LittleMap()
    mapita.load_data(dataframe)
    obtained_columns = len(mapita.geopandas.columns)
    assert obtained_columns == dataframe_columns + 1
    mapita.plot("salidita.png")
    expected_hash = "01df0b13f403016caf4c9de2d622d86a"
    obtained_hash = _make_hash("salidita.png")
    assert obtained_hash == expected_hash
    mapita.read_island("tests/data/linea_costa_isla_guadalupe.shp")
    mapita.plot("salidita_con_isla.png")
    expected_hash = "0c94c323c1e97d1b777067b1fe07cbe6"
    obtained_hash = _make_hash("salidita_con_isla.png", remove = False)
    assert obtained_hash == expected_hash

def _make_hash(png_path, remove = True):
    file_content = open(png_path, "rb").read()
    obtained_hash = hashlib.md5(file_content).hexdigest()
    if remove:
        _remove_file(png_path)
    return obtained_hash

def _remove_file(path):
    if os.path.exists(path):
        os.remove(path)
