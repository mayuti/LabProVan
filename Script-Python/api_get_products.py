import requests
import json
import os

java_api_url = "http://host.docker.internal:8080/api/products"

output_dir = "/app/data-py"
os.makedirs(output_dir, exist_ok=True)  # crea el directorio si no existe

output_path = os.path.join(output_dir, "GetAllProduct.json")

try:
    response = requests.get(java_api_url)
    response.raise_for_status()
    products = response.json()

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    print(f"✅ Archivo JSON generado correctamente en {output_path}")

except requests.exceptions.RequestException as e:
    print(f"❌ Error al obtener los productos: {e}")
