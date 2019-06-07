""" Запись в файл """

filename = 'text_files/programming.txt'
""" Создаем или перезаписываем файл """
with open(filename, 'w', encoding='utf8') as file_object:
    file_object.write("Я люблю программировать.\n")   # если не ставить знак конца строки всё записывается подряд
    file_object.write("I love programming.\n")

""" Добавляем информацию в конец файла """
with open(filename, 'a', encoding='utf8') as file_object:
    file_object.write("Я люблю добавлять.\n")
    file_object.write("I love adding.\n")