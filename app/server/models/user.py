from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class userSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    Address: str = Field(...)
    

    class Config:
        schema_extra = {
            "example": {
                "fullname": "sandeep",
                "email": "vinay.kireeti@gmail.com",
                "Address": "Pakala",
                
            }
        }

class UpdateuserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    Address: Optional[str]
    

    class Config:
        schema_extra = {
            "example": {
                "fullname": "vinay",
                "email": "sandy@gmail.com",
                "Address": "Bangalore",
                
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
