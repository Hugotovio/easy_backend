from railway_db import Base
from sqlalchemy import Column, Integer, String, Float
class Aforo(Base):
    __tablename__ = "aforos"

    id = Column(Integer, primary_key=True)
    tanque = Column(String(10), index=True)
    altura = Column(Integer, index=True)
    volumen = Column(Float)
