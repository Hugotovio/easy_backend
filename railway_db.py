from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.getenv("ENV", "DEV")

if ENV == "PROD":
    DATABASE_URL = os.getenv("DATABASE_URL_PROD")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_DEV")

# 🔴 Validación
if not DATABASE_URL:
    raise ValueError("❌ No se encontró la URL de la base de datos")

print(f"✅ Conectando a base de datos en modo: {ENV}")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()