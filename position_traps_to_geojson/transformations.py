def pandas_to_geojson(dataframe) -> list[dict]:
    list_of_dictionary = dataframe.to_dict("records")
    result = [la_funcion(dictionary) for dictionary in list_of_dictionary]
    return result


def la_funcion(result2):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [result2["lat"][0], result2["long"][0]],
        },
        "properties": {
            "is_active": result2["is_active"][0],
            "date": result2["date"][0],
            "id": result2["id"][0],
        },
    }
