""" создаем файл JSON записываем в него и читаем из него """

import json

filename = 'text_files/username.json'
squares = [1, 4, 9, 16, 25, 36]

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Как ваше имя? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("Мы запомнили Ваше имя " + username + "!")
else:
    print("С возвращением, " + username + "!")