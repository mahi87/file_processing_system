import base64
import json
import os

from dotenv import load_dotenv
from google.cloud import storage
from google.oauth2 import service_account

load_dotenv()

def get_bucket():
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    sa_base64=os.getenv("GCP_SA_JSON_BASE64")
    
    sa_json = json.loads(base64.b64decode(sa_base64))
    
    credentials = service_account.Credentials.from_service_account_info(sa_json)
    
    storage_client = storage.Client(credentials=credentials)
    return storage_client.bucket(bucket_name=bucket_name)
    
    