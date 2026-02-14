from pydantic import BaseModel, Field
from datetime import datetime

class LiquidacionBase(BaseModel):
    tanque: str = Field(..., description="Tipo de tanque")
    altura_inicial: int = Field(..., description="Altura inicial del tanque")
    altura_final: int = Field(..., description="Altura final del tanque")
    volumen_bruto: float = Field(..., description="Volumen bruto")
    volumen_neto: float = Field(..., description="Volumen neto")
    api_observado: float
    api_corregido: float
    temperatura: float
    

class LiquidacionCreate(LiquidacionBase):
    pass

class LiquidacionResponse(LiquidacionBase):
    id: int

    class Config:
        from_attributes = True