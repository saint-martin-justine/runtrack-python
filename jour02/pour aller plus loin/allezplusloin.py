def est_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def type_triangle(a, b, c):
    if a == b == c:
        return "Équilatéral"
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Rectangle et isocèle"
        return "Isocèle"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Rectangle"
    else:
        return "Quelconque"


a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))


if est_triangle(a, b, c):
    print("Ces longueurs peuvent former un triangle.")
   
    print("Type de triangle :", type_triangle(a, b, c))
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
