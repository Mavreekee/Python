def show_menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')
    choise = int(input('Выберите пункт меню: '))
    return choise

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print()
        print('Телефонная книга пуста')
        print()
    else:
        print()
        for id, item in enumerate(phone_book):
            print(id, " | ".join(item))
        print()

def notopen_phone_book():
    print()
    print('Телефонная книга не открыта')
    print()

def input_path():
    path = input('Введите имя файла: ')
    return path

def input_contact():
    name_contact = input('Введите ФИО контакта: ')
    phone_contact = input('Введите номер контакта: ')
    comment_contact = input('Введите комментарий: ')
    return (name_contact, phone_contact, comment_contact)

def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить?')
    choise = input('0 - ФИО, 1 - Телефон, 2 - Комментарий, 3 - Отмена\nВыбор: ')
    if choise == '3':
        print('Возврат в меню')
        return choise
    else:
        value = input('Введите изменение: ')
        return (id, choise, value)

def input_delete():
    id = int(input('Введите номер контакта: '))
    print('Контакт удален')
    return id

def input_search():
    value = input('Поиск по частичному совпадению\nВведите значение: ')
    return value

def output_search(result):
    if len(result) < 1:
        print()
        print('Совпадений не найдено')
        print()
    else:
        print()
        for id, item in enumerate(result):
            print(id, " | ".join(item))
        print()