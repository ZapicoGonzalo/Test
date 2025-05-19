from fastapi import FastAPI, Response, Query
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

phase_data = {
    5:  {"specific_volume_liquid": 0.0011,  "specific_volume_vapor": 0.3928},
    6:  {"specific_volume_liquid": 0.00115, "specific_volume_vapor": 0.3021},
    7:  {"specific_volume_liquid": 0.0012,  "specific_volume_vapor": 0.2486},
    8:  {"specific_volume_liquid": 0.00125, "specific_volume_vapor": 0.2103},
    9:  {"specific_volume_liquid": 0.0013,  "specific_volume_vapor": 0.1814},
    10: {"specific_volume_liquid": 0.0035,  "specific_volume_vapor": 0.0035}
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


@app.get("/phase-change-diagram")
def get_phase_change_diagram(pressure: float = Query(..., ge=5, le=10)):
    pressure_int = int(pressure)
    if pressure_int in phase_data:
        return JSONResponse(content=phase_data[pressure_int])
    return JSONResponse(status_code=404, content={"error": "Pressure not found"})
