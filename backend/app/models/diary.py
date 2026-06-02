from pydantic import BaseModel, Field
from datetime import datetime

class DiaryEntry(BaseModel):
    content: str  # Lo que el usuario escribe
    ai_phrase: str  # La frase que genera la IA
    date_str: str  # Guardaremos "YYYY-MM-DD" para buscarlo fácil desde el calendario
    created_at: datetime = Field(default_factory=datetime.utcnow)