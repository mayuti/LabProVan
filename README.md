
# 📦 LabProVan - Plataforma de Gestión de Stock

> Trabajo Práctico Final – Programación de Vanguardia 2025

---

## 🧾 Carátula

**Materia:** Programación de Vanguardia  
**Año:** 2025  
**Trabajo:** Proyecto Integrador - Gestión de Stock con Predicción  
**Carrera:** Licenciatura en Tecnologías Digitales  
**Universidad:** Universidad de la Ciudad de Buenos Aires

**Integrantes del equipo:**
- Francisco Carracedo
- Cristian Mayuti
- Carlos Vizcaino
- Florencia Murano
- Marcos Castillo

---

## 🎯 Descripción del Proyecto

**LabProVan** es una plataforma modular diseñada para gestionar productos en stock, visualizar historiales de inventario y aplicar modelos de predicción de consumo.

Incluye:

- Backend en **Python (Flask)** que expone endpoints RESTful.
- Extracción de datos desde una base **H2 embebida** en una aplicación Java.
- Microservicios Python para el cálculo de predicciones con regresión lineal.
- Visualización de datos históricos y predicción en gráficos generados automáticamente.
- Interfaz web HTML + CSS desplegada en contenedor Docker.
- Uso de **submódulo Git** para incorporar el backend Java de gestión de stock desarrollado por otro integrante.

---

## 🗂️ Estructura del Proyecto

```
LabProVan/
├── stock/                ← Submódulo Git con backend Java de stock
├── app/
│   ├── data-py/          ← Archivos de entrada y salida (.json, .csv, gráficos)
│   ├── predict.py        ← Script de predicción con regresión lineal
│   └── ...
├── webserver/
│   └── index.html        ← Frontend visual del proyecto
├── Dockerfile            ← Imagen web del sistema
├── .gitmodules           ← Configuración del submódulo 'stock'
└── README.md             ← Este archivo
```

---

## 🚀 Ejecución

### Clonación del repositorio (con submódulo incluido):

```bash
git clone --recurse-submodules https://github.com/mayuti/LabProVan.git
cd LabProVan
```

Si ya clonaste el repositorio:

```bash
git submodule update --init --recursive
```

### Ejecución del backend:

- Asegurate de tener la base de datos H2 corriendo desde el proyecto Java (`stock/`).
- Ejecutá el microservicio Flask para acceder a los datos y procesar la predicción.
- Visualizá el resultado en la interfaz web servida con Docker (contenedor `webserver`).

---

## 🧪 Pruebas y Validación

- Se realizaron pruebas con Postman sobre endpoints `/api/product` y `/api/predict`.
- Se documentaron casos de prueba y bugs encontrados en archivos separados.
- La carpeta `data-py/` contiene las evidencias de resultados.

---

## 📈 Herramientas y Tecnologías

- Python 3.x, Flask, Pandas, Matplotlib
- Java con H2 Database
- Postman
- Git + Git Submodules
- Docker
- HTML, CSS
- Visual Studio Code

---

## 📌 Observaciones Finales

Este proyecto permite validar una arquitectura distribuida compuesta por distintas tecnologías y lenguajes. La integración entre servicios y la separación por módulos demuestra escalabilidad, mantenibilidad y reutilización de componentes.

---
