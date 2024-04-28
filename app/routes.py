from flask import request, jsonify
from werkzeug.utils import secure_filename
from .utilities.file_processor import process_file, validate_file_contents
import os
import logging

def init_app(app):
    # Configurar el nivel básico de logging
    logging.basicConfig(level=logging.INFO)

    @app.route('/')
    def hello():
        # Una ruta de prueba simple que devuelve un saludo
        return "Hello World!"

    @app.route('/upload', methods=['POST'])
    def upload_file():
        # Obtener el archivo del formulario subido
        file = request.files.get('file')
        
        # Validar que el archivo existe y tiene el formato correcto
        if file and file.filename.endswith('.txt'):
            # Asegurar que el nombre del archivo es seguro
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            try:
                # Intentar guardar el archivo
                file.save(filepath)
            except Exception as e:
                # Loguear el error si falla la operación de guardado
                logging.error(f"Error al guardar el archivo: {e}")
                return jsonify({'message': 'Error al guardar el archivo'}), 500

            # Validar el contenido del archivo antes de procesarlo
            if not validate_file_contents(filepath):
                # Eliminar el archivo si el contenido no es válido
                os.remove(filepath)
                logging.info("Contenido inválido detectado y archivo eliminado")
                return jsonify({'message': 'Contenido del archivo inválido, cada línea debe tener exactamente 3 caracteres numéricos'}), 400

            try:
                # Procesar el archivo para deducir el código secreto
                code = process_file(filepath)
                return jsonify({'message': 'Éxito', 'code': code}), 200
            except Exception as e:
                # Loguear el error si falla el procesamiento
                logging.error(f"Error al procesar el archivo: {e}")
                return jsonify({'message': str(e)}), 500
        else:
            # Devolver un error si el formato del archivo no es correcto
            return jsonify({'message': 'Formato de archivo inválido, solo se aceptan archivos .txt'}), 400
