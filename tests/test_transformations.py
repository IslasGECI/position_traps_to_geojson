from position_traps_to_geojson import pandas_to_geojson
import pandas as pd


def fix_expected(expected):
    return {"type": "FeatureCollection", "features": expected}


def test_pandas_to_geojson_list():
    dataframe = pd.read_csv("tests/data/example_geographic_data.csv")
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.27, 28.89831545888804],
            },
            "properties": {
                "is_active": True,
                "date": "2021-04-06",
                "id": "TC-01-003-AC",
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-178.28, 38.87],
            },
            "properties": {
                "is_active": True,
                "date": "2022-03-08",
                "id": "TC-01-004-NR",
            },
        },
    ]
    expected = fix_expected(expected)
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained
