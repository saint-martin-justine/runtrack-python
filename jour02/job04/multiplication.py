# Demander à l'utilisateur de saisir N
while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un entier valide.")

# Afficher les tables de multiplication
for i in range(1, N+1):
    print(f"\nTable de multiplication pour {i} :")
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
