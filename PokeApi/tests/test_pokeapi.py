#Este código fue creado por Jackson Rojas.
import requests
import datetime

# Nombre del archivo de reporte
REPORTE_HTML = "../reporte.html"

# Función para agregar resultados al reporte
def agregar_reporte(caso, resultado, detalles=""):
    color = "green" if resultado else "red"
    with open(REPORTE_HTML, "a", encoding="utf-8") as f:
        f.write(f"<p style='color:{color};'><b>{caso}:</b> {'✅ PASÓ' if resultado else '❌ FALLÓ'} - {detalles}</p>\n")

# Crear/limpiar el reporte al inicio
with open(REPORTE_HTML, "w", encoding="utf-8") as f:
    f.write(f"<h1>Reporte PokeAPI - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h1>\n")

# -------------------
# Caso 1 - berry/1
# -------------------
url1 = "https://pokeapi.co/api/v2/berry/1"
resp1 = requests.get(url1)
data1 = resp1.json()

agregar_reporte("Caso 1 - size", data1["size"] == 20, f"size={data1['size']}")
agregar_reporte("Caso 1 - soil_dryness", data1["soil_dryness"] == 15, f"soil_dryness={data1['soil_dryness']}")
agregar_reporte("Caso 1 - firmness", data1["firmness"]["name"] == "soft", f"firmness={data1['firmness']['name']}")

# -------------------
# Caso 2 - berry/2
# -------------------
url2 = "https://pokeapi.co/api/v2/berry/2"
resp2 = requests.get(url2)
data2 = resp2.json()

agregar_reporte("Caso 2 - firmness", data2["firmness"]["name"] == "super-hard", f"firmness={data2['firmness']['name']}")
agregar_reporte("Caso 2 - size mayor que caso1", data2["size"] > data1["size"], f"size={data2['size']}")
agregar_reporte("Caso 2 - soil_dryness igual que caso1", data2["soil_dryness"] == data1["soil_dryness"], f"soil_dryness={data2['soil_dryness']}")

# -------------------
# Caso 3 - pokemon/pikachu
# -------------------
url3 = "https://pokeapi.co/api/v2/pokemon/pikachu/"
resp3 = requests.get(url3)
data3 = resp3.json()

# Experiencia base entre 10 y 1000
exp_correcta = 10 < data3["base_experience"] < 1000
agregar_reporte("Caso 3 - base_experience", exp_correcta, f"base_experience={data3['base_experience']}")

# Tipo "electric"
tipos = [t["type"]["name"] for t in data3["types"]]
agregar_reporte("Caso 3 - tipo electric", "electric" in tipos, f"tipos={tipos}")

# -------------------
# Fin del reporte
# -------------------
with open(REPORTE_HTML, "a", encoding="utf-8") as f:
    f.write("<p>✅ Fin de la ejecución</p>\n")
