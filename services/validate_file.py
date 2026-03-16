import csv
import io

from fastapi import HTTPException
from pydantic import ValidationError
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_406_NOT_ACCEPTABLE, HTTP_500_INTERNAL_SERVER_ERROR

from repository.save_content import save_content
from schemas.validate_file import Content
from services import google_connect as gc
from custom_exception import DBException


async def validate_file(file_address,db):

    bucket = gc.get_bucket()
    blob = bucket.blob(file_address)
    data = blob.download_as_bytes(timeout=10)
    
    try:
        decoded=data.decode("utf-8-sig")
        reader=csv.DictReader(io.StringIO(decoded))
        validated_content=[]
        for i, row in enumerate(reader, start=1):
            try:
                model=Content(**row)
                validated_content.append(model.model_dump())
            except ValidationError as e:
                raise HTTPException(status_code=HTTP_406_NOT_ACCEPTABLE, detail=f"row {i} has invalid type {e}")
        response=await save_content(validated_content,db)
        return response
    except DBException as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=e.detail)
    except HTTPException as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"Invalid CSV")
        