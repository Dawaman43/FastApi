from fastapi import FastAPI
from path import router as path_router
from query import router as query_router

app = FastAPI()

app.include_router(path_router)
app.include_router(query_router)

