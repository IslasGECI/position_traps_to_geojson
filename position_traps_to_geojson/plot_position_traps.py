import geopandas
import matplotlib.pyplot as plt


class LittleMap:
    def __init__(self):
        self.geopandas = None
        self.island = None

    def load_data(self, original_data):
        self.geopandas = self._add_geometry(original_data)
        self.inactivated_traps = self.geopandas.loc[~self.geopandas["is_active"]]
        self.activated_traps = self.geopandas.loc[self.geopandas["is_active"]]

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
