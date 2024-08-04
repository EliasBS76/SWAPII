import pandas as pd

def estadisticas(excel_path):
    # Cargar el archivo Excel
    df = pd.read_excel(excel_path)

    # Estadísticas por género
    genero_stats = df['gender'].value_counts(normalize=True) * 100
    print("Estadísticas por género:")
    print(genero_stats)

    # Estadísticas por color de cabello
    cabello_stats = df['hair_color'].value_counts(normalize=True) * 100
    print("\nEstadísticas por color de cabello:")
    print(cabello_stats)

    # Porcentaje de hombres, mujeres y de cada tipo de cabello
    total_registros = len(df)
    porcentaje_hombres = (df['gender'].eq('male').sum() / total_registros) * 100
    porcentaje_mujeres = (df['gender'].eq('female').sum() / total_registros) * 100
    porcentaje_cabello_brown = (df['hair_color'].eq('brown').sum() / total_registros) * 100
    porcentaje_cabello_black = (df['hair_color'].eq('black').sum() / total_registros) * 100
    porcentaje_cabello_none = (df['hair_color'].eq('none').sum() / total_registros) * 100
    porcentaje_cabello_brown_grey = (df['hair_color'].eq('brown, grey').sum() / total_registros) * 100



# Prueba del módulo
if __name__ == "__main__":
    estadisticas("Reportes_numericos/personajes.xlsx")