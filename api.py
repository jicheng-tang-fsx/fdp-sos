from fastapi import FastAPI, HTTPException
import os, tomllib
from datetime import datetime

app = FastAPI()

@app.get("/api/config")
async def read_config():
    config_path = "/app/config.toml"
    try:
        with open(config_path, 'rb') as config_file:
            config = tomllib.load(config_file)
        return config
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Config file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/add/")
async def add(a: int, b: int):
    return {"result": a + b}

@app.get("/time/")
async def get_time():
    return {"time": datetime.now().isoformat()}
