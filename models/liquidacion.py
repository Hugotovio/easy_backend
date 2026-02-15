from sqlalchemy import Column, Date, Integer, Float, String, Time
from database import Base

class Liquidacion(Base):
    __tablename__ = "viajes"

    id = Column(Integer, primary_key=True, index=True)
    tanque = Column(String(50))
    altura_inicial = Column(Integer)
    altura_final = Column(Integer)
    volumen_bruto = Column(Float)
    volumen_neto = Column(Float)
    api_observado = Column(Float)
    api_corregido = Column(Float)
    factor_correccion = Column(Float)
    temperatura = Column(Float)
    fecha_finalizacion = Column(String(10))
    hora_finalizacion = Column(String(8))
    fecha_liberacion = Column(String(10))
    hora_liberacion = Column(String(8))

   
    