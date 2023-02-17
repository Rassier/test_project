# Основной модуль программы, реализующий функционал


# Импортируем модуль telebot, а также конфигурационные данные и дополнительный функционал из других модулей
import telebot
from config import keys, TOKEN
from extensions import ConversionException, CryptoConverter


# Создаем бота
bot = telebot.TeleBot(TOKEN)


# Функция вывода справки для пользователя
@bot.message_handler(commands=['start', 'help'])
def userhelp(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду для бота в следующем формате: \n<название валюты> ' \
            '<в какую валюту перевести><количество переводимой валюты> \n' \
            'Пример: доллар рубль 10.\n' \
            '<Команда для вывода списка всех доступных валют: /values'
    bot.reply_to(message, text)


# Обработчик сообщений вывода списка доступных к использованию валют
@bot.message_handler(commands=['values'])
def currencies(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


# Обработчик сообщений для конвертации валют
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        # Проверка корректности количества параметров, введенных пользователем.
        if len(values) != 3:
            raise ConversionException('Некорректный запрос.\n Для вывода справки введите команду: /help.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    # Вывод сообщения в чат, в случае некорректного ввода со стороны пользователя.
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    # Вывод сообщения в чат, в случае проблем, не связанных с действиями пользователя
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    # Вывод ответа на запрос
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


# Запускаем бота
bot.polling()
