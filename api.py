from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/add/")
async def add(a: int, b: int):
    return {"result": a + b}

@app.get("/time/")
async def get_time():
    return {"time": datetime.now().isoformat()}
