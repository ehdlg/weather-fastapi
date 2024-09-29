# Weather API

This project is based on the [Weather API Wrapper Service](https://roadmap.sh/projects/weather-api-wrapper-service) from roadmap.sh. It's designed to provide weather data by fetching from the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api).

## Objectives

The main goals of this project were to practice creating APIs with FastAPI and to strengthen my knowledge of caching mechanisms using Redis.

## Features

- Fetch current weather data based on location input.
- Support for optional parameters, including country, language, and unit group.
- In-memory caching using Redis to store and retrieve weather data efficiently.

## Technologies Used

- **FastAPI**: Framework for building the weather API.
- **Redis**: In-memory data structure store for caching.
- **Requests**: For making HTTP requests to the Visual Crossing Weather API.
