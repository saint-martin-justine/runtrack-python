def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro impossible."
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Modulo par zéro impossible."
    else:
        return "Opérateur non valide."

result_addition = calcule(5, '+', 3)
result_subtraction = calcule(10, '-', 7)
result_multiplication = calcule(4, '*', 6)
result_division = calcule(15, '/', 3)
result_modulo = calcule(20, '%', 7)

print("Résultat de l'addition:", result_addition)
print("Résultat de la soustraction:", result_subtraction)
print("Résultat de la multiplication:", result_multiplication)
print("Résultat de la division:", result_division)
print("Résultat du modulo:", result_modulo)
