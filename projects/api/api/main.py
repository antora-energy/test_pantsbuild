from fastapi import FastAPI
from library.main import hello

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": hello("Liz")}
