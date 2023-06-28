# -*- coding: utf-8 -*-
import os
import unicodedata

#pesos=input("¿Cual es la cantidad de pesos que quieres convertir?")

#pesos =float(pesos)
#valor_dolar=25
#dolares=pesos + valor_dolar
#dolares=round(dolares,2)
#dolares=str(dolares)
#print("Tienes: $" + dolares + "dolares")


def limpiar_nombre(nombre):
    # Eliminar acentos y diacríticos
    nombre_limpio = unicodedata.normalize('NFKD', nombre).encode('ASCII', 'ignore').decode('utf-8')
    # Eliminar puntos y comas
    nombre_limpio = nombre_limpio.replace('"', '').replace(',', '')
    nombre_limpio = nombre_limpio.replace(')', '').replace(',', '')
    nombre_limpio = nombre_limpio.replace('(', '').replace(',', '')
    nombre_limpio = nombre_limpio.replace(',', '').replace(',', '')
    nombre_limpio = nombre_limpio.replace('.', '').replace(',', '')
    nombre_limpio = nombre_limpio.replace('_', '').replace(',', '')
    return nombre_limpio

# Ruta de la carpeta que deseas renombrar
ruta_carpeta = '/Users/albertopintor/Downloads/correctos/CambioProceso'

# Obtener la lista de archivos y carpetas en la ruta especificada
archivos = os.listdir(ruta_carpeta)

for archivo in archivos:
    # Ruta completa del archivo o carpeta
    ruta_archivo = os.path.join(ruta_carpeta, archivo)
    
    # Nuevo nombre sin caracteres no deseados
    nuevo_nombre = limpiar_nombre(archivo)
    
    # Renombrar el archivo o carpeta
    os.rename(ruta_archivo, os.path.join(ruta_carpeta, nuevo_nombre))
