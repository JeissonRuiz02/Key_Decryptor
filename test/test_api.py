from flask_testing import TestCase
from werkzeug.datastructures import FileStorage

from app import create_app
from io import BytesIO
import os

class TestAPIRoutes(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['UPLOAD_FOLDER'] = 'temp_uploads'
        return app

    def setUp(self):
        if not os.path.exists(self.app.config['UPLOAD_FOLDER']):
            os.makedirs(self.app.config['UPLOAD_FOLDER'])

    def tearDown(self):
        for filename in os.listdir(self.app.config['UPLOAD_FOLDER']):
            os.remove(os.path.join(self.app.config['UPLOAD_FOLDER'], filename))
        os.rmdir(self.app.config['UPLOAD_FOLDER'])

    def test_upload_endpoint_valid_file(self):
        data = {'file': (BytesIO(b'123\n456\n789'), 'valid.txt')}
        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Éxito', response.json['message'])

    def test_upload_endpoint_invalid_file(self):
        data = {'file': (BytesIO(b'abc'), 'invalid.txt')}
        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Contenido del archivo inválido, cada línea debe tener exactamente 3 caracteres numéricos', response.json['message'])
