import json
from main import app
from schemas.upload_file import Metadata
from fastapi import UploadFile, File, Form


@app.post("/upload_csv")
def upload_csv(file: UploadFile=File(), metadata: str =Form()):
    metadata_obj = Metadata(**json.loads(metadata))
    return metadata_obj.email