from fastapi import APIRouter, status
from schemas.user_scheme import User
from typing import List

user_router = APIRouter()

@user_router.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register an user',
    tags=['User']
)
def signup():
    pass

@user_router.post(
    path='/login',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary='Login an user',
    tags=['User']
)
def login():
    pass

@user_router.get(
    path='/users',
    response_model=List[User],
    status_code = status.HTTP_200_OK,
    summary='Get all users',
    tags=['User']
)
def get_users():
    pass

@user_router.get(
    path='/users/{user_id}',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary='Get an user',
    tags=['User']
)
def get_user():
    pass

@user_router.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary='Delete an user',
    tags=['User']
)
def delete_user():
    pass

@user_router.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary='Update an user',
    tags=['User']
)
def update_user():
    pass