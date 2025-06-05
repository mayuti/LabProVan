import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import os

input_path = "/app/data-py/GetAllProduct.json"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Listas para predicción y stock histórico
predicciones_totales = []
historico_totales = []

for producto in data:
    nombre = producto.get("productName", "Desconocido")
    movimientos = producto.get("inventoryMovements", [])
    
    if len(movimientos) < 2:
        fechas = [datetime.today() - timedelta(days=i) for i in range(5, 0, -1)]
        current_stock = producto.get("currentStock")
        if current_stock and isinstance(current_stock, dict):
            cantidad_stock = current_stock.get("quantity", 0)
        else:
            cantidad_stock = 0
        cantidades = [cantidad_stock] * 5
    else:
        fechas = []
        cantidades = []
        stock_acumulado = 0
        for mov in sorted(movimientos, key=lambda x: x["date"]):
            fecha = datetime.fromisoformat(mov["date"].split("T")[0])
            cantidad = mov["quantity"]
            tipo = mov.get("movementType", "")
            if tipo == "INBOUND":
                stock_acumulado += cantidad
            elif tipo == "OUTBOUND":
                stock_acumulado -= cantidad
            fechas.append(fecha)
            cantidades.append(stock_acumulado)  # acumulado

        # Guardar datos históricos por producto
        for f, s in zip(fechas, cantidades):
            historico_totales.append({
                "productName": nombre,
                "fecha": f.strftime("%Y-%m-%d"),
                "stock_historico": s
            })
    
    # Convertimos a DataFrame
    df = pd.DataFrame({
        "fecha": fechas,
        "cantidad": cantidades
    }).sort_values("fecha")

    # Creamos una variable de tiempo numérica
    df["dias"] = np.arange(len(df)).reshape(-1)

    # Modelo de regresión lineal
    X = df[["dias"]]
    y = df["cantidad"]

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Predecir próximos 5 días
    futuros_dias = pd.DataFrame({"dias": np.arange(len(df), len(df)+5)})
    pred = modelo.predict(futuros_dias)
    fechas_pred = [df["fecha"].max() + timedelta(days=i+1) for i in range(5)]

    for fecha, valor in zip(fechas_pred, pred):
        predicciones_totales.append({
            "productName": nombre,
            "fecha": fecha.strftime("%Y-%m-%d"),
            "prediccion_stock": valor
        })

# Guardar CSVs
df_pred = pd.DataFrame(predicciones_totales)
df_pred.to_csv("/app/data-py/tablePredictStock.csv", index=False)

df_hist = pd.DataFrame(historico_totales)
df_hist.to_csv("/app/data-py/tableStockHistorico.csv", index=False)
