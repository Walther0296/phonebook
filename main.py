# Создать телефонный справочник с возможностью импорта и экспорта данных в формте txt. Фамилия, имя, отчество, номер телефона.
# Программа должна выводить данные
# Программа должна сохранить данные в текстовом файле
# Пользователь может ввести одну из хараетристик: для поиска определенной записи (Например, имя или фамилия человека). 
# Использование функций. Ваша программа не должна быть линейной

#1. Создать сам файл: 
# - открываем файл на дозапись; 

# 2. Добавление контакта
# - запросить\получить у пользователя данные (проверка на корректность)
# - подготовить форматирование данных к записи
# - открыть файл для дозаписи
# - добавить новый контакт в файл
# - присвоить id контакту

# 3. Вывод данных на экран: 
# - открыть файл на чтение 
# - вывод на экран

# 4. Поиск контакта
# - запросить/получить у пользователя данные для поиска
# - открыть файл на чтение 
# - произвести поиск контактов
# - вывести на экран

# 5. Интерфейс
# - вывод на экран меню пользователя 
# - запросить\получить у пользователя вариант режима работы
# - вызов соответствующей функции
# - осуществление выхода из программы


# Домашнее задание: Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
# Формат сдачи: ссылка на свой репо.

# Алгоритм мероприятий по выполнению дз: 
# - Присвоить каждой записи порядковый номер; 
# - Прописать возможность переноса строчки в новый документ

#Очистить консоль
import os 

def print_data(): 
    with open ("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)

def input_name():
    return input ("Введите имя контакта: ").title() 

def input_surname():
    return input ("Введите фамилию контакта: ").title()  

def input_patronymic():
    return input ("Введите отчество контакта: ").title()  

def input_phone():
    return input ("Введите номер телефона контакта: ")  

def input_address():
    return input ("Введите адрес контакта: ").title()

def id_contact():
   id = 1 
   return id

def input_data():
    id = id_contact() 
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " " 
    return f"{f"{id}. "}{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}{address}\n" 

def add_contact(): 
    new_contact_str = input_data()
    with open ("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(new_contact_str)

def search_contact (): 
    print("Варианты поиска:\n"
            "1. По фамилии\n"
            "2. По имени\n"
            "3. По отчеству\n"
            "4. По телефону\n"
            "5. По адресу\n"            )
    command = input ("Выберите вариант поиска: ")


    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод. Повторите запрос.")
        command = input ("Выберите вариант поиска: ")

    i_search = int(command)-1
    search = input ("Введите данные для поиска: ").lower()
    print()

    with open ("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")


    check_cont = False 
    for contact_str in contacts_list: 
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if search in lst_contact[i_search]: 
            print(contact_str)
            print()
            check_cont = True
    
    if not check_cont: 
        print ("Такого контакта нет!")


def replace_contact(): 
    print_data()
    command1 = input ("Выберите номер контакта, который Вы хотите переместить в Любимые номера: ")



def interface(): 
    with open ("phonebook.txt", "a", encoding="utf-8"):
        pass 

    command = ""
    os.system("cls")
    while command != "5": 
        print("Меню пользователя:\n"
        "1. Вывод всех записей \n"
        "2. Добавить контакт \n"
        "3. Поиск контакта \n"
        "4. Переместить контакт в любимые номера\n"
        "5. Выход \n")
        command = input ("Выберите пункт меню: ")
        
        while (command not in ("1", "2", "3", "4", "5")):
            print("Некорректный ввод. Повторите запрос")
            command =  input ("Выберите пункт меню: ")
        
        match command:
            case "1": 
                print_data()
            case "2": 
                add_contact()
            case "3": 
                search_contact()
            case "4":
                replace_contact()
            case "5": 
                print("Завершение программы")

        print()    
            
if __name__ == "__main__": 
    interface()
