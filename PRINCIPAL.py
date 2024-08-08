
import pandas as pd
import requests
import os 
import openpyxl
import json  
from Modulos import Estadisticas,local,swapi
from Reportes_numericos import GRAFICAS
from pathlib import Path
directorio_usuario = Path.home()
def borrar_datos(tipo, nombre):
    directorio_actual = os.path.dirname(__file__)
    ruta_excel = os.path.join(directorio_actual, "Reportes_numericos")
    
    

    ruta_excel_archivo = os.path.join(ruta_excel, f"{tipo}.xlsx")

    if os.path.exists(ruta_excel_archivo):
        df = pd.read_excel(ruta_excel_archivo)
        df = df[df['name'] != nombre]
        df.to_excel(ruta_excel_archivo, index=False)
        print(f"Los datos de {nombre} han sido eliminados del archivo {tipo}.xlsx.")
    else:
        print(f"No se encontró el archivo {tipo}.xlsx.")

# Este es el menu principal
while True:
    print("\nMENU:")
    print("1- CONSULTA WEB")
    print("2- CONSULTA LOCAL")
    print("3- ESTADISTICAS")
    print("4- GRAFICAS")
    print("5- BORRAR DATOS")
    print("6- SALIR")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        swapi.obtener_info_star_wars()  
    elif opcion == "2":
        print("\nARCHIVOS DISPONIBLES:")
        print("1. Personajes")
        print("2. Naves")
        print("3. Películas")
        print("4. Planetas")
        opcion_archivo = input("Selecciona una opción (1/2/3/4): ")
        #ruta_excel = "C:/Users/Elias/Desktop/SWAPI_STATS/Reportes_numericos"
        ruta_excel =directorio_usuario/"OneDrive"/"Desktop"/"SWAPI_STATS"/"Reportes_numericos"
        columnas_deseadas = None
        if opcion_archivo == "1":
            tipo = "personajes"
            columnas_deseadas = ["name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year", "gender"]
        elif opcion_archivo == "2":
            tipo = "naves"
            columnas_deseadas = ["name", "model", "manufacturer", "cost_in_credits", "length", "max_atmosphering_speed", "crew", "passengers", "cargo_capacity", "consumables", "hyperdrive_rating", "MGLT"]
        elif opcion_archivo == "3":
            tipo = "peliculas"
            columnas_deseadas = ["title", "episode_id", "opening_crawl", "director", "producer", "release_date"]
        elif opcion_archivo == "4":
            tipo = "planetas"
            columnas_deseadas = ["name", "rotation_period", "orbital_period", "diameter", "climate", "gravity", "terrain", "surface_water", "population"]
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
            continue
        
        ruta_excel_archivo = os.path.join(ruta_excel, f"{tipo}.xlsx")
        if os.path.exists(ruta_excel_archivo):
            df = pd.read_excel(ruta_excel_archivo)
            print(f"\nInformación de {tipo}:")
            print(df[columnas_deseadas])
        else:
            print(f"No se encontró el archivo {tipo}.xlsx.")
    elif opcion == "3":
        
        Estadisticas.estadisticas("Reportes_numericos/personajes.xlsx")
    elif opcion == "4":
        
        
        
        GRAFICAS.generar_graficas()
        
    elif opcion == "5":
        print("\nBORRAR DATOS:")
        print("1. Personajes")
        print("2. Naves")
        print("3. Películas")
        print("4. Planetas")
        opcion_borrar = input("Selecciona una opción (1/2/3/4): ")
        nombre_borrar = input("Introduce el nombre del registro que deseas borrar: ")

        if opcion_borrar == "1":
            tipo_borrar = "personajes"
        elif opcion_borrar == "2":
            tipo_borrar = "naves"
        elif opcion_borrar == "3":
            tipo_borrar = "peliculas"
        elif opcion_borrar == "4":
            tipo_borrar = "planetas"
        else:
            print("Opción no válida.")
            continue

        borrar_datos(tipo_borrar, nombre_borrar)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
