from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from app.routers import (
    patients_router,
    services_router,
    appointments_router,
    doctors_router,
    medical_records_router
)

app = FastAPI(
    title="CRM Medical Diagnostic Center API",
    description="RESTful API для CRM-системы медицинского диагностического центра",
    version="1.0.0"
)

app.include_router(patients_router)
app.include_router(services_router)
app.include_router(appointments_router)
app.include_router(doctors_router)
app.include_router(medical_records_router)

frontend_path = os.path.join(os.path.dirname(__file__), "../../frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
