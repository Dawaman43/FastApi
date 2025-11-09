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


# this is query parameter with type conversion
# it uses boolean for to decide if the term is long or short, it can be helpful in many scenarios
# you can test it using http://127.0.0.1:8000/terms?term_id=1&q=good&short=true
@router.get("/terms")
async def read_terms(term_id: str, q: str | None = None, short: bool = False):
    term = {"term_id": term_id}
    if q:
        term.update({"q": q})
    if not short:
        term.update({"Description": "The term has long description"})

    return term
