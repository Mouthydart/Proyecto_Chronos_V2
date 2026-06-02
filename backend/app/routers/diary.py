from fastapi import APIRouter, HTTPException, Body
from backend.services.ai_service import generate_motivational_phrase
from backend.app.database.mongodb import mongodb
from datetime import datetime

router = APIRouter()

@router.post("/save-entry")
async def save_diary(payload: dict = Body(...)):
    # Extraemos el texto del body
    text_content = payload.get("content")
    if not text_content:
        raise HTTPException(status_code=400, detail="El contenido no puede estar vacío")

    # genera la frase
    phrase = await generate_motivational_phrase(text_content)
    
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = {
        "content": text_content,
        "ai_phrase": phrase,
        "date_str": today,
        "updated_at": datetime.now()
    }
    
    # guardar la frase
    collection = mongodb.get_collection("diary")
    
    collection.update_one(
        {"date_str": today},
        {"$set": new_entry},
        upsert=True
    )
    
    return {"message": "Diario actualizado", "ai_phrase": phrase}

@router.get("/get-entry/{date}")
async def get_diary_by_date(date: str):
    # date debe ser YYYY-MM-DD
    collection = mongodb.get_collection("diary")
    entry = collection.find_one({"date_str": date})
    
    if not entry:
        return {"content": "", "ai_phrase": "No hay registros para este día."}
    
    return {
        "content": entry["content"],
        "ai_phrase": entry["ai_phrase"]
    }