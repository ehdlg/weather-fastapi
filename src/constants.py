from os import getenv, path

from dotenv import load_dotenv

env_path = path.join(path.dirname(__file__), "..", ".env")
load_dotenv(env_path)

API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
API_KEY = getenv("API_KEY")
