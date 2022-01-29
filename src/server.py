import json
from random import randrange

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import RedirectResponse

with open("./database/data.json") as json_file:
    data = json.load(json_file)
    dataLength = len(data)

app = FastAPI()


@app.get("/", tags=["Root"], include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")


@app.get("/api/v1/resources/dogs/all")
async def api_all():
    return jsonable_encoder(data)


@app.get("/api/v1/resources/dogs")
async def api_number(number: int = None, index: int = None):
    results = []
    if number:
        for _ in range(number):
            results.append(data[randrange(dataLength)])
    elif index:
        if index >= 0 and index < dataLength:
            results.append(data[index])
    else:
        raise HTTPException(
            status_code=404,
            detail="The resource could not be found. Please check your query",
        )
    return jsonable_encoder(results)