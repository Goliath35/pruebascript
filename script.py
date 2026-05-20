import pandas as pd
import json
import math
import subprocess

# 1. Leer Excel
df = pd.read_excel("Proyectores QR.xlsx")

# 2. Limpiar columnas basura
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# 3. Filtrar filas vacías
df = df.dropna(subset=["Marca"])

# 4. Convertir a JSON
data = df.to_dict(orient="records")

# 7. Git (IMPORTANTE: con control de errores)
subprocess.run(["git", "add", "."], check=True)

commit = subprocess.run(
    ["git", "commit", "-m", "Actualización automática"],
    capture_output=True,
    text=True
)

print(commit.stdout)

# Solo hacer push si hubo commit real
# 5. Limpiar NaN
def limpiar_nans(obj):
    if isinstance(obj, list):
        return [limpiar_nans(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: limpiar_nans(v) for k, v in obj.items()}
    elif isinstance(obj, float) and math.isnan(obj):
        return None
    return obj

data = limpiar_nans(data)

# 6. Guardar JSON
with open("proyectores.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✔ JSON creado correctamente")

# 7. Git
subprocess.run(["git", "add", "."], check=True)

commit = subprocess.run(
    ["git", "commit", "-m", "Actualización automática"],
    capture_output=True,
    text=True
)
print(commit.stdout)

# 8. Pull antes de push para evitar conflictos
subprocess.run(["git", "pull", "--rebase"], check=True)

# 9. Solo hacer push si hubo commit real
if "nothing to commit" not in commit.stdout:
    subprocess.run(["git", "push"], check=True)
    print("✔ GitHub actualizado")
else:
    print("⚠ No había cambios para subir")
    print("⚠ No había cambios para subir")
