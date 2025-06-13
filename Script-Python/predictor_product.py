import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import os

input_path = "/app/data-py/GetAllProduct.json"

def procesar_producto(producto):
    nombre = producto.get("productName", "Desconocido")
    movimientos = producto.get("inventoryMovements", [])

    historico = []
    predicciones = []

    if len(movimientos) < 2:
        fechas = [datetime.today() - timedelta(days=i) for i in range(5, 0, -1)]
        current_stock = producto.get("currentStock")
        cantidad_stock = current_stock.get("quantity", 0) if current_stock and isinstance(current_stock, dict) else 0
        cantidades = [cantidad_stock] * 5
    else:
        fechas = []
        cantidades = []
        stock_acumulado = 0
        for mov in sorted(movimientos, key=lambda x: x["date"]):
            fecha = datetime.fromisoformat(mov["date"].split("T")[0])
            cantidad = mov["quantity"]
            tipo = mov.get("movementType", "")
            stock_acumulado += cantidad if tipo == "INBOUND" else -cantidad
            fechas.append(fecha)
            cantidades.append(stock_acumulado)
        for f, s in zip(fechas, cantidades):
            historico.append({
                "productName": nombre,
                "fecha": f.strftime("%Y-%m-%d"),
                "stock_historico": s
            })

    df = pd.DataFrame({
        "fecha": fechas,
        "cantidad": cantidades
    }).sort_values("fecha")

    df["dias"] = np.arange(len(df)).reshape(-1)
    modelo = LinearRegression()
    modelo.fit(df[["dias"]], df["cantidad"])
    futuros_dias = pd.DataFrame({"dias": np.arange(len(df), len(df)+5)})
    pred = modelo.predict(futuros_dias)
    fechas_pred = [df["fecha"].max() + timedelta(days=i+1) for i in range(5)]

    for fecha, valor in zip(fechas_pred, pred):
        predicciones.append({
            "productName": nombre,
            "fecha": fecha.strftime("%Y-%m-%d"),
            "prediccion_stock": valor
        })

    return historico, predicciones

# Cargar datos y procesar
with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

historico_totales = []
predicciones_totales = []

for producto in data:
    hist, pred = procesar_producto(producto)
    historico_totales.extend(hist)
    predicciones_totales.extend(pred)

# Guardar CSVs
pd.DataFrame(predicciones_totales).to_csv("/app/data-py/tablePredictStock.csv", index=False)
pd.DataFrame(historico_totales).to_csv("/app/data-py/tableStockHistorico.csv", index=False)
