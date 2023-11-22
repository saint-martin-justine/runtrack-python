def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:  # Vérification pour éviter une division par zéro
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        return num1 % num2
    else:
        return "Opérateur non reconnu"
resultat_addition = calcule(5, "+", 3)
resultat_multiplication = calcule(4, "*", 6)
resultat_division = calcule(10, "/", 2)

print("Résultat de l'addition :", resultat_addition)
print("Résultat de la multiplication :", resultat_multiplication)
print("Résultat de la division :", resultat_division)
