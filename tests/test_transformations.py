import position_traps_to_geojson as ptg


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = ptg.add_offset(augend, addend)
    assert expected == obtained


def test_pandas_to_geojson():
    expected = [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [125.6, 10.1]},
            "properties": {"is_active": "true", "date": "2021-01-23"},
        }
    ]
    obtained = ptg.pandas_to_geojson()
    assert expected == obtained
