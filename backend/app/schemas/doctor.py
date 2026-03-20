from pydantic import BaseModel
from typing import Optional

class DoctorBase(BaseModel):
    user_id: int
    specialty: str
    room_number: Optional[str] = None
    license_number: str

class DoctorCreate(DoctorBase):
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 2,
                "specialty": "Терапевт",
                "room_number": "101",
                "license_number": "LIC12345"
            }
        }

class DoctorUpdate(BaseModel):
    user_id: Optional[int] = None
    specialty: Optional[str] = None
    room_number: Optional[str] = None
    license_number: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "specialty": "Кардиолог",
                "room_number": "202"
            }
        }

class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True
