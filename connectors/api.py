
from fastapi import fastapi

app = FastAPI()

@app.get("/status")
async def get_status():
    return {"status": "Cycle Sync API is running"}

@app.get("/periods/")
async def list_periods():
    return {"periods": ["period1", "period2", "period3"]} 

@app.get("/periods/{period_id}")
async def read_period(period_id: int):
    return {"period_id": period_id, "period_data": "Details of the period"}

@app.post("/period/")
async def add_new_period(period: dict):
    return {"created_period": period}   

@app.put("/period/{period_id}")
async def update_period(period_id: int, period: dict):
    return {"period_id": period_id, "updated_data": period}   

@app.delete("/data/{period_id}")
async def delete_data(period_id: int):
    return {"period_id": period_id, "status": "Deleted"}    





@app.put("/periods/{period_id}")
async def modify_period(period_id: int, period: dict):
    return {"period_id": period_id, "modified_period": period}

@app.delete("/periods/{period_id}")
async def remove_period(period_id: int):
    return {"period_id": period_id, "status": "period removed"}
