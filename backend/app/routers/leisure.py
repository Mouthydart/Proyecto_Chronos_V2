#endpoints para modulo de ocio

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import List
from app.models.leisure import LeisureCreate, LeisureResponse, LeisureUpdate
from bson import ObjectId
from app.database.mongodb import mongodb
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/leisure", response_model=LeisureResponse)
async def create_leisure(leisure: LeisureCreate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    leisure_collection = db.leisure
    
    leisure_dict = leisure.dict()
    leisure_dict["user_id"] = str(current_user["_id"])
    leisure_dict["created_at"] = datetime.utcnow()
    leisure_dict["updated_at"] = datetime.utcnow()
    
    result = leisure_collection.insert_one(leisure_dict)
    leisure_dict["id"] = str(result.inserted_id)
    
    return LeisureResponse(**leisure_dict)

@router.get("/leisure", response_model=List[LeisureResponse])
async def get_leisure_records(current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    leisure_collection = db.leisure
    
    records = leisure_collection.find({"user_id": str(current_user["_id"])})
    return [LeisureResponse(**record, id=str(record["_id"])) for record in records]

@router.get("/leisure/{record_id}", response_model=LeisureResponse)
async def get_leisure_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    leisure_collection = db.leisure
    
    try:
        record = leisure_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    return LeisureResponse(**record, id=str(record["_id"]))

@router.put("/leisure/{record_id}", response_model=LeisureResponse)
async def update_leisure_record(record_id: str, leisure_update: LeisureUpdate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    leisure_collection = db.leisure
    
    try:
        record = leisure_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    update_data = leisure_update.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    leisure_collection.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": update_data}
    )
    
    updated_record = leisure_collection.find_one({"_id": ObjectId(record_id)})
    return LeisureResponse(**updated_record, id=str(updated_record["_id"]))

@router.delete("/leisure/{record_id}")
async def delete_leisure_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    leisure_collection = db.leisure
    
    try:
        record = leisure_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    leisure_collection.delete_one({"_id": ObjectId(record_id)})
    return {"message": "Record deleted successfully"}
