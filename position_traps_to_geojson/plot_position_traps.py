import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import utm


class LittleMap:
    def __init__(self):
        self.coordinatesGRS = None
        self.geopandas = None
        self.island = None
        self.datos = pd.read_csv("tests/data/actived_and_inactive_traps.csv")

    def load_data(self, original_data):
        self.datos = original_data.copy()
        self.geopandas = self._add_geometry(original_data)
        self.inactivated_traps = self.geopandas.loc[~self.geopandas["is_active"]]
        self.activated_traps = self.geopandas.loc[self.geopandas["is_active"]]

    def write_geojson(self, geojson_path):
        self.geopandas.to_file(geojson_path, driver="GeoJSON")

    def plot(self, output_path):
        fig, ax = plt.subplots()
        plt.gca().set_facecolor("#E6FFFF")
        self.geopandas.plot(ax=ax)
        if isinstance(self.island, geopandas.GeoDataFrame):
            ax1 = self.island.plot(ax=ax, edgecolor="black", facecolor="#fffae6", linewidth=0.5)
            self.activated_traps.plot(ax=ax1, color="blue", markersize=2)
            self.inactivated_traps.plot(ax=ax1, color="black", markersize=1)
        plt.savefig(output_path)

    def read_island(self, shp_path):
        self.island = geopandas.read_file(shp_path)

    def _add_geometry(self, df):
        return geopandas.GeoDataFrame(
            df, geometry=geopandas.points_from_xy(df["Coor-X"], df["Coor-Y"])
        )

    def add_latlon(self):
        self.coordinatesGRS = self.datos.copy()
        coordinatesGRS = utm.to_latlon(
            self.coordinatesGRS["Coor-X"], self.coordinatesGRS["Coor-Y"], 11, "R"
        )
        self.coordinatesGRS["lat"] = coordinatesGRS[0]
        self.coordinatesGRS["lon"] = coordinatesGRS[1]
