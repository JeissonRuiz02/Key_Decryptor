# app/utilities/file_processor.py

def validate_file_contents(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    # Verificar que cada línea tenga exactamente tres caracteres
    for line in lines:
        if len(line.strip()) != 3:
            return False  # Si alguna línea no tiene exactamente tres caracteres, retorna False
    
    return True  # Si todas las líneas son válidas, retorna True
