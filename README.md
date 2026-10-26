# 🚀 AutoReporte - Automatización de Reportes con Python e IA

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

> **Convierte un Excel desordenado en un reporte profesional con análisis de Inteligencia Artificial en segundos.**

AutoReporte es una aplicación web diseñada para **PYMES y contadores** que pierden horas semanales limpiando datos y armando reportes manualmente. Sube tu archivo desordenado y obtén un Excel con formato profesional, gráficos, resúmenes y un **análisis de negocio generado por IA**.

## 🌐 Demo en Vivo
Puedes probar la aplicación funcionando en la nube aquí: 
👉 **[https://autoreporte-5.onrender.com](https://autoreporte-5.onrender.com)**
*(Nota: Al estar en el plan gratuito de Render, si el enlace tarda en abrir, es porque el servidor está iniciando. Espera unos segundos y refresca).*

## ✨ Características Principales
- 🤖 **Análisis con Inteligencia Artificial:** Integración con modelos de lenguaje (LLMs) para generar recomendaciones automáticas basadas en los datos.
- 📤 **Subida sencilla:** Arrastra y suelta archivos .xlsx, .xls o .csv.
- 🧹 **Limpieza automática:** Elimina duplicados, filas vacías y espacios en blanco.
- 📊 **Generación de reportes:** Crea un Excel profesional con 3 hojas (Resumen, Datos limpios, Gráfico).
- 📈 **Gráficos automáticos:** Genera gráficos de barras basados en los datos numéricos.
- 📥 **Descarga inmediata:** Obtén tu archivo procesado en segundos.

## 🛠️ Tecnologías Utilizadas
*   **Backend:** Python 3, Flask, Gunicorn.
*   **Procesamiento de Datos:** Pandas, OpenPyXL.
*   **Inteligencia Artificial:** Integración con API de Pollinations AI (LLM).
*   **Frontend:** HTML5, CSS3, JavaScript (Vanilla).
*   **Despliegue:** Render (Cloud Hosting) y GitHub.
*   **Desarrollo:** 100% programado y desplegado desde un dispositivo Android usando **Termux**.

## ⚙️ Cómo funciona el flujo
1. El cliente sube su archivo Excel/CSV mediante la interfaz web.
2. Flask recibe el archivo y lo pasa a Pandas para su limpieza.
3. OpenPyXL genera un nuevo archivo Excel con estilos, colores y gráficos.
4. Se envía un resumen de los datos al LLM para generar un análisis escrito.
5. El servidor devuelve el reporte y el análisis al cliente.

## 🚀 Instalación y Ejecución Local
Si deseas clonar este proyecto y correrlo en tu propia máquina:

1. Clona el repositorio:
   git clone https://github.com/CruzCd/autoreporte-.git
   cd autoreporte-
   
2. Crea un entorno virtual e instala dependencias:
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
3. Ejecuta la aplicación:
   python app.py
   
4. Abre tu navegador en http://127.0.0.1:5000

---
*Desarrollado con pasión por [CruzCd](https://github.com/CruzCd). ¿Necesitas automatizar los reportes de tu negocio? ¡Contáctame!*
