FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt .
COPY api_get_products.py .
COPY predictor_product.py .
COPY graph_predict_stock.py .

# Instalar librerías
RUN pip install --no-cache-dir -r requirements.txt

# Mantener contenedor abierto con bash interactivo
CMD ["/bin/bash"]
