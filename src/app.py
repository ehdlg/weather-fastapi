from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world(name: str = "World"):
    return "Welcome to the Weather API made in FastAPI"
