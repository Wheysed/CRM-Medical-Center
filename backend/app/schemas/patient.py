from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBase(BaseModel):
    user_id: int
    birth_date: date
    gender: str
    blood_type: Optional[str] = None
    allergies: Optional[str] = None
    insurance_policy: str

class PatientCreate(PatientBase):
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "birth_date": "1990-05-15",
                "gender": "male",
                "blood_type": "A+",
                "allergies": "Нет",
                "insurance_policy": "POL123456"
            }
        }

class PatientUpdate(BaseModel):
    user_id: Optional[int] = None
    birth_date: Optional[date] = None
    gender: Optional[str] = None
    blood_type: Optional[str] = None
    allergies: Optional[str] = None
    insurance_policy: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 2,
                "gender": "female",
                "blood_type": "B-",
                "allergies": "Пенициллин",
                "insurance_policy": "POL789012"
            }
        }

class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True
