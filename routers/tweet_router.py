from fastapi import APIRouter, status
from schemas.tweet_scheme import Tweet
from typing import List

tweet_router = APIRouter()

@tweet_router.get(
    path="/all_tweets",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Get all tweets',
    tags=['Tweet']
)
def get_all_tweets():
    return {"Twitter API": "Working"}

@tweet_router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweet']
)
def post_tweet():
    pass

@tweet_router.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweet']
)
def show_a_tweet():
    pass

@tweet_router.delete(
    path="/tweet/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweet']
)
def delete_tweet():
    pass

@tweet_router.put(
    path="/tweet/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweet']
)
def update_tweet():
    pass