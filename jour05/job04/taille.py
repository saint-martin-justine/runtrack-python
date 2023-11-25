def draw_diagonal_carpet(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print('\\', end='')
            elif i == n and j == 0:
                print('/', end='')
            else:
                print('#', end='')
        print()

draw_diagonal_carpet(5)
