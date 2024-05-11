from fastapi import FastAPI, HTTPException
from datetime import datetime
import singleton


app = FastAPI()
singleton.logger.info('FDP-SOS is starting up')

@app.get("/api/config")
async def read_config():
    try:
        return singleton.config
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
