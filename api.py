from fastapi import FastAPI, HTTPException
from datetime import datetime
import singleton
import uvicorn

app = FastAPI()

@app.get("/api/config")
async def read_config():
    try:
        return singleton.config
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Config file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/disconnet")
async def disconnet():
    return {"message": "Welcome to the FastAPI application!"}


@app.post("/api/cancelorder")
async def cancel_order(a: int, b: int):
    return {"result": a + b}


@app.post("/api/canceltrade")
async def cancel_trade():
    return {"time": datetime.now().isoformat()}


if __name__ == "__main__":
    singleton.logger.info("FDP-SOS is starting up")
    singleton.logger.info(f"application config: {singleton.config}")
    from uvicorn.config import LOGGING_CONFIG
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = '%(asctime)s    %(levelname)s:    %(message)s'
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s    %(levelname)s:    %(client_addr)s - "%(request_line)s" %(status_code)s'
    uvicorn.run("api:app", host="0.0.0.0", port=singleton.config["api"]["port"], log_config=LOGGING_CONFIG)