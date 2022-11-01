import geopandas
import utm
import matplotlib.pyplot as plt


class LittleMap():
    def __init__(self):
        self.geopandas = None
    def load_data(self, original_data):
        self.geopandas = add_geometry(original_data)
    def plot(self, output_path):
        self.geopandas.plot()
        plt.savefig(output_path)


def utm_2_lat_lon(x_coor, y_coor):
    return utm.to_latlon(x_coor, y_coor, 11, "R")


def add_lat_lon(df):
    transformed_coordinate = utm_2_lat_lon(df["Coor-X"], df["Coor-Y"])
    df["Lat"] = transformed_coordinate[0]
    df["Lon"] = transformed_coordinate[1]
    return df


def add_geometry(df):
    df = add_lat_lon(df)
    return geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Lon, df.Lat))
