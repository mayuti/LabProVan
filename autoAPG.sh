#!/bin/bash

echo "🔄 Paso 1: Ejecutando api_get_products.py"
echo "📥 Función: Consulta la API Java y guarda los productos en GetAllProduct.json"
sleep 3
python /app/Script-Python/api_get_products.py
echo ""

echo "🔄 Paso 2: Ejecutando predictor_product.py"
echo "📈 Función: Toma el JSON y genera predicción de stock guardando tablePredictStock.csv"
sleep 3
python /app/Script-Python/predictor_product.py
echo ""

echo "🔄 Paso 3: Ejecutando graph_predict_stock.py"
echo "📊 Función: Toma las predicciones y genera el gráfico en graphPredictStock.png"
sleep 3
PRODUCT_NAME="Notebook Lenovo" python /app/Script-Python/graph_predict_stock.py
echo ""

echo "✅ Proceso completo. Archivos generados:"
echo "📄 GetAllProduct.json"
echo "📄 tablePredictStock.csv"
echo "🖼️  graphPredictStock.png"
