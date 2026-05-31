import json
def show_all():
     with open('info_human.json','r',encoding='utf-8') as file:
         data = json.load(file)
         for i in data['information']:
             print('Информация')
             print('Имя:',i['name'])
             print('Возраст:',i['age'])
             print('Работа:',i['work'])
             print('Навыки:',*i['skills'])    
             print('Номер телефона',i['phone'])
             print('Почтовый ящик',i['email'])



def add_info(name,age,work,skills,phone,email):
    with open('info_human.json','r',encoding='utf-8') as file:
        data = json.load(file)
        add_person = data['information']
        user_info = {'name':name,'age':age,'work':work,'skills':skills,'phone':phone,'email':email}
        add_person.append(user_info)
    
    with open('info_human.json','w',encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

        
def find_user(name):
    with open('info_human.json','r',encoding='utf-8') as file:
        data = json.load(file)
        for i in data['information']:
            if i['name'] == name:
                print('----------')
                print('Имя:', i['name'])
                print('Возраст:', i['age'])
                print('Работа:', i['work'])
            print('----------')
            return
        print('Контакт не найден!')


def delete_user(name):
    with open('info_human.json','r',encoding='utf-8') as file:
        data = json.load(file)
        for i in data['information']:
            if i['name'] == name:
                data['information'].remove(i)
                print(f'{name} удален!')
                break
        else:
                print('Контакт не найден')
    with open('info_human.json','w',encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

show_all()
add_info('Leroy',20,'программист',['Python','PHP','MySQL'],89348543,'leroy@mail.ru')
find_user('Leroy')
delete_user('Leroy')
show_all()