from lxml import html
import requests
from pprint import pprint
import csv

# Строка агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}

# 1.  Выберите веб-сайт с табличными данными, который вас интересует. (Например, news.mail.ru)
url = 'https://news.mail.ru/'

# 2.  Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт
# и получения HTML-содержимого страницы.
response = requests.get(url, headers = header)
if response.status_code == 200:
    print("Успешный запрос API!")
    dom = html.fromstring(response.text)

    # 3.  Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
    # Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
    links = dom.xpath("//div[@data-logger = 'news__MainTopNews']//li[@class = 'list__item']//@href | //div[@data-logger = 'news__MainTopNews']//td[not(@class = 'daynews__spring')]//@href")
    items_list = []
    for link in links:
        item_info = {}
        response = requests.get(link, headers=header)
        info = html.fromstring(response.text)
        article = info.xpath("//h1[@data-qa = 'Title'][1]/text()")
        source = info.xpath("//div[@aria-label = 'Навигация']//a[@href]/text()")
        item_info["article"] = article[0]
        item_info["source"] = source[0]
        item_info["teg"] = []
        for teg in range(len(source)):
            item_info["teg"].append(source[teg])
        item_info["link"] = link
        items_list.append(item_info)
        # print(article, source)
    pprint(items_list)

    # 4.  Сохраните извлеченные данные в CSV-файл с помощью модуля csv.
    # Открытие файла для записи
    with open('pz_4.csv', 'w', newline='') as file:
        fieldnames = ['article', 'source', 'teg' , "link"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Запись заголовков столбцов
        writer.writeheader()
        # Запись строк данных
        writer.writerows(items_list)

else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

print("Всего хорошего!")