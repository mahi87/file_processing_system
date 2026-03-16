import json
from fastapi import HTTPException, Response, Depends
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from main import app
from services import validate_file as vf
from schemas.validate_file import FileAddress
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db


@app.post("/validate")
async def validate_file(file_address: FileAddress, db: AsyncSession = Depends(get_db)):
    
    try:
        response=await vf.validate_file(file_address.file_address,db)
        return Response(status_code=HTTP_201_CREATED, content=response)
    except ValueError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {e}")
        