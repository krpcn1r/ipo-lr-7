import json
with open("C:/Users/ZaytsSte_89/Desktop/ИПО/lr5/dump.json", "r", encoding = "UTF-8") as file:
    data = json.load(file) # считываем данные из файла

num = input("Введите номер квалификации: ") # Зарпашиваем номер квалификации
flag = False
for item in data: 
    fields = item.get("fields", {}) # Получаю все поля
    code = fields.get("code", "") # Получаю номер из поля
    if code == num: # Проверяю есть ли такой номер
        print("-" * 20 + "Найдено" + "-" * 20)
        print(str(num) + " >> " + fields.get("title", ""))
        flag = True
        
if flag == False:  # Если нет такого номера
    print("-" * 20 + "Не найдено" + "-" * 20)
