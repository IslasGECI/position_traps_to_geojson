from position_traps_to_geojson import pandas_to_geojson
import pandas as pd


def test_pandas_to_geojson():
    dataframe = pd.DataFrame.from_dict(
        {
            "lat": [-118.28],
            "long": [28.87],
            "is_active": [True],
            "date": ["2021-04-06"],
            "id": ["TC-01-003-AC"],
        }
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.27174112495435, 28.89831545888804],
            },
            "properties": {
                "is_active": "true",
                "date": "2021-04-06",
                "id": "TC-01-003-AC",
            },
        }
    ]
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained
    dataframe = pd.DataFrame.from_dict(
        {
            "lat": [-118.28],
            "long": [28.87],
            "is_active": [True],
            "date": ["2021-04-06"],
            "id": ["TC-01-003-AC"],
        }
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.28, 28.87],
            },
            "properties": {
                "is_active": "true",
                "date": "2021-04-06",
                "id": "TC-01-003-AC",
            },
        }
    ]
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained
