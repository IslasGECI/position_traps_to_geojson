def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def pandas_to_geojson() -> list[dict]:
    result = [
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
    return result
