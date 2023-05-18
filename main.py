from fastapi import FastAPI
from routers.user_router import user_router
from routers.tweet_router import tweet_router, get_all_tweets

app = FastAPI()
app.title = "My personal Twitter App"
app.version = "0.0.1"
app.description = "This is an app for course of Platzi"

app.include_router(user_router)
app.include_router(tweet_router)

@app.get(
    path='/',
    tags=["Home"]
    )
def home():
    """
    Default API of application
    """
    return get_all_tweets()