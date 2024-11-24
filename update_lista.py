import os
import json

def buscar_imagenes(ruta):
    extensiones_imagen = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    lista_imagenes = []

    for raiz, dirs, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.lower().endswith(extensiones_imagen):
                ruta_completa = os.path.join(raiz, archivo)
                lista_imagenes.append(ruta_completa[len(config['input_path']):])

    return lista_imagenes

try:
    with open("config.json", 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"El archivo de configuración config.json no se encontró.")
except json.JSONDecodeError as e:
    print(f"Error al decodificar el archivo JSON: {e}")

imagenes_encontradas = buscar_imagenes(config['input_path'])

with open(config['output_path'] + '/lista.txt', 'w') as f:
    for imagen in imagenes_encontradas:
        f.write(f"{imagen}\n")

print(f"Se han encontrado {len(imagenes_encontradas)} imágenes. La lista se ha guardado en lista.txt")