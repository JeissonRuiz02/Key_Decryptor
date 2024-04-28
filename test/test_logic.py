import unittest
from app.utilities.file_processor import validate_file_contents, process_file
from unittest.mock import patch

class TestFileProcessingLogic(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='123\n456\n789')
    def test_validate_file_contents_valid(self, mock_file):
        # Simular la lectura de un archivo con contenido válido
        filepath = 'dummy_path.txt'  # La ruta exacta no importa porque estamos simulando la apertura del archivo
        result = validate_file_contents(filepath)
        self.assertTrue(result)
        mock_file.assert_called_once_with(filepath, 'r')  # Verificar que se intentó abrir el archivo

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='abc\ndef\nghi')
    def test_validate_file_contents_invalid(self, mock_file):
        # Simular la lectura de un archivo con contenido inválido
        filepath = 'dummy_path.txt'
        result = validate_file_contents(filepath)
        self.assertFalse(result)
        mock_file.assert_called_once_with(filepath, 'r')  # Verificar que se intentó abrir el archivo
