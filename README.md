

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
├── stock/                  ← Submódulo Git con backend Java de stock
├── Script-Python/          ← Scripts en Python refactorizados
│   ├── graph_predict_stock.py   ← Generación del gráfico de predicción
│   └── predictor_product.py     ← Predicción de stock por producto
├── data-py/                ← Archivos de entrada/salida (.json, .csv, gráficos)
│   └── .gitkeep            ← Archivo vacío para mantener la carpeta en Git
├── webserver/
│   └── index.html          ← Interfaz web visual del proyecto
├── .gitignore              ← Exclusiones de archivos del repositorio
├── .gitmodules             ← Configuración del submódulo 'stock'
└── README.md               ← Este archivo
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

- **Arquitectura**
  - Cliente-Servidor basada en HTTP y RESTful API
  - Formato de datos: JSON

- **Lenguajes y Frameworks**
  - Python 3.x (Flask, Pandas, Matplotlib)
  - Java (JDK 1.8+), JDBC, uso de objetos, clases y colecciones (Collections)
  - Bash scripting
  - HTML, CSS

- **Bases de Datos**
  - H2 Database (Java embebida)
  - Conexión mediante JDBC
  - SQL básico (SELECT, INSERT, UPDATE, etc.)

- **Control de versiones**
  - Git y GitHub
  - Submódulos de Git
  - Archivo `.gitignore` personalizado

- **Contenedores y despliegue**
  - Docker
  - Servidor web simple con contenedor

- **Testing y desarrollo**
  - JUnit para pruebas unitarias (Java)
  - Soporte de pruebas automatizadas con Maven
  - Postman para pruebas de API REST
  - IDEs: Visual Studio Code / IntelliJ IDEA

- **Gestión de proyectos**
  - Maven (para estructura y dependencias en proyectos Java)

- **Buenas prácticas aplicadas**
  - PEP8 (estilo Python)
  - Nombres significativos y comentarios claros
  - Uso de convenciones de nombres para test y scripts

---

## 📌 Observaciones Finales

Este proyecto permite validar una arquitectura distribuida compuesta por distintas tecnologías y lenguajes. La integración entre servicios y la separación por módulos demuestra escalabilidad, mantenibilidad y reutilización de componentes.

---

## 🆕 Mejoras Recientes

### 🔁 Versión actual: v1.1 – Junio 2025

- Refactorización del código en:
  - `graph_predict_stock.py`: separación en funciones para modularizar y reutilizar el código.
  - `predictor_product.py`: restructuración funcional para facilitar mantenimiento y pruebas.
- Incorporación del archivo `.gitignore` para excluir archivos temporales, logs, datos generados, carpetas de entorno virtual y configuraciones locales.
- Añadido `.gitkeep` para mantener la estructura vacía de `data-py/` sin incluir sus contenidos.

> Estas mejoras permiten una mayor claridad del código, control de versiones más limpio y mayor facilidad de colaboración.



