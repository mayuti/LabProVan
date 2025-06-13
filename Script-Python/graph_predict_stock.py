import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from io import BytesIO
import subprocess

# Rutas
csv_pred = "/app/data-py/tablePredictStock.csv"
csv_hist = "/app/data-py/tableStockHistorico.csv"
img_local = "graphPredictStock.png"
img_final = "/app/data-py/graphPredictStock.png"

def generar_grafico_stock(df_pred, df_hist, product_name, img_local, img_final):
    df_p = df_pred[df_pred["productName"] == product_name]
    df_h = df_hist[df_hist["productName"] == product_name]

    if df_p.empty or df_h.empty:
        raise ValueError(f"❌ No se encontraron datos suficientes para el producto: '{product_name}'")

    df_p["fecha"] = pd.to_datetime(df_p["fecha"])
    df_h["fecha"] = pd.to_datetime(df_h["fecha"])

    plt.figure(figsize=(9, 5))
    plt.plot(df_h["fecha"], df_h["stock_historico"], marker='o', linestyle='--', label="Stock histórico", color="orange")
    plt.plot(df_p["fecha"], df_p["prediccion_stock"], marker='o', linestyle='-', label="Predicción", color="blue")
    plt.title(f"Stock - Histórico y Predicción: {product_name}")
    plt.xlabel("Fecha")
    plt.ylabel("Stock")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    print(f"🖼️ Guardando imagen local: {img_local}")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()

    with open(img_local, "wb") as f:
        f.write(buf.getvalue())

    print(f"📂 Moviendo imagen a: {img_final}")
    subprocess.run(["mv", img_local, img_final])


# Leer datos
df_pred = pd.read_csv(csv_pred)
df_hist = pd.read_csv(csv_hist)

# Obtener producto
product_name = os.getenv("PRODUCT_NAME")
if not product_name:
    if df_pred.empty:
        raise ValueError("❌ El archivo de predicciones está vacío.")
    product_name = df_pred["productName"].unique()[0]
    print(f"⚠️ PRODUCT_NAME no definido. Usando automáticamente: '{product_name}'")
else:
    print(f"📌 Producto definido por variable de entorno: '{product_name}'")

# Generar gráfico
generar_grafico_stock(df_pred, df_hist, product_name, img_local, img_final)
