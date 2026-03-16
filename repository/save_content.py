from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from models.content import Content
from custom_exception import DBException

async def save_content(content,db):
    try:
        async with db.begin():
            objects = []
            
            for _,row in enumerate(content, start=1):
                obj=Content(**row)
                objects.append(obj)
                
            db.add_all(objects)
        return "Saved to database"
        
    except Exception as e:
        print("DB error in save_content:", repr(e))
        raise DBException(detail=f"DB error in save_content: {repr(e)}")