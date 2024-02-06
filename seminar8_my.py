# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)

# f = open('myfile.txt', 'w', encoding='utf-8') # w - write, заменяет содержимое в файле
# f.write('какая-то строка\n')
# f.close()
#
# f = open('myfile.txt', 'a', encoding='utf-8') # a - add, добавляет содержимое в файле
# f.write('новая строка\n')
# f.close()

# with open('myfile.txt', 'w', encoding='utf-8') as fd:
#     fd.write('какая-то строка\n')

# with open('myfile.txt', 'r', encoding='utf-8') as fd: # r - read, читает содержимое в файле
#     from_file = fd.readlines()
#     print(from_file)
#
# with open('myfile2.txt', 'w', encoding='utf-8') as fd: # with - включает автоматическое закрытие файла после проведения операции
#     lines = ['строка\n', 'ещё строка\n', 'и ещё одна строчка\n']
#     fd.writelines(lines)

def read_file(file): # Функция чтения данных
    try: # Попытка выполнить функцию, но если не создан файл - выдает ошибку, которая уходит в 'except'
        with open(file, 'r', encoding='utf-8') as f: # 'r' - чтение данных
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []


def show_data(data: list): # Функция вывода данных
    for line in data:
        print(line)
    

def save_data(file): # Функция сохранения данных
    print('Введите данные контакта')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f: # 'a' - добавление данных
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')


def new_save(file, data): # Функция сохранения данных после изменений/ удалений
    if len(data)>0:
        with open(file, 'w', encoding='utf-8') as f: # Открытие файла с возможностью записи
            f.seek(0) # Установка чтения файла в начальное положение (нулевое)
            f.writelines(data) #(Перезапись всего файла с произведенными изменениями)
        return True   


def search_data(contacts: list[str]): # Функция поиска данных
    founded = []
    print('0 - поиск по имени')
    print('1 - поиск по фамилии')
    print('2 - поиск по отчеству')
    print('3 - поиск по номеру телефона')
    search_idx = input('Выберите вариант поиска: ') # для поиска по фамилии, имени, отчеству или номеру телефона
    #search_str = input('Введите данные для поиска: ')
    if search_idx == '0':
        search_str = input('Введите имя для поиска: ')
    elif search_idx == '1':
        search_str = input('Введите фамилию для поиска: ')
    elif search_idx == '2':
        search_str = input('Введите отчество для поиска: ') 
    elif search_idx == '3':
        search_str = input('Введите номер телефона для поиска: ')   
    else:
        print('Ошибка, такой функции нет') 
        return
    for contact in contacts:
        #contact_split = contact.split(', ')
        #if search_str.lower() in contact_split[int(search_idx)].lower(): # разделитель - запятая, поиск индексу
        if search_str.lower() in contact.split(', ')[int(search_idx)].lower(): # разделитель - запятая, поиск индексу
            founded.append(contact)
    if len(founded) == 0:
        print('Ни одного пользователя по запросу не найдено')
    return founded


def edit_data(data, idx, file): # Функция изменения данных
    print('0 - изменение имени')
    print('1 - изменение фамилии')
    print('2 - изменение отчества')
    print('3 - изменение номера телефона')
    edit_idx = input('Выберите, что вы хотите изменить: ') # для изменения фамилии, имени, отчества или номера телефона
    # Блок выбора меню 
                                                                                             #PS дописать с помощью try, потому что выдает ошибку при 'else'!!!
    if edit_idx == '0':
        edit_str = input('Введите новое имя: ')
    elif edit_idx == '1':
        edit_str = input('Введите новую фамилию: ')
    elif edit_idx == '2':
        edit_str = input('Введите новое отчество: ') 
    elif edit_idx == '3':
        edit_str = input('Введите новый номер телефона: ')   
    else:
        print('Ошибка, такой функции нет')    
    # Блок изменения данных в список (массив)
    contact_split = data[idx].split(', ') # 'idx' - номер строки в файле, которую надо изменить 
    contact_split[int(edit_idx)] = edit_str # изменение имени, фамилии или номера телефона, в зависимости от 'edit_idx' после разделения ее на список (массив)
    data[idx] = ', '.join(contact_split) # изменение указанной строки в списке (массиве)
    # Блок изменения данных в сам файл
    # if len(data)>0:
    #     with open(file, 'w', encoding='utf-8') as f: # Открытие файла с возможностью записи
    #         f.seek(0) # Установка чтения файла в начальное положение (нулевое)
    #         f.writelines(data) #(Перезапись всего файла с произведенными изменениями)
    #     return True
    new_save(file, data)


def delete_data(data, idx, file): # Функция удаления данных
    # Блок удаления данных данных в список (массив)
    del data[idx]  # удаление указанной строки в списке (массиве)
    new_save(file, data)


def copy_to_file(data, idx, file_2): # Функция копирования (экспорта) данных в другой файл
    if idx > len(data):
        print('Нет строки с таким номером')
        return
    with open(file_2, 'a', encoding='utf-8') as export:
        export.write(f'{data[idx]}\n')
        # for i in range(len(data)):
        #     if i != idx-1:
        #         export.write(data[i])


def main(): # Главная функция работы с данными
    file_name = 'phone_book.txt' # Создание константы в виде названия файла
    file_name_copy = 'phone_book_copy.txt'
    flag = True
    while flag: # Создание цикла бесконечного для выбора опции в меню
        print('0 - выход')
        print('1 - запись в записную книжку')
        print('2 - показать записную книжку')
        print('3 - выполнить поиск в записной книжке')
        print('4 - изменить данные в записной книжке')
        print('5 - удалить данные о пользователе из записной книжки')
        print('6 - копировать данные о пользователе в другой файл')
        answer = input('Выберите действие: ')
        if answer == '0': # в логике строчный вариант, а не цифра
            flag = False # Окончание работы программы
        elif answer == '1':
            save_data(file_name) # Вызов функции сохранения данных
        elif answer == '2':
            data = read_file(file_name) # Вызов функции чтения данных
            show_data(data) # Вызов функции вывода данных
        elif answer == '3':
            data = read_file(file_name) # Вызов функции чтения данных
            founded_data = search_data(data) # Вызов функции поиска данных
            show_data(founded_data) # Вызов функции выводы данных после поиска
        elif answer == '4': # Вызов функции изменения данных
            data = read_file(file_name) # Вызов функции чтения данных 
            idx_change = int(input('Введите строку, которую надо изменить: ')) - 1
            edit_data(data, idx_change, file_name) # Вызов функции изменения данных
        elif answer == '5': # Вызов функции удаления данных
            data = read_file(file_name) # Вызов функции чтения данных 
            idx_delete = int(input('Введите строку, которую надо удалить: ')) - 1
            delete_data(data, idx_delete, file_name) # Вызов функции изменения данных
        elif answer == '6': # Вызов функции удаления данных
            data = read_file(file_name) # Вызов функции чтения данных 
            idx_copy = int(input('Введите номер строки, для экспорта: ')) - 1
            copy_to_file(data, idx_copy, file_name_copy) # Вызов функции копирования (экспорта) данных в другой файл
        else:
            print('Такого дейсвтия нет!')
            return



if __name__ == '__main__': # Вызывается напрямую из главной программы
    main()