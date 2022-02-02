def pandas_to_geojson(dataframe) -> list[dict]:
    result2 = dataframe.to_dict("records")
    result = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [result2[0]["lat"], result2[0]["long"]],
            },
            "properties": {
                "is_active": "true",
                "date": result2[0]["date"],
                "id": "TC-01-003-AC",
            },
        }
    ]
    return result
