from pydantic import BaseModel

class Content(BaseModel):
    serial_number: str
    sku_id: str
    variant_type: str
    sku_name: str
    price: int
    qty: int
    store_location: str
    
class FileAddress(BaseModel):
    file_address: str