#endpoints para \models\academy.py 

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import List
from backend.app.models.academy import AcademyCreate, AcademyResponse, AcademyUpdate
from bson import ObjectId
from backend.app.database.mongodb import mongodb
from backend.app.routers.auth import get_current_user

router = APIRouter()

@router.post("/academy", response_model=AcademyResponse)
async def create_academy(academy: AcademyCreate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    academy_collection = db.academy
    
    academy_dict = academy.dict()
    academy_dict["user_id"] = str(current_user["_id"])
    academy_dict["created_at"] = datetime.utcnow()
    academy_dict["updated_at"] = datetime.utcnow()
    
    result = academy_collection.insert_one(academy_dict)
    academy_dict["id"] = str(result.inserted_id)
    
    return AcademyResponse(**academy_dict)

@router.get("/academy", response_model=List[AcademyResponse])
async def get_academy_records(current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    academy_collection = db.academy
    
    try:
        records = academy_collection.find({"user_id": str(current_user["_id"])})
        result = []
        for record in records:
            # Construir manualmente el diccionario para evitar problemas
            academy_data = {
                "id": str(record["_id"]),
                "title": record.get("title", ""),
                "description": record.get("description", ""),
                "subject": record.get("subject", ""),
                "priority": record.get("priority", "media").lower(),
                "due_date": record.get("due_date"),
                "status": record.get("status", "pendiente"),
                "user_id": record.get("user_id", ""),
                "created_at": record.get("created_at"),
                "updated_at": record.get("updated_at")
            }
            result.append(AcademyResponse(**academy_data))
        return result
    except Exception as e:
        print(f"Error en get_academy_records: {e}")
        print(f"Record: {record}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/academy/{record_id}", response_model=AcademyResponse)
async def get_academy_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    academy_collection = db.academy
    
    try:
        record = academy_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    return AcademyResponse(**record, id=str(record["_id"]))

@router.put("/academy/{record_id}", response_model=AcademyResponse)
async def update_academy_record(record_id: str, academy_update: AcademyUpdate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    academy_collection = db.academy
    
    try:
        record = academy_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    update_data = academy_update.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    academy_collection.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": update_data}
    )
    
    updated_record = academy_collection.find_one({"_id": ObjectId(record_id)})
    return AcademyResponse(**updated_record, id=str(updated_record["_id"]))

@router.delete("/academy/{record_id}")
async def delete_academy_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    academy_collection = db.academy
    
    try:
        record = academy_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    academy_collection.delete_one({"_id": ObjectId(record_id)})
    return {"message": "Record deleted successfully"}
