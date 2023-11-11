# Домашнее задание: Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
# Также выполнено задание из урока. Добавление функции удаления строк. 

import os
file_book = "phonebook.txt"

def print_data(): 
    with open (file_book, "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    if phonebook_str == "": 
        print("Телефонный справочник пуст! Добавьте запись!")

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
    file = open(file_book, encoding="utf-8")
    for line in file:
        id +=1
    return id

def input_data():
    id = id_contact() 
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " " 
    return f"{f"{id}. "}{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}{my_sep}{address}\n" 

def add_contact(): 
    new_contact_str = input_data()
    with open (file_book, "a", encoding="utf-8") as file:
        file.write(new_contact_str)
    print ("\n Сохранено!")
    

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

    with open (file_book, "r", encoding="utf-8") as file:
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
    num = input ("Выберите номер контакта, который Вы хотите переместить в Любимые номера: ")
    print()

    with open(file_book) as source, open('LikePhones.txt', 'a') as destination:
        check_cont = False 
        for line in source:
            if line.startswith(num):
                destination.write(line) 
                check_cont = True
                print ("Контакт добавлен в файл Любимые номера.") 
        
        if not check_cont: 
            print("Такого контакта нет!")            

def del_contact():
        with open (file_book, "r") as file:
            phonebook_str = file.read()
            print(phonebook_str)
            if phonebook_str == "":
                print("Телефонный справочник пуст! Добавьте запись!")
                return
            else:  
                num_del = input ("Выберите номер контакта, который Вы хотите удалить: ")
        
        with open(file_book, "r") as f:
            lines = f.readlines()
        with open(file_book, "w") as f:
            check_cont = False 
            for line in lines:
                if line.startswith(num_del):
                    f.write("")
                    check_cont = True
                    print("Контакт удален")
                else: 
                    f.write(line)
            if not check_cont: 
                print("Такого контакта нет!")     





def interface(): 
    with open (file_book, "a", encoding="utf-8"):
        pass 

    command = ""
    os.system("cls")
    while command != "6": 
        print("Меню пользователя:\n"
        "1. Вывод всех записей \n"
        "2. Добавить контакт \n"
        "3. Поиск контакта \n"
        "4. Переместить контакт в любимые номера\n"
        "5. Удалить контакт\n"
        "6. Выход \n")
        command = input ("Выберите пункт меню: ")
        
        while (command not in ("1", "2", "3", "4", "5", "6")):
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
                del_contact()    
            case "6": 
                print("Завершение программы")

        print()    
            
if __name__ == "__main__": 
    interface()
