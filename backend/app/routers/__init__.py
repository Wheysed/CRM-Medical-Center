from .patients import router as patients_router
from .services import router as services_router
from .appointments import router as appointments_router
from .doctors import router as doctors_router
from .medical_records import router as medical_records_router

__all__ = [
    "patients_router",
    "services_router",
    "appointments_router",
    "doctors_router",
    "medical_records_router"
]
