#estructura de datos para modulo financiero

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class FinanceBase(BaseModel):
    title: str
    description: str
    type: str = Field(..., pattern="^(ingreso|gasto|ahorro|inversion)$")
    amount: float
    category: str = Field(..., pattern="^(salario|comida|transporte|entretenimiento|facturas|otros)$")
    priority: str = Field(..., pattern="^(alta|media|baja)$")
    due_date: Optional[datetime] = None
    status: str = Field(default="pendiente", pattern="^(pendiente|en_progreso|completada)$")

class FinanceCreate(FinanceBase):
    user_id: str

class FinanceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None

class FinanceResponse(FinanceBase):
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
