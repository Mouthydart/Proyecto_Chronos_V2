from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from backend.app.database.mongodb import mongodb
from backend.app.routers import auth, academy, health, finance, leisure, diary

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    mongodb.connect()
    yield
    # Shutdown
    mongodb.disconnect()

app = FastAPI(title="Chronos API", version="1.0.0", lifespan=lifespan)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporal: permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(academy.router, prefix="/api", tags=["academy"])
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(finance.router, prefix="/api", tags=["finance"])
app.include_router(leisure.router, prefix="/api", tags=["leisure"])
app.include_router(diary.router, prefix="/api", tags=["diary"])

@app.get("/")
async def root():
    return {"message": "Chronos API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
