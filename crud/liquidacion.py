from sqlalchemy.orm import Session
from models.liquidacion import Liquidacion


def create_liquidacion(db: Session, liquidacion):
    nueva_liquidacion = Liquidacion(
        tanque=liquidacion.tanque,
        altura_inicial=liquidacion.altura_inicial,
        altura_final=liquidacion.altura_final,
        volumen_bruto=liquidacion.volumen_bruto,
        volumen_neto=liquidacion.volumen_neto,
        api_observado=liquidacion.api_observado,
        api_corregido=liquidacion.api_corregido,
        factor_correccion=liquidacion.factor_correccion,
        temperatura=liquidacion.temperatura,
        fecha_finalizacion=liquidacion.fecha_finalizacion,
        hora_finalizacion=liquidacion.hora_finalizacion,
        fecha_liberacion=liquidacion.fecha_liberacion,
        hora_liberacion=liquidacion.hora_liberacion,
    )

    db.add(nueva_liquidacion)
    db.commit()
    db.refresh(nueva_liquidacion)

    return nueva_liquidacion