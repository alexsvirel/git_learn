""" Открывает файл и читает его """

with open('text_files/pi_digits.txt') as file_object:
    # # читает файл полностью
    # contents = file_object.read()
    # print(contents.rstrip())

    # # Читает файл по строкам
    # for line in file_object:
    #     print(line.rstrip())

    # Создает список строк
    lines = file_object.readlines()
    # for line in lines:
    #     print(line.rstrip())

    # Собираем все строки в одну строку
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))