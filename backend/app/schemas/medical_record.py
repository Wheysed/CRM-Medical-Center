from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicalRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    record_date: date
    diagnosis: str
    prescription: Optional[str] = None
    notes: Optional[str] = None
    attachments: Optional[str] = None

class MedicalRecordCreate(MedicalRecordBase):
    class Config:
        json_schema_extra = {
            "example": {
                "patient_id": 1,
                "doctor_id": 1,
                "record_date": "2026-03-20",
                "diagnosis": "Острый бронхит",
                "prescription": "Амоксициллин 500мг 3 раза в день",
                "notes": "Постельный режим",
                "attachments": ""
            }
        }

class MedicalRecordUpdate(BaseModel):
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    record_date: Optional[date] = None
    diagnosis: Optional[str] = None
    prescription: Optional[str] = None
    notes: Optional[str] = None
    attachments: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "diagnosis": "Уточнённый диагноз: бронхит",
                "prescription": "Амоксициллин 500мг 3 раза в день, мукалтин"
            }
        }

class MedicalRecordResponse(MedicalRecordBase):
    id: int

    class Config:
        from_attributes = True
