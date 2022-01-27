def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def pandas_to_geojson() -> list[dict]:
    result = [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [125.6, 10.1]},
            "properties": {"is_active": "true", "date": "2021-01-23"},
        }
    ]
    return result
