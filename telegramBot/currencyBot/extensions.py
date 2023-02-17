# Модуль, реализующий проверки на неправильную работу бота и вывод сообщений об ошибках.


import requests
import json
from config import keys


# Класс вызова исключений
class ConversionException(Exception):
    pass


# Класс обработки исключений
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        # Проверка на запрос конвертации валюты саму в себя
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        # Проверка на некорректное наименование первой валюты в запросе
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}.')

        # Проверка на некорректное наименование второй валюты в запросе
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}.')

        # Проверка на некорректную запись суммы
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}.')

        # Обращение к API сайта, предоставляющего сведения о курсах валют
        r = requests.get(f'https://api.exchangerate.host/convert?from={quote_ticker}&to={base_ticker}&amount={amount}')
        total_base = json.loads(r.content)['result']

        return total_base
