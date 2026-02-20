from pydantic import BaseModel, EmailStr

class Metadata(BaseModel):
    email: EmailStr

    