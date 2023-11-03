from logger import *

def interface(): # меню пользователя
    with open('phonebook.txt', 'a', encoding="UTF-8"): # инициализация файла в кодировке utf-8
        pass # чтобы структура кода осталась корректной (pass - ничего не делай)
    command = ''
    while command != '6': # условие выхода из программы
        print('Выберете вариант работы с телефонной книгой: \n\n'
                '1) Запись данных \n'
                '2) Вывод данных на экран \n'
                '3) Поиск \n'
                '4) Редактировать контакт \n'
                '5) Удалить контакт \n'
                '6) Выход')
        print() # тупо для красоты пустая строка
        command = input('Введите номер операции: ')
        while command not in ('1', '2', '3', '4', '5', '6'): # отработка некорректного ввода
            print('Некорректный ввод номера операции! \n'
                'Повторите ввод')
            command = input('Введите номер операции: ')
            print()
        match command: # шаблоны для пунктов меню
            case '1':
                print() # тупо для красоты пустая строка
                input_data()
                print()
            case '2':
                print()
                print_data()
                print()
            case '3':
                print()
                search_data()
                print()
            case '4':
                print()
                edit_data()
                print()
            case '5':
                print()
                del_data()   
                print()     
            case '6':
                print()
                print('Приложение закрыто')