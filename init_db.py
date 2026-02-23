import asyncio
from database import engine, Base
import models.csv_upload

async def init():
    async with engine.begin() as conn:
        print(Base.metadata.tables)
        await conn.run_sync(Base.metadata.create_all)
        
asyncio.run(init())