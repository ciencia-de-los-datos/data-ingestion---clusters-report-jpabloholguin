"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    data = pd.read_fwf(        "clusters_report.txt", widths = [9, 16, 16, 80], header = None,
        names = ["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave", "-"],
        skip_blank_lines = False, converters = {"porcentaje_de_palabras_clave": 
        lambda x: x.rstrip(" %").replace(",",".")}).drop([0,1,2,3], axis=0)

    columna4 = data["-"]
    data = data[data["cluster"].notna()].drop("-", axis=1)
    data = data.astype({ "cluster": int, "cantidad_de_palabras_clave": int, "porcentaje_de_palabras_clave": float})

    c4Pro = []
    text = ""
    for lin in columna4:
        if isinstance(lin, str): text += lin+" "
        else:
            text = ", ".join([" ".join(x.split()) for x in text.split(",")])
            c4Pro.append(text.rstrip("."))
            text = ""
            continue

    data["principales_palabras_clave"] = c4Pro

    return data
