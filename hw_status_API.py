import requests
import datetime
import time

from pprint import pprint

date_time = int(time.time())

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': 'OAuth y0_AgAAAAAITYfWAAYckQAAAADZo1R_5AgYraIdTU2JUVwB8L4gfitUmVs'}
payload = {'from_date': date_time}
print({'from_date': date_time})

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())