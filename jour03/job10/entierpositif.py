def verifier_pair_impair(nombre):
    # Vérifier si le nombre est un entier positif
    if isinstance(nombre, int) and nombre >= 0:
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")
# Appeler la fonction avec différentes valeurs
verifier_pair_impair(4)
verifier_pair_impair(7)
verifier_pair_impair(0)
verifier_pair_impair(-5)  # Valeur non positive
verifier_pair_impair(3.14)  # Valeur non entière
10