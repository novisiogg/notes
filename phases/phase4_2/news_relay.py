from fastapi import FastAPI, Header, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


# This is your "door" for the agent to knock on
@app.get("/sources")
async def get_sources(x_agent_secret: str = Header(...)):

    # 1. SECURITY: Check if the Agent provided the correct secret
    if x_agent_secret != "couple-bands":
        raise HTTPException(status_code=403, detail="Unauthorized")

    # 2. RELAY: Call the actual NewsAPI
    # We use httpx.AsyncClient() to keep the server non-blocking
    async with httpx.AsyncClient() as client:
        # You need your actual API key for the NewsAPI here
        api_key = os.getenv("NEWS_KEY")
        url = "https://newsapi.org/v2/top-headlines/sources"

        # We pass the key in the headers as required by NewsAPI docs
        headers = {"X-Api-Key": api_key}

        response = await client.get(url, headers=headers)

        # 3. RETURN: Send the data back to your agent
        return response.json()
    
    

