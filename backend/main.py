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

# Modifica esta línea en tu main.py
app = FastAPI(title="Chronos API", version="1.0.0", lifespan=lifespan, redirect_slashes=False)

# Configurar CORS de forma segura
origins = [
    "http://localhost:5173",          # Tu Vue.js en local (PC)
    "http://127.0.0.1:5173",          # Alternativa local
    "https://chronos-copy-v2.vercel.app", # <-- ¡Tu URL real de Vercel!
    "https://chronos-copy-v2.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # <-- Cambiamos el ["*"] por la lista explícita
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
