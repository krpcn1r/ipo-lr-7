# Вариант 2, Зайцев
print("start code …")
book = []
for i in range(1,6):
    book.append(dict(title = input("Введите название: "), author = input("Введите автора: "), year = input("Введите год: "))) # Создаю список словарей книг

for i in range(len(book)):
    print("-" * 20, f"Книга{" " + str(1 + i)}", "-" * 20) 
    print(f"Название: {book[i]["title"]}, Автор: {book[i]["author"]}") # Вывод данных
    print("-" * 20, f"{book[i]["year"]}", "-" * 20)
print("end code …")
