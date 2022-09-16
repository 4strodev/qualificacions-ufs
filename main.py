# Author Juan Alejandro Marin AKA 4strodev
# Definició de classes
class UnitatFormativa:
    nom = None
    nota = None

    def __init__(self, nom):
        self.nom = nom


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari")
uf2 = UnitatFormativa("UF2. Optimització del programari")
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes")

uf1.nota = 8
uf2.nota = 10
uf3.nota = 4

print(uf1.nom, ":", uf1.nota)
print(uf2.nom, ":", uf1.nota)
print(uf3.nom, ":", uf1.nota)