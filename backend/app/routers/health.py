#endpoints para modulo de salud

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import List
from app.models.health import HealthCreate, HealthResponse, HealthUpdate
from bson import ObjectId
from app.database.mongodb import mongodb
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/health", response_model=HealthResponse)
async def create_health(health: HealthCreate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    health_collection = db.health
    
    health_dict = health.dict()
    health_dict["user_id"] = str(current_user["_id"])
    health_dict["created_at"] = datetime.utcnow()
    health_dict["updated_at"] = datetime.utcnow()
    
    result = health_collection.insert_one(health_dict)
    health_dict["id"] = str(result.inserted_id)
    
    return HealthResponse(**health_dict)

@router.get("/health", response_model=List[HealthResponse])
async def get_health_records(current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    health_collection = db.health
    
    records = health_collection.find({"user_id": str(current_user["_id"])})
    return [HealthResponse(**record, id=str(record["_id"])) for record in records]

@router.get("/health/{record_id}", response_model=HealthResponse)
async def get_health_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    health_collection = db.health
    
    try:
        record = health_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    return HealthResponse(**record, id=str(record["_id"]))

@router.put("/health/{record_id}", response_model=HealthResponse)
async def update_health_record(record_id: str, health_update: HealthUpdate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    health_collection = db.health
    
    try:
        record = health_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    update_data = health_update.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    health_collection.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": update_data}
    )
    
    updated_record = health_collection.find_one({"_id": ObjectId(record_id)})
    return HealthResponse(**updated_record, id=str(updated_record["_id"]))

@router.delete("/health/{record_id}")
async def delete_health_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    health_collection = db.health
    
    try:
        record = health_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    health_collection.delete_one({"_id": ObjectId(record_id)})
    return {"message": "Record deleted successfully"}
