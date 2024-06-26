*Данная секция временная, задания сдаю с опазданием, если вы проверите, то буду благодарна. Спасибо!* <br>
_В программах есть комментарии_ <br>
_Начало временной секции_ <br>

### Выполнение практического задания № 7
### Урок 7. Selenium в Python

_Задание выполнено полностью_ <br>
pz_7.py		- Python-скрипт <br>
letters.json	- образец извлеченных данных <br>
letters.pdf	- краткий отчет <br>

#### Задания:

1.  Выберите веб-сайт, который содержит информацию, представляющую интерес для извлечения данных. 
Это может быть новостной сайт, платформа для электронной коммерции или любой другой сайт, 
который позволяет осуществлять скрейпинг (убедитесь в соблюдении условий обслуживания сайта).
2.  Используя Selenium, напишите сценарий для автоматизации процесса перехода на нужную страницу сайта.
3.  Определите элементы HTML, содержащие информацию, которую вы хотите извлечь 
(например, заголовки статей, названия продуктов, цены и т.д.).
4.  Используйте BeautifulSoup для парсинга содержимого HTML и извлечения нужной информации из идентифицированных элементов.
5.  Обработайте любые ошибки или исключения, которые могут возникнуть в процессе скрейпинга.
6.  Протестируйте свой скрипт на различных сценариях, чтобы убедиться, что он точно извлекает нужные данные.
7.  Предоставьте ваш Python-скрипт вместе с кратким отчетом (не более 1 страницы), который включает следующее: 
URL сайта. Укажите URL сайта, который вы выбрали для анализа. 
Описание. Предоставьте краткое описание информации, которую вы хотели извлечь из сайта. 
Подход. Объясните подход, который вы использовали для навигации по сайту, 
определения соответствующих элементов и извлечения нужных данных. 
Трудности. Опишите все проблемы и препятствия, с которыми вы столкнулись в ходе реализации проекта, 
и как вы их преодолели. 
Результаты. Включите образец извлеченных данных в выбранном вами структурированном формате 
(например, CSV или JSON). 

Примечание: Обязательно соблюдайте условия обслуживания сайта и избегайте чрезмерного скрейпинга, 
который может нарушить нормальную работу сайта.

_В программах есть комментарии_ <br>
_Конец временной секции_ <br>
*Данная секция временная, задания сдаю с опазданием, если вы проверите, то буду благодарна. Спасибо!*

### Выполнение практического задания № 8
### Урок 8. Работа с данными

pz_8.ipynb		          - Python-ноутбук (в процессе разработки) <br>
cleaned_house_prices.csv- очищенный и преобразованный набор данных (в процессе) <br>

#### Задания:

1.  Скачайте датасет House Prices Kaggle со страницы конкурса 
(https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
и сохраните его в том же каталоге, что и ваш скрипт или блокнот Python.
2.  Загрузите датасет в pandas DataFrame под названием df.
3.  Выполните предварительную обработку данных, выполнив следующие шаги:  
a.  Определите и обработайте отсутствующие значения в датасете.  <br>
Определите, в каких столбцах есть отсутствующие значения, и решите, как их обработать  <br>
(например, заполнить средним, медианой или модой, или отбросить столбцы/строки с существенными отсутствующими значениями).  <br>
b.  Проверьте и обработайте любые дублирующиеся строки в датасете.  <br>
c.  Проанализируйте типы данных в каждом столбце и при необходимости преобразуйте их (например, из объектных в числовые типы). <br>
4.  Проведите разведочный анализ данных (EDA), ответив на следующие вопросы:  <br>
a.  Каково распределение целевой переменной 'SalePrice'? Есть ли какие-либо выбросы?  <br>
b.  Исследуйте взаимосвязи между целевой переменной и другими характеристиками. Есть ли сильные корреляции?  <br>
c.  Исследуйте распределение и взаимосвязи других важных характеристик, таких как 'OverallQual', 'GrLivArea', 'GarageCars' и т.д.  <br>
d.  Визуализируйте данные, используя соответствующие графики (например, гистограммы, диаграммы рассеяния, квадратные диаграммы), чтобы получить представление о датасете. <br>
5.  Выполните проектирование признаков путем реализации следующих преобразований:  <br>
a.  Работайте с категориальными переменными, применяя one-hot encoding или label encoding, в зависимости от характера переменной.  <br>
b.  При необходимости создайте новые характеристики, такие как общая площадь или возраст объекта недвижимости, путем объединения существующих характеристик. <br>
6.  Сохраните очищенный и преобразованный набор данных в новый CSV-файл под названием 'cleaned_house_prices.csv'.
