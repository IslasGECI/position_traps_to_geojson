def pandas_to_geojson(dataframe) -> dict:
    list_of_dictionary = dataframe.to_dict("records")
    feature_collection = [dictionary_to_geojson(dictionary) for dictionary in list_of_dictionary]
    return {"type": "FeatureCollection", "features": feature_collection}


def dictionary_to_geojson(row: dict) -> dict:
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row["lat"][0], row["long"][0]],
        },
        "properties": {
            "is_active": row["is_active"][0],
            "date": row["date"][0],
            "id": row["id"][0],
        },
    }
