# app.py
import os
from datetime import datetime
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from procesador import procesar_archivo

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB maximo

ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'csv'}

# 1. Calculamos la dirección exacta de la carpeta del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_REPORTES = os.path.join(BASE_DIR, 'reportes')

def permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if 'archivo' not in request.files:
        return jsonify({'error': 'No se envio ningun archivo'}), 400

    archivo = request.files['archivo']
    
    if archivo.filename == '':
        return jsonify({'error': 'Nombre de archivo vacio'}), 400

    if not permitido(archivo.filename):
        return jsonify({'error': 'Solo se permiten archivos .xlsx, .xls o .csv'}), 400

    try:
        nombre_seguro = secure_filename(archivo.filename)
        reporte, resumen = procesar_archivo(archivo.stream, nombre_seguro)

        nombre_reporte = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        
        # 2. Usamos la ruta absoluta para crear la carpeta y guardar el archivo
        os.makedirs(CARPETA_REPORTES, exist_ok=True)
        
        ruta = os.path.join(CARPETA_REPORTES, nombre_reporte)
        with open(ruta, 'wb') as f:
            f.write(reporte.read())

        return jsonify({
            'ok': True,
            'reporte': nombre_reporte,
            'resumen': resumen
        })
        
    except Exception as e:
        return jsonify({'error': f'Error procesando el archivo: {str(e)}'}), 500

@app.route('/descargar/<nombre>')
def descargar(nombre):
    # 3. Usamos la ruta absoluta también para buscar el archivo al descargar
    ruta = os.path.join(CARPETA_REPORTES, secure_filename(nombre))
    if not os.path.exists(ruta):
        return "Archivo no encontrado", 404
    return send_file(ruta, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)