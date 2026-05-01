#endpoints para modulo financiero

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import List
from app.models.finance import FinanceCreate, FinanceResponse, FinanceUpdate
from bson import ObjectId
from app.database.mongodb import mongodb
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/finance", response_model=FinanceResponse)
async def create_finance(finance: FinanceCreate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    finance_collection = db.finance
    
    finance_dict = finance.dict()
    finance_dict["user_id"] = str(current_user["_id"])
    finance_dict["created_at"] = datetime.utcnow()
    finance_dict["updated_at"] = datetime.utcnow()
    
    result = finance_collection.insert_one(finance_dict)
    finance_dict["id"] = str(result.inserted_id)
    
    return FinanceResponse(**finance_dict)

@router.get("/finance", response_model=List[FinanceResponse])
async def get_finance_records(current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    finance_collection = db.finance
    
    records = finance_collection.find({"user_id": str(current_user["_id"])})
    return [FinanceResponse(**record, id=str(record["_id"])) for record in records]

@router.get("/finance/{record_id}", response_model=FinanceResponse)
async def get_finance_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    finance_collection = db.finance
    
    try:
        record = finance_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    return FinanceResponse(**record, id=str(record["_id"]))

@router.put("/finance/{record_id}", response_model=FinanceResponse)
async def update_finance_record(record_id: str, finance_update: FinanceUpdate, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    finance_collection = db.finance
    
    try:
        record = finance_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    update_data = finance_update.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    finance_collection.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": update_data}
    )
    
    updated_record = finance_collection.find_one({"_id": ObjectId(record_id)})
    return FinanceResponse(**updated_record, id=str(updated_record["_id"]))

@router.delete("/finance/{record_id}")
async def delete_finance_record(record_id: str, current_user: dict = Depends(get_current_user)):
    db = mongodb.get_database()
    finance_collection = db.finance
    
    try:
        record = finance_collection.find_one({
            "_id": ObjectId(record_id),
            "user_id": str(current_user["_id"])
        })
    except:
        raise HTTPException(status_code=400, detail="Invalid record ID")
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    finance_collection.delete_one({"_id": ObjectId(record_id)})
    return {"message": "Record deleted successfully"}
