import json
import uuid


from services import google_connect as gc
from schemas.upload_file import Metadata
from repository.save_metadata import save_metadata

async def upload_csv(file, metadata,db):
    try:
        metadata_obj = Metadata(**json.loads(metadata))
        bucket = gc.get_bucket()
        blob = bucket.blob(f"{uuid.uuid4()}_{file.filename}")
        blob.upload_from_file(
            file.file, 
            content_type=file.content_type,
            timeout=30)
        record=await save_metadata(metadata_obj.email, blob.name, db)
    except Exception as e:
        raise ValueError(f"Error uploading file: {e}")
    return record