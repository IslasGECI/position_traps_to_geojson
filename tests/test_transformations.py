from position_traps_to_geojson import pandas_to_geojson


def test_pandas_to_geojson():
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
    obtained = pandas_to_geojson()
    assert expected == obtained
