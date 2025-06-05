from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/graph')
def graph():
    image_path = '/app/data-py/graphPredictStock.png'
    print(f"Buscando imagen en: {image_path}")
    exists = os.path.exists(image_path)
    print(f"Existe? {exists}")
    if exists:
        return send_file(image_path, mimetype='image/png')
    else:
        return "Imagen no disponible", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
