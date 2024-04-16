from typing import Optional

import uvicorn as uvicorn
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware

from resolver import random_items, random_genres_items
from recommender import item_based_recommendation, user_based_recommendation

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello 전영준의 영화추천 서비스"}

@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre:str):
    result = random_genres_items(genre)
    return {"result": result}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}

# 사용예
# http://localhost:8000/user-based/?params=1:5&params=100:1&params=50:3
@app.get("/user-based/")
async def user_based(params:Optional[list[str]]=Query(None)):
    input_ratings_dict = dict(
        (int(x.split(":")[0]), float(x.split(":")[1])) for x in params)
    # print(input_ratings_dict)
    result = user_based_recommendation(input_ratings_dict)
    return {"result": result}

# 2024.4.3
# query parameter 실습
# localhost:8000/weather?q=seoul&units=metric
@app.get("/weather/")
async def weather(q: Optional [list[str]]=Query(None), units: str='today'):
    print(q)
    print(units)
    q_dict = dict((int(x.split(":")[0]), float(x.split(":")[1])) for x in q)
    print(q_dict)
    return {"result": f'q={q}  :  units={units}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

