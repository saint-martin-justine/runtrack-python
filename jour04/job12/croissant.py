def tri_croissant(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

ma_liste = [7, 11, 42, 39, 2]
tri_croissant(ma_liste)
print(ma_liste)
