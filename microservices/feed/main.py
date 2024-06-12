from fastapi import FastAPI, HTTPException
from .services import fetch_posts
from .schemas import Post

app = FastAPI()

@app.get("/feed/", response_model=list[Post])
async def get_feed(skip: int = 0, limit: int = 10):
    try:
        posts = await fetch_posts(skip=skip, limit=limit)
        return posts
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
