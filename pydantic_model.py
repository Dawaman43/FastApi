from typing import Annotated, Literal
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

# FastApi extracts data from each field  from query parameters and it will give us pydantic model
# You can visualize and test in http://127.0.0.1:8000/docs#/default/
router = APIRouter()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@router.get("/orders")
async def read_orders(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
