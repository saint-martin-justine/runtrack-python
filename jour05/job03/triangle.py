def draw_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if i == 1:
            print(spaces + '_')
        elif i == height:
            print('/' + '_' * (2 * i - 3) + '\\')
        else:
            print(spaces + '/' + ' ' * (2 * i - 3) + '\\')

draw_triangle(5)
