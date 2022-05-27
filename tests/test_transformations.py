import pytest
from position_traps_to_geojson import pandas_to_geojson
import pandas as pd


def fix_expected(expected):
    return {"type": "FeatureCollection", "features": expected}


dataframe = pd.DataFrame.from_dict(
    [
        {
            "lat": [-118.27174112495435],
            "long": [28.89831545888804],
            "is_active": [True],
            "date": ["2021-04-06"],
            "id": ["TC-01-003-AC"],
        }
    ]
)
expected = [
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [-118.27174112495435, 28.89831545888804],
        },
        "properties": {
            "is_active": True,
            "date": "2021-04-06",
            "id": "TC-01-003-AC",
        },
    }
]
expected = fix_expected(expected)

testdata = [(dataframe, expected)]


@pytest.mark.parametrize("dataframe,expected", testdata)
def test_pandas_to_geojson(dataframe, expected):
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained


def test_pandas_to_geojson_():
    dataframe = pd.DataFrame.from_dict(
        [
            {
                "lat": [-118.28],
                "long": [28.87],
                "is_active": [True],
                "date": ["2021-04-06"],
                "id": ["TC-01-003-AC"],
            }
        ]
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.28, 28.87],
            },
            "properties": {
                "is_active": True,
                "date": "2021-04-06",
                "id": "TC-01-003-AC",
            },
        }
    ]
    expected = fix_expected(expected)
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained

    dataframe = pd.DataFrame.from_dict(
        [
            {
                "lat": [-118.28],
                "long": [28.87],
                "is_active": [True],
                "date": ["2022-02-02"],
                "id": ["TC-01-003-AC"],
            }
        ]
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.28, 28.87],
            },
            "properties": {
                "is_active": True,
                "date": "2022-02-02",
                "id": "TC-01-003-AC",
            },
        }
    ]
    expected = fix_expected(expected)
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained

    dataframe = pd.DataFrame.from_dict(
        [
            {
                "lat": [-118.28],
                "long": [28.87],
                "is_active": [False],
                "date": ["2022-02-02"],
                "id": ["TC-01-003-AC"],
            }
        ]
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.28, 28.87],
            },
            "properties": {
                "is_active": False,
                "date": "2022-02-02",
                "id": "TC-01-003-AC",
            },
        }
    ]
    expected = fix_expected(expected)
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained

    dataframe = pd.DataFrame.from_dict(
        [
            {
                "lat": [-118.28],
                "long": [28.87],
                "is_active": [False],
                "date": ["2022-02-02"],
                "id": ["TC-01-003-XP"],
            }
        ]
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.28, 28.87],
            },
            "properties": {
                "is_active": False,
                "date": "2022-02-02",
                "id": "TC-01-003-XP",
            },
        }
    ]
    expected = fix_expected(expected)
    obtained = pandas_to_geojson(dataframe)
    assert expected == obtained


def test_pandas_to_geojson_list():
    dataframe = pd.DataFrame.from_dict(
        [
            {
                "lat": [-118.28],
                "long": [28.87],
                "is_active": [False],
                "date": ["2022-02-02"],
                "id": ["TC-01-003-XP"],
            },
            {
                "lat": [-178.28],
                "long": [38.87],
                "is_active": [True],
                "date": ["2022-03-08"],
                "id": ["TC-01-004-NR"],
            },
        ]
    )
    expected = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-118.28, 28.87],
            },
            "properties": {
                "is_active": False,
                "date": "2022-02-02",
                "id": "TC-01-003-XP",
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
