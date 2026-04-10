from sqlalchemy import Column, Integer, String, Float, DateTime
from railway_db import Base

class CierreTurno(Base):
    __tablename__ = "cierre_turno"

    id = Column(Integer, primary_key=True, index=True)
    medida_tk10 = Column(Float)
    medida_tk08 = Column(Float)
    medida_tk09 = Column(Float)
    volumen_tk08 = Column(Float)
    volumen_tk09 = Column(Float)
    volumen_tk10 = Column(Float)
    totalizado_recibo = Column(Integer)
    totalizador_despacho = Column(Integer)
    fecha_cierre = Column(DateTime)