product = {'001': ['Батончик', '70'], '002': ['Вода', '45'], '003': ['Газировка', '64'], '004': ['Булочка', '33']}
banknotes = ['10', '50', '100', '500']

def print_table():
    print('ID'.ljust(5), 'ProductName'.ljust(15), 'Цена'.ljust(5), sep='')
    for i in product:
        print(i.ljust(5), product[i][0].ljust(15), product[i][1].ljust(5))
    print()


def read_id():
    id_prod = input('Введите ID желаемого товара:  ')
    price = None

    flag = True
    if id_prod in product:
        price = product[id_prod][1]
        print(f'Внесите {price} тугриков')
    elif id_prod == 'ОТМЕНА':
        return False, False, False
    else:
        print("Товара с таким ID не существует")
        flag = False

    return id_prod, flag, price


# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы

# Your code here(づ ᴗ _ᴗ)づ♡
print_table()
id_prod, flag, price = read_id()

if flag:
    bill = input('Внесите купюру  ')
    price = int(price)
    while True:
        if bill == 'ОТМЕНА':
            break
        elif bill in banknotes:
            price -= int(bill)
            if price > 0:
                print(f"Осталось внести {price} тугриков")
            else:
                print(f"Ваша сдача: {abs(price)} тугриков")
                break

        else:
            print("Внесена фальшивая куплюра")

        bill = input('Внесите купюру  ')

