from typing import Annotated

from fastapi import FastAPI, Path, Query
from requests import get

from constants import API_KEY, API_URL

app = FastAPI()


@app.get("/")
def hello_world(name: str = "World"):
    return "Welcome to the Weather API made in FastAPI"


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
    data = get(URL).json()

    return data
