import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Supporter API")

# CORS configuration - frontend'in backend'e erişebilmesi için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment configuration
APP_ENV = os.getenv("APP_ENV", "local")


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "env": APP_ENV,
        "service": "supporter-backend"
    }
