from fastapi import FastAPI
from routers import liquidacion
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://beneficial-courtesy-desarrollo.up.railway.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(liquidacion.router, prefix="/api/v1")