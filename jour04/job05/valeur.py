def remplacer_element(liste, index):
    if 0 < index < len(liste) - 1:
        liste[index] = liste[index - 1] + liste[index + 1]

L = [1, 2, 3, 4, 5]

deuxieme_valeur = L[1]
print(deuxieme_valeur)

remplacer_element(L, 3)

print(L)

derniere_valeur = L[-1]
print(derniere_valeur)

