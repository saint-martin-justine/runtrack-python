chaine = "abcdefghijklmnopqrstuvwxyz" * 10

longueur = len(chaine)
hauteur_pyramide = 10  # Vous pouvez ajuster la hauteur de la pyramide ici

for i in range(hauteur_pyramide):
    espaces = " " * (hauteur_pyramide - i - 1)
    caracteres = chaine[:i * 2 + 1]
    ligne = espaces + caracteres + espaces
    print(ligne.center(longueur))