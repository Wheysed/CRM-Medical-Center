from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    blood_type = Column(String(5))
    allergies = Column(Text)
    insurance_policy = Column(String(50), unique=True)

    # Связи
    user = relationship("User", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")
    medical_records = relationship("MedicalRecord", back_populates="patient")

    def __repr__(self):
        return f"<Patient(id={self.id}, user_id={self.user_id})>"
