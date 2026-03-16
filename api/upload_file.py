from fastapi import Depends, File, Form, HTTPException, Response, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

import json
from main import app
from services import upload_file as uf
from database import get_db


@app.post("/upload_csv")
async def upload_csv(file: UploadFile=File(), metadata: str =Form(), db: AsyncSession = Depends(get_db)):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"{file.content_type} is not supported, only CSV allowed")
    try:
        response = await uf.upload_csv(file,metadata,db)
        result={"email":response.user}
        return Response(status_code=HTTP_201_CREATED, content=json.dumps(result))
    except ValueError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {e}")