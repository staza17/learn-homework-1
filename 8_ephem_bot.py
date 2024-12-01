"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from ephem import constellation
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


zodiacs = {'Aries': 'Овен', 'Leo': 'Лев', 'Sagittarius': 'Стрелец',
           'Taurus': 'Телец', 'Virgo': 'Дева', 'Capricorn': 'Козерог',
            'Gemini': 'Близнецы', 'Libra,': 'Весы', 'Aquarius': 'Водолей',
           'Cancer': 'Рак', 'Scorpio': 'Скорпион', 'Pisces': 'Рыбы', 'Ophiuchus': 'Змееносец'}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет!')

def planet_check(update, context):
    print('Вызван /planet')
    if len(update.message.text.lower().split()) < 2:
        update.message.reply_text('Некорректный запрос')
    user_text = update.message.text.lower().split()[1]
    if user_text == 'mars':
        planet = ephem.Mars('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    elif user_text == 'mercury':
        planet = ephem.Mercury('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    elif user_text == 'venus':
        planet = ephem.Venus('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    elif user_text == 'jupiter':
        planet = ephem.Jupiter('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    elif user_text == 'saturn':
        planet = ephem.Saturn('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    elif user_text == 'uranus':
        planet = ephem.Uranus('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    elif user_text == 'neptune':
        planet = ephem.Neptune('2024/11/29')
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(zodiacs[constellation[1]])
    else:
        update.message.reply_text('Некорректный запрос')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_check))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
