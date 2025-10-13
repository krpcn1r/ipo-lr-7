# Вариант 2
import json
choice = 0
with open("dump.json", "r+", encoding = "UTF-8") as file:
    data = json.load(file)
while True:
    print(">> 1   Вывод записей")
    print(">> 2   Вывод записи по полю")
    print(">> 3   Добавить запись")
    print(">> 4   Удалить запись по полю ")
    print(">> 5   Выход их программы")
    print(" ")
    choice = int(input("Выберите пункт: "))
    if(choice == 0 or choice <= 0 or choice > 5):
        print("Введено неверное число")
        print(" ")
    else:
        match choice:
            case 1:
                print("Выбран пункт 1")
            case 2:
                print("Выбран пункт 2")
            case 3:
                print("Выбран пункт 3")
            case 4:
                print("Выбран пункт 4")
            case 5:
                break


