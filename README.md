# Key_Decryptor
 
# Key Decryptor API

Key Decryptor es una API de Flask diseñada para deducir el código secreto más corto posible a partir de tríos de caracteres suministrados en un archivo `.txt`. Este proyecto es ideal para demostrar cómo procesar archivos de texto y realizar cálculos complejos, como el ordenamiento topológico, en un entorno de backend.

## Comenzando

Estas instrucciones te proporcionarán una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Prerrequisitos

Antes de instalar, asegúrate de tener Python y pip instalados en tu sistema. Este proyecto está testeado con Python 3.8+.

### Instalación

Sigue estos pasos para configurar el entorno de desarrollo local:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JeissonRuiz02/Key-Decryptor.git
   cd key-decryptor
   
2. Instala las dependencias necesarias:
```bash
 pip install -r requirements.txt
```
3. Inicia la aplicación:
 ```bash
python run.py
 ```
# Uso
Para usar la API, sube un archivo .txt que contenga tríos de caracteres numéricos, cada trío en una línea nueva.

##Subir un archivo
Puedes subir un archivo utilizando cURL de la siguiente manera:
```bash
curl --location 'http://127.0.0.1:5000/upload' \
--form 'file=@"postman-cloud:///1ef03fe8-d0d7-42a0-b5c7-91755aaeb4c7"'
```
La API te retornará el código secreto deducido o un mensaje de error si el archivo no cumple con el formato esperado.

# Desarrollo
## Ejecutar pruebas
Para ejecutar las pruebas automatizadas para este sistema:
```bash
pytest
```
## Autores
Jeisson Daniel Ruiz Lizarazo - jeissonruizdev@gmail.com

# Licencia
 Este proyecto está licenciado bajo la Licencia MIT - ve el archivo LICENSE para más detalles.
