import view, model

def start():
    choise = 1
    while choise != 9:
        choise = view.show_menu()
        match(choise):
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 1:
                path = view.input_path()
                model.set_path(path)
                model.open_file()
            case 2:
                pass
            case 3:
                phone_book = model.get_phone_book()
                if len(phone_book) < 1:
                    view.notopen_phone_book()
                else:
                    contact = view.input_contact()
                    model.new_contact(contact)
            case 4:
                phone_book = model.get_phone_book()
                if len(phone_book) < 1:
                    view.notopen_phone_book()
                else:
                    contact = view.input_change()
                    if contact == '3':
                        pass
                    else:
                        model.change_contact(*contact)
            case 5:
                phone_book = model.get_phone_book()
                if len(phone_book) < 1:
                    view.notopen_phone_book()
                else:
                    contact = view.input_delete()
                    if contact == 'null':
                        pass
                    else:
                        model.delete_contact(contact)
            case 6:
                phone_book = model.get_phone_book()
                if len(phone_book) < 1:
                    view.notopen_phone_book()
                else:
                    value = view.input_search()
                    result = model.search_contact(value)
                    view.output_search(result)