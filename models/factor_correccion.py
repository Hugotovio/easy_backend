from sqlalchemy import Column, Integer, Float, UniqueConstraint
from railway_db import Base

class FactorCorreccion(Base):
    __tablename__ = "factor_correccion"

    id = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Float, nullable=False)
    api_corregido = Column(Float, nullable=False)
    factor = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint("temperatura", "api_corregido", name="unique_temp_api"),
    )
