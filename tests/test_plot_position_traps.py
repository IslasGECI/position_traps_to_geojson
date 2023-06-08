import hashlib
import os
import pandas as pd
import pytest

from position_traps_to_geojson import LittleMap

dataframe = pd.read_csv("tests/data/actived_and_inactive_traps.csv")
dataframe_columns = len(dataframe.columns)


class Test_LittleMap:
    mapita = LittleMap()
    mapita.load_data(dataframe)

    def test_init(self):
        mapita = LittleMap()
        assert mapita.geopandas is None
        assert mapita.island is None

    def test_property_geopandas(self):
        obtained_columns = len(self.mapita.geopandas.columns)
        assert obtained_columns == dataframe_columns + 1

    @pytest.mark.skip(reason="It is the gold")
    def test_write_geojson(self):
        geojson_path = "output.geojson"
        self.mapita.write_geojson(geojson_path)
        assert os.path.exists(geojson_path)
        expected_hash = "2157d06ce842e21e7cec7fcd6cd1e509"
        obtained_hash = self._make_hash(geojson_path)
        assert obtained_hash == expected_hash

    def test_plot_only_traps(self):
        self.mapita.plot("salidita.png")
        expected_hash = "d7ed621f49929e7c69b859c11512a6ed"
        obtained_hash = self._make_hash("salidita.png")
        assert obtained_hash == expected_hash

    def test_plot_island_with_traps(self):
        self.mapita.read_island("tests/data/linea_costa_isla_guadalupe.shp")
        self.mapita.plot("salidita_con_isla.png")
        expected_hash = "7626703fa9c07a5a772299baf350fcf8"
        obtained_hash = self._make_hash("salidita_con_isla.png", remove=False)
        assert obtained_hash == expected_hash

    def test_add_latlon(self):
        self.mapita.add_latlon()
        expected_columns = ["lat", "lon"]
        obtained_columns = self.mapita.coordinatesGRS.columns
        assert all([expected_column in obtained_columns for expected_column in expected_columns])

    def _make_hash(self, png_path, remove=True):
        file_content = open(png_path, "rb").read()
        obtained_hash = hashlib.md5(file_content).hexdigest()
        if remove:
            self._remove_file(png_path)
        return obtained_hash

    def _remove_file(self, path):
        if os.path.exists(path):
            os.remove(path)
