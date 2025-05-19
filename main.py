from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

import random

app = FastAPI()

SYSTEM_CODES = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}


current_damaged_system = {"damaged_system": random.choice(list(SYSTEM_CODES.keys()))}


@app.get("/status")
def get_status():
    return current_damaged_system


@app.get("/repair-bay", response_class=HTMLResponse)
def get_repair_bay():
    system = current_damaged_system["damaged_system"]
    code = SYSTEM_CODES.get(system, "UNKNOWN")
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Repair</title></head>
    <body>
    <div class="anchor-point">{code}</div>
    </body>
    </html>
    """


@app.post("/teapot")
def post_teapot():
    return Response(content="I'm a teapot", status_code=418)
