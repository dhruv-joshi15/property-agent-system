from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agents.cook_agent import CookCountyAgent
from agents.dallas_agent import DallasAgent
from agents.la_agent import LosAngelesAgent
from data.properties import PROPERTY_DATA as PROPERTIES_DATA
from agents.comparable_agent import get_comparables

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents with shared property data
cook_agent = CookCountyAgent(PROPERTIES_DATA)
dallas_agent = DallasAgent(PROPERTIES_DATA)
la_agent = LosAngelesAgent(PROPERTIES_DATA)

### ---------- GET ENDPOINTS ---------- ###

@app.get("/api/cook/properties")
def get_cook_properties():
    return {"results": cook_agent.run_agent("COOK", "M1")}

@app.get("/api/dallas/properties")
def get_dallas_properties():
    return {"results": dallas_agent.run_agent("DALLAS", "I-2")}

@app.get("/api/la/properties")
def get_la_properties():
    return {"results": la_agent.run_agent("LA", "M2")}

### ---------- POST ENDPOINTS (Comparables) ---------- ###

@app.post("/api/cook/properties")
async def get_cook_comparables(request: Request):
    try:
        body = await request.json()
        parcel_id = body.get("parcel_id")
        if not parcel_id:
            raise ValueError("Missing parcel_id")
        return {"comparables": get_comparables(parcel_id)}
    except Exception as e:
        print(f"[ERROR] Cook comparables: {e}")
        raise HTTPException(status_code=500, detail="Failed to get comparables")

@app.post("/api/dallas/properties")
async def get_dallas_comparables(request: Request):
    try:
        body = await request.json()
        parcel_id = body.get("parcel_id")
        if not parcel_id:
            raise ValueError("Missing parcel_id")
        return {"comparables": get_comparables(parcel_id)}
    except Exception as e:
        print(f"[ERROR] Dallas comparables: {e}")
        raise HTTPException(status_code=500, detail="Failed to get comparables")

@app.post("/api/la/properties")
async def get_la_comparables(request: Request):
    try:
        body = await request.json()
        parcel_id = body.get("parcel_id")
        if not parcel_id:
            raise ValueError("Missing parcel_id")
        return {"comparables": get_comparables(parcel_id)}
    except Exception as e:
        print(f"[ERROR] LA comparables: {e}")
        raise HTTPException(status_code=500, detail="Failed to get comparables")
