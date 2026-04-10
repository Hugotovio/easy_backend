from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from railway_db import SessionLocal
from schemas.liquidacion import LiquidacionRequest
from service.liquidaciones_service import liquidar

router = APIRouter(prefix="/liquidacion", tags=["Liquidacion"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def procesar_liquidacion(
    datos: LiquidacionRequest,
    db: Session = Depends(get_db)
):
    return liquidar(db, datos)
