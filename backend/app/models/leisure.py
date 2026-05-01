#estructura de datos para modulo de ocio

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class LeisureBase(BaseModel):
    title: str
    description: str
    category: str = Field(..., pattern="^(deportes|lectura|videojuegos|social|viajes|otros)$")
    priority: str = Field(..., pattern="^(alta|media|baja)$")
    due_date: Optional[datetime] = None
    status: str = Field(default="pendiente", pattern="^(pendiente|en_progreso|completada)$")

class LeisureCreate(LeisureBase):
    user_id: str

class LeisureUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None

class LeisureResponse(LeisureBase):
    id: Optional[str] = None
    user_id: str
    created_at: datetime
    updated_at: datetime

    @field_validator('id', mode='before')
    @classmethod
    def validate_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v
