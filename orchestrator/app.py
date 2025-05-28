from fastapi import FastAPI
from orchestrator import app  # Import the app created in orchestrator.py (if applicable)

# If your app is already created within orchestrator.py
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/market_brief/{symbol}")
async def get_market_brief(symbol: str):
    # Your logic to generate a market brief
    market_data = api_agent.get_data(symbol)
    narrative = language_agent.generate_narrative(market_data)
    return {"narrative": narrative}
