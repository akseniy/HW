# Your code here (づ｡◕‿‿◕｡)づ

my_dict = {'меч': 0, 'лук': 0, 'топор': 0, 'щит': 0, 'зелье': 0}

c = 0
while c < 3:
    mass_c = input().split()
    if all([i in my_dict for i in mass_c]):
        c += 1
        for i in mass_c:
            my_dict[i] += 1
    else:
        print("Неверный предмет, попробуйте снова")

res = 0
for i in my_dict.values():
    if i == 3:
        res += 1

print(res)