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

## API /upload

## Endpoint: Subida de Archivos

### POST /upload

Este endpoint permite a los usuarios subir archivos de texto que contienen secuencias de tres caracteres numéricos. Cada línea del archivo debe contener exactamente tres caracteres numéricos. El sistema procesará estas secuencias para deducir un código secreto basado en un criterio de ordenamiento topológico.

#### Parámetros:

- **file** (multipart/form-data): El archivo `.txt` que se desea subir. Debe estar codificado como `multipart/form-data`.

#### Respuestas:

##### 200 OK
- **Descripción**: La solicitud fue exitosa y el código secreto ha sido deducido correctamente.
- **Cuerpo**:
  ```json
  {
    "message": "Éxito",
    "code": "Código Secreto Deduced"
  }

Nota: "Código Secreto Deduced" será reemplazado por el código real deducido del archivo proporcionado.



Documentación del Endpoint /upload
markdown
Copy code
## Endpoint: Subida de Archivos

### POST /upload

Este endpoint permite a los usuarios subir archivos de texto que contienen secuencias de tres caracteres numéricos. Cada línea del archivo debe contener exactamente tres caracteres numéricos. El sistema procesará estas secuencias para deducir un código secreto basado en un criterio de ordenamiento topológico.

#### Parámetros:

- **file** (multipart/form-data): El archivo `.txt` que se desea subir. Debe estar codificado como `multipart/form-data`.

#### Respuestas:

##### 200 OK
- **Descripción**: La solicitud fue exitosa y el código secreto ha sido deducido correctamente.
- **Cuerpo**:
  ```json
  {
    "message": "Éxito",
    "code": "Código Secreto Deduced"
  }
  ```
Nota: "Código Secreto Deduced" será reemplazado por el código real deducido del archivo proporcionado.

### 400 Bad Request
Descripción: El archivo subido no cumple con el formato esperado o no contiene únicamente caracteres numéricos en secuencias de tres.
```json
{
  "message": "Contenido del archivo inválido, cada línea debe tener exactamente 3 caracteres numéricos"
}
```
### 500 Internal Server Error
Descripción: Hubo un error al intentar guardar o procesar el archivo.
Cuerpo:
```json
{
  "message": "Error interno del servidor. Por favor, intente de nuevo más tarde."
}
```

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
