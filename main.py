from fastapi import FastAPI

app = FastAPI()
app.title = "My personal Twitter App"
app.version = "0.0.1"
app.description = "This is an app for course of Platzi"

@app.get(
    path='/',
    tags=["Home"]
    )
def home():
    """
    Default API of application
    """
    return {"Twitter API": "Working"}

