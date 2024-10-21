num = int(input())
flag = False

while num > 0:
    ost = num % 10
    if ost != 0:
        flag = True
    if flag:
        print(ost, end='')

    num //= 10

if not flag:
    print(0)
