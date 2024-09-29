from json import dumps, loads
from typing import Annotated

from fastapi import FastAPI, Path, Query
from requests import get

from cache import get_cache, set_cache
from constants import API_KEY, API_URL

app = FastAPI()


@app.get("/")
def hello_world(name: str = "World"):
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
):
    if country is not None:
        location = f"{location},{country}"

    URL = f"{API_URL}/{location}?key={API_KEY}&unitGroup={'metric'}"

    cached_data = get_cache(URL)

    if cached_data is not None:
        return loads(cached_data)

    data = get(URL).json()
    set_cache(URL, dumps(data))

    return data
