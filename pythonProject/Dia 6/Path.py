from pathlib import Path
"""
base = Path.home() # ruta absoluta al directorio principal del usuario.
guia = Path(base, "Europa","España",Path("Barcelona", "Sagrada_Familia.txt"))
# guia2 = guia.with_name("La_Pedrera.txt")
# print(guia2)

print(guia.parent.parent) # Recorrer guias


"""

guia = Path(Path.home(),"Europa")

for txt in Path(guia).glob("**/*.txt"): # * todos - **/* todas las carpetas y subcarpetas
    print(txt)

guia1 = Path("Europa","España","Barcelona", "Sagrada_Familia.txt")
en_europa = guia1.relative_to(Path("Europa"))
en_espania = guia1.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)

""" PRACTICAS 

# Práctica Path 1

from pathlib import Path
ruta_base = Path.home()

# Práctica Path 2

from pathlib import Path
ruta = Path("Curso Python","Día 6","practicas_path.py")


# Práctica Path 3
from pathlib import Path
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")
"""