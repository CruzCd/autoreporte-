from flask import Flask, render_template, request, send_file, jsonify
from procesador import procesar_archivo, generar_analisis_llm
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED = {'xlsx', 'xls', 'csv'}

def permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if 'archivo' not in request.files:
        return jsonify({'error': 'No se envió ningún archivo'}), 400
    archivo = request.files['archivo']
    if archivo.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400
    if not permitido(archivo.filename):
        return jsonify({'error': 'Solo se permiten .xlsx, .xls o .csv'}), 400

    try:
        nombre_seguro = secure_filename(archivo.filename)
        reporte, resumen = procesar_archivo(archivo.stream, nombre_seguro)
        analisis_ia = generar_analisis_llm(resumen)

        nombre_reporte = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        os.makedirs('reportes', exist_ok=True)
        ruta = os.path.join('reportes', nombre_reporte)
        with open(ruta, 'wb') as f:
            f.write(reporte.read())

        return jsonify({
            'ok': True,
            'reporte': nombre_reporte,
            'resumen': resumen,
            'analisis': analisis_ia
        })
    except Exception as e:
        return jsonify({'error': f'Error procesando: {str(e)}'}), 500

@app.route('/descargar/<nombre>')
def descargar(nombre):
    ruta = os.path.join('reportes', secure_filename(nombre))
    if not os.path.exists(ruta):
        return "No encontrado", 404
    return send_file(ruta, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
