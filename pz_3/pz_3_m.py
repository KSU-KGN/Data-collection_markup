"""
Урок 3. Системы управления базами данных MongoDB и ClickHouse в Python
1. Загрузите данные которые вы получили на предыдущем уроке путем скрейпинга сайта
с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
2. Поэкспериментируйте с различными методами запросов
(например, цена в определённых пределах, наличие не менее скольки-то штук).
"""
import json
from pymongo import MongoClient
from pymongo.errors import *
from pprint import pprint

# Подключение к серверу MongoDB
client = MongoClient('localhost', 27017)

# Выбор базы данных и коллекций
db = client['shop']
info = db.info
books = db.books
duplicates = db.duplicates

info.delete_many({})
books.delete_many({})
duplicates.delete_many({})

# Чтение файла JSON
with open('books_data.json', 'r') as f:
    data = json.load(f)

# Запись в коллекции MongoDB
id_info = 0
id_book = 0
count_duplicates = 0
for book in data:
    # список книг с инфо в магазине
    id_info += 1
    book['_id'] = id_info
    info.insert_one(book)
    # справочник книг
    book_list = {}
    book_list['_id'] = book['name']
    book_list['url'] = book['url']
    try:
        books.insert_one(book_list)
    except DuplicateKeyError as e:
        # список дубликатов книг
        count_duplicates += 1
        book['_id'] = count_duplicates
        duplicates.insert_one(book)
        print(f'Обнаружен {count_duplicates}-й дубликат, книга "{book["name"]}"')

if count_duplicates:
    print(f"Всего дубликатов: {count_duplicates}")

"""
2. Поэкспериментируйте с различными методами запросов
(например, цена в определённых пределах, наличие не менее скольки-то штук).
"""
# Получение количества документов в коллекции с помощью функции count_documents()
print(f'Число всех книг в магазине: {info.count_documents({})}')
print(f'Число различных книг: {books.count_documents({})}')
print(f'Количество книг с одинаковым названием: {duplicates.count_documents({})}')

# Использование оператора $lt и $gte
query = {'price.0': {'$gte': 55.0, '$lt': 56.0}}
for book in info.find(query, {'url': 0}).sort('price.0', -1):
    print(book)
print(f"Кол-во книг по цене от 55£ до 56£: {info.count_documents(query)}")
print()
query = {'avail.0': {'$gte': 22}}
for book in info.find(query, {'url': 0}).sort('avail.0'):
    print(book)
print(f"Кол-во книг не менее 22 экземпляров: {info.count_documents(query)}")
print()

# Использование оператора $regex
query = {'_id': {'$regex': '.Light.'}}
for book in books.find(query).sort('_id'):
    print(book)
print(f"Кол-во книг, содержащих в названии 'Light': {books.count_documents(query)}")
