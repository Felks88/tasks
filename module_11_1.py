import requests
import matplotlib.pyplot as plt
from collections import Counter

# Построить круговцю диаграмму успеваемости класса по годовым оценкам:

final_grades = {'Вася П': 5, 'Петя К': 3, 'Коля С': 4, 'Игорь З': 4, 'Костя Г': 5, 'Маша П': 4, 'Дима Я': 5,
                'Вдим Л': 3, 'Юля С': 5}
values = final_grades.values()
chart_values = dict(Counter(values))
print(chart_values)

grade_ = chart_values.values()
dial_ = chart_values.keys()

plt.pie(grade_, labels=dial_, autopct='%1.1f%%')
plt.title("Успеваемость класса в процентах")
plt.show()

# Проверка соединения с сайтом, получение данных:

# url = 'https://mail.ru/'
# res = requests.get(url)
# if res.status_code == 200:
#     print(res.status_code)  # код состояния запроса. 200 - запрос успешен, ответ получен
#     print(res.text)  # получение содержимого страницы в строковом виде
#     print(res.headers)  # получение содержимого заголовков
# else:
#     print('Ошибка запроса')
