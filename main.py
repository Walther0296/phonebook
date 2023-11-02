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

# 3. Вывод данных на экран: 
# - открыть фалй на чтение 
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

#Очистить консоль
import os 

def print_data(): 
    with open ("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()

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

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " " 
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n" 

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





def interface(): 
    with open ("phonebook.txt", "a", encoding="utf-8"):
        pass 

    command = ""
    os.system("cls")
    while command != "4": 
        print("Меню пользователя:\n"
        "1. Ввод данных на экран \n"
        "2. Добавить контакт \n"
        "3. Поиск контакта \n"
        "4. Выход \n")
        command = input ("Выберите пункт меню: ")
        
        while (command not in ("1", "2", "3", "4")):
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
                print("Завершение программы")

        print()    
            
if __name__ == "__main__": 
    interface()
