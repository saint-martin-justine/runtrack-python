L = [8, 24, 48, 2, 16]

nombre_multiples_de_trois = sum(nombre % 3 == 0 for nombre in L)

print(nombre_multiples_de_trois)
