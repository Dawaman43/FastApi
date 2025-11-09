from typing import Union
from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}


#path parameter 
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#path parameter with type
@app.get("/products/{product_id}")
async def read_item(product_id: int):
    return {"product_id": product_id} 
    # http://127.0.0.1:8000/products/1 this works and prints returns {"product_id":1}
    # but if i try to log http://127.0.0.1:8000/products/string  this will return 

    #     {
    #   "detail": [
    #     {
    #       "type": "int_parsing",
    #       "loc": [
    #         "path",
    #         "product_id"
    #       ],
    #       "msg": "Input should be a valid integer, unable to parse string as an integer",
    #       "input": "string"
    #     }
    #   ]
    # }

    #Fastapi gives automatic data conversion


    # to get the ui docs of the project use http://127.0.0.1:8000/docs and you will see swagger ui 
    # if you need alternative ui docs http://127.0.0.1:8000/redoc

    # in FastApi order of routes matters

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}