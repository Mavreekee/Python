phone_book = []
path = 'Homework 8/data/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path 
    path += file

def open_file():
    global path 
    global phone_book
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        for line in phone_book:
            data.write(';'.join(str(i) for i in line) + '\n')

def change_contact(id, choise, value):
    global path
    global phone_book
    phone_book [int(id)][int(choise)] = value
    with open(path, 'w', encoding='UTF-8') as data:
        for line in phone_book:
            data.write(';'.join(str(i) for i in line) + '\n')

def delete_contact(id):
    global phone_book
    phone_book.pop(id)
    with open(path, 'w', encoding='UTF-8') as data:
        for line in phone_book:
            data.write(';'.join(str(i) for i in line) + '\n')

def search_contact(value):
    global phone_book
    result = [x for x in phone_book if any([value in str(y) for y in x])]
    return result