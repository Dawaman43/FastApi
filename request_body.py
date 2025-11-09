from typing import Annotated
from fastapi import APIRouter, Path, Query
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/")
async def create_items(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        if item.price == 0:
            return {"item": "Price is 0"}

        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@router.put("/items/")
async def update_items(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@router.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}


@router.get("/itemss")
async def read_itemss(
    q: Annotated[
        list[str] | None,
        Query(
            title="String query",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    query_items = {"q": q}
    return query_items


@router.get("/item")
async def read_item(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bas"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/product/{product_id}")
async def read_product(
    product_id: Annotated[int, Path(title="The id of the product", gt=2)],
    q: Annotated[str | None, Query(alias="product-query")] = None,
):
    results = {"product_id": product_id}
    if q:
        results.update({"q": q})
    return results

