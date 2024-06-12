import httpx
from .config import settings
from .schemas import Post

async def fetch_posts(skip: int = 0, limit: int = 10):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.post_service_url}/posts/", params={"skip": skip, "limit": limit})
        response.raise_for_status()
        return [Post(**post) for post in response.json()]
