import geopandas
import utm


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
