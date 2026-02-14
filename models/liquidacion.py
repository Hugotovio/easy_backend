from sqlalchemy import Column, Integer, Float, DateTime, String
from database import Base
from datetime import datetime

class Liquidacion(Base):
    __tablename__ = "viajes"

    id = Column(Integer, primary_key=True, index=True)
    tanque=Column(String(50))
    altura_inicial = Column(Integer)
    altura_final = Column(Integer)
    volumen_bruto = Column(Float)
    volumen_neto = Column(Float)
    api_observado = Column(Float)
    api_corregido = Column(Float)
    temperatura = Column(Float)
   