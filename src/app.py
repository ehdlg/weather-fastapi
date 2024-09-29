from json import dumps, loads
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query
from requests import get

from cache import get_cache, set_cache
from constants import API_KEY, API_URL
from utils import generate_query

app = FastAPI()


@app.get("/")
def hello_api():
    return "Welcome to the WeatherAPI"


@app.get("/{location}")
def get_weather(
    location: Annotated[
        str,
        Path(
            description="Location to search the weather data",
        ),
    ],
    country: Annotated[
        str | None,
        Query(description="Country to retrieve weather information."),
    ] = None,
    language: Annotated[
        str | None,
        Query(
            description="Sets the language of the translatable parts of the output such as the conditions field.",
        ),
    ] = None,
    unit_group: Annotated[
        str | None,
        Query(
            description="The system of units used for the output data. Supported values are us, uk, metric, base",
        ),
    ] = "metric",
):
    query = generate_query(location, country, language, unit_group)

    URL = f"{API_URL}/{query}&key={API_KEY}"

    cached_data = get_cache(query)

    if cached_data is not None:
        return loads(cached_data)

    response = get(URL)

    if not response.ok:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    data = response.json()
    set_cache(query, dumps(data))

    return data
