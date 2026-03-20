from pydantic import BaseModel
from typing import Optional

class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    duration_minutes: int

class ServiceCreate(ServiceBase):
    class Config:
        json_schema_extra = {
            "example": {
                "name": "УЗИ брюшной полости",
                "description": "Ультразвуковое исследование органов брюшной полости",
                "price": 2500.00,
                "duration_minutes": 30
            }
        }

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    duration_minutes: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "price": 2700.00,
                "duration_minutes": 40
            }
        }

class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True
