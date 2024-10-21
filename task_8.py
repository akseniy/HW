text = """
[Куплет 1]  
В истерике кружилась мама Валя  
На заднем фоне замер папа Толя  
В радиусе метра воцарился жесточайший хаос  
Когда всем понятно стало: сын остался без диплома  
Мама, не кричи, хватит плакать, не смей      
Я не спорю — надо, но послушай отец:  
Есть у меня своя волна, и на своей волне  
Меня где-то поджидает успех  

[Предприпев]      
Боже, как хотел я увидеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне  
Вдруг увидел солнце — и тогда себе я сказал:  

[Припев]  
Я выбираю — жить в кайф!    
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!       
Я выбираю — жить в кайф!

[Куплет 2]  
Это был сон, в котором я
Не прогорал, не огорчал родных и не нуждался ни в чём
В котором мне не пришлось скрывать глаза       
И лгать давним знакомым: мол, в жизни моей всё хорошо  
В моём рюкзаке пару маек, носки     
И пускай начало оставляет желать лучшего        
Все, кто меня помнит — знает, я не был таким  
А значит, и у вас получится     

[Предприпев]  
Ведь всё, что я хотел, это видеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне         
Вдруг услышав музыку — я сам себе сказал:  

[Припев]  
Я выбираю — жить в кайф!    
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!      
Я выбираю — жить в кайф!      

[Предприпев]  
Боже, как хотел я увидеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне             
Вдруг увидел солнце — и тогда себе я сказал:  

[Припев]  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!         
Я выбираю — жить в кайф!
"""

# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼

new_text = text.split('\n\n')
my_dict = {}

for elem in new_text:
    elem = elem.strip()
    elem_list = elem.split('\n')
    name = elem_list[0].strip()[1:-1].lower()
    if name != 'предприпев':
        my_dict[name] = []
        for i in range(1, len(elem_list)):
            my_dict[name].append(elem_list[i].strip())
    else:
        if 'предприпев 1' in my_dict:
            help_mass = []
            for i in range(1, len(elem_list)):
                help_mass.append(elem_list[i].strip())
            if help_mass == my_dict['предприпев 1']:
                continue
            else:
                my_dict['предприпев 2'] = help_mass

        else:
            my_dict['предприпев 1'] = []
            for i in range(1, len(elem_list)):
                my_dict['предприпев 1'].append(elem_list[i].strip())


def task_1():
    position = input()
    print(*my_dict[position.lower()], sep='\n')


def task_2():
    for elem in new_text:
        elem = elem.strip()
        elem_list = elem.split('\n')
        for i in elem_list[1:]:
            print(i.strip().center(60))
        print()


def task_3():
    mode = input().lower()
    if mode == 'песня':
        line_text = ''
        for elem in new_text:
            elem = elem.strip()
            elem_list = elem.split('\n')
            for i in elem_list[1:]:
                line_text += i.strip() + ' '
    else:
        line_text = ''
        elem_list = my_dict['куплет 1']
        for i in elem_list:
            line_text += i.strip() + ' '
        elem_list = my_dict['куплет 2']
        for i in elem_list:
            line_text += i.strip() + ' '

    line_text = line_text.replace(':', '')
    line_text = line_text.replace(',', '')
    line_text = line_text.replace('— ', '')
    line_text = line_text.replace('!', '')
    line_text = ' ' + line_text.lower() + ' '
    print(line_text)

    my_set = set(line_text.split())
    words_num = dict()
    for i in my_set:
        words_num[i] = line_text.count(' ' + i + ' ')
    sorted_words = sorted(words_num.items(), key=lambda x: x[1], reverse=True)

    for i in sorted_words[:3]:
        print(f'"{i[0]}" - {i[1]} раз')


num = input()
if num == '1':
    task_1()
elif num == '2':
    task_2()
elif num == '3':
    task_3()
else:
    print('Введите корректное значение')
