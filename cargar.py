import pandas as pd
from database import SessionLocal
from models.factor_correccion import FactorCorreccion

def cargar_factor():

    db = SessionLocal()

    try:
        # Leer hoja CTL usando fila 4 como encabezado
        df = pd.read_excel(
            "TABLA_API.xlsx",
            sheet_name="CTL",
            engine="openpyxl",
            header=4
        )

        # Renombrar primera columna
        df.rename(columns={df.columns[0]: "temperatura"}, inplace=True)

        # Eliminar filas sin temperatura
        df = df.dropna(subset=["temperatura"])

        # Convertir matriz a formato largo
        df_long = df.melt(
            id_vars="temperatura",
            var_name="api_corregido",
            value_name="factor"
        )

        # Convertir a numérico
        df_long["temperatura"] = pd.to_numeric(df_long["temperatura"], errors="coerce")
        df_long["api_corregido"] = pd.to_numeric(df_long["api_corregido"], errors="coerce")
        df_long["factor"] = pd.to_numeric(df_long["factor"], errors="coerce")

        # Eliminar filas inválidas
        df_long = df_long.dropna()

        registros = []

        for _, row in df_long.iterrows():
            registro = FactorCorreccion(
                temperatura=float(row["temperatura"]),
                api_corregido=float(row["api_corregido"]),
                factor=round(float(row["factor"]) / 10000, 4)  # división + 4 decimales
            )
            registros.append(registro)

        db.bulk_save_objects(registros)
        db.commit()

        print(f"✅ {len(registros)} registros insertados en factor_correccion.")

    except Exception as e:
        db.rollback()
        print("❌ Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    cargar_factor()
