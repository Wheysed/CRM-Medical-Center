from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    status: str = "scheduled"

class AppointmentCreate(AppointmentBase):
    class Config:
        json_schema_extra = {
            "example": {
                "patient_id": 1,
                "doctor_id": 1,
                "appointment_date": "2026-03-25",
                "appointment_time": "10:30:00",
                "status": "scheduled"
            }
        }

class AppointmentUpdate(BaseModel):
    status: Optional[str] = None
    appointment_date: Optional[date] = None
    appointment_time: Optional[time] = None

    class Config:
        json_schema_extra = {
            "example": {
                "status": "completed"
            }
        }

class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attributes = True
