# models/api_correccion.py

from sqlalchemy import Column, Integer, Float, UniqueConstraint
from database import Base

class ApiCorreccion(Base):
    __tablename__ = "api_correcciones"

    id = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Float, nullable=False)
    api_observado = Column(Float, nullable=False)
    api_corregido = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint("temperatura", "api_observado"),
    )
