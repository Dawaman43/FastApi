from fastapi import FastAPI
from path import router as path_router
from query import router as query_router
from request_body import router as body_router
from pydantic_model import router as pydantic_router

app = FastAPI()

app.include_router(path_router)
app.include_router(query_router)
app.include_router(body_router)
app.include_router(pydantic_router)

