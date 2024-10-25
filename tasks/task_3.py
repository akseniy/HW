person = ['Энакин Скайуокер',
          41,
          ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
          {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
          ]


def task_1():
    name, surname = person[0].split()
    print(f'Персона: {{{surname}}}, {{{name}}}')


def task_2():
    print(person[1])


def task_3():
    print(*person[2], sep=', ')


def task_4():
    print(len(person[2]))


def task_5():
    print('Звезда Смерти' in person[2])


def task_6():
    print(person[3]['световой меч'])


def task_7():
    person[1] = 42
    print(person[1])


def task_8():
    if "Эндор" in person[2]:
        print(*person[2], sep=', ')
    else:
        person[2].append("Эндор")
        print(*person[2], sep=', ')


def task_9():
    if person[3]['ранг'] == 'лорд ситхов':
        print("Энакин - лорд ситхов")
    else:
        print("Энакин - джедай")


def task_10():
    if len(person[2]) > 4:
        print("Энакин побывал во многих местах")
    else:
        print('Энакин не так много путешествовал')


# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here /ᐠ˵- ⩊ -˵マ

num = int(input())

if num == 1:
	task_1()
elif num == 2:
	task_2()
elif num == 3:
	task_3()
elif num == 4:
	task_4()
elif num == 5:
	task_5()
elif num == 6:
	task_6()
elif num == 7:
	task_7()
elif num == 8:
	task_8()
elif num == 9:
	task_9()
elif num == 10:
	task_10()
else:
	print('Введите корректное значение')
