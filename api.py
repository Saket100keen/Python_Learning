from system_utils import get_system_health
from fastapi import FastAPI #type: ignore

app = FastAPI(title="DevOps Utilities API")

@app.get("/hello")
def hello():
    return {"message": "Hello, Friends from DevOps Utilities API!"} 

@app.get("/metrics")
def metrics():
    return get_system_health()