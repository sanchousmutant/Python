from data_create import *

def input_data(): #ввод данных
    surname = input_surname().title()
    name = input_name().title()
    patronymic = input_patronymic().title()
    phone = input_phone()
    adress = input_adress().title()
    str_contact = f'{surname} {name} {patronymic} {phone} \n{adress} \n\n' # формирование данных контакта 
    with open('phonebook.txt', 'a', encoding="UTF-8") as file: # открытие для дозаписи в кодировке utf-8
        file.write(str_contact) # запись сформированных данных
    with open('copy_phonebook.txt', 'a', encoding="UTF-8") as file: # резервная копия
        file.write(str_contact)    

def read_file(): # чтение файла
    with open('phonebook.txt', 'r', encoding="UTF-8") as file: # открытие для чтения в кодировке utf-8
        return file.read() # чтение файла

def print_data(): # вывод на экран данных файла
    print(read_file()) # считываем данные файла (вызов функции чтения) и выводим данные на экран

def search_data(): # поиск
    command = ''
    print('Выберете параметр поиска: \n\n'
            '1) Фамилия \n'
            '2) Имя \n'
            '3) Отчество \n'
            '4) Номер телефона \n'
            '5) Адрес')
    print() # для красоты пустая строка
    command = input('Введите номер варианта поиска: ')
    while command not in ('1', '2', '3', '4', '5'): # отработка некорректного ввода
        print('Некорректный ввод номера варианта поиска! \n'
            'Повторите ввод' + '\n')
        command = input('Введите номер операции: ')
        print()
    id_search_param = int(command) - 1 # индекс параметра поиска   
    search = input("Введите данные для поиска: ").title()
    contacts_lst = read_file().rstrip().split('\n\n') # список контактов
    for contact_str in contacts_lst:
        contact_lst = contact_str.replace('\n', ' ').split() # данные контакта списком
        if search in contact_lst[id_search_param]:
            print()
            print(contact_str)
            
def edit_data():  
    search = input("Введите данные для поиска: ").title()
    contacts_lst = read_file().rstrip().split('\n\n') # список контактов
    for contact_str in contacts_lst: # перебираю контакты
        command = ''
        if search in contact_str:
            print() # для красоты
            print(contact_str + '\n')
            command = input('Редактировать контакт? \n\n'          
                  '1) Да \n'
                  '2) Нет \n\n'
                  'Введите номер операции: ')
            print() # для красоты
            while command not in ('1', '2'): # отработка некорректного ввода
                print('Некорректный ввод! \n'
                        'Повторите ввод' + '\n')
                command = input('Введите номер операции: ')
                print() # для красоты пустая строка
            match command: # шаблоны для пунктов меню
                case '1':
                    contacts_lst.remove(contact_str)
                    print('Выберете пункт для редактирования: \n\n'
                            '1) Фамилия \n'
                            '2) Имя \n'
                            '3) Отчество \n'
                            '4) Номер телефона \n'
                            '5) Адрес')
                    print() # для красоты пустая строка
                    command = input('Введите номер параметра: ')
                    while command not in ('1', '2', '3', '4', '5'): # отработка некорректного ввода
                        print('Некорректный ввод номера варианта поиска! \n'
                        'Повторите ввод' + '\n')
                        command = input('Введите номер операции: ')
                        print() # для красоты пустая строка
                    id_search_param = int(command) - 1 # индекс параметра поиска   
                    contact_lst = contact_str.replace('\n', ' ').split() # данные контакта списком
                    contact_lst[id_search_param] = (input('Введите необходимые изменения: ')).title()
                    contact_lst[-1] = '\n' + contact_lst[-1] # чтобы адрес был на новой строке
                    contact_str = ' '.join(contact_lst) # собираю строку контакта
                    contacts_lst.append(contact_str) # добавляю измененный контакт в список контактов
                    break # не рассматриваем др контакты с аналогичными параметрами
                case '2':
                    continue
    with open('phonebook.txt', 'w', encoding="UTF-8") as file: # перезаписываю телефонную книгу
        for contact in contacts_lst:
            file.writelines(contact + '\n\n')                   

def del_data():
    command = ''  
    search = input("Введите данные для поиска: ").title()
    contacts_lst = read_file().rstrip().split('\n\n') # список контактов
    for contact_str in contacts_lst:
        if search in contact_str:
            print(contact_str + '\n')
            command = input('Удалить контакт? \n\n'          
                  '1) Да \n'
                  '2) Нет \n\n'
                  'Введите номер операции: ')
            print()
            while command not in ('1', '2'): # отработка некорректного ввода
                        print('Некорректный ввод! \n'
                        'Повторите ввод' + '\n')
                        command = input('Введите номер операции: ')
                        print() # для красоты пустая строка
            match command: # шаблоны для пунктов меню
                case '1':
                    contacts_lst.remove(contact_str)
                case '2':
                    continue          
    with open('phonebook.txt', 'w', encoding="UTF-8") as file: # перезаписываю телефонную книгу
        for contact in contacts_lst:
            file.writelines(contact + '\n\n')