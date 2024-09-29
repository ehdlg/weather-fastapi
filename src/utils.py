def generate_query(
    location: str,
    country: str | None = None,
    language: str | None = None,
    unit_group: str | None = "metric",
) -> str:
    if country is not None:
        location = f"{location},{country}"

    query = f"{location}?unitGroup={unit_group}"

    if language:
        query += f"&language={language}"

    return query
