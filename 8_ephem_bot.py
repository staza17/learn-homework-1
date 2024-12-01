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
from datetime import datetime, date, time
import settings
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


zodiacs = {'Aries': 'Овен', 'Leo': 'Лев', 'Sagittarius': 'Стрелец',
           'Taurus': 'Телец', 'Virgo': 'Дева', 'Capricorn': 'Козерог',
            'Gemini': 'Близнецы', 'Libra,': 'Весы', 'Aquarius': 'Водолей',
           'Cancer': 'Рак', 'Scorpio': 'Скорпион', 'Pisces': 'Рыбы', 'Ophiuchus': 'Змееносец'}

planets = {
'mars': ephem.Mars(datetime.now().strftime('%Y/%m/%d')),
'mercury': ephem.Mercury(datetime.now().strftime('%Y/%m/%d')),
'venus': ephem.Venus(datetime.now().strftime('%Y/%m/%d')),
'jupiter': ephem.Jupiter(datetime.now().strftime('%Y/%m/%d')),
'saturn': ephem.Saturn(datetime.now().strftime('%Y/%m/%d')),
'uranus': ephem.Uranus(datetime.now().strftime('%Y/%m/%d')),
'neptune': ephem.Neptune(datetime.now().strftime('%Y/%m/%d'))
}

# Внесла (datetime.now().strftime('%Y/%m/%d')) в словарь, потому что иначе planets.get(user_text)
# возвращал <class 'ephem.Neptune'>, и ephem.constellation(planet) не работал

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет!')

def planet_check(update, context):
    print('Вызван /planet')
    if len(update.message.text.lower().split()) < 2:
        update.message.reply_text('Некорректный запрос')
    user_text = update.message.text.lower().split()[1]
    planet_func = planets.get(user_text)
    print(planet_func)
    if planet_func is None:
        update.message.reply_text('Некорректный запрос')
    else:
        planet = planet_func
        constellation = ephem.constellation(planet)
        update.message.reply_text(zodiacs[constellation[1]])


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_check))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
