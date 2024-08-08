import os
import requests
import json
import pandas as pd
from pathlib import Path
directorio_usuario = Path.home()
URL_BASE = "https://swapi.py4e.com/api"

def obtener_info(url):
    resultado = requests.get(url)
    if resultado.status_code == 200:
        return resultado.json()
    else:
        return None

def guardar_diccionario(diccionario, archivo):
    if diccionario:
        # Verificar si el diccionario ya existe en el archivo
        if not existe_en_archivo(diccionario, archivo):
            with open(archivo, 'a') as file:
                json.dump(diccionario, file)
                file.write('\n')
        else:
            print("Ya existe este registro.")

def existe_en_archivo(diccionario, archivo):
    try:
        with open(archivo, 'r') as file:
            for line in file:
                if json.loads(line) == diccionario:
                    return True
        return False
    except FileNotFoundError:
        return False

def json_to_excel(json_file, excel_file):
    # Cargar el archivo JSON en un DataFrame de pandas
    df = pd.read_json(json_file, lines=True)
    
    # Escribir el DataFrame en un archivo Excel
    excel_path = os.path.join("Reportes_numericos", excel_file)
    df.to_excel(excel_path, index=False)

def mostrar_info_personaje(id_personaje, personajes, archivo_json, archivo_excel):
    url = f"{URL_BASE}/people/{id_personaje}/"
    info_personaje = obtener_info(url)
    if info_personaje:
        print("Información del personaje:")
        print("Nombre:", info_personaje["name"])
        print("Altura:", info_personaje["height"])
        print("Peso:", info_personaje["mass"])
        print("Color de pelo:", info_personaje["hair_color"])
        print("Color de piel:", info_personaje["skin_color"])
        print("Color de ojos:", info_personaje["eye_color"])
        print("Género:", info_personaje["gender"])
        json_path = os.path.join("reportes_consulta", archivo_json)
        guardar_diccionario(info_personaje, json_path)
        json_to_excel(json_path, archivo_excel)
    else:
        print("No se pudo obtener información del personaje.")

def mostrar_info_pelicula(id_pelicula, peliculas, archivo_json, archivo_excel):
    url = f"{URL_BASE}/films/{id_pelicula}/"
    info_pelicula = obtener_info(url)
    if info_pelicula:
        print("DATOS DE LA PELICULA ")
        print("TITULO:", info_pelicula["title"])
        print("EPISODIO : ", info_pelicula["episode_id"])
        print("OPENING : ", info_pelicula["opening_crawl"])
        print("DIRECTOR : ", info_pelicula["director"])
        print("PRODUCTOS: ", info_pelicula["producer"])
        print("Personajes : ", info_pelicula["characters"])
        print("PLANETAS : ", info_pelicula["planets"])
        print("NAVES : ", info_pelicula["starships"])
        print("VEHICULOS : ", info_pelicula["vehicles"])
        print("Especies : ", info_pelicula["species"])
        json_path = os.path.join("reportes_consulta", archivo_json)
        guardar_diccionario(info_pelicula, json_path)
        json_to_excel(json_path, archivo_excel)
    else:
        print("No se pudo obtener información de la película.")

def mostrar_info_nave(id_nave, naves, archivo_json, archivo_excel):
    url = f"{URL_BASE}/starships/{id_nave}/"
    info_nave = obtener_info(url)
    if info_nave:
        print("DATOS DE LA NAVE")
        print("MGLT ", info_nave["MGLT"])
        print("Capacidad de carga : ", info_nave["cargo_capacity"])
        print("consumables : ", info_nave["consumables"])
        print("costo en creditos : ", info_nave["cost_in_credits"])
        print("creada : ", info_nave["created"])
        print("crew : ", info_nave["crew"])
        print("edited : ", info_nave["edited"])
        print("hyperdrive_rating : ", info_nave["hyperdrive_rating"])
        print("lenght", info_nave["length"])
        print("Manuacturada : ", info_nave["manufacturer"])
        print("maxima velocidad : ", info_nave["max_atmosphering_speed"])
        print("Modelo : ", info_nave["model"])
        print("Nombre : ", info_nave["name"])
        print("Pasajeros :", info_nave["passengers"])
        json_path = os.path.join("reportes_consulta", archivo_json)
        guardar_diccionario(info_nave, json_path)
        json_to_excel(json_path, archivo_excel)
    else:
        print("No se pudo obtener información de la nave.")

def mostrar_info_vehiculo(id_vehiculo, vehiculos, archivo_json, archivo_excel):
    url = f"{URL_BASE}/vehicles/{id_vehiculo}/"
    info_vehiculo = obtener_info(url)
    if info_vehiculo:
        print("capacidad de carga : ", info_vehiculo["cargo_capacity"])
        print("Consumibles : ", info_vehiculo["consumables"])
        print("Costo en creditos : ", info_vehiculo["cost_in_cresdits"])
        print("Creada"), info_vehiculo["created"]
        print("Crew : ", info_vehiculo["crew"])
        print("tamaño : ", info_vehiculo["length"])
        print("Manufacturada : ", info_vehiculo["manufacturer"])
        print("Maxima velocidad en  atmosfera : ", info_vehiculo["max_atmosphering_speed"])
        print("Modelo : ", info_vehiculo["model"])
        print("Nombre :", info_vehiculo["name"])
        print("pasajeros : ", info_vehiculo["passengers"])
        json_path = os.path.join("reportes_consulta", archivo_json)
        guardar_diccionario(info_vehiculo, json_path)
        json_to_excel(json_path, archivo_excel)
    else:
        print("No se pudo obtener información del vehículo.")

def mostrar_info_planeta(id_planeta, planetas, archivo_json, archivo_excel):
    url = f"{URL_BASE}/planets/{id_planeta}/"
    info_planeta = obtener_info(url)
    if info_planeta:
        print("Nombre : ", info_planeta["name"])
        print("Periodo de orbita :", info_planeta["orbital_period"])
        print("Poblacion : ", info_planeta["population"])
        print("clima : ", info_planeta["climate"])
        print("Diametro ; ", info_planeta["diameter"])
        json_path = os.path.join("reportes_consulta", archivo_json)
        guardar_diccionario(info_planeta, json_path)
        json_to_excel(json_path, archivo_excel)
    else:
        print("No se pudo obtener información del planeta.")

def obtener_info_star_wars():
    while True:
        print("1 PARA PERSONAJES, 2 PARA PELICULAS, 3 PARA NAVES, 4 VEHICULOS , 5 ESPECIES Y 6 PLANETAS")
        opc = int(input("Ingrese el numero que desea: "))
        if opc == 1:
            id_personaje = input("Dame el id del personaje: ")
            mostrar_info_personaje(id_personaje, [], "personajes.json", "personajes.xlsx")
        elif opc == 2:
            id_pelicula = input("Ingresa el id de la película que deseas: ")
            mostrar_info_pelicula(id_pelicula, [], "peliculas.json", "peliculas.xlsx")
        elif opc == 3:
            id_nave = input("Dame el id de la nave que deseas: ")
            mostrar_info_nave(id_nave, [], "naves.json", "naves.xlsx")
        elif opc == 4:
            id_vehiculo = input("Dame el id del vehículo: ")
            mostrar_info_vehiculo(id_vehiculo, [], "vehiculos.json", "vehiculos.xlsx")
        elif opc == 5:
            id_planeta = input("Dame el id del planeta que deseas: ")
            mostrar_info_planeta(id_planeta, [], "planetas.json", "planetas.xlsx")
        else:
            print("Opción no válida.")

        seguir = input("¿Desea continuar (SI/NO)? ")
        if seguir.lower() != "si":
            break

if __name__ == "__main__":
    obtener_info_star_wars()