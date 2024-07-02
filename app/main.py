from fastapi import FastAPI
import os
import asyncpg
from datetime import datetime
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

# Retrieve database credentials from environment variables
db_url = os.getenv("DATABASE_URL")

# Database connection pool
db_pool = None

async def connect_to_database():
    global db_pool
    db_pool = await asyncpg.create_pool(dsn=db_url)

async def insert_timestamp():
    async with db_pool.acquire() as connection:
        current_time = datetime.now()
        await connection.execute("INSERT INTO ping_timestamps (timestamp) VALUES ($1)", current_time)
        return current_time

@app.on_event("startup")
async def startup_event():
    await connect_to_database()

@app.get("/ping")
async def root():
    timestamp = await insert_timestamp()
    return {"message": "Timestamp inserted: %s" % timestamp}

@app.get("/ping_timestamps")
async def get_ping_timestamps():
    async with db_pool.acquire() as connection:
        timestamps = await connection.fetch("SELECT timestamp FROM ping_timestamps ORDER BY timestamp DESC")
        return {"ping_timestamps": [row[0] for row in timestamps]}
