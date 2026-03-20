from locust import HttpUser, task, between
import random

class MedicalCenterUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Выполняется при старте каждого пользователя"""
        # Можно добавить авторизацию, если нужно
        pass
    
    @task(3)
    def get_patients(self):
        """GET /api/patients/ - список пациентов"""
        self.client.get("/api/patients/")
    
    @task(3)
    def get_services(self):
        """GET /api/services/ - список услуг"""
        self.client.get("/api/services/")
    
    @task(3)
    def get_appointments(self):
        """GET /api/appointments/ - список записей"""
        self.client.get("/api/appointments/")
    
    @task(2)
    def get_doctors(self):
        """GET /api/doctors/ - список врачей"""
        self.client.get("/api/doctors/")
    
    @task(1)
    def get_medical_records(self):
        """GET /api/medical-records/ - список медзаписей"""
        self.client.get("/api/medical-records/")
    
    @task(1)
    def create_appointment(self):
        """POST /api/appointments/ - создание записи"""
        # Используем существующие ID (1-5)
        patient_id = random.randint(1, 5)
        doctor_id = random.randint(1, 3)
        self.client.post("/api/appointments/", json={
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "appointment_date": "2026-03-28",
            "appointment_time": "14:00:00",
            "status": "scheduled"
        })
    
    @task(1)
    def update_appointment(self):
        """PATCH /api/appointments/{id} - обновление статуса"""
        appointment_id = random.randint(1, 10)
        self.client.patch(f"/api/appointments/{appointment_id}", json={
            "status": "completed"
        })
