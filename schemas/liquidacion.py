from pydantic import BaseModel

class LiquidacionRequest(BaseModel):
    tanque: str
    altura_inicial: int
    volumen_contador: float
    temperatura: float
    api_observado: float
    fecha_finalizacion: str
    hora_finalizacion: str
