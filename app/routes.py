# app/routes.py

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from .utilities.file_processor import process_file
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def init_app(app):
    @app.route('/')
    def hello():
        return "Hello World!"


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.txt'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        try:
            code = process_file(filepath)
            return jsonify({'message': 'Success', 'code': code}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 400
    else:
        return jsonify({'message': 'Invalid file format'}), 400
