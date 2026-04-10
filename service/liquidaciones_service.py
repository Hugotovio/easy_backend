from sqlalchemy.orm import Session
from models.liquidacion import Liquidacion
from models.factor_correccion import FactorCorreccion
from models.api_correccion import ApiCorreccion
from datetime import datetime, timedelta
import pytz
from sqlalchemy import and_

# 🔥 Redondeo a múltiplos de 0.5
def redondear_05(valor):
    return round(valor * 2) / 2


def liquidar(db: Session, datos):

    # =========================
    # 1️⃣ ALTURA FINAL
    # =========================
    altura_final = datos.altura_inicial + datos.volumen_contador

    # =========================
    # 2️⃣ REDONDEOS CORRECTOS
    # =========================
    temp_tabla = redondear_05(datos.temperatura)
    api_obs_tabla = redondear_05(datos.api_observado)

    print(f"T ajustada: {temp_tabla}")
    print(f"API observado ajustado: {api_obs_tabla}")

    # =========================
    # 3️⃣ BUSCAR API CORREGIDO
    # =========================
    registro_api = db.query(ApiCorreccion).filter(
        and_(
            ApiCorreccion.temperatura == temp_tabla,
            ApiCorreccion.api_observado == api_obs_tabla
        )
    ).first()

    if not registro_api:
        raise Exception(
            f"No se encontró API corregido para T={temp_tabla} y API={api_obs_tabla}"
        )

    api_corregido_tabla = redondear_05(registro_api.api_corregido)

    print(f"API corregido ajustado: {api_corregido_tabla}")

    # =========================
    # 4️⃣ BUSCAR FACTOR
    # =========================
    factor = db.query(FactorCorreccion).filter(
        and_(
            FactorCorreccion.temperatura == temp_tabla,
            FactorCorreccion.api_corregido == api_corregido_tabla
        )
    ).first()

    if not factor:
        raise Exception(
            f"No se encontró factor para T={temp_tabla} y APIc={api_corregido_tabla}"
        )

    factor_valor = factor.factor

    # =========================
    # 5️⃣ CÁLCULO DE VOLUMEN
    # =========================
    volumen_bruto = round(datos.volumen_contador, 2)
    volumen_neto = round(volumen_bruto * factor_valor, 2)

    # =========================
    # 6️⃣ FORMATO VISUAL
    # =========================
    api_observado_visual = round(datos.api_observado, 1)
    api_corregido_visual = round(api_corregido_tabla, 1)

    # =========================
    # 7️⃣ FECHA LIBERACIÓN
    # =========================
    zona_horaria = pytz.timezone("America/Bogota")

    fecha_hora_str = f"{datos.fecha_finalizacion} {datos.hora_finalizacion}"
    tiempo_actual = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
    tiempo_actual = zona_horaria.localize(tiempo_actual)

    horas_para_liberar = (altura_final / 1000) * 3
    if horas_para_liberar >= 24:
        horas_para_liberar = 24

    hora_liberacion_dt = tiempo_actual + timedelta(hours=horas_para_liberar)
    hora_liberacion_dt = zona_horaria.normalize(hora_liberacion_dt)

    fecha_liberacion = hora_liberacion_dt.strftime("%Y-%m-%d")
    hora_liberacion = hora_liberacion_dt.strftime("%H:%M:%S")

    # =========================
    # 8️⃣ GUARDAR EN BASE
    # =========================
    nueva_liquidacion = Liquidacion(
        tanque=datos.tanque,
        altura_inicial=datos.altura_inicial,
        altura_final=altura_final,
        volumen_bruto=volumen_bruto,
        volumen_neto=volumen_neto,
        api_observado=api_observado_visual,
        api_corregido=api_corregido_visual,
        factor_correccion=factor_valor,
        temperatura=temp_tabla,
        fecha_finalizacion=datos.fecha_finalizacion,
        hora_finalizacion=datos.hora_finalizacion,
        fecha_liberacion=fecha_liberacion,
        hora_liberacion=hora_liberacion
    )

    db.add(nueva_liquidacion)
    db.commit()
    db.refresh(nueva_liquidacion)

    # =========================
    # 9️⃣ RESPUESTA
    # =========================
    return {
        "tanque": datos.tanque,
        "volumen_bruto": volumen_bruto,
        "volumen_neto": volumen_neto,
        "api_observado": api_observado_visual,
        "api_corregido": api_corregido_visual,
        "factor": factor_valor,
        "fecha_liberacion": fecha_liberacion,
        "hora_liberacion": hora_liberacion
    }