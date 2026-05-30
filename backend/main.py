from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database.mongodb import mongodb
from app.routers import auth, academy, health, finance, leisure

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    mongodb.connect()
    yield
    # Shutdown
    mongodb.disconnect()

app = FastAPI(title="Chronos API", version="1.0.0", lifespan=lifespan)

# Configurar CORS - debe estar antes de los routers
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8001",
    "http://127.0.0.1:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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

@app.get("/")
async def root():
    return {"message": "Chronos API is running", "cors": "enabled"}

@app.options("/api/auth/register")
async def options_register():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
