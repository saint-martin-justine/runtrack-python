def arrondir_et_trier(liste):
    for i in range(len(liste)):
        liste[i] = int(liste[i] + 0.5)
    n = len(liste)
    for i in range(n):
        tri_effectue = False
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                tri_effectue = True
        if not tri_effectue:
            break

    return liste

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
ma_liste_arrondie_et_triee = arrondir_et_trier(ma_liste)
print(ma_liste_arrondie_et_triee)
