from pydantic import BaseModel, Field
from datetime import date, time

class LiquidacionBase(BaseModel):
    tanque: str = Field(..., description="Tipo de tanque")
    altura_inicial: int = Field(..., description="Altura inicial del tanque")
    altura_final: int = Field(..., description="Altura final del tanque")
    volumen_bruto: float = Field(..., description="Volumen bruto")
    volumen_neto: float = Field(..., description="Volumen neto")
    api_observado: float
    api_corregido: float
    factor_correccion: float
    temperatura: float
    fecha_finalizacion: str
    hora_finalizacion: str    
    fecha_liberacion: str
    hora_liberacion: str
   


class LiquidacionCreate(LiquidacionBase):
    pass

class LiquidacionResponse(LiquidacionBase):
    id: int
    

    class Config:
        from_attributes = True  # Pydantic v2