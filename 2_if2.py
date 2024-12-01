"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main(one, two):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not type(one) == str and not type(two) == str:
        return 0
    elif one == two:
        return 1
    elif len(one) > len(two) and not two == 'learn':
        return 2
    elif not one == two and two == 'learn':
        return 3

if __name__ == "__main__":
    print(main(1, 2))
    print(main('same', 'same'))
    print(main('longer', 'short'))
    print(main('python', 'learn'))
