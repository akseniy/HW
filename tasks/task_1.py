def CamelCase(user: str):
    new = user[0].lower()
    for i in range(1, len(user)):
        if user[i].isupper():
            new = new + '_' + user[i].lower()
        else:
            new = new + user[i]

    return new


alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

user_input = input()

user_input = user_input.replace('-', '_')

user_input = user_input.replace('_', ' ')

input_list = user_input.split()

for i in range(len(input_list)):
    input_list[i] = CamelCase(input_list[i])
output_text = '_'.join(input_list)

while len(output_text) > 0 and (output_text[0].isdigit() or output_text[0] == '_'):
    output_text = output_text[1:]

flag = True
for elem in output_text:
    if elem.isdigit() or elem == '_' or elem in alf:
        continue
    else:
        flag = False
        break

if not flag or len(output_text) == 0:
    print("Введено некорректное имя переменной")
else:
    print(output_text)
