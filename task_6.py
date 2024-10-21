# Your code here (˶ˆᗜˆ˵)

x, y = 0, 0
n = int(input('Введите N: '))

for i in range(1, n+1):
    nap = input(f'Ход {i}: ')
    if nap == 'Вверх':
        y += 1
    elif nap == 'Вниз':
        y -= 1
    elif nap == 'Вправо':
        x += 1
    elif nap == 'Влево':
        x -= 1

print(abs(x) + abs(y))
