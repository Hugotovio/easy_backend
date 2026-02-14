from fastapi import FastAPI
from routers import liquidacion
 
app = FastAPI()
app.include_router(liquidacion.router, prefix="/api/v1", tags=["liquidacion"])