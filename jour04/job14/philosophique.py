def my_long_word(longueur_minimale, phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if len(mot) > longueur_minimale]
    resultat = " ".join(mots_filtres)
    return resultat

output = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(output)
