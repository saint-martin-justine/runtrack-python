def echanger_premier_dernier(liste):
    if liste:
        liste[0], liste[-1] = liste[-1], liste[0]

ma_liste = [1, 2, 3, 4, 5]
echanger_premier_dernier(ma_liste)
print(ma_liste)
