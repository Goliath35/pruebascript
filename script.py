import pandas as pd
import json
import math

# 1. Leer el Excel
df = pd.read_excel("Proyectores QR.xlsx")

# 2. Eliminar columnas "Unnamed"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# 3. Eliminar filas donde "Marca" esté vacía (filas basura)
df = df.dropna(subset=["Marca"])

# 4. Convertir a lista de objetos
data = df.to_dict(orient="records")

# 5. Reemplazar NaN por None
def limpiar_nans(obj):
    if isinstance(obj, list):
        return [limpiar_nans(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: limpiar_nans(v) for k, v in obj.items()}
    elif isinstance(obj, float) and math.isnan(obj):
        return None
    return obj

data = limpiar_nans(data)

# 6. Guardar como JSON
with open("proyectores.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✔ JSON creado correctamente")

import subprocess

# Git add
subprocess.run(["git", "add", "."])

# Commit
subprocess.run(["git", "commit", "-m", "Actualización automática"])

# Push a GitHub
subprocess.run(["git", "push"])

subprocess.run(["git", "pull", "--rebase"])

print("✔ GitHub actualizado")
