from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from railway_db import get_db

from schemas.liquidacion import LiquidacionCreate, LiquidacionResponse
from crud.liquidacion import create_liquidacion

router = APIRouter()

@router.post("/liquidacion/", response_model=LiquidacionResponse)
def crear_liquidacion(
    liquidacion: LiquidacionCreate,
    db: Session = Depends(get_db)
):
    return create_liquidacion(db=db, liquidacion=liquidacion)

