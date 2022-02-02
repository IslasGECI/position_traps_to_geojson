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
                "is_active": result2[0]["is_active"],
                "date": result2[0]["date"],
                "id": result2[0]["id"],
            },
        }
    ]
    return result
