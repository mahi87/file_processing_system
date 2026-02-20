import json
import uuid

from fastapi import File, Form, HTTPException, Response, UploadFile
from starlette.status import HTTP_201_CREATED

from api import google_connect as gc
from main import app
from schemas.upload_file import Metadata


@app.post("/upload_csv")
def upload_csv(file: UploadFile=File(), metadata: str =Form()):
    try:
        metadata_obj = Metadata(**json.loads(metadata))
        bucket = gc.get_bucket()
        blob = bucket.blob(f"{uuid.uuid4()}_{file.filename}")
        blob.upload_from_file(
            file.file, 
            content_type=file.content_type)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid metadata: {e}")
    return Response(status_code=HTTP_201_CREATED, content=metadata_obj.email)