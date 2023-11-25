def my_sort(liste):
    coups = 0
    trie = False

    while not trie:
        trie = True
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                trie = False
                coups += 1

    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")
    return liste

ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee = my_sort(ma_liste)
print("Liste triée :", liste_triee)
