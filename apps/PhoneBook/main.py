'''
Создать телефонный справочник с  возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Дополнить справочник возможностью копирования данных из одного файла в другой.
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

'''


# вывод меню
def menu() -> list:
    list_menu = list()
    list_menu.append("Вывести весь список")
    list_menu.append("Найти по фамилии")
    list_menu.append("Найти по телефону")
    list_menu.append("добавить запись в справочник")
    list_menu.append("изменить телефон в справочнике по фамилии")
    list_menu.append("удалить запись по фамилии")  # 6
    list_menu.append("сохранить в файл")
    list_menu.append("добавить строки из другого файла")  # 8
    list_menu.append("закончить")
    return list_menu


def merge_file():
    name_donor = input("введите имя файла из которого будем копировать строку: ")
    number = int(input(" и номер строки для копирования: "))
    with open(name_donor, 'r', encoding="utf-8") as tf:
        eggs = list()
        for line in tf:
            if line != "\n":
                eggs.append(line)

    if len(eggs) < number:
        print("Копирование не удалось: в файле всего " + str(len(eggs)) + " строк")
    else:
        with open(name_file, "a") as tf:
            tf.write(str(eggs))
        phone_book.clear()
        read_file()
        print("копирование прошло удачно. загруженный справочник обновлен")


def choice_menu(choice):
    match choice:
        case 1:
            print_phone()
        case 2:
            find_by_first_name()
        case 3:
            find_by_first_phone()
        case 4:
            add_in_dict()
        case 5:
            change_record()
        case 6:
            delete_record_by_first_name()
        case 7:
            save_to_file()
        case 8:
            merge_file()
        case _:
            print("ошибка запроса")


# читаю из файла
def read_file():
    title = ["first_name", "last_name", "phone", "description"]
    with open(name_file, 'r', encoding="utf-8") as tf:
        for line in tf:
            if line != "\n":
                phone_book.append(dict(zip(title, line[:-1].split(","))))


# запись в файл
def write_file():
    with open(name_file, "w") as tf:
        for item in phone_book:
            eggs = [item["first_name"], item["last_name"], str(item["phone"]), item["description"]]
            spam = ",".join(eggs) + "\n"
            tf.write(spam)


# вывод меню на экран
def show_menu():
    print("\nМеню:")
    for i, item in enumerate(menu(), 1):
        print(i, item)


# вывод на экран всего справочника
def print_phone():
    print("Вывод списка: ")
    for item in phone_book:
        print(toString_record(item))


def find_by_first_name():
    print("поиск по фамилии:")
    search_name = input("Введите фамилию для поиска: ")
    count = 0
    print("результат поиска по фамилии: ")
    for item in phone_book:
        if str(item.get("first_name")).lower() == search_name.lower():
            print(toString_record(item))
            count += 1
    print("найдено " + str(count) + " записей")


def delete_record_by_first_name():
    print("поиск по фамилии:")
    search_name = input("Введите фамилию для поиска для удаления: ")
    result = list()
    for i in range(len(phone_book)):
        if str(phone_book[i].get("first_name")).lower() == search_name.lower():
            result.append(i)
    print("найдено записей по вашему запросу: " + str(len(result)))
    if len(result) > 0:
        for i, item in enumerate(result, 1):
            print(i, toString_record(phone_book[item]))
        number_delete = int(input("\nукажите номер записи для удаления: "))
        if number_delete > len(result):
            print("некорректно указан номер. удаление невозможно")
        else:
            eggs = phone_book.pop(result[number_delete - 1])
            print("удалена запись: " + toString_record(eggs))


def toString_record(item: dict) -> str:
    eggs = [item.get("first_name"), item.get("last_name"), str(item.get("phone")), item.get("description")]
    title = ["Фамилия: ", "Имя: ", "Телефон:", "Описание: "]
    return "\t".join(list(map(lambda x: x[0] + x[1], zip(title, eggs))))


def find_by_first_phone():
    print("поиск по телефону")
    search_name = input("Введите телефон для поиска: ")
    count = 0
    print("результат поиска по телефону: ")
    for item in phone_book:
        if str(item.get("phone")).lower() == str(search_name).lower():
            print(toString_record(item))
            count += 1
    print("найдено " + str(count) + " записей")


def add_in_dict():
    print("добавление записи")
    print("Введите данные для записи в файл в формате: 'Фамилия, Имя, Телефон, Описание' через пробел ")
    spam = input("новая запись: ").split(" ")
    if len(spam) < 4:
        print("Не удалось добавить запись: некорректно введены данные")
    else:
        first_name, last_name, phone, *descr = spam
        phone_book.append({"first_name": first_name,
                           "last_name": last_name,
                           "phone": phone,
                           "description": " ".join(descr)})


def save_to_file():
    print("сохранение в файл")
    write_file()


def change_record():
    print("изменение телефона записи по фамилии:")
    spam = input("Введите фамилию для поиска и новый номер: ").split(" ")
    if len(spam) != 2:
        print("некорректно указаны данные")
    else:
        search_name, new_phone = spam
        result = list()
        for i in range(len(phone_book)):
            if str(phone_book[i].get("first_name")).lower() == search_name.lower():
                result.append(i)
        print("найдено записей по вашему запросу: " + str(len(result)))
        if len(result) == 1:
            phone_book[result[0]]["phone"] = new_phone
            print("запись изменена: " + toString_record(phone_book[result[0]]))

        elif len(result) > 1:
            for i, item in enumerate(result, 1):
                print(i, toString_record(phone_book[item]))
            number_delete = int(input("\nукажите номер записи для изменения: "))
            if number_delete > len(result):
                print("некорректно указан номер. изменение невозможно")
            else:
                phone_book[result[number_delete - 1]]["phone"] = new_phone
                print("запись изменена: " + toString_record(phone_book[result[number_delete - 1]]))


def work_phone():
    work = True
    read_file()
    while work:
        show_menu()
        choice = input("\nвыберете пункт: ")
        if choice.isnumeric():
            if int(choice) < len(menu()):
                choice_menu(int(choice))
            elif int(choice) == len(menu()):
                print("\nработа закончена")
                work = False


def init():
    book = list()
    book.append({"first_name": "Cat", "last_name": "Tom", "phone": "111", "description": "cat in home"})
    book.append({"first_name": "Mouse", "last_name": "Jerry", "phone": 222, "description": "mouse in home"})
    book.append({"first_name": "Woman", "last_name": "Lulu", "phone": 333, "description": "owner in home"})
    return book


name_file = "book.txt"
phone_book = list()
work_phone()
