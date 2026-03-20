from .patient import PatientCreate, PatientUpdate, PatientResponse
from .service import ServiceCreate, ServiceUpdate, ServiceResponse
from .appointment import AppointmentCreate, AppointmentUpdate, AppointmentResponse
from .doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from .medical_record import MedicalRecordCreate, MedicalRecordUpdate, MedicalRecordResponse

__all__ = [
    "PatientCreate", "PatientUpdate", "PatientResponse",
    "ServiceCreate", "ServiceUpdate", "ServiceResponse",
    "AppointmentCreate", "AppointmentUpdate", "AppointmentResponse",
    "DoctorCreate", "DoctorUpdate", "DoctorResponse",
    "MedicalRecordCreate", "MedicalRecordUpdate", "MedicalRecordResponse"
]
