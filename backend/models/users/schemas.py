from pydantic import BaseModel

class UserSchema(BaseModel):
    whatsapp_number: str
    profile_name: str

    class Config:
        from_attributes = True