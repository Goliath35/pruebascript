import pandas as pd
import json

# 1. Leer el Excel
df = pd.read_excel("Proyectores QR.xlsx")

# 2. Convertirlo a lista de objetos
data = df.to_dict(orient="records")

# 3. Guardar como JSON
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

print("✔ GitHub actualizado")
