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
        fig, ax = plt.subplots()
        plt.gca().set_facecolor("#E6FFFF")
        self.geopandas.plot(ax=ax)
        if isinstance(self.island, geopandas.GeoDataFrame):
            ax1 = self.island.plot(ax=ax,edgecolor="black", facecolor="#fffae6")
            self.geopandas.plot(ax=ax1, color="blue", markersize=4)
        plt.savefig(output_path)

    def read_island(self, shp_path):
        self.island = geopandas.read_file(shp_path)

    def _add_geometry(self, df):
        return geopandas.GeoDataFrame(
            df, geometry=geopandas.points_from_xy(df["Coor-X"], df["Coor-Y"])
        )

    def margins_from_polygon(
    geoambiental_polygon, gap_left=100, gap_right=100, gap_up=100, gap_down=100, n_points=100
):
        margin_x = margins_from_coordinate(geoambiental_polygon.x, gap_left, gap_right, n_points)
        margin_y = margins_from_coordinate(geoambiental_polygon.y, gap_down, gap_up, n_points)
        return margin_x, margin_y
