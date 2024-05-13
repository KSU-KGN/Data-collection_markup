import requests
import json
import os

# Безопасность
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), 'foursquare.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Ваши учетные данные API
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
api_key = os.getenv("api_key")

# Определение параметров для запроса API
url = "https://api.foursquare.com/v3/places/search"
city = input("Введите название города: ")
query = input("Введите интересующую вас категорию (например, кофейни, музеи, парки и т.д.): ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    #"query": "restaurant",
    "query": query,
    "fields": "name,location,rating"
}

headers = {
    "Accept": "application/json",
    "Authorization": api_key
}

# Отправка запроса API и получение ответа
response = requests.get(url, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    pr = 1
    for venue in venues:
        try:
            print("Название:", venue["name"])
            pr = 2
            print("Адрес:", venue["location"]["address"])
            pr = 3
            print("Рейтинг:",venue["rating"])
            print("------------------------")
        except Exception as e:
            if pr == 1:
                print("Название: нет данных")
            elif pr == 2:
                print("Адрес: нет данных")
            elif pr == 3:
                print("Рейтинг: нет данных")
            else:
                print(f"Обнаружено исключение: {type(e).__name__}, {e}")
            print("------------------------")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

print("Всего хорошего!")