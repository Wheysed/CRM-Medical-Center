from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    record_date = Column(Date, nullable=False)
    diagnosis = Column(String(500), nullable=False)
    prescription = Column(Text)
    notes = Column(Text)
    attachments = Column(String(500))  # путь к файлу или ссылка

    # Связи
    patient = relationship("Patient", back_populates="medical_records")
    doctor = relationship("Doctor", back_populates="medical_records")

    def __repr__(self):
        return f"<MedicalRecord(id={self.id}, diagnosis='{self.diagnosis[:30]}...')>"
