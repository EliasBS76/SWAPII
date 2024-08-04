import os
import pandas as pd

def cargar_datos_desde_excel(archivo_excel):
    ruta_excel = os.path.join("C:\\Users\\Elias\\Desktop\\SWAPI_STATS\\Reportes_numericos", f"{archivo_excel}.xlsx")
    try:
        df = pd.read_excel(ruta_excel)
        return df
    except FileNotFoundError:
        print(f"El archivo {ruta_excel} no se encontró.")
        return None

def mostrar_info_desde_excel(archivo_excel, columnas_deseadas):
    datos = cargar_datos_desde_excel(archivo_excel)
    if datos is not None:
        print(f"Información de {archivo_excel}:")
        datos_filtrados = datos[columnas_deseadas]
        print(datos_filtrados)
    else:
        print(f"No se pudieron cargar los datos de {archivo_excel}.")

def obtener_archivo_excel():
    while True:
        print("Archivos disponibles:")
        print("1. Personajes")
        print("2. Naves")
        print("3. Películas")
        print("4. Planetas")
        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == "1":
            return "personajes", ["name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year", "gender"]
        elif opcion == "2":
            return "naves", ["name", "model", "manufacturer", "cost_in_credits", "length", "max_atmosphering_speed",
                             "crew", "passengers", "cargo_capacity", "consumables", "hyperdrive_rating", "MGLT"]
        elif opcion == "3":
            return "peliculas", ["title", "episode_id", "opening_crawl", "director", "producer", "release_date"]
        elif opcion == "4":
            return "planetas", ["name", "rotation_period", "orbital_period", "diameter", "climate", "gravity",
                                "terrain", "surface_water", "population"]
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    while True:
        try:
            archivo_excel, columnas_deseadas = obtener_archivo_excel()
            mostrar_info_desde_excel(archivo_excel, columnas_deseadas)
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"Se produjo un error: {e}")

        continuar = input("¿Desea realizar otra consulta? (s/n): ")
        if continuar.lower() != "s":
            break