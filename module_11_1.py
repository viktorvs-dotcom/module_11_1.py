# Библиотека requests
# Библиотека requests позволяет легко делать HTTP-запросы и обрабатывать ответы.
# Это полезно для получения данных с веб-сайтов или API.

import requests

# Запрос данных с сайта
response = requests.get('https://api.github.com')
# Вывод ответа в консоль
print(response.json())  # Печатает JSON-ответ от GitHub API
print("\n код requests завершён \n")

'''
 Возможности библиотеки requests:

    -Отправка HTTP-запросов (GET, POST, PUT, DELETE и т.д.)
    -Управление заголовками запросов
    -Обработка параметров и данных формы
    -Работа с ответами, включая статус-коды и содержимое
'''


# Библиотека pandas
# Библиотека pandas предназначена для работы с данными и предоставляет мощные структуры данных для анализа.
# Она особенно удобна для обработки таблиц и временных рядов.

import pandas as pd

# Создание DataFrame из словаря
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Простая аналитика
print("Средний возраст:", df['Age'].mean())  # Средний возраст
print("Данные по городам:\n", df.groupby('City').size())  # Количество людей по городам

# Сохранение DataFrame в CSV файл
df.to_csv('people.csv', index=False)
print("\n код pandas завершён \n")

'''
 Возможности библиотеки pandas:

    -Чтение и запись данных из/в различные форматы (CSV, Excel, SQL и т.д.)
    -Манипуляция данными (фильтрация, группировка, агрегация)
    -Работа с временными рядами и индексы
    -Обработка пропущенных данных и работа с дублированными записями
'''


# Библиотека matplotlib
# Библиотека matplotlib используется для создания графиков и визуализации данных.
# Она позволяет строить различные виды графиков и настроить их внешний вид.

import matplotlib.pyplot as plt

# Данные для графика
x = [1, 4, 7, 10, 15]
y = [2, 5, 9, 13, 16]

# Создание графика
plt.plot(x, y, marker='o')

# Настройка графика
plt.title('Пример графика')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Показ графика
plt.show()
print("\n код matplotlib завершён \n")

'''
 Возможности библиотеки matplotlib:

    -Построение различных типов графиков (линейные, столбчатые, круговые и т.д.)
    -Настройка визуальных элементов графика (цвета, метки, заголовки)
    -Создание сложных композиций из нескольких графиков
    -Сохранение графиков в различные форматы изображений
'''


"""
Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.

Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. 
К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и 
как вы расширили возможности Python с её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
"""
