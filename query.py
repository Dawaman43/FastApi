from fastapi import APIRouter


router = APIRouter()

fake_items_db = [
    {"item_name": "food"},
    {"item_name": "electronics"},
    {"item_name": "books"},
]


@router.get("/items_db")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
