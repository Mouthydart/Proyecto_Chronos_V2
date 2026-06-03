
#Autenticacion (registrar, login, obtener usuario actual)

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from backend.app.models.user import UserCreate, UserLogin, UserResponse
from backend.app.database.mongodb import mongodb
from backend.app.auth.auth import (
    get_password_hash, 
    verify_password, 
    create_access_token, 
    verify_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()
security = HTTPBearer()

#@router.post("/register", response_model=UserResponse)
#async def register(user: UserCreate):
@router.post("/register")
async def register(user_data: dict): # <-- Cambiamos temporalmente a dict para que no de 404
    print("--- DATOS RECIBIDOS DESDE EL FRONTEND ---")
    print(user_data)
    print("-----------------------------------------")
    db = mongodb.get_database()
    users_collection = db.users
    
    # Verificar si el usuario ya existe
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Crear nuevo usuario
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict.pop("password")
    user_dict["hashed_password"] = hashed_password
    user_dict["created_at"] = datetime.utcnow()
    user_dict["is_active"] = True
    
    result = users_collection.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    
    return UserResponse(**user_dict)

@router.post("/login")
async def login(user_credentials: UserLogin):
    db = mongodb.get_database()
    users_collection = db.users
    
    # Buscar usuario
    user = users_collection.find_one({"email": user_credentials.email})
    if not user or not verify_password(user_credentials.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Crear token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    email = verify_token(token)
    
    db = mongodb.get_database()
    users_collection = db.users
    
    user = users_collection.find_one({"email": email})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    return UserResponse(**current_user, id=str(current_user["_id"]))

@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: dict,
    current_user: dict = Depends(get_current_user)
):
    db = mongodb.get_database()
    users_collection = db.users
    
    # Actualizar campos permitidos
    update_data = {}
    allowed_fields = ["full_name", "username", "birth_date", "location", "profile_picture"]
    
    for field in allowed_fields:
        if field in user_update:
            update_data[field] = user_update[field]
    
    # Si hay cambio de contraseña
    if "current_password" in user_update and "new_password" in user_update:
        if verify_password(user_update["current_password"], current_user["hashed_password"]):
            update_data["hashed_password"] = get_password_hash(user_update["new_password"])
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is incorrect"
            )
    
    update_data["updated_at"] = datetime.utcnow()
    
    # Actualizar en la base de datos
    result = users_collection.update_one(
        {"_id": current_user["_id"]},
        {"$set": update_data}
    )
    
    if result.modified_count == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No changes made"
        )
    
    # Obtener usuario actualizado
    updated_user = users_collection.find_one({"_id": current_user["_id"]})
    return UserResponse(**updated_user, id=str(updated_user["_id"]))
