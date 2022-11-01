import hashlib
import os
import pandas as pd
import pytest

from position_traps_to_geojson import LittleMap

dataframe = pd.read_csv("tests/data/position_traps_example.csv")
dataframe_columns = len(dataframe.columns)


class Test_LittleMap:
    mapita = LittleMap()
    mapita.load_data(dataframe)

    def test_property_geopandas(self):
        obtained_columns = len(self.mapita.geopandas.columns)
        assert obtained_columns == dataframe_columns + 1

    def test_plot_only_traps(self):
        self.mapita.plot("salidita.png")
        expected_hash = "01df0b13f403016caf4c9de2d622d86a"
        obtained_hash = self._make_hash("salidita.png")
        assert obtained_hash == expected_hash

    def test_plot_island_with_traps(self):
        self.mapita.read_island("tests/data/linea_costa_isla_guadalupe.shp")
        self.mapita.plot("salidita_con_isla.png")
        expected_hash = "2b326af621af7eba167c4ed3cecbef1a"
        obtained_hash = self._make_hash("salidita_con_isla.png", remove=False)
        assert obtained_hash == expected_hash

    def _make_hash(self, png_path, remove=True):
        file_content = open(png_path, "rb").read()
        obtained_hash = hashlib.md5(file_content).hexdigest()
        if remove:
            self._remove_file(png_path)
        return obtained_hash

    def _remove_file(self, path):
        if os.path.exists(path):
            os.remove(path)
