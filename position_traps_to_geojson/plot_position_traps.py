import geopandas
import utm
import matplotlib.pyplot as plt


class LittleMap:
    def __init__(self):
        self.geopandas = None
        self.island = None

    def load_data(self, original_data):
        self.geopandas = self._add_geometry(original_data)

    def plot(self, output_path):
        self.geopandas.plot()
        if isinstance(self.island, geopandas.GeoDataFrame):
            ax = self.island.plot(color="white", edgecolor="black")
            self.geopandas.plot(ax=ax)
        plt.savefig(output_path)

    def read_island(self, shp_path):
        self.island = geopandas.read_file(shp_path)

    def _add_geometry(self, df):
        return geopandas.GeoDataFrame(
            df, geometry=geopandas.points_from_xy(df["Coor-X"], df["Coor-Y"])
        )
